import dataclasses
import os
import typing
import math
import settings
import hashlib
import threading
import pkgutil

from BaseClasses import Item, MultiWorld, Tutorial, ItemClassification
from Options import PerGameCommonOptions
from worlds.AutoWorld import World, WebWorld
from .Items import DKC2Item, ItemData, item_table, junk_table, item_groups
from .Locations import DKC2Location, setup_locations, all_locations, location_groups
from .Regions import create_regions, connect_regions
from .Names import ItemName, LocationName, EventName
from .Options import DKC2Options, Logic, StartingKong
from .Client import DKC2SNIClient
from .Levels import generate_level_list, level_map, location_id_to_level_id
from .Rules import DKC2StrictRules, DKC2LooseRules, DKC2ExpertRules
from .Rom import patch_rom, DKC2ProcedurePatch, HASH_US, HASH_US_REV_1

class DKC2Settings(settings.Group):
    class RomFile(settings.SNESRomPath):
        """File name of the Mega Man X US ROM"""
        description = "Donkey Kong Country 2 (USA) ROM File"
        copy_to = "Donkey Kong Country 2 - Diddy's Kong Quest (USA).sfc"
        md5s = [HASH_US, HASH_US_REV_1]

    rom_file: RomFile = RomFile(RomFile.copy_to)


class DKC2Web(WebWorld):
    theme = "grass"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to playing Donkey Kong Country 2 - Diddy's Kong Quest with Archipelago",
        "English",
        "setup_en.md",
        "setup/en",
        ["lx5"]
    )

    tutorials = [setup_en]


class DKC2World(World):
    """
    Donkey Kong Country 2 WIP
    """
    game = "Donkey Kong Country 2"
    web = DKC2Web()

    settings: typing.ClassVar[DKC2Settings]
    
    options_dataclass = DKC2Options
    options: DKC2Options
    
    required_client_version = (0, 5, 0)

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = all_locations
    item_name_groups = item_groups
    location_name_groups = location_groups
    hint_blacklist = {
    }

    def __init__(self, multiworld: MultiWorld, player: int):
        self.rom_name_available_event = threading.Event()
        super().__init__(multiworld, player)

    def create_regions(self) -> None:
        location_table = setup_locations(self)
        create_regions(self.multiworld, self.player, self, location_table)

        itempool: typing.List[DKC2Item] = []
        
        connect_regions(self)
        
        total_required_locations = 191

        # Set starting kong
        if self.options.starting_kong == StartingKong.option_diddy:
            self.multiworld.push_precollected(self.create_item(ItemName.diddy))
            itempool += [self.create_item(ItemName.dixie)]
        elif self.options.starting_kong == StartingKong.option_dixie:
            self.multiworld.push_precollected(self.create_item(ItemName.dixie))
            itempool += [self.create_item(ItemName.diddy)]
        elif self.options.starting_kong == StartingKong.option_both:
            self.multiworld.push_precollected(self.create_item(ItemName.diddy))
            self.multiworld.push_precollected(self.create_item(ItemName.dixie))

        self.multiworld.push_precollected(self.create_item(ItemName.gangplank_galleon))

        # Add progression items
        itempool += [self.create_item(ItemName.crocodile_cauldron)]
        itempool += [self.create_item(ItemName.krem_quay)]
        itempool += [self.create_item(ItemName.krazy_kremland)]
        itempool += [self.create_item(ItemName.gloomy_gulch)]
        itempool += [self.create_item(ItemName.krools_keep)]
        itempool += [self.create_item(ItemName.the_flying_krock)]
        itempool += [self.create_item(ItemName.lost_world_cauldron)]
        itempool += [self.create_item(ItemName.lost_world_quay)]
        itempool += [self.create_item(ItemName.lost_world_kremland)]
        itempool += [self.create_item(ItemName.lost_world_gulch)]
        itempool += [self.create_item(ItemName.lost_world_keep)]

        for item in item_groups["Abilities"]:
            if item in self.options.shuffle_abilities.value:
                itempool += [self.create_item(item)]
            else:
                self.multiworld.push_precollected(self.create_item(item))

        for item in item_groups["Animals"]:
            if item in self.options.shuffle_animals.value:
                itempool += [self.create_item(item)]
            else:
                self.multiworld.push_precollected(self.create_item(item))
                
        for item in item_groups["Barrels"]:
            if item in self.options.shuffle_barrels.value:
                itempool += [self.create_item(item)]
            else:
                self.multiworld.push_precollected(self.create_item(item))

        for _ in range(self.options.lost_world_rocks.value):
            itempool.append(self.create_item(ItemName.lost_world_rock))

        # Add trap items into the pool
        junk_count = total_required_locations - len(itempool)
        trap_weights = []
        trap_weights += ([ItemName.freeze_trap] * self.options.freeze_trap_weight.value)
        trap_weights += ([ItemName.reverse_trap] * self.options.reverse_trap_weight.value)
        trap_count = 0 if (len(trap_weights) == 0) else math.ceil(junk_count * (self.options.trap_fill_percentage.value / 100.0))
        junk_count -= trap_count

        trap_pool = []
        for _ in range(trap_count):
            trap_item = self.random.choice(trap_weights)
            trap_pool.append(self.create_item(trap_item))
        
        itempool += trap_pool

        # Add junk items into the pool
        junk_weights = []
        junk_weights += ([ItemName.red_balloon] * 40)
        junk_weights += ([ItemName.banana_coin] * 20)

        junk_pool = []
        for _ in range(junk_count):
            junk_item = self.random.choice(junk_weights)
            junk_pool.append(self.create_item(junk_item))

        itempool += junk_pool

        # Finish
        self.multiworld.itempool += itempool


    def create_item(self, name: str, force_classification=False) -> DKC2Item:
        data = item_table[name]

        if force_classification:
            classification = force_classification
        elif data.progression:
            classification = ItemClassification.progression
        elif data.trap:
            classification = ItemClassification.trap
        else:
            classification = ItemClassification.filler
        
        created_item = DKC2Item(name, classification, data.code, self.player)

        return created_item


    def interpret_slot_data(self, slot_data):
        return slot_data
    

    def set_rules(self):
        logic = self.options.logic
        if logic == Logic.option_strict:
            DKC2StrictRules(self).set_dkc2_rules()
        elif logic == Logic.option_loose:
            DKC2LooseRules(self).set_dkc2_rules()
        elif logic == Logic.option_expert:
            DKC2ExpertRules(self).set_dkc2_rules()
        else:
            raise ValueError(f"Somehow you have a logic option that's currently invalid."
                             f" {logic} for {self.multiworld.get_player_name(self.player)}")


    def fill_slot_data(self):
        slot_data = {}
        slot_data["level_connections"] = self.level_connections
        slot_data["boss_connections"] = self.boss_connections
        slot_data["goal"] = self.options.goal.value
        slot_data["starting_kong"] = self.options.starting_kong.value
        slot_data["lost_world_rocks"] = self.options.lost_world_rocks.value
        slot_data["shuffled_abilities"] = self.options.shuffle_abilities.value
        slot_data["shuffled_animals"] = self.options.shuffle_animals.value
        slot_data["shuffled_barrels"] = self.options.shuffle_barrels.value
        return slot_data


    def generate_early(self):
        self.level_connections = dict()
        self.boss_connections = dict()
        self.rom_connections = dict()
        generate_level_list(self)

        # Handle Universal Tracker support, doesn't do anything during regular generation
        if hasattr(self.multiworld, "re_gen_passthrough"):
            if "Donkey Kong Country 2" in self.multiworld.re_gen_passthrough:
                passthrough = self.multiworld.re_gen_passthrough["Donkey Kong Country 2"]
                self.level_connections = passthrough["level_connections"]
                self.boss_connections = passthrough["boss_connections"]
                self.options.goal.value = passthrough["goal"]
                self.options.starting_kong.value = passthrough["starting_kong"]
                self.options.lost_world_rocks.value = passthrough["lost_world_rocks"]
                self.options.shuffle_abilities.value = passthrough["shuffled_abilities"]
                self.options.shuffle_animals.value = passthrough["shuffled_animals"]
                self.options.shuffle_barrels.value = passthrough["shuffled_barrels"]


    def write_spoiler(self, spoiler_handle: typing.TextIO) -> None:
        pass


    def extend_hint_information(self, hint_data: typing.Dict[int, typing.Dict[int, str]]):
        er_hint_data = {}
        map_connections = {**self.level_connections, **self.boss_connections}
        for loc_name in location_id_to_level_id.keys():
            level_name = loc_name.split(' - ')[0] + ": Level"
            for map_spot, level in map_connections.items():
                if level != level_name:
                    continue
                location = self.multiworld.get_location(loc_name, self.player)
                er_hint_data[location.address] = level_map[map_spot]
        
        hint_data[self.player] = er_hint_data


    def get_filler_item_name(self) -> str:
        return self.random.choice(list(junk_table.keys()))


    def generate_output(self, output_directory: str):
        try:
            patch = DKC2ProcedurePatch(player=self.player, player_name=self.multiworld.player_name[self.player])
            patch.write_file("dkc2_basepatch.bsdiff4", pkgutil.get_data(__name__, "data/dkc2_basepatch.bsdiff4"))
            patch_rom(self, patch)

            self.rom_name = patch.name

            patch.write(os.path.join(output_directory,
                                     f"{self.multiworld.get_out_file_name_base(self.player)}{patch.patch_file_ending}"))
        except Exception:
            raise
        finally:
            self.rom_name_available_event.set()  # make sure threading continues and errors are collected


    def modify_multidata(self, multidata: dict):
        import base64
        # wait for self.rom_name to be available.
        self.rom_name_available_event.wait()
        rom_name = getattr(self, "rom_name", None)
        # we skip in case of error, so that the original error in the output thread is the one that gets raised
        if rom_name:
            new_name = base64.b64encode(bytes(self.rom_name)).decode()
            multidata["connect_names"][new_name] = multidata["connect_names"][self.multiworld.player_name[self.player]]