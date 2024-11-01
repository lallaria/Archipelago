from typing import NamedTuple, Optional, Dict
from BaseClasses import Item, ItemClassification

class ChatipelagoItem(Item):
    game: str = "Chatipelago"

class ChatipelagoItemData(NamedTuple):
    code: Optional[int] = None
    classification: ItemClassification = ItemClassification.useful

item_table = [
    "Adam's Couch",
    "Red M&M",
    "VTuber",
    "Cappy",
    "Hazard, Eating a Cookie bbirbNom",
    "Abandoned Sphere 0 Check",
    "Speedrunners & Dragons Official Dice Tower",
    "Rubber Band",
    "Dangers' Progressive Key",
    "Nothing bbirbSus",
    "DICKS",
    "GDQ Hat",
    "Link's Bokoblin Mask",
    "Unregulated Capitalism",
    "Level 5 Hype Train",
    "A Vallu Dive",
    "Super Mario Sunshine Disc",
    "A Goose Doing the Griddy",
    "!quote 180",
    "Frog With Heart on Their Butt",
    "Dangers' Last Input",
    "Perish Song",
    "wideVIBE",
    "An Amiibo of Wario Scratching his Butt",
    "My Peanits",
    "TITS",
    "ImagineBeingAMobileViewerThatCouldNotBeMeLMAOHowSillyAnywayLookAtThisCoolStarIFound",
    "Murder Mittens the Stray Cat",
    "Two Tickets to a Furcon",
    "(1) Whole Ass Meal",
    "https://www.twitch.tv/dangers/clip/YawningInnocentGaurSMOrc",
    "A Framed Unban Request",
    "Someone Who Went Out For A Rip",
    "Formosa Chipotle Hot Sauce",
    "Hol\u00E9 Mol\u00E9",
    "708 7 Pot Citrus Hot Sauce",
    "FirstTimeChadder",
    "A Panda",
    "Fursuit",
    "A Lisa Frank Trapper Keeper",
    "My Sonic OC (DO NOT STEAL)",
    "AAAA",
    "Magpie Cooperation", #Magpie is required logic for Progression Region
    "Magpie Boldness",
    "Magpie Treasure"
    ]

item_data_table = Dict[str, ChatipelagoItemData]
for item in item_table:
    item_data_table[item] = ChatipelagoItemData(
        code=100+len(item_data_table)
    )

# stuff that can be duplicated to fill in extras
filler_list = [
    "Drinking Water"
    "Sunflower Seeds"
    "The Top of the Hour Ad Break"
    "Set of Broken Joycons"
    ]