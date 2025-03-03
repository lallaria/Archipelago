import random
import typing
import os
import json
from typing import List
from .Items import item_table, SMOItem, filler_item_table
from .Locations import locations_table, SMOLocation,loc_Cascade, loc_Cascade_Revisit,  \
    loc_Sand, loc_Lake, loc_Wooded, loc_Cloud, loc_Lost, loc_Metro, loc_Snow, \
    loc_Seaside, loc_Luncheon, loc_Ruined, loc_Bowser, loc_Cascade_Postgame,  \
    loc_Sand_Postgame, loc_Lake_Postgame, loc_Wooded_Postgame, loc_Cloud_Postgame, \
    loc_Lost_Postgame, loc_Metro_Postgame, loc_Snow_Postgame, loc_Seaside_Postgame, \
    loc_Luncheon_Postgame, loc_Ruined_Postgame, loc_Bowser_Postgame, locations_list
from .Options import SMOOptions
from .Rules import set_rules
from .Regions import create_regions
from BaseClasses import Item, Region, ItemClassification
from worlds.AutoWorld import World
"""
class MyGameSettings(settings.Group):
    class RomFile(settings.SNESRomPath):
        Insert help text for host.yaml here.

    rom_file: RomFile = RomFile("MyGame.sfc")
"""

class SMOWorld(World):
    """Insert description of the world/game here."""
    game = "Super Mario Odyssey"
    # this gives the generator all the definitions for our options
    options_dataclass = SMOOptions
    # this gives us typing hints for all the options we defined
    options: SMOOptions
    #options_dataclass = MyGameOptions  # options the player can set
    #options: MyGameOptions  # typing hints for option results
    #settings: typing.ClassVar[MyGameSettings]  # will be automatically assigned from type hint
    topology_present = True  # show path to required location checks in spoiler

    # ID of first item and location, could be hard-coded but code may be easier
    # to read with this as a property.
    #base_id = 829000
    # instead of dynamic numbering, IDs could be part of data

    # The following two dicts are required for the generation to know which
    # items exist. They could be generated from json or something else. They can
    # include events, but don't have to since events will be placed manually.
    item_name_to_id = item_table
    location_name_to_id = locations_table
    # Items can be grouped using their names to allow easy checking if any item
    # from that group has been collected. Group names can also be used for !hint

    item_name_groups = {
        "Cascade": loc_Cascade.keys() | loc_Cascade_Revisit.keys() | loc_Cascade_Postgame.keys(),
        "Sand": loc_Sand.keys() | loc_Sand_Postgame.keys(),
        "Lake": loc_Lake.keys() | loc_Lake_Postgame.keys(),
        "Wooded": loc_Wooded.keys() | loc_Wooded_Postgame.keys(),
        "Lost": loc_Lost.keys() | loc_Lost_Postgame.keys(),
        "Metro": loc_Metro.keys() | loc_Metro_Postgame.keys(),
        "Snow": loc_Snow.keys() | loc_Snow_Postgame.keys(),
        "Seaside": loc_Seaside.keys() | loc_Seaside_Postgame.keys(),
        "Luncheon": loc_Luncheon.keys() | loc_Luncheon_Postgame.keys(),
        "Ruined": loc_Ruined.keys() | loc_Ruined_Postgame.keys(),
        "Bowser": loc_Lake.keys() | loc_Lake_Postgame.keys()
    }



    def create_regions(self):
        create_regions(self, self.multiworld, self.player)

    def generate_early(self):
        self.multiworld.early_items[self.player]["Multi Moon Atop the Falls"] = 1
        self.multiworld.early_items[self.player]["Our First Power Moon"] = 1
        self.multiworld.early_items[self.player][list(loc_Cascade.keys())[random.randint(2,12)]] = 1


    def set_rules(self):
        set_rules(self, self.options)

    def create_item(self, name: str) -> Item:
        item_id = item_table[name]
        if name == "Life Up Heart" or name == "Coins":
            classification = ItemClassification.filler
        else:
            classification = ItemClassification.progression_skip_balancing
        item : SMOItem
        kingdom = ""
        for i in self.item_name_groups.keys():
            if name in self.item_name_groups[i]:
                kingdom = i
                break
        if kingdom == "":
            kingdom = "Post Game"
        item = SMOItem(name, classification, self.player, kingdom, item_id)
        return item

    def create_items(self):
        # Coins
        # Add Life Up Hearts
        pool = item_table.keys() - filler_item_table.keys()
        pool.remove("Beat the Game")
        pool.remove("Big Broodal Battle")


        # filler = 0
        # if self.options.goal < 14:
        #     for i in range(self.options.goal - 1, 32):
        #         pool -= locations_list[i].keys()
        for i in pool:
            self.multiworld.itempool += [self.create_item(i)]

        # filler = 776 - len(pool) -25
        # for i in range(filler):
        #     self.multiworld.itempool += [self.create_item("Coins")]
        # for check in self.unused_locations:
        #     self.multiworld.get_location(check, self.player).place_locked_item(self.create_item(check))


    """
    def generate_output(self, output_directory: str):
        if self.multiworld.players != 1:
            return
        data = {
            "slot_data": self.fill_slot_data(),
            "location_to_item": {self.location_name_to_id[i.name] : item_table[i.item.name] for i in self.multiworld.get_locations()},
            "data_package": {
                "data": {
                    "games": {
                        self.game: {
                            "item_name_to_id": self.item_name_to_id,
                            "location_name_to_id": self.location_name_to_id
                        }
                    }
                }
            }
        }
        filename = f"{self.multiworld.get_out_file_name_base(self.player)}.apsmo"
        with open(os.path.join(output_directory, filename), 'w') as f:
            json.dump(data, f)
    """