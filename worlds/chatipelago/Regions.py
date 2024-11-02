from typing import NamedTuple, Optional

from BaseClasses import Location, Region

class ChatipelagoLoc(Location):
    game: str = "Chatipelago"

class ChatipelagoLocationData(NamedTuple):
    region: str
    address: Optional[int] = None

class ChatipelagoRegionData(NamedTuple):
    connecting_regions: list[str] = []

region_table: dict[str, list[str]] = {
    "Menu": [],
    "Chatroom": [
        "Treasure Chest",
        "Another Treasure Chest",
        "Yet Another Drawer",
        "One More Treasure Chest",
        "New Treasure Chest",
        "Another Chest of Treasure",
        "Yet Another Chest of Treasures",
        "One More Chest of Treasures",
        "Fresh Treasure Chest",
        "Another Hidden Treasure Chest",
        "Yet Another Hidden Treasure Chest",
        "Another Bounty Chest",
        "Second Treasure Chest",
        "Another Box of Treasure",
        "You Found a Treasure Chest",
        "Yet Another Vault of Treasure",
        "Treasure Chest Appears",
        "Different Treasure Chest",
        "Another Gold-Filled Chest",
        "Yet Another Trove of Treasure",
        "One More Chest Packed with Treasure",
        "Another Treasure Box",
        "Yet Another Container of Treasure",
        "Surprise Treasure Chest",
        "Another Loot Chest",
        "Another Wealth-Filled Chest",
        "New Cache of Treasure",
        "Yet Another Chest of Riches",
        "Another Glimmering Treasure Chest",
        "Wee Treasure Vault",
        "Dull Glittering Treasure Chest",
        "Another Box Overflowing with Treasure",
        "Girthy Unusually Shaped Box",
        "Yet Another Oddly Shaped Box",
        "Another Box with an Odd Shape",
        "Strange Shaped Box",
        "Another Uncommon Shaped Box",
        "Another Peculiarly Shaped Box",
        "An Oddly Formed Box",
        "Another Irregularly Shaped Box",
        "Another Strange Formed Box",
        "Yet Another Unconventionally Shaped Box",
        "Another Weirdly Shaped Box",
        "Another Box with Strange Shape",
        "Box of Odd Proportions",
        "Another Bizarre Drawer",
        "An Unusually Formed Box",
        "Yet Another Strangely Shaped Box",
        "Another Odd Formed Box",
        "Another Unusual Shaped Box",
        "Drawer with Peculiar Shape",
        "Another Quirkily Shaped Box",
        "Another Abnormally Shaped Box",
        "Box with an Irregular Shape",
        "Yet Another Uniquely Shaped Box",
        "Another Box with Curious Shape",
        "Another Awkward Drawer",
        "Box with an Odd Structure",
        "Another Eccentrically Shaped Box",
        "Yet Another Box of Strange Shape",
        "Box with Weird Form",
        "Another Box of Unusual Shape",
        "Cursed Drawer",
        "Somewhere Under Curse",
        "Land Cursed",
        "Lost Cursed Realm",
        "Drawer Where the Curse Lingers",
        "Trapped Cursed Spot",
        "Somewhere the Curse Holds",
        "Hidden Cursed Place",
        "Place Marked by Curse",
        "Somewhere with Dark Curse",
        "Shadows of Curse",
        "Somewhere Under Dark Curse",
        "Somewhere Cursed Beyond Redemption",
        "Lost Cursed Land",
        "Somewhere Under the Weight of Curse",
        "Place Cursed by Evil",
        "Cursed Territory",
        "Somewhere Haunted by Curse",
        "Somewhere With Vile Curse",
        "Cursed, Forsaken Place",
        "Cursed Location",
        "Grips of Curse",
        "Somewhere Bound by Curse",
        "Somewhere Touched by Curse",
        "Under a Cursed Spell",
        "Somewhere Cursed and Forgotten",
        "Realm Tainted by a Drawer",
        "Lost World Cursed by Fate",
        "Somewhere Doomed by Curse",
        "Some Ensnared Curse",
    ],
    "Trees": [
        "Oak Tree", ## All Trees are Priority & Progression and need logic
        "Colorful Maple Tree",
        "Hidden Cypress Tree",
        "High Cedar Tree",
        "Willow Tree",
        "Nestled Birch Tree",
        "Tucked Away Redwood Tree",
        "Cherry Blossom Tree",
        "Concealed Elm Tree",
        "Resting Aspen Tree"
    ]
}
chati_region_conn: dict[str, dict[str, str]] = {
    "Menu": {"Chatroom": "Start Game"},
    "Chatroom": {"Trees": "Fly"}
}

# Give the locations IDs, and the Tree locations meme IDs
location_data_table: dict[str, ChatipelagoLocationData] = {}
count = 0
for loc in region_table["Chatroom"]:
    location_data_table[loc] = ChatipelagoLocationData(
        region = "Chatroom",
        address = 100+count
    )
    count+=1
count = 0
for loc in region_table["Trees"]:
    location_data_table[loc] = ChatipelagoLocationData(
        region = "Trees",
        address = 600+count
    )
    count+=1
