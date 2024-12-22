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
        "Pear Tree",
        "Bethlehem",
        "Rokefeller Center",
        "Christmas Markets",
        "Ski Lodge (Top of the Mountain)",
        "Stonehenge",
        "Ice Cavern",
        "Whoville",
        "Tinsel Town",
        "Jack Frost's Realm",
        "Mistletoe Mountain",
        "Candy Cane Lane",
        "Gingerbread Land",
        "Sugarplum Kingdom",
        "Toyland",
        "Land of Forgotten Toys",
        "Elflandia",
        "Aurora Grove",
        "Thornvale Hollow",
        "Tree Farm",
        "Ymir's Realm",
        "Whispering Wood",
        "Starshadow Forest",
        "34th Street",
        "FAO Schwarz",
        "Lights Festival",
        "Church (Offering Real Help)",
        "Park Ice Rink",
        "Fireside Couch",
        "Snow Tubing Park",
        "Polar Bear Den",
        "Cozy Mountain Lodge",
        "Scrooge's Office",
        "Nakatomi Plaza",
        "Hoth",
        "Frozen Wilds",
        "Santa's Workshop",
        "Someone's House With Christmas Lights and Music",
        "Christmastown",
        "Freezeey Peak",
    ],
    "Prog": [
        "\u2605AGDQ2025 Main Stage\u2605",
        "\u2605Tier 3 Subscriber Lounge\u2605",
        "\u2605The North Pole\u2605",
        "\u2605Ice Cap Zone\u2605",
        "\u2605Phendrana Drifts\u2605",
        "\u2605Home (With loved ones)\u2605",
        "\u2605Mount Lanayru\u2605",
        "\u2605Snowpeak Ruins\u2605",
        "\u2605Shiveria\u2605",
        "\u2605Cool, Cool Mountain\u2605"
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
