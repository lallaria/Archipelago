from ..game_data.local_data import item_id_table, character_item_table, party_id_nums
from ..game_data.text_data import eb_text_table, text_encoder
from ..game_data.static_location_data import location_groups
import struct


def setup_hints(world):
    hint_types = [
        # gives a hint for a specific out of the way location in this player's world, regardless of what item it is
        "item_at_location",
        # woth or foolish hint, checks specific location groups of this world so as to be more helpful.
        "region_progression_check",
        "hint_for_good_item",  # gives the exact location and sender of a good item for the local player
        "item_in_local_region",  # Hints a random item that can be found in a specific local location group
        "prog_item_at_region",  # Hints the region that a good item can be found for this player
        "joke_hint"  # Doesn't hint anything
        # specific characters?
        # dungeon er?
    ]
    world.in_game_hint_types = []
    world.hinted_locations = {}
    world.hinted_items = {}
    world.hinted_regions = {}

    # may not need to be world.
    world.local_hintable_locations = [
        "Onett - Mayor Pirkle",
        "Onett - South Road Present",
        "Onett - Meteor Item",
        "Onett - Treehouse Guy",
        "Twoson - Orange Kid Donation",
        "Twoson - Everdred Meeting",
        "Twoson - Apple Kid Invention",
        "Fourside - Post-Moonside Delivery",
        "Lost Underworld - Talking Rock",
        "Dungeon Man - 2F Hole Present",
        "Poo - Starting Item",
        "Summers - Magic Cake",
        "Deep Darkness - Teleporting Monkey",
        "Twoson - Insignificant Location",
        "Peaceful Rest Valley - North Side Present",
        "Twoson - Paula's Mother",
        "Happy-Happy Village - Prisoner",
        "Threed - Boogey Tent Trashcan",
        "Threed - Zombie Prisoner",
        "Grapefruit Falls - Saturn Cave Present",
        "Saturn Valley - Saturn Coffee",
        "Dusty Dunes - South Side Present",
        "Stonehenge - Tony Item",
        "Stonehenge - Kidnapped Mr. Saturn",
        "Stonehenge - Dead End Present",
        "Stonehenge - Near End of the Maze Present",
        "Stonehenge - Bridge Room East Balcony Present",
        "Gold Mine - B1F Isolated Present",
        "Fourside - Venus Gift",
        "Fourside - Bakery 2F Gift",
        "Fourside - Department Store Blackout",
        "Monotoli Building - Monotoli Character",
        "Dungeon Man - 1F Exit Ledge Present",
        "Deep Darkness - Barf Character",
        "Lumine Hall - B1F West Alcove Present",
        "Cave of the Present - Star Master",
        "Cave of the Present - Broken Phase Distorter",
        "Fire Spring - 1st Cave Present",
        "Tenda Village - Tenda Tea",
        "Deep Darkness - Barf Character",
        "Dalaam - Trial of Mu",
        "Pyramid - Northwest Door Sarcophagus"
    ]

    world.local_hintable_items = [
        "Franklin Badge",
        "Key to the Shack",
        "Key to the Cabin",
        "Key to the Tower",
        "Key to the Locker",
        "Bad Key Machine",
        "Pencil Eraser",
        "Eraser Eraser",
        "UFO Engine",
        "Yogurt Dispenser",
        "Zombie Paper",
        "King Banana",
        "Signed Banana",
        "Tendakraut",
        "Jar of Fly Honey",
        "Wad of Bills",
        "Tiny Ruby",
        "Diamond",
        "Meteorite Piece",
        "Hieroglyph Copy",
        "Piggy Nose",
        "Carrot Key",
        "Police Badge",
        "Letter For Tony",
        "Mining Permit",
        "Contact Lens",
        "Insignificant Item",
        "Pak of Bubble Gum",
        "Sea Pendant",
        "Shyness Book",
        "Hawk Eye",
        "Paula",
        "Jeff",
        "Poo",
        "Onett Teleport",
        "Twoson Teleport",
        "Happy-Happy Village Teleport",
        "Threed Teleport",
        "Saturn Valley Teleport",
        "Dusty Dunes Teleport",
        "Fourside Teleport",
        "Winters Teleport",
        "Summers Teleport",
        "Scaraba Teleport",
        "Dalaam Teleport",
        "Deep Darkness Teleport",
        "Tenda Village Teleport",
        "Lost Underworld Teleport"
    ]

    world.joke_hints = [
        "you can find 6 hint shops around the world.",
        "if you want to hint for an item, use !hint in your text client!",
        "the mouse at the Fourside Department Store knows what the Spook has.",
        "my business may be a scam.",
        "there's a guy near Threed's hotel who saw the Zombies take someone away.",
        "you can use the Y button to run or mash through text.",
        "you can submit custom window flavors in the game's Archipelago thread.",
        "you can buy a ruler at the Fourside Department Store.",
        "you can store a lot of items in your backpack with the R button.",
        "Giygas's guard may actually be from another seed...",
        "if you have multiple of something important, you can throw away the extras.",
        "the chicken crossed the road because it was trying to use Teleport α.",
        "Figment's Ice Palace can probably be found in Ice Palace.",
        "you can talk to the hint shop owners for a hint.",
        "deliveryman are bad at using keys.",
        "PK scramble is a pretty good time.",
        "Apple Kid researched the Power of the Earth with Dr. Andonuts.",
        "you can find beta Archipelago games on the Archipelago discord.",
        "you can randomize EarthBound with Archipelago.",
        "hint prices double with each one bought.",
        "you probably should have kept your money.",
        "there's a secret option to plando Lumine Hall's text.",
        "this isn't a very good hint.",
        "some hints are good hints.\n@But not this one."
    ]

    if world.options.magicant_mode.value in [0, 3]:
        world.local_hintable_items.append("Magicant Teleport")

    for item in world.removed_teleports:
        if item.name in world.local_hintable_items:
            #let's not hint an item that doesn't exist
            world.local_hintable_items.remove(item.name)

    if world.options.giygas_required:
        world.local_hintable_locations.append("Cave of the Past - Present")
    
    if world.options.magicant_mode == 0:
        world.local_hintable_locations.append("Magicant - Ness's Nightmare")

    for i in range(6):
        world.in_game_hint_types.append(world.random.choice(hint_types))
    # print(world.in_game_hint_types)

    for index, hint in enumerate(world.in_game_hint_types):
        if hint == "item_at_location":
            location = world.random.choice(world.local_hintable_locations)
            world.hinted_locations[index] = location
        
        elif hint == "region_progression_check":
            key, value = world.random.choice(list(location_groups.items()))
            group = key
            world.hinted_regions[index] = group

        elif hint == "hint_for_good_item" or hint == "prog_item_at_region":
            item = world.random.choice(world.local_hintable_items)
            world.hinted_items[index] = item

        elif hint == "item_in_local_region":
            key, value = world.random.choice(list(location_groups.items()))
            group = key
            location = world.random.choice(sorted(value))
            world.hinted_regions[index] = group
            world.hinted_locations[index] = location


def parse_hint_data(world, location, rom, hint):
    if hint == "item_at_location":
        if world.player == location.item.player and location.item.name in character_item_table:
            player_text = "your friend "
            # In-game text command to display party member names
            item_text = bytearray([0x1C, 0x02, party_id_nums[location.item.name]])
        elif world.player == location.item.player:
            player_text = "your "
            if location.item.name in item_id_table:
                # In-game text command to display item names
                item_text = bytearray([0x1C, 0x05, item_id_table[location.item.name]])
            else:
                # if the item doesn't have a name (e.g it's PSI)
                item_text = text_encoder(location.item.name, eb_text_table, 128)
        else:
            player_text = f"{world.multiworld.get_player_name(location.item.player)}'s "
            item_text = text_encoder(location.item.name, eb_text_table, 128)
            item_text.extend([0x50])

        player_text = text_encoder(player_text, eb_text_table, 255)
        location_text = text_encoder(f" can be found at {location.name}.", eb_text_table, 255)
        text = player_text + item_text + location_text
        # [player]'s [item] can be found at [location].
        text.append(0x02)

    elif hint == "region_progression_check":
        if world.progression_count == 1:
            text = f"you can find {world.progression_count} important item at {world.hinted_area}."
        else:
            text = f"you can find {world.progression_count} important items at {world.hinted_area}."
        text = text_encoder(text, eb_text_table, 255)
        text.append(0x02)
        
    elif hint == "hint_for_good_item" or hint == "prog_item_at_region" or hint == "item_in_local_region":
        if location.item.name in character_item_table and location.item.player == world.player:
            item_text = text_encoder("your friend ", eb_text_table, 255)
            item_text.extend([0x1C, 0x02, party_id_nums[location.item.name]])
        elif location.item.name in item_id_table and location.item.player == world.player:
            item_text = text_encoder("your ", eb_text_table, 255)
            item_text.extend([0x1C, 0x05, item_id_table[location.item.name]])
        elif location.item.player == world.player:
            item_text = text_encoder(f"your {location.item.name}", eb_text_table, 128)
        else:
            item_text = f"{world.multiworld.get_player_name(location.item.player)}'s {location.item.name}"
            item_text = text_encoder(item_text, eb_text_table, 255)
        item_text.extend(text_encoder(" can be found ", eb_text_table, 255))
        
        if location.player != world.player:
            player_text = text_encoder(f"by {world.multiworld.get_player_name(location.player)}", eb_text_table, 255)
        else:
            player_text = text_encoder(" ", eb_text_table, 255)
        
        if hint == "hint_for_good_item":
            location_text = text_encoder(f"at {location.name}.", eb_text_table, 255)
            # your [item] can be found by [player] at [location]

        else:
            location_name_groups = world.multiworld.worlds[location.player].location_name_groups
            possible_location_groups = [
                group_name for group_name, group_locations in location_name_groups.items()
                if location.name in group_locations and group_name != "Everywhere"
            ]
            if not possible_location_groups:
                if location.parent_region.name == "Menu":
                    area = ""
                else:
                    area = f"near {location.parent_region.name}"
            else:
                area = f"near {world.random.choice(possible_location_groups)}"
            location_text = text_encoder(f"somewhere {area}.", eb_text_table, 255)
            # your [item] can be found by [player] somewhere near [location group]
        text = item_text + player_text + location_text
        text.append(0x02)

    elif hint == "joke_hint":
        text = world.random.choice(world.joke_hints)
        text = text_encoder(text, eb_text_table, 255)
        text.append(0x02)

    hint_addresses = [
        0x070376,
        0x0703A8,
        0x0703DA,
        0x07040C,
        0x07043E,
        0x070470
    ]

    scoutable_hint_addresses = [
        0x2EF3D5,
        0x2EF3EB,
        0x2EF401,
        0x2EF417,
        0x2EF42D,
        0x2EF443
    ]
    rom.write_bytes(0x310000 + world.hint_pointer, text)
    rom.write_bytes(hint_addresses[world.hint_number], struct.pack("I", 0xF10000 + world.hint_pointer))

    if hint in ["item_at_location", "hint_for_good_item"] and location.player == world.player:
        rom.write_bytes(scoutable_hint_addresses[world.hint_number], struct.pack("I", 0xEEF451))
        rom.write_bytes(0x310250 + (world.hint_number * 2), struct.pack("H", location.address - 0xEB0000))
    else:
        rom.write_bytes(scoutable_hint_addresses[world.hint_number], struct.pack("I", 0xEEF4B2))

    world.hint_pointer = world.hint_pointer + len(text)
    world.hint_number += 1

    # Word on the street is that PLAYER's ITEM can be found at LOCATION
    # Word on the street is that REGION has X important items
    # Word on the street is that your ITEM can be found by PLAYER at LOCATION
    # Word on the street is that PLAYER's ITEM can be found somewhere near REGION...
    # Word on the street is that your ITEM can be found somewhere near REGION...
    # char item hint?
    # That's all for today.
    # Like text part 1, extend 0x1C 0x05 0xItem Item, extend (the rest of the string)