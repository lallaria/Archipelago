from typing import Callable, Dict, NamedTuple, Optional, Set, TYPE_CHECKING
import typing

from BaseClasses import Location

if TYPE_CHECKING:
    from . import KHDDDWorld

class KHDDDLocation(Location):
    game = "Kingdom Hearts Dream Drop Distance"

class KHDDDLocationData(NamedTuple):
    region: str
    code: int
    category: str = "Chest"

def get_locations_by_region(region: str) -> Dict[str, KHDDDLocationData]:
    location_dict: Dict[str, KHDDDLocationData] = {}
    for name, data in location_data_table.items():
        if data.region == region:
            location_dict.setdefault(name, data)

    return location_dict

def get_location_type(loc_code:int):
    for name, data in location_data_table.items():
        if data.code == loc_code:
            return data.category
    return "None"

def get_locations_by_category(category: str) -> Dict[str, KHDDDLocationData]:
    location_dict: Dict[str, KHDDDLocationData] = {}
    for name, data in location_data_table.items():
        if data.category == category:
            location_dict.setdefault(name, data)

    return location_dict

def get_location_name(loc_code:int) -> str:
    for name, data in location_data_table.items():
        if data.code == loc_code:
            return name
    return ""

def get_location_id(loc_name:str) -> int:
    return location_data_table[loc_name].code

location_data_table: Dict[str, KHDDDLocationData] = {
    ########################################
    ###########Secret Portals###############
    ########################################
    "Traverse Town Secret Portal [Sora]": KHDDDLocationData(
        region="Traverse Town [Sora]",
        code=2680201,
        category="Portal"
    ),
    "Traverse Town Secret Portal [Riku]": KHDDDLocationData(
        region="Traverse Town [Riku]",
        code=2680202,
        category="Portal"
    ),

    "La Cite des Cloches Secret Portal [Sora]": KHDDDLocationData(
        region="La Cite des Cloches [Sora]",
        code=2680203,
        category="Portal"
    ),
    "La Cite des Cloches Secret Portal [Riku]": KHDDDLocationData(
        region="La Cite des Cloches [Riku]",
        code=2680204,
        category="Portal"
    ),

    "The Grid Secret Portal [Sora]": KHDDDLocationData(
        region="The Grid [Sora]",
        code=2680205,
        category="Portal"
    ),
    "The Grid Secret Portal [Riku]": KHDDDLocationData(
        region="The Grid [Riku]",
        code=2680206,
        category="Portal"
    ),

    "Prankster's Paradise Secret Portal [Sora]": KHDDDLocationData(
        region="Prankster's Paradise [Sora]",
        code=2680207,
        category="Portal"
    ),
    "Prankster's Paradise Secret Portal [Riku]": KHDDDLocationData(
        region="Prankster's Paradise [Riku]",
        code=2680208,
        category="Portal"
    ),

    "Country of the Musketeers Secret Portal [Sora]": KHDDDLocationData(
        region="Country of the Musketeers [Sora]",
        code=2680209,
        category="Portal"
    ),
    "Country of the Musketeers Secret Portal [Riku]": KHDDDLocationData(
        region="Country of the Musketeers [Riku]",
        code=2680210,
        category="Portal"
    ),

    "Symphony of Sorcery Secret Portal [Sora]": KHDDDLocationData(
        region="Symphony of Sorcery [Sora]",
        code=2680211,
        category="Portal"
    ),

    "Unbound Keyblade Reward [Sora]": KHDDDLocationData(
        region="World Map [Sora]",
        code = 2680212,
        category="Reward"
    ),

    "Unbound Keyblade Reward [Riku]": KHDDDLocationData(
        region="World Map [Riku]",
        code = 2680213,
        category="Reward"
    ),

    ########################################
    #############Sora Events################
    ########################################
    "Destiny Islands Ursula Bonus Slot 1 [Sora]": KHDDDLocationData(
        region="Destiny Islands",
        code=2670201,
        category="Slot"
    ),
    "Destiny Islands Flashback: The Mark of Mastery Exam Reward [Sora]": KHDDDLocationData(
        region="Destiny Islands",
        code=2670202,
        category="Reward"
    ),
    "Destiny Islands Glossary: Keyblades Reward [Sora]": KHDDDLocationData(
        region="Destiny Islands",
        code=2670203,
        category="Reward"
    ),
    "Destiny Islands Glossary: Keyblade Masters Reward [Sora]": KHDDDLocationData(
        region="Destiny Islands",
        code=2670204,
        category="Reward"
    ),
    "Destiny Islands Glossary: Master Xehanort Reward [Sora]": KHDDDLocationData(
        region="Destiny Islands",
        code=2670205,
        category="Reward"
    ),

    "Traverse Town Flashback: Dream Eaters Reward [Sora]": KHDDDLocationData(
        region="Traverse Town [Sora]",
        code=2670206,
        category="Reward"
    ),
    "Traverse Town Glossary: Heartless Reward [Sora]": KHDDDLocationData(
        region="Traverse Town [Sora]",
        code=2670207,
        category="Reward"
    ),
    "Traverse Town Hockomonkey Bonus Slot 1 [Sora]": KHDDDLocationData(
        region="Traverse Town [Sora]",
        code=2670211,
        category="Slot"
    ),
    "Traverse Town Hockomonkey Bonus Slot 2 [Sora]": KHDDDLocationData(
        region="Traverse Town [Sora]",
        code=2670212,
        category="Slot"
    ),
    "Traverse Town Skull Noise Reward [Sora]": KHDDDLocationData(
        region="Traverse Town [Sora]",
        code=2670213,
        category="Reward"
    ),
    "La Cite des Cloches Zolephant Recipe Reward [Sora]": KHDDDLocationData(
        region="La Cite des Cloches [Sora]",
        code=2670214,
        category="Reward"
    ),
    "La Cite des Cloches Flashback: Frollo Warns Quasimodo Reward [Sora]": KHDDDLocationData(
        region="La Cite des Cloches [Sora]",
        code=2670215,
        category="Reward"
    ),
    "La Cite des Cloches Flower Fight Bonus Slot 1 [Sora]": KHDDDLocationData(
        region="La Cite des Cloches [Sora]",
        code=2670216,
        category="Slot"
    ),
    "La Cite des Cloches Wargoyle Bonus Slot 1 [Sora]": KHDDDLocationData(
        region="La Cite des Cloches [Sora]",
        code=2670217,
        category="Slot"
    ),
    "La Cite des Cloches Guardian Bell Reward [Sora]": KHDDDLocationData(
        region="La Cite des Cloches [Sora]",
        code=2670218,
        category="Reward"
    ),
    "La Cite des Cloches Chronicle BBS Reward [Sora]": KHDDDLocationData(
        region="La Cite des Cloches [Sora]",
        code=2670219,
        category="Reward"
    ),
    "The Grid Counter Rush Reward [Sora]": KHDDDLocationData(
        region="The Grid [Sora]",
        code=2670220,
        category="Reward"
    ),
    "The Grid Rinzler Bonus Slot 1 [Sora]": KHDDDLocationData(
        region="The Grid [Sora]",
        code=2670221,
        category="Slot"
    ),
    "The Grid Rinzler Bonus Slot 2 [Sora]": KHDDDLocationData(
        region="The Grid [Sora]",
        code=2670222,
        category="Slot"
    ),
    "The Grid Dual Disc Reward [Sora]": KHDDDLocationData(
        region="The Grid [Sora]",
        code=2670223,
        category="Reward"
    ),
    "Prankster's Paradise Flashback: When World's Dream Reward [Sora]": KHDDDLocationData(
        region="Prankster's Paradise [Sora]",
        code=2670224,
        category="Reward"
    ),
    "Prankster's Paradise Flashback: Pinocchio Lies Reward [Sora]": KHDDDLocationData(
        region="Prankster's Paradise [Sora]",
        code=2670225,
        category="Reward"
    ),
    "Prankster's Paradise Found Pinocchio HP Bonus [Sora]": KHDDDLocationData(
        region="Prankster's Paradise [Sora]",
        code=2670226,
        category="Slot"
    ),
    "Prankster's Paradise Jestabocky Recipe Reward [Sora]": KHDDDLocationData(
        region="Prankster's Paradise [Sora]",
        code=2670227,
        category="Reward"
    ),
    "Prankster's Paradise High Jump Reward [Sora]": KHDDDLocationData(
        region="Prankster's Paradise [Sora]",
        code=2670228,
        category="Reward"
    ),
    "Prankster's Paradise Glossary: Nobodies Reward [Sora]": KHDDDLocationData(
        region="Prankster's Paradise [Sora]",
        code=2670229,
        category="Reward"
    ),
    "Prankster's Paradise Glossary: Organization XIII Reward [Sora]": KHDDDLocationData(
        region="Prankster's Paradise [Sora]",
        code=2670230,
        category="Reward"
    ),
    "Prankster's Paradise Chronicle: KH2 Reward [Sora]": KHDDDLocationData(
        region="Prankster's Paradise [Sora]",
        code=2670231,
        category="Reward"
    ),
    "Prankster's Paradise Flashback: In Search of Monstro Reward [Sora]": KHDDDLocationData(
        region="Prankster's Paradise [Sora]",
        code=2670232,
        category="Reward"
    ),
    "Prankster's Paradise Chill Clawbster Bonus Slot 1 [Sora]": KHDDDLocationData(
        region="Prankster's Paradise [Sora]",
        code=2670233,
        category="Slot"
    ),
    "Prankster's Paradise Ferris Gear Reward [Sora]": KHDDDLocationData(
        region="Prankster's Paradise [Sora]",
        code=2670234,
        category="Reward"
    ),
    "Country of the Musketeers Flashback: Overnight Musketeers Reward [Sora]": KHDDDLocationData(
        region="Country of the Musketeers [Sora]",
        code=2670235,
        category="Reward"
    ),
    "Country of the Musketeers Tyranto Rex Recipe Reward [Sora]": KHDDDLocationData(
        region="Country of the Musketeers [Sora]",
        code=2670236,
        category="Reward"
    ),
    "Country of the Musketeers Slide Roll Reward [Sora]": KHDDDLocationData(
        region="Country of the Musketeers [Sora]",
        code=2670237,
        category="Reward"
    ),
    "Country of the Musketeers Pete Bonus Slot 1 [Sora]": KHDDDLocationData(
        region="Country of the Musketeers [Sora]",
        code=2670238,
        category="Slot"
    ),
    "Country of the Musketeers All For One Reward [Sora]": KHDDDLocationData(
        region="Country of the Musketeers [Sora]",
        code=2670239,
        category="Reward"
    ),
    "Symphony of Sorcery Flashback: Sorcerer's Apprentice Reward [Sora]": KHDDDLocationData(
        region="Symphony of Sorcery [Sora]",
        code=2670240,
        category="Reward"
    ),
    "Symphony of Sorcery Double Impact Reward [Sora]": KHDDDLocationData(
        region="Symphony of Sorcery [Sora]",
        code=2670241,
        category="Reward"
    ),
    "Symphony of Sorcery Spellican Bonus Slot 1 [Sora]": KHDDDLocationData(
        region="Symphony of Sorcery [Sora]",
        code=2670242,
        category="Slot"
    ),
    "Symphony of Sorcery Spellican Bonus Slot 2 [Sora]": KHDDDLocationData(
        region="Symphony of Sorcery [Sora]",
        code=2670243,
        category="Slot"
    ),
    "Symphony of Sorcery Counterpoint Reward [Sora]": KHDDDLocationData(
        region="Symphony of Sorcery [Sora]",
        code=2670244,
        category="Reward"
    ),
    "The World That Never Was Xemnas Bonus Slot 1 [Sora]": KHDDDLocationData(
        region="The World That Never Was [Sora]",
        code=2670245,
        category="Slot"
    ),
    "The World That Never Was Glossary: Recusant's Sigil Reward [Sora]": KHDDDLocationData(
        region="The World That Never Was [Sora]",
        code=2670246,
        category="Reward"
    ),
    "The World That Never Was Glossary: Hearts Tied to Sora Reward [Sora]": KHDDDLocationData(
        region="The World That Never Was [Sora]",
        code=2670247,
        category="Reward"
    ),
    "Traverse Town Meow Wow Recipe Reward [Sora]": KHDDDLocationData(
        region="Traverse Town [Sora]",
        code=2670248,
        category="Reward"
    ),

    ########################################
    #############Riku Events################
    ########################################
    "Traverse Town Komory Bat Recipe Reward [Riku]": KHDDDLocationData(
        region="Traverse Town [Riku]",
        code=2670249,
        category="Reward"
    ),
    "Traverse Town Flashback: Keyblade War Reward [Riku]": KHDDDLocationData(
        region="Traverse Town [Riku]",
        code=2670250,
        category="Reward"
    ),
    "Traverse Town Glossary: Keyblade War Reward [Riku]": KHDDDLocationData(
        region="Traverse Town [Riku]",
        code=2670251,
        category="Reward"
    ),
    "Traverse Town Glossary: Kingdom Hearts Reward [Riku]": KHDDDLocationData(
        region="Traverse Town [Riku]",
        code=2670252,
        category="Reward"
    ),
    "Traverse Town Glossary: Keyblade Reward [Riku]": KHDDDLocationData(
        region="Traverse Town [Riku]",
        code=2670253,
        category="Reward"
    ),
    "Traverse Town Rescue Shiki Bonus Slot [Riku]": KHDDDLocationData(
        region="Traverse Town [Riku]",
        code=2670254,
        category="Slot"
    ),
    "Traverse Town Hockomonkey Bonus Slot 1 [Riku]": KHDDDLocationData(
        region="Traverse Town [Riku]",
        code=2670255,
        category="Slot"
    ),
    "Traverse Town Hockomonkey Bonus Slot 2 [Riku]": KHDDDLocationData(
        region="Traverse Town [Riku]",
        code=2670256,
        category="Slot"
    ),
    "Traverse Town Skull Noise Reward [Riku]": KHDDDLocationData(
        region="Traverse Town [Riku]",
        code=2670257,
        category="Reward"
    ),
    "La Cite des Cloches Flashback: Dark Obsession Reward [Riku]": KHDDDLocationData(
        region="La Cite des Cloches [Riku]",
        code=2670258,
        category="Reward"
    ),
    "La Cite des Cloches Sonic Impact Reward [Riku]": KHDDDLocationData(
        region="La Cite des Cloches [Riku]",
        code=2670259,
        category="Reward"
    ),
    "La Cite des Cloches Wargoyle Bonus Slot 1 [Riku]": KHDDDLocationData(
        region="La Cite des Cloches [Riku]",
        code=2670260,
        category="Slot"
    ),
    "La Cite des Cloches Wargoyle Bonus Slot 2 [Riku]": KHDDDLocationData(
        region="La Cite des Cloches [Riku]",
        code=2670261,
        category="Slot"
    ),
    "La Cite des Cloches Chronicle: Kingdom Hearts Reward [Riku]": KHDDDLocationData(
        region="La Cite des Cloches [Riku]",
        code=2670262,
        category="Reward"
    ),
    "La Cite des Cloches Guardian Bell Reward [Riku]": KHDDDLocationData(
        region="La Cite des Cloches [Riku]",
        code=2670263,
        category="Reward"
    ),
    "The Grid Light Cycle Bonus Slot [Riku]": KHDDDLocationData(
        region="The Grid [Riku]",
        code=2670264,
        category="Slot"
    ),
    "The Grid Flashback: Father and Son Reward [Riku]": KHDDDLocationData(
        region="The Grid [Riku]",
        code=2670265,
        category="Reward"
    ),
    "The Grid City Dream Eater Fight Bonus Slot [Riku]": KHDDDLocationData(
        region="The Grid [Riku]",
        code=2670266,
        category="Slot"
    ),
    "The Grid Flashback: Stolen Disk Reward [Riku]": KHDDDLocationData(
        region="The Grid [Riku]",
        code=2670267,
        category="Reward"
    ),
    "The Grid Commantis Bonus Slot 1 [Riku]": KHDDDLocationData(
        region="The Grid [Riku]",
        code=2670268,
        category="Slot"
    ),
    "The Grid Dual Disc Reward [Riku]": KHDDDLocationData(
        region="The Grid [Riku]",
        code=2670269,
        category="Reward"
    ),
    "Prankster's Paradise Chronicle: Chain of Memories Reward [Riku]": KHDDDLocationData(
        region="Prankster's Paradise [Riku]",
        code=2670270,
        category="Reward"
    ),
    "Prankster's Paradise Char Clobster Bonus Slot 1 [Riku]": KHDDDLocationData(
        region="Prankster's Paradise [Riku]",
        code=2670271,
        category="Slot"
    ),
    "Prankster's Paradise Ocean's Rage Reward [Riku]": KHDDDLocationData(
        region="Prankster's Paradise [Riku]",
        code=2670272,
        category="Reward"
    ),
    "Country of the Musketeers Flashback: Bon Journey Reward [Riku]": KHDDDLocationData(
        region="Country of the Musketeers [Riku]",
        code=2670273,
        category="Reward"
    ),
    "Country of the Musketeers Stage Gadget Reward [Riku]": KHDDDLocationData(
        region="Country of the Musketeers [Riku]",
        code=2670274,
        category="Bonus" #Player gets rewarded the stage gadget here as well, so extra item is a bonus
    ),
    "Country of the Musketeers Holey Moley Bonus Slot 1 [Riku]": KHDDDLocationData(
        region="Country of the Musketeers [Riku]",
        code=2670275,
        category="Slot"
    ),
    "Country of the Musketeers Shadow Slide Reward [Riku]": KHDDDLocationData(
        region="Country of the Musketeers [Riku]",
        code=2670276,
        category="Reward"
    ),
    "Country of the Musketeers Shadow Strike Reward [Riku]": KHDDDLocationData(
        region="Country of the Musketeers [Riku]",
        code=2670277,
        category="Reward"
    ),
    "Country of the Musketeers All For One Reward [Riku]": KHDDDLocationData(
        region="Country of the Musketeers [Riku]",
        code=2670278,
        category="Reward"
    ),
    "Symphony of Sorcery Flashback: A Magical Mishap Reward [Riku]": KHDDDLocationData(
        region="Symphony of Sorcery [Riku]",
        code=2670279,
        category="Reward"
    ),
    "Symphony of Sorcery Chernobog Bonus Slot 1 [Riku]": KHDDDLocationData(
        region="Symphony of Sorcery [Riku]",
        code=2670280,
        category="Slot"
    ),
    "Symphony of Sorcery Chernobog Bonus Slot 2 [Riku]": KHDDDLocationData(
        region="Symphony of Sorcery [Riku]",
        code=2670281,
        category="Slot"
    ),
    "Symphony of Sorcery Counterpoint Reward [Riku]": KHDDDLocationData(
        region="Symphony of Sorcery [Riku]",
        code=2670282,
        category="Reward"
    ),
    "The World That Never Was Ansem II Defeated [Riku]": KHDDDLocationData(
        region="The World That Never Was [Riku]",
        code=2670283,
        category="Slot" #This was previously a bonus; genned seeds might treat it as such
    ),
    "The World That Never Was Young Xehanort Defeated [Riku]": KHDDDLocationData(
        region="The World That Never Was [Riku]",
        code=2670284,
        category="Bonus"
    ),
    "Armored Ventus Nightmare Defeated [Riku]": KHDDDLocationData(
        region="The World That Never Was [Riku]",
        code=2670295,
        category="Bonus"
    ),
    "The World That Never Was Ansem I Defeated [Riku]": KHDDDLocationData(
        region="The World That Never Was [Riku]",
        code=2670296,
        category="Bonus"
    ),
    "The World That Never Was Anti Black Coat Nightmare Defeated [Riku]": KHDDDLocationData(
        region="The World That Never Was [Riku]",
        code=2670297,
        category="Bonus"
    ),

    ########################################
    #############TT2 Rewards################
    ########################################
    "Traverse Town 2 Sliding Sidewinder Reward [Sora]": KHDDDLocationData(
        region="Traverse Town 2 [Sora]",
        code=2670285,
        category="Reward"
    ),
    "Traverse Town 2 Knockout Punch Reward [Sora]": KHDDDLocationData(
        region="Traverse Town 2 [Sora]",
        code=2670286,
        category="Reward"
    ),
    "Traverse Town 2 Boss Gauntlet Reward [Sora]": KHDDDLocationData(
        region="Traverse Town 2 [Sora]",
        code=2670287,
        category="Bonus"
    ),
    "Traverse Town 2 Boss Gauntlet Bonus Slot 1 [Sora]": KHDDDLocationData(
        region="Traverse Town 2 [Sora]",
        code=2670298,
        category="Slot"
    ),
    "Traverse Town 2 Boss Gauntlet Bonus Slot 2 [Sora]": KHDDDLocationData(
        region="Traverse Town 2 [Sora]",
        code=2670299,
        category="Slot"
    ),
    "Traverse Town 2 Cera Terror Battle Bonus Slot 1 [Riku]": KHDDDLocationData(
        region="Traverse Town 2 [Riku]",
        code=2670288,
        category="Slot"
    ),
    "Traverse Town 2 Cera Terror Battle Bonus Slot 2 [Riku]": KHDDDLocationData(
        region="Traverse Town 2 [Riku]",
        code=2670289,
        category="Slot"
    ),
    "Traverse Town 2 Cera Terror Recipe Reward [Riku]": KHDDDLocationData(
        region="Traverse Town 2 [Riku]",
        code=2670290,
        category="Reward"
    ),
    "Traverse Town 2 Knockout Punch Reward [Riku]": KHDDDLocationData(
        region="Traverse Town 2 [Riku]",
        code=2670291,
        category="Reward"
    ),
    "Traverse Town 2 Ultima Weapon Reward [Sora]": KHDDDLocationData(
        region="Traverse Town 2 [Sora]",
        code=2670292,
        category="Reward"
    ),
    "Traverse Town 2 Ultima Weapon Reward [Riku]": KHDDDLocationData(
        region="Traverse Town 2 [Riku]",
        code=2670293,
        category="Reward"
    ),
    "All Superbosses Defeated [Sora] [Riku]": KHDDDLocationData(
        region="World Map [Sora]",
        code=2670294,
        category="Bonus"
    ),
    "All Lucky Emblems Found [Sora] [Riku]": KHDDDLocationData(
        region="World Map [Sora]",
        code=2670300,
        category="Bonus"
    ),
    
    ########################################
    #############Sora Chests################
    ########################################
    "Traverse Town First District Potion [Sora]": KHDDDLocationData(
            region="Traverse Town [Sora]",
            code=2650212 #Address is +A42D80
        ),
    "Traverse Town First District Ice Dream Cone [Sora]": KHDDDLocationData(
        region="Traverse Town [Sora]",
        code=2650211
    ),
    "Traverse Town Second District Confetti Candy [Sora]": KHDDDLocationData(
        region="Traverse Town [Sora]",
        code=2650213
    ),
    "Traverse Town Second District Balloon [Sora]": KHDDDLocationData(
        region="Traverse Town [Sora]",
        code=2650214
    ),
    "Traverse Town Second District Hi-Potion [Sora]": KHDDDLocationData(
        region="Traverse Town [Sora]",
        code=2650215
    ),
    "Traverse Town Third District Vibrant Fantasy [Sora]": KHDDDLocationData(
        region="Traverse Town [Sora]",
        code=2650216
    ),
    "Traverse Town Third District Block-It Chocolate [Sora]": KHDDDLocationData(
        region="Traverse Town [Sora]",
        code=2650217
    ),
    "Traverse Town Fourth District Shield Cookie [Sora]": KHDDDLocationData(
        region="Traverse Town [Sora]",
        code=2650218
    ),
    "Traverse Town Fourth District Water Barrel [Sora]": KHDDDLocationData(
        region="Traverse Town [Sora]",
        code=2650219
    ),
    "Traverse Town Fourth District Hi-Potion [Sora]": KHDDDLocationData(
        region="Traverse Town [Sora]",
        code=2650220
    ),
    "Traverse Town Fourth District Ice Dream Cone [Sora]": KHDDDLocationData(
        region="Traverse Town [Sora]",
        code=2650221
    ),
    "Traverse Town Fifth District Shield Cookie [Sora]": KHDDDLocationData(
        region="Traverse Town [Sora]",
        code=2650222
    ),
    "Traverse Town Fifth District Potion [Sora]": KHDDDLocationData(
        region="Traverse Town [Sora]",
        code=2650223
    ),
    "Traverse Town Fifth District Block-It Chocolate [Sora]": KHDDDLocationData(
        region="Traverse Town [Sora]",
        code=2650224
    ),
    "Traverse Town Fountain Plaza Balloon [Sora]": KHDDDLocationData(
        region="Traverse Town [Sora]",
        code=2650225
    ),
    "Traverse Town Fountain Plaza Intrepid Figment [Sora]": KHDDDLocationData(
        region="Traverse Town [Sora]",
        code=2650226
    ),
    "Traverse Town Fountain Plaza Ice Dream Cone [Sora]": KHDDDLocationData(
        region="Traverse Town [Sora]",
        code=2650227
    ),
    "Traverse Town Fountain Plaza Rampant Fantasy [Sora]": KHDDDLocationData(
        region="Traverse Town [Sora]",
        code=2650228
    ),
    "Country of the Musketeers Grand Lobby Mega-Potion [Sora]": KHDDDLocationData(
        region="Country of the Musketeers [Sora]",
        code=2650229
    ),
    "Country of the Musketeers Grand Lobby Confetti Candy 2 [Sora]": KHDDDLocationData(
        region="Country of the Musketeers [Sora]",
        code=2650230
    ),
    "Country of the Musketeers Grand Lobby Ice Dream Cone 3 [Sora]": KHDDDLocationData(
        region="Country of the Musketeers [Sora]",
        code=2650231
    ),
    "Country of the Musketeers Grand Lobby Hi-Potion [Sora]": KHDDDLocationData(
        region="Country of the Musketeers [Sora]",
        code=2650232
    ),
    "Country of the Musketeers Grand Lobby Block-It Chocolate 2 [Sora]": KHDDDLocationData(
        region="Country of the Musketeers [Sora]",
        code=2650233
    ),
    "Symphony of Sorcery Tower Entrance Dream Candy [Sora]": KHDDDLocationData(
        region="Symphony of Sorcery [Sora]",
        code=2650234
    ),
    "Symphony of Sorcery Tower Block-It Chocolate 3 [Sora]": KHDDDLocationData(
        region="Symphony of Sorcery [Sora]",
        code=2650235
    ),
    "Symphony of Sorcery Tower Elixir [Sora]": KHDDDLocationData(
        region="Symphony of Sorcery [Sora]",
        code=2650236
    ),
    "La Cite des Cloches Square Block-It Chocolate [Sora]": KHDDDLocationData(
        region="La Cite des Cloches [Sora]",
        code=2650237
    ),
    "La Cite des Cloches Square Balloon [Sora]": KHDDDLocationData(
        region="La Cite des Cloches [Sora]",
        code=2650238
    ),
    "La Cite des Cloches Square Ice Dream Cone [Sora]": KHDDDLocationData(
        region="La Cite des Cloches [Sora]",
        code=2650239
    ),
    "La Cite des Cloches Square Potion [Sora]": KHDDDLocationData(
        region="La Cite des Cloches [Sora]",
        code=2650240
    ),
    "La Cite des Cloches Nave Water Barrel [Sora]": KHDDDLocationData(
        region="La Cite des Cloches [Sora]",
        code=2650241
    ),
    "La Cite des Cloches Nave Royal Cake [Sora]": KHDDDLocationData(
        region="La Cite des Cloches [Sora]",
        code=2650242
    ),
    "La Cite des Cloches Nave Block-It Chocolate [Sora]": KHDDDLocationData(
        region="La Cite des Cloches [Sora]",
        code=2650243
    ),
    "La Cite des Cloches Nave Drop-Me-Not [Sora]": KHDDDLocationData(
        region="La Cite des Cloches [Sora]",
        code=2650244
    ),
    "La Cite des Cloches Nave Potion [Sora]": KHDDDLocationData(
        region="La Cite des Cloches [Sora]",
        code=2650245
    ),
    "La Cite des Cloches Nave 2nd Drop-Me-Not [Sora]": KHDDDLocationData(
        region="La Cite des Cloches [Sora]",
        code=2650246
    ),
    "La Cite des Cloches Bell Tower Dulcet Figment [Sora]": KHDDDLocationData(
        region="La Cite des Cloches [Sora]",
        code=2650247
    ),
    "La Cite des Cloches Bell Tower Drop-Me-Not [Sora]": KHDDDLocationData(
        region="La Cite des Cloches [Sora]",
        code=2650248
    ),
    "La Cite des Cloches Bell Tower Balloon [Sora]": KHDDDLocationData(
        region="La Cite des Cloches [Sora]",
        code=2650249
    ),
    "La Cite des Cloches Bell Tower 2nd Drop-Me-Not [Sora]": KHDDDLocationData(
        region="La Cite des Cloches [Sora]",
        code=2650250
    ),
    "La Cite des Cloches Town Sparkra [Sora]": KHDDDLocationData(
        region="La Cite des Cloches [Sora]",
        code=2650251
    ),
    "La Cite des Cloches Town Candy Goggles [Sora]": KHDDDLocationData(
        region="La Cite des Cloches [Sora]",
        code=2650252
    ),
    "La Cite des Cloches Town Lofty Figment [Sora]": KHDDDLocationData(
        region="La Cite des Cloches [Sora]",
        code=2650253
    ),
    "La Cite des Cloches Town Ice Dream Cone [Sora]": KHDDDLocationData(
        region="La Cite des Cloches [Sora]",
        code=2650254
    ),
    "La Cite des Cloches Town Wheeflower Recipe [Sora]": KHDDDLocationData(
        region="La Cite des Cloches [Sora]",
        code=2650255
    ),
    "La Cite des Cloches Town Confetti Candy [Sora]": KHDDDLocationData(
        region="La Cite des Cloches [Sora]",
        code=2650256
    ),
    "La Cite des Cloches Town Troubling Fancy [Sora]": KHDDDLocationData(
        region="La Cite des Cloches [Sora]",
        code=2650257
    ),
    "La Cite des Cloches Bridge Shield Cookie [Sora]": KHDDDLocationData(
        region="La Cite des Cloches [Sora]",
        code=2650258
    ),
    "La Cite des Cloches Bridge Paint Gun: Red [Sora]": KHDDDLocationData(
        region="La Cite des Cloches [Sora]",
        code=2650259
    ),
    "La Cite des Cloches Bridge Block-It Chocolate [Sora]": KHDDDLocationData(
        region="La Cite des Cloches [Sora]",
        code=2650260
    ),
    "La Cite des Cloches Bridge Potion [Sora]": KHDDDLocationData(
        region="La Cite des Cloches [Sora]",
        code=2650261
    ),
    "La Cite des Cloches Outskirts Confetti Candy [Sora]": KHDDDLocationData(
        region="La Cite des Cloches [Sora]",
        code=2650262
    ),
    "La Cite des Cloches Outskirts Noble Figment [Sora]": KHDDDLocationData(
        region="La Cite des Cloches [Sora]",
        code=2650263
    ),
    "La Cite des Cloches Outskirts Balloon [Sora]": KHDDDLocationData(
        region="La Cite des Cloches [Sora]",
        code=2650264
    ),
    "La Cite des Cloches Outskirts Potion [Sora]": KHDDDLocationData(
        region="La Cite des Cloches [Sora]",
        code=2650265
    ),
    "La Cite des Cloches Outskirts Drop-Me-Not [Sora]": KHDDDLocationData(
        region="La Cite des Cloches [Sora]",
        code=2650266
    ),
    "The Grid Rectifier 1F Ice Dream Cone 2 [Sora]": KHDDDLocationData(
        region="The Grid [Sora]",
        code=2650267
    ),
    "The Grid Rectifier 1F Drop-Me-Not [Sora]": KHDDDLocationData(
        region="The Grid [Sora]",
        code=2650268
    ),
    "The Grid Rectifier 1F Potion [Sora]": KHDDDLocationData(
        region="The Grid [Sora]",
        code=2650269
    ),
    "The Grid Rectifier 1F Panacea [Sora]": KHDDDLocationData(
        region="The Grid [Sora]",
        code=2650270
    ),
    "The Grid Rectifier 1F Shield Cookie [Sora]": KHDDDLocationData(
        region="The Grid [Sora]",
        code=2650271
    ),
    "The Grid Rectifier 1F Hi-Potion [Sora]": KHDDDLocationData(
        region="The Grid [Sora]",
        code=2650272
    ),
    "The Grid Rectifier 1F Lofty Fantasy [Sora]": KHDDDLocationData(
        region="The Grid [Sora]",
        code=2650273
    ),
    "The Grid Rectifier 1F Ice Dream Cone [Sora]": KHDDDLocationData(
        region="The Grid [Sora]",
        code=2650274
    ),
    "The Grid Docks Eaglider Recipe [Sora]": KHDDDLocationData(
        region="The Grid [Sora]",
        code=2650275
    ),
    "The Grid Docks Candy Goggles [Sora]": KHDDDLocationData(
        region="The Grid [Sora]",
        code=2650276
    ),
    "The Grid Docks Paint Gun: Black [Sora]": KHDDDLocationData(
        region="The Grid [Sora]",
        code=2650277
    ),
    "The Grid Docks Panacea [Sora]": KHDDDLocationData(
        region="The Grid [Sora]",
        code=2650278
    ),
    "The Grid Docks Drop-Me-Not [Sora]": KHDDDLocationData(
        region="The Grid [Sora]",
        code=2650279
    ),
    "The Grid Docks Balloon [Sora]": KHDDDLocationData(
        region="The Grid [Sora]",
        code=2650280
    ),
    "The Grid City Drop-Me-Not [Sora]": KHDDDLocationData(
        region="The Grid [Sora]",
        code=2650281
    ),
    "The Grid City Troubling Fancy [Sora]": KHDDDLocationData(
        region="The Grid [Sora]",
        code=2650282
    ),
    "The Grid City Potion [Sora]": KHDDDLocationData(
        region="The Grid [Sora]",
        code=2650283
    ),
    "The Grid City Water Barrel [Sora]": KHDDDLocationData(
        region="The Grid [Sora]",
        code=2650284
    ),
    "The Grid City Block-It Chocolate 2 [Sora]": KHDDDLocationData(
        region="The Grid [Sora]",
        code=2650285
    ),
    "The Grid Throughput Fleeting Figment [Sora]": KHDDDLocationData(
        region="The Grid [Sora]",
        code=2650286
    ),
    "The Grid Throughput Circle Raid [Sora]": KHDDDLocationData(
        region="The Grid [Sora]",
        code=2650287
    ),
    "The Grid Throughput Dulcet Figment [Sora]": KHDDDLocationData(
        region="The Grid [Sora]",
        code=2650288
    ),
    "The Grid Throughput Royal Cake [Sora]": KHDDDLocationData(
        region="The Grid [Sora]",
        code=2650289
    ),
    "The Grid Throughput Confetti Candy [Sora]": KHDDDLocationData(
        region="The Grid [Sora]",
        code=2650290
    ),
    "The Grid Throughput Potion [Sora]": KHDDDLocationData(
        region="The Grid [Sora]",
        code=2650291
    ),
    "The Grid Bridge Block-It Chocolate [Sora]": KHDDDLocationData(
        region="The Grid [Sora]",
        code=2650292
    ),
    "The Grid Bridge Drop-Me-Not [Sora]": KHDDDLocationData(
        region="The Grid [Sora]",
        code=2650293
    ),
    "The Grid Rectifier 2F Cyber Yog Recipe [Sora]": KHDDDLocationData(
        region="The Grid [Sora]",
        code=2650294
    ),
    "The Grid Rectifier 2F Shield Cookie 2 [Sora]": KHDDDLocationData(
        region="The Grid [Sora]",
        code=2650295
    ),
    "The Grid Rectifier 2F Ice Dream Cone [Sora]": KHDDDLocationData(
        region="The Grid [Sora]",
        code=2650296
    ),
    "The Grid Rectifier 2F Potion [Sora]": KHDDDLocationData(
        region="The Grid [Sora]",
        code=2650297
    ),
    "The Grid Rectifier 2F Drop-Me-Not [Sora]": KHDDDLocationData(
        region="The Grid [Sora]",
        code=2650298
    ),
    "The Grid Rectifier 2F Paint Gun: Green [Sora]": KHDDDLocationData(
        region="The Grid [Sora]",
        code=2650299
    ),
    "The Grid Solar Sailer Confetti Candy 2 [Sora]": KHDDDLocationData(
        region="The Grid [Sora]",
        code=2650300
    ),
    "The Grid Solar Sailer Wondrous Figment [Sora]": KHDDDLocationData(
        region="The Grid [Sora]",
        code=2650301
    ),
    "The Grid Solar Sailer Fleeting Figment [Sora]": KHDDDLocationData(
        region="The Grid [Sora]",
        code=2650302
    ),
    "The Grid Solar Sailer Balloon [Sora]": KHDDDLocationData(
        region="The Grid [Sora]",
        code=2650303
    ),
    "The Grid Solar Sailer Hi-Potion [Sora]": KHDDDLocationData(
        region="The Grid [Sora]",
        code=2650304
    ),
    "The Grid Solar Sailer Panacea [Sora]": KHDDDLocationData(
        region="The Grid [Sora]",
        code=2650305
    ),
    "The Grid Solar Sailer Candy Goggles [Sora]": KHDDDLocationData(
        region="The Grid [Sora]",
        code=2650306
    ),
    "Traverse Town Garden Royal Cake [Sora]": KHDDDLocationData(
        region="Traverse Town [Sora]",
        code=2650307
    ),
    "Traverse Town Garden Confetti Candy [Sora]": KHDDDLocationData(
        region="Traverse Town [Sora]",
        code=2650308
    ),
    "Traverse Town Garden Rampant Figment [Sora]": KHDDDLocationData(
        region="Traverse Town [Sora]",
        code=2650309
    ),
    "Traverse Town Garden Drop-Me-Not [Sora]": KHDDDLocationData(
        region="Traverse Town [Sora]",
        code=2650310
    ),
    "Traverse Town Fourth District Potion [Sora]": KHDDDLocationData(
        region="Traverse Town [Sora]",
        code=2650311
    ),
    "Traverse Town Fourth District Block-It Chocolate [Sora]": KHDDDLocationData(
        region="Traverse Town [Sora]",
        code=2650312
    ),
    "Traverse Town Fourth District 2nd Potion [Sora]": KHDDDLocationData(
        region="Traverse Town [Sora]",
        code=2650313
    ),
    "Traverse Town Fourth District Balloon (Command) [Sora]": KHDDDLocationData(
        region="Traverse Town [Sora]",
        code=2650314
    ),
    "The Grid Solar Sailer Balloonra [Sora]": KHDDDLocationData(
        region="The Grid [Sora]",
        code=2650315
    ),
    "The Grid Solar Sailer Water Barrel [Sora]": KHDDDLocationData(
        region="The Grid [Sora]",
        code=2650316
    ),
    "Traverse Town Fountain Plaza Strike Raid [Sora]": KHDDDLocationData(
        region="Traverse Town [Sora]",
        code=2650317
    ),
    "Country of the Musketeers Theatre Confetti Candy 3 [Sora]": KHDDDLocationData(
        region="Country of the Musketeers [Sora]",
        code=2650318
    ),
    "Country of the Musketeers Theatre Dulcet Fancy [Sora]": KHDDDLocationData(
        region="Country of the Musketeers [Sora]",
        code=2650319
    ),
    "Traverse Town Post Office Rampant Fantasy [Sora]": KHDDDLocationData(
        region="Traverse Town [Sora]",
        code=2650320
    ),
    "Traverse Town Post Office Vibrant Fantasy [Sora]": KHDDDLocationData(
        region="Traverse Town [Sora]",
        code=2650321
    ),
    "Traverse Town Post Office Troubling Fantasy [Sora]": KHDDDLocationData(
        region="Traverse Town [Sora]",
        code=2650322
    ),
    "Traverse Town Post Office Spark [Sora]": KHDDDLocationData(
        region="Traverse Town [Sora]",
        code=2650323
    ),
    "Traverse Town Post Office Paint Gun: Red [Sora]": KHDDDLocationData(
        region="Traverse Town [Sora]",
        code=2650324
    ),
    "Traverse Town Post Office Potion [Sora]": KHDDDLocationData(
        region="Traverse Town [Sora]",
        code=2650325
    ),
    "Traverse Town Post Office Ice Dream Cone [Sora]": KHDDDLocationData(
        region="Traverse Town [Sora]",
        code=2650326
    ),
    "Country of the Musketeers The Opera Drop-Me-Not [Sora]": KHDDDLocationData(
        region="Country of the Musketeers [Sora]",
        code=2650327
    ),
    "Country of the Musketeers The Opera Hi-Potion [Sora]": KHDDDLocationData(
        region="Country of the Musketeers [Sora]",
        code=2650328
    ),
    "Country of the Musketeers The Opera Block-It Chocolate 2 [Sora]": KHDDDLocationData(
        region="Country of the Musketeers [Sora]",
        code=2650329
    ),
    "Country of the Musketeers Mont Saint-Michel Fleeting Fantasy [Sora]": KHDDDLocationData(
        region="Country of the Musketeers [Sora]",
        code=2650330
    ),
    "Country of the Musketeers Mont Saint-Michel Sparkga [Sora]": KHDDDLocationData(
        region="Country of the Musketeers [Sora]",
        code=2650331
    ),
    "Country of the Musketeers Mont Saint-Michel Hi-Potion [Sora]": KHDDDLocationData(
        region="Country of the Musketeers [Sora]",
        code=2650332
    ),
    "Country of the Musketeers Mont Saint-Michel Royal Cake [Sora]": KHDDDLocationData(
        region="Country of the Musketeers [Sora]",
        code=2650333
    ),
    "Country of the Musketeers Tower Road Firaga [Sora]": KHDDDLocationData(
        region="Country of the Musketeers [Sora]",
        code=2650334
    ),
    "Country of the Musketeers Tower Road Dream Candy [Sora]": KHDDDLocationData(
        region="Country of the Musketeers [Sora]",
        code=2650335
    ),
    "Country of the Musketeers Tower Road Shield Cookie 2 [Sora]": KHDDDLocationData(
        region="Country of the Musketeers [Sora]",
        code=2650336
    ),
    "Country of the Musketeers Tower Candy Goggles [Sora]": KHDDDLocationData(
        region="Country of the Musketeers [Sora]",
        code=2650337
    ),
    "Country of the Musketeers Tower Drop-Me-Not [Sora]": KHDDDLocationData(
        region="Country of the Musketeers [Sora]",
        code=2650338
    ),
    "Country of the Musketeers Tower Ice Dream Cone 2 [Sora]": KHDDDLocationData(
        region="Country of the Musketeers [Sora]",
        code=2650339
    ),
    "Country of the Musketeers Dungeon Block-It Chocolate 3 [Sora]": KHDDDLocationData(
        region="Country of the Musketeers [Sora]",
        code=2650340
    ),
    "Country of the Musketeers Dungeon Sonic Blade [Sora]": KHDDDLocationData(
        region="Country of the Musketeers [Sora]",
        code=2650341
    ),
    "Country of the Musketeers Dungeon Fleeting Fancy [Sora]": KHDDDLocationData(
        region="Country of the Musketeers [Sora]",
        code=2650342
    ),
    "Country of the Musketeers Dungeon Chef Kyroo Recipe [Sora]": KHDDDLocationData(
        region="Country of the Musketeers [Sora]",
        code=2650343
    ),
    "Country of the Musketeers Dungeon Water Barrel [Sora]": KHDDDLocationData(
        region="Country of the Musketeers [Sora]",
        code=2650344
    ),
    "Country of the Musketeers Dungeon Royal Cake [Sora]": KHDDDLocationData(
        region="Country of the Musketeers [Sora]",
        code=2650345
    ),
    "Country of the Musketeers Training Yard Mega-Potion [Sora]": KHDDDLocationData(
        region="Country of the Musketeers [Sora]",
        code=2650346
    ),
    "Country of the Musketeers Training Yard Ice Dream Cone 2 [Sora]": KHDDDLocationData(
        region="Country of the Musketeers [Sora]",
        code=2650347
    ),
    "Country of the Musketeers Training Yard Paint Gun: Sky Blue [Sora]": KHDDDLocationData(
        region="Country of the Musketeers [Sora]",
        code=2650348
    ),
    "Country of the Musketeers Shore Paint Gun: Blue [Sora]": KHDDDLocationData(
        region="Country of the Musketeers [Sora]",
        code=2650349
    ),
    "Country of the Musketeers Shore Dream Candy [Sora]": KHDDDLocationData(
        region="Country of the Musketeers [Sora]",
        code=2650350
    ),
    "Country of the Musketeers Cell Tornado Strike [Sora]": KHDDDLocationData(
        region="Country of the Musketeers [Sora]",
        code=2650351
    ),
    "Symphony of Sorcery Cloudwalk Glide [Sora]": KHDDDLocationData(
        region="Symphony of Sorcery [Sora]",
        code=2650352
    ),
    "Symphony of Sorcery Cloudwalk Intrepid Fantasy [Sora]": KHDDDLocationData(
        region="Symphony of Sorcery [Sora]",
        code=2650353
    ),
    "Symphony of Sorcery Cloudwalk Ice Dream Cone 3 [Sora]": KHDDDLocationData(
        region="Symphony of Sorcery [Sora]",
        code=2650354
    ),
    "Symphony of Sorcery Cloudwalk Mega-Potion [Sora]": KHDDDLocationData(
        region="Symphony of Sorcery [Sora]",
        code=2650355
    ),
    "Symphony of Sorcery Cloudwalk Prism Windmill [Sora]": KHDDDLocationData(
        region="Symphony of Sorcery [Sora]",
        code=2650356
    ),
    "Symphony of Sorcery Cloudwalk Paint Gun: White [Sora]": KHDDDLocationData(
        region="Symphony of Sorcery [Sora]",
        code=2650357
    ),
    "Symphony of Sorcery Cloudwalk Elixir [Sora]": KHDDDLocationData(
        region="Symphony of Sorcery [Sora]",
        code=2650358
    ),
    "Symphony of Sorcery Glen Tornado [Sora]": KHDDDLocationData(
        region="Symphony of Sorcery [Sora]",
        code=2650359
    ),
    "Symphony of Sorcery Glen Royal Cake [Sora]": KHDDDLocationData(
        region="Symphony of Sorcery [Sora]",
        code=2650360
    ),
    "Symphony of Sorcery Glen Intrepid Fantasy [Sora]": KHDDDLocationData(
        region="Symphony of Sorcery [Sora]",
        code=2650361
    ),
    "Symphony of Sorcery Glen Ice Dream Cone 3 [Sora]": KHDDDLocationData(
        region="Symphony of Sorcery [Sora]",
        code=2650362
    ),
    "Symphony of Sorcery Glen Mega-Potion [Sora]": KHDDDLocationData(
        region="Symphony of Sorcery [Sora]",
        code=2650363
    ),
    "Symphony of Sorcery Fields Block-It Chocolate 3 [Sora]": KHDDDLocationData(
        region="Symphony of Sorcery [Sora]",
        code=2650364
    ),
    "Symphony of Sorcery Fields Epic Fantasy [Sora]": KHDDDLocationData(
        region="Symphony of Sorcery [Sora]",
        code=2650365
    ),
    "Symphony of Sorcery Fields Electricorn Recipe [Sora]": KHDDDLocationData(
        region="Symphony of Sorcery [Sora]",
        code=2650366
    ),
    "Symphony of Sorcery Fields Triple Plasma [Sora]": KHDDDLocationData(
        region="Symphony of Sorcery [Sora]",
        code=2650367
    ),
    "Symphony of Sorcery Fields Panacea [Sora]": KHDDDLocationData(
        region="Symphony of Sorcery [Sora]",
        code=2650368
    ),
    "Symphony of Sorcery Fields Mega-Potion [Sora]": KHDDDLocationData(
        region="Symphony of Sorcery [Sora]",
        code=2650369
    ),
    "Prankster's Paradise Amusement Park Blizzara [Sora]": KHDDDLocationData(
        region="Prankster's Paradise [Sora]",
        code=2650370
    ),
    "Prankster's Paradise Amusement Park Drop-Me-Not [Sora]": KHDDDLocationData(
        region="Prankster's Paradise [Sora]",
        code=2650371
    ),
    "Prankster's Paradise Amusement Park Balloon [Sora]": KHDDDLocationData(
        region="Prankster's Paradise [Sora]",
        code=2650372
    ),
    "Prankster's Paradise Amusement Park Shield Cookie 2 [Sora]": KHDDDLocationData(
        region="Prankster's Paradise [Sora]",
        code=2650373
    ),
    "Prankster's Paradise Amusement Park Malleable Fantasy [Sora]": KHDDDLocationData(
        region="Prankster's Paradise [Sora]",
        code=2650374
    ),
    "Prankster's Paradise Amusement Park Paint Gun: Yellow [Sora]": KHDDDLocationData(
        region="Prankster's Paradise [Sora]",
        code=2650375
    ),
    "Prankster's Paradise Amusement Park Ice Dream Cone 2 [Sora]": KHDDDLocationData(
        region="Prankster's Paradise [Sora]",
        code=2650376
    ),
    "Prankster's Paradise Amusement Park Block-It Chocolate 2 [Sora]": KHDDDLocationData(
        region="Prankster's Paradise [Sora]",
        code=2650377
    ),
    "Prankster's Paradise Amusement Park Hi-Potion [Sora]": KHDDDLocationData(
        region="Prankster's Paradise [Sora]",
        code=2650378
    ),
    "Prankster's Paradise Ocean Floor Panacea [Sora]": KHDDDLocationData(
        region="Prankster's Paradise [Sora]",
        code=2650379
    ),
    "Prankster's Paradise Ocean Floor Lofty Fantasy [Sora]": KHDDDLocationData(
        region="Prankster's Paradise [Sora]",
        code=2650380
    ),
    "Prankster's Paradise Ocean Floor Paint Gun: Sky Blue [Sora]": KHDDDLocationData(
        region="Prankster's Paradise [Sora]",
        code=2650381
    ),
    "Prankster's Paradise Ocean Floor Zero Gravira [Sora]": KHDDDLocationData(
        region="Prankster's Paradise [Sora]",
        code=2650382
    ),
    "Prankster's Paradise Ocean Depths Rampant Fancy [Sora]": KHDDDLocationData(
        region="Prankster's Paradise [Sora]",
        code=2650383
    ),
    "Prankster's Paradise Ocean Depths Candy Goggles [Sora]": KHDDDLocationData(
        region="Prankster's Paradise [Sora]",
        code=2650384
    ),
    "Prankster's Paradise Ocean Depths Royal Cake [Sora]": KHDDDLocationData(
        region="Prankster's Paradise [Sora]",
        code=2650385
    ),
    "Prankster's Paradise Ocean Depths Tatsu Steed Recipe [Sora]": KHDDDLocationData(
        region="Prankster's Paradise [Sora]",
        code=2650386
    ),
    "Prankster's Paradise Ocean Depths Shield Cookie 2 [Sora]": KHDDDLocationData(
        region="Prankster's Paradise [Sora]",
        code=2650387
    ),
    "Prankster's Paradise Promontory Hi-Potion [Sora]": KHDDDLocationData(
        region="Prankster's Paradise [Sora]",
        code=2650388
    ),
    "Prankster's Paradise Promontory Water Barrel [Sora]": KHDDDLocationData(
        region="Prankster's Paradise [Sora]",
        code=2650389
    ),
    "Prankster's Paradise Promontory Ice Dream Cone 2 [Sora]": KHDDDLocationData(
        region="Prankster's Paradise [Sora]",
        code=2650390
    ),
    "Prankster's Paradise Windup Way Block-It Chocolate 2 [Sora]": KHDDDLocationData(
        region="Prankster's Paradise [Sora]",
        code=2650391
    ),
    "Prankster's Paradise Windup Way Drop-Me-Not [Sora]": KHDDDLocationData(
        region="Prankster's Paradise [Sora]",
        code=2650392
    ),
    "Prankster's Paradise Windup Way Aerial Slam [Sora]": KHDDDLocationData(
        region="Prankster's Paradise [Sora]",
        code=2650393
    ),
    "Prankster's Paradise Windup Way Royal Cake [Sora]": KHDDDLocationData(
        region="Prankster's Paradise [Sora]",
        code=2650394
    ),
    "Prankster's Paradise Windup Way Hi-Potion [Sora]": KHDDDLocationData(
        region="Prankster's Paradise [Sora]",
        code=2650395
    ),
    "Prankster's Paradise Circus Balloon [Sora]": KHDDDLocationData(
        region="Prankster's Paradise [Sora]",
        code=2650396
    ),
    "Prankster's Paradise Circus Drop-Me-Not [Sora]": KHDDDLocationData(
        region="Prankster's Paradise [Sora]",
        code=2650397
    ),
    "Prankster's Paradise Circus Confetti Candy 2 [Sora]": KHDDDLocationData(
        region="Prankster's Paradise [Sora]",
        code=2650398
    ),
    "Prankster's Paradise Circus Rampant Fancy [Sora]": KHDDDLocationData(
        region="Prankster's Paradise [Sora]",
        code=2650399
    ),
    "La Cite des Cloches Graveyard Gate Ice Dream Cone [Sora]": KHDDDLocationData(
        region="La Cite des Cloches [Sora]",
        code=2650400
    ),
    "La Cite des Cloches Graveyard Gate Drop-Me-Not [Sora]": KHDDDLocationData(
        region="La Cite des Cloches [Sora]",
        code=2650401
    ),
    "La Cite des Cloches Graveyard Gate Potion [Sora]": KHDDDLocationData(
        region="La Cite des Cloches [Sora]",
        code=2650402
    ),
    "La Cite des Cloches Tunnels Sleepra [Sora]": KHDDDLocationData(
        region="La Cite des Cloches [Sora]",
        code=2650403
    ),
    "La Cite des Cloches Tunnels Drop-Me-Not [Sora]": KHDDDLocationData(
        region="La Cite des Cloches [Sora]",
        code=2650404
    ),
    "La Cite des Cloches Tunnels Catanuki Recipe [Sora]": KHDDDLocationData(
        region="La Cite des Cloches [Sora]",
        code=2650405
    ),
    "La Cite des Cloches Tunnels Paint Gun: Purple [Sora]": KHDDDLocationData(
        region="La Cite des Cloches [Sora]",
        code=2650406
    ),
    "La Cite des Cloches Tunnels Ice Dream Cone 2 [Sora]": KHDDDLocationData(
        region="La Cite des Cloches [Sora]",
        code=2650407
    ),
    "La Cite des Cloches Old Graveyard Drop-Me-Not [Sora]": KHDDDLocationData(
        region="La Cite des Cloches [Sora]",
        code=2650408
    ),
    "La Cite des Cloches Catacombs Water Barrel [Sora]": KHDDDLocationData(
        region="La Cite des Cloches [Sora]",
        code=2650409
    ),
    "La Cite des Cloches Catacombs Fire Windmill [Sora]": KHDDDLocationData(
        region="La Cite des Cloches [Sora]",
        code=2650410
    ),
    "La Cite des Cloches Catacombs Toximander Recipe [Sora]": KHDDDLocationData(
        region="La Cite des Cloches [Sora]",
        code=2650411
    ),
    "La Cite des Cloches Catacombs Royal Cake [Sora]": KHDDDLocationData(
        region="La Cite des Cloches [Sora]",
        code=2650412
    ),
    "La Cite des Cloches Catacombs Drop-Me-Not [Sora]": KHDDDLocationData(
        region="La Cite des Cloches [Sora]",
        code=2650413
    ),
    "La Cite des Cloches Catacombs Shield Cookie [Sora]": KHDDDLocationData(
        region="La Cite des Cloches [Sora]",
        code=2650414
    ),
    "La Cite des Cloches Court of Miracles Thunder Dash [Sora]": KHDDDLocationData(
        region="La Cite des Cloches [Sora]",
        code=2650415
    ),
    "La Cite des Cloches Court of Miracles Hi-Potion [Sora]": KHDDDLocationData(
        region="La Cite des Cloches [Sora]",
        code=2650416
    ),
    "La Cite des Cloches Court of Miracles Block-It Chocolate [Sora]": KHDDDLocationData(
        region="La Cite des Cloches [Sora]",
        code=2650417
    ),
    "The World That Never Was Avenue to Dreams Shield Cookie 3 [Sora]": KHDDDLocationData(
        region="The World That Never Was [Sora]",
        code=2650418
    ),
    "The World That Never Was Avenue to Dreams Dulcet Fantasy [Sora]": KHDDDLocationData(
        region="The World That Never Was [Sora]",
        code=2650419
    ),
    "The World That Never Was Avenue to Dreams Savage Fantasy [Sora]": KHDDDLocationData(
        region="The World That Never Was [Sora]",
        code=2650420
    ),
    "The World That Never Was Avenue to Dreams Salvation [Sora]": KHDDDLocationData(
        region="The World That Never Was [Sora]",
        code=2650421
    ),
    "The World That Never Was Avenue to Dreams Elixir [Sora]": KHDDDLocationData(
        region="The World That Never Was [Sora]",
        code=2650422
    ),
    "The World That Never Was Avenue to Dreams Dream Candy [Sora]": KHDDDLocationData(
        region="The World That Never Was [Sora]",
        code=2650423
    ),
    "The World That Never Was Avenue to Dreams Water Barrel [Sora]": KHDDDLocationData(
        region="The World That Never Was [Sora]",
        code=2650424
    ),
    "The World That Never Was Avenue to Dreams Drak Quack Recipe [Sora]": KHDDDLocationData(
        region="The World That Never Was [Sora]",
        code=2650425
    ),
    "The World That Never Was Contorted City Elixir [Sora]": KHDDDLocationData(
        region="The World That Never Was [Sora]",
        code=2650426
    ),
    "The World That Never Was Contorted City Block-It Chocolate 3 [Sora]": KHDDDLocationData(
        region="The World That Never Was [Sora]",
        code=2650427
    ),
    "The World That Never Was Contorted City Shield Cookie 3 [Sora]": KHDDDLocationData(
        region="The World That Never Was [Sora]",
        code=2650428
    ),
    "The World That Never Was Contorted City Confetti Candy 3 [Sora]": KHDDDLocationData(
        region="The World That Never Was [Sora]",
        code=2650429
    ),
    "The World That Never Was Contorted City Wondrous Fantasy [Sora]": KHDDDLocationData(
        region="The World That Never Was [Sora]",
        code=2650430
    ),
    "The World That Never Was Contorted City Ice Dream Cone 3 [Sora]": KHDDDLocationData(
        region="The World That Never Was [Sora]",
        code=2650431
    ),
    "The World That Never Was Contorted City Ars Arcanum [Sora]": KHDDDLocationData(
        region="The World That Never Was [Sora]",
        code=2650432
    ),
    "Prankster's Paradise Amusement Park Candy Goggles [Sora]": KHDDDLocationData(
        region="Prankster's Paradise [Sora]",
        code=2650433
    ),
    "Symphony of Sorcery Cloudwalk Candy Goggles [Sora]": KHDDDLocationData(
        region="Symphony of Sorcery [Sora]",
        code=2650434
    ),
    "La Cite des Cloches Tunnels Noble Fantasy [Sora]": KHDDDLocationData(
        region="La Cite des Cloches [Sora]",
        code=2650435
    ),

    ########################################
    #############Riku Chests################
    ########################################
    "Traverse Town First District Rampant Fantasy [Riku]": KHDDDLocationData(
        region="Traverse Town [Riku]",
        code=2650436
    ),
    "Traverse Town First District Potion [Riku]": KHDDDLocationData(
        region="Traverse Town [Riku]",
        code=2650437
    ),
    "Traverse Town Second District Block-It Chocolate [Riku]": KHDDDLocationData(
        region="Traverse Town [Riku]",
        code=2650438
    ),
    "Traverse Town Second District Balloon [Riku]": KHDDDLocationData(
        region="Traverse Town [Riku]",
        code=2650439
    ),
    "Traverse Town Second District Yoggy Ram Recipe [Riku]": KHDDDLocationData(
        region="Traverse Town [Riku]",
        code=2650440
    ),
    "Traverse Town Third District Ice Dream Cone [Riku]": KHDDDLocationData(
        region="Traverse Town [Riku]",
        code=2650441
    ),
    "Traverse Town Third District Confetti Candy [Riku]": KHDDDLocationData(
        region="Traverse Town [Riku]",
        code=2650442
    ),
    "Traverse Town Fourth District Potion [Riku]": KHDDDLocationData(
        region="Traverse Town [Riku]",
        code=2650443
    ),
    "Traverse Town Fourth District Intrepid Figment [Riku]": KHDDDLocationData(
        region="Traverse Town [Riku]",
        code=2650444
    ),
    "Traverse Town Fourth District Balloon [Riku]": KHDDDLocationData(
        region="Traverse Town [Riku]",
        code=2650445
    ),
    "Traverse Town Fourth District Confetti Candy [Riku]": KHDDDLocationData(
        region="Traverse Town [Riku]",
        code=2650446
    ),
    "Traverse Town Fifth District Troubling Fantasy [Riku]": KHDDDLocationData(
        region="Traverse Town [Riku]",
        code=2650447
    ),
    "Traverse Town Fifth District Hi-Potion [Riku]": KHDDDLocationData(
        region="Traverse Town [Riku]",
        code=2650448
    ),
    "Traverse Town Fifth District Block-It Chocolate [Riku]": KHDDDLocationData(
        region="Traverse Town [Riku]",
        code=2650449
    ),
    "Traverse Town Fountain Plaza Vibrant Fantasy [Riku]": KHDDDLocationData(
        region="Traverse Town [Riku]",
        code=2650450
    ),
    "Traverse Town Fountain Plaza Ice Dream Cone [Riku]": KHDDDLocationData(
        region="Traverse Town [Riku]",
        code=2650451
    ),
    "Country of the Musketeers Grand Lobby Water Barrel [Riku]": KHDDDLocationData(
        region="Country of the Musketeers [Riku]",
        code=2650452
    ),
    "Country of the Musketeers Grand Lobby Confetti Candy 2 [Riku]": KHDDDLocationData(
        region="Country of the Musketeers [Riku]",
        code=2650453
    ),
    "Country of the Musketeers Grand Lobby Royal Cake [Riku]": KHDDDLocationData(
        region="Country of the Musketeers [Riku]",
        code=2650454
    ),
    "Country of the Musketeers Grand Lobby Shadowbreaker [Riku]": KHDDDLocationData(
        region="Country of the Musketeers [Riku]",
        code=2650455
    ),
    "Country of the Musketeers Grand Lobby Mega-Potion [Riku]": KHDDDLocationData(
        region="Country of the Musketeers [Riku]",
        code=2650456
    ),
    "Symphony of Sorcery Tower Entrance Water Barrel [Riku]": KHDDDLocationData(
        region="Symphony of Sorcery [Riku]",
        code=2650457
    ),
    "Symphony of Sorcery Tower Royal Cake [Riku]": KHDDDLocationData(
        region="Symphony of Sorcery [Riku]",
        code=2650458
    ),
    "Symphony of Sorcery Tower Dream Candy [Riku]": KHDDDLocationData(
        region="Symphony of Sorcery [Riku]",
        code=2650459
    ),
    "La Cite des Cloches Square Balloon [Riku]": KHDDDLocationData(
        region="La Cite des Cloches [Riku]",
        code=2650460
    ),
    "La Cite des Cloches Square Shield Cookie [Riku]": KHDDDLocationData(
        region="La Cite des Cloches [Riku]",
        code=2650461
    ),
    "La Cite des Cloches Square Confetti Candy [Riku]": KHDDDLocationData(
        region="La Cite des Cloches [Riku]",
        code=2650462
    ),
    "La Cite des Cloches Square Potion [Riku]": KHDDDLocationData(
        region="La Cite des Cloches [Riku]",
        code=2650463
    ),
    "La Cite des Cloches Nave Shield Cookie 2 [Riku]": KHDDDLocationData(
        region="La Cite des Cloches [Riku]",
        code=2650464
    ),
    "La Cite des Cloches Nave Fira [Riku]": KHDDDLocationData(
        region="La Cite des Cloches [Riku]",
        code=2650465
    ),
    "La Cite des Cloches Nave Drop-Me-Not [Riku]": KHDDDLocationData(
        region="La Cite des Cloches [Riku]",
        code=2650466
    ),
    "La Cite des Cloches Nave Rampant Figment [Riku]": KHDDDLocationData(
        region="La Cite des Cloches [Riku]",
        code=2650467
    ),
    "La Cite des Cloches Nave Paint Gun: Yellow [Riku]": KHDDDLocationData(
        region="La Cite des Cloches [Riku]",
        code=2650468
    ),
    "La Cite des Cloches Nave Second Drop-Me-Not [Riku]": KHDDDLocationData(
        region="La Cite des Cloches [Riku]",
        code=2650469
    ),
    "La Cite des Cloches Bell Tower Royal Cake [Riku]": KHDDDLocationData(
        region="La Cite des Cloches [Riku]",
        code=2650470
    ),
    "La Cite des Cloches Bell Tower Dulcet Figment [Riku]": KHDDDLocationData(
        region="La Cite des Cloches [Riku]",
        code=2650471
    ),
    "La Cite des Cloches Bell Tower Drop-Me-Not [Riku]": KHDDDLocationData(
        region="La Cite des Cloches [Riku]",
        code=2650472
    ),
    "La Cite des Cloches Bell Tower Second Drop-Me-Not [Riku]": KHDDDLocationData(
        region="La Cite des Cloches [Riku]",
        code=2650473
    ),
    "La Cite des Cloches Town Block-It Chocolate [Riku]": KHDDDLocationData(
        region="La Cite des Cloches [Riku]",
        code=2650474
    ),
    "La Cite des Cloches Town Candy Goggles [Riku]": KHDDDLocationData(
        region="La Cite des Cloches [Riku]",
        code=2650475
    ),
    "La Cite des Cloches Town Water Barrel [Riku]": KHDDDLocationData(
        region="La Cite des Cloches [Riku]",
        code=2650476
    ),
    "La Cite des Cloches Town Noble Fantasy [Riku]": KHDDDLocationData(
        region="La Cite des Cloches [Riku]",
        code=2650477
    ),
    "La Cite des Cloches Town Potion [Riku]": KHDDDLocationData(
        region="La Cite des Cloches [Riku]",
        code=2650478
    ),
    "La Cite des Cloches Town Ice Dream Cone [Riku]": KHDDDLocationData(
        region="La Cite des Cloches [Riku]",
        code=2650479
    ),
    "La Cite des Cloches Town Drop-Me-Not [Riku]": KHDDDLocationData(
        region="La Cite des Cloches [Riku]",
        code=2650480
    ),
    "La Cite des Cloches Bridge Balloon [Riku]": KHDDDLocationData(
        region="La Cite des Cloches [Riku]",
        code=2650481
    ),
    "La Cite des Cloches Bridge Confetti Candy 2 [Riku]": KHDDDLocationData(
        region="La Cite des Cloches [Riku]",
        code=2650482
    ),
    "La Cite des Cloches Bridge Confetti Candy [Riku]": KHDDDLocationData(
        region="La Cite des Cloches [Riku]",
        code=2650483
    ),
    "La Cite des Cloches Bridge Potion [Riku]": KHDDDLocationData(
        region="La Cite des Cloches [Riku]",
        code=2650484
    ),
    "La Cite des Cloches Outskirts Shield Cookie [Riku]": KHDDDLocationData(
        region="La Cite des Cloches [Riku]",
        code=2650485
    ),
    "La Cite des Cloches Outskirts Potion [Riku]": KHDDDLocationData(
        region="La Cite des Cloches [Riku]",
        code=2650486
    ),
    "La Cite des Cloches Outskirts Drop-Me-Not [Riku]": KHDDDLocationData(
        region="La Cite des Cloches [Riku]",
        code=2650487
    ),
    "La Cite des Cloches Outskirts Paint Gun: Purple [Riku]": KHDDDLocationData(
        region="La Cite des Cloches [Riku]",
        code=2650488
    ),
    "La Cite des Cloches Outskirts Confetti Candy [Riku]": KHDDDLocationData(
        region="La Cite des Cloches [Riku]",
        code=2650489
    ),
    "The Grid Rectifier 1F Balloon [Riku]": KHDDDLocationData(
        region="The Grid [Riku]",
        code=2650490
    ),
    "The Grid Rectifier 1F Hi-Potion [Riku]": KHDDDLocationData(
        region="The Grid [Riku]",
        code=2650491
    ),
    "The Grid Rectifier 1F Block-It Chocolate [Riku]": KHDDDLocationData(
        region="The Grid [Riku]",
        code=2650492
    ),
    "The Grid Rectifier 1F Shield Cookie 2 [Riku]": KHDDDLocationData(
        region="The Grid [Riku]",
        code=2650493
    ),
    "The Grid Rectifier 1F Panacea [Riku]": KHDDDLocationData(
        region="The Grid [Riku]",
        code=2650494
    ),
    "The Grid Rectifier 1F Potion [Riku]": KHDDDLocationData(
        region="The Grid [Riku]",
        code=2650495
    ),
    "The Grid Rectifier 1F Fleeting Figment [Riku]": KHDDDLocationData(
        region="The Grid [Riku]",
        code=2650496
    ),
    "The Grid Rectifier 1F Peepsta Hoo Recipe [Riku]": KHDDDLocationData(
        region="The Grid [Riku]",
        code=2650497
    ),
    "The Grid Docks Confetti Candy 2 [Riku]": KHDDDLocationData(
        region="The Grid [Riku]",
        code=2650498
    ),
    "The Grid Docks Counter Aura [Riku]": KHDDDLocationData(
        region="The Grid [Riku]",
        code=2650499
    ),
    "The Grid Docks Shield Cookie [Riku]": KHDDDLocationData(
        region="The Grid [Riku]",
        code=2650500
    ),
    "The Grid Docks Drop-Me-Not [Riku]": KHDDDLocationData(
        region="The Grid [Riku]",
        code=2650501
    ),
    "The Grid Docks Potion [Riku]": KHDDDLocationData(
        region="The Grid [Riku]",
        code=2650502
    ),
    "The Grid Docks Balloon [Riku]": KHDDDLocationData(
        region="The Grid [Riku]",
        code=2650503
    ),
    "The Grid City Confetti Candy [Riku]": KHDDDLocationData(
        region="The Grid [Riku]",
        code=2650504
    ),
    "The Grid City Thundara [Riku]": KHDDDLocationData(
        region="The Grid [Riku]",
        code=2650505
    ),
    "The Grid City Potion [Riku]": KHDDDLocationData(
        region="The Grid [Riku]",
        code=2650506
    ),
    "The Grid City Fleeting Figment [Riku]": KHDDDLocationData(
        region="The Grid [Riku]",
        code=2650507
    ),
    "The Grid City Drop-Me-Not [Riku]": KHDDDLocationData(
        region="The Grid [Riku]",
        code=2650508
    ),
    "The Grid Throughput Royal Cake [Riku]": KHDDDLocationData(
        region="The Grid [Riku]",
        code=2650509
    ),
    "The Grid Throughput Wondrous Figment [Riku]": KHDDDLocationData(
        region="The Grid [Riku]",
        code=2650510
    ),
    "The Grid Throughput Noble Fantasy [Riku]": KHDDDLocationData(
        region="The Grid [Riku]",
        code=2650511
    ),
    "The Grid Throughput Ice Dream Cone 2 [Riku]": KHDDDLocationData(
        region="The Grid [Riku]",
        code=2650512
    ),
    "The Grid Throughput Shield Cookie [Riku]": KHDDDLocationData(
        region="The Grid [Riku]",
        code=2650513
    ),
    "The Grid Throughput Potion [Riku]": KHDDDLocationData(
        region="The Grid [Riku]",
        code=2650514
    ),
    "The Grid Bridge Panacea [Riku]": KHDDDLocationData(
        region="The Grid [Riku]",
        code=2650515
    ),
    "The Grid Bridge Water Barrel [Riku]": KHDDDLocationData(
        region="The Grid [Riku]",
        code=2650516
    ),
    "The Grid Rectifier 2F Gravity Strike [Riku]": KHDDDLocationData(
        region="The Grid [Riku]",
        code=2650517
    ),
    "The Grid Rectifier 2F Block-It Chocolate 2 [Riku]": KHDDDLocationData(
        region="The Grid [Riku]",
        code=2650518
    ),
    "The Grid Rectifier 2F Noble Figment [Riku]": KHDDDLocationData(
        region="The Grid [Riku]",
        code=2650519
    ),
    "The Grid Rectifier 2F Potion [Riku]": KHDDDLocationData(
        region="The Grid [Riku]",
        code=2650520
    ),
    "The Grid Rectifier 2F Confetti Candy 2 [Riku]": KHDDDLocationData(
        region="The Grid [Riku]",
        code=2650521
    ),
    "The Grid Rectifier 2F Drop-Me-Not [Riku]": KHDDDLocationData(
        region="The Grid [Riku]",
        code=2650522
    ),
    "The Grid Solar Sailer Panacea [Riku]": KHDDDLocationData(
        region="The Grid [Riku]",
        code=2650523
    ),
    "The Grid Solar Sailer Troubling Fancy [Riku]": KHDDDLocationData(
        region="The Grid [Riku]",
        code=2650524
    ),
    "The Grid Solar Sailer Wondrous Figment [Riku]": KHDDDLocationData(
        region="The Grid [Riku]",
        code=2650525
    ),
    "The Grid Solar Sailer Paint Gun: White [Riku]": KHDDDLocationData(
        region="The Grid [Riku]",
        code=2650526
    ),
    "The Grid Solar Sailer Hi-Potion [Riku]": KHDDDLocationData(
        region="The Grid [Riku]",
        code=2650527
    ),
    "The Grid Solar Sailer Drop-Me-Not [Riku]": KHDDDLocationData(
        region="The Grid [Riku]",
        code=2650528
    ),
    "The Grid Solar Sailer Candy Goggles [Riku]": KHDDDLocationData(
        region="The Grid [Riku]",
        code=2650529
    ),
    "Traverse Town Garden Drop-Me-Not [Riku]": KHDDDLocationData(
        region="Traverse Town [Riku]",
        code=2650530
    ),
    "Traverse Town Garden Paint Gun: Green [Riku]": KHDDDLocationData(
        region="Traverse Town [Riku]",
        code=2650531
    ),
    "Traverse Town Garden Royal Cake [Riku]": KHDDDLocationData(
        region="Traverse Town [Riku]",
        code=2650532
    ),
    "Traverse Town Garden Hi-Potion [Riku]": KHDDDLocationData(
        region="Traverse Town [Riku]",
        code=2650533
    ),
    "Traverse Town Fourth District Second Potion [Riku]": KHDDDLocationData(
        region="Traverse Town [Riku]",
        code=2650534
    ),
    "Traverse Town Fourth District Shield Cookie [Riku]": KHDDDLocationData(
        region="Traverse Town [Riku]",
        code=2650535,
    ),
    "Traverse Town Fourth District Second Confetti Candy [Riku]": KHDDDLocationData(
        region="Traverse Town [Riku]",
        code=2650536,
    ),
    "Traverse Town Fourth District Candy Goggles [Riku]": KHDDDLocationData(
        region="Traverse Town [Riku]",
        code=2650537,
    ),
    "The Grid Solar Sailer Shield Cookie 2 [Riku]": KHDDDLocationData(
        region="The Grid [Riku]",
        code=2650538,
    ),
    "The Grid Solar Sailer Royal Cake [Riku]": KHDDDLocationData(
        region="The Grid [Riku]",
        code=2650539,
    ),
    "Traverse Town Fountain Plaza Blizzard Edge [Riku]": KHDDDLocationData(
        region="Traverse Town [Riku]",
        code=2650540,
    ),
    "Country of the Musketeers Theatre Confetti Candy 2 [Riku]": KHDDDLocationData(
        region="Country of the Musketeers [Riku]",
        code=2650541,
    ),
    "Country of the Musketeers Theatre Balloon [Riku]": KHDDDLocationData(
        region="Country of the Musketeers [Riku]",
        code=2650542,
    ),
    "Traverse Town Back Streets Troubling Fantasy [Riku]": KHDDDLocationData(
        region="Traverse Town [Riku]",
        code=2650543,
    ),
    "Traverse Town Back Streets Thunder [Riku]": KHDDDLocationData(
        region="Traverse Town [Riku]",
        code=2650544,
    ),
    "Traverse Town Back Streets Potion [Riku]": KHDDDLocationData(
        region="Traverse Town [Riku]",
        code=2650545,
    ),
    "Traverse Town Back Streets Shield Cookie [Riku]": KHDDDLocationData(
        region="Traverse Town [Riku]",
        code=2650546,
    ),
    "Traverse Town Back Streets Intrepid Figment [Riku]": KHDDDLocationData(
        region="Traverse Town [Riku]",
        code=2650547,
    ),
    "Traverse Town Back Streets Paint Gun: Sky Blue [Riku]": KHDDDLocationData(
        region="Traverse Town [Riku]",
        code=2650548,
    ),
    "Traverse Town Back Streets Second Potion [Riku]": KHDDDLocationData(
        region="Traverse Town [Riku]",
        code=2650549,
    ),
    "Country of the Musketeers The Opera Hi-Potion [Riku]": KHDDDLocationData(
        region="Country of the Musketeers [Riku]",
        code=2650550,
    ),
    "Country of the Musketeers The Opera Shield Cookie 2 [Riku]": KHDDDLocationData(
        region="Country of the Musketeers [Riku]",
        code=2650551,
    ),
    "Country of the Musketeers The Opera Panacea [Riku]": KHDDDLocationData(
        region="Country of the Musketeers [Riku]",
        code=2650552,
    ),
    "Country of the Musketeers The Opera Dream Candy [Riku]": KHDDDLocationData(
        region="Country of the Musketeers [Riku]",
        code=2650553,
    ),
    "Country of the Musketeers Green Room Candy Goggles [Riku]": KHDDDLocationData(
        region="Country of the Musketeers [Riku]",
        code=2650554,
    ),
    "Country of the Musketeers Green Room Prickly Fantasy [Riku]": KHDDDLocationData(
        region="Country of the Musketeers [Riku]",
        code=2650555,
    ),
    "Country of the Musketeers Green Room Fleeting Fantasy [Riku]": KHDDDLocationData(
        region="Country of the Musketeers [Riku]",
        code=2650556,
    ),
    "Country of the Musketeers Green Room Shield Cookie 3 [Riku]": KHDDDLocationData(
        region="Country of the Musketeers [Riku]",
        code=2650557,
    ),
    "Country of the Musketeers Green Room Hi-Potion [Riku]": KHDDDLocationData(
        region="Country of the Musketeers [Riku]",
        code=2650558,
    ),
    "Country of the Musketeers Machine Room Blizzaga [Riku]": KHDDDLocationData(
        region="Country of the Musketeers [Riku]",
        code=2650559,
    ),
    "Country of the Musketeers Machine Room Ducky Goose Recipe [Riku]": KHDDDLocationData(
        region="Country of the Musketeers [Riku]",
        code=2650560,
    ),
    "Country of the Musketeers Machine Room Ice Dream Cone 2 [Riku]": KHDDDLocationData(
        region="Country of the Musketeers [Riku]",
        code=2650561,
    ),
    "Country of the Musketeers Machine Room Drop-Me-Not [Riku]": KHDDDLocationData(
        region="Country of the Musketeers [Riku]",
        code=2650562,
    ),
    "Country of the Musketeers Backstage Royal Cake [Riku]": KHDDDLocationData(
        region="Country of the Musketeers [Riku]",
        code=2650563,
    ),
    "Country of the Musketeers Backstage Fleeting Fantasy [Riku]": KHDDDLocationData(
        region="Country of the Musketeers [Riku]",
        code=2650564,
    ),
    "Country of the Musketeers Backstage Dream Candy [Riku]": KHDDDLocationData(
        region="Country of the Musketeers [Riku]",
        code=2650565,
    ),
    "Country of the Musketeers Backstage Staggerceps Recipe [Riku]": KHDDDLocationData(
        region="Country of the Musketeers [Riku]",
        code=2650566,
    ),
    "Symphony of Sorcery Moonlight Wood Zero Graviza [Riku]": KHDDDLocationData(
        region="Symphony of Sorcery [Riku]",
        code=2650567,
    ),
    "Symphony of Sorcery Moonlight Wood Confetti Candy 3 [Riku]": KHDDDLocationData(
        region="Symphony of Sorcery [Riku]",
        code=2650568,
    ),
    "Symphony of Sorcery Moonlight Wood Shield Cookie 3 [Riku]": KHDDDLocationData(
        region="Symphony of Sorcery [Riku]",
        code=2650569,
    ),
    "Symphony of Sorcery Moonlight Wood Paint Gun: Green [Riku]": KHDDDLocationData(
        region="Symphony of Sorcery [Riku]",
        code=2650570,
    ),
    "Symphony of Sorcery Golden Wood Elixir [Riku]": KHDDDLocationData(
        region="Symphony of Sorcery [Riku]",
        code=2650571,
    ),
    "Symphony of Sorcery Golden Wood Intrepid Fantasy [Riku]": KHDDDLocationData(
        region="Symphony of Sorcery [Riku]",
        code=2650572,
    ),
    "Symphony of Sorcery Golden Wood Mega-Potion [Riku]": KHDDDLocationData(
        region="Symphony of Sorcery [Riku]",
        code=2650573,
    ),
    "Symphony of Sorcery Snowgleam Wood Ice Barrage [Riku]": KHDDDLocationData(
        region="Symphony of Sorcery [Riku]",
        code=2650574,
    ),
    "Symphony of Sorcery Snowgleam Wood Candy Goggles [Riku]": KHDDDLocationData(
        region="Symphony of Sorcery [Riku]",
        code=2650575,
    ),
    "Symphony of Sorcery Snowgleam Wood Block-It Chocolate [Riku]": KHDDDLocationData(
        region="Symphony of Sorcery [Riku]",
        code=2650576,
    ),
    "Symphony of Sorcery Snowgleam Wood Ice Dream Cone 3 [Riku]": KHDDDLocationData(
        region="Symphony of Sorcery [Riku]",
        code=2650577,
    ),
    "La Cite des Cloches Windmill Block-It Chocolate [Riku]": KHDDDLocationData(
        region="La Cite des Cloches [Riku]",
        code=2650578
    ),
    "La Cite des Cloches Windmill Sliding Crescent [Riku]": KHDDDLocationData(
        region="La Cite des Cloches [Riku]",
        code=2650579
    ),
    "La Cite des Cloches Windmill Water Barrel [Riku]": KHDDDLocationData(
        region="La Cite des Cloches [Riku]",
        code=2650580
    ),
    "The Grid Portal Stairs Paint Gun: Black [Riku]": KHDDDLocationData(
        region="The Grid [Riku]",
        code=2650581,
    ),
    "The Grid Portal Stairs Drop-Me-Not [Riku]": KHDDDLocationData(
        region="The Grid [Riku]",
        code=2650582,
    ),
    "The Grid Portal Stairs Hi-Potion [Riku]": KHDDDLocationData(
        region="The Grid [Riku]",
        code=2650583,
    ),
    "The World That Never Was Delusive Beginning Dream Candy [Riku]": KHDDDLocationData(
        region="The World That Never Was [Riku]",
        code=2650584,
    ),
    "The World That Never Was Delusive Beginning Elixir [Riku]": KHDDDLocationData(
        region="The World That Never Was [Riku]",
        code=2650585,
    ),
    "The World That Never Was Delusive Beginning Confetti Candy 3 [Riku]": KHDDDLocationData(
        region="The World That Never Was [Riku]",
        code=2650586,
    ),
    "The World That Never Was Delusive Beginning Dulcet Fantasy [Riku]": KHDDDLocationData(
        region="The World That Never Was [Riku]",
        code=2650587,
    ),
    "The World That Never Was Delusive Beginning Dark Splicer [Riku]": KHDDDLocationData(
        region="The World That Never Was [Riku]",
        code=2650588,
    ),
    "The World That Never Was Delusive Beginning Second Dream Candy [Riku]": KHDDDLocationData(
        region="The World That Never Was [Riku]",
        code=2650589
    ),
    "The World That Never Was Walk of Delusions Ice Dream Cone 3 [Riku]": KHDDDLocationData(
        region="The World That Never Was [Riku]",
        code=2650590,
    ),
    "The World That Never Was Walk of Delusions Drop-Me-Not [Riku]": KHDDDLocationData(
        region="The World That Never Was [Riku]",
        code=2650591,
    ),
    "The World That Never Was Walk of Delusions Lofty Fantasy [Riku]": KHDDDLocationData(
        region="The World That Never Was [Riku]",
        code=2650592,
    ),
    "The World That Never Was Fact Within Fiction Spark Raid [Riku]": KHDDDLocationData(
        region="The World That Never Was [Riku]",
        code=2650593,
    ),
    "The World That Never Was Fact Within Fiction Intrepid Fancy [Riku]": KHDDDLocationData(
        region="The World That Never Was [Riku]",
        code=2650594,
    ),
    "The World That Never Was Fact Within Fiction Royal Cake [Riku]": KHDDDLocationData(
        region="The World That Never Was [Riku]",
        code=2650595,
    ),
    "The World That Never Was Fact Within Fiction Block-It Chocolate 3 [Riku]": KHDDDLocationData(
        region="The World That Never Was [Riku]",
        code=2650596,
    ),
    "The World That Never Was Fact Within Fiction Mega-Potion [Riku]": KHDDDLocationData(
        region="The World That Never Was [Riku]",
        code=2650597,
    ),
    "The World That Never Was Verge of Chaos Elixir [Riku]": KHDDDLocationData(
        region="The World That Never Was [Riku]",
        code=2650598,
    ),
    "The World That Never Was Verge of Chaos Skelterwild Recipe [Riku]": KHDDDLocationData(
        region="The World That Never Was [Riku]",
        code=2650599,
    ),
    "The World That Never Was Verge of Chaos Candy Goggles [Riku]": KHDDDLocationData(
        region="The World That Never Was [Riku]",
        code=2650600,
    ),
    "The World That Never Was Verge of Chaos Wondrous Fantasy [Riku]": KHDDDLocationData(
        region="The World That Never Was [Riku]",
        code=2650601,
    ),
    "Prankster's Paradise Monstro: Mouth Ice Dream Cone 2 [Riku]": KHDDDLocationData(
        region="Prankster's Paradise [Riku]",
        code=2650602,
    ),
    "Prankster's Paradise Monstro: Mouth Paint Gun: Blue [Riku]": KHDDDLocationData(
        region="Prankster's Paradise [Riku]",
        code=2650603,
    ),
    "Prankster's Paradise Monstro: Mouth Balloon [Riku]": KHDDDLocationData(
        region="Prankster's Paradise [Riku]",
        code=2650604,
    ),
    "Prankster's Paradise Monstro: Mouth Panacea [Riku]": KHDDDLocationData(
        region="Prankster's Paradise [Riku]",
        code=2650605,
    ),
    "Prankster's Paradise Monstro: Belly Drop-Me-Not [Riku]": KHDDDLocationData(
        region="Prankster's Paradise [Riku]",
        code=2650606,
    ),
    "Prankster's Paradise Monstro: Belly Confetti Candy 2 [Riku]": KHDDDLocationData(
        region="Prankster's Paradise [Riku]",
        code=2650607,
    ),
    "Prankster's Paradise Monstro: Belly Block-It Chocolate 2 [Riku]": KHDDDLocationData(
        region="Prankster's Paradise [Riku]",
        code=2650608,
    ),
    "Prankster's Paradise Monstro: Belly Hi-Potion [Riku]": KHDDDLocationData(
        region="Prankster's Paradise [Riku]",
        code=2650609,
    ),
    "Prankster's Paradise Monstro: Belly Collision Magnet [Riku]": KHDDDLocationData(
        region="Prankster's Paradise [Riku]",
        code=2650610,
    ),
    "Prankster's Paradise Monstro: Gullet Shield Cookie 2 [Riku]": KHDDDLocationData(
        region="Prankster's Paradise [Riku]",
        code=2650611,
    ),
    "Prankster's Paradise Monstro: Gullet Sir Kyroo Recipe [Riku]": KHDDDLocationData(
        region="Prankster's Paradise [Riku]",
        code=2650612,
    ),
    "Prankster's Paradise Monstro: Gullet Charming Fantasy [Riku]": KHDDDLocationData(
        region="Prankster's Paradise [Riku]",
        code=2650613,
    ),
    "Prankster's Paradise Monstro: Gullet Mini [Riku]": KHDDDLocationData(
        region="Prankster's Paradise [Riku]",
        code=2650614,
    ),
    "Prankster's Paradise Monstro: Gullet Hi-Potion [Riku]": KHDDDLocationData(
        region="Prankster's Paradise [Riku]",
        code=2650615,
    ),
    "Prankster's Paradise Monstro: Gullet Second Shield Cookie 2 [Riku]": KHDDDLocationData(
        region="Prankster's Paradise [Riku]",
        code=2650616,
    ),
    "Prankster's Paradise Monstro: Cavity Confetti Candy 2 [Riku]": KHDDDLocationData(
        region="Prankster's Paradise [Riku]",
        code=2650617,
    ),
    "Prankster's Paradise Monstro: Cavity Royal Cake [Riku]": KHDDDLocationData(
        region="Prankster's Paradise [Riku]",
        code=2650618,
    ),
    "Prankster's Paradise Monstro: Cavity Water Barrel [Riku]": KHDDDLocationData(
        region="Prankster's Paradise [Riku]",
        code=2650619,
    ),
    "Prankster's Paradise Monstro: Cavity Drop-Me-Not [Riku]": KHDDDLocationData(
        region="Prankster's Paradise [Riku]",
        code=2650620,
    ),
    "Prankster's Paradise Monstro: Cavity Panacea [Riku]": KHDDDLocationData(
        region="Prankster's Paradise [Riku]",
        code=2650621,
    ),
    "La Cite des Cloches Windmill Shield Cookie [Riku]": KHDDDLocationData(
        region="La Cite des Cloches [Riku]",
        code=2650622,
    ),
    "Prankster's Paradise Monstro: Mouth Hi-Potion [Riku]": KHDDDLocationData(
        region="Prankster's Paradise [Riku]",
        code=2650623,
    ),
    "Prankster's Paradise Monstro: Gullet Candy Goggles [Riku]": KHDDDLocationData(
        region="Prankster's Paradise [Riku]",
        code=2650624,
    ),
    "Country of the Musketeers Green Room Stop [Riku]": KHDDDLocationData(
        region="Country of the Musketeers [Riku]",
        code=2650625
    ),
    "Country of the Musketeers Green Room Drop-Me-Not [Riku]": KHDDDLocationData(
        region="Country of the Musketeers [Riku]",
        code=2650626
    ),
    "Country of the Musketeers Green Room Confetti Candy 3 [Riku]": KHDDDLocationData(
        region="Country of the Musketeers [Riku]",
        code=2650627
    ),
    "The World That Never Was Verge of Chaos Paint Gun: Black [Riku]": KHDDDLocationData(
        region="The World That Never Was [Riku]",
        code=2650628,
    ),
    "The World That Never Was Verge of Chaos Shield Cookie 3 [Riku]": KHDDDLocationData(
        region="The World That Never Was [Riku]",
        code=2650629,
    ),
    "The World That Never Was Verge of Chaos Second Elixir [Riku]": KHDDDLocationData(
        region="The World That Never Was [Riku]",
        code=2650630,
    ),
    "Symphony of Sorcery Golden Wood Paint Gun: Red [Riku]": KHDDDLocationData(
        region="Symphony of Sorcery [Riku]",
        code=2650631,
    ),
    "Symphony of Sorcery Golden Wood Ryu Dragon Recipe [Riku]": KHDDDLocationData(
        region="Symphony of Sorcery [Riku]",
        code=2650632,
    ),
    "Symphony of Sorcery Moonlight Wood Mega-Potion [Riku]": KHDDDLocationData(
        region="Symphony of Sorcery [Riku]",
        code=2650633,
    ),
    "Symphony of Sorcery Moonlight Wood Drop-Me-Not [Riku]": KHDDDLocationData(
        region="Symphony of Sorcery [Riku]",
        code=2650634,
    ),
    "Symphony of Sorcery Moonlight Wood Intrepid Fancy [Riku]": KHDDDLocationData(
        region="Symphony of Sorcery [Riku]",
        code=2650635,
    ),
    "Symphony of Sorcery Snowgleam Wood Dulcet Fancy [Riku]": KHDDDLocationData(
        region="Symphony of Sorcery [Riku]",
        code=2650636,
    ),
    "Symphony of Sorcery Snowgleam Wood Confetti Candy 3 [Riku]": KHDDDLocationData(
        region="Symphony of Sorcery [Riku]",
        code=2650637,
    ),
    "Country of the Musketeers Machine Room Hi-Potion [Riku]": KHDDDLocationData(
        region="Country of the Musketeers [Riku]",
        code=2650638,
    ),
    "Country of the Musketeers Machine Room Mega-Potion [Riku]": KHDDDLocationData(
        region="Country of the Musketeers [Riku]",
        code=2650639,
    ),
    "Country of the Musketeers Backstage Drop-Me-Not [Riku]": KHDDDLocationData(
        region="Country of the Musketeers [Riku]",
        code=2650640,
    ),
    "Country of the Musketeers Backstage Mega-Potion [Riku]": KHDDDLocationData(
        region="Country of the Musketeers [Riku]",
        code=2650641,
    ),
    "The World That Never Was Fact Within Fiction Balloon [Riku]": KHDDDLocationData(
        region="The World That Never Was [Riku]",
        code=2650642,
    ),
    "The World That Never Was Fact Within Fiction Elixir [Riku]": KHDDDLocationData(
        region="The World That Never Was [Riku]",
        code=2650643,
    ),
    "The World That Never Was Delusive Beginning Second Elixir [Riku]": KHDDDLocationData(
        region="The World That Never Was [Riku]",
        code=2650644,
    ),
    "The World That Never Was Delusive Beginning Keeba Tiger Recipe [Riku]": KHDDDLocationData(
        region="The World That Never Was [Riku]",
        code=2650645,
    ),
    "The World That Never Was Delusive Beginning Curaga [Riku]": KHDDDLocationData(
        region="The World That Never Was [Riku]",
        code=2650646,
    ),
    "The World That Never Was Delusive Beginning Doubleflight [Riku]": KHDDDLocationData(
        region="The World That Never Was [Riku]",
        code=2650647,
    ),
    "The World That Never Was Delusive Beginning Third Elixir [Riku]": KHDDDLocationData(
        region="The World That Never Was [Riku]",
        code=2650648,
    ),

    #Lord Kyroo
    "La Cite des Cloches Nave Lord Kyroo Fight [Riku]": KHDDDLocationData(
        region="La Cite des Cloches [Riku]",
        code=2650649,
        category="Bonus"
    ),
    "Prankster's Paradise Promontory Lord Kyroo Fight [Sora]": KHDDDLocationData(
        region="Prankster's Paradise [Sora]",
        code=2650650,
        category="Bonus"
    ),
    "Symphony of Sorcery Moonlight Wood Lord Kyroo Fight [Riku]": KHDDDLocationData(
        region="Symphony of Sorcery [Riku]",
        code=2650651,
        category="Bonus"
    ),
    "Lord Kyroo Defeated [Sora] [Riku]": KHDDDLocationData(
        region="World Map [Sora]",
        code=2650652,
        category="Reward"
    ),

    #Link Boards
    "Meow Wow Node 01": KHDDDLocationData(region="World Map [Sora]", code=2690100, category="Board"),
    "Meow Wow Node 02": KHDDDLocationData(region="World Map [Sora]", code=2690101, category="Board"),
    "Meow Wow Node 03": KHDDDLocationData(region="World Map [Sora]", code=2690102, category="Board"),
    "Meow Wow Node 04": KHDDDLocationData(region="World Map [Sora]", code=2690103, category="Board"),
    "Meow Wow Node 05": KHDDDLocationData(region="World Map [Sora]", code=2690104, category="Board"),
    "Meow Wow Node 06": KHDDDLocationData(region="World Map [Sora]", code=2690105, category="Board"),
    "Meow Wow Node 07": KHDDDLocationData(region="World Map [Sora]", code=2690106, category="Board"),
    "Meow Wow Node 08": KHDDDLocationData(region="World Map [Sora]", code=2690107, category="Board"),
    "Meow Wow Node 09": KHDDDLocationData(region="World Map [Sora]", code=2690108, category="Board"),
    "Meow Wow Node 10": KHDDDLocationData(region="World Map [Sora]", code=2690109, category="Board"),
    "Meow Wow Node 11": KHDDDLocationData(region="World Map [Sora]", code=2690110, category="Board"),
    "Meow Wow Node 12": KHDDDLocationData(region="World Map [Sora]", code=2690111, category="Board"),
    "Meow Wow Node 13": KHDDDLocationData(region="World Map [Sora]", code=2690112, category="Board"),
    "Meow Wow Node 14": KHDDDLocationData(region="World Map [Sora]", code=2690113, category="Board"),
    "Meow Wow Node 15": KHDDDLocationData(region="World Map [Sora]", code=2690114, category="Board"),
    "Meow Wow Node 16": KHDDDLocationData(region="World Map [Sora]", code=2690115, category="Board"),

    "Tama Sheep Node 01": KHDDDLocationData(region="World Map [Sora]", code=2690200, category="Board"),
    "Tama Sheep Node 02": KHDDDLocationData(region="World Map [Sora]", code=2690201, category="Board"),
    "Tama Sheep Node 03": KHDDDLocationData(region="World Map [Sora]", code=2690202, category="Board"),
    "Tama Sheep Node 04": KHDDDLocationData(region="World Map [Sora]", code=2690203, category="Board"),
    "Tama Sheep Node 05": KHDDDLocationData(region="World Map [Sora]", code=2690204, category="Board"),
    "Tama Sheep Node 06": KHDDDLocationData(region="World Map [Sora]", code=2690205, category="Board"),
    "Tama Sheep Node 07": KHDDDLocationData(region="World Map [Sora]", code=2690206, category="Board"),
    "Tama Sheep Node 08": KHDDDLocationData(region="World Map [Sora]", code=2690207, category="Board"),
    "Tama Sheep Node 09": KHDDDLocationData(region="World Map [Sora]", code=2690208, category="Board"),
    "Tama Sheep Node 10": KHDDDLocationData(region="World Map [Sora]", code=2690209, category="Board"),
    "Tama Sheep Node 11": KHDDDLocationData(region="World Map [Sora]", code=2690210, category="Board"),
    "Tama Sheep Node 12": KHDDDLocationData(region="World Map [Sora]", code=2690211, category="Board"),
    "Tama Sheep Node 13": KHDDDLocationData(region="World Map [Sora]", code=2690212, category="Board"),
    "Tama Sheep Node 14": KHDDDLocationData(region="World Map [Sora]", code=2690213, category="Board"),
    "Tama Sheep Node 15": KHDDDLocationData(region="World Map [Sora]", code=2690214, category="Board"),
    "Tama Sheep Node 16": KHDDDLocationData(region="World Map [Sora]", code=2690215, category="Board"),

    "Yoggy Ram Node 01": KHDDDLocationData(region="World Map [Sora]", code=2690300, category="Board"),
    "Yoggy Ram Node 02": KHDDDLocationData(region="World Map [Sora]", code=2690301, category="Board"),
    "Yoggy Ram Node 03": KHDDDLocationData(region="World Map [Sora]", code=2690302, category="Board"),
    "Yoggy Ram Node 04": KHDDDLocationData(region="World Map [Sora]", code=2690303, category="Board"),
    "Yoggy Ram Node 05": KHDDDLocationData(region="World Map [Sora]", code=2690304, category="Board"),
    "Yoggy Ram Node 06": KHDDDLocationData(region="World Map [Sora]", code=2690305, category="Board"),
    "Yoggy Ram Node 07": KHDDDLocationData(region="World Map [Sora]", code=2690306, category="Board"),
    "Yoggy Ram Node 08": KHDDDLocationData(region="World Map [Sora]", code=2690307, category="Board"),
    "Yoggy Ram Node 09": KHDDDLocationData(region="World Map [Sora]", code=2690308, category="Board"),
    "Yoggy Ram Node 10": KHDDDLocationData(region="World Map [Sora]", code=2690309, category="Board"),
    "Yoggy Ram Node 11": KHDDDLocationData(region="World Map [Sora]", code=2690310, category="Board"),
    "Yoggy Ram Node 12": KHDDDLocationData(region="World Map [Sora]", code=2690311, category="Board"),
    "Yoggy Ram Node 13": KHDDDLocationData(region="World Map [Sora]", code=2690312, category="Board"),
    "Yoggy Ram Node 14": KHDDDLocationData(region="World Map [Sora]", code=2690313, category="Board"),
    "Yoggy Ram Node 15": KHDDDLocationData(region="World Map [Sora]", code=2690314, category="Board"),
    "Yoggy Ram Node 16": KHDDDLocationData(region="World Map [Sora]", code=2690315, category="Board"),

    "Komory Bat Node 01": KHDDDLocationData(region="World Map [Sora]", code=2690400, category="Board"),
    "Komory Bat Node 02": KHDDDLocationData(region="World Map [Sora]", code=2690401, category="Board"),
    "Komory Bat Node 03": KHDDDLocationData(region="World Map [Sora]", code=2690402, category="Board"),
    "Komory Bat Node 04": KHDDDLocationData(region="World Map [Sora]", code=2690403, category="Board"),
    "Komory Bat Node 05": KHDDDLocationData(region="World Map [Sora]", code=2690404, category="Board"),
    "Komory Bat Node 06": KHDDDLocationData(region="World Map [Sora]", code=2690405, category="Board"),
    "Komory Bat Node 07": KHDDDLocationData(region="World Map [Sora]", code=2690406, category="Board"),
    "Komory Bat Node 08": KHDDDLocationData(region="World Map [Sora]", code=2690407, category="Board"),
    "Komory Bat Node 09": KHDDDLocationData(region="World Map [Sora]", code=2690408, category="Board"),
    "Komory Bat Node 10": KHDDDLocationData(region="World Map [Sora]", code=2690409, category="Board"),
    "Komory Bat Node 11": KHDDDLocationData(region="World Map [Sora]", code=2690410, category="Board"),
    "Komory Bat Node 12": KHDDDLocationData(region="World Map [Sora]", code=2690411, category="Board"),
    "Komory Bat Node 13": KHDDDLocationData(region="World Map [Sora]", code=2690412, category="Board"),
    "Komory Bat Node 14": KHDDDLocationData(region="World Map [Sora]", code=2690413, category="Board"),
    "Komory Bat Node 15": KHDDDLocationData(region="World Map [Sora]", code=2690414, category="Board"),
    "Komory Bat Node 16": KHDDDLocationData(region="World Map [Sora]", code=2690415, category="Board"),

    "Pricklemane Node 01": KHDDDLocationData(region="World Map [Sora]", code=2690500, category="Board"),
    "Pricklemane Node 02": KHDDDLocationData(region="World Map [Sora]", code=2690501, category="Board"),
    "Pricklemane Node 03": KHDDDLocationData(region="World Map [Sora]", code=2690502, category="Board"),
    "Pricklemane Node 04": KHDDDLocationData(region="World Map [Sora]", code=2690503, category="Board"),
    "Pricklemane Node 05": KHDDDLocationData(region="World Map [Sora]", code=2690504, category="Board"),
    "Pricklemane Node 06": KHDDDLocationData(region="World Map [Sora]", code=2690505, category="Board"),
    "Pricklemane Node 07": KHDDDLocationData(region="World Map [Sora]", code=2690506, category="Board"),
    "Pricklemane Node 08": KHDDDLocationData(region="World Map [Sora]", code=2690507, category="Board"),
    "Pricklemane Node 09": KHDDDLocationData(region="World Map [Sora]", code=2690508, category="Board"),
    "Pricklemane Node 10": KHDDDLocationData(region="World Map [Sora]", code=2690509, category="Board"),
    "Pricklemane Node 11": KHDDDLocationData(region="World Map [Sora]", code=2690510, category="Board"),
    "Pricklemane Node 12": KHDDDLocationData(region="World Map [Sora]", code=2690511, category="Board"),
    "Pricklemane Node 13": KHDDDLocationData(region="World Map [Sora]", code=2690512, category="Board"),
    "Pricklemane Node 14": KHDDDLocationData(region="World Map [Sora]", code=2690513, category="Board"),
    "Pricklemane Node 15": KHDDDLocationData(region="World Map [Sora]", code=2690514, category="Board"),
    "Pricklemane Node 16": KHDDDLocationData(region="World Map [Sora]", code=2690515, category="Board"),

    "Hebby Repp Node 01": KHDDDLocationData(region="World Map [Sora]", code=2690600, category="Board"),
    "Hebby Repp Node 02": KHDDDLocationData(region="World Map [Sora]", code=2690601, category="Board"),
    "Hebby Repp Node 03": KHDDDLocationData(region="World Map [Sora]", code=2690602, category="Board"),
    "Hebby Repp Node 04": KHDDDLocationData(region="World Map [Sora]", code=2690603, category="Board"),
    "Hebby Repp Node 05": KHDDDLocationData(region="World Map [Sora]", code=2690604, category="Board"),
    "Hebby Repp Node 06": KHDDDLocationData(region="World Map [Sora]", code=2690605, category="Board"),
    "Hebby Repp Node 07": KHDDDLocationData(region="World Map [Sora]", code=2690606, category="Board"),
    "Hebby Repp Node 08": KHDDDLocationData(region="World Map [Sora]", code=2690607, category="Board"),
    "Hebby Repp Node 09": KHDDDLocationData(region="World Map [Sora]", code=2690608, category="Board"),
    "Hebby Repp Node 10": KHDDDLocationData(region="World Map [Sora]", code=2690609, category="Board"),
    "Hebby Repp Node 11": KHDDDLocationData(region="World Map [Sora]", code=2690610, category="Board"),
    "Hebby Repp Node 12": KHDDDLocationData(region="World Map [Sora]", code=2690611, category="Board"),
    "Hebby Repp Node 13": KHDDDLocationData(region="World Map [Sora]", code=2690612, category="Board"),
    "Hebby Repp Node 14": KHDDDLocationData(region="World Map [Sora]", code=2690613, category="Board"),
    "Hebby Repp Node 15": KHDDDLocationData(region="World Map [Sora]", code=2690614, category="Board"),
    "Hebby Repp Node 16": KHDDDLocationData(region="World Map [Sora]", code=2690615, category="Board"),

    "Sir Kyroo Node 01": KHDDDLocationData(region="World Map [Sora]", code=2690700, category="Board"),
    "Sir Kyroo Node 02": KHDDDLocationData(region="World Map [Sora]", code=2690701, category="Board"),
    "Sir Kyroo Node 03": KHDDDLocationData(region="World Map [Sora]", code=2690702, category="Board"),
    "Sir Kyroo Node 04": KHDDDLocationData(region="World Map [Sora]", code=2690703, category="Board"),
    "Sir Kyroo Node 05": KHDDDLocationData(region="World Map [Sora]", code=2690704, category="Board"),
    "Sir Kyroo Node 06": KHDDDLocationData(region="World Map [Sora]", code=2690705, category="Board"),
    "Sir Kyroo Node 07": KHDDDLocationData(region="World Map [Sora]", code=2690706, category="Board"),
    "Sir Kyroo Node 08": KHDDDLocationData(region="World Map [Sora]", code=2690707, category="Board"),
    "Sir Kyroo Node 09": KHDDDLocationData(region="World Map [Sora]", code=2690708, category="Board"),
    "Sir Kyroo Node 10": KHDDDLocationData(region="World Map [Sora]", code=2690709, category="Board"),
    "Sir Kyroo Node 11": KHDDDLocationData(region="World Map [Sora]", code=2690710, category="Board"),
    "Sir Kyroo Node 12": KHDDDLocationData(region="World Map [Sora]", code=2690711, category="Board"),
    "Sir Kyroo Node 13": KHDDDLocationData(region="World Map [Sora]", code=2690712, category="Board"),
    "Sir Kyroo Node 14": KHDDDLocationData(region="World Map [Sora]", code=2690713, category="Board"),
    "Sir Kyroo Node 15": KHDDDLocationData(region="World Map [Sora]", code=2690714, category="Board"),
    "Sir Kyroo Node 16": KHDDDLocationData(region="World Map [Sora]", code=2690715, category="Board"),

    "Toximander Node 01": KHDDDLocationData(region="World Map [Sora]", code=2690800, category="Board"),
    "Toximander Node 02": KHDDDLocationData(region="World Map [Sora]", code=2690801, category="Board"),
    "Toximander Node 03": KHDDDLocationData(region="World Map [Sora]", code=2690802, category="Board"),
    "Toximander Node 04": KHDDDLocationData(region="World Map [Sora]", code=2690803, category="Board"),
    "Toximander Node 05": KHDDDLocationData(region="World Map [Sora]", code=2690804, category="Board"),
    "Toximander Node 06": KHDDDLocationData(region="World Map [Sora]", code=2690805, category="Board"),
    "Toximander Node 07": KHDDDLocationData(region="World Map [Sora]", code=2690806, category="Board"),
    "Toximander Node 08": KHDDDLocationData(region="World Map [Sora]", code=2690807, category="Board"),
    "Toximander Node 09": KHDDDLocationData(region="World Map [Sora]", code=2690808, category="Board"),
    "Toximander Node 10": KHDDDLocationData(region="World Map [Sora]", code=2690809, category="Board"),
    "Toximander Node 11": KHDDDLocationData(region="World Map [Sora]", code=2690810, category="Board"),
    "Toximander Node 12": KHDDDLocationData(region="World Map [Sora]", code=2690811, category="Board"),
    "Toximander Node 13": KHDDDLocationData(region="World Map [Sora]", code=2690812, category="Board"),
    "Toximander Node 14": KHDDDLocationData(region="World Map [Sora]", code=2690813, category="Board"),
    "Toximander Node 15": KHDDDLocationData(region="World Map [Sora]", code=2690814, category="Board"),
    "Toximander Node 16": KHDDDLocationData(region="World Map [Sora]", code=2690815, category="Board"),

    "Fin Fatale Node 01": KHDDDLocationData(region="World Map [Sora]", code=2690900, category="Board"),
    "Fin Fatale Node 02": KHDDDLocationData(region="World Map [Sora]", code=2690901, category="Board"),
    "Fin Fatale Node 03": KHDDDLocationData(region="World Map [Sora]", code=2690902, category="Board"),
    "Fin Fatale Node 04": KHDDDLocationData(region="World Map [Sora]", code=2690903, category="Board"),
    "Fin Fatale Node 05": KHDDDLocationData(region="World Map [Sora]", code=2690904, category="Board"),
    "Fin Fatale Node 06": KHDDDLocationData(region="World Map [Sora]", code=2690905, category="Board"),
    "Fin Fatale Node 07": KHDDDLocationData(region="World Map [Sora]", code=2690906, category="Board"),
    "Fin Fatale Node 08": KHDDDLocationData(region="World Map [Sora]", code=2690907, category="Board"),
    "Fin Fatale Node 09": KHDDDLocationData(region="World Map [Sora]", code=2690908, category="Board"),
    "Fin Fatale Node 10": KHDDDLocationData(region="World Map [Sora]", code=2690909, category="Board"),
    "Fin Fatale Node 11": KHDDDLocationData(region="World Map [Sora]", code=2690910, category="Board"),
    "Fin Fatale Node 12": KHDDDLocationData(region="World Map [Sora]", code=2690911, category="Board"),
    "Fin Fatale Node 13": KHDDDLocationData(region="World Map [Sora]", code=2690912, category="Board"),
    "Fin Fatale Node 14": KHDDDLocationData(region="World Map [Sora]", code=2690913, category="Board"),
    "Fin Fatale Node 15": KHDDDLocationData(region="World Map [Sora]", code=2690914, category="Board"),
    "Fin Fatale Node 16": KHDDDLocationData(region="World Map [Sora]", code=2690915, category="Board"),

    "Tatsu Steed Node 01": KHDDDLocationData(region="World Map [Sora]", code=2691000, category="Board"),
    "Tatsu Steed Node 02": KHDDDLocationData(region="World Map [Sora]", code=2691001, category="Board"),
    "Tatsu Steed Node 03": KHDDDLocationData(region="World Map [Sora]", code=2691002, category="Board"),
    "Tatsu Steed Node 04": KHDDDLocationData(region="World Map [Sora]", code=2691003, category="Board"),
    "Tatsu Steed Node 05": KHDDDLocationData(region="World Map [Sora]", code=2691004, category="Board"),
    "Tatsu Steed Node 06": KHDDDLocationData(region="World Map [Sora]", code=2691005, category="Board"),
    "Tatsu Steed Node 07": KHDDDLocationData(region="World Map [Sora]", code=2691006, category="Board"),
    "Tatsu Steed Node 08": KHDDDLocationData(region="World Map [Sora]", code=2691007, category="Board"),
    "Tatsu Steed Node 09": KHDDDLocationData(region="World Map [Sora]", code=2691008, category="Board"),
    "Tatsu Steed Node 10": KHDDDLocationData(region="World Map [Sora]", code=2691009, category="Board"),
    "Tatsu Steed Node 11": KHDDDLocationData(region="World Map [Sora]", code=2691010, category="Board"),
    "Tatsu Steed Node 12": KHDDDLocationData(region="World Map [Sora]", code=2691011, category="Board"),
    "Tatsu Steed Node 13": KHDDDLocationData(region="World Map [Sora]", code=2691012, category="Board"),
    "Tatsu Steed Node 14": KHDDDLocationData(region="World Map [Sora]", code=2691013, category="Board"),
    "Tatsu Steed Node 15": KHDDDLocationData(region="World Map [Sora]", code=2691014, category="Board"),
    "Tatsu Steed Node 16": KHDDDLocationData(region="World Map [Sora]", code=2691015, category="Board"),

    "Necho Cat Node 01": KHDDDLocationData(region="World Map [Sora]", code=2691100, category="Board"),
    "Necho Cat Node 02": KHDDDLocationData(region="World Map [Sora]", code=2691101, category="Board"),
    "Necho Cat Node 03": KHDDDLocationData(region="World Map [Sora]", code=2691102, category="Board"),
    "Necho Cat Node 04": KHDDDLocationData(region="World Map [Sora]", code=2691103, category="Board"),
    "Necho Cat Node 05": KHDDDLocationData(region="World Map [Sora]", code=2691104, category="Board"),
    "Necho Cat Node 06": KHDDDLocationData(region="World Map [Sora]", code=2691105, category="Board"),
    "Necho Cat Node 07": KHDDDLocationData(region="World Map [Sora]", code=2691106, category="Board"),
    "Necho Cat Node 08": KHDDDLocationData(region="World Map [Sora]", code=2691107, category="Board"),
    "Necho Cat Node 09": KHDDDLocationData(region="World Map [Sora]", code=2691108, category="Board"),
    "Necho Cat Node 10": KHDDDLocationData(region="World Map [Sora]", code=2691109, category="Board"),
    "Necho Cat Node 11": KHDDDLocationData(region="World Map [Sora]", code=2691110, category="Board"),
    "Necho Cat Node 12": KHDDDLocationData(region="World Map [Sora]", code=2691111, category="Board"),
    "Necho Cat Node 13": KHDDDLocationData(region="World Map [Sora]", code=2691112, category="Board"),
    "Necho Cat Node 14": KHDDDLocationData(region="World Map [Sora]", code=2691113, category="Board"),
    "Necho Cat Node 15": KHDDDLocationData(region="World Map [Sora]", code=2691114, category="Board"),
    "Necho Cat Node 16": KHDDDLocationData(region="World Map [Sora]", code=2691115, category="Board"),

    "Thunderaffe Node 01": KHDDDLocationData(region="World Map [Sora]", code=2691200, category="Board"),
    "Thunderaffe Node 02": KHDDDLocationData(region="World Map [Sora]", code=2691201, category="Board"),
    "Thunderaffe Node 03": KHDDDLocationData(region="World Map [Sora]", code=2691202, category="Board"),
    "Thunderaffe Node 04": KHDDDLocationData(region="World Map [Sora]", code=2691203, category="Board"),
    "Thunderaffe Node 05": KHDDDLocationData(region="World Map [Sora]", code=2691204, category="Board"),
    "Thunderaffe Node 06": KHDDDLocationData(region="World Map [Sora]", code=2691205, category="Board"),
    "Thunderaffe Node 07": KHDDDLocationData(region="World Map [Sora]", code=2691206, category="Board"),
    "Thunderaffe Node 08": KHDDDLocationData(region="World Map [Sora]", code=2691207, category="Board"),
    "Thunderaffe Node 09": KHDDDLocationData(region="World Map [Sora]", code=2691208, category="Board"),
    "Thunderaffe Node 10": KHDDDLocationData(region="World Map [Sora]", code=2691209, category="Board"),
    "Thunderaffe Node 11": KHDDDLocationData(region="World Map [Sora]", code=2691210, category="Board"),
    "Thunderaffe Node 12": KHDDDLocationData(region="World Map [Sora]", code=2691211, category="Board"),
    "Thunderaffe Node 13": KHDDDLocationData(region="World Map [Sora]", code=2691212, category="Board"),
    "Thunderaffe Node 14": KHDDDLocationData(region="World Map [Sora]", code=2691213, category="Board"),
    "Thunderaffe Node 15": KHDDDLocationData(region="World Map [Sora]", code=2691214, category="Board"),
    "Thunderaffe Node 16": KHDDDLocationData(region="World Map [Sora]", code=2691215, category="Board"),

    "Kooma Panda Node 01": KHDDDLocationData(region="World Map [Sora]", code=2691300, category="Board"),
    "Kooma Panda Node 02": KHDDDLocationData(region="World Map [Sora]", code=2691301, category="Board"),
    "Kooma Panda Node 03": KHDDDLocationData(region="World Map [Sora]", code=2691302, category="Board"),
    "Kooma Panda Node 04": KHDDDLocationData(region="World Map [Sora]", code=2691303, category="Board"),
    "Kooma Panda Node 05": KHDDDLocationData(region="World Map [Sora]", code=2691304, category="Board"),
    "Kooma Panda Node 06": KHDDDLocationData(region="World Map [Sora]", code=2691305, category="Board"),
    "Kooma Panda Node 07": KHDDDLocationData(region="World Map [Sora]", code=2691306, category="Board"),
    "Kooma Panda Node 08": KHDDDLocationData(region="World Map [Sora]", code=2691307, category="Board"),
    "Kooma Panda Node 09": KHDDDLocationData(region="World Map [Sora]", code=2691308, category="Board"),
    "Kooma Panda Node 10": KHDDDLocationData(region="World Map [Sora]", code=2691309, category="Board"),
    "Kooma Panda Node 11": KHDDDLocationData(region="World Map [Sora]", code=2691310, category="Board"),
    "Kooma Panda Node 12": KHDDDLocationData(region="World Map [Sora]", code=2691311, category="Board"),
    "Kooma Panda Node 13": KHDDDLocationData(region="World Map [Sora]", code=2691312, category="Board"),
    "Kooma Panda Node 14": KHDDDLocationData(region="World Map [Sora]", code=2691313, category="Board"),
    "Kooma Panda Node 15": KHDDDLocationData(region="World Map [Sora]", code=2691314, category="Board"),
    "Kooma Panda Node 16": KHDDDLocationData(region="World Map [Sora]", code=2691315, category="Board"),

    "Pegaslick Node 01": KHDDDLocationData(region="World Map [Sora]", code=2691400, category="Board"),
    "Pegaslick Node 02": KHDDDLocationData(region="World Map [Sora]", code=2691401, category="Board"),
    "Pegaslick Node 03": KHDDDLocationData(region="World Map [Sora]", code=2691402, category="Board"),
    "Pegaslick Node 04": KHDDDLocationData(region="World Map [Sora]", code=2691403, category="Board"),
    "Pegaslick Node 05": KHDDDLocationData(region="World Map [Sora]", code=2691404, category="Board"),
    "Pegaslick Node 06": KHDDDLocationData(region="World Map [Sora]", code=2691405, category="Board"),
    "Pegaslick Node 07": KHDDDLocationData(region="World Map [Sora]", code=2691406, category="Board"),
    "Pegaslick Node 08": KHDDDLocationData(region="World Map [Sora]", code=2691407, category="Board"),
    "Pegaslick Node 09": KHDDDLocationData(region="World Map [Sora]", code=2691408, category="Board"),
    "Pegaslick Node 10": KHDDDLocationData(region="World Map [Sora]", code=2691409, category="Board"),
    "Pegaslick Node 11": KHDDDLocationData(region="World Map [Sora]", code=2691410, category="Board"),
    "Pegaslick Node 12": KHDDDLocationData(region="World Map [Sora]", code=2691411, category="Board"),
    "Pegaslick Node 13": KHDDDLocationData(region="World Map [Sora]", code=2691412, category="Board"),
    "Pegaslick Node 14": KHDDDLocationData(region="World Map [Sora]", code=2691413, category="Board"),
    "Pegaslick Node 15": KHDDDLocationData(region="World Map [Sora]", code=2691414, category="Board"),
    "Pegaslick Node 16": KHDDDLocationData(region="World Map [Sora]", code=2691415, category="Board"),

    "Iceguin Ace Node 01": KHDDDLocationData(region="World Map [Sora]", code=2691500, category="Board"),
    "Iceguin Ace Node 02": KHDDDLocationData(region="World Map [Sora]", code=2691501, category="Board"),
    "Iceguin Ace Node 03": KHDDDLocationData(region="World Map [Sora]", code=2691502, category="Board"),
    "Iceguin Ace Node 04": KHDDDLocationData(region="World Map [Sora]", code=2691503, category="Board"),
    "Iceguin Ace Node 05": KHDDDLocationData(region="World Map [Sora]", code=2691504, category="Board"),
    "Iceguin Ace Node 06": KHDDDLocationData(region="World Map [Sora]", code=2691505, category="Board"),
    "Iceguin Ace Node 07": KHDDDLocationData(region="World Map [Sora]", code=2691506, category="Board"),
    "Iceguin Ace Node 08": KHDDDLocationData(region="World Map [Sora]", code=2691507, category="Board"),
    "Iceguin Ace Node 09": KHDDDLocationData(region="World Map [Sora]", code=2691508, category="Board"),
    "Iceguin Ace Node 10": KHDDDLocationData(region="World Map [Sora]", code=2691509, category="Board"),
    "Iceguin Ace Node 11": KHDDDLocationData(region="World Map [Sora]", code=2691510, category="Board"),
    "Iceguin Ace Node 12": KHDDDLocationData(region="World Map [Sora]", code=2691511, category="Board"),
    "Iceguin Ace Node 13": KHDDDLocationData(region="World Map [Sora]", code=2691512, category="Board"),
    "Iceguin Ace Node 14": KHDDDLocationData(region="World Map [Sora]", code=2691513, category="Board"),
    "Iceguin Ace Node 15": KHDDDLocationData(region="World Map [Sora]", code=2691514, category="Board"),
    "Iceguin Ace Node 16": KHDDDLocationData(region="World Map [Sora]", code=2691515, category="Board"),

    "Peepsta Hoo Node 01": KHDDDLocationData(region="World Map [Sora]", code=2691600, category="Board"),
    "Peepsta Hoo Node 02": KHDDDLocationData(region="World Map [Sora]", code=2691601, category="Board"),
    "Peepsta Hoo Node 03": KHDDDLocationData(region="World Map [Sora]", code=2691602, category="Board"),
    "Peepsta Hoo Node 04": KHDDDLocationData(region="World Map [Sora]", code=2691603, category="Board"),
    "Peepsta Hoo Node 05": KHDDDLocationData(region="World Map [Sora]", code=2691604, category="Board"),
    "Peepsta Hoo Node 06": KHDDDLocationData(region="World Map [Sora]", code=2691605, category="Board"),
    "Peepsta Hoo Node 07": KHDDDLocationData(region="World Map [Sora]", code=2691606, category="Board"),
    "Peepsta Hoo Node 08": KHDDDLocationData(region="World Map [Sora]", code=2691607, category="Board"),
    "Peepsta Hoo Node 09": KHDDDLocationData(region="World Map [Sora]", code=2691608, category="Board"),
    "Peepsta Hoo Node 10": KHDDDLocationData(region="World Map [Sora]", code=2691609, category="Board"),
    "Peepsta Hoo Node 11": KHDDDLocationData(region="World Map [Sora]", code=2691610, category="Board"),
    "Peepsta Hoo Node 12": KHDDDLocationData(region="World Map [Sora]", code=2691611, category="Board"),
    "Peepsta Hoo Node 13": KHDDDLocationData(region="World Map [Sora]", code=2691612, category="Board"),
    "Peepsta Hoo Node 14": KHDDDLocationData(region="World Map [Sora]", code=2691613, category="Board"),
    "Peepsta Hoo Node 15": KHDDDLocationData(region="World Map [Sora]", code=2691614, category="Board"),
    "Peepsta Hoo Node 16": KHDDDLocationData(region="World Map [Sora]", code=2691615, category="Board"),

    "Escarglow Node 01": KHDDDLocationData(region="World Map [Sora]", code=2691700, category="Board"),
    "Escarglow Node 02": KHDDDLocationData(region="World Map [Sora]", code=2691701, category="Board"),
    "Escarglow Node 03": KHDDDLocationData(region="World Map [Sora]", code=2691702, category="Board"),
    "Escarglow Node 04": KHDDDLocationData(region="World Map [Sora]", code=2691703, category="Board"),
    "Escarglow Node 05": KHDDDLocationData(region="World Map [Sora]", code=2691704, category="Board"),
    "Escarglow Node 06": KHDDDLocationData(region="World Map [Sora]", code=2691705, category="Board"),
    "Escarglow Node 07": KHDDDLocationData(region="World Map [Sora]", code=2691706, category="Board"),
    "Escarglow Node 08": KHDDDLocationData(region="World Map [Sora]", code=2691707, category="Board"),
    "Escarglow Node 09": KHDDDLocationData(region="World Map [Sora]", code=2691708, category="Board"),
    "Escarglow Node 10": KHDDDLocationData(region="World Map [Sora]", code=2691709, category="Board"),
    "Escarglow Node 11": KHDDDLocationData(region="World Map [Sora]", code=2691710, category="Board"),
    "Escarglow Node 12": KHDDDLocationData(region="World Map [Sora]", code=2691711, category="Board"),
    "Escarglow Node 13": KHDDDLocationData(region="World Map [Sora]", code=2691712, category="Board"),
    "Escarglow Node 14": KHDDDLocationData(region="World Map [Sora]", code=2691713, category="Board"),
    "Escarglow Node 15": KHDDDLocationData(region="World Map [Sora]", code=2691714, category="Board"),
    "Escarglow Node 16": KHDDDLocationData(region="World Map [Sora]", code=2691715, category="Board"),

    "KO Kabuto Node 01": KHDDDLocationData(region="World Map [Sora]", code=2691800, category="Board"),
    "KO Kabuto Node 02": KHDDDLocationData(region="World Map [Sora]", code=2691801, category="Board"),
    "KO Kabuto Node 03": KHDDDLocationData(region="World Map [Sora]", code=2691802, category="Board"),
    "KO Kabuto Node 04": KHDDDLocationData(region="World Map [Sora]", code=2691803, category="Board"),
    "KO Kabuto Node 05": KHDDDLocationData(region="World Map [Sora]", code=2691804, category="Board"),
    "KO Kabuto Node 06": KHDDDLocationData(region="World Map [Sora]", code=2691805, category="Board"),
    "KO Kabuto Node 07": KHDDDLocationData(region="World Map [Sora]", code=2691806, category="Board"),
    "KO Kabuto Node 08": KHDDDLocationData(region="World Map [Sora]", code=2691807, category="Board"),
    "KO Kabuto Node 09": KHDDDLocationData(region="World Map [Sora]", code=2691808, category="Board"),
    "KO Kabuto Node 10": KHDDDLocationData(region="World Map [Sora]", code=2691809, category="Board"),
    "KO Kabuto Node 11": KHDDDLocationData(region="World Map [Sora]", code=2691810, category="Board"),
    "KO Kabuto Node 12": KHDDDLocationData(region="World Map [Sora]", code=2691811, category="Board"),
    "KO Kabuto Node 13": KHDDDLocationData(region="World Map [Sora]", code=2691812, category="Board"),
    "KO Kabuto Node 14": KHDDDLocationData(region="World Map [Sora]", code=2691813, category="Board"),
    "KO Kabuto Node 15": KHDDDLocationData(region="World Map [Sora]", code=2691814, category="Board"),
    "KO Kabuto Node 16": KHDDDLocationData(region="World Map [Sora]", code=2691815, category="Board"),

    "Wheeflower Node 01": KHDDDLocationData(region="World Map [Sora]", code=2691900, category="Board"),
    "Wheeflower Node 02": KHDDDLocationData(region="World Map [Sora]", code=2691901, category="Board"),
    "Wheeflower Node 03": KHDDDLocationData(region="World Map [Sora]", code=2691902, category="Board"),
    "Wheeflower Node 04": KHDDDLocationData(region="World Map [Sora]", code=2691903, category="Board"),
    "Wheeflower Node 05": KHDDDLocationData(region="World Map [Sora]", code=2691904, category="Board"),
    "Wheeflower Node 06": KHDDDLocationData(region="World Map [Sora]", code=2691905, category="Board"),
    "Wheeflower Node 07": KHDDDLocationData(region="World Map [Sora]", code=2691906, category="Board"),
    "Wheeflower Node 08": KHDDDLocationData(region="World Map [Sora]", code=2691907, category="Board"),
    "Wheeflower Node 09": KHDDDLocationData(region="World Map [Sora]", code=2691908, category="Board"),
    "Wheeflower Node 10": KHDDDLocationData(region="World Map [Sora]", code=2691909, category="Board"),
    "Wheeflower Node 11": KHDDDLocationData(region="World Map [Sora]", code=2691910, category="Board"),
    "Wheeflower Node 12": KHDDDLocationData(region="World Map [Sora]", code=2691911, category="Board"),
    "Wheeflower Node 13": KHDDDLocationData(region="World Map [Sora]", code=2691912, category="Board"),
    "Wheeflower Node 14": KHDDDLocationData(region="World Map [Sora]", code=2691913, category="Board"),
    "Wheeflower Node 15": KHDDDLocationData(region="World Map [Sora]", code=2691914, category="Board"),
    "Wheeflower Node 16": KHDDDLocationData(region="World Map [Sora]", code=2691915, category="Board"),

    "Ghostabocky Node 01": KHDDDLocationData(region="World Map [Sora]", code=2692000, category="Board"),
    "Ghostabocky Node 02": KHDDDLocationData(region="World Map [Sora]", code=2692001, category="Board"),
    "Ghostabocky Node 03": KHDDDLocationData(region="World Map [Sora]", code=2692002, category="Board"),
    "Ghostabocky Node 04": KHDDDLocationData(region="World Map [Sora]", code=2692003, category="Board"),
    "Ghostabocky Node 05": KHDDDLocationData(region="World Map [Sora]", code=2692004, category="Board"),
    "Ghostabocky Node 06": KHDDDLocationData(region="World Map [Sora]", code=2692005, category="Board"),
    "Ghostabocky Node 07": KHDDDLocationData(region="World Map [Sora]", code=2692006, category="Board"),
    "Ghostabocky Node 08": KHDDDLocationData(region="World Map [Sora]", code=2692007, category="Board"),
    "Ghostabocky Node 09": KHDDDLocationData(region="World Map [Sora]", code=2692008, category="Board"),
    "Ghostabocky Node 10": KHDDDLocationData(region="World Map [Sora]", code=2692009, category="Board"),
    "Ghostabocky Node 11": KHDDDLocationData(region="World Map [Sora]", code=2692010, category="Board"),
    "Ghostabocky Node 12": KHDDDLocationData(region="World Map [Sora]", code=2692011, category="Board"),
    "Ghostabocky Node 13": KHDDDLocationData(region="World Map [Sora]", code=2692012, category="Board"),
    "Ghostabocky Node 14": KHDDDLocationData(region="World Map [Sora]", code=2692013, category="Board"),
    "Ghostabocky Node 15": KHDDDLocationData(region="World Map [Sora]", code=2692014, category="Board"),
    "Ghostabocky Node 16": KHDDDLocationData(region="World Map [Sora]", code=2692015, category="Board"),

    "Zolephant Node 01": KHDDDLocationData(region="World Map [Sora]", code=2692100, category="Board"),
    "Zolephant Node 02": KHDDDLocationData(region="World Map [Sora]", code=2692101, category="Board"),
    "Zolephant Node 03": KHDDDLocationData(region="World Map [Sora]", code=2692102, category="Board"),
    "Zolephant Node 04": KHDDDLocationData(region="World Map [Sora]", code=2692103, category="Board"),
    "Zolephant Node 05": KHDDDLocationData(region="World Map [Sora]", code=2692104, category="Board"),
    "Zolephant Node 06": KHDDDLocationData(region="World Map [Sora]", code=2692105, category="Board"),
    "Zolephant Node 07": KHDDDLocationData(region="World Map [Sora]", code=2692106, category="Board"),
    "Zolephant Node 08": KHDDDLocationData(region="World Map [Sora]", code=2692107, category="Board"),
    "Zolephant Node 09": KHDDDLocationData(region="World Map [Sora]", code=2692108, category="Board"),
    "Zolephant Node 10": KHDDDLocationData(region="World Map [Sora]", code=2692109, category="Board"),
    "Zolephant Node 11": KHDDDLocationData(region="World Map [Sora]", code=2692110, category="Board"),
    "Zolephant Node 12": KHDDDLocationData(region="World Map [Sora]", code=2692111, category="Board"),
    "Zolephant Node 13": KHDDDLocationData(region="World Map [Sora]", code=2692112, category="Board"),
    "Zolephant Node 14": KHDDDLocationData(region="World Map [Sora]", code=2692113, category="Board"),
    "Zolephant Node 15": KHDDDLocationData(region="World Map [Sora]", code=2692114, category="Board"),
    "Zolephant Node 16": KHDDDLocationData(region="World Map [Sora]", code=2692115, category="Board"),

    "Juggle Pup Node 01": KHDDDLocationData(region="World Map [Sora]", code=2692200, category="Board"),
    "Juggle Pup Node 02": KHDDDLocationData(region="World Map [Sora]", code=2692201, category="Board"),
    "Juggle Pup Node 03": KHDDDLocationData(region="World Map [Sora]", code=2692202, category="Board"),
    "Juggle Pup Node 04": KHDDDLocationData(region="World Map [Sora]", code=2692203, category="Board"),
    "Juggle Pup Node 05": KHDDDLocationData(region="World Map [Sora]", code=2692204, category="Board"),
    "Juggle Pup Node 06": KHDDDLocationData(region="World Map [Sora]", code=2692205, category="Board"),
    "Juggle Pup Node 07": KHDDDLocationData(region="World Map [Sora]", code=2692206, category="Board"),
    "Juggle Pup Node 08": KHDDDLocationData(region="World Map [Sora]", code=2692207, category="Board"),
    "Juggle Pup Node 09": KHDDDLocationData(region="World Map [Sora]", code=2692208, category="Board"),
    "Juggle Pup Node 10": KHDDDLocationData(region="World Map [Sora]", code=2692209, category="Board"),
    "Juggle Pup Node 11": KHDDDLocationData(region="World Map [Sora]", code=2692210, category="Board"),
    "Juggle Pup Node 12": KHDDDLocationData(region="World Map [Sora]", code=2692211, category="Board"),
    "Juggle Pup Node 13": KHDDDLocationData(region="World Map [Sora]", code=2692212, category="Board"),
    "Juggle Pup Node 14": KHDDDLocationData(region="World Map [Sora]", code=2692213, category="Board"),
    "Juggle Pup Node 15": KHDDDLocationData(region="World Map [Sora]", code=2692214, category="Board"),
    "Juggle Pup Node 16": KHDDDLocationData(region="World Map [Sora]", code=2692215, category="Board"),

    "Halbird Node 01": KHDDDLocationData(region="World Map [Sora]", code=2692300, category="Board"),
    "Halbird Node 02": KHDDDLocationData(region="World Map [Sora]", code=2692301, category="Board"),
    "Halbird Node 03": KHDDDLocationData(region="World Map [Sora]", code=2692302, category="Board"),
    "Halbird Node 04": KHDDDLocationData(region="World Map [Sora]", code=2692303, category="Board"),
    "Halbird Node 05": KHDDDLocationData(region="World Map [Sora]", code=2692304, category="Board"),
    "Halbird Node 06": KHDDDLocationData(region="World Map [Sora]", code=2692305, category="Board"),
    "Halbird Node 07": KHDDDLocationData(region="World Map [Sora]", code=2692306, category="Board"),
    "Halbird Node 08": KHDDDLocationData(region="World Map [Sora]", code=2692307, category="Board"),
    "Halbird Node 09": KHDDDLocationData(region="World Map [Sora]", code=2692308, category="Board"),
    "Halbird Node 10": KHDDDLocationData(region="World Map [Sora]", code=2692309, category="Board"),
    "Halbird Node 11": KHDDDLocationData(region="World Map [Sora]", code=2692310, category="Board"),
    "Halbird Node 12": KHDDDLocationData(region="World Map [Sora]", code=2692311, category="Board"),
    "Halbird Node 13": KHDDDLocationData(region="World Map [Sora]", code=2692312, category="Board"),
    "Halbird Node 14": KHDDDLocationData(region="World Map [Sora]", code=2692313, category="Board"),
    "Halbird Node 15": KHDDDLocationData(region="World Map [Sora]", code=2692314, category="Board"),
    "Halbird Node 16": KHDDDLocationData(region="World Map [Sora]", code=2692315, category="Board"),

    "Staggerceps Node 01": KHDDDLocationData(region="World Map [Sora]", code=2692400, category="Board"),
    "Staggerceps Node 02": KHDDDLocationData(region="World Map [Sora]", code=2692401, category="Board"),
    "Staggerceps Node 03": KHDDDLocationData(region="World Map [Sora]", code=2692402, category="Board"),
    "Staggerceps Node 04": KHDDDLocationData(region="World Map [Sora]", code=2692403, category="Board"),
    "Staggerceps Node 05": KHDDDLocationData(region="World Map [Sora]", code=2692404, category="Board"),
    "Staggerceps Node 06": KHDDDLocationData(region="World Map [Sora]", code=2692405, category="Board"),
    "Staggerceps Node 07": KHDDDLocationData(region="World Map [Sora]", code=2692406, category="Board"),
    "Staggerceps Node 08": KHDDDLocationData(region="World Map [Sora]", code=2692407, category="Board"),
    "Staggerceps Node 09": KHDDDLocationData(region="World Map [Sora]", code=2692408, category="Board"),
    "Staggerceps Node 10": KHDDDLocationData(region="World Map [Sora]", code=2692409, category="Board"),
    "Staggerceps Node 11": KHDDDLocationData(region="World Map [Sora]", code=2692410, category="Board"),
    "Staggerceps Node 12": KHDDDLocationData(region="World Map [Sora]", code=2692411, category="Board"),
    "Staggerceps Node 13": KHDDDLocationData(region="World Map [Sora]", code=2692412, category="Board"),
    "Staggerceps Node 14": KHDDDLocationData(region="World Map [Sora]", code=2692413, category="Board"),
    "Staggerceps Node 15": KHDDDLocationData(region="World Map [Sora]", code=2692414, category="Board"),
    "Staggerceps Node 16": KHDDDLocationData(region="World Map [Sora]", code=2692415, category="Board"),

    "Fishbone Node 01": KHDDDLocationData(region="World Map [Sora]", code=2692500, category="Board"),
    "Fishbone Node 02": KHDDDLocationData(region="World Map [Sora]", code=2692501, category="Board"),
    "Fishbone Node 03": KHDDDLocationData(region="World Map [Sora]", code=2692502, category="Board"),
    "Fishbone Node 04": KHDDDLocationData(region="World Map [Sora]", code=2692503, category="Board"),
    "Fishbone Node 05": KHDDDLocationData(region="World Map [Sora]", code=2692504, category="Board"),
    "Fishbone Node 06": KHDDDLocationData(region="World Map [Sora]", code=2692505, category="Board"),
    "Fishbone Node 07": KHDDDLocationData(region="World Map [Sora]", code=2692506, category="Board"),
    "Fishbone Node 08": KHDDDLocationData(region="World Map [Sora]", code=2692507, category="Board"),
    "Fishbone Node 09": KHDDDLocationData(region="World Map [Sora]", code=2692508, category="Board"),
    "Fishbone Node 10": KHDDDLocationData(region="World Map [Sora]", code=2692509, category="Board"),
    "Fishbone Node 11": KHDDDLocationData(region="World Map [Sora]", code=2692510, category="Board"),
    "Fishbone Node 12": KHDDDLocationData(region="World Map [Sora]", code=2692511, category="Board"),
    "Fishbone Node 13": KHDDDLocationData(region="World Map [Sora]", code=2692512, category="Board"),
    "Fishbone Node 14": KHDDDLocationData(region="World Map [Sora]", code=2692513, category="Board"),
    "Fishbone Node 15": KHDDDLocationData(region="World Map [Sora]", code=2692514, category="Board"),
    "Fishbone Node 16": KHDDDLocationData(region="World Map [Sora]", code=2692515, category="Board"),

    "Flowbermeow Node 01": KHDDDLocationData(region="World Map [Sora]", code=2692600, category="Board"),
    "Flowbermeow Node 02": KHDDDLocationData(region="World Map [Sora]", code=2692601, category="Board"),
    "Flowbermeow Node 03": KHDDDLocationData(region="World Map [Sora]", code=2692602, category="Board"),
    "Flowbermeow Node 04": KHDDDLocationData(region="World Map [Sora]", code=2692603, category="Board"),
    "Flowbermeow Node 05": KHDDDLocationData(region="World Map [Sora]", code=2692604, category="Board"),
    "Flowbermeow Node 06": KHDDDLocationData(region="World Map [Sora]", code=2692605, category="Board"),
    "Flowbermeow Node 07": KHDDDLocationData(region="World Map [Sora]", code=2692606, category="Board"),
    "Flowbermeow Node 08": KHDDDLocationData(region="World Map [Sora]", code=2692607, category="Board"),
    "Flowbermeow Node 09": KHDDDLocationData(region="World Map [Sora]", code=2692608, category="Board"),
    "Flowbermeow Node 10": KHDDDLocationData(region="World Map [Sora]", code=2692609, category="Board"),
    "Flowbermeow Node 11": KHDDDLocationData(region="World Map [Sora]", code=2692610, category="Board"),
    "Flowbermeow Node 12": KHDDDLocationData(region="World Map [Sora]", code=2692611, category="Board"),
    "Flowbermeow Node 13": KHDDDLocationData(region="World Map [Sora]", code=2692612, category="Board"),
    "Flowbermeow Node 14": KHDDDLocationData(region="World Map [Sora]", code=2692613, category="Board"),
    "Flowbermeow Node 15": KHDDDLocationData(region="World Map [Sora]", code=2692614, category="Board"),
    "Flowbermeow Node 16": KHDDDLocationData(region="World Map [Sora]", code=2692615, category="Board"),

    "Cyber Yog Node 01": KHDDDLocationData(region="World Map [Sora]", code=2692700, category="Board"),
    "Cyber Yog Node 02": KHDDDLocationData(region="World Map [Sora]", code=2692701, category="Board"),
    "Cyber Yog Node 03": KHDDDLocationData(region="World Map [Sora]", code=2692702, category="Board"),
    "Cyber Yog Node 04": KHDDDLocationData(region="World Map [Sora]", code=2692703, category="Board"),
    "Cyber Yog Node 05": KHDDDLocationData(region="World Map [Sora]", code=2692704, category="Board"),
    "Cyber Yog Node 06": KHDDDLocationData(region="World Map [Sora]", code=2692705, category="Board"),
    "Cyber Yog Node 07": KHDDDLocationData(region="World Map [Sora]", code=2692706, category="Board"),
    "Cyber Yog Node 08": KHDDDLocationData(region="World Map [Sora]", code=2692707, category="Board"),
    "Cyber Yog Node 09": KHDDDLocationData(region="World Map [Sora]", code=2692708, category="Board"),
    "Cyber Yog Node 10": KHDDDLocationData(region="World Map [Sora]", code=2692709, category="Board"),
    "Cyber Yog Node 11": KHDDDLocationData(region="World Map [Sora]", code=2692710, category="Board"),
    "Cyber Yog Node 12": KHDDDLocationData(region="World Map [Sora]", code=2692711, category="Board"),
    "Cyber Yog Node 13": KHDDDLocationData(region="World Map [Sora]", code=2692712, category="Board"),
    "Cyber Yog Node 14": KHDDDLocationData(region="World Map [Sora]", code=2692713, category="Board"),
    "Cyber Yog Node 15": KHDDDLocationData(region="World Map [Sora]", code=2692714, category="Board"),
    "Cyber Yog Node 16": KHDDDLocationData(region="World Map [Sora]", code=2692715, category="Board"),

    "Chef Kyroo Node 01": KHDDDLocationData(region="World Map [Sora]", code=2692800, category="Board"),
    "Chef Kyroo Node 02": KHDDDLocationData(region="World Map [Sora]", code=2692801, category="Board"),
    "Chef Kyroo Node 03": KHDDDLocationData(region="World Map [Sora]", code=2692802, category="Board"),
    "Chef Kyroo Node 04": KHDDDLocationData(region="World Map [Sora]", code=2692803, category="Board"),
    "Chef Kyroo Node 05": KHDDDLocationData(region="World Map [Sora]", code=2692804, category="Board"),
    "Chef Kyroo Node 06": KHDDDLocationData(region="World Map [Sora]", code=2692805, category="Board"),
    "Chef Kyroo Node 07": KHDDDLocationData(region="World Map [Sora]", code=2692806, category="Board"),
    "Chef Kyroo Node 08": KHDDDLocationData(region="World Map [Sora]", code=2692807, category="Board"),
    "Chef Kyroo Node 09": KHDDDLocationData(region="World Map [Sora]", code=2692808, category="Board"),
    "Chef Kyroo Node 10": KHDDDLocationData(region="World Map [Sora]", code=2692809, category="Board"),
    "Chef Kyroo Node 11": KHDDDLocationData(region="World Map [Sora]", code=2692810, category="Board"),
    "Chef Kyroo Node 12": KHDDDLocationData(region="World Map [Sora]", code=2692811, category="Board"),
    "Chef Kyroo Node 13": KHDDDLocationData(region="World Map [Sora]", code=2692812, category="Board"),
    "Chef Kyroo Node 14": KHDDDLocationData(region="World Map [Sora]", code=2692813, category="Board"),
    "Chef Kyroo Node 15": KHDDDLocationData(region="World Map [Sora]", code=2692814, category="Board"),
    "Chef Kyroo Node 16": KHDDDLocationData(region="World Map [Sora]", code=2692815, category="Board"),

    "Lord Kyroo Node 01": KHDDDLocationData(region="World Map [Sora]", code=2692900, category="Board"),
    "Lord Kyroo Node 02": KHDDDLocationData(region="World Map [Sora]", code=2692901, category="Board"),
    "Lord Kyroo Node 03": KHDDDLocationData(region="World Map [Sora]", code=2692902, category="Board"),
    "Lord Kyroo Node 04": KHDDDLocationData(region="World Map [Sora]", code=2692903, category="Board"),
    "Lord Kyroo Node 05": KHDDDLocationData(region="World Map [Sora]", code=2692904, category="Board"),
    "Lord Kyroo Node 06": KHDDDLocationData(region="World Map [Sora]", code=2692905, category="Board"),
    "Lord Kyroo Node 07": KHDDDLocationData(region="World Map [Sora]", code=2692906, category="Board"),
    "Lord Kyroo Node 08": KHDDDLocationData(region="World Map [Sora]", code=2692907, category="Board"),
    "Lord Kyroo Node 09": KHDDDLocationData(region="World Map [Sora]", code=2692908, category="Board"),
    "Lord Kyroo Node 10": KHDDDLocationData(region="World Map [Sora]", code=2692909, category="Board"),
    "Lord Kyroo Node 11": KHDDDLocationData(region="World Map [Sora]", code=2692910, category="Board"),
    "Lord Kyroo Node 12": KHDDDLocationData(region="World Map [Sora]", code=2692911, category="Board"),
    "Lord Kyroo Node 13": KHDDDLocationData(region="World Map [Sora]", code=2692912, category="Board"),
    "Lord Kyroo Node 14": KHDDDLocationData(region="World Map [Sora]", code=2692913, category="Board"),
    "Lord Kyroo Node 15": KHDDDLocationData(region="World Map [Sora]", code=2692914, category="Board"),
    "Lord Kyroo Node 16": KHDDDLocationData(region="World Map [Sora]", code=2692915, category="Board"),

    "Tatsu Blaze Node 01": KHDDDLocationData(region="World Map [Sora]", code=2693000, category="Board"),
    "Tatsu Blaze Node 02": KHDDDLocationData(region="World Map [Sora]", code=2693001, category="Board"),
    "Tatsu Blaze Node 03": KHDDDLocationData(region="World Map [Sora]", code=2693002, category="Board"),
    "Tatsu Blaze Node 04": KHDDDLocationData(region="World Map [Sora]", code=2693003, category="Board"),
    "Tatsu Blaze Node 05": KHDDDLocationData(region="World Map [Sora]", code=2693004, category="Board"),
    "Tatsu Blaze Node 06": KHDDDLocationData(region="World Map [Sora]", code=2693005, category="Board"),
    "Tatsu Blaze Node 07": KHDDDLocationData(region="World Map [Sora]", code=2693006, category="Board"),
    "Tatsu Blaze Node 08": KHDDDLocationData(region="World Map [Sora]", code=2693007, category="Board"),
    "Tatsu Blaze Node 09": KHDDDLocationData(region="World Map [Sora]", code=2693008, category="Board"),
    "Tatsu Blaze Node 10": KHDDDLocationData(region="World Map [Sora]", code=2693009, category="Board"),
    "Tatsu Blaze Node 11": KHDDDLocationData(region="World Map [Sora]", code=2693010, category="Board"),
    "Tatsu Blaze Node 12": KHDDDLocationData(region="World Map [Sora]", code=2693011, category="Board"),
    "Tatsu Blaze Node 13": KHDDDLocationData(region="World Map [Sora]", code=2693012, category="Board"),
    "Tatsu Blaze Node 14": KHDDDLocationData(region="World Map [Sora]", code=2693013, category="Board"),
    "Tatsu Blaze Node 15": KHDDDLocationData(region="World Map [Sora]", code=2693014, category="Board"),
    "Tatsu Blaze Node 16": KHDDDLocationData(region="World Map [Sora]", code=2693015, category="Board"),

    "Electricorn Node 01": KHDDDLocationData(region="World Map [Sora]", code=2693100, category="Board"),
    "Electricorn Node 02": KHDDDLocationData(region="World Map [Sora]", code=2693101, category="Board"),
    "Electricorn Node 03": KHDDDLocationData(region="World Map [Sora]", code=2693102, category="Board"),
    "Electricorn Node 04": KHDDDLocationData(region="World Map [Sora]", code=2693103, category="Board"),
    "Electricorn Node 05": KHDDDLocationData(region="World Map [Sora]", code=2693104, category="Board"),
    "Electricorn Node 06": KHDDDLocationData(region="World Map [Sora]", code=2693105, category="Board"),
    "Electricorn Node 07": KHDDDLocationData(region="World Map [Sora]", code=2693106, category="Board"),
    "Electricorn Node 08": KHDDDLocationData(region="World Map [Sora]", code=2693107, category="Board"),
    "Electricorn Node 09": KHDDDLocationData(region="World Map [Sora]", code=2693108, category="Board"),
    "Electricorn Node 10": KHDDDLocationData(region="World Map [Sora]", code=2693109, category="Board"),
    "Electricorn Node 11": KHDDDLocationData(region="World Map [Sora]", code=2693110, category="Board"),
    "Electricorn Node 12": KHDDDLocationData(region="World Map [Sora]", code=2693111, category="Board"),
    "Electricorn Node 13": KHDDDLocationData(region="World Map [Sora]", code=2693112, category="Board"),
    "Electricorn Node 14": KHDDDLocationData(region="World Map [Sora]", code=2693113, category="Board"),
    "Electricorn Node 15": KHDDDLocationData(region="World Map [Sora]", code=2693114, category="Board"),
    "Electricorn Node 16": KHDDDLocationData(region="World Map [Sora]", code=2693115, category="Board"),

    "Woeflower Node 01": KHDDDLocationData(region="World Map [Sora]", code=2693200, category="Board"),
    "Woeflower Node 02": KHDDDLocationData(region="World Map [Sora]", code=2693201, category="Board"),
    "Woeflower Node 03": KHDDDLocationData(region="World Map [Sora]", code=2693202, category="Board"),
    "Woeflower Node 04": KHDDDLocationData(region="World Map [Sora]", code=2693203, category="Board"),
    "Woeflower Node 05": KHDDDLocationData(region="World Map [Sora]", code=2693204, category="Board"),
    "Woeflower Node 06": KHDDDLocationData(region="World Map [Sora]", code=2693205, category="Board"),
    "Woeflower Node 07": KHDDDLocationData(region="World Map [Sora]", code=2693206, category="Board"),
    "Woeflower Node 08": KHDDDLocationData(region="World Map [Sora]", code=2693207, category="Board"),
    "Woeflower Node 09": KHDDDLocationData(region="World Map [Sora]", code=2693208, category="Board"),
    "Woeflower Node 10": KHDDDLocationData(region="World Map [Sora]", code=2693209, category="Board"),
    "Woeflower Node 11": KHDDDLocationData(region="World Map [Sora]", code=2693210, category="Board"),
    "Woeflower Node 12": KHDDDLocationData(region="World Map [Sora]", code=2693211, category="Board"),
    "Woeflower Node 13": KHDDDLocationData(region="World Map [Sora]", code=2693212, category="Board"),
    "Woeflower Node 14": KHDDDLocationData(region="World Map [Sora]", code=2693213, category="Board"),
    "Woeflower Node 15": KHDDDLocationData(region="World Map [Sora]", code=2693214, category="Board"),
    "Woeflower Node 16": KHDDDLocationData(region="World Map [Sora]", code=2693215, category="Board"),

    "Jestabocky Node 01": KHDDDLocationData(region="World Map [Sora]", code=2693300, category="Board"),
    "Jestabocky Node 02": KHDDDLocationData(region="World Map [Sora]", code=2693301, category="Board"),
    "Jestabocky Node 03": KHDDDLocationData(region="World Map [Sora]", code=2693302, category="Board"),
    "Jestabocky Node 04": KHDDDLocationData(region="World Map [Sora]", code=2693303, category="Board"),
    "Jestabocky Node 05": KHDDDLocationData(region="World Map [Sora]", code=2693304, category="Board"),
    "Jestabocky Node 06": KHDDDLocationData(region="World Map [Sora]", code=2693305, category="Board"),
    "Jestabocky Node 07": KHDDDLocationData(region="World Map [Sora]", code=2693306, category="Board"),
    "Jestabocky Node 08": KHDDDLocationData(region="World Map [Sora]", code=2693307, category="Board"),
    "Jestabocky Node 09": KHDDDLocationData(region="World Map [Sora]", code=2693308, category="Board"),
    "Jestabocky Node 10": KHDDDLocationData(region="World Map [Sora]", code=2693309, category="Board"),
    "Jestabocky Node 11": KHDDDLocationData(region="World Map [Sora]", code=2693310, category="Board"),
    "Jestabocky Node 12": KHDDDLocationData(region="World Map [Sora]", code=2693311, category="Board"),
    "Jestabocky Node 13": KHDDDLocationData(region="World Map [Sora]", code=2693312, category="Board"),
    "Jestabocky Node 14": KHDDDLocationData(region="World Map [Sora]", code=2693313, category="Board"),
    "Jestabocky Node 15": KHDDDLocationData(region="World Map [Sora]", code=2693314, category="Board"),
    "Jestabocky Node 16": KHDDDLocationData(region="World Map [Sora]", code=2693315, category="Board"),

    "Eaglider Node 01": KHDDDLocationData(region="World Map [Sora]", code=2693400, category="Board"),
    "Eaglider Node 02": KHDDDLocationData(region="World Map [Sora]", code=2693401, category="Board"),
    "Eaglider Node 03": KHDDDLocationData(region="World Map [Sora]", code=2693402, category="Board"),
    "Eaglider Node 04": KHDDDLocationData(region="World Map [Sora]", code=2693403, category="Board"),
    "Eaglider Node 05": KHDDDLocationData(region="World Map [Sora]", code=2693404, category="Board"),
    "Eaglider Node 06": KHDDDLocationData(region="World Map [Sora]", code=2693405, category="Board"),
    "Eaglider Node 07": KHDDDLocationData(region="World Map [Sora]", code=2693406, category="Board"),
    "Eaglider Node 08": KHDDDLocationData(region="World Map [Sora]", code=2693407, category="Board"),
    "Eaglider Node 09": KHDDDLocationData(region="World Map [Sora]", code=2693408, category="Board"),
    "Eaglider Node 10": KHDDDLocationData(region="World Map [Sora]", code=2693409, category="Board"),
    "Eaglider Node 11": KHDDDLocationData(region="World Map [Sora]", code=2693410, category="Board"),
    "Eaglider Node 12": KHDDDLocationData(region="World Map [Sora]", code=2693411, category="Board"),
    "Eaglider Node 13": KHDDDLocationData(region="World Map [Sora]", code=2693412, category="Board"),
    "Eaglider Node 14": KHDDDLocationData(region="World Map [Sora]", code=2693413, category="Board"),
    "Eaglider Node 15": KHDDDLocationData(region="World Map [Sora]", code=2693414, category="Board"),
    "Eaglider Node 16": KHDDDLocationData(region="World Map [Sora]", code=2693415, category="Board"),

    "Me Me Bunny Node 01": KHDDDLocationData(region="World Map [Sora]", code=2693500, category="Board"),
    "Me Me Bunny Node 02": KHDDDLocationData(region="World Map [Sora]", code=2693501, category="Board"),
    "Me Me Bunny Node 03": KHDDDLocationData(region="World Map [Sora]", code=2693502, category="Board"),
    "Me Me Bunny Node 04": KHDDDLocationData(region="World Map [Sora]", code=2693503, category="Board"),
    "Me Me Bunny Node 05": KHDDDLocationData(region="World Map [Sora]", code=2693504, category="Board"),
    "Me Me Bunny Node 06": KHDDDLocationData(region="World Map [Sora]", code=2693505, category="Board"),
    "Me Me Bunny Node 07": KHDDDLocationData(region="World Map [Sora]", code=2693506, category="Board"),
    "Me Me Bunny Node 08": KHDDDLocationData(region="World Map [Sora]", code=2693507, category="Board"),
    "Me Me Bunny Node 09": KHDDDLocationData(region="World Map [Sora]", code=2693508, category="Board"),
    "Me Me Bunny Node 10": KHDDDLocationData(region="World Map [Sora]", code=2693509, category="Board"),
    "Me Me Bunny Node 11": KHDDDLocationData(region="World Map [Sora]", code=2693510, category="Board"),
    "Me Me Bunny Node 12": KHDDDLocationData(region="World Map [Sora]", code=2693511, category="Board"),
    "Me Me Bunny Node 13": KHDDDLocationData(region="World Map [Sora]", code=2693512, category="Board"),
    "Me Me Bunny Node 14": KHDDDLocationData(region="World Map [Sora]", code=2693513, category="Board"),
    "Me Me Bunny Node 15": KHDDDLocationData(region="World Map [Sora]", code=2693514, category="Board"),
    "Me Me Bunny Node 16": KHDDDLocationData(region="World Map [Sora]", code=2693515, category="Board"),

    "Drill Sye Node 01": KHDDDLocationData(region="World Map [Sora]", code=2693600, category="Board"),
    "Drill Sye Node 02": KHDDDLocationData(region="World Map [Sora]", code=2693601, category="Board"),
    "Drill Sye Node 03": KHDDDLocationData(region="World Map [Sora]", code=2693602, category="Board"),
    "Drill Sye Node 04": KHDDDLocationData(region="World Map [Sora]", code=2693603, category="Board"),
    "Drill Sye Node 05": KHDDDLocationData(region="World Map [Sora]", code=2693604, category="Board"),
    "Drill Sye Node 06": KHDDDLocationData(region="World Map [Sora]", code=2693605, category="Board"),
    "Drill Sye Node 07": KHDDDLocationData(region="World Map [Sora]", code=2693606, category="Board"),
    "Drill Sye Node 08": KHDDDLocationData(region="World Map [Sora]", code=2693607, category="Board"),
    "Drill Sye Node 09": KHDDDLocationData(region="World Map [Sora]", code=2693608, category="Board"),
    "Drill Sye Node 10": KHDDDLocationData(region="World Map [Sora]", code=2693609, category="Board"),
    "Drill Sye Node 11": KHDDDLocationData(region="World Map [Sora]", code=2693610, category="Board"),
    "Drill Sye Node 12": KHDDDLocationData(region="World Map [Sora]", code=2693611, category="Board"),
    "Drill Sye Node 13": KHDDDLocationData(region="World Map [Sora]", code=2693612, category="Board"),
    "Drill Sye Node 14": KHDDDLocationData(region="World Map [Sora]", code=2693613, category="Board"),
    "Drill Sye Node 15": KHDDDLocationData(region="World Map [Sora]", code=2693614, category="Board"),
    "Drill Sye Node 16": KHDDDLocationData(region="World Map [Sora]", code=2693615, category="Board"),

    "Tyranto Rex Node 01": KHDDDLocationData(region="World Map [Sora]", code=2693700, category="Board"),
    "Tyranto Rex Node 02": KHDDDLocationData(region="World Map [Sora]", code=2693701, category="Board"),
    "Tyranto Rex Node 03": KHDDDLocationData(region="World Map [Sora]", code=2693702, category="Board"),
    "Tyranto Rex Node 04": KHDDDLocationData(region="World Map [Sora]", code=2693703, category="Board"),
    "Tyranto Rex Node 05": KHDDDLocationData(region="World Map [Sora]", code=2693704, category="Board"),
    "Tyranto Rex Node 06": KHDDDLocationData(region="World Map [Sora]", code=2693705, category="Board"),
    "Tyranto Rex Node 07": KHDDDLocationData(region="World Map [Sora]", code=2693706, category="Board"),
    "Tyranto Rex Node 08": KHDDDLocationData(region="World Map [Sora]", code=2693707, category="Board"),
    "Tyranto Rex Node 09": KHDDDLocationData(region="World Map [Sora]", code=2693708, category="Board"),
    "Tyranto Rex Node 10": KHDDDLocationData(region="World Map [Sora]", code=2693709, category="Board"),
    "Tyranto Rex Node 11": KHDDDLocationData(region="World Map [Sora]", code=2693710, category="Board"),
    "Tyranto Rex Node 12": KHDDDLocationData(region="World Map [Sora]", code=2693711, category="Board"),
    "Tyranto Rex Node 13": KHDDDLocationData(region="World Map [Sora]", code=2693712, category="Board"),
    "Tyranto Rex Node 14": KHDDDLocationData(region="World Map [Sora]", code=2693713, category="Board"),
    "Tyranto Rex Node 15": KHDDDLocationData(region="World Map [Sora]", code=2693714, category="Board"),
    "Tyranto Rex Node 16": KHDDDLocationData(region="World Map [Sora]", code=2693715, category="Board"),

    "Majik Lapin Node 01": KHDDDLocationData(region="World Map [Sora]", code=2693800, category="Board"),
    "Majik Lapin Node 02": KHDDDLocationData(region="World Map [Sora]", code=2693801, category="Board"),
    "Majik Lapin Node 03": KHDDDLocationData(region="World Map [Sora]", code=2693802, category="Board"),
    "Majik Lapin Node 04": KHDDDLocationData(region="World Map [Sora]", code=2693803, category="Board"),
    "Majik Lapin Node 05": KHDDDLocationData(region="World Map [Sora]", code=2693804, category="Board"),
    "Majik Lapin Node 06": KHDDDLocationData(region="World Map [Sora]", code=2693805, category="Board"),
    "Majik Lapin Node 07": KHDDDLocationData(region="World Map [Sora]", code=2693806, category="Board"),
    "Majik Lapin Node 08": KHDDDLocationData(region="World Map [Sora]", code=2693807, category="Board"),
    "Majik Lapin Node 09": KHDDDLocationData(region="World Map [Sora]", code=2693808, category="Board"),
    "Majik Lapin Node 10": KHDDDLocationData(region="World Map [Sora]", code=2693809, category="Board"),
    "Majik Lapin Node 11": KHDDDLocationData(region="World Map [Sora]", code=2693810, category="Board"),
    "Majik Lapin Node 12": KHDDDLocationData(region="World Map [Sora]", code=2693811, category="Board"),
    "Majik Lapin Node 13": KHDDDLocationData(region="World Map [Sora]", code=2693812, category="Board"),
    "Majik Lapin Node 14": KHDDDLocationData(region="World Map [Sora]", code=2693813, category="Board"),
    "Majik Lapin Node 15": KHDDDLocationData(region="World Map [Sora]", code=2693814, category="Board"),
    "Majik Lapin Node 16": KHDDDLocationData(region="World Map [Sora]", code=2693815, category="Board"),

    "Cera Terror Node 01": KHDDDLocationData(region="World Map [Sora]", code=2693900, category="Board"),
    "Cera Terror Node 02": KHDDDLocationData(region="World Map [Sora]", code=2693901, category="Board"),
    "Cera Terror Node 03": KHDDDLocationData(region="World Map [Sora]", code=2693902, category="Board"),
    "Cera Terror Node 04": KHDDDLocationData(region="World Map [Sora]", code=2693903, category="Board"),
    "Cera Terror Node 05": KHDDDLocationData(region="World Map [Sora]", code=2693904, category="Board"),
    "Cera Terror Node 06": KHDDDLocationData(region="World Map [Sora]", code=2693905, category="Board"),
    "Cera Terror Node 07": KHDDDLocationData(region="World Map [Sora]", code=2693906, category="Board"),
    "Cera Terror Node 08": KHDDDLocationData(region="World Map [Sora]", code=2693907, category="Board"),
    "Cera Terror Node 09": KHDDDLocationData(region="World Map [Sora]", code=2693908, category="Board"),
    "Cera Terror Node 10": KHDDDLocationData(region="World Map [Sora]", code=2693909, category="Board"),
    "Cera Terror Node 11": KHDDDLocationData(region="World Map [Sora]", code=2693910, category="Board"),
    "Cera Terror Node 12": KHDDDLocationData(region="World Map [Sora]", code=2693911, category="Board"),
    "Cera Terror Node 13": KHDDDLocationData(region="World Map [Sora]", code=2693912, category="Board"),
    "Cera Terror Node 14": KHDDDLocationData(region="World Map [Sora]", code=2693913, category="Board"),
    "Cera Terror Node 15": KHDDDLocationData(region="World Map [Sora]", code=2693914, category="Board"),
    "Cera Terror Node 16": KHDDDLocationData(region="World Map [Sora]", code=2693915, category="Board"),

    "Skelterwild Node 01": KHDDDLocationData(region="World Map [Sora]", code=2694000, category="Board"),
    "Skelterwild Node 02": KHDDDLocationData(region="World Map [Sora]", code=2694001, category="Board"),
    "Skelterwild Node 03": KHDDDLocationData(region="World Map [Sora]", code=2694002, category="Board"),
    "Skelterwild Node 04": KHDDDLocationData(region="World Map [Sora]", code=2694003, category="Board"),
    "Skelterwild Node 05": KHDDDLocationData(region="World Map [Sora]", code=2694004, category="Board"),
    "Skelterwild Node 06": KHDDDLocationData(region="World Map [Sora]", code=2694005, category="Board"),
    "Skelterwild Node 07": KHDDDLocationData(region="World Map [Sora]", code=2694006, category="Board"),
    "Skelterwild Node 08": KHDDDLocationData(region="World Map [Sora]", code=2694007, category="Board"),
    "Skelterwild Node 09": KHDDDLocationData(region="World Map [Sora]", code=2694008, category="Board"),
    "Skelterwild Node 10": KHDDDLocationData(region="World Map [Sora]", code=2694009, category="Board"),
    "Skelterwild Node 11": KHDDDLocationData(region="World Map [Sora]", code=2694010, category="Board"),
    "Skelterwild Node 12": KHDDDLocationData(region="World Map [Sora]", code=2694011, category="Board"),
    "Skelterwild Node 13": KHDDDLocationData(region="World Map [Sora]", code=2694012, category="Board"),
    "Skelterwild Node 14": KHDDDLocationData(region="World Map [Sora]", code=2694013, category="Board"),
    "Skelterwild Node 15": KHDDDLocationData(region="World Map [Sora]", code=2694014, category="Board"),
    "Skelterwild Node 16": KHDDDLocationData(region="World Map [Sora]", code=2694015, category="Board"),

    "Ducky Goose Node 01": KHDDDLocationData(region="World Map [Sora]", code=2694100, category="Board"),
    "Ducky Goose Node 02": KHDDDLocationData(region="World Map [Sora]", code=2694101, category="Board"),
    "Ducky Goose Node 03": KHDDDLocationData(region="World Map [Sora]", code=2694102, category="Board"),
    "Ducky Goose Node 04": KHDDDLocationData(region="World Map [Sora]", code=2694103, category="Board"),
    "Ducky Goose Node 05": KHDDDLocationData(region="World Map [Sora]", code=2694104, category="Board"),
    "Ducky Goose Node 06": KHDDDLocationData(region="World Map [Sora]", code=2694105, category="Board"),
    "Ducky Goose Node 07": KHDDDLocationData(region="World Map [Sora]", code=2694106, category="Board"),
    "Ducky Goose Node 08": KHDDDLocationData(region="World Map [Sora]", code=2694107, category="Board"),
    "Ducky Goose Node 09": KHDDDLocationData(region="World Map [Sora]", code=2694108, category="Board"),
    "Ducky Goose Node 10": KHDDDLocationData(region="World Map [Sora]", code=2694109, category="Board"),
    "Ducky Goose Node 11": KHDDDLocationData(region="World Map [Sora]", code=2694110, category="Board"),
    "Ducky Goose Node 12": KHDDDLocationData(region="World Map [Sora]", code=2694111, category="Board"),
    "Ducky Goose Node 13": KHDDDLocationData(region="World Map [Sora]", code=2694112, category="Board"),
    "Ducky Goose Node 14": KHDDDLocationData(region="World Map [Sora]", code=2694113, category="Board"),
    "Ducky Goose Node 15": KHDDDLocationData(region="World Map [Sora]", code=2694114, category="Board"),
    "Ducky Goose Node 16": KHDDDLocationData(region="World Map [Sora]", code=2694115, category="Board"),

    "Aura Lion Node 01": KHDDDLocationData(region="World Map [Sora]", code=2694200, category="Board"),
    "Aura Lion Node 02": KHDDDLocationData(region="World Map [Sora]", code=2694201, category="Board"),
    "Aura Lion Node 03": KHDDDLocationData(region="World Map [Sora]", code=2694202, category="Board"),
    "Aura Lion Node 04": KHDDDLocationData(region="World Map [Sora]", code=2694203, category="Board"),
    "Aura Lion Node 05": KHDDDLocationData(region="World Map [Sora]", code=2694204, category="Board"),
    "Aura Lion Node 06": KHDDDLocationData(region="World Map [Sora]", code=2694205, category="Board"),
    "Aura Lion Node 07": KHDDDLocationData(region="World Map [Sora]", code=2694206, category="Board"),
    "Aura Lion Node 08": KHDDDLocationData(region="World Map [Sora]", code=2694207, category="Board"),
    "Aura Lion Node 09": KHDDDLocationData(region="World Map [Sora]", code=2694208, category="Board"),
    "Aura Lion Node 10": KHDDDLocationData(region="World Map [Sora]", code=2694209, category="Board"),
    "Aura Lion Node 11": KHDDDLocationData(region="World Map [Sora]", code=2694210, category="Board"),
    "Aura Lion Node 12": KHDDDLocationData(region="World Map [Sora]", code=2694211, category="Board"),
    "Aura Lion Node 13": KHDDDLocationData(region="World Map [Sora]", code=2694212, category="Board"),
    "Aura Lion Node 14": KHDDDLocationData(region="World Map [Sora]", code=2694213, category="Board"),
    "Aura Lion Node 15": KHDDDLocationData(region="World Map [Sora]", code=2694214, category="Board"),
    "Aura Lion Node 16": KHDDDLocationData(region="World Map [Sora]", code=2694215, category="Board"),

    "Ryu Dragon Node 01": KHDDDLocationData(region="World Map [Sora]", code=2694300, category="Board"),
    "Ryu Dragon Node 02": KHDDDLocationData(region="World Map [Sora]", code=2694301, category="Board"),
    "Ryu Dragon Node 03": KHDDDLocationData(region="World Map [Sora]", code=2694302, category="Board"),
    "Ryu Dragon Node 04": KHDDDLocationData(region="World Map [Sora]", code=2694303, category="Board"),
    "Ryu Dragon Node 05": KHDDDLocationData(region="World Map [Sora]", code=2694304, category="Board"),
    "Ryu Dragon Node 06": KHDDDLocationData(region="World Map [Sora]", code=2694305, category="Board"),
    "Ryu Dragon Node 07": KHDDDLocationData(region="World Map [Sora]", code=2694306, category="Board"),
    "Ryu Dragon Node 08": KHDDDLocationData(region="World Map [Sora]", code=2694307, category="Board"),
    "Ryu Dragon Node 09": KHDDDLocationData(region="World Map [Sora]", code=2694308, category="Board"),
    "Ryu Dragon Node 10": KHDDDLocationData(region="World Map [Sora]", code=2694309, category="Board"),
    "Ryu Dragon Node 11": KHDDDLocationData(region="World Map [Sora]", code=2694310, category="Board"),
    "Ryu Dragon Node 12": KHDDDLocationData(region="World Map [Sora]", code=2694311, category="Board"),
    "Ryu Dragon Node 13": KHDDDLocationData(region="World Map [Sora]", code=2694312, category="Board"),
    "Ryu Dragon Node 14": KHDDDLocationData(region="World Map [Sora]", code=2694313, category="Board"),
    "Ryu Dragon Node 15": KHDDDLocationData(region="World Map [Sora]", code=2694314, category="Board"),
    "Ryu Dragon Node 16": KHDDDLocationData(region="World Map [Sora]", code=2694315, category="Board"),

    "Drak Quack Node 01": KHDDDLocationData(region="World Map [Sora]", code=2694400, category="Board"),
    "Drak Quack Node 02": KHDDDLocationData(region="World Map [Sora]", code=2694401, category="Board"),
    "Drak Quack Node 03": KHDDDLocationData(region="World Map [Sora]", code=2694402, category="Board"),
    "Drak Quack Node 04": KHDDDLocationData(region="World Map [Sora]", code=2694403, category="Board"),
    "Drak Quack Node 05": KHDDDLocationData(region="World Map [Sora]", code=2694404, category="Board"),
    "Drak Quack Node 06": KHDDDLocationData(region="World Map [Sora]", code=2694405, category="Board"),
    "Drak Quack Node 07": KHDDDLocationData(region="World Map [Sora]", code=2694406, category="Board"),
    "Drak Quack Node 08": KHDDDLocationData(region="World Map [Sora]", code=2694407, category="Board"),
    "Drak Quack Node 09": KHDDDLocationData(region="World Map [Sora]", code=2694408, category="Board"),
    "Drak Quack Node 10": KHDDDLocationData(region="World Map [Sora]", code=2694409, category="Board"),
    "Drak Quack Node 11": KHDDDLocationData(region="World Map [Sora]", code=2694410, category="Board"),
    "Drak Quack Node 12": KHDDDLocationData(region="World Map [Sora]", code=2694411, category="Board"),
    "Drak Quack Node 13": KHDDDLocationData(region="World Map [Sora]", code=2694412, category="Board"),
    "Drak Quack Node 14": KHDDDLocationData(region="World Map [Sora]", code=2694413, category="Board"),
    "Drak Quack Node 15": KHDDDLocationData(region="World Map [Sora]", code=2694414, category="Board"),
    "Drak Quack Node 16": KHDDDLocationData(region="World Map [Sora]", code=2694415, category="Board"),

    "Keeba Tiger Node 01": KHDDDLocationData(region="World Map [Sora]", code=2694500, category="Board"),
    "Keeba Tiger Node 02": KHDDDLocationData(region="World Map [Sora]", code=2694501, category="Board"),
    "Keeba Tiger Node 03": KHDDDLocationData(region="World Map [Sora]", code=2694502, category="Board"),
    "Keeba Tiger Node 04": KHDDDLocationData(region="World Map [Sora]", code=2694503, category="Board"),
    "Keeba Tiger Node 05": KHDDDLocationData(region="World Map [Sora]", code=2694504, category="Board"),
    "Keeba Tiger Node 06": KHDDDLocationData(region="World Map [Sora]", code=2694505, category="Board"),
    "Keeba Tiger Node 07": KHDDDLocationData(region="World Map [Sora]", code=2694506, category="Board"),
    "Keeba Tiger Node 08": KHDDDLocationData(region="World Map [Sora]", code=2694507, category="Board"),
    "Keeba Tiger Node 09": KHDDDLocationData(region="World Map [Sora]", code=2694508, category="Board"),
    "Keeba Tiger Node 10": KHDDDLocationData(region="World Map [Sora]", code=2694509, category="Board"),
    "Keeba Tiger Node 11": KHDDDLocationData(region="World Map [Sora]", code=2694510, category="Board"),
    "Keeba Tiger Node 12": KHDDDLocationData(region="World Map [Sora]", code=2694511, category="Board"),
    "Keeba Tiger Node 13": KHDDDLocationData(region="World Map [Sora]", code=2694512, category="Board"),
    "Keeba Tiger Node 14": KHDDDLocationData(region="World Map [Sora]", code=2694513, category="Board"),
    "Keeba Tiger Node 15": KHDDDLocationData(region="World Map [Sora]", code=2694514, category="Board"),
    "Keeba Tiger Node 16": KHDDDLocationData(region="World Map [Sora]", code=2694515, category="Board"),

    "Meowjesty Node 01": KHDDDLocationData(region="World Map [Sora]", code=2694600, category="Board"),
    "Meowjesty Node 02": KHDDDLocationData(region="World Map [Sora]", code=2694601, category="Board"),
    "Meowjesty Node 03": KHDDDLocationData(region="World Map [Sora]", code=2694602, category="Board"),
    "Meowjesty Node 04": KHDDDLocationData(region="World Map [Sora]", code=2694603, category="Board"),
    "Meowjesty Node 05": KHDDDLocationData(region="World Map [Sora]", code=2694604, category="Board"),
    "Meowjesty Node 06": KHDDDLocationData(region="World Map [Sora]", code=2694605, category="Board"),
    "Meowjesty Node 07": KHDDDLocationData(region="World Map [Sora]", code=2694606, category="Board"),
    "Meowjesty Node 08": KHDDDLocationData(region="World Map [Sora]", code=2694607, category="Board"),
    "Meowjesty Node 09": KHDDDLocationData(region="World Map [Sora]", code=2694608, category="Board"),
    "Meowjesty Node 10": KHDDDLocationData(region="World Map [Sora]", code=2694609, category="Board"),
    "Meowjesty Node 11": KHDDDLocationData(region="World Map [Sora]", code=2694610, category="Board"),
    "Meowjesty Node 12": KHDDDLocationData(region="World Map [Sora]", code=2694611, category="Board"),
    "Meowjesty Node 13": KHDDDLocationData(region="World Map [Sora]", code=2694612, category="Board"),
    "Meowjesty Node 14": KHDDDLocationData(region="World Map [Sora]", code=2694613, category="Board"),
    "Meowjesty Node 15": KHDDDLocationData(region="World Map [Sora]", code=2694614, category="Board"),
    "Meowjesty Node 16": KHDDDLocationData(region="World Map [Sora]", code=2694615, category="Board"),

    "Sudo Neku Node 01": KHDDDLocationData(region="World Map [Sora]", code=2694700, category="Board"),
    "Sudo Neku Node 02": KHDDDLocationData(region="World Map [Sora]", code=2694701, category="Board"),
    "Sudo Neku Node 03": KHDDDLocationData(region="World Map [Sora]", code=2694702, category="Board"),
    "Sudo Neku Node 04": KHDDDLocationData(region="World Map [Sora]", code=2694703, category="Board"),
    "Sudo Neku Node 05": KHDDDLocationData(region="World Map [Sora]", code=2694704, category="Board"),
    "Sudo Neku Node 06": KHDDDLocationData(region="World Map [Sora]", code=2694705, category="Board"),
    "Sudo Neku Node 07": KHDDDLocationData(region="World Map [Sora]", code=2694706, category="Board"),
    "Sudo Neku Node 08": KHDDDLocationData(region="World Map [Sora]", code=2694707, category="Board"),
    "Sudo Neku Node 09": KHDDDLocationData(region="World Map [Sora]", code=2694708, category="Board"),
    "Sudo Neku Node 10": KHDDDLocationData(region="World Map [Sora]", code=2694709, category="Board"),
    "Sudo Neku Node 11": KHDDDLocationData(region="World Map [Sora]", code=2694710, category="Board"),
    "Sudo Neku Node 12": KHDDDLocationData(region="World Map [Sora]", code=2694711, category="Board"),
    "Sudo Neku Node 13": KHDDDLocationData(region="World Map [Sora]", code=2694712, category="Board"),
    "Sudo Neku Node 14": KHDDDLocationData(region="World Map [Sora]", code=2694713, category="Board"),
    "Sudo Neku Node 15": KHDDDLocationData(region="World Map [Sora]", code=2694714, category="Board"),
    "Sudo Neku Node 16": KHDDDLocationData(region="World Map [Sora]", code=2694715, category="Board"),

    "Frootz Cat Node 01": KHDDDLocationData(region="World Map [Sora]", code=2694800, category="Board"),
    "Frootz Cat Node 02": KHDDDLocationData(region="World Map [Sora]", code=2694801, category="Board"),
    "Frootz Cat Node 03": KHDDDLocationData(region="World Map [Sora]", code=2694802, category="Board"),
    "Frootz Cat Node 04": KHDDDLocationData(region="World Map [Sora]", code=2694803, category="Board"),
    "Frootz Cat Node 05": KHDDDLocationData(region="World Map [Sora]", code=2694804, category="Board"),
    "Frootz Cat Node 06": KHDDDLocationData(region="World Map [Sora]", code=2694805, category="Board"),
    "Frootz Cat Node 07": KHDDDLocationData(region="World Map [Sora]", code=2694806, category="Board"),
    "Frootz Cat Node 08": KHDDDLocationData(region="World Map [Sora]", code=2694807, category="Board"),
    "Frootz Cat Node 09": KHDDDLocationData(region="World Map [Sora]", code=2694808, category="Board"),
    "Frootz Cat Node 10": KHDDDLocationData(region="World Map [Sora]", code=2694809, category="Board"),
    "Frootz Cat Node 11": KHDDDLocationData(region="World Map [Sora]", code=2694810, category="Board"),
    "Frootz Cat Node 12": KHDDDLocationData(region="World Map [Sora]", code=2694811, category="Board"),
    "Frootz Cat Node 13": KHDDDLocationData(region="World Map [Sora]", code=2694812, category="Board"),
    "Frootz Cat Node 14": KHDDDLocationData(region="World Map [Sora]", code=2694813, category="Board"),
    "Frootz Cat Node 15": KHDDDLocationData(region="World Map [Sora]", code=2694814, category="Board"),
    "Frootz Cat Node 16": KHDDDLocationData(region="World Map [Sora]", code=2694815, category="Board"),

    "Ursa Circus Node 01": KHDDDLocationData(region="World Map [Sora]", code=2694900, category="Board"),
    "Ursa Circus Node 02": KHDDDLocationData(region="World Map [Sora]", code=2694901, category="Board"),
    "Ursa Circus Node 03": KHDDDLocationData(region="World Map [Sora]", code=2694902, category="Board"),
    "Ursa Circus Node 04": KHDDDLocationData(region="World Map [Sora]", code=2694903, category="Board"),
    "Ursa Circus Node 05": KHDDDLocationData(region="World Map [Sora]", code=2694904, category="Board"),
    "Ursa Circus Node 06": KHDDDLocationData(region="World Map [Sora]", code=2694905, category="Board"),
    "Ursa Circus Node 07": KHDDDLocationData(region="World Map [Sora]", code=2694906, category="Board"),
    "Ursa Circus Node 08": KHDDDLocationData(region="World Map [Sora]", code=2694907, category="Board"),
    "Ursa Circus Node 09": KHDDDLocationData(region="World Map [Sora]", code=2694908, category="Board"),
    "Ursa Circus Node 10": KHDDDLocationData(region="World Map [Sora]", code=2694909, category="Board"),
    "Ursa Circus Node 11": KHDDDLocationData(region="World Map [Sora]", code=2694910, category="Board"),
    "Ursa Circus Node 12": KHDDDLocationData(region="World Map [Sora]", code=2694911, category="Board"),
    "Ursa Circus Node 13": KHDDDLocationData(region="World Map [Sora]", code=2694912, category="Board"),
    "Ursa Circus Node 14": KHDDDLocationData(region="World Map [Sora]", code=2694913, category="Board"),
    "Ursa Circus Node 15": KHDDDLocationData(region="World Map [Sora]", code=2694914, category="Board"),
    "Ursa Circus Node 16": KHDDDLocationData(region="World Map [Sora]", code=2694915, category="Board"),

    "Kab Kannon Node 01": KHDDDLocationData(region="World Map [Sora]", code=2695000, category="Board"),
    "Kab Kannon Node 02": KHDDDLocationData(region="World Map [Sora]", code=2695001, category="Board"),
    "Kab Kannon Node 03": KHDDDLocationData(region="World Map [Sora]", code=2695002, category="Board"),
    "Kab Kannon Node 04": KHDDDLocationData(region="World Map [Sora]", code=2695003, category="Board"),
    "Kab Kannon Node 05": KHDDDLocationData(region="World Map [Sora]", code=2695004, category="Board"),
    "Kab Kannon Node 06": KHDDDLocationData(region="World Map [Sora]", code=2695005, category="Board"),
    "Kab Kannon Node 07": KHDDDLocationData(region="World Map [Sora]", code=2695006, category="Board"),
    "Kab Kannon Node 08": KHDDDLocationData(region="World Map [Sora]", code=2695007, category="Board"),
    "Kab Kannon Node 09": KHDDDLocationData(region="World Map [Sora]", code=2695008, category="Board"),
    "Kab Kannon Node 10": KHDDDLocationData(region="World Map [Sora]", code=2695009, category="Board"),
    "Kab Kannon Node 11": KHDDDLocationData(region="World Map [Sora]", code=2695010, category="Board"),
    "Kab Kannon Node 12": KHDDDLocationData(region="World Map [Sora]", code=2695011, category="Board"),
    "Kab Kannon Node 13": KHDDDLocationData(region="World Map [Sora]", code=2695012, category="Board"),
    "Kab Kannon Node 14": KHDDDLocationData(region="World Map [Sora]", code=2695013, category="Board"),
    "Kab Kannon Node 15": KHDDDLocationData(region="World Map [Sora]", code=2695014, category="Board"),
    "Kab Kannon Node 16": KHDDDLocationData(region="World Map [Sora]", code=2695015, category="Board"),

    "R & R Seal Node 01": KHDDDLocationData(region="World Map [Sora]", code=2695100, category="Board"),
    "R & R Seal Node 02": KHDDDLocationData(region="World Map [Sora]", code=2695101, category="Board"),
    "R & R Seal Node 03": KHDDDLocationData(region="World Map [Sora]", code=2695102, category="Board"),
    "R & R Seal Node 04": KHDDDLocationData(region="World Map [Sora]", code=2695103, category="Board"),
    "R & R Seal Node 05": KHDDDLocationData(region="World Map [Sora]", code=2695104, category="Board"),
    "R & R Seal Node 06": KHDDDLocationData(region="World Map [Sora]", code=2695105, category="Board"),
    "R & R Seal Node 07": KHDDDLocationData(region="World Map [Sora]", code=2695106, category="Board"),
    "R & R Seal Node 08": KHDDDLocationData(region="World Map [Sora]", code=2695107, category="Board"),
    "R & R Seal Node 09": KHDDDLocationData(region="World Map [Sora]", code=2695108, category="Board"),
    "R & R Seal Node 10": KHDDDLocationData(region="World Map [Sora]", code=2695109, category="Board"),
    "R & R Seal Node 11": KHDDDLocationData(region="World Map [Sora]", code=2695110, category="Board"),
    "R & R Seal Node 12": KHDDDLocationData(region="World Map [Sora]", code=2695111, category="Board"),
    "R & R Seal Node 13": KHDDDLocationData(region="World Map [Sora]", code=2695112, category="Board"),
    "R & R Seal Node 14": KHDDDLocationData(region="World Map [Sora]", code=2695113, category="Board"),
    "R & R Seal Node 15": KHDDDLocationData(region="World Map [Sora]", code=2695114, category="Board"),
    "R & R Seal Node 16": KHDDDLocationData(region="World Map [Sora]", code=2695115, category="Board"),

    "Catanuki Node 01": KHDDDLocationData(region="World Map [Sora]", code=2695200, category="Board"),
    "Catanuki Node 02": KHDDDLocationData(region="World Map [Sora]", code=2695201, category="Board"),
    "Catanuki Node 03": KHDDDLocationData(region="World Map [Sora]", code=2695202, category="Board"),
    "Catanuki Node 04": KHDDDLocationData(region="World Map [Sora]", code=2695203, category="Board"),
    "Catanuki Node 05": KHDDDLocationData(region="World Map [Sora]", code=2695204, category="Board"),
    "Catanuki Node 06": KHDDDLocationData(region="World Map [Sora]", code=2695205, category="Board"),
    "Catanuki Node 07": KHDDDLocationData(region="World Map [Sora]", code=2695206, category="Board"),
    "Catanuki Node 08": KHDDDLocationData(region="World Map [Sora]", code=2695207, category="Board"),
    "Catanuki Node 09": KHDDDLocationData(region="World Map [Sora]", code=2695208, category="Board"),
    "Catanuki Node 10": KHDDDLocationData(region="World Map [Sora]", code=2695209, category="Board"),
    "Catanuki Node 11": KHDDDLocationData(region="World Map [Sora]", code=2695210, category="Board"),
    "Catanuki Node 12": KHDDDLocationData(region="World Map [Sora]", code=2695211, category="Board"),
    "Catanuki Node 13": KHDDDLocationData(region="World Map [Sora]", code=2695212, category="Board"),
    "Catanuki Node 14": KHDDDLocationData(region="World Map [Sora]", code=2695213, category="Board"),
    "Catanuki Node 15": KHDDDLocationData(region="World Map [Sora]", code=2695214, category="Board"),
    "Catanuki Node 16": KHDDDLocationData(region="World Map [Sora]", code=2695215, category="Board"),

    "Beatalike Node 01": KHDDDLocationData(region="World Map [Sora]", code=2695300, category="Board"),
    "Beatalike Node 02": KHDDDLocationData(region="World Map [Sora]", code=2695301, category="Board"),
    "Beatalike Node 03": KHDDDLocationData(region="World Map [Sora]", code=2695302, category="Board"),
    "Beatalike Node 04": KHDDDLocationData(region="World Map [Sora]", code=2695303, category="Board"),
    "Beatalike Node 05": KHDDDLocationData(region="World Map [Sora]", code=2695304, category="Board"),
    "Beatalike Node 06": KHDDDLocationData(region="World Map [Sora]", code=2695305, category="Board"),
    "Beatalike Node 07": KHDDDLocationData(region="World Map [Sora]", code=2695306, category="Board"),
    "Beatalike Node 08": KHDDDLocationData(region="World Map [Sora]", code=2695307, category="Board"),
    "Beatalike Node 09": KHDDDLocationData(region="World Map [Sora]", code=2695308, category="Board"),
    "Beatalike Node 10": KHDDDLocationData(region="World Map [Sora]", code=2695309, category="Board"),
    "Beatalike Node 11": KHDDDLocationData(region="World Map [Sora]", code=2695310, category="Board"),
    "Beatalike Node 12": KHDDDLocationData(region="World Map [Sora]", code=2695311, category="Board"),
    "Beatalike Node 13": KHDDDLocationData(region="World Map [Sora]", code=2695312, category="Board"),
    "Beatalike Node 14": KHDDDLocationData(region="World Map [Sora]", code=2695313, category="Board"),
    "Beatalike Node 15": KHDDDLocationData(region="World Map [Sora]", code=2695314, category="Board"),
    "Beatalike Node 16": KHDDDLocationData(region="World Map [Sora]", code=2695315, category="Board"),

    "Tubguin Ace Node 01": KHDDDLocationData(region="World Map [Sora]", code=2695400, category="Board"),
    "Tubguin Ace Node 02": KHDDDLocationData(region="World Map [Sora]", code=2695401, category="Board"),
    "Tubguin Ace Node 03": KHDDDLocationData(region="World Map [Sora]", code=2695402, category="Board"),
    "Tubguin Ace Node 04": KHDDDLocationData(region="World Map [Sora]", code=2695403, category="Board"),
    "Tubguin Ace Node 05": KHDDDLocationData(region="World Map [Sora]", code=2695404, category="Board"),
    "Tubguin Ace Node 06": KHDDDLocationData(region="World Map [Sora]", code=2695405, category="Board"),
    "Tubguin Ace Node 07": KHDDDLocationData(region="World Map [Sora]", code=2695406, category="Board"),
    "Tubguin Ace Node 08": KHDDDLocationData(region="World Map [Sora]", code=2695407, category="Board"),
    "Tubguin Ace Node 09": KHDDDLocationData(region="World Map [Sora]", code=2695408, category="Board"),
    "Tubguin Ace Node 10": KHDDDLocationData(region="World Map [Sora]", code=2695409, category="Board"),
    "Tubguin Ace Node 11": KHDDDLocationData(region="World Map [Sora]", code=2695410, category="Board"),
    "Tubguin Ace Node 12": KHDDDLocationData(region="World Map [Sora]", code=2695411, category="Board"),
    "Tubguin Ace Node 13": KHDDDLocationData(region="World Map [Sora]", code=2695412, category="Board"),
    "Tubguin Ace Node 14": KHDDDLocationData(region="World Map [Sora]", code=2695413, category="Board"),
    "Tubguin Ace Node 15": KHDDDLocationData(region="World Map [Sora]", code=2695414, category="Board"),
    "Tubguin Ace Node 16": KHDDDLocationData(region="World Map [Sora]", code=2695415, category="Board"),

    #Levels
    "Sora Level 02": KHDDDLocationData(region="Levels",code=2660002,category="Slot"),
    "Sora Level 03": KHDDDLocationData(region="Levels",code=2660003,category="Slot"),
    "Sora Level 04": KHDDDLocationData(region="Levels",code=2660004,category="Slot"),
    "Sora Level 05": KHDDDLocationData(region="Levels",code=2660005,category="Slot"),
    "Sora Level 06": KHDDDLocationData(region="Levels",code=2660006,category="Slot"),
    "Sora Level 07": KHDDDLocationData(region="Levels", code=2660007,category="Slot"),
    "Sora Level 08": KHDDDLocationData(region="Levels", code=2660008,category="Slot"),
    "Sora Level 09": KHDDDLocationData(region="Levels", code=2660009,category="Slot"),
    "Sora Level 10": KHDDDLocationData(region="Levels", code=2660010,category="Slot"),
    "Sora Level 11": KHDDDLocationData(region="Levels", code=2660011,category="Slot"),
    "Sora Level 12": KHDDDLocationData(region="Levels", code=2660012,category="Slot"),
    "Sora Level 13": KHDDDLocationData(region="Levels", code=2660013,category="Slot"),
    "Sora Level 14": KHDDDLocationData(region="Levels", code=2660014,category="Slot"),
    "Sora Level 15": KHDDDLocationData(region="Levels", code=2660015,category="Slot"),
    "Sora Level 16": KHDDDLocationData(region="Levels", code=2660016,category="Slot"),
    "Sora Level 17": KHDDDLocationData(region="Levels", code=2660017,category="Slot"),
    "Sora Level 18": KHDDDLocationData(region="Levels", code=2660018,category="Slot"),
    "Sora Level 19": KHDDDLocationData(region="Levels", code=2660019,category="Slot"),
    "Sora Level 20": KHDDDLocationData(region="Levels", code=2660020,category="Slot"),
    "Sora Level 21": KHDDDLocationData(region="Levels", code=2660021,category="Slot"),
    "Sora Level 22": KHDDDLocationData(region="Levels", code=2660022,category="Slot"),
    "Sora Level 23": KHDDDLocationData(region="Levels", code=2660023,category="Slot"),
    "Sora Level 24": KHDDDLocationData(region="Levels", code=2660024,category="Slot"),
    "Sora Level 25": KHDDDLocationData(region="Levels", code=2660025,category="Slot"),
    "Sora Level 26": KHDDDLocationData(region="Levels", code=2660026,category="Slot"),
    "Sora Level 27": KHDDDLocationData(region="Levels", code=2660027,category="Slot"),
    "Sora Level 28": KHDDDLocationData(region="Levels", code=2660028,category="Slot"),
    "Sora Level 29": KHDDDLocationData(region="Levels", code=2660029,category="Slot"),
    "Sora Level 30": KHDDDLocationData(region="Levels", code=2660030,category="Slot"),
    "Sora Level 31": KHDDDLocationData(region="Levels", code=2660031,category="Slot"),
    "Sora Level 32": KHDDDLocationData(region="Levels", code=2660032,category="Slot"),
    "Sora Level 33": KHDDDLocationData(region="Levels", code=2660033,category="Slot"),
    "Sora Level 34": KHDDDLocationData(region="Levels", code=2660034,category="Slot"),
    "Sora Level 35": KHDDDLocationData(region="Levels", code=2660035,category="Slot"),
    "Sora Level 36": KHDDDLocationData(region="Levels", code=2660036,category="Slot"),
    "Sora Level 37": KHDDDLocationData(region="Levels", code=2660037,category="Slot"),
    "Sora Level 38": KHDDDLocationData(region="Levels", code=2660038,category="Slot"),
    "Sora Level 39": KHDDDLocationData(region="Levels", code=2660039,category="Slot"),
    "Sora Level 40": KHDDDLocationData(region="Levels", code=2660040,category="Slot"),
    "Sora Level 41": KHDDDLocationData(region="Levels", code=2660041,category="Slot"),
    "Sora Level 42": KHDDDLocationData(region="Levels", code=2660042,category="Slot"),
    "Sora Level 43": KHDDDLocationData(region="Levels", code=2660043,category="Slot"),
    "Sora Level 44": KHDDDLocationData(region="Levels", code=2660044,category="Slot"),
    "Sora Level 45": KHDDDLocationData(region="Levels", code=2660045,category="Slot"),
    "Sora Level 46": KHDDDLocationData(region="Levels", code=2660046,category="Slot"),
    "Sora Level 47": KHDDDLocationData(region="Levels", code=2660047,category="Slot"),
    "Sora Level 48": KHDDDLocationData(region="Levels", code=2660048,category="Slot"),
    "Sora Level 49": KHDDDLocationData(region="Levels", code=2660049,category="Slot"),
    "Sora Level 50": KHDDDLocationData(region="Levels", code=2660050,category="Slot"),

    "Sora Level 51": KHDDDLocationData(region="Levels", code=2660051,category="Slot"),
    "Sora Level 52": KHDDDLocationData(region="Levels", code=2660052,category="Slot"),
    "Sora Level 53": KHDDDLocationData(region="Levels", code=2660053,category="Slot"),
    "Sora Level 54": KHDDDLocationData(region="Levels", code=2660054,category="Slot"),
    "Sora Level 55": KHDDDLocationData(region="Levels", code=2660055,category="Slot"),
    "Sora Level 56": KHDDDLocationData(region="Levels", code=2660056,category="Slot"),
    "Sora Level 57": KHDDDLocationData(region="Levels", code=2660057,category="Slot"),
    "Sora Level 58": KHDDDLocationData(region="Levels", code=2660058,category="Slot"),
    "Sora Level 59": KHDDDLocationData(region="Levels", code=2660059,category="Slot"),
    "Sora Level 60": KHDDDLocationData(region="Levels", code=2660060, category="Slot"),
    "Sora Level 61": KHDDDLocationData(region="Levels", code=2660061, category="Slot"),
    "Sora Level 62": KHDDDLocationData(region="Levels", code=2660062, category="Slot"),
    "Sora Level 63": KHDDDLocationData(region="Levels", code=2660063, category="Slot"),
    "Sora Level 64": KHDDDLocationData(region="Levels", code=2660064, category="Slot"),
    "Sora Level 65": KHDDDLocationData(region="Levels", code=2660065, category="Slot"),
    "Sora Level 66": KHDDDLocationData(region="Levels", code=2660066, category="Slot"),
    "Sora Level 67": KHDDDLocationData(region="Levels", code=2660067, category="Slot"),
    "Sora Level 68": KHDDDLocationData(region="Levels", code=2660068, category="Slot"),
    "Sora Level 69": KHDDDLocationData(region="Levels", code=2660069, category="Slot"),
    "Sora Level 70": KHDDDLocationData(region="Levels", code=2660070, category="Slot"),
    "Sora Level 71": KHDDDLocationData(region="Levels", code=2660071, category="Slot"),
    "Sora Level 72": KHDDDLocationData(region="Levels", code=2660072, category="Slot"),
    "Sora Level 73": KHDDDLocationData(region="Levels", code=2660073, category="Slot"),
    "Sora Level 74": KHDDDLocationData(region="Levels", code=2660074, category="Slot"),
    "Sora Level 75": KHDDDLocationData(region="Levels", code=2660075, category="Slot"),
    "Sora Level 76": KHDDDLocationData(region="Levels", code=2660076, category="Slot"),
    "Sora Level 77": KHDDDLocationData(region="Levels", code=2660077, category="Slot"),
    "Sora Level 78": KHDDDLocationData(region="Levels", code=2660078, category="Slot"),
    "Sora Level 79": KHDDDLocationData(region="Levels", code=2660079, category="Slot"),
    "Sora Level 80": KHDDDLocationData(region="Levels", code=2660080, category="Slot"),
    "Sora Level 81": KHDDDLocationData(region="Levels", code=2660081, category="Slot"),
    "Sora Level 82": KHDDDLocationData(region="Levels", code=2660082, category="Slot"),
    "Sora Level 83": KHDDDLocationData(region="Levels", code=2660083, category="Slot"),
    "Sora Level 84": KHDDDLocationData(region="Levels", code=2660084, category="Slot"),
    "Sora Level 85": KHDDDLocationData(region="Levels", code=2660085, category="Slot"),
    "Sora Level 86": KHDDDLocationData(region="Levels", code=2660086, category="Slot"),
    "Sora Level 87": KHDDDLocationData(region="Levels", code=2660087, category="Slot"),
    "Sora Level 88": KHDDDLocationData(region="Levels", code=2660088, category="Slot"),
    "Sora Level 89": KHDDDLocationData(region="Levels", code=2660089, category="Slot"),
    "Sora Level 90": KHDDDLocationData(region="Levels", code=2660090, category="Slot"),
    "Sora Level 91": KHDDDLocationData(region="Levels", code=2660091, category="Slot"),
    "Sora Level 92": KHDDDLocationData(region="Levels", code=2660092, category="Slot"),
    "Sora Level 93": KHDDDLocationData(region="Levels", code=2660093, category="Slot"),
    "Sora Level 94": KHDDDLocationData(region="Levels", code=2660094, category="Slot"),
    "Sora Level 95": KHDDDLocationData(region="Levels", code=2660095, category="Slot"),
    "Sora Level 96": KHDDDLocationData(region="Levels", code=2660096, category="Slot"),
    "Sora Level 97": KHDDDLocationData(region="Levels", code=2660097, category="Slot"),
    "Sora Level 98": KHDDDLocationData(region="Levels", code=2660098, category="Slot"),
    "Sora Level 99": KHDDDLocationData(region="Levels", code=2660099, category="Slot"),

    "Riku Level 02": KHDDDLocationData(region="Levels",code=2660102,category="Slot"),
    "Riku Level 03": KHDDDLocationData(region="Levels",code=2660103,category="Slot"),
    "Riku Level 04": KHDDDLocationData(region="Levels",code=2660104,category="Slot"),
    "Riku Level 05": KHDDDLocationData(region="Levels",code=2660105,category="Slot"),
    "Riku Level 06": KHDDDLocationData(region="Levels",code=2660106,category="Slot"),
    "Riku Level 07": KHDDDLocationData(region="Levels", code=2660107,category="Slot"),
    "Riku Level 08": KHDDDLocationData(region="Levels", code=2660108,category="Slot"),
    "Riku Level 09": KHDDDLocationData(region="Levels", code=2660109,category="Slot"),
    "Riku Level 10": KHDDDLocationData(region="Levels", code=2660110,category="Slot"),
    "Riku Level 11": KHDDDLocationData(region="Levels", code=2660111,category="Slot"),
    "Riku Level 12": KHDDDLocationData(region="Levels", code=2660112,category="Slot"),
    "Riku Level 13": KHDDDLocationData(region="Levels", code=2660113,category="Slot"),
    "Riku Level 14": KHDDDLocationData(region="Levels", code=2660114,category="Slot"),
    "Riku Level 15": KHDDDLocationData(region="Levels", code=2660115,category="Slot"),
    "Riku Level 16": KHDDDLocationData(region="Levels", code=2660116,category="Slot"),
    "Riku Level 17": KHDDDLocationData(region="Levels", code=2660117,category="Slot"),
    "Riku Level 18": KHDDDLocationData(region="Levels", code=2660118,category="Slot"),
    "Riku Level 19": KHDDDLocationData(region="Levels", code=2660119,category="Slot"),
    "Riku Level 20": KHDDDLocationData(region="Levels", code=2660120,category="Slot"),
    "Riku Level 21": KHDDDLocationData(region="Levels", code=2660121,category="Slot"),
    "Riku Level 22": KHDDDLocationData(region="Levels", code=2660122,category="Slot"),
    "Riku Level 23": KHDDDLocationData(region="Levels", code=2660123,category="Slot"),
    "Riku Level 24": KHDDDLocationData(region="Levels", code=2660124,category="Slot"),
    "Riku Level 25": KHDDDLocationData(region="Levels", code=2660125,category="Slot"),
    "Riku Level 26": KHDDDLocationData(region="Levels", code=2660126,category="Slot"),
    "Riku Level 27": KHDDDLocationData(region="Levels", code=2660127,category="Slot"),
    "Riku Level 28": KHDDDLocationData(region="Levels", code=2660128,category="Slot"),
    "Riku Level 29": KHDDDLocationData(region="Levels", code=2660129,category="Slot"),
    "Riku Level 30": KHDDDLocationData(region="Levels", code=2660130,category="Slot"),
    "Riku Level 31": KHDDDLocationData(region="Levels", code=2660131,category="Slot"),
    "Riku Level 32": KHDDDLocationData(region="Levels", code=2660132,category="Slot"),
    "Riku Level 33": KHDDDLocationData(region="Levels", code=2660133,category="Slot"),
    "Riku Level 34": KHDDDLocationData(region="Levels", code=2660134,category="Slot"),
    "Riku Level 35": KHDDDLocationData(region="Levels", code=2660135,category="Slot"),
    "Riku Level 36": KHDDDLocationData(region="Levels", code=2660136,category="Slot"),
    "Riku Level 37": KHDDDLocationData(region="Levels", code=2660137,category="Slot"),
    "Riku Level 38": KHDDDLocationData(region="Levels", code=2660138,category="Slot"),
    "Riku Level 39": KHDDDLocationData(region="Levels", code=2660139,category="Slot"),
    "Riku Level 40": KHDDDLocationData(region="Levels", code=2660140,category="Slot"),
    "Riku Level 41": KHDDDLocationData(region="Levels", code=2660141,category="Slot"),
    "Riku Level 42": KHDDDLocationData(region="Levels", code=2660142,category="Slot"),
    "Riku Level 43": KHDDDLocationData(region="Levels", code=2660143,category="Slot"),
    "Riku Level 44": KHDDDLocationData(region="Levels", code=2660144,category="Slot"),
    "Riku Level 45": KHDDDLocationData(region="Levels", code=2660145,category="Slot"),
    "Riku Level 46": KHDDDLocationData(region="Levels", code=2660146,category="Slot"),
    "Riku Level 47": KHDDDLocationData(region="Levels", code=2660147,category="Slot"),
    "Riku Level 48": KHDDDLocationData(region="Levels", code=2660148,category="Slot"),
    "Riku Level 49": KHDDDLocationData(region="Levels", code=2660149,category="Slot"),
    "Riku Level 50": KHDDDLocationData(region="Levels", code=2660150,category="Slot"),

    "Riku Level 51": KHDDDLocationData(region="Levels", code=2660151,category="Slot"),
    "Riku Level 52": KHDDDLocationData(region="Levels", code=2660152,category="Slot"),
    "Riku Level 53": KHDDDLocationData(region="Levels", code=2660153,category="Slot"),
    "Riku Level 54": KHDDDLocationData(region="Levels", code=2660154,category="Slot"),
    "Riku Level 55": KHDDDLocationData(region="Levels", code=2660155,category="Slot"),
    "Riku Level 56": KHDDDLocationData(region="Levels", code=2660156,category="Slot"),
    "Riku Level 57": KHDDDLocationData(region="Levels", code=2660157,category="Slot"),
    "Riku Level 58": KHDDDLocationData(region="Levels", code=2660158,category="Slot"),
    "Riku Level 59": KHDDDLocationData(region="Levels", code=2660159,category="Slot"),
    "Riku Level 60": KHDDDLocationData(region="Levels", code=2660160, category="Slot"),
    "Riku Level 61": KHDDDLocationData(region="Levels", code=2660161, category="Slot"),
    "Riku Level 62": KHDDDLocationData(region="Levels", code=2660162, category="Slot"),
    "Riku Level 63": KHDDDLocationData(region="Levels", code=2660163, category="Slot"),
    "Riku Level 64": KHDDDLocationData(region="Levels", code=2660164, category="Slot"),
    "Riku Level 65": KHDDDLocationData(region="Levels", code=2660165, category="Slot"),
    "Riku Level 66": KHDDDLocationData(region="Levels", code=2660166, category="Slot"),
    "Riku Level 67": KHDDDLocationData(region="Levels", code=2660167, category="Slot"),
    "Riku Level 68": KHDDDLocationData(region="Levels", code=2660168, category="Slot"),
    "Riku Level 69": KHDDDLocationData(region="Levels", code=2660169, category="Slot"),
    "Riku Level 70": KHDDDLocationData(region="Levels", code=2660170, category="Slot"),
    "Riku Level 71": KHDDDLocationData(region="Levels", code=2660171, category="Slot"),
    "Riku Level 72": KHDDDLocationData(region="Levels", code=2660172, category="Slot"),
    "Riku Level 73": KHDDDLocationData(region="Levels", code=2660173, category="Slot"),
    "Riku Level 74": KHDDDLocationData(region="Levels", code=2660174, category="Slot"),
    "Riku Level 75": KHDDDLocationData(region="Levels", code=2660175, category="Slot"),
    "Riku Level 76": KHDDDLocationData(region="Levels", code=2660176, category="Slot"),
    "Riku Level 77": KHDDDLocationData(region="Levels", code=2660177, category="Slot"),
    "Riku Level 78": KHDDDLocationData(region="Levels", code=2660178, category="Slot"),
    "Riku Level 79": KHDDDLocationData(region="Levels", code=2660179, category="Slot"),
    "Riku Level 80": KHDDDLocationData(region="Levels", code=2660180, category="Slot"),
    "Riku Level 81": KHDDDLocationData(region="Levels", code=2660181, category="Slot"),
    "Riku Level 82": KHDDDLocationData(region="Levels", code=2660182, category="Slot"),
    "Riku Level 83": KHDDDLocationData(region="Levels", code=2660183, category="Slot"),
    "Riku Level 84": KHDDDLocationData(region="Levels", code=2660184, category="Slot"),
    "Riku Level 85": KHDDDLocationData(region="Levels", code=2660185, category="Slot"),
    "Riku Level 86": KHDDDLocationData(region="Levels", code=2660186, category="Slot"),
    "Riku Level 87": KHDDDLocationData(region="Levels", code=2660187, category="Slot"),
    "Riku Level 88": KHDDDLocationData(region="Levels", code=2660188, category="Slot"),
    "Riku Level 89": KHDDDLocationData(region="Levels", code=2660189, category="Slot"),
    "Riku Level 90": KHDDDLocationData(region="Levels", code=2660190, category="Slot"),
    "Riku Level 91": KHDDDLocationData(region="Levels", code=2660191, category="Slot"),
    "Riku Level 92": KHDDDLocationData(region="Levels", code=2660192, category="Slot"),
    "Riku Level 93": KHDDDLocationData(region="Levels", code=2660193, category="Slot"),
    "Riku Level 94": KHDDDLocationData(region="Levels", code=2660194, category="Slot"),
    "Riku Level 95": KHDDDLocationData(region="Levels", code=2660195, category="Slot"),
    "Riku Level 96": KHDDDLocationData(region="Levels", code=2660196, category="Slot"),
    "Riku Level 97": KHDDDLocationData(region="Levels", code=2660197, category="Slot"),
    "Riku Level 98": KHDDDLocationData(region="Levels", code=2660198, category="Slot"),
    "Riku Level 99": KHDDDLocationData(region="Levels", code=2660199, category="Slot"),
}

event_location_table: Dict[str, KHDDDLocationData] = {}
location_table = {name: data.code for name, data in location_data_table.items() if data.code is not None}

lookup_id_to_name: typing.Dict[int, str] = {data.code: name for name, data in location_data_table.items() if data.code}

location_name_groups: Dict[str, Set[str]] = { #TODO: Streamline this
    "Meow Wow Ability Link": {"Meow Wow Node 01", "Meow Wow Node 02", "Meow Wow Node 03", "Meow Wow Node 04", "Meow Wow Node 05", "Meow Wow Node 06", "Meow Wow Node 07", "Meow Wow Node 08",
                              "Meow Wow Node 09", "Meow Wow Node 10", "Meow Wow Node 11", "Meow Wow Node 12", "Meow Wow Node 13", "Meow Wow Node 14", "Meow Wow Node 15", "Meow Wow Node 16"},
    "Tama Sheep Ability Link": {"Tama Sheep Node 01", "Tama Sheep Node 02", "Tama Sheep Node 03", "Tama Sheep Node 04", "Tama Sheep Node 05", "Tama Sheep Node 06", "Tama Sheep Node 07", "Tama Sheep Node 08",
                              "Tama Sheep Node 09", "Tama Sheep Node 10", "Tama Sheep Node 11", "Tama Sheep Node 12", "Tama Sheep Node 13", "Tama Sheep Node 14", "Tama Sheep Node 15", "Tama Sheep Node 16"},
    "Yoggy Ram Ability Link": {"Yoggy Ram Node 01", "Yoggy Ram Node 02", "Yoggy Ram Node 03", "Yoggy Ram Node 04", "Yoggy Ram Node 05", "Yoggy Ram Node 06", "Yoggy Ram Node 07", "Yoggy Ram Node 08",
                              "Yoggy Ram Node 09", "Yoggy Ram Node 10", "Yoggy Ram Node 11", "Yoggy Ram Node 12", "Yoggy Ram Node 13", "Yoggy Ram Node 14", "Yoggy Ram Node 15", "Yoggy Ram Node 16"},
    "Komory Bat Ability Link": {"Komory Bat Node 01", "Komory Bat Node 02", "Komory Bat Node 03", "Komory Bat Node 04","Komory Bat Node 05", "Komory Bat Node 06", "Komory Bat Node 07", "Komory Bat Node 08",
                                "Komory Bat Node 09", "Komory Bat Node 10", "Komory Bat Node 11", "Komory Bat Node 12", "Komory Bat Node 13", "Komory Bat Node 14", "Komory Bat Node 15", "Komory Bat Node 16"},
    "Pricklemane Ability Link": {"Pricklemane Node 01", "Pricklemane Node 02", "Pricklemane Node 03", "Pricklemane Node 04","Pricklemane Node 05", "Pricklemane Node 06", "Pricklemane Node 07", "Pricklemane Node 08",
                                "Pricklemane Node 09", "Pricklemane Node 10", "Pricklemane Node 11", "Pricklemane Node 12", "Pricklemane Node 13", "Pricklemane Node 14", "Pricklemane Node 15", "Pricklemane Node 16"},
    "Hebby Repp Ability Link": {"Hebby Repp Node 01", "Hebby Repp Node 02", "Hebby Repp Node 03", "Hebby Repp Node 04","Hebby Repp Node 05", "Hebby Repp Node 06", "Hebby Repp Node 07", "Hebby Repp Node 08",
                                "Hebby Repp Node 09", "Hebby Repp Node 10", "Hebby Repp Node 11", "Hebby Repp Node 12", "Hebby Repp Node 13", "Hebby Repp Node 14", "Hebby Repp Node 15", "Hebby Repp Node 16"},
    "Sir Kyroo Ability Link": {"Sir Kyroo Node 01", "Sir Kyroo Node 02", "Sir Kyroo Node 03", "Sir Kyroo Node 04","Sir Kyroo Node 05", "Sir Kyroo Node 06", "Sir Kyroo Node 07", "Sir Kyroo Node 08",
                                "Sir Kyroo Node 09", "Sir Kyroo Node 10", "Sir Kyroo Node 11", "Sir Kyroo Node 12", "Sir Kyroo Node 13", "Sir Kyroo Node 14", "Sir Kyroo Node 15", "Sir Kyroo Node 16"},
    "Toximander Ability Link": {"Toximander Node 01", "Toximander Node 02", "Toximander Node 03", "Toximander Node 04","Toximander Node 05", "Toximander Node 06", "Toximander Node 07", "Toximander Node 08",
                                "Toximander Node 09", "Toximander Node 10", "Toximander Node 11", "Toximander Node 12", "Toximander Node 13", "Toximander Node 14", "Toximander Node 15", "Toximander Node 16"},
    "Fin Fatale Ability Link": {"Fin Fatale Node 01", "Fin Fatale Node 02", "Fin Fatale Node 03", "Fin Fatale Node 04","Fin Fatale Node 05", "Fin Fatale Node 06", "Fin Fatale Node 07", "Fin Fatale Node 08",
                                "Fin Fatale Node 09", "Fin Fatale Node 10", "Fin Fatale Node 11", "Fin Fatale Node 12", "Fin Fatale Node 13", "Fin Fatale Node 14", "Fin Fatale Node 15", "Fin Fatale Node 16"},
    "Tatsu Steed Ability Link": {"Tatsu Steed Node 01", "Tatsu Steed Node 02", "Tatsu Steed Node 03", "Tatsu Steed Node 04","Tatsu Steed Node 05", "Tatsu Steed Node 06", "Tatsu Steed Node 07", "Tatsu Steed Node 08",
                                "Tatsu Steed Node 09", "Tatsu Steed Node 10", "Tatsu Steed Node 11", "Tatsu Steed Node 12", "Tatsu Steed Node 13", "Tatsu Steed Node 14", "Tatsu Steed Node 15", "Tatsu Steed Node 16"},
    "Necho Cat Ability Link": {"Necho Cat Node 01", "Necho Cat Node 02", "Necho Cat Node 03", "Necho Cat Node 04","Necho Cat Node 05", "Necho Cat Node 06", "Necho Cat Node 07", "Necho Cat Node 08",
                                "Necho Cat Node 09", "Necho Cat Node 10", "Necho Cat Node 11", "Necho Cat Node 12", "Necho Cat Node 13", "Necho Cat Node 14", "Necho Cat Node 15", "Necho Cat Node 16"},
    "Thunderaffe Ability Link": {"Thunderaffe Node 01", "Thunderaffe Node 02", "Thunderaffe Node 03", "Thunderaffe Node 04","Thunderaffe Node 05", "Thunderaffe Node 06", "Thunderaffe Node 07", "Thunderaffe Node 08",
                                "Thunderaffe Node 09", "Thunderaffe Node 10", "Thunderaffe Node 11", "Thunderaffe Node 12", "Thunderaffe Node 13", "Thunderaffe Node 14", "Thunderaffe Node 15", "Thunderaffe Node 16"},
    "Kooma Panda Ability Link": {"Kooma Panda Node 01", "Kooma Panda Node 02", "Kooma Panda Node 03", "Kooma Panda Node 04","Kooma Panda Node 05", "Kooma Panda Node 06", "Kooma Panda Node 07", "Kooma Panda Node 08",
                                "Kooma Panda Node 09", "Kooma Panda Node 10", "Kooma Panda Node 11", "Kooma Panda Node 12", "Kooma Panda Node 13", "Kooma Panda Node 14", "Kooma Panda Node 15", "Kooma Panda Node 16"},
    "Pegaslick Ability Link": {"Pegaslick Node 01", "Pegaslick Node 02", "Pegaslick Node 03", "Pegaslick Node 04","Pegaslick Node 05", "Pegaslick Node 06", "Pegaslick Node 07", "Pegaslick Node 08",
                                "Pegaslick Node 09", "Pegaslick Node 10", "Pegaslick Node 11", "Pegaslick Node 12", "Pegaslick Node 13", "Pegaslick Node 14", "Pegaslick Node 15", "Pegaslick Node 16"},
    "Iceguin Ace Ability Link": {"Iceguin Ace Node 01", "Iceguin Ace Node 02", "Iceguin Ace Node 03", "Iceguin Ace Node 04","Iceguin Ace Node 05", "Iceguin Ace Node 06", "Iceguin Ace Node 07", "Iceguin Ace Node 08",
                                "Iceguin Ace Node 09", "Iceguin Ace Node 10", "Iceguin Ace Node 11", "Iceguin Ace Node 12", "Iceguin Ace Node 13", "Iceguin Ace Node 14", "Iceguin Ace Node 15", "Iceguin Ace Node 16"},
    "Peepsta Hoo Ability Link": {"Peepsta Hoo Node 01", "Peepsta Hoo Node 02", "Peepsta Hoo Node 03", "Peepsta Hoo Node 04","Peepsta Hoo Node 05", "Peepsta Hoo Node 06", "Peepsta Hoo Node 07", "Peepsta Hoo Node 08",
                                "Peepsta Hoo Node 09", "Peepsta Hoo Node 10", "Peepsta Hoo Node 11", "Peepsta Hoo Node 12", "Peepsta Hoo Node 13", "Peepsta Hoo Node 14", "Peepsta Hoo Node 15", "Peepsta Hoo Node 16"},
    "Escarglow Ability Link": {"Escarglow Node 01", "Escarglow Node 02", "Escarglow Node 03", "Escarglow Node 04","Escarglow Node 05", "Escarglow Node 06", "Escarglow Node 07", "Escarglow Node 08",
                                "Escarglow Node 09", "Escarglow Node 10", "Escarglow Node 11", "Escarglow Node 12", "Escarglow Node 13", "Escarglow Node 14", "Escarglow Node 15", "Escarglow Node 16"},
    "KO Kabuto Ability Link": {"KO Kabuto Node 01", "KO Kabuto Node 02", "KO Kabuto Node 03", "KO Kabuto Node 04","KO Kabuto Node 05", "KO Kabuto Node 06", "KO Kabuto Node 07", "KO Kabuto Node 08",
                                "KO Kabuto Node 09", "KO Kabuto Node 10", "KO Kabuto Node 11", "KO Kabuto Node 12", "KO Kabuto Node 13", "KO Kabuto Node 14", "KO Kabuto Node 15", "KO Kabuto Node 16"},
    "Wheeflower Ability Link": {"Wheeflower Node 01", "Wheeflower Node 02", "Wheeflower Node 03", "Wheeflower Node 04","Wheeflower Node 05", "Wheeflower Node 06", "Wheeflower Node 07", "Wheeflower Node 08",
                                "Wheeflower Node 09", "Wheeflower Node 10", "Wheeflower Node 11", "Wheeflower Node 12", "Wheeflower Node 13", "Wheeflower Node 14", "Wheeflower Node 15", "Wheeflower Node 16"},
    "Ghostabocky Ability Link": {"Ghostabocky Node 01", "Ghostabocky Node 02", "Ghostabocky Node 03", "Ghostabocky Node 04","Ghostabocky Node 05", "Ghostabocky Node 06", "Ghostabocky Node 07", "Ghostabocky Node 08",
                                "Ghostabocky Node 09", "Ghostabocky Node 10", "Ghostabocky Node 11", "Ghostabocky Node 12", "Ghostabocky Node 13", "Ghostabocky Node 14", "Ghostabocky Node 15", "Ghostabocky Node 16"},
    "Zolephant Ability Link": {"Zolephant Node 01", "Zolephant Node 02", "Zolephant Node 03", "Zolephant Node 04","Zolephant Node 05", "Zolephant Node 06", "Zolephant Node 07", "Zolephant Node 08",
                                "Zolephant Node 09", "Zolephant Node 10", "Zolephant Node 11", "Zolephant Node 12", "Zolephant Node 13", "Zolephant Node 14", "Zolephant Node 15", "Zolephant Node 16"},
    "Juggle Pup Ability Link": {"Juggle Pup Node 01", "Juggle Pup Node 02", "Juggle Pup Node 03", "Juggle Pup Node 04","Juggle Pup Node 05", "Juggle Pup Node 06", "Juggle Pup Node 07", "Juggle Pup Node 08",
                                "Juggle Pup Node 09", "Juggle Pup Node 10", "Juggle Pup Node 11", "Juggle Pup Node 12", "Juggle Pup Node 13", "Juggle Pup Node 14", "Juggle Pup Node 15", "Juggle Pup Node 16"},
    "Halbird Ability Link": {"Halbird Node 01", "Halbird Node 02", "Halbird Node 03", "Halbird Node 04","Halbird Node 05", "Halbird Node 06", "Halbird Node 07", "Halbird Node 08",
                                "Halbird Node 09", "Halbird Node 10", "Halbird Node 11", "Halbird Node 12", "Halbird Node 13", "Halbird Node 14", "Halbird Node 15", "Halbird Node 16"},
    "Staggerceps Ability Link": {"Staggerceps Node 01", "Staggerceps Node 02", "Staggerceps Node 03", "Staggerceps Node 04","Staggerceps Node 05", "Staggerceps Node 06", "Staggerceps Node 07", "Staggerceps Node 08",
                                "Staggerceps Node 09", "Staggerceps Node 10", "Staggerceps Node 11", "Staggerceps Node 12", "Staggerceps Node 13", "Staggerceps Node 14", "Staggerceps Node 15", "Staggerceps Node 16"},
    "Fishbone Ability Link": {"Fishbone Node 01", "Fishbone Node 02", "Fishbone Node 03", "Fishbone Node 04","Fishbone Node 05", "Fishbone Node 06", "Fishbone Node 07", "Fishbone Node 08",
                                "Fishbone Node 09", "Fishbone Node 10", "Fishbone Node 11", "Fishbone Node 12", "Fishbone Node 13", "Fishbone Node 14", "Fishbone Node 15", "Fishbone Node 16"},
    "Flowbermeow Ability Link": {"Flowbermeow Node 01", "Flowbermeow Node 02", "Flowbermeow Node 03", "Flowbermeow Node 04","Flowbermeow Node 05", "Flowbermeow Node 06", "Flowbermeow Node 07", "Flowbermeow Node 08",
                                "Flowbermeow Node 09", "Flowbermeow Node 10", "Flowbermeow Node 11", "Flowbermeow Node 12", "Flowbermeow Node 13", "Flowbermeow Node 14", "Flowbermeow Node 15", "Flowbermeow Node 16"},
    "Cyber Yog Ability Link": {"Cyber Yog Node 01", "Cyber Yog Node 02", "Cyber Yog Node 03", "Cyber Yog Node 04","Cyber Yog Node 05", "Cyber Yog Node 06", "Cyber Yog Node 07", "Cyber Yog Node 08",
                                "Cyber Yog Node 09", "Cyber Yog Node 10", "Cyber Yog Node 11", "Cyber Yog Node 12", "Cyber Yog Node 13", "Cyber Yog Node 14", "Cyber Yog Node 15", "Cyber Yog Node 16"},
    "Chef Kyroo Ability Link": {"Chef Kyroo Node 01", "Chef Kyroo Node 02", "Chef Kyroo Node 03", "Chef Kyroo Node 04","Chef Kyroo Node 05", "Chef Kyroo Node 06", "Chef Kyroo Node 07", "Chef Kyroo Node 08",
                                "Chef Kyroo Node 09", "Chef Kyroo Node 10", "Chef Kyroo Node 11", "Chef Kyroo Node 12", "Chef Kyroo Node 13", "Chef Kyroo Node 14", "Chef Kyroo Node 15", "Chef Kyroo Node 16"},
    "Lord Kyroo Ability Link": {"Lord Kyroo Node 01", "Lord Kyroo Node 02", "Lord Kyroo Node 03", "Lord Kyroo Node 04","Lord Kyroo Node 05", "Lord Kyroo Node 06", "Lord Kyroo Node 07", "Lord Kyroo Node 08",
                                "Lord Kyroo Node 09", "Lord Kyroo Node 10", "Lord Kyroo Node 11", "Lord Kyroo Node 12", "Lord Kyroo Node 13", "Lord Kyroo Node 14", "Lord Kyroo Node 15", "Lord Kyroo Node 16"},
    "Tatsu Blaze Ability Link": {"Tatsu Blaze Node 01", "Tatsu Blaze Node 02", "Tatsu Blaze Node 03", "Tatsu Blaze Node 04","Tatsu Blaze Node 05", "Tatsu Blaze Node 06", "Tatsu Blaze Node 07", "Tatsu Blaze Node 08",
                                "Tatsu Blaze Node 09", "Tatsu Blaze Node 10", "Tatsu Blaze Node 11", "Tatsu Blaze Node 12", "Tatsu Blaze Node 13", "Tatsu Blaze Node 14", "Tatsu Blaze Node 15", "Tatsu Blaze Node 16"},
    "Electricorn Ability Link": {"Electricorn Node 01", "Electricorn Node 02", "Electricorn Node 03", "Electricorn Node 04","Electricorn Node 05", "Electricorn Node 06", "Electricorn Node 07", "Electricorn Node 08",
                                "Electricorn Node 09", "Electricorn Node 10", "Electricorn Node 11", "Electricorn Node 12", "Electricorn Node 13", "Electricorn Node 14", "Electricorn Node 15", "Electricorn Node 16"},
    "Woeflower Ability Link": {"Woeflower Node 01", "Woeflower Node 02", "Woeflower Node 03", "Woeflower Node 04","Woeflower Node 05", "Woeflower Node 06", "Woeflower Node 07", "Woeflower Node 08",
                                "Woeflower Node 09", "Woeflower Node 10", "Woeflower Node 11", "Woeflower Node 12", "Woeflower Node 13", "Woeflower Node 14", "Woeflower Node 15", "Woeflower Node 16"},
    "Jestabocky Ability Link": {"Jestabocky Node 01", "Jestabocky Node 02", "Jestabocky Node 03", "Jestabocky Node 04","Jestabocky Node 05", "Jestabocky Node 06", "Jestabocky Node 07", "Jestabocky Node 08",
                                "Jestabocky Node 09", "Jestabocky Node 10", "Jestabocky Node 11", "Jestabocky Node 12", "Jestabocky Node 13", "Jestabocky Node 14", "Jestabocky Node 15", "Jestabocky Node 16"},
    "Eaglider Ability Link": {"Eaglider Node 01", "Eaglider Node 02", "Eaglider Node 03", "Eaglider Node 04","Eaglider Node 05", "Eaglider Node 06", "Eaglider Node 07", "Eaglider Node 08",
                                "Eaglider Node 09", "Eaglider Node 10", "Eaglider Node 11", "Eaglider Node 12", "Eaglider Node 13", "Eaglider Node 14", "Eaglider Node 15", "Eaglider Node 16"},
    "Me Me Bunny Ability Link": {"Me Me Bunny Node 01", "Me Me Bunny Node 02", "Me Me Bunny Node 03", "Me Me Bunny Node 04","Me Me Bunny Node 05", "Me Me Bunny Node 06", "Me Me Bunny Node 07", "Me Me Bunny Node 08",
                                "Me Me Bunny Node 09", "Me Me Bunny Node 10", "Me Me Bunny Node 11", "Me Me Bunny Node 12", "Me Me Bunny Node 13", "Me Me Bunny Node 14", "Me Me Bunny Node 15", "Me Me Bunny Node 16"},
    "Drill Sye Ability Link": {"Drill Sye Node 01", "Drill Sye Node 02", "Drill Sye Node 03", "Drill Sye Node 04","Drill Sye Node 05", "Drill Sye Node 06", "Drill Sye Node 07", "Drill Sye Node 08",
                                "Drill Sye Node 09", "Drill Sye Node 10", "Drill Sye Node 11", "Drill Sye Node 12", "Drill Sye Node 13", "Drill Sye Node 14", "Drill Sye Node 15", "Drill Sye Node 16"},
    "Tyranto Rex Ability Link": {"Tyranto Rex Node 01", "Tyranto Rex Node 02", "Tyranto Rex Node 03", "Tyranto Rex Node 04","Tyranto Rex Node 05", "Tyranto Rex Node 06", "Tyranto Rex Node 07", "Tyranto Rex Node 08",
                                "Tyranto Rex Node 09", "Tyranto Rex Node 10", "Tyranto Rex Node 11", "Tyranto Rex Node 12", "Tyranto Rex Node 13", "Tyranto Rex Node 14", "Tyranto Rex Node 15", "Tyranto Rex Node 16"},
    "Majik Lapin Ability Link": {"Majik Lapin Node 01", "Majik Lapin Node 02", "Majik Lapin Node 03", "Majik Lapin Node 04","Majik Lapin Node 05", "Majik Lapin Node 06", "Majik Lapin Node 07", "Majik Lapin Node 08",
                                "Majik Lapin Node 09", "Majik Lapin Node 10", "Majik Lapin Node 11", "Majik Lapin Node 12", "Majik Lapin Node 13", "Majik Lapin Node 14", "Majik Lapin Node 15", "Majik Lapin Node 16"},
    "Cera Terror Ability Link": {"Cera Terror Node 01", "Cera Terror Node 02", "Cera Terror Node 03", "Cera Terror Node 04","Cera Terror Node 05", "Cera Terror Node 06", "Cera Terror Node 07", "Cera Terror Node 08",
                                "Cera Terror Node 09", "Cera Terror Node 10", "Cera Terror Node 11", "Cera Terror Node 12", "Cera Terror Node 13", "Cera Terror Node 14", "Cera Terror Node 15", "Cera Terror Node 16"},
    "Skelterwild Ability Link": {"Skelterwild Node 01", "Skelterwild Node 02", "Skelterwild Node 03", "Skelterwild Node 04","Skelterwild Node 05", "Skelterwild Node 06", "Skelterwild Node 07", "Skelterwild Node 08",
                                "Skelterwild Node 09", "Skelterwild Node 10", "Skelterwild Node 11", "Skelterwild Node 12", "Skelterwild Node 13", "Skelterwild Node 14", "Skelterwild Node 15", "Skelterwild Node 16"},
    "Ducky Goose Ability Link": {"Ducky Goose Node 01", "Ducky Goose Node 02", "Ducky Goose Node 03", "Ducky Goose Node 04","Ducky Goose Node 05", "Ducky Goose Node 06", "Ducky Goose Node 07", "Ducky Goose Node 08",
                                "Ducky Goose Node 09", "Ducky Goose Node 10", "Ducky Goose Node 11", "Ducky Goose Node 12", "Ducky Goose Node 13", "Ducky Goose Node 14", "Ducky Goose Node 15", "Ducky Goose Node 16"},
    "Aura Lion Ability Link": {"Aura Lion Node 01", "Aura Lion Node 02", "Aura Lion Node 03", "Aura Lion Node 04","Aura Lion Node 05", "Aura Lion Node 06", "Aura Lion Node 07", "Aura Lion Node 08",
                                "Aura Lion Node 09", "Aura Lion Node 10", "Aura Lion Node 11", "Aura Lion Node 12", "Aura Lion Node 13", "Aura Lion Node 14", "Aura Lion Node 15", "Aura Lion Node 16"},
    "Ryu Dragon Ability Link": {"Ryu Dragon Node 01", "Ryu Dragon Node 02", "Ryu Dragon Node 03", "Ryu Dragon Node 04","Ryu Dragon Node 05", "Ryu Dragon Node 06", "Ryu Dragon Node 07", "Ryu Dragon Node 08",
                                "Ryu Dragon Node 09", "Ryu Dragon Node 10", "Ryu Dragon Node 11", "Ryu Dragon Node 12", "Ryu Dragon Node 13", "Ryu Dragon Node 14", "Ryu Dragon Node 15", "Ryu Dragon Node 16"},
    "Drak Quack Ability Link": {"Drak Quack Node 01", "Drak Quack Node 02", "Drak Quack Node 03", "Drak Quack Node 04","Drak Quack Node 05", "Drak Quack Node 06", "Drak Quack Node 07", "Drak Quack Node 08",
                                "Drak Quack Node 09", "Drak Quack Node 10", "Drak Quack Node 11", "Drak Quack Node 12", "Drak Quack Node 13", "Drak Quack Node 14", "Drak Quack Node 15", "Drak Quack Node 16"},
    "Keeba Tiger Ability Link": {"Keeba Tiger Node 01", "Keeba Tiger Node 02", "Keeba Tiger Node 03", "Keeba Tiger Node 04","Keeba Tiger Node 05", "Keeba Tiger Node 06", "Keeba Tiger Node 07", "Keeba Tiger Node 08",
                                "Keeba Tiger Node 09", "Keeba Tiger Node 10", "Keeba Tiger Node 11", "Keeba Tiger Node 12", "Keeba Tiger Node 13", "Keeba Tiger Node 14", "Keeba Tiger Node 15", "Keeba Tiger Node 16"},
    "Meowjesty Ability Link": {"Meowjesty Node 01", "Meowjesty Node 02", "Meowjesty Node 03", "Meowjesty Node 04","Meowjesty Node 05", "Meowjesty Node 06", "Meowjesty Node 07", "Meowjesty Node 08",
                                "Meowjesty Node 09", "Meowjesty Node 10", "Meowjesty Node 11", "Meowjesty Node 12", "Meowjesty Node 13", "Meowjesty Node 14", "Meowjesty Node 15", "Meowjesty Node 16"},
    "Sudo Neku Ability Link": {"Sudo Neku Node 01", "Sudo Neku Node 02", "Sudo Neku Node 03", "Sudo Neku Node 04","Sudo Neku Node 05", "Sudo Neku Node 06", "Sudo Neku Node 07", "Sudo Neku Node 08",
                                "Sudo Neku Node 09", "Sudo Neku Node 10", "Sudo Neku Node 11", "Sudo Neku Node 12", "Sudo Neku Node 13", "Sudo Neku Node 14", "Sudo Neku Node 15", "Sudo Neku Node 16"},
    "Frootz Cat Ability Link": {"Frootz Cat Node 01", "Frootz Cat Node 02", "Frootz Cat Node 03", "Frootz Cat Node 04","Frootz Cat Node 05", "Frootz Cat Node 06", "Frootz Cat Node 07", "Frootz Cat Node 08",
                                "Frootz Cat Node 09", "Frootz Cat Node 10", "Frootz Cat Node 11", "Frootz Cat Node 12", "Frootz Cat Node 13", "Frootz Cat Node 14", "Frootz Cat Node 15", "Frootz Cat Node 16"},
    "Ursa Circus Ability Link": {"Ursa Circus Node 01", "Ursa Circus Node 02", "Ursa Circus Node 03", "Ursa Circus Node 04","Ursa Circus Node 05", "Ursa Circus Node 06", "Ursa Circus Node 07", "Ursa Circus Node 08",
                                "Ursa Circus Node 09", "Ursa Circus Node 10", "Ursa Circus Node 11", "Ursa Circus Node 12", "Ursa Circus Node 13", "Ursa Circus Node 14", "Ursa Circus Node 15", "Ursa Circus Node 16"},
    "Kab Kannon Ability Link": {"Kab Kannon Node 01", "Kab Kannon Node 02", "Kab Kannon Node 03", "Kab Kannon Node 04","Kab Kannon Node 05", "Kab Kannon Node 06", "Kab Kannon Node 07", "Kab Kannon Node 08",
                                "Kab Kannon Node 09", "Kab Kannon Node 10", "Kab Kannon Node 11", "Kab Kannon Node 12", "Kab Kannon Node 13", "Kab Kannon Node 14", "Kab Kannon Node 15", "Kab Kannon Node 16"},
    "R & R Seal Ability Link": {"R & R Seal Node 01", "R & R Seal Node 02", "R & R Seal Node 03", "R & R Seal Node 04","R & R Seal Node 05", "R & R Seal Node 06", "R & R Seal Node 07", "R & R Seal Node 08",
                                "R & R Seal Node 09", "R & R Seal Node 10", "R & R Seal Node 11", "R & R Seal Node 12", "R & R Seal Node 13", "R & R Seal Node 14", "R & R Seal Node 15", "R & R Seal Node 16"},
    "Catanuki Ability Link": {"Catanuki Node 01", "Catanuki Node 02", "Catanuki Node 03", "Catanuki Node 04","Catanuki Node 05", "Catanuki Node 06", "Catanuki Node 07", "Catanuki Node 08",
                                "Catanuki Node 09", "Catanuki Node 10", "Catanuki Node 11", "Catanuki Node 12", "Catanuki Node 13", "Catanuki Node 14", "Catanuki Node 15", "Catanuki Node 16"},
    "Beatalike Ability Link": {"Beatalike Node 01", "Beatalike Node 02", "Beatalike Node 03", "Beatalike Node 04","Beatalike Node 05", "Beatalike Node 06", "Beatalike Node 07", "Beatalike Node 08",
                                "Beatalike Node 09", "Beatalike Node 10", "Beatalike Node 11", "Beatalike Node 12", "Beatalike Node 13", "Beatalike Node 14", "Beatalike Node 15", "Beatalike Node 16"},
    "Tubguin Ace Ability Link": {"Tubguin Ace Node 01", "Tubguin Ace Node 02", "Tubguin Ace Node 03", "Tubguin Ace Node 04","Tubguin Ace Node 05", "Tubguin Ace Node 06", "Tubguin Ace Node 07", "Tubguin Ace Node 08",
                                "Tubguin Ace Node 09", "Tubguin Ace Node 10", "Tubguin Ace Node 11", "Tubguin Ace Node 12", "Tubguin Ace Node 13", "Tubguin Ace Node 14", "Tubguin Ace Node 15", "Tubguin Ace Node 16"},
}

#Which nodes are locked behind gates
gate_thresholds = { #First node counts starting from 0
    "Meow Wow": [7, 11],
    "Tama Sheep": [4, 11],
    "Yoggy Ram": [9, 12],
    "Komory Bat": [12, 8],
    "Pricklemane": [5, 10],
    "Hebby Repp": [7],
    "Sir Kyroo": [7, 11],
    "Toximander": [7],
    "Fin Fatale": [8, 12],
    "Tatsu Steed": [7],
    "Necho Cat": [8],
    "Thunderaffe": [8],
    "Kooma Panda": [6, 12],
    "Pegaslick": [10, 13],
    "Iceguin Ace": [7],
    "Peepsta Hoo": [8],
    "Escarglow": [8],
    "KO Kabuto": [5, 12],
    "Wheeflower": [8],
    "Ghostabocky": [14], #Technically has 2 gates
    "Zolephant": [7],
    "Juggle Pup": [7, 12],
    "Halbird": [8, 12],
    "Staggerceps": [7],
    "Fishbone": [8],
    "Flowbermeow": [8, 12],
    "Cyber Yog": [7],
    "Chef Kyroo": [6, 11],
    "Lord Kyroo": [7, 11],
    "Tatsu Blaze": [8, 12],
    "Electricorn": [6, 11],
    "Woeflower": [6],
    "Jestabocky": [9, 12],
    "Eaglider": [8],
    "Me Me Bunny": [7, 11],
    "Drill Sye": [7],
    "Tyranto Rex": [11, 6],
    "Majik Lapin": [8, 12],
    "Cera Terror": [6, 11],
    "Skelterwild": [6, 11],
    "Ducky Goose": [12, 8],
    "Aura Lion": [6],
    "Ryu Dragon": [6],
    "Drak Quack": [11, 6],
    "Keeba Tiger": [6],
    "Meowjesty": [6, 11],
    "Sudo Neku": [6],
    "Frootz Cat": [11, 6],
    "Ursa Circus": [6, 11],
    "Kab Kannon": [6, 11],
    "R & R Seal": [6, 11],
    "Catanuki": [11, 6],
    "Beatalike": [7],
    "Tubguin Ace": [12, 8]
}

#Make location categories
#location_name_groups: Dict[str, Set[str]] = {}
#for location in location_data_table.keys():
#    region = event_location_table[location].region
#    if region not in location_name_groups.keys():
#        location_name_groups[region] = set()
#    location_name_groups[region].add(location)