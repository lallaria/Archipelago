from BaseClasses import Item, Region, Tutorial, ItemClassification
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
    options: ChatipelagoOptions

    web = ChatipelagoWeb()
    
    world_item_data = item_data_table
    world_filler_data = filler_table
    world_trap_data = trap_item_table
    world_prog_data = prog_item_table
    world_location_data = location_data_table
    world_region_data = region_table

    location_name_to_id = {name: l_id.address for name, l_id in location_data_table.items()}
    item_name_to_id = {name: i_id.code for name, i_id in item_data_table.items()}

    def __init__(self, multiworld: "MultiWorld", player: int):
        super().__init__(multiworld, player)

        self._item_list = []
        self._progression_list = []
        self._filler_list = []
        self._trap_list = []
        self._location_list = []
        self._progression_location_list = []

    def generate_early(self):
        self._item_list = self.options.Inventory_List.value.rstrip("\"]'").lstrip("r'[\"").split('","')
        logging.info(f"{self._item_list} | {self.options.Inventory_List.value}")
        self._progression_list = self.options.Progression_List.value.rstrip("\"]'").lstrip("r'[\"").split('","')
        logging.info(self._progression_list)
        self._filler_list = self.options.Filler_List.value.rstrip("\"]'").lstrip("r'[\"").split('","')
        self._trap_list = self.options.Trap_List.value.rstrip("\"]'").lstrip("r'[\"").split('","')
        self._location_list = self.options.Location_List.value.rstrip("\"]'").lstrip("r'[\"").split('","')
        self._progression_location_list = self.options.Progression_Location_List.value.rstrip("\"]'").lstrip("r'[\"").split('","')

        ## Replace any items before we set the pool
        new_item_dict = {}
        new_loc_dict = {}

        for n,i in self.item_name_to_id.items():
            n_str = ""
            if i < 11490 and self._item_list:
                n_str = self._item_list.pop()
                new_item_dict[n_str] = ChatipelagoItemData(
                    code = i)
            elif 11490 <= i < 12490 and self._progression_list:
                n_str = self._progression_list.pop()
                new_item_dict[n_str] = ChatipelagoItemData(
                    code = i)
                self.world_prog_data.remove(n)
                self.world_prog_data.append(n_str)
            elif 12490 <= i < 13490 and self._filler_list:
                n_str = self._filler_list.pop()
                new_item_dict[n_str] = ChatipelagoItemData(
                    code = i)
                self.world_filler_data.remove(n)
                self.world_filler_data.append(n_str)
            elif 13490 <= i < 14900 and self._trap_list:
                n_str = self._trap_list.pop()
                new_item_dict[n_str] = ChatipelagoItemData(
                    code = i)
                self.world_trap_data.remove(n)
                self.world_trap_data.append(n_str)
            else:
                new_item_dict[n] = ChatipelagoItemData(
                    code = i)

        for l,i in self.location_name_to_id.items():
            l_str = ""
            if i < 600 and self._location_list:
                l_str = self._location_list.pop()
                new_loc_dict[l_str] = ChatipelagoLocationData(
                    region = "Chatroom",
                    address = i)
                self.world_region_data["Chatroom"].append(l_str)
                self.world_region_data["Chatroom"].remove(l)
            elif i >= 600 and self._progression_location_list:
                l_str = self._progression_location_list.pop()
                new_loc_dict[l_str] = ChatipelagoLocationData(
                    region = "Prog",
                    address = i)
                self.world_region_data["Prog"].append(l_str)
                self.world_region_data["Prog"].remove(l)
            else:
                new_loc_dict[l] = location_data_table[l]

        self.world_location_data = new_loc_dict
        self.world_item_data = new_item_dict
        self.item_name_to_id = {name: l_id.address for name, l_id in self.world_location_data.items()}
        self.location_name_to_id = {name: i_id.code for name, i_id in self.world_item_data.items()}

    def create_items(self):
        itempool = []
        for name in self.world_item_data.keys():
            itempool.append(self.create_item(name))

        total_locations = len(self.world_location_data)
        itempool += [self.create_filler() for _ in range(total_locations - len(itempool))]

        self.multiworld.itempool += itempool

    def create_regions(self) -> None:   
        for region_name in self.world_region_data.keys():
            chati_region = Region(region_name, self.player, self.multiworld)
            self.multiworld.regions.append(chati_region)

        for name, data in self.world_region_data.items():
            chati_region = self.get_region(name)
            chati_region.add_locations({                                                                 \
                loc_name: loc_data.address for loc_name, loc_data in self.world_location_data.items()    \
                if loc_data.region == name
            },ChatipelagoLoc)

        for source, target in chati_region_conn.items():
            source_region = self.multiworld.get_region(source, self.player)
            source_region.add_exits(target)

        for prio_loc in self.world_region_data["Prog"]:
            self.options.priority_locations.value.add(prio_loc)

    def set_rules(self) -> None:
        prog_list: list[Location] = [] #For Completion
        chat_rule = get_chat_rule(self)
        prog_rule = get_prog_rule(self)
        for loc in self.world_region_data["Chatroom"]:
            self.get_location(loc).access_rule = chat_rule
            self.get_location(loc).item_rule = lambda item: ItemClassification.progression not in item.classification
        for loc in self.world_region_data["Prog"]:
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
        if name in self.world_prog_data:
            return ChatipelagoItem(name, self.world_item_data[name].classification, self.world_item_data[name].code, self.player)
        elif name in self.world_trap_data:
            self.trapcode = self.world_item_data[name].code
            return ChatipelagoItem(name, ItemClassification.trap, self.world_item_data[name].code, self.player)
        else:
            return ChatipelagoItem(name, classification, self.world_item_data[name].code, self.player)

    def get_filler_item_name(self) -> str:
        return self.multiworld.random.choice(self.world_filler_data + self.world_trap_data)
