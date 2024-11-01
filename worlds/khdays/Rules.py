from typing import TYPE_CHECKING

import worlds.khdays.Items
import math
from BaseClasses import CollectionState, MultiWorld

from ..generic.Rules import add_rule, set_rule

from .Locations import location_table
from .Items import days, true_days, days_to_index
from .Options import KHDaysOptions

if TYPE_CHECKING:
    from . import KHDaysWorld

from ..AutoWorld import LogicMixin


def days_mission_to_day(mission_number: int):
    if mission_number >= 93:
        return days[92-1]
    return days[mission_number-1]


def days_day_to_mission(day_number_2: int):
    if day_number_2 >= 358:
        return days_to_index[357]+1
    return days_to_index[day_number_2]+1


def days_day_to_true_day(day_number_2: int):
    return true_days[days_day_to_mission(day_number_2)-1]


class KHDaysLogic(LogicMixin):

    def days_has_magic(self, state: CollectionState, player: int):
        return state.has_any({"Fire"}, player)

    def days_can_get_materials(self, state: CollectionState, material_name: str, player: int):
        if material_name == "Gold":
            return self.days_has_day_access(state, days_mission_to_day(73), player)
        if material_name == "Blazing Shard":
            return self.days_has_day_access(state, days_mission_to_day(6), player)
        if material_name == "Blazing Gem":
            return self.days_has_day_access(state, days_mission_to_day(51), player)
        if material_name == "Blazing Crystal":
            return self.days_has_day_access(state, days_mission_to_day(63), player)
        if material_name == "Frost Shard":
            return self.days_has_day_access(state, days_mission_to_day(21), player)
        if material_name == "Frost Gem":
            return self.days_has_day_access(state, days_mission_to_day(51), player)
        if material_name == "Frost Crystal":
            return self.days_has_day_access(state, days_mission_to_day(73), player)
        if material_name == "Lightning Shard":
            return self.days_has_day_access(state, days_mission_to_day(38), player)
        if material_name == "Lightning Gem":
            return self.days_has_day_access(state, days_mission_to_day(52), player)
        if material_name == "Lightning Crystal":
            return self.days_has_day_access(state, days_mission_to_day(77), player)
        if material_name == "Gust Shard":
            return self.days_has_day_access(state, days_mission_to_day(38), player)
        if material_name == "Gust Gem":
            return self.days_has_day_access(state, days_mission_to_day(62), player)
        if material_name == "Gust Crystal":
            return self.days_has_day_access(state, days_mission_to_day(73), player)
        if material_name == "Shining Shard":
            return self.days_has_day_access(state, days_mission_to_day(13), player)
        if material_name == "Shining Gem":
            return self.days_has_day_access(state, days_mission_to_day(53), player)
        if material_name == "Shining Crystal":
            return self.days_has_day_access(state, days_mission_to_day(73), player)
        if material_name == "Combo Tech":
            return self.days_has_day_access(state, days_mission_to_day(31), player)
        if material_name == "Combo Tech+":
            return self.days_has_day_access(state, days_mission_to_day(67), player)
        if material_name == "Combo Tech++":
            return self.days_has_day_access(state, days_mission_to_day(63), player)
        if material_name == "Power Tech":
            return self.days_has_day_access(state, days_mission_to_day(38), player)
        if material_name == "Power Tech+":
            return self.days_has_day_access(state, days_mission_to_day(58), player)
        if material_name == "Power Tech++":
            return self.days_has_day_access(state, days_mission_to_day(83), player)
        if material_name == "Moonstone":
            return self.days_has_day_access(state, 14, player)
        if material_name == "Premium Orb":
            return self.days_has_day_access(state, days_mission_to_day(73), player)
        if material_name == "Diamond":
            return self.days_has_day_access(state, days_mission_to_day(82), player)
        if material_name == "Range Tech":
            return self.days_has_day_access(state, days_mission_to_day(40), player)
        if material_name == "Range Tech+":
            return self.days_has_day_access(state, days_mission_to_day(63), player)
        if material_name == "Range Tech++":
            return self.days_has_day_access(state, days_mission_to_day(79), player)
        if material_name == "Adamantite":
            return self.days_has_day_access(state, days_mission_to_day(73), player)
        if material_name == "Combo Tech":
            return self.days_has_day_access(state, days_mission_to_day(29), player)
        if material_name == "Combo Tech+":
            return self.days_has_day_access(state, days_mission_to_day(67), player)
        if material_name == "Combo Tech++":
            return self.days_has_day_access(state, days_mission_to_day(63), player)
        if material_name == "Shield Tech":
            return self.days_has_day_access(state, days_mission_to_day(39), player)
        if material_name == "Shield Tech+":
            return self.days_has_day_access(state, days_mission_to_day(65), player)
        if material_name == "Shield Tech++":
            return self.days_has_day_access(state, days_mission_to_day(74), player)
        if material_name == "Aerial Tech":
            return self.days_has_day_access(state, days_mission_to_day(47), player)
        if material_name == "Aerial Tech+":
            return self.days_has_day_access(state, days_mission_to_day(65), player)
        if material_name == "Aerial Tech++":
            return self.days_has_day_access(state, days_mission_to_day(81), player)
        if material_name == "Luck Tech":
            return self.days_has_day_access(state, days_mission_to_day(77), player)
        if material_name == "Rune Tech":
            return self.days_has_day_access(state, days_mission_to_day(47), player)
        if material_name == "Rune Tech+":
            return self.days_has_day_access(state, days_mission_to_day(65), player)
        if material_name == "Rune Tech++":
            return self.days_has_day_access(state, days_mission_to_day(85), player)
        if material_name == "Gear Component A":
            return self.days_has_day_access(state, days_mission_to_day(36), player)
        if material_name == "Gear Component B":
            return self.days_has_day_access(state, days_mission_to_day(51), player)
        if material_name == "Gear Component C":
            return self.days_has_day_access(state, days_mission_to_day(62), player)
        if material_name == "Gear Component D":
            return self.days_has_day_access(state, days_mission_to_day(82), player)
        if material_name == "Dark Ingot":
            return self.days_has_day_access(state, days_mission_to_day(52), player)
        if material_name == "Bronze":
            return self.days_has_day_access(state, days_mission_to_day(49), player)
        if material_name == "Mithril":
            return self.days_has_day_access(state, days_mission_to_day(85), player)
        if material_name == "Silver":
            return self.days_has_day_access(state, days_mission_to_day(64), player)
        if material_name == "Orichalcum":
            return self.days_has_day_access(state, days_mission_to_day(82), player)
        if material_name == "Iron":
            return self.days_has_day_access(state, days_mission_to_day(16), player)
        if material_name == "Ankharite":
            return self.days_has_day_access(state, days_mission_to_day(73), player)
        print("not found: "+material_name)
        return False

    def days_levels_obtainable(self, state: CollectionState, player: int):
        obtainable = 0
        access_days = 0
        for day in days:
            if self.days_has_day_access(state, day, player):
                access_days += 1
        obtainable += math.floor(access_days / len(days) * 32)
        if self.days_challenges_completable(state, player) >= 90:
            obtainable += 1
        if self.days_challenges_completable(state, player) >= 140:
            obtainable += 1
        if self.days_challenges_completable(state, player) >= 210:
            obtainable += 1
        if self.days_challenges_completable(state, player) >= 230:
            obtainable += 1
        return obtainable

    def days_levels_reachable(self, state: CollectionState, player: int):
        has = state.count("Level Up", player)
        reached = 1
        if state.has("LV Quadrupler 3C", player):
            for i in range(2):
                if has > 0:
                    has -= 1
                    reached += 4
        if state.has("LV Quadrupler 3B", player):
            for i in range(2):
                if has > 0:
                    has -= 1
                    reached += 4
        if state.has("LV Quadrupler 3", player):
            for i in range(2):
                if has > 0:
                    has -= 1
                    reached += 4
        if state.has("LV Tripler 4C", player):
            for i in range(3):
                if has > 0:
                    has -= 1
                    reached += 3
        if state.has("LV Tripler 4B", player):
            for i in range(3):
                if has > 0:
                    has -= 1
                    reached += 3
        if state.has("LV Tripler 4", player):
            for i in range(3):
                if has > 0:
                    has -= 1
                    reached += 3
        if state.has("LV Doubler 6D", player):
            for i in range(5):
                if has > 0:
                    has -= 1
                    reached += 2
        if state.has("LV Doubler 6C", player):
            for i in range(5):
                if has > 0:
                    has -= 1
                    reached += 2
        if state.has("LV Doubler 6B", player):
            for i in range(5):
                if has > 0:
                    has -= 1
                    reached += 2
        if state.has("LV Doubler 6", player):
            for i in range(5):
                if has > 0:
                    has -= 1
                    reached += 2
        if state.has("LV Doubler 5", player):
            for i in range(4):
                if has > 0:
                    has -= 1
                    reached += 2
        reached += has
        has = 0
        return reached

    def days_crowns_obtainable(self, state: CollectionState, player: int):
        obtainable = 0
        if self.days_has_day_access(state, days_mission_to_day(93), player):
            obtainable += 1000
        return obtainable

    def days_challenges_completable(self, state: CollectionState, player: int):
        completable = 0
        if self.days_has_day_access(state, days_mission_to_day(93), player):
            completable += 1000
        return completable

    def days_has_day_access(self, state: CollectionState, day_number: int, player: int):
        if day_number <= 8:
            return True
        true_day = days_day_to_true_day(day_number)
        can_do = state.has("Day Unlock: "+str(true_day), player)
        can_do = can_do and self.day_logic(state, day_number, player)
        return can_do and self.day_logic(state, true_day, player)

    def day_logic(self, state: CollectionState, true_day: int, player: int):
        can_do = True
        if days_day_to_mission(true_day) >= 11:
            can_do = can_do and self.days_levels_reachable(state, player) >= math.floor((days_day_to_mission(true_day)-11) / 92 * 51)
        if days_day_to_mission(true_day) >= 28:
            can_do = can_do and state.has("Panel Slot", player, math.floor((days_day_to_mission(true_day)-28) / 92 * 30))
        if true_day == 193:
            can_do = can_do and state.has_any({"Glide 3", "Glide 5"}, player)
        if true_day == 11:
            can_do = can_do and self.days_has_magic(state, player)
        return can_do

    def days_shop_status(self, state: CollectionState, player: int):
        moogle_has_access = False
        for i in days:
            if i >= 26:
                moogle_has_access = moogle_has_access or self.days_has_day_access(state, i, player)
        if moogle_has_access:
            return state.count("Progressive Rank", player)
        return 0
        # if self.days_has_day_access(state, 358, player):
        #     return 6  # Legend
        # if self.days_has_day_access(state, 296, player):
        #     return 5  # Master
        # if self.days_has_day_access(state, 225, player):
        #     return 4  # Expert
        # if self.days_has_day_access(state, 172, player):
        #     return 3  # Agent
        # if self.days_has_day_access(state, 117, player):
        #     return 2  # Rookie
        # if self.days_has_day_access(state, 26, player):
        #     return 1  # Novice
        # return 0


def set_rules(world: MultiWorld, options: KHDaysOptions, player: int):
    for i in world.get_locations(player):
        if i.name.startswith("Mission "):
            set_rule(i, lambda state, i=i: state.days_has_day_access(state, days_mission_to_day(int(i.name.removeprefix("Mission ").split(":")[0])), player) and state.days_has_day_access(state, max(15, days_mission_to_day(int(i.name.removeprefix("Mission ").split(":")[0]))), player))
        else:
            set_rule(i, lambda state, i=i: state.days_has_day_access(state, 15, player))

    set_rule(world.get_location("Mission 1: Chest 1", player), lambda state: True)
    add_rule(world.get_location("Mission 15: Chest 3", player),
                 lambda state: state.has_any({"Glide 3", "Glide 5"}, player) or (
                             state.has("Air Slide 5", player) and state.has("Air Slide LV+", player, 2)))
    add_rule(world.get_location("Mission 16: Chest 3", player),
                 lambda state: state.has_any({"Glide 3", "Glide 5"}, player) or (
                             state.has("Air Slide 5", player) and state.has("Air Slide LV+", player, 2)))
    add_rule(world.get_location("Mission 19: Chest 1", player),
                 lambda state: state.has_any({"Glide 3", "Glide 5"}, player) or (
                             state.has("Air Slide 5", player) and state.has("Air Slide LV+", player, 2)))
    for i in range(93):
        set_rule(world.get_location("Mission "+str(i+1)+": Reward 1", player), lambda state, i=i: state.days_has_day_access(state, days_mission_to_day(i+1), player))
        set_rule(world.get_location("Mission "+str(i+1)+": Reward 2", player), lambda state, i=i: state.days_has_day_access(state, days_mission_to_day(i+1), player))

    for i in range(93):
        set_rule(world.get_location("Mission "+str(i+1)+": Full Clear", player), lambda state, i=i: state.days_has_day_access(state, max(15, days_mission_to_day(i+1)), player))
    add_rule(world.get_location("Mission 16: Full Clear", player), lambda state: True)  # look into the logic
    add_rule(world.get_location("Mission 9: Full Clear", player), lambda state: state.has("Level Up", player, 2))
    set_rule(world.get_location("Mission 1: Full Clear", player), lambda state: state.days_has_day_access(state, days_mission_to_day(1), player))
    set_rule(world.get_location("Mission 2: Full Clear", player), lambda state: state.days_has_day_access(state, days_mission_to_day(2), player))
    set_rule(world.get_location("Mission 4: Full Clear", player), lambda state: state.days_has_day_access(state, days_mission_to_day(4), player))
    set_rule(world.get_location("Mission 6: Full Clear", player), lambda state: state.days_has_day_access(state, days_mission_to_day(6), player))
    add_rule(world.get_location("Mission 20: Full Clear", player), lambda state: state.has_any({"Glide 3", "Glide 5"}, player) or (state.has("Air Slide 5", player) and state.has("Air Slide LV+", player, 4)))

    if options.RandomizeHubGifts:
        set_rule(world.get_location("Hub: LV Doubler 5 1", player), lambda state: state.days_has_day_access(state, 52, player))
        set_rule(world.get_location("Hub: Panacea 1", player), lambda state: state.days_has_day_access(state, 75, player))
        set_rule(world.get_location("Hub: Combo Tech 1", player), lambda state: state.days_has_day_access(state, 152, player))

    if options.RandomizeLevelRewards:
        for i in range(36):
            set_rule(world.get_location("Hub: Level Up "+str(i+1), player), lambda state, i=i: state.days_levels_obtainable(state, player) >= i+1)

    if options.RandomizeSynthesis:
        set_rule(world.get_location("Synthesis: Magic Ring 1", player), lambda state: state.days_shop_status(state, player) >= 1 and state.days_can_get_materials(state, "Moonstone", player) and state.days_can_get_materials(state, "Iron", player))
        set_rule(world.get_location("Synthesis: Fencer's Ring 1", player), lambda state: state.days_shop_status(state, player) >= 1 and state.days_can_get_materials(state, "Moonstone", player) and state.days_can_get_materials(state, "Iron", player) and state.days_can_get_materials(state, "Shining Shard", player))
        set_rule(world.get_location("Synthesis: Fire Charm 1", player), lambda state: state.days_shop_status(state, player) >= 1 and state.days_can_get_materials(state, "Moonstone", player) and state.days_can_get_materials(state, "Iron", player) and state.days_can_get_materials(state, "Blazing Shard", player) and state.days_can_get_materials(state, "Aerial Tech", player))
        for i in range(5):
            set_rule(world.get_location("Synthesis: Fire "+str(i+1), player), lambda state, i=i: state.days_shop_status(state, player) >= 1 and state.has("Fire Recipe", player, i+1) and state.days_can_get_materials(state, "Blazing Shard", player))
            set_rule(world.get_location("Synthesis: Limit Recharge " + str(i + 1), player),
                     lambda state, i=i: state.days_shop_status(state, player) >= 1 and state.days_can_get_materials(state, "Blazing Shard", player) and state.days_can_get_materials(state, "Shining Shard", player) and state.days_can_get_materials(state, "Moonstone", player))

    for i in range(5):
        set_rule(world.get_location("Moogle: Mega-Potion "+str(i+1), player), lambda state, i=i: state.days_shop_status(state, player) >= 5)
        set_rule(world.get_location("Moogle: Mega-Ether "+str(i+1), player), lambda state, i=i: state.days_shop_status(state, player) >= 5)
        set_rule(world.get_location("Moogle: Panacea "+str(i+1), player), lambda state, i=i: state.days_shop_status(state, player) >= 2)
        set_rule(world.get_location("Moogle: Adamantite "+str(i+1), player), lambda state, i=i: state.days_shop_status(state, player) >= 5)
    for i in range(10):
        set_rule(world.get_location("Moogle: Potion "+str(i+1), player), lambda state, i=i: state.days_shop_status(state, player) >= 1)
        set_rule(world.get_location("Moogle: Hi-Potion "+str(i+1), player), lambda state, i=i: state.days_shop_status(state, player) >= 3)
        set_rule(world.get_location("Moogle: Ether "+str(i+1), player), lambda state, i=i: state.days_shop_status(state, player) >= 2)
        set_rule(world.get_location("Moogle: Hi-Ether "+str(i+1), player), lambda state, i=i: state.days_shop_status(state, player) >= 3)
        set_rule(world.get_location("Moogle: Moonstone "+str(i+1), player), lambda state, i=i: state.days_shop_status(state, player) >= 1)
        set_rule(world.get_location("Moogle: Diamond "+str(i+1), player), lambda state, i=i: state.days_shop_status(state, player) >= 4)
    set_rule(world.get_location("Moogle: Panel Slot 1", player), lambda state: state.days_shop_status(state, player) >= 1)
    set_rule(world.get_location("Moogle: Panel Slot 2", player), lambda state: state.days_shop_status(state, player) >= 2)
    set_rule(world.get_location("Moogle: Panel Slot 3", player), lambda state: state.days_shop_status(state, player) >= 3)
    set_rule(world.get_location("Moogle: Panel Slot 4", player), lambda state: state.days_shop_status(state, player) >= 4)
    set_rule(world.get_location("Moogle: Panel Slot 5", player), lambda state: state.days_shop_status(state, player) >= 5)
    set_rule(world.get_location("Moogle: Panel Slot 6", player), lambda state: state.days_shop_status(state, player) >= 6)
    set_rule(world.get_location("Moogle: Panel Slot 7", player), lambda state: state.days_shop_status(state, player) >= 6)
    set_rule(world.get_location("Moogle: Aerial Recovery 1", player), lambda state: state.days_shop_status(state, player) >= 1)
    set_rule(world.get_location("Moogle: Power Unit 1", player), lambda state: state.days_shop_status(state, player) >= 1)
    set_rule(world.get_location("Moogle: Brawl Ring 1", player), lambda state: state.days_shop_status(state, player) >= 1)
    set_rule(world.get_location("Moogle: Level Up 1", player), lambda state: state.days_shop_status(state, player) >= 1)
    set_rule(world.get_location("Moogle: Level Up 2", player), lambda state: state.days_shop_status(state, player) >= 2)
    set_rule(world.get_location("Moogle: Level Up 3", player), lambda state: state.days_shop_status(state, player) >= 4)
    set_rule(world.get_location("Moogle: LV Quadrupler 3B 1", player), lambda state: state.days_shop_status(state, player) >= 6)
    set_rule(world.get_location("Moogle: Backpack 1", player), lambda state: state.days_shop_status(state, player) >= 2)
    set_rule(world.get_location("Moogle: Fire 1", player), lambda state: state.days_shop_status(state, player) >= 1)
    set_rule(world.get_location("Moogle: Fire 2", player), lambda state: state.days_shop_status(state, player) >= 2)
    set_rule(world.get_location("Moogle: Fira 1", player), lambda state: state.days_shop_status(state, player) >= 3)
    set_rule(world.get_location("Moogle: Fira 2", player), lambda state: state.days_shop_status(state, player) >= 3)
    set_rule(world.get_location("Moogle: Blizzard 1", player), lambda state: state.days_shop_status(state, player) >= 2)
    set_rule(world.get_location("Moogle: Blizzard 2", player), lambda state: state.days_shop_status(state, player) >= 2)
    set_rule(world.get_location("Moogle: Blizzara 1", player), lambda state: state.days_shop_status(state, player) >= 3)
    set_rule(world.get_location("Moogle: Blizzara 2", player), lambda state: state.days_shop_status(state, player) >= 3)
    set_rule(world.get_location("Moogle: Thunder 1", player), lambda state: state.days_shop_status(state, player) >= 2)
    set_rule(world.get_location("Moogle: Thunder 2", player), lambda state: state.days_shop_status(state, player) >= 2)
    set_rule(world.get_location("Moogle: Thundara 1", player), lambda state: state.days_shop_status(state, player) >= 4)
    set_rule(world.get_location("Moogle: Thundara 2", player), lambda state: state.days_shop_status(state, player) >= 4)
    set_rule(world.get_location("Moogle: Aero 1", player), lambda state: state.days_shop_status(state, player) >= 2)
    set_rule(world.get_location("Moogle: Aero 2", player), lambda state: state.days_shop_status(state, player) >= 2)
    set_rule(world.get_location("Moogle: Cure 1", player), lambda state: state.days_shop_status(state, player) >= 2)
    set_rule(world.get_location("Moogle: Cure 2", player), lambda state: state.days_shop_status(state, player) >= 2)
    set_rule(world.get_location("Moogle: Cura 1", player), lambda state: state.days_shop_status(state, player) >= 3)
    set_rule(world.get_location("Moogle: Cura 2", player), lambda state: state.days_shop_status(state, player) >= 3)
    set_rule(world.get_location("Moogle: Magic LV2 4B 1", player), lambda state: state.days_shop_status(state, player) >= 5)
    set_rule(world.get_location("Moogle: Magic LV2 4C 1", player), lambda state: state.days_shop_status(state, player) >= 2)
    set_rule(world.get_location("Moogle: Magic LV3 4 1", player), lambda state: state.days_shop_status(state, player) >= 3)
    set_rule(world.get_location("Moogle: Magic LV3 4B 1", player), lambda state: state.days_shop_status(state, player) >= 4)
    set_rule(world.get_location("Moogle: Triplecast 3 1", player), lambda state: state.days_shop_status(state, player) >= 1)
    set_rule(world.get_location("Moogle: Quadcast 3 1", player), lambda state: state.days_shop_status(state, player) >= 4)
    set_rule(world.get_location("Moogle: Dodge Roll LV+ 1", player), lambda state: state.days_shop_status(state, player) >= 3)
    set_rule(world.get_location("Moogle: Dodge Roll LV+ 2", player), lambda state: state.days_shop_status(state, player) >= 6)
    set_rule(world.get_location("Moogle: Block 4 1", player), lambda state: state.days_shop_status(state, player) >= 5)
    set_rule(world.get_location("Moogle: Block LV+ 1", player), lambda state: state.days_shop_status(state, player) >= 5)
    set_rule(world.get_location("Moogle: Block LV+ 2", player), lambda state: state.days_shop_status(state, player) >= 6)
    set_rule(world.get_location("Moogle: Aerial Recovery 1", player), lambda state: state.days_shop_status(state, player) >= 1)
    set_rule(world.get_location("Moogle: Aerial Recovery 3 1", player), lambda state: state.days_shop_status(state, player) >= 3)
    set_rule(world.get_location("Moogle: Air Slide LV+ 1", player), lambda state: state.days_shop_status(state, player) >= 5)
    set_rule(world.get_location("Moogle: Air Slide LV+ 2", player), lambda state: state.days_shop_status(state, player) >= 6)
    set_rule(world.get_location("Moogle: Glide LV+ 1", player), lambda state: state.days_shop_status(state, player) >= 4)
    set_rule(world.get_location("Moogle: High Jump LV+ 1", player), lambda state: state.days_shop_status(state, player) >= 5)
    set_rule(world.get_location("Moogle: High Jump LV+ 2", player), lambda state: state.days_shop_status(state, player) >= 6)
    set_rule(world.get_location("Moogle: Treasure Magnet 3 1", player), lambda state: state.days_shop_status(state, player) >= 4)
    set_rule(world.get_location("Moogle: Treasure Magnet LV+ 1", player), lambda state: state.days_shop_status(state, player) >= 5)
    set_rule(world.get_location("Moogle: Treasure Magnet LV+ 2", player), lambda state: state.days_shop_status(state, player) >= 5)
    set_rule(world.get_location("Moogle: Auto-Life 3 1", player), lambda state: state.days_shop_status(state, player) >= 2)
    set_rule(world.get_location("Moogle: Auto-Life LV+ 1", player), lambda state: state.days_shop_status(state, player) >= 3)
    set_rule(world.get_location("Moogle: Auto-Life LV+ 2", player), lambda state: state.days_shop_status(state, player) >= 5)
    set_rule(world.get_location("Moogle: Limit Boost 1", player), lambda state: state.days_shop_status(state, player) >= 3)
    set_rule(world.get_location("Moogle: Range Extender 1", player), lambda state: state.days_shop_status(state, player) >= 2)
    set_rule(world.get_location("Moogle: Auto-Lock 1", player), lambda state: state.days_shop_status(state, player) >= 3)
    set_rule(world.get_location("Moogle: Technical Gear 3 1", player), lambda state: state.days_shop_status(state, player) >= 1)
    set_rule(world.get_location("Moogle: Chrono Gear 3 1", player), lambda state: state.days_shop_status(state, player) >= 1)
    set_rule(world.get_location("Moogle: Lift Gear 3 1", player), lambda state: state.days_shop_status(state, player) >= 1)
    set_rule(world.get_location("Moogle: Nimble Gear 4 1", player), lambda state: state.days_shop_status(state, player) >= 2)
    set_rule(world.get_location("Moogle: Wild Gear 3 1", player), lambda state: state.days_shop_status(state, player) >= 1)
    set_rule(world.get_location("Moogle: Fearless Gear 3 1", player), lambda state: state.days_shop_status(state, player) >= 2)
    set_rule(world.get_location("Moogle: Prestige Gear 4 1", player), lambda state: state.days_shop_status(state, player) >= 3)
    set_rule(world.get_location("Moogle: Champion Gear+ 5 1", player), lambda state: state.days_shop_status(state, player) >= 5)
    set_rule(world.get_location("Moogle: Pandora's Gear 5 1", player), lambda state: state.days_shop_status(state, player) >= 6)
    set_rule(world.get_location("Moogle: Zero Gear 5 1", player), lambda state: state.days_shop_status(state, player) >= 6)
    set_rule(world.get_location("Moogle: Ability Unit 1", player), lambda state: state.days_shop_status(state, player) >= 2)
    set_rule(world.get_location("Moogle: Power Unit 1", player), lambda state: state.days_shop_status(state, player) >= 1)
    set_rule(world.get_location("Moogle: Power Unit 2", player), lambda state: state.days_shop_status(state, player) >= 3)
    set_rule(world.get_location("Moogle: Power Unit 3", player), lambda state: state.days_shop_status(state, player) >= 6)
    set_rule(world.get_location("Moogle: Magic Unit 1", player), lambda state: state.days_shop_status(state, player) >= 2)
    set_rule(world.get_location("Moogle: Magic Unit 2", player), lambda state: state.days_shop_status(state, player) >= 4)
    set_rule(world.get_location("Moogle: Magic Unit 3", player), lambda state: state.days_shop_status(state, player) >= 6)
    set_rule(world.get_location("Moogle: Guard Unit 1", player), lambda state: state.days_shop_status(state, player) >= 2)
    set_rule(world.get_location("Moogle: Guard Unit 2", player), lambda state: state.days_shop_status(state, player) >= 4)
    set_rule(world.get_location("Moogle: Guard Unit 3", player), lambda state: state.days_shop_status(state, player) >= 6)
    set_rule(world.get_location("Moogle: Brawl Ring 1", player), lambda state: state.days_shop_status(state, player) >= 1)
    set_rule(world.get_location("Moogle: Soldier Ring 1", player), lambda state: state.days_shop_status(state, player) >= 1)
    set_rule(world.get_location("Moogle: Flower Charm 1", player), lambda state: state.days_shop_status(state, player) >= 2)
    set_rule(world.get_location("Moogle: Blizzard Charm 1", player), lambda state: state.days_shop_status(state, player) >= 2)
    set_rule(world.get_location("Moogle: Knight's Defense 1", player), lambda state: state.days_shop_status(state, player) >= 3)
    set_rule(world.get_location("Moogle: Rainforce Ring 1", player), lambda state: state.days_shop_status(state, player) >= 3)
    set_rule(world.get_location("Moogle: Critical Ring 1", player), lambda state: state.days_shop_status(state, player) >= 4)
    set_rule(world.get_location("Moogle: Lucky Star 1", player), lambda state: state.days_shop_status(state, player) >= 5)
    set_rule(world.get_location("Moogle: Princess's Crown 1", player), lambda state: state.days_shop_status(state, player) >= 6)
    set_rule(world.get_location("Moogle: Deep Sky 1", player), lambda state: state.days_shop_status(state, player) >= 6)
    set_rule(world.get_location("Moogle: Critical Sun 1", player), lambda state: state.days_shop_status(state, player) >= 6)
    set_rule(world.get_location("Moogle: Iron 1", player), lambda state: state.days_shop_status(state, player) >= 1)
    set_rule(world.get_location("Moogle: Bronze 1", player), lambda state: state.days_shop_status(state, player) >= 2)
    set_rule(world.get_location("Moogle: Dark Ingot 1", player), lambda state: state.days_shop_status(state, player) >= 3)
    set_rule(world.get_location("Moogle: Silver 1", player), lambda state: state.days_shop_status(state, player) >= 4)
    set_rule(world.get_location("Moogle: Gold 1", player), lambda state: state.days_shop_status(state, player) >= 5)

    if options.RandomizeEmblems:
        pass


def set_completion_rules(world: MultiWorld, player: int):
    world.completion_condition[player] = lambda state, world=world: state.has("Memory Shard", player, world.worlds[player].options.ShardRequirement.value)
