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

class shop_items(Range):
    #"""number of archipelago items in the shop Note if there is not enough locations for items it will add shop locations to satisfy the locations needed, MAX is 494 so total locations isn't over 1000"""
    """DISABLED DOES NOTHING AT THE MOMENT"""
    display_name = "shop items"
    range_start = 0
    range_end = 0
    default = 0

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
    number_extra_gifts: extra_gifts