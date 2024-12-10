from dataclasses import dataclass
from Options import FreeText, PerGameCommonOptions, Visibility

class Inventory_List(FreeText):
    """JSON style list of items to replace default items
    Max 25 items (will be truncated)
    '["a","b","c","d","e","f","g"]'
    Quote style does matter!"""
    display_name = "Items"
    default = "[]"
    visibility = Visibility.template

class Progression_List(FreeText):
    """JSON style list of progression items to replace default progression items
    Max 3 items (will be truncated)
    '["a","b","c"]'
    Quote style does matter!"""
    display_name = "Progression Items"
    default = "[]"
    visibility = Visibility.template

class Filler_List(FreeText):
    """JSON style list of filler items to replace default filler items
    Max 3 items (will be truncated)
    '["a","b","c"]'
    Quote style does matter! """
    display_name = "Filler Items"
    default = "[]"
    visibility = Visibility.template

class Trap_List(FreeText):
    """JSON style list of trap items to replace default trap items
    Max 3 items (will be truncated)
    '["a","b","c"]'
    Quote style does matter! """
    display_name = "Trap Items"
    default = "[]"
    visibility = Visibility.template

class Location_List(FreeText):
    """JSON style list of locations to replace default locations
    Max 25 items (will be truncated)
    '["a","b","c","d","e","f","g"]'
    Quote style does matter! """
    display_name = "Location List"
    default = "[]"
    visibility = Visibility.template

class Progression_Location_List(FreeText):
    """JSON style list of progression locations to replace default progression locations
    Max 10 items (will be truncated)
    '["a","b","c","d","e","f","g"]'
    Quote style does matter! """
    display_name = "Progression Locations"
    default = "[]"
    visibility = Visibility.template

@dataclass
class ChatipelagoOptions(PerGameCommonOptions):
    Inventory_List: Inventory_List
    Progression_List: Progression_List
    Filler_List: Filler_List
    Trap_List: Trap_List
    Location_List: Location_List
    Progression_Location_List: Progression_Location_List
