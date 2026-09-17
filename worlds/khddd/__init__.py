from typing import List, Dict, Any

from BaseClasses import Region, Entrance, Tutorial, ItemClassification
from worlds.AutoWorld import World
from .Items import KHDDDItem, item_data_table, item_table, get_items_by_category, get_items_by_character_category
from .Locations import KHDDDLocation, location_data_table, location_table, event_location_table, get_locations_by_region
from .Options import KHDDDOptions
from .Regions import region_data_table, create_regions
from .Rules import set_rules
from worlds.LauncherComponents import Component, components, Type, launch as launch_component
import random

from ..generic.Rules import add_item_rule


def launch_client():
    from .Client import launch
    launch_component(launch, name="KHDDD Client")

components.append(Component("KHDDD Client", "KHDDD Client", func=launch_client, component_type=Type.CLIENT))

class KHDDDWorld(World):
    """KHDDD is a cool KH game"""
    game = "Kingdom Hearts Dream Drop Distance"
    options: KHDDDOptions
    options_dataclass = KHDDDOptions
    #location_name_to_id = event_location_table
    location_name_to_id = {name: data.code for name, data in location_data_table.items()}
    item_name_to_id = item_table
    origin_region_name = "World"

    def create_item(self, name: str) -> KHDDDItem:
        return KHDDDItem(name, item_data_table[name].type, item_data_table[name].code, self.player)

    def create_items(self) -> None:
        self.place_predetermined_items()
        self.place_starting_items()
        starting_worlds = self.determine_starting_worlds()

        item_pool: List[KHDDDItem] = []

        # Pre-fill level up locations if applicable
        filler_stat_names = ["Strength Increase [Sora]", "Magic Increase [Sora]", "Defense Increase [Sora]",
                             "Strength Increase [Riku]", "Magic Increase [Riku]", "Defense Increase [Riku]"]

        item_pool = self.place_stat_items(item_pool, filler_stat_names)

        total_locations = len(self.multiworld.get_unfilled_locations(self.player))

        #Add correct flowmotion to the item pool
        if int(self.options.single_flowmotion) == 1: #Flowmotion is a single item
            item_pool += [self.create_item("Flowmotion")]
        else:
            for name, data in get_items_by_category("Flowmotion").items(): #Each flowmotion is an individual item
                if name == "Flowmotion":
                    continue
                if name == "Super Jump" and self.options.super_jump_start:
                    continue
                item_pool += [self.create_item(name)]

        #Add recipes to the item pool
        recipe_count = max(int(self.options.recipes_in_pool-2), int(self.options.recipe_reqs-2))
        recipes = []
        for name, data in get_items_by_category("Recipe").items():
            if name != "Meow Wow Recipe" and name != "Komory Bat Recipe":
                recipes.append(name)

        #Shuffle recipes and add to item pool based on reqs
        random.shuffle(recipes)
        for x in range(recipe_count):
            item_pool += [self.create_item(recipes[x])]

        #Always have Meow Wow and Komory Bat in the item pool
        item_pool += [self.create_item("Meow Wow Recipe")]
        item_pool += [self.create_item("Komory Bat Recipe")]

        non_filler_categories = ["Stat", "World", "Keyblade", "Movement", "Defense", "Ability", "Special"]

        for name, data in item_data_table.items():
            quantity = data.qty
            if data.category in non_filler_categories:
                #Prevent starting worlds and str/mag/def increases from being placed in pool again
                if name in starting_worlds or name in filler_stat_names:
                    continue

                #Omit any items not for the selected character
                if data.character > 0 and int(self.options.character) > 0 and data.character != self.options.character:
                    continue

                if name == "Lucky Emblem":
                    continue

                item_pool += [self.create_item(name) for _ in range(0, quantity)]

        #Create lucky emblems
        emblems_to_create = self.verify_emblems()
        item_pool += [self.create_item("Lucky Emblem") for _ in range(0, emblems_to_create)]

        #Fill empty locations with filler
        while len(item_pool) < total_locations:
            item_pool.append(self.create_item(self.get_filler_item_name()))

        self.multiworld.itempool += item_pool

    def determine_starting_worlds(self):
        #Starting Worlds
        starting_worlds = []
        world_count = self.options.starting_worlds
        if self.options.starting_worlds == 0 and self.options.play_destiny_islands == 0 or self.options.character == 2:
            world_count = 1
        if world_count > 0:
            possible_starting_worlds = []
            if self.options.character < 2: #TODO: Include Traverse Town
                possible_starting_worlds = possible_starting_worlds + ["La Cite des Cloches [Sora]", "Prankster's Paradise [Sora]",
                    "Country of the Musketeers [Sora]", "Symphony of Sorcery [Sora]"]
            if self.options.character == 2 or self.options.character == 0:
                possible_starting_worlds = possible_starting_worlds + [ "The Grid [Riku]",
                    "La Cite des Cloches [Riku]", "Prankster's Paradise [Riku]", "Country of the Musketeers [Riku]", "Symphony of Sorcery [Riku]"]
            starting_worlds = self.random.sample(possible_starting_worlds, min(world_count, len(possible_starting_worlds)))
            for starting_world in starting_worlds:
                self.multiworld.push_precollected(self.create_item(starting_world))
        return starting_worlds

    def place_starting_items(self):
        if self.options.super_jump_start:
            self.multiworld.push_precollected(self.create_item("Super Jump"))

    def place_stat_items(self, item_pool, filler_stat_names):
        #Stats Options:
        # 0 - Random Items
        # 1 - Random Items; No Progression
        # 2 - Stat Items Only
        # 3 - Vanilla; Exclude Locations

        if self.options.stats_on_levels == 3: return item_pool #Do not pre-place items if vanilla stats are enabled

        level_cap = self.options.level_cap
        level_up_locations = list(get_locations_by_region("Levels").keys())

        for num in range(level_cap, 100):
            level_result = f"{num:02}"
            if self.options.character < 2: #Add level cap rule to Sora levels
                add_item_rule(self.get_location("Sora Level "+level_result), lambda item: item.classification == ItemClassification.filler)
            if self.options.character == 0 or self.options.character == 2: #Add level cap rule to Riku levels
                add_item_rule(self.get_location("Riku Level "+level_result), lambda item: item.classification == ItemClassification.filler)


        if self.options.stats_on_levels < 2: #Add stat requirements from options to item pool without necessarily assigning to levels
            for _ in range(self.options.strength_in_pool):
                if self.options.character == 0 or self.options.character == 1:
                    item_pool += [self.create_item("Strength Increase [Sora]")]
                if self.options.character == 0 or self.options.character == 2:
                    item_pool += [self.create_item("Strength Increase [Riku]")]
            for _ in range(self.options.magic_in_pool):
                if self.options.character == 0 or self.options.character == 1:
                    item_pool += [self.create_item("Magic Increase [Sora]")]
                if self.options.character == 0 or self.options.character == 2:
                    item_pool += [self.create_item("Magic Increase [Riku]")]
            for _ in range(self.options.defense_in_pool):
                if self.options.character == 0 or self.options.character == 1:
                    item_pool += [self.create_item("Defense Increase [Sora]")]
                if self.options.character == 0 or self.options.character == 2:
                    item_pool += [self.create_item("Defense Increase [Riku]")]

            if self.options.stats_on_levels == 1:
                # Create item rules for level locations to prevent progression
                for num in range(2, level_cap-1):
                    level_result = f"{num:02}"
                    if self.options.character < 2:
                        add_item_rule(self.get_location("Sora Level " + level_result), lambda item: not item.classification == ItemClassification.progression)
                    if self.options.character == 0 or self.options.character == 2:  # Add level cap rule to Riku levels
                        add_item_rule(self.get_location("Riku Level " + level_result), lambda item: not item.classification == ItemClassification.progression)

        # Place Stats on levels
        if self.options.stats_on_levels == 2:
            possible_level_up_item_pool = []

            for name, data in get_items_by_category("Stat").items():
                quantity = data.qty
                if data.category == "Stat":
                    if name in filler_stat_names:
                        if self.options.character == 0 or self.options.character == 1 and "Sora" in name or self.options.character == 2 and "Riku" in name:
                            for _ in range(quantity):
                                possible_level_up_item_pool.append(name)

            #Create more stat items in the event stats in options do not total to level cap
            items_for_levels = level_cap
            if self.options.character == 0:
                items_for_levels *= 2 #Double needed items to account for both characters
            while len(possible_level_up_item_pool) < items_for_levels:
                #Pad out with more stats TODO: Maybe replace with filler?
                random_stat = 0
                if self.options.character == 0:
                    random_stat = random.randint(0, 5)
                elif self.options.character == 1:
                    random_stat = random.randint(0, 2)
                elif self.options.character == 2:
                    random_stat = random.randint(3, 5)
                possible_level_up_item_pool.append(filler_stat_names[random_stat])

            self.random.shuffle(possible_level_up_item_pool)

            level_up_item_pool = possible_level_up_item_pool

            current_level_for_placing_stats = 2

            while current_level_for_placing_stats <= level_cap:
                level_result = f"{current_level_for_placing_stats:02}"
                if self.options.character < 2:
                    self.get_location("Sora Level "+level_result).place_locked_item(self.create_item(level_up_item_pool.pop()))
                if self.options.character == 2 or self.options.character == 0:
                    self.get_location("Riku Level "+level_result).place_locked_item(self.create_item(level_up_item_pool.pop()))
                current_level_for_placing_stats += 1

        return item_pool

    def place_predetermined_items(self) -> None:
        if self.options.goal == 1: #Place Superboss Goal Item
            self.get_location("All Superbosses Defeated [Sora] [Riku]").place_locked_item(self.create_item("Victory"))
        elif self.options.goal == 0:
            #Place Goal item based on who the final boss actually is
            if self.options.character == 0 or self.options.character == 2: #Either both characters or riku
                if self.options.armored_ventus_nightmare: #Are we fighting avn?
                    self.get_location("Armored Ventus Nightmare Defeated [Riku]").place_locked_item(self.create_item("Victory"))
                else: #We are fighting YX
                    self.get_location("The World That Never Was Young Xehanort Defeated [Riku]").place_locked_item(self.create_item("Victory"))
            else: #We are fighting Xemnas
                self.get_location("The World That Never Was Xemnas Bonus Slot 1 [Sora]").place_locked_item(self.create_item("Victory"))
        else: #Lucky emblem hunt
            self.get_location("All Lucky Emblems Found [Sora] [Riku]").place_locked_item(self.create_item("Victory"))

    def create_regions(self) -> None:
        create_regions(self.multiworld, self.player, self.options)

    def get_filler_item_name(self) -> str:
        if int(self.options.instant_drop_trap_chance) > 0: #Check to see if a trap was rolled
            if int(self.random.randint(0, 99) < int(self.options.instant_drop_trap_chance)):
                return "Instant Drop"
        fillers = {}
        fillers.update(get_items_by_character_category(int(self.options.character), "Command"))
        fillers.update(get_items_by_character_category(int(self.options.character), "Item"))
        return self.random.choices([filler for filler in fillers.keys()])[0]


    def set_rules(self):
        set_rules(self)

    def fill_slot_data(self) -> Dict[str, Any]:
        slot_data = {"character": int(self.options.character)}
        #Roll random keyblade stats
        if self.options.randomize_keyblade_stats:
            slot_data["keyblade_stats"] = ""
            min_str_bonus = self.options.keyblade_min_str.value
            max_str_bonus = self.options.keyblade_max_str.value
            min_mag_bonus = self.options.keyblade_min_mag.value
            max_mag_bonus = self.options.keyblade_max_mag.value
            for i in range(30):
                str_bonus = int(self.random.randint(min_str_bonus, max_str_bonus))
                mag_bonus = int(self.random.randint(min_mag_bonus, max_mag_bonus))
                slot_data["keyblade_stats"] = slot_data["keyblade_stats"] + str(str_bonus) + "," + str(mag_bonus) + ","
            slot_data["keyblade_stats"] = slot_data["keyblade_stats"][:-1]

        if int(self.options.character) < 2:
            slot_data["play_destiny_islands"] = str(self.options.play_destiny_islands.value)
        else:
            slot_data["play_destiny_islands"] = "0"

        slot_data["skip_light_cycle"] = str(self.options.skip_light_cycle.value)
        slot_data["fast_go_mode"] = str(self.options.fast_go_mode.value)
        slot_data["exp_multiplier"] = int(self.options.exp_multiplier.value)
        slot_data["stat_bonus"] = int(self.options.stat_bonus.value)

        slot_data["recipe_reqs"] = int(self.options.recipe_reqs.value)
        slot_data["win_con"] = int(self.options.goal.value)

        slot_data["lord_kyroo"] = str(self.options.lord_kyroo.value)
        slot_data["local_item_notifs"] = str(self.options.received_notifications.value)
        slot_data["remote_item_notifs"] = str(self.options.sent_notifications.value)

        #For making items local
        slot_data["non_remote_ids"] = str(self.get_non_remote_ids())

        slot_data["use_vanilla_levels"] = int(self.using_vanilla_stats())

        slot_data["emblem_reqs"] = self.convert_required_emblems()

        return slot_data

    def get_non_remote_ids(self):
        non_remote_ids = []
        remote_categories = ["Trap", "Item"]
        remote_locations = ["Bonus"]

        for location in self.multiworld.get_filled_locations(self.player):
            if location.item.player == self.player:
                location_data = location_data_table[location.name]
                item_data = item_data_table[location.item.name]
                if location.item.name != "Victory" and item_data.category not in remote_categories:
                    #This is a local item
                    if location_data.category not in remote_locations: #Make sure game can award local item in this spot
                        if location.name == "The Grid Light Cycle Bonus Slot [Riku]" and self.options.skip_light_cycle: #This location cannot be local if the minigame is skipped
                            continue
                        non_remote_ids.append([location_data.code, item_data.code])
        return non_remote_ids

    def using_vanilla_stats(self):
        is_vanilla = 0
        if self.options.stats_on_levels == 3:
            is_vanilla = 1
        return is_vanilla

    def verify_emblems(self):
        emb_req = self.convert_required_emblems()
        return max(emb_req, int(self.options.emblems_in_pool.value))

    def convert_required_emblems(self):
        emb_req = int(self.options.emblem_reqs.value)
        if self.options.goal == 2 and emb_req == 0:
            emb_req = 1
        return emb_req