from ..generic.Rules import add_rule, set_rule, forbid_item, add_item_rule
from BaseClasses import MultiWorld
from .Locations import locations_table
from .Options import SMOOptions

def set_rules(self, options : SMOOptions) -> None:

    # place "Victory" at Lake Multimoon and set collection as win condition

    if options.goal == "lake":
        self.multiworld.get_location("Broodals Over the Lake", self.player).place_locked_item(self.create_item("Beat the Game"))
    if options.goal == "metro":
        self.multiworld.get_location("A Traditional Festival!", self.player).place_locked_item(self.create_item("Beat the Game"))
    if options.goal == "luncheon":
        self.multiworld.get_location("Cookatiel Showdown!", self.player).place_locked_item(self.create_item("Beat the Game"))
    if options.goal == "moon":
        self.multiworld.get_location("Beat the Game", self.player).place_locked_item(self.create_item("Beat the Game"))
    if options.goal == "dark":
        self.multiworld.get_location("Arrival at Rabbit Ridge", self.player).place_locked_item(self.create_item("Beat the Game"))
    if options.goal == "darker":
        self.multiworld.get_location("A Long Journey's End!", self.player).place_locked_item(self.create_item("Beat the Game"))

    # Prevents a softlock in Bowser from not having this moon in the moon list
    self.multiworld.get_location("Big Broodal Battle" , self.player).place_locked_item(self.create_item("Big Broodal Battle"))




# for debugging purposes, you may want to visualize the layout of your world. Uncomment the following code to
# write a PlantUML diagram to the file "my_world.puml" that can help you see whether your regions and locations
# are connected and placed as desired
# from Utils import visualize_regions
# visualize_regions(self.multiworld.get_region("Menu", self.player), "my_world.puml")
