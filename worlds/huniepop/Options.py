from dataclasses import dataclass

from Options import PerGameCommonOptions, Range, OptionSet


class enabled_girls(OptionSet):
    """girls enabled to be accessed NOTE kyu cannot be disabled"""
    display_name = "enabled girls"
    valid_keys = [
        "tiffany",
        "aiko",
        "kyanna",
        "audrey",
        "lola",
        "nikki",
        "jessie",
        "beli",
        "momo",
        "celeste",
        "venus"
    ]
    default = valid_keys.copy()

class starting_girls(Range):
    """number of girls you start unlocked"""
    display_name = "Girls Unlocked"
    range_start = 2
    range_end = 12
    default = 3

class puzzle_moves(Range):
    """number of moves you start the puzzles with"""
    display_name = "puzzle moves"
    range_start = 10
    range_end = 99
    default = 20

class puzzle_affection_base(Range):
    """the base affection you start the puzzles with"""
    display_name = "puzzle affection base"
    range_start = 1
    range_end = 5000
    default = 200

class puzzle_affection_add(Range):
    """affection added to base affection after every successful date capped at 999999"""
    display_name = "puzzle affection add"
    range_start = 10
    range_end = 500
    default = 100

class shop_items(Range):
    """number of archipelago items in the shop Note if there is not enough locations for items it will add shop locations to satisfy the locations needed, MAX is 494 so total locations isn't over 1000"""
    #"""DISABLED DOES NOTHING AT THE MOMENT"""
    display_name = "shop items"
    range_start = 0
    range_end = 494
    default = 0

class shop_item_cost(Range):
    """the cost of each arch item location in the shop"""
    display_name = "shop item cost"
    range_start = 100
    range_end = 50000
    default = 1000

class extra_gifts(Range):
    """number of extra gifts to add to the item pool"""
    display_name = "extra gifts"
    range_start = 0
    range_end = 10
    default = 0



@dataclass
class HPOptions(PerGameCommonOptions):
    enabled_girls: enabled_girls
    number_of_staring_girls: starting_girls
    number_shop_items: shop_items
    shop_item_cost: shop_item_cost
    number_extra_gifts: extra_gifts
    puzzle_moves: puzzle_moves
    puzzle_affection_base: puzzle_affection_base
    puzzle_affection_add: puzzle_affection_add
