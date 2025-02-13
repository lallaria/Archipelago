from typing import List

from BaseClasses import Region, Tutorial, ItemClassification
from worlds.AutoWorld import WebWorld, World
from .items import WordipelagoItem, item_data_table, item_table
from .locations import WordipelagoLocation, location_data_table, location_table
from .options import WordipelagoOptions
from .regions import region_data_table
from .rules import create_rules



class WordipelagoWebWorld(WebWorld):
    theme = "partyTime"
    
    setup_en = Tutorial(
        tutorial_name="Start Guide",
        description="A guide to playing Wordipelago.",
        language="English",
        file_name="guide_en.md",
        link="guide/en",
        authors=["ProfDeCube"]
    )
    
    tutorials = [setup_en]


class WordipelagoWorld(World):
    """The greatest game of all time."""

    game = "Wordipelago"
    web = WordipelagoWebWorld()
    options: WordipelagoOptions
    options_dataclass = WordipelagoOptions
    location_name_to_id = location_table
    item_name_to_id = item_table
    starting_items = []
    
    # def add_time_rewards(options):
    #     for i in range(options.time_reward_count):
    #         item_data_table["time " + str(i)] =  WordipelagoItemData(code=200 + i,name="Time",type=ItemClassification.filler),
    def generate_basic(self):
        for i in range(self.options.time_reward_count):
            self.item_name_to_id["Time"] = 200

    def fill_slot_data(self):
            """
            make slot data, which consists of options, and some other variables.
            """
            yacht_dice_options = self.options.as_dict(
                "words_to_win",
                "starting_letters",
                "starting_guesses",
                "starting_cooldown",
                "time_reward_count",
                "time_reward_seconds",
                "yellow_unlocked",
                "unused_letters_unlocked",
                "shuffle_typing",
                "start_inventory_from_pool",
            )
            slot_data = yacht_dice_options # combine the two
            return {**slot_data, "starting_items": self.starting_items}
            
    def create_item(self, name: str) -> WordipelagoItem:
        return WordipelagoItem(name, item_data_table[name].type, item_data_table[name].code, self.player)

    def create_items(self) -> None:
        item_pool: List[WordipelagoItem] = []
        starting_letters: List[str] = []

        for i in range(self.options.starting_letters):
            weighted_letter = 'E'
            starting_letters.append('The Letter ' + weighted_letter)
            self.starting_items.append(weighted_letter)
            self.multiworld.push_precollected(self.create_item('The Letter ' + weighted_letter))

        for key, item in item_data_table.items():
            if item.code and item.can_create(self) and key not in starting_letters:
                for i in range(item.count(self)):
                    item_pool.append(self.create_item(key))
        for i in range(self.options.time_reward_count):
            item_pool.append(WordipelagoItem("Time", ItemClassification.filler, 200, self.player))
            
        # Filler Items
        location_count = 26 + 5 + self.options.words_to_win
        item_count = 26 - self.options.starting_letters + 6 - self.options.starting_guesses + self.options.time_reward_count
        if not self.options.yellow_unlocked: 
            item_count += 1
        if not self.options.unused_letters_unlocked: 
            item_count += 1
        
        print("locations")
        print(location_count)
        print("items")
        print(item_count)
        if(location_count > item_count):
            for i in range(location_count - item_count):
                item_pool.append(WordipelagoItem("Time", ItemClassification.filler, 200, self.player))
                # item_pool.append(WordipelagoItem("Not Much", ItemClassification.filler, 1000, self.player))
        
        print(len(item_pool))
        # if(location_count < item_count):        
            
        self.multiworld.itempool += item_pool
        # self.multiworld.precollected_items = {self.player: starting_item_pool}
        

    def create_regions(self) -> None:
        # Create regions.
        for region_name in region_data_table.keys():
            region = Region(region_name, self.player, self.multiworld)
            self.multiworld.regions.append(region)

        # Create locations.
        for region_name, region_data in region_data_table.items():
            region = self.get_region(region_name)
            region.add_locations({
                location_name: location_data.address for location_name, location_data in location_data_table.items()
                if location_data.region == region_name and location_data.can_create(self)
            }, WordipelagoLocation)
            if(region_name == 'Words'):
                for i in range(self.options.words_to_win):
                    name = "Word " + str(i + 1)
                    region.add_locations({name: 200 + i})
            region.add_exits(region_data_table[region_name].connecting_regions)

        # Set priority location for the Big Red Button!
        self.options.priority_locations.value.add("1 Correct Letter In Word")
        self.options.priority_locations.value.add("2 Correct Letter In Word")
        self.options.priority_locations.value.add("3 Correct Letter In Word")
        self.options.priority_locations.value.add("4 Correct Letter In Word")
        self.options.priority_locations.value.add("5 Correct Letter In Word")
        
        self.options.priority_locations.value.add("Word 1")

    def set_rules(self):
        create_rules(self)
        print("rules")

    def get_filler_item_name(self) -> str:
        return "A Cool Filler Item (No Satisfaction Guaranteed)"
