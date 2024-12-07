import logging
import asyncio
import time

from NetUtils import ClientStatus, color
from worlds.AutoSNIClient import SNIClient

logger = logging.getLogger("Client")
snes_logger = logging.getLogger("SNES")

# FXPAK Pro protocol memory mapping used by SNI
ROM_START = 0x000000
WRAM_START = 0xF50000
WRAM_SIZE = 0x20000
SRAM_START = 0xE00000

STARTING_ID = 0xBF0000

DKC2_SETTINGS = ROM_START + 0x3DFF80

DKC2_MISC_FLAGS = WRAM_START + 0x08D2
DKC2_GAME_FLAGS = WRAM_START + 0x59B2

DKC2_EFFECT_BUFFER = WRAM_START + 0x0619
DKC2_SOUND_BUFFER = WRAM_START + 0x0622
DKC2_SPC_NEXT_INDEX = WRAM_START + 0x0634
DKC2_SPC_INDEX = WRAM_START + 0x0632
DKC2_SPC_CHANNEL_BUSY = WRAM_START + 0x0621

DKC2_SRAM = SRAM_START + 0x800
DKC2_RECV_INDEX = DKC2_SRAM + 0x020
DKC2_INIT_FLAG = DKC2_SRAM + 0x022

DKC2_GAME_TIME = WRAM_START + 0x00D5
DKC2_IN_LEVEL = WRAM_START + 0x01FF
DKC2_CURRENT_LEVEL = WRAM_START + 0x08A8    # 0xD3?
DKC2_CURRENT_MODE = WRAM_START + 0x00D0

DKC2_CRANKY_FLAGS = WRAM_START + 0x08D2
DKC2_WRINKLY_FLAGS = WRAM_START + 0x08E0
DKC2_FUNKY_FLAGS = WRAM_START + 0x08E7
DKC2_SWANKY_FLAGS = WRAM_START + 0x08F0
DKC2_KLUBBA_TOLLS = WRAM_START + 0x08FA
DKC2_KONG_LETTERS = WRAM_START + 0x0902

DKC2_BONUS_FLAGS = WRAM_START + 0x59B2
DKC2_DK_COIN_FLAGS = WRAM_START + 0x59D2
DKC2_STAGE_FLAGS = WRAM_START + 0x59F2

DKC2_ROMHASH_START = 0xFFC0
ROMHASH_SIZE = 0x15

class DKC2SNIClient(SNIClient):
    game = "Donkey Kong Country 2"
    patch_suffix = ".apdkc2"

    def __init__(self):
        super().__init__()
        self.game_state = False


    async def deathlink_kill_player(self, ctx):
        from SNIClient import DeathState, snes_buffered_write, snes_flush_writes, snes_read

        await snes_flush_writes(ctx)

        ctx.death_state = DeathState.dead
        ctx.last_death_link = time.time()


    async def validate_rom(self, ctx):
        from SNIClient import snes_read

        rom_name = await snes_read(ctx, DKC2_ROMHASH_START, ROMHASH_SIZE)
        if rom_name is None or rom_name == bytes([0] * ROMHASH_SIZE) or rom_name[:4] != b"DKC2":
            return False
        
        ctx.game = self.game
        ctx.items_handling = 0b111
        ctx.receive_option = 0
        ctx.send_option = 0
        ctx.allow_collect = True

        #death_link = await snes_read(ctx, MMX_DEATH_LINK_ACTIVE, 1)
        #if death_link[0]:
        #    await ctx.update_death_link(bool(death_link[0] & 0b1))

        ctx.rom = rom_name

        return True


    async def game_watcher(self, ctx):
        from SNIClient import snes_buffered_write, snes_flush_writes, snes_read

        setting_data = await snes_read(ctx, DKC2_SETTINGS, 0x40)
        general_data = await snes_read(ctx, WRAM_START + 0x00D0, 0x0F)
        game_flags = await snes_read(ctx, DKC2_GAME_FLAGS, 0x60)
        misc_flags = await snes_read(ctx, DKC2_MISC_FLAGS, 0x80)

        if general_data is None or game_flags is None or misc_flags is None or setting_data is None:
            return

        loaded_save = int.from_bytes(general_data[0x05:0x07], "little")
        if loaded_save == 0:
            return

        validation = int.from_bytes(await snes_read(ctx, DKC2_INIT_FLAG, 0x2), "little")
        if validation != 0xDEAD:
            snes_logger.info(f'ROM not properly validated.')
            self.game_state = False
            return
        
        from .Levels import location_id_to_level_id
        from worlds import AutoWorldRegister

        new_checks = []
        current_level = int.from_bytes(await snes_read(ctx, DKC2_CURRENT_LEVEL, 0x01))
        kong_flags = misc_flags[0x30]
        stage_flags = game_flags[0x40:0x60]
        bonus_flags = list(game_flags[0x00:0x20])
        dk_coin_flags = list(game_flags[0x20:0x40])
        for loc_name, data in location_id_to_level_id.items():
            loc_id = AutoWorldRegister.world_types[ctx.game].location_name_to_id[loc_name]
            if loc_id not in ctx.locations_checked:
                loc_type = data[0]
                level_num = data[1]
                level_offset = (level_num >> 3) & 0x1E
                level_bit = 1 << (level_num & 0x0F)

                if loc_type == 0x00:
                    # Level clear
                    level_data = int.from_bytes(stage_flags[level_offset:level_offset+2], "little")
                    if level_data & level_bit:
                        new_checks.append(loc_id)
                elif loc_type == 0x01:
                    # KONG
                    if level_num == current_level and kong_flags & 0x0F == 0x0F:
                        new_checks.append(loc_id)
                elif loc_type == 0x02:
                    # DK Coin
                    level_data = int.from_bytes(dk_coin_flags[level_offset:level_offset+2], "little")
                    if level_data & level_bit:
                        new_checks.append(loc_id)
                elif loc_type == 0x03:
                    # Bonus
                    level_data = int.from_bytes(bonus_flags[level_offset:level_offset+2], "little")
                    if level_data & level_bit:
                        new_checks.append(loc_id)

        # Check goals
        goal_check = 0
        selected_goal = setting_data[0x01]

        level_num = 0x61
        level_offset = (level_num >> 3) & 0x1E
        level_bit = 1 << (level_num & 0x0F)
        level_data = int.from_bytes(bonus_flags[level_offset:level_offset+2], "little")
        if level_data & level_bit:
            goal_check |= 1
        
        level_num = 0x6B
        level_offset = (level_num >> 3) & 0x1E
        level_bit = 1 << (level_num & 0x0F)
        level_data = int.from_bytes(dk_coin_flags[level_offset:level_offset+2], "little")
        if level_data & level_bit:
            goal_check |= 2

        if goal_check & selected_goal == selected_goal:
            if not ctx.finished_game:
                await ctx.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
                ctx.finished_game = True
                return

        # Receive items
        rom = await snes_read(ctx, DKC2_ROMHASH_START, ROMHASH_SIZE)
        if rom != ctx.rom:
            ctx.rom = None
            snes_logger.info(f'Exit ROM.')
            return
        
        for new_check_id in new_checks:
            ctx.locations_checked.add(new_check_id)
            location = ctx.location_names.lookup_in_game(new_check_id)
            snes_logger.info(
                f'New Check: {location} ({len(ctx.locations_checked)}/{len(ctx.missing_locations) + len(ctx.checked_locations)})')
            await ctx.send_msgs([{"cmd": 'LocationChecks', "locations": [new_check_id]}])

        recv_count = await snes_read(ctx, DKC2_RECV_INDEX, 2)
        if recv_count is None:
            # Add a small failsafe in case we get a None. Other SNI games do this...
            return

        from .Rom import unlock_data, currency_data, trap_data
        recv_index = int.from_bytes(recv_count, "little")

        if recv_index < len(ctx.items_received):
            item = ctx.items_received[recv_index]
            recv_index += 1
            sending_game = ctx.slot_info[item.player].game
            logging.info('Received %s from %s (%s) (%d/%d in list)' % (
                color(ctx.item_names.lookup_in_game(item.item), 'red', 'bold'),
                color(ctx.player_names[item.player], 'yellow'),
                ctx.location_names.lookup_in_slot(item.location, item.player), recv_index, len(ctx.items_received)))
            
            sfx = 0
            # Give kongs
            if item.item in {STARTING_ID + 0x0010, STARTING_ID + 0x0011}:
                offset = unlock_data[item.item][0]
                sfx = unlock_data[item.item][1]
                count = await snes_read(ctx, DKC2_SRAM + offset, 0x02)
                if count is None:
                    recv_index -= 1
                    return
                count = int.from_bytes(count, "little")
                if item.item == STARTING_ID + 0x0010:
                    count |= 0x0001
                else:
                    count |= 0x0002
                count &= 0x00FF
                snes_buffered_write(ctx, DKC2_SRAM + offset, bytes([count]))

            # Give items
            elif item.item in unlock_data:
                offset = unlock_data[item.item][0]
                sfx = unlock_data[item.item][1]
                snes_buffered_write(ctx, DKC2_SRAM + offset, bytearray([0x01]))
            
            # Give currency-like items
            elif item.item in currency_data:
                offset = currency_data[item.item][0]
                if offset & 0x8000 == 0x8000:
                    addr = DKC2_SRAM + (offset & 0x7FFF)
                else:
                    addr = WRAM_START + offset
                sfx = currency_data[item.item][1]
                currency = await snes_read(ctx, addr, 0x02)
                if currency is None:
                    recv_index -= 1
                    return
                currency = int.from_bytes(currency, "little") + 1
                currency &= 0x00FF
                snes_buffered_write(ctx, addr, bytes([currency]))

            # Give traps 
            elif item.item in trap_data:
                offset = trap_data[item.item][0]
                sfx = trap_data[item.item][1]
                traps = await snes_read(ctx, DKC2_SRAM + offset, 0x02)
                if traps is None:
                    recv_index -= 1
                    return
                traps = int.from_bytes(traps, "little") + 1
                traps &= 0x00FF
                snes_buffered_write(ctx, DKC2_SRAM + offset, bytes([traps]))

            if sfx:
                snes_buffered_write(ctx, DKC2_SOUND_BUFFER, bytearray([sfx, 0x05]))
                snes_buffered_write(ctx, DKC2_EFFECT_BUFFER + 0x05, bytearray([sfx]))
                snes_buffered_write(ctx, DKC2_SPC_INDEX, bytearray([0x00]))
                snes_buffered_write(ctx, DKC2_SPC_NEXT_INDEX, bytearray([0x00]))

            snes_buffered_write(ctx, DKC2_RECV_INDEX, bytes([recv_index]))

            await snes_flush_writes(ctx)
                
        # Handle collected locations
        new_level_clear = False
        new_dk_coin = False
        new_bonus = False
        stage_flags = list(game_flags[0x40:0x60])
        bonus_flags = list(game_flags[0x00:0x20])
        dk_coin_flags = list(game_flags[0x20:0x40])
        i = 0
        for loc_id in ctx.checked_locations:
            if loc_id not in ctx.locations_checked:
                ctx.locations_checked.add(loc_id)
                loc_name = ctx.location_names.lookup_in_game(loc_id)

                if loc_name not in location_id_to_level_id:
                    continue

                logging.info(f"Recovered checks ({i:03}): {loc_name}")
                i += 1

                data = location_id_to_level_id[loc_name]

                loc_type = data[0]
                level_num = data[1]
                level_offset = (level_num >> 3) & 0x1E
                level_bit = 1 << (level_num & 0x0F)

                if loc_type == 0x00:
                    # Level clear
                    level_data = int.from_bytes(stage_flags[level_offset:level_offset+2], "little")
                    level_data |= level_bit
                    stage_flags[level_offset:level_offset+2] = level_data.to_bytes(2, "little")
                    new_level_clear = True
                elif loc_type == 0x02:
                    # DK Coin
                    level_data = int.from_bytes(dk_coin_flags[level_offset:level_offset+2], "little")
                    level_data |= level_bit
                    dk_coin_flags[level_offset:level_offset+2] = level_data.to_bytes(2, "little")
                    new_dk_coin = True
                elif loc_type == 0x03:
                    # Bonus
                    level_data = int.from_bytes(bonus_flags[level_offset:level_offset+2], "little")
                    level_data |= level_bit
                    bonus_flags[level_offset:level_offset+2] = level_data.to_bytes(2, "little")
                    new_bonus = True
        
        if new_level_clear:
            snes_buffered_write(ctx, DKC2_STAGE_FLAGS, bytearray(stage_flags))
        if new_dk_coin:
            snes_buffered_write(ctx, DKC2_DK_COIN_FLAGS, bytearray(dk_coin_flags))
        if new_bonus:
            snes_buffered_write(ctx, DKC2_BONUS_FLAGS, bytearray(bonus_flags))
