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
        "The Hidden Flame Tavern",
        "Fading Ember Forge",
        "Underground Gallery 56",
        "The Broken Star Pub",
        "The Cloak Room",
        "Shake Your Tailfeathers Hall",
        "Cloudchaser Inn",
        "Sunspire Aviary",
        "Whispering Winds Market",
        "Beast Beat Club",
        "Critter Carnival",
        "Pride Paws Park",
        "Fursona Studios",
        "Flufftail Forest",
        "Howl & Roar Arcade",
        "Whiskers & Claws Spa",
        "The Bear's Den",
        "The Furred Haven Caf\u00E9",
        "Radiant Cinema",
        "Aurora Dance Studio",
        "Unity Gym",
        "Sapphire Shores Beach Club",
        "The Ally Alley",
        "The Velvet Underground",
        "Equality Park",
        "Celestial Glow Spa",
        "Colors Caf\u00E9 & Bakery",
        "The Quirk Collective",
        "Spectrum Arcade",
        "Pride Plaza",
        "Queertopia",
        "Phoenix Fire Tattoo Parlor",
        "Crimson Dawn Bridge",
        "Emberwood Refuge",
        "Veiled Vein Tunnel",
        "Windswept Hilltop",
        "The Golden Paw Lodge",
        "Feathers & Fins Falls",
        "Wild Whiskers Motel",
        "Moonlit Meadows",
    ],
    "Prog": [
        "\u2605SGDQ Main Stage\u2605",
        "\u2605Tier 3 Subscriber Lounge\u2605",
        "\u2605The Elite 4\u2605",
        "\u2605Ganondorf's Music Room\u2605",
        "\u2605Samus' Ship\u2605",
        "\u2605Bowser's Hot Tub\u2605",
        "\u2605Epona's Field\u2605",
        "\u2605The Odyssey\u2605",
        "\u2605Adam's Couch\u2605",
        "\u2605Delilah's Basement\u2605"
    ]
}
chati_region_conn: dict[str, dict[str, str]] = {
    "Menu": {"Chatroom": "Start Game"},
    "Chatroom": {"Prog": "Fight"}
}

#Give everything an ID
location_data_table: dict[str, ChatipelagoLocationData] = {}
count = 0
for loc in region_table["Chatroom"]:
    location_data_table[loc] = ChatipelagoLocationData(
        region = "Chatroom",
        address = 100+count
    )
    count+=1
count = 0
for loc in region_table["Prog"]:
    location_data_table[loc] = ChatipelagoLocationData(
        region = "Prog",
        address = 600+count
    )
    count+=1
