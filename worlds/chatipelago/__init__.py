from BaseClasses import Region, Entrance, Tutorial, ItemClassification
from .Items import *
from .Regions import *
from Options import PerGameCommonOptions
from .Rules import *
from worlds.AutoWorld import World, WebWorld

class ChatipelagoWeb(WebWorld):
    tutorials = [Tutorial(
    "Multiworld Setup Guide",
    "A guide to setting up the Archipelago Chatipelago software on your computer. This guide covers "
    "single-player, multiworld, and related software.",
    "English",
    "setup_en.md",
    "setup/en",
    ["DelilahIsDidi"]
)]

class ChatipelagoWorld(World):
    """
    Chat plays Archipelago!
    """
    game = "Chatipelago"
    options_dataclass = PerGameCommonOptions
    web = ChatipelagoWeb()

    location_name_to_id = location_table
    item_name_to_id = item_table

    def create_regions(self):
        regionpool = []

        for _ in location_table:
            if not "Tree" in _:
                locations += [ChatipelagoLoc(self.player, _, loc_data.id)
                    for loc_name, loc_data in .items()]
            else:
                self.options.priority_locations.value.add(_)

        connection = Entrance(self.player, "Open Chat", menu)
        menu.exits.append(connection)
        connection.connect(board)
        self.multiworld.regions += [menu, board]

        

    def create_items(self):
        itempool = []
        for _ in item_table:
            if "Magpie" in _:
                itempool.append(self.create_item(_, ItemClassification.progression))
            else:
                prog = self.random.choice(ItemClassification.useful, ItemClassification.filler)
                itempool.append(self.create_item(_, prog))

        self.multiworld.itempool += itempool

    def set_rules(self):
        set_rules(self.multiworld, self.player)
        set_completion_rules(self.multiworld, self.player)

    def fill_slot_data(self):
        return {
            "world_seed": self.random.getrandbits(32),
            "seed_name": self.multiworld.seed_name,
            "player_name": self.player_name,
            "player_id": self.player,
            "client_version": client_version,
            "race": self.multiworld.is_race,
        }

    def create_item(self, name: str, prog: ItemClassification) -> ChatipelagoItem:
        item_data = item_table[name]
        return ChatipelagoItem(name, prog, item_data.code, self.player)

