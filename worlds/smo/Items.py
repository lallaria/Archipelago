from BaseClasses import Item, ItemClassification
from .Locations import locations_table


class SMOItem(Item):
	game: str = "Super Mario Odyssey"
	kingdom : str
	moon_value : int

	def __init__(self, name : str, classification : ItemClassification, player : int,  kingdom : str, id : int):
		super().__init__( name, classification, id , player)
		self.kingdom = kingdom
		self.moon_value = 3 if self.name in multi_moons else 1

# def create_event(self, event: str) -> SMOItem:
# 	# while we are at it, we can also add a helper to create events
#     return SMOItem(event, ItemClassification.progression, self.player, "None", )

moon_item_table = locations_table

multi_moons = [
    "Multi Moon Atop the Falls"
	"Showdown on the Inverted Pyramid"
	"The Hole in the Desert"
	"Broodals Over the Lake"
    "Flower Thieves of Sky Garden"
	"Defend the Secret Flower Field!"
	"New Donk City's Pest Problem"
	"A Traditional Festival!"
	"The Bound Bowl Grand Prix"
	"The Glass Is Half Full!"
	"Big Pot on the Volcano: Dive In!"
	"Cookatiel Showdown!"
	"Battle with the Lord of Lightning!"
	"Showdown at Bowser's Castle"
	"Tussle in Tostarena: Rematch"
	"Struggle in Steam Gardens: Rematch"
	"Dust-Up in New Donk City: Rematch"
	"Battle in Bubblaine: Rematch"
	"Blowup at Mount Volbono: Rematch"
	"Rumble in Crumbleden: Rematch"
	"Arrival at Rabbit Ridge!"
	"Long Journey's End"
]

filler_item_table = {
    "Coins" : 9999
}

item_table = {
    **moon_item_table,
    **filler_item_table
}