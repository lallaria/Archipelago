from random import Random

import settings
import string
import typing

from BaseClasses import Item, Tutorial, ItemClassification
from .Items import item_table, faction_table, Wargroove2Item
from .Levels import Wargroove2Level, get_level_table, get_first_level, get_final_levels, region_names, FINAL_LEVEL_1, \
    FINAL_LEVEL_2, FINAL_LEVEL_3, FINAL_LEVEL_4, LEVEL_COUNT, FINAL_LEVEL_COUNT
from .Locations import location_table
from .Presets import wargroove2_option_presets
from .Regions import create_regions
from .Rules import set_rules
from worlds.AutoWorld import World, WebWorld
from .Options import wargroove2_options
from worlds.LauncherComponents import Component, components, Type, launch_subprocess


def launch_client():
    from .client import launch
    launch_subprocess(launch, name="Wargroove2Client")


components.append(Component("Wargroove 2 Client", "Wargroove2Client", func=launch_client, component_type=Type.CLIENT))


class Wargroove2Settings(settings.Group):
    class RootDirectory(settings.UserFolderPath):
        """
        Locate the Wargroove 2 root directory on your system.
        This is used by the Wargroove 2 client, so it knows where to send communication files to
        """
        description = "Wargroove 2 root directory"

    root_directory: RootDirectory = RootDirectory("C:/Program Files (x86)/Steam/steamapps/common/Wargroove 2")


class Wargroove2Web(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Wargroove 2 for Archipelago.",
        "English",
        "wargroove2_en.md",
        "wargroove2/en",
        ["Fly Sniper"]
    )]

    options_presets = wargroove2_option_presets


class Wargroove2World(World):
    """
    Command an army, in the sequel to the hit turn based strategy game Wargroove!
    """

    option_definitions = wargroove2_options
    settings: typing.ClassVar[Wargroove2Settings]
    game = "Wargroove 2"
    topology_present = True
    data_version = 1
    web = Wargroove2Web()
    level_list: [Wargroove2Level] = None
    first_level: Wargroove2Level = None
    final_levels: [Wargroove2Level] = None

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = location_table

    def _get_slot_data(self):
        return {
            'seed': "".join(
                self.random.choice(string.ascii_letters) for i in range(16)),
            'income_boost': self.options.income_boost.value,
            'commander_defense_boost': self.options.commander_defense_boost.value,
            'starting_groove_multiplier': self.options.groove_boost.value,
            'level_shuffle_seed': self.options.level_shuffle_seed.value,
            'can_choose_commander': self.options.commander_choice.value != 0,
            'final_levels': self.options.final_levels.value,
            'death_link': self.options.death_link.value == 1
        }

    def generate_early(self):
        # First level
        self.first_level = get_first_level(self.player)

        # Standard levels
        self.level_list = get_level_table(self.player)
        low_victory_checks_levels = list(level for level in self.level_list if level.low_victory_checks)
        high_victory_checks_levels = list(level for level in self.level_list if not level.low_victory_checks)
        if self.multiworld.level_shuffle_seed[self.player] == 0:
            random = self.multiworld.random
        else:
            random = Random(str(self.multiworld.level_shuffle_seed[self.player]))

        random.shuffle(low_victory_checks_levels)
        random.shuffle(high_victory_checks_levels)
        non_starting_levels = high_victory_checks_levels + low_victory_checks_levels[4:]
        random.shuffle(non_starting_levels)
        self.level_list = low_victory_checks_levels[0:4] + non_starting_levels

        # Final Levels
        self.final_levels = get_final_levels(self.player)
        final_levels_no_ocean = list(level for level in self.final_levels if not level.has_ocean)
        final_levels_ocean = list(level for level in self.final_levels if level.has_ocean)
        random.shuffle(final_levels_no_ocean)
        random.shuffle(final_levels_ocean)
        non_north_levels = final_levels_ocean + final_levels_no_ocean[1:]
        random.shuffle(non_north_levels)
        self.final_levels = final_levels_no_ocean[0:1] + non_north_levels

        # Selecting a random starting faction
        if self.multiworld.commander_choice[self.player] == 2:
            factions = [faction for faction in faction_table.keys() if faction != "Starter"]
            starting_faction = Wargroove2Item(self.multiworld.random.choice(factions) + ' Commanders', self.player)
            self.multiworld.push_precollected(starting_faction)

    def create_items(self):
        # Fill out our pool with our items from the item table
        pool = []
        precollected_item_names = {item.name for item in self.multiworld.precollected_items[self.player]}
        ignore_faction_items = self.multiworld.commander_choice[self.player] == 0
        for name, data in item_table.items():
            if data.code is not None and name not in precollected_item_names and \
                    not data.classification == ItemClassification.filler:
                if name.endswith(' Commanders') and ignore_faction_items:
                    continue
                item = Wargroove2Item(name, self.player)
                pool.append(item)

        for i in range(0, 5):
            pool.append(Wargroove2Item("Commander Defense Boost", self.player))
            pool.append(Wargroove2Item("Income Boost", self.player))

        # Matching number of unfilled locations with filler items
        total_locations = len(self.first_level.location_rules.keys())
        for level in self.level_list[0:LEVEL_COUNT]:
            total_locations += len(level.location_rules.keys())
        locations_remaining = total_locations - len(pool)
        while locations_remaining > 0:
            # Filling the pool equally with the groove boost
            pool.append(Wargroove2Item("Groove Boost", self.player))
            locations_remaining -= 1

        self.multiworld.itempool += pool

        victory = Wargroove2Item("Wargroove 2 Victory", self.player)
        for i in range(0, 4):
            final_level = self.final_levels[i]
            self.multiworld.get_location(final_level.victory_locations[0], self.player).place_locked_item(victory)
        # Placing victory event at final location
        self.multiworld.completion_condition[self.player] = lambda state: \
            state.has("Wargroove 2 Victory", self.player, self.multiworld.final_levels[self.player])

    def set_rules(self):
        set_rules(self.multiworld, self.level_list, self.first_level, self.final_levels, self.player)

    def create_item(self, name: str) -> Item:
        return Wargroove2Item(name, self.player)

    def create_regions(self):
        create_regions(self.multiworld, self.player, self.level_list, self.first_level, self.final_levels)

    def fill_slot_data(self) -> dict:
        slot_data = self._get_slot_data()
        for option_name in wargroove2_options:
            option = getattr(self.multiworld, option_name)[self.player]
            slot_data[option_name] = int(option.value)
        for i in range(0, min(LEVEL_COUNT, len(self.level_list))):
            slot_data[f"Level File #{i}"] = self.level_list[i].file_name
            slot_data[region_names[i]] = self.level_list[i].name
            for location_name in self.level_list[i].location_rules.keys():
                slot_data[location_name] = region_names[i]
        for i in range(0, FINAL_LEVEL_COUNT):
            slot_data[f"Final Level File #{i}"] = self.final_levels[i].file_name
        slot_data[FINAL_LEVEL_1] = self.final_levels[0].name
        for location_name in self.final_levels[0].location_rules.keys():
            slot_data[location_name] = FINAL_LEVEL_1
        slot_data[FINAL_LEVEL_2] = self.final_levels[1].name
        for location_name in self.final_levels[0].location_rules.keys():
            slot_data[location_name] = FINAL_LEVEL_2
        slot_data[FINAL_LEVEL_3] = self.final_levels[2].name
        for location_name in self.final_levels[0].location_rules.keys():
            slot_data[location_name] = FINAL_LEVEL_3
        slot_data[FINAL_LEVEL_4] = self.final_levels[3].name
        for location_name in self.final_levels[0].location_rules.keys():
            slot_data[location_name] = FINAL_LEVEL_4
        return slot_data

    def get_filler_item_name(self) -> str:
        return "Groove Boost"
