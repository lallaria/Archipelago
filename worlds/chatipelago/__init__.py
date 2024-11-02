from BaseClasses import Item, Region, Entrance, Tutorial, ItemClassification
from .Items import *
from .Regions import *
from Options import PerGameCommonOptions
from .Rules import *
from worlds.AutoWorld import World, WebWorld

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
    options_dataclass = PerGameCommonOptions
    web = ChatipelagoWeb()

    location_name_to_id = {name: l_id.address for name, l_id in location_data_table.items()}
    item_name_to_id = {name: i_id.code for name, i_id in item_data_table.items()}

    def create_items(self):
        #load up the items!
        itempool = []

        for name, data in item_data_table.items():
            prog: ItemClassification = self.random.choice([ItemClassification.filler,
                ItemClassification.useful])
            if not "Magpie" in name:
                itempool.append(self.create_item(name, prog, data))
            else:
                itempool.append(self.create_item(name, data.classification, data))

        itempool += [self.create_filler() for _ in range(len(location_data_table) - len(itempool))]
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

        for deprio_loc in region_table["Chatroom"]:
            self.options.exclude_locations.value.add(deprio_loc)

        for prio_loc in region_table["Trees"]:
            self.options.priority_locations.value.add(prio_loc)

    def set_rules(self) -> None:
        tree_list: list[Location] = [] #For Completion
        chat_rule = get_chat_rule(self)
        tree_rule = get_tree_rule(self)
        for loc in region_table["Chatroom"]:
            self.get_location(loc).access_rule = chat_rule
        for loc in region_table["Trees"]:
            self.get_location(loc).access_rule = tree_rule
            tree_list.append(self.get_location(loc))

        self.multiworld.completion_condition[self.player] = lambda state: has_win_locs(state)

        def has_win_locs(state: CollectionState) -> bool:
            any_check: bool = False
            for l in tree_list:
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

    def create_item(self, name: str, prog: ItemClassification, data: ChatipelagoItemData) -> ChatipelagoItem:
        return ChatipelagoItem(name, prog, data.code, self.player)
    def create_filler(self) -> ChatipelagoItem:
        return self.create_item(self.get_filler_item_name(), ItemClassification.filler, ChatipelagoItemData())
    def get_filler_item_name(self) -> str:
        return self.multiworld.random.choice(filler_list)

