from typing import Self
from BaseClasses import Item, Region, Entrance, Tutorial, ItemClassification
from .Items import *
from .Regions import *
from .Options import ChatipelagoOptions
from .Rules import *
from worlds.AutoWorld import World, WebWorld
import logging
from json import loads

class ChatipelagoWeb(WebWorld):
    theme = "partyTime"
    tutorials = [Tutorial(
    "Multiworld Setup Guide",
    "A guide to setting up the Archipelago Chatipelago software on your computer. This guide covers "
    "single-player, multiworld, and related software.",
    "English",
    "setup_en.md",
    "setup/en",
    ["DelilahIsDidi","LMarioza","Dranzior"]
)]

class ChatipelagoWorld(World):
    """
    Chat plays Archipelago!
    """
    game = "Chatipelago"
    options_dataclass = ChatipelagoOptions
    options = ChatipelagoOptions
    web = ChatipelagoWeb()

    location_name_to_id = dict()
    item_name_to_id = dict()

    def __init__(self, multiworld: "MultiWorld", player: int):
        super().__init__(multiworld, player)

        self._item_list = loads(self.options.Item_List)
        self._progression_list = loads(self.options.Progression_List)
        self._filler_list = loads(self.options.Filler_List)
        self._trap_list = loads(self.options.Trap_List)
        self._location_list = loads(self.options.Location_List)
        self._progression_location_list = loads(self.options.Progression_Location_List)

    def generate_early(self):
        ## Replace any items before we set the pool
        if self._item_list:
            for i in item_table: item_table[i] = self._item_list.pop() 
        elif self._trap_list:
            for i in trap_item_table: trap_item_table[i] = self._trap_list.pop()
        elif self._filler_list:
            for i in filler_table: filler_table[i] = self._filler_list.pop()
        elif self._progression_list:
            for i in prog_item_table: prog_item_table[i] = self._progression_list.pop()

        if self._location_list:
            for i in region_table["Chatroom"]: region_table["Chatroom"][i] = self._location_list
        elif self._progression_location_list:
            for i in region_table["Prog"]: region_table["Prog"][i] = self._progression_location_list

        self.location_name_to_id = {name: l_id.address for name, l_id in location_data_table.items()}
        self.item_name_to_id = {name: i_id.code for name, i_id in item_data_table.items()}

    def create_items(self):
        itempool = []
        for name in item_data_table.keys():
            itempool.append(self.create_item(name))

        total_locations = len(region_table["Chatroom"]) + len(region_table["Prog"])
        itempool += [self.create_filler() for _ in range(total_locations - len(itempool))]

        self.multiworld.itempool += itempool

    def create_regions(self) -> None:   
        for region_name in region_table.keys():
            chati_region = Region(region_name, self.player, self.multiworld)
            self.multiworld.regions.append(chati_region)

        for name, data in region_table.items():
            chati_region = self.get_region(name)
            chati_region.add_locations({                                                            \
                loc_name: loc_data.address for loc_name, loc_data in location_data_table.items()    \
                if loc_data.region == name
            },ChatipelagoLoc)

        for source, target in chati_region_conn.items():
            source_region = self.multiworld.get_region(source, self.player)
            source_region.add_exits(target)

        for prio_loc in region_table["Prog"]:
            logging.info(f"prio: {prio_loc}")
            self.options.priority_locations.value.add(prio_loc)

    def set_rules(self) -> None:
        prog_list: list[Location] = [] #For Completion
        chat_rule = get_chat_rule(self)
        prog_rule = get_prog_rule(self)
        for loc in region_table["Chatroom"]:
            self.get_location(loc).access_rule = chat_rule
            self.get_location(loc).item_rule = lambda item: ItemClassification.progression not in item.classification
        for loc in region_table["Prog"]:
            self.get_location(loc).access_rule = prog_rule
            prog_list.append(self.get_location(loc))

        self.multiworld.completion_condition[self.player] = lambda state: has_win_locs(state)

        def has_win_locs(state: CollectionState) -> bool:
            any_check: bool = False
            for l in prog_list:
                if l in state.locations_checked:
                    any_check = True
                else:
                    return False
            return any_check

    def fill_slot_data(self):
        return {
            "seed_name": self.multiworld.seed_name,
            "player_name": self.player_name,
            "player_id": self.player
        }

    def create_item(self, name: str) -> Item:
        classification: ItemClassification = self.random.choice([ItemClassification.filler,
                                                       ItemClassification.useful])
        if name in prog_item_table:
            return ChatipelagoItem(name, item_data_table[name].classification, item_data_table[name].code, self.player)
        elif name in trap_item_table:
            self.trapcode = item_data_table[name].code
            return ChatipelagoItem(name, ItemClassification.trap, item_data_table[name].code, self.player)
        else:
            return ChatipelagoItem(name, classification, item_data_table[name].code, self.player)

    def get_filler_item_name(self) -> str:
        return self.multiworld.random.choice(filler_table + trap_item_table)
