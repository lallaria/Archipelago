from BaseClasses import Region, Entrance, Tutorial, ItemClassification
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

    location_name_to_id = {name: l_id.address for name, l_id in location_data_table}
    item_name_to_id = {name: i_id.code for name, i_id in item_data_table}

    def create_items(self):
        #load up the items!
        for item in item_table:
            item_data_table[item].classification=self.random.choice(ItemClassification.filler, \
                ItemClassification.useful) if not "Magpie" in item else ItemClassification.progression

        itempool = []
        for name, data in item_data_table:
            itempool.append(self.create_item(name, data))
        self.multiworld.itempool += itempool

    def get_filler_item_name(self) -> str:
        return self.multiworld.random.choice(filler_list)
    
    def create_regions(self) -> None:   
        for region_name in region_table.keys():
            chati_region = Region(region_name, self.player, self.multiworld)
            self.multiworld.regions.append(chati_region)

        for name, data in region_table:
            chati_region = self.get_region(name)
            chati_region.add_locations({                                                    \
                loc_name: loc_data.address for loc_name, loc_data in location_data_table    \
                if loc_data.region == name
            },ChatipelagoLoc)
            chati_region.add_exits(chati_region_conn[name])

        for prio_loc in region_table["Trees"]:
            self.options.priority_locations.value.add(prio_loc)

    def set_rules(self) -> None:
        tree_list = List[Location] #For Completion
        chat_rule = get_chat_rule(self)
        tree_rule = get_tree_rule(self)
        for loc in self.get_location(region_table["Chatroom"]):
            loc.access_rule = chat_rule
        for loc in self.get_location(region_table["Trees"]):
            loc.access_rule = tree_rule
            tree_list.append(loc)

        self.multiworld.completion_condition[self.player] = lambda state: state.locations_checked[tree_list]

    def fill_slot_data(self):
        return {
            "seed_name": self.multiworld.seed_name,
            "player_name": self.player_name,
            "player_id": self.player
        }

    def create_item(self, name: str, data: ChatipelagoItemData) -> ChatipelagoItem:
        return ChatipelagoItem(name, data.classification, data.code, self.player)

