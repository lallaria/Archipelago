# This file was generated using jinja2 from a template. If this file needs
# to be changed, either change the template, or the code leveraging the template.
from enum import Enum, IntEnum
from typing import List, NamedTuple, Dict, Optional, Set
from worlds.gstla.GameData import ElementType, ItemType
from BaseClasses import ItemClassification
from .ItemNames import ItemName

class TrapType(str, Enum):
   Mimic = "Mimic"

class FillerType(str, Enum):
    ForgeMaterials = "Forge Materials"
    RustyMaterials = "Rusty Materials"
    StatBoosts = "Stat Boosts"
    UsefulConsumables = "Useful Consumables"
    ForgedEquipment = "Forged Equipment"
    LuckyEquipment = "Lucky Equipment"
    ShopEquipment = "Shop Equipment"
    Coins = "Coins"
    CommonConsumables = "Common Consumables"

class ItemData(NamedTuple):
    id: int
    name: str
    progression: ItemClassification
    addr: int
    type: ItemType
    # TODO: The event type is really a property of the locations, not of the items
    # event_type:int = 131
    is_mimic: bool =  False

class DjinnItemData(ItemData):
    element: ElementType
    vanilla_id: int
    stats_addr: int
    stats: List[int]

    def __new__(cls, id: int, name: str, addr: int, element: ElementType, stats_addr: int, stats: List[int]):
        self = super(ItemData, cls).__new__(cls, (addr, name, ItemClassification.progression_skip_balancing, addr, ItemType.Djinn))
        self.element = element
        self.stats_addr = stats_addr
        self.stats = stats
        self.vanilla_id = id
        return self

    def get_rando_flag(self):
        return 0x30 + self.element * 20 + self.vanilla_id

class EventItemData(ItemData):
    flag: int
    location: str

    def __new__(cls, event_id: int, flag: int, location: str, name: str):
        self = super(ItemData, cls).__new__(cls, (event_id, name, ItemClassification.progression, 0, ItemType.Event, 0))
        self.location = location
        self.flag = flag
        return self

summon_list: List[ItemData] = [
    ItemData(3840, 'Venus', ItemClassification.useful, 791824, ItemType.Psyenergy),
    ItemData(3841, 'Mercury', ItemClassification.useful, 791832, ItemType.Psyenergy),
    ItemData(3842, 'Mars', ItemClassification.useful, 791840, ItemType.Psyenergy),
    ItemData(3843, 'Jupiter', ItemClassification.useful, 791848, ItemType.Psyenergy),
    ItemData(3844, 'Ramses', ItemClassification.useful, 791856, ItemType.Psyenergy),
    ItemData(3845, 'Nereid', ItemClassification.useful, 791864, ItemType.Psyenergy),
    ItemData(3846, 'Kirin', ItemClassification.useful, 791872, ItemType.Psyenergy),
    ItemData(3847, 'Atalanta', ItemClassification.useful, 791880, ItemType.Psyenergy),
    ItemData(3848, 'Cybele', ItemClassification.useful, 791888, ItemType.Psyenergy),
    ItemData(3849, 'Neptune', ItemClassification.useful, 791896, ItemType.Psyenergy),
    ItemData(3850, 'Tiamat', ItemClassification.useful, 791904, ItemType.Psyenergy),
    ItemData(3851, 'Procne', ItemClassification.useful, 791912, ItemType.Psyenergy),
    ItemData(3852, 'Judgment', ItemClassification.useful, 791920, ItemType.Psyenergy),
    ItemData(3853, 'Boreas', ItemClassification.useful, 791928, ItemType.Psyenergy),
    ItemData(3854, 'Meteor', ItemClassification.useful, 791936, ItemType.Psyenergy),
    ItemData(3855, 'Thor', ItemClassification.useful, 791944, ItemType.Psyenergy),
    ItemData(3856, 'Zagan', ItemClassification.useful, 791952, ItemType.Psyenergy),
    ItemData(3857, 'Megaera', ItemClassification.useful, 791960, ItemType.Psyenergy),
    ItemData(3858, 'Flora', ItemClassification.useful, 791968, ItemType.Psyenergy),
    ItemData(3859, 'Moloch', ItemClassification.useful, 791976, ItemType.Psyenergy),
    ItemData(3860, 'Ulysses', ItemClassification.useful, 791984, ItemType.Psyenergy),
    ItemData(3861, 'Haures', ItemClassification.useful, 791992, ItemType.Psyenergy),
    ItemData(3862, 'Eclipse', ItemClassification.useful, 792000, ItemType.Psyenergy),
    ItemData(3863, 'Coatlique', ItemClassification.useful, 792008, ItemType.Psyenergy),
    ItemData(3864, 'Daedalus', ItemClassification.useful, 792016, ItemType.Psyenergy),
    ItemData(3865, 'Azul', ItemClassification.useful, 792024, ItemType.Psyenergy),
    ItemData(3866, 'Catastrophe', ItemClassification.useful, 792032, ItemType.Psyenergy),
    ItemData(3867, 'Charon', ItemClassification.useful, 792040, ItemType.Psyenergy),
    ItemData(3868, 'Iris', ItemClassification.useful, 792048, ItemType.Psyenergy),
    
]

psyenergy_list: List[ItemData] = [
    ItemData(3596, "Growth", ItemClassification.progression, 3596, ItemType.Psyenergy),
    ItemData(3662, "Whirlwind", ItemClassification.progression, 3662, ItemType.Psyenergy),
    ItemData(3722, "Parch", ItemClassification.progression, 3722, ItemType.Psyenergy),
    ItemData(3723, "Sand", ItemClassification.progression, 3723, ItemType.Psyenergy),
    ItemData(3725, "Mind Read", ItemClassification.progression, 3725, ItemType.Psyenergy),
    ItemData(3728, "Reveal", ItemClassification.progression, 3728, ItemType.Psyenergy),
    ItemData(3738, "Blaze", ItemClassification.progression, 3738, ItemType.Psyenergy),
    
]

psyenergy_as_item_list: List[ItemData] = [
    ItemData(133 + 0xE00, 'Lash Pebble', ItemClassification.progression, 738668, ItemType.PsyenergyItem),
    ItemData(134 + 0xE00, 'Pound Cube', ItemClassification.progression, 738712, ItemType.PsyenergyItem),
    ItemData(142 + 0xE00, 'Orb of Force', ItemClassification.progression, 738756, ItemType.PsyenergyItem),
    ItemData(33 + 0xE00, 'Douse Drop', ItemClassification.progression, 738800, ItemType.PsyenergyItem),
    ItemData(24 + 0xE00, 'Frost Jewel', ItemClassification.progression, 738844, ItemType.PsyenergyItem),
    ItemData(143 + 0xE00, 'Lifting Gem', ItemClassification.progression, 738888, ItemType.PsyenergyItem),
    ItemData(145 + 0xE00, 'Halt Gem', ItemClassification.progression, 738932, ItemType.PsyenergyItem),
    ItemData(146 + 0xE00, 'Cloak Ball', ItemClassification.progression, 738976, ItemType.PsyenergyItem),
    ItemData(147 + 0xE00, 'Carry Stone', ItemClassification.progression, 739020, ItemType.PsyenergyItem),
    ItemData(148 + 0xE00, 'Catch Beads', ItemClassification.progression, 739064, ItemType.PsyenergyItem),
    ItemData(135 + 0xE00, 'Tremor Bit', ItemClassification.progression, 739108, ItemType.PsyenergyItem),
    ItemData(136 + 0xE00, 'Scoop Gem', ItemClassification.progression, 739152, ItemType.PsyenergyItem),
    ItemData(137 + 0xE00, 'Cyclone Chip', ItemClassification.progression, 739196, ItemType.PsyenergyItem),
    ItemData(151 + 0xE00, 'Burst Brooch', ItemClassification.progression, 739328, ItemType.PsyenergyItem),
    ItemData(152 + 0xE00, 'Grindstone', ItemClassification.progression, 739372, ItemType.PsyenergyItem),
    ItemData(153 + 0xE00, 'Hover Jade', ItemClassification.progression, 739416, ItemType.PsyenergyItem),
    ItemData(156 + 0xE00, 'Teleport Lapis', ItemClassification.progression, 739504, ItemType.PsyenergyItem),
    
]

djinn_items: List[ItemData] = [
    DjinnItemData(0, 'Flint', 16384000, ElementType(ElementType.Earth), 814004, [8, 4, 3, 0, 0, 0]),
    DjinnItemData(1, 'Granite', 16384002, ElementType(ElementType.Earth), 814016, [9, 0, 0, 2, 2, 1]),
    DjinnItemData(2, 'Quartz', 16384004, ElementType(ElementType.Earth), 814028, [10, 3, 0, 0, 3, 0]),
    DjinnItemData(3, 'Vine', 16384006, ElementType(ElementType.Earth), 814040, [12, 4, 0, 3, 0, 1]),
    DjinnItemData(4, 'Sap', 16384008, ElementType(ElementType.Earth), 814052, [10, 0, 3, 0, 0, 1]),
    DjinnItemData(5, 'Ground', 16384010, ElementType(ElementType.Earth), 814064, [9, 3, 0, 0, 3, 0]),
    DjinnItemData(6, 'Bane', 16384012, ElementType(ElementType.Earth), 814076, [12, 0, 4, 0, 0, 0]),
    DjinnItemData(7, 'Echo', 16384014, ElementType(ElementType.Earth), 814088, [9, 4, 3, 0, 0, 0]),
    DjinnItemData(8, 'Iron', 16384016, ElementType(ElementType.Earth), 814100, [11, 0, 0, 2, 3, 0]),
    DjinnItemData(9, 'Steel', 16384018, ElementType(ElementType.Earth), 814112, [9, 0, 4, 2, 0, 1]),
    DjinnItemData(10, 'Mud', 16384020, ElementType(ElementType.Earth), 814124, [10, 4, 0, 0, 3, 0]),
    DjinnItemData(11, 'Flower', 16384022, ElementType(ElementType.Earth), 814136, [12, 4, 0, 0, 0, 0]),
    DjinnItemData(12, 'Meld', 16384024, ElementType(ElementType.Earth), 814148, [9, 0, 0, 0, 4, 1]),
    DjinnItemData(13, 'Petra', 16384026, ElementType(ElementType.Earth), 814160, [11, 0, 0, 3, 0, 0]),
    DjinnItemData(14, 'Salt', 16384028, ElementType(ElementType.Earth), 814172, [9, 5, 0, 0, 0, 1]),
    DjinnItemData(15, 'Geode', 16384030, ElementType(ElementType.Earth), 814184, [12, 0, 6, 0, 0, 0]),
    DjinnItemData(16, 'Mold', 16384032, ElementType(ElementType.Earth), 814196, [8, 0, 4, 0, 2, 1]),
    DjinnItemData(17, 'Crystal', 16384034, ElementType(ElementType.Earth), 814208, [10, 5, 0, 2, 0, 0]),
    DjinnItemData(0, 'Fizz', 16384036, ElementType(ElementType.Water), 814244, [9, 4, 0, 3, 0, 0]),
    DjinnItemData(1, 'Sleet', 16384038, ElementType(ElementType.Water), 814256, [12, 0, 3, 0, 0, 1]),
    DjinnItemData(2, 'Mist', 16384040, ElementType(ElementType.Water), 814268, [11, 0, 4, 0, 0, 0]),
    DjinnItemData(3, 'Spritz', 16384042, ElementType(ElementType.Water), 814280, [8, 4, 0, 0, 3, 0]),
    DjinnItemData(4, 'Hail', 16384044, ElementType(ElementType.Water), 814292, [9, 0, 4, 0, 0, 1]),
    DjinnItemData(5, 'Tonic', 16384046, ElementType(ElementType.Water), 814304, [8, 3, 0, 2, 0, 2]),
    DjinnItemData(6, 'Dew', 16384048, ElementType(ElementType.Water), 814316, [13, 4, 0, 0, 4, 0]),
    DjinnItemData(7, 'Fog', 16384050, ElementType(ElementType.Water), 814328, [9, 0, 0, 2, 2, 1]),
    DjinnItemData(8, 'Sour', 16384052, ElementType(ElementType.Water), 814340, [8, 4, 3, 0, 0, 0]),
    DjinnItemData(9, 'Spring', 16384054, ElementType(ElementType.Water), 814352, [11, 5, 0, 0, 0, 0]),
    DjinnItemData(10, 'Shade', 16384056, ElementType(ElementType.Water), 814364, [9, 0, 0, 3, 0, 2]),
    DjinnItemData(11, 'Chill', 16384058, ElementType(ElementType.Water), 814376, [10, 3, 0, 2, 0, 0]),
    DjinnItemData(12, 'Steam', 16384060, ElementType(ElementType.Water), 814388, [10, 0, 5, 0, 0, 0]),
    DjinnItemData(13, 'Rime', 16384062, ElementType(ElementType.Water), 814400, [10, 6, 0, 0, 0, 0]),
    DjinnItemData(14, 'Gel', 16384064, ElementType(ElementType.Water), 814412, [9, 0, 5, 0, 2, 0]),
    DjinnItemData(15, 'Eddy', 16384066, ElementType(ElementType.Water), 814424, [9, 0, 0, 0, 3, 2]),
    DjinnItemData(16, 'Balm', 16384068, ElementType(ElementType.Water), 814436, [13, 4, 0, 0, 0, 0]),
    DjinnItemData(17, 'Serac', 16384070, ElementType(ElementType.Water), 814448, [12, 0, 3, 0, 0, 0]),
    DjinnItemData(0, 'Forge', 16384072, ElementType(ElementType.Fire), 814484, [10, 0, 2, 0, 2, 2]),
    DjinnItemData(1, 'Fever', 16384074, ElementType(ElementType.Fire), 814496, [8, 0, 3, 0, 2, 0]),
    DjinnItemData(2, 'Corona', 16384076, ElementType(ElementType.Fire), 814508, [12, 3, 0, 3, 0, 1]),
    DjinnItemData(3, 'Scorch', 16384078, ElementType(ElementType.Fire), 814520, [8, 0, 3, 0, 0, 0]),
    DjinnItemData(4, 'Ember', 16384080, ElementType(ElementType.Fire), 814532, [9, 4, 0, 2, 2, 0]),
    DjinnItemData(5, 'Flash', 16384082, ElementType(ElementType.Fire), 814544, [14, 3, 0, 2, 0, 0]),
    DjinnItemData(6, 'Torch', 16384084, ElementType(ElementType.Fire), 814556, [9, 0, 3, 0, 0, 1]),
    DjinnItemData(7, 'Cannon', 16384086, ElementType(ElementType.Fire), 814568, [10, 0, 3, 0, 0, 0]),
    DjinnItemData(8, 'Spark', 16384088, ElementType(ElementType.Fire), 814580, [11, 6, 0, 0, 0, 0]),
    DjinnItemData(9, 'Kindle', 16384090, ElementType(ElementType.Fire), 814592, [8, 0, 5, 0, 0, 1]),
    DjinnItemData(10, 'Char', 16384092, ElementType(ElementType.Fire), 814604, [9, 0, 2, 0, 2, 1]),
    DjinnItemData(11, 'Coal', 16384094, ElementType(ElementType.Fire), 814616, [11, 3, 0, 0, 3, 0]),
    DjinnItemData(12, 'Reflux', 16384096, ElementType(ElementType.Fire), 814628, [9, 0, 0, 3, 0, 2]),
    DjinnItemData(13, 'Core', 16384098, ElementType(ElementType.Fire), 814640, [8, 0, 4, 2, 0, 0]),
    DjinnItemData(14, 'Tinder', 16384100, ElementType(ElementType.Fire), 814652, [12, 5, 0, 0, 0, 0]),
    DjinnItemData(15, 'Shine', 16384102, ElementType(ElementType.Fire), 814664, [9, 0, 3, 3, 2, 0]),
    DjinnItemData(16, 'Fury', 16384104, ElementType(ElementType.Fire), 814676, [12, 4, 0, 0, 0, 0]),
    DjinnItemData(17, 'Fugue', 16384106, ElementType(ElementType.Fire), 814688, [11, 4, 0, 2, 0, 0]),
    DjinnItemData(0, 'Gust', 16384108, ElementType(ElementType.Air), 814724, [9, 0, 2, 0, 2, 0]),
    DjinnItemData(1, 'Breeze', 16384110, ElementType(ElementType.Air), 814736, [12, 5, 0, 2, 0, 1]),
    DjinnItemData(2, 'Zephyr', 16384112, ElementType(ElementType.Air), 814748, [11, 3, 0, 0, 2, 1]),
    DjinnItemData(3, 'Smog', 16384114, ElementType(ElementType.Air), 814760, [9, 0, 3, 0, 0, 0]),
    DjinnItemData(4, 'Kite', 16384116, ElementType(ElementType.Air), 814772, [8, 4, 0, 0, 3, 0]),
    DjinnItemData(5, 'Squall', 16384118, ElementType(ElementType.Air), 814784, [10, 0, 5, 0, 0, 0]),
    DjinnItemData(6, 'Luff', 16384120, ElementType(ElementType.Air), 814796, [11, 5, 0, 2, 0, 1]),
    DjinnItemData(7, 'Breath', 16384122, ElementType(ElementType.Air), 814808, [9, 0, 0, 3, 4, 0]),
    DjinnItemData(8, 'Blitz', 16384124, ElementType(ElementType.Air), 814820, [10, 4, 3, 0, 0, 0]),
    DjinnItemData(9, 'Ether', 16384126, ElementType(ElementType.Air), 814832, [8, 4, 0, 0, 3, 2]),
    DjinnItemData(10, 'Waft', 16384128, ElementType(ElementType.Air), 814844, [11, 0, 4, 0, 0, 0]),
    DjinnItemData(11, 'Haze', 16384130, ElementType(ElementType.Air), 814856, [10, 0, 0, 2, 3, 2]),
    DjinnItemData(12, 'Wheeze', 16384132, ElementType(ElementType.Air), 814868, [9, 3, 5, 0, 0, 0]),
    DjinnItemData(13, 'Aroma', 16384134, ElementType(ElementType.Air), 814880, [11, 0, 0, 0, 3, 2]),
    DjinnItemData(14, 'Whorl', 16384136, ElementType(ElementType.Air), 814892, [9, 0, 4, 2, 0, 0]),
    DjinnItemData(15, 'Gasp', 16384138, ElementType(ElementType.Air), 814904, [12, 5, 0, 0, 0, 0]),
    DjinnItemData(16, 'Lull', 16384140, ElementType(ElementType.Air), 814916, [11, 6, 0, 0, 0, 0]),
    DjinnItemData(17, 'Gale', 16384142, ElementType(ElementType.Air), 814928, [10, 0, 0, 0, 5, 3]),
    
]



events: List[EventItemData] = [
    EventItemData(5001, 1912, "Mars Lighthouse - Doom Dragon Fight", "Victory"),
    EventItemData(5002, 2219, "Alhafra Briggs", "Briggs defeated"),
    EventItemData(5003, 2431, "Alhafra Prison Briggs", "Briggs escaped"),
    EventItemData(5004, 2303, "Gabomba Statue", "Gabomba Statue Completed"),
    EventItemData(5005, 2542, "Gaia Rock - Serpent Fight", "Serpent defeated"),
    EventItemData(5006, 2269, "Sea of Time - Poseidon fight", "Poseidon defeated"),
    EventItemData(5007, 2367, "Lemurian Ship - Aqua Hydra fight", "Aqua Hydra defeated"),
    EventItemData(5008, 2381, "Shaman Village - Moapa fight", "Moapa defeated"),
    EventItemData(5009, 2593, "Jupiter_Lighthouse Aeri - Agatio and Karst fight", "Jupiter Beacon Lit"),
    EventItemData(5010, 2635, "Mars Lighthouse - Flame Dragons fight", "Flame Dragons - defeated"),
    EventItemData(5011, 2270, "Lemurian Ship - Engine Room", "Ship"),
    EventItemData(5012, 2271, "Contigo - Wings of Anemos", "Wings of Anemos"),
    
]

characters: List[ItemData] = [
    ItemData(3328, "Isaac", ItemClassification.progression, 16384384, ItemType.Character),
    ItemData(3329, "Garet", ItemClassification.progression, 16384386, ItemType.Character),
    ItemData(3330, "Ivan", ItemClassification.progression, 16384388, ItemType.Character),
    ItemData(3331, "Mia", ItemClassification.progression, 16384390, ItemType.Character),
    ItemData(3333, "Jenna", ItemClassification.progression, 16384392, ItemType.Character),
    ItemData(3334, "Sheba", ItemClassification.progression, 16384394, ItemType.Character),
    ItemData(3335, "Piers", ItemClassification.progression, 16384396, ItemType.Character),
    
]

mimics: List[ItemData] = [
ItemData(2561, "Milquetoast Mimic", ItemClassification.trap, 991872, ItemType.Mimic, True),
ItemData(2562, "Clumsy Mimic", ItemClassification.trap, 992520, ItemType.Mimic, True),
ItemData(2563, "Mimic", ItemClassification.trap, 992852, ItemType.Mimic, True),
ItemData(2564, "Journeyman Mimic", ItemClassification.trap, 993268, ItemType.Mimic, True),
ItemData(2565, "Advanced Mimic", ItemClassification.trap, 993476, ItemType.Mimic, True),
ItemData(2566, "Sacred Mimic", ItemClassification.trap, 994268, ItemType.Mimic, True),
ItemData(2567, "Royal Mimic", ItemClassification.trap, 994388, ItemType.Mimic, True),
ItemData(2568, "Imperial Mimic", ItemClassification.trap, 994536, ItemType.Mimic, True),
ItemData(2569, "Divine Mimic", ItemClassification.trap, 994644, ItemType.Mimic, True),

]

other_progression: List[ItemData] = [
ItemData(65, "Shaman's Rod", ItemClassification.progression, 732816, ItemType.Weapon, False),
ItemData(222, "Mars Star", ItemClassification.progression, 739724, ItemType.KeyItem, False),
ItemData(242, "Black Crystal", ItemClassification.progression, 740604, ItemType.Consumable, False),
ItemData(243, "Red Key", ItemClassification.progression, 740648, ItemType.Consumable, False),
ItemData(244, "Blue Key", ItemClassification.progression, 740692, ItemType.Consumable, False),
ItemData(326, "Trident", ItemClassification.progression, 744300, ItemType.Trident, False),
ItemData(439, "Right Prong", ItemClassification.progression, 749272, ItemType.Consumable, False),
ItemData(440, "Left Prong", ItemClassification.progression, 749316, ItemType.Consumable, False),
ItemData(441, "Center Prong", ItemClassification.progression, 749360, ItemType.Consumable, False),
ItemData(448, "Healing Fungus", ItemClassification.progression, 749668, ItemType.Consumable, False),
ItemData(451, "Dancing Idol", ItemClassification.progression, 749800, ItemType.Consumable, False),
ItemData(452, "Pretty Stone", ItemClassification.progression, 749844, ItemType.Consumable, False),
ItemData(453, "Red Cloth", ItemClassification.progression, 749888, ItemType.Consumable, False),
ItemData(454, "Milk", ItemClassification.progression, 749932, ItemType.Consumable, False),
ItemData(455, "Li'l Turtle", ItemClassification.progression, 749976, ItemType.Consumable, False),
ItemData(456, "Aquarius Stone", ItemClassification.progression, 750020, ItemType.Consumable, False),
ItemData(458, "Sea God's Tear", ItemClassification.progression, 750108, ItemType.Consumable, False),
ItemData(459, "Ruin Key", ItemClassification.progression, 750152, ItemType.Consumable, False),
ItemData(460, "Magma Ball", ItemClassification.progression, 750196, ItemType.Consumable, False),

]

useful_consumables = [
    
        ItemData(186, "Psy Crystal", ItemClassification.useful, 738140, ItemType.Consumable, False),
        ItemData(189, "Water of Life", ItemClassification.useful, 738272, ItemType.Consumable, False),
        ItemData(190, "Mist Potion", ItemClassification.useful, 738316, ItemType.Consumable, False),
        ItemData(183, "Potion", ItemClassification.useful, 738008, ItemType.Consumable, False),
]

stat_boosters = [
    
        ItemData(192, "Cookie", ItemClassification.useful, 738404, ItemType.Consumable, False),
        ItemData(193, "Apple", ItemClassification.useful, 738448, ItemType.Consumable, False),
        ItemData(194, "Hard Nut", ItemClassification.useful, 738492, ItemType.Consumable, False),
        ItemData(195, "Mint", ItemClassification.useful, 738536, ItemType.Consumable, False),
        ItemData(196, "Lucky Pepper", ItemClassification.useful, 738580, ItemType.Consumable, False),
        ItemData(191, "Power Bread", ItemClassification.useful, 738360, ItemType.Consumable, False),
]

rusty_items = [
    
        ItemData(417, "Rusty Sword - Robber's Blade", ItemClassification.useful, 748304, ItemType.Weapon, False),
        ItemData(418, "Rusty Sword - Soul Brand", ItemClassification.useful, 748348, ItemType.Weapon, False),
        ItemData(419, "Rusty Sword - Corsair's Edge", ItemClassification.useful, 748392, ItemType.Weapon, False),
        ItemData(420, "Rusty Sword - Pirate's Sabre", ItemClassification.useful, 748436, ItemType.Weapon, False),
        ItemData(421, "Rusty Axe - Captain's Axe", ItemClassification.useful, 748480, ItemType.Weapon, False),
        ItemData(422, "Rusty Axe - Viking Axe", ItemClassification.useful, 748524, ItemType.Weapon, False),
        ItemData(423, "Rusty Mace - Demon Mace", ItemClassification.useful, 748568, ItemType.Weapon, False),
        ItemData(424, "Rusty Mace - Hagbone Mace", ItemClassification.useful, 748612, ItemType.Weapon, False),
        ItemData(425, "Rusty Staff - Dracomace", ItemClassification.useful, 748656, ItemType.Weapon, False),
        ItemData(426, "Rusty Staff - Glower Staff", ItemClassification.useful, 748700, ItemType.Weapon, False),
        ItemData(427, "Rusty Staff - Goblin's Rod", ItemClassification.useful, 748744, ItemType.Weapon, False),
]

forge_materials = [
    
        ItemData(429, "Tear Stone", ItemClassification.useful, 748832, ItemType.Consumable, False),
        ItemData(430, "Star Dust", ItemClassification.useful, 748876, ItemType.Consumable, False),
        ItemData(431, "Sylph Feather", ItemClassification.useful, 748920, ItemType.Consumable, False),
        ItemData(432, "Dragon Skin", ItemClassification.useful, 748964, ItemType.Consumable, False),
        ItemData(433, "Salamander Tail", ItemClassification.useful, 749008, ItemType.Consumable, False),
        ItemData(434, "Golem Core", ItemClassification.useful, 749052, ItemType.Consumable, False),
        ItemData(435, "Mythril Silver", ItemClassification.useful, 749096, ItemType.Consumable, False),
        ItemData(436, "Dark Matter", ItemClassification.useful, 749140, ItemType.Consumable, False),
        ItemData(437, "Orihalcon", ItemClassification.useful, 749184, ItemType.Consumable, False),
]

class_change_items = [
    
        ItemData(443, "Mysterious Card", ItemClassification.useful, 749448, ItemType.Class, False),
        ItemData(444, "Trainer's Whip", ItemClassification.useful, 749492, ItemType.Class, False),
        ItemData(445, "Tomegathericon", ItemClassification.useful, 749536, ItemType.Class, False),
]



useful_remainder = [
    
        ItemData(384, "Thorn Crown", ItemClassification.useful, 746852, ItemType.Helm, False),
        ItemData(259, "Turtle Boots", ItemClassification.useful, 741352, ItemType.Boots, False),
        ItemData(388, "Alastor's Hood", ItemClassification.useful, 747028, ItemType.Helm, False),
        ItemData(7, "Fire Brand", ItemClassification.useful, 730264, ItemType.Weapon, False),
        ItemData(10, "Sol Blade", ItemClassification.useful, 730396, ItemType.Weapon, False),
        ItemData(266, "Unicorn Ring", ItemClassification.useful, 741660, ItemType.Ring, False),
        ItemData(394, "Clarity Circlet", ItemClassification.useful, 747292, ItemType.Helm, False),
        ItemData(279, "Storm Brand", ItemClassification.useful, 742232, ItemType.Weapon, False),
        ItemData(281, "Lightning Sword", ItemClassification.useful, 742320, ItemType.Weapon, False),
        ItemData(26, "Masamune", ItemClassification.useful, 731100, ItemType.Weapon, False),
        ItemData(283, "Cloud Brand", ItemClassification.useful, 742408, ItemType.Weapon, False),
        ItemData(414, "Guardian Ring", ItemClassification.useful, 748172, ItemType.Ring, False),
        ItemData(287, "Pirate's Sword", ItemClassification.useful, 742584, ItemType.Weapon, False),
        ItemData(290, "Hypnos' Sword", ItemClassification.useful, 742716, ItemType.Weapon, False),
        ItemData(291, "Mist Sabre", ItemClassification.useful, 742760, ItemType.Weapon, False),
        ItemData(292, "Phaeton's Blade", ItemClassification.useful, 742804, ItemType.Weapon, False),
        ItemData(300, "Disk Axe", ItemClassification.useful, 743156, ItemType.Weapon, False),
        ItemData(301, "Themis' Axe", ItemClassification.useful, 743200, ItemType.Weapon, False),
        ItemData(309, "Blow Mace", ItemClassification.useful, 743552, ItemType.Weapon, False),
        ItemData(311, "Thanatos Mace", ItemClassification.useful, 743640, ItemType.Weapon, False),
        ItemData(319, "Meditation Rod", ItemClassification.useful, 743992, ItemType.Weapon, False),
        ItemData(333, "Ixion Mail", ItemClassification.useful, 744608, ItemType.Armor, False),
        ItemData(334, "Phantasmal Mail", ItemClassification.useful, 744652, ItemType.Armor, False),
        ItemData(336, "Valkyrie Mail", ItemClassification.useful, 744740, ItemType.Armor, False),
        ItemData(340, "Full Metal Vest", ItemClassification.useful, 744916, ItemType.Armor, False),
        ItemData(343, "Festival Coat", ItemClassification.useful, 745048, ItemType.Armor, False),
        ItemData(344, "Erinyes Tunic", ItemClassification.useful, 745092, ItemType.Armor, False),
        ItemData(349, "Muni Robe", ItemClassification.useful, 745312, ItemType.Armor, False),
        ItemData(351, "Iris Robe", ItemClassification.useful, 745400, ItemType.Armor, False),
        ItemData(358, "Fujin Shield", ItemClassification.useful, 745708, ItemType.Shield, False),
        ItemData(366, "Spirit Gloves", ItemClassification.useful, 746060, ItemType.Shield, False),
        ItemData(370, "Bone Armlet", ItemClassification.useful, 746236, ItemType.Shield, False),
        ItemData(371, "Jester's Armlet", ItemClassification.useful, 746280, ItemType.Shield, False),
        ItemData(378, "Viking Helm", ItemClassification.useful, 746588, ItemType.Helm, False),
        ItemData(383, "Nurse's Cap", ItemClassification.useful, 746808, ItemType.Helm, False),
]

other_useful: List[ItemData] = useful_remainder  + useful_consumables  + stat_boosters  + rusty_items  + forge_materials  + class_change_items 



shop_only: List[ItemData] = [
ItemData(1, "Long Sword", ItemClassification.filler, 730000, ItemType.Weapon, False),
ItemData(2, "Broad Sword", ItemClassification.filler, 730044, ItemType.Weapon, False),
ItemData(3, "Claymore", ItemClassification.filler, 730088, ItemType.Weapon, False),
ItemData(4, "Great Sword", ItemClassification.filler, 730132, ItemType.Weapon, False),
ItemData(5, "Shamshir", ItemClassification.filler, 730176, ItemType.Weapon, False),
ItemData(6, "Silver Blade", ItemClassification.filler, 730220, ItemType.Weapon, False),
ItemData(16, "Short Sword", ItemClassification.filler, 730660, ItemType.Weapon, False),
ItemData(17, "Hunter's Sword", ItemClassification.filler, 730704, ItemType.Weapon, False),
ItemData(18, "Battle Rapier", ItemClassification.filler, 730748, ItemType.Weapon, False),
ItemData(19, "Master Rapier", ItemClassification.filler, 730792, ItemType.Weapon, False),
ItemData(20, "Ninja Blade", ItemClassification.filler, 730836, ItemType.Weapon, False),
ItemData(21, "Swift Sword", ItemClassification.filler, 730880, ItemType.Weapon, False),
ItemData(31, "Battle Axe", ItemClassification.filler, 731320, ItemType.Weapon, False),
ItemData(32, "Broad Axe", ItemClassification.filler, 731364, ItemType.Weapon, False),
ItemData(33, "Great Axe", ItemClassification.filler, 731408, ItemType.Weapon, False),
ItemData(34, "Dragon Axe", ItemClassification.filler, 731452, ItemType.Weapon, False),
ItemData(43, "Mace", ItemClassification.filler, 731848, ItemType.Weapon, False),
ItemData(44, "Heavy Mace", ItemClassification.filler, 731892, ItemType.Weapon, False),
ItemData(45, "Battle Mace", ItemClassification.filler, 731936, ItemType.Weapon, False),
ItemData(46, "War Mace", ItemClassification.filler, 731980, ItemType.Weapon, False),
ItemData(47, "Righteous Mace", ItemClassification.filler, 732024, ItemType.Weapon, False),
ItemData(55, "Wooden Stick", ItemClassification.filler, 732376, ItemType.Weapon, False),
ItemData(56, "Magic Rod", ItemClassification.filler, 732420, ItemType.Weapon, False),
ItemData(57, "Witch's Wand", ItemClassification.filler, 732464, ItemType.Weapon, False),
ItemData(58, "Blessed Ankh", ItemClassification.filler, 732508, ItemType.Weapon, False),
ItemData(59, "Psynergy Rod", ItemClassification.filler, 732552, ItemType.Weapon, False),
ItemData(60, "Frost Wand", ItemClassification.filler, 732596, ItemType.Weapon, False),
ItemData(61, "Angelic Ankh", ItemClassification.filler, 732640, ItemType.Weapon, False),
ItemData(62, "Demonic Staff", ItemClassification.filler, 732684, ItemType.Weapon, False),
ItemData(63, "Crystal Rod", ItemClassification.filler, 732728, ItemType.Weapon, False),
ItemData(75, "Leather Armor", ItemClassification.filler, 733256, ItemType.Armor, False),
ItemData(76, "Psynergy Armor", ItemClassification.filler, 733300, ItemType.Armor, False),
ItemData(77, "Chain Mail", ItemClassification.filler, 733344, ItemType.Armor, False),
ItemData(78, "Armored Shell", ItemClassification.filler, 733388, ItemType.Armor, False),
ItemData(79, "Plate Mail", ItemClassification.filler, 733432, ItemType.Armor, False),
ItemData(80, "Steel Armor", ItemClassification.filler, 733476, ItemType.Armor, False),
ItemData(89, "Cotton Shirt", ItemClassification.filler, 733872, ItemType.Armor, False),
ItemData(90, "Travel Vest", ItemClassification.filler, 733916, ItemType.Armor, False),
ItemData(92, "Adept's Clothes", ItemClassification.filler, 734004, ItemType.Armor, False),
ItemData(94, "Silver Vest", ItemClassification.filler, 734092, ItemType.Armor, False),
ItemData(103, "OnePiece Dress", ItemClassification.filler, 734488, ItemType.Armor, False),
ItemData(104, "Travel Robe", ItemClassification.filler, 734532, ItemType.Armor, False),
ItemData(105, "Silk Robe", ItemClassification.filler, 734576, ItemType.Armor, False),
ItemData(107, "Jerkin", ItemClassification.filler, 734664, ItemType.Armor, False),
ItemData(109, "Blessed Robe", ItemClassification.filler, 734752, ItemType.Armor, False),
ItemData(110, "Magical Cassock", ItemClassification.filler, 734796, ItemType.Armor, False),
ItemData(111, "Mysterious Robe", ItemClassification.filler, 734840, ItemType.Armor, False),
ItemData(118, "Wooden Shield", ItemClassification.filler, 735148, ItemType.Shield, False),
ItemData(119, "Bronze Shield", ItemClassification.filler, 735192, ItemType.Shield, False),
ItemData(120, "Iron Shield", ItemClassification.filler, 735236, ItemType.Shield, False),
ItemData(121, "Knight's Shield", ItemClassification.filler, 735280, ItemType.Shield, False),
ItemData(122, "Mirrored Shield", ItemClassification.filler, 735324, ItemType.Shield, False),
ItemData(127, "Padded Gloves", ItemClassification.filler, 735544, ItemType.Shield, False),
ItemData(128, "Leather Gloves", ItemClassification.filler, 735588, ItemType.Shield, False),
ItemData(129, "Gauntlets", ItemClassification.filler, 735632, ItemType.Shield, False),
ItemData(131, "War Gloves", ItemClassification.filler, 735720, ItemType.Shield, False),
ItemData(136, "Leather Armlet", ItemClassification.filler, 735940, ItemType.Shield, False),
ItemData(137, "Armlet", ItemClassification.filler, 735984, ItemType.Shield, False),
ItemData(138, "Heavy Armlet", ItemClassification.filler, 736028, ItemType.Shield, False),
ItemData(139, "Silver Armlet", ItemClassification.filler, 736072, ItemType.Shield, False),
ItemData(140, "Spirit Armlet", ItemClassification.filler, 736116, ItemType.Shield, False),
ItemData(145, "Open Helm", ItemClassification.filler, 736336, ItemType.Helm, False),
ItemData(146, "Bronze Helm", ItemClassification.filler, 736380, ItemType.Helm, False),
ItemData(147, "Iron Helm", ItemClassification.filler, 736424, ItemType.Helm, False),
ItemData(148, "Steel Helm", ItemClassification.filler, 736468, ItemType.Helm, False),
ItemData(149, "Silver Helm", ItemClassification.filler, 736512, ItemType.Helm, False),
ItemData(150, "Knight's Helm", ItemClassification.filler, 736556, ItemType.Helm, False),
ItemData(156, "Leather Cap", ItemClassification.filler, 736820, ItemType.Helm, False),
ItemData(157, "Wooden Cap", ItemClassification.filler, 736864, ItemType.Helm, False),
ItemData(158, "Mail Cap", ItemClassification.filler, 736908, ItemType.Helm, False),
ItemData(159, "Jeweled Crown", ItemClassification.filler, 736952, ItemType.Helm, False),
ItemData(166, "Circlet", ItemClassification.filler, 737260, ItemType.Helm, False),
ItemData(167, "Silver Circlet", ItemClassification.filler, 737304, ItemType.Helm, False),
ItemData(168, "Guardian Circlet", ItemClassification.filler, 737348, ItemType.Helm, False),
ItemData(169, "Platinum Circlet", ItemClassification.filler, 737392, ItemType.Helm, False),
ItemData(402, "Leather Boots", ItemClassification.filler, 747644, ItemType.Boots, False),
ItemData(404, "Safety Boots", ItemClassification.filler, 747732, ItemType.Boots, False),

]

forge_only: List[ItemData] = [
ItemData(272, "Huge Sword", ItemClassification.filler, 741924, ItemType.Weapon, False),
ItemData(273, "Mythril Blade", ItemClassification.filler, 741968, ItemType.Weapon, False),
ItemData(274, "Levatine", ItemClassification.filler, 742012, ItemType.Weapon, False),
ItemData(275, "Darksword", ItemClassification.filler, 742056, ItemType.Weapon, False),
ItemData(276, "Excalibur", ItemClassification.filler, 742100, ItemType.Weapon, False),
ItemData(277, "Robber's Blade", ItemClassification.filler, 742144, ItemType.Weapon, False),
ItemData(278, "Soul Brand", ItemClassification.filler, 742188, ItemType.Weapon, False),
ItemData(285, "Sylph Rapier", ItemClassification.filler, 742496, ItemType.Weapon, False),
ItemData(286, "Burning Sword", ItemClassification.filler, 742540, ItemType.Weapon, False),
ItemData(288, "Corsair's Edge", ItemClassification.filler, 742628, ItemType.Weapon, False),
ItemData(289, "Pirate's Sabre", ItemClassification.filler, 742672, ItemType.Weapon, False),
ItemData(295, "Apollo's Axe", ItemClassification.filler, 742936, ItemType.Weapon, False),
ItemData(296, "Gaia's Axe", ItemClassification.filler, 742980, ItemType.Weapon, False),
ItemData(297, "Stellar Axe", ItemClassification.filler, 743024, ItemType.Weapon, False),
ItemData(298, "Captain's Axe", ItemClassification.filler, 743068, ItemType.Weapon, False),
ItemData(299, "Viking Axe", ItemClassification.filler, 743112, ItemType.Weapon, False),
ItemData(305, "Comet Mace", ItemClassification.filler, 743376, ItemType.Weapon, False),
ItemData(306, "Tungsten Mace", ItemClassification.filler, 743420, ItemType.Weapon, False),
ItemData(307, "Demon Mace", ItemClassification.filler, 743464, ItemType.Weapon, False),
ItemData(308, "Hagbone Mace", ItemClassification.filler, 743508, ItemType.Weapon, False),
ItemData(313, "Cloud Wand", ItemClassification.filler, 743728, ItemType.Weapon, False),
ItemData(314, "Salamander Rod", ItemClassification.filler, 743772, ItemType.Weapon, False),
ItemData(315, "Nebula Wand", ItemClassification.filler, 743816, ItemType.Weapon, False),
ItemData(316, "Dracomace", ItemClassification.filler, 743860, ItemType.Weapon, False),
ItemData(317, "Glower Staff", ItemClassification.filler, 743904, ItemType.Weapon, False),
ItemData(318, "Goblin's Rod", ItemClassification.filler, 743948, ItemType.Weapon, False),
ItemData(328, "Planet Armor", ItemClassification.filler, 744388, ItemType.Armor, False),
ItemData(329, "Dragon Mail", ItemClassification.filler, 744432, ItemType.Armor, False),
ItemData(330, "Chronos Mail", ItemClassification.filler, 744476, ItemType.Armor, False),
ItemData(331, "Stealth Armor", ItemClassification.filler, 744520, ItemType.Armor, False),
ItemData(332, "Xylion Armor", ItemClassification.filler, 744564, ItemType.Armor, False),
ItemData(338, "Faery Vest", ItemClassification.filler, 744828, ItemType.Armor, False),
ItemData(339, "Mythril Clothes", ItemClassification.filler, 744872, ItemType.Armor, False),
ItemData(347, "Dragon Robe", ItemClassification.filler, 745224, ItemType.Armor, False),
ItemData(348, "Ardagh Robe", ItemClassification.filler, 745268, ItemType.Armor, False),
ItemData(353, "Luna Shield", ItemClassification.filler, 745488, ItemType.Shield, False),
ItemData(354, "Dragon Shield", ItemClassification.filler, 745532, ItemType.Shield, False),
ItemData(355, "Flame Shield", ItemClassification.filler, 745576, ItemType.Shield, False),
ItemData(356, "Terra Shield", ItemClassification.filler, 745620, ItemType.Shield, False),
ItemData(357, "Cosmos Shield", ItemClassification.filler, 745664, ItemType.Shield, False),
ItemData(361, "Aerial Gloves", ItemClassification.filler, 745840, ItemType.Shield, False),
ItemData(362, "Titan Gloves", ItemClassification.filler, 745884, ItemType.Shield, False),
ItemData(363, "Big Bang Gloves", ItemClassification.filler, 745928, ItemType.Shield, False),
ItemData(368, "Clear Bracelet", ItemClassification.filler, 746148, ItemType.Shield, False),
ItemData(369, "Mythril Armlet", ItemClassification.filler, 746192, ItemType.Shield, False),
ItemData(374, "Dragon Helm", ItemClassification.filler, 746412, ItemType.Helm, False),
ItemData(375, "Mythril Helm", ItemClassification.filler, 746456, ItemType.Helm, False),
ItemData(376, "Fear Helm", ItemClassification.filler, 746500, ItemType.Helm, False),
ItemData(377, "Millenium Helm", ItemClassification.filler, 746544, ItemType.Helm, False),
ItemData(382, "Floating Hat", ItemClassification.filler, 746764, ItemType.Helm, False),
ItemData(390, "Pure Circlet", ItemClassification.filler, 747116, ItemType.Helm, False),
ItemData(391, "Astral Circlet", ItemClassification.filler, 747160, ItemType.Helm, False),
ItemData(392, "Psychic Circlet", ItemClassification.filler, 747204, ItemType.Helm, False),
ItemData(393, "Demon Circlet", ItemClassification.filler, 747248, ItemType.Helm, False),
ItemData(403, "Dragon Boots", ItemClassification.filler, 747688, ItemType.Boots, False),
ItemData(409, "Spirit Ring", ItemClassification.filler, 747952, ItemType.Ring, False),
ItemData(410, "Stardust Ring", ItemClassification.filler, 747996, ItemType.Ring, False),

]

lucky_only: List[ItemData] = [
ItemData(280, "Hestia Blade", ItemClassification.filler, 742276, ItemType.Weapon, False),
ItemData(302, "Mighty Axe", ItemClassification.filler, 743244, ItemType.Weapon, False),
ItemData(320, "Fireman's Pole", ItemClassification.filler, 744036, ItemType.Weapon, False),
ItemData(335, "Erebus Armor", ItemClassification.filler, 744696, ItemType.Armor, False),
ItemData(341, "Wild Coat", ItemClassification.filler, 744960, ItemType.Armor, False),
ItemData(342, "Floral Dress", ItemClassification.filler, 745004, ItemType.Armor, False),
ItemData(359, "Aegis Shield", ItemClassification.filler, 745752, ItemType.Shield, False),
ItemData(364, "Crafted Gloves", ItemClassification.filler, 745972, ItemType.Shield, False),
ItemData(380, "Minerva Helm", ItemClassification.filler, 746676, ItemType.Helm, False),
ItemData(387, "Crown of Glory", ItemClassification.filler, 746984, ItemType.Helm, False),
ItemData(395, "Brilliant Circlet", ItemClassification.filler, 747336, ItemType.Helm, False),

]

non_vanilla: List[ItemData] = [
ItemData(8, "Arctic Blade", ItemClassification.filler, 730308, ItemType.Weapon, False),
ItemData(9, "Gaia Blade", ItemClassification.filler, 730352, ItemType.Weapon, False),
ItemData(11, "Muramasa", ItemClassification.filler, 730440, ItemType.Weapon, False),
ItemData(15, "Machete", ItemClassification.filler, 730616, ItemType.Weapon, False),
ItemData(22, "Elven Rapier", ItemClassification.filler, 730924, ItemType.Weapon, False),
ItemData(23, "Assassin Blade", ItemClassification.filler, 730968, ItemType.Weapon, False),
ItemData(24, "Mystery Blade", ItemClassification.filler, 731012, ItemType.Weapon, False),
ItemData(25, "Kikuichimonji", ItemClassification.filler, 731056, ItemType.Weapon, False),
ItemData(27, "Bandit's Sword", ItemClassification.filler, 731144, ItemType.Weapon, False),
ItemData(35, "Giant Axe", ItemClassification.filler, 731496, ItemType.Weapon, False),
ItemData(36, "Vulcan Axe", ItemClassification.filler, 731540, ItemType.Weapon, False),
ItemData(37, "Burning Axe", ItemClassification.filler, 731584, ItemType.Weapon, False),
ItemData(38, "Demon Axe", ItemClassification.filler, 731628, ItemType.Weapon, False),
ItemData(48, "Grievous Mace", ItemClassification.filler, 732068, ItemType.Weapon, False),
ItemData(49, "Blessed Mace", ItemClassification.filler, 732112, ItemType.Weapon, False),
ItemData(50, "Wicked Mace", ItemClassification.filler, 732156, ItemType.Weapon, False),
ItemData(64, "Zodiac Wand", ItemClassification.filler, 732772, ItemType.Weapon, False),
ItemData(81, "Spirit Armor", ItemClassification.filler, 733520, ItemType.Armor, False),
ItemData(82, "Dragon Scales", ItemClassification.filler, 733564, ItemType.Armor, False),
ItemData(83, "Demon Mail", ItemClassification.filler, 733608, ItemType.Armor, False),
ItemData(84, "Asura's Armor", ItemClassification.filler, 733652, ItemType.Armor, False),
ItemData(85, "Spiked Armor", ItemClassification.filler, 733696, ItemType.Armor, False),
ItemData(91, "Fur Coat", ItemClassification.filler, 733960, ItemType.Armor, False),
ItemData(93, "Elven Shirt", ItemClassification.filler, 734048, ItemType.Armor, False),
ItemData(95, "Water Jacket", ItemClassification.filler, 734136, ItemType.Armor, False),
ItemData(96, "Storm Gear", ItemClassification.filler, 734180, ItemType.Armor, False),
ItemData(97, "Kimono", ItemClassification.filler, 734224, ItemType.Armor, False),
ItemData(98, "Ninja Garb", ItemClassification.filler, 734268, ItemType.Armor, False),
ItemData(106, "China Dress", ItemClassification.filler, 734620, ItemType.Armor, False),
ItemData(108, "Cocktail Dress", ItemClassification.filler, 734708, ItemType.Armor, False),
ItemData(112, "Feathered Robe", ItemClassification.filler, 734884, ItemType.Armor, False),
ItemData(113, "Oracle's Robe", ItemClassification.filler, 734928, ItemType.Armor, False),
ItemData(123, "Dragon Shield GS", ItemClassification.filler, 735368, ItemType.Shield, False),
ItemData(124, "Earth Shield", ItemClassification.filler, 735412, ItemType.Shield, False),
ItemData(130, "Vambrace", ItemClassification.filler, 735676, ItemType.Shield, False),
ItemData(132, "Spirit Gloves GS", ItemClassification.filler, 735764, ItemType.Shield, False),
ItemData(133, "Battle Gloves", ItemClassification.filler, 735808, ItemType.Shield, False),
ItemData(134, "Aura Gloves", ItemClassification.filler, 735852, ItemType.Shield, False),
ItemData(141, "Virtuous Armlet", ItemClassification.filler, 736160, ItemType.Shield, False),
ItemData(142, "Guardian Armlet", ItemClassification.filler, 736204, ItemType.Shield, False),
ItemData(151, "Warrior's Helm", ItemClassification.filler, 736600, ItemType.Helm, False),
ItemData(152, "Adept's Helm", ItemClassification.filler, 736644, ItemType.Helm, False),
ItemData(160, "Ninja Hood", ItemClassification.filler, 736996, ItemType.Helm, False),
ItemData(161, "Lucky Cap", ItemClassification.filler, 737040, ItemType.Helm, False),
ItemData(162, "Thunder Crown", ItemClassification.filler, 737084, ItemType.Helm, False),
ItemData(163, "Prophet's Hat", ItemClassification.filler, 737128, ItemType.Helm, False),
ItemData(164, "Lure Cap", ItemClassification.filler, 737172, ItemType.Helm, False),
ItemData(170, "Mythril Circlet", ItemClassification.filler, 737436, ItemType.Helm, False),
ItemData(171, "Glittering Tiara", ItemClassification.filler, 737480, ItemType.Helm, False),
ItemData(250, "Mythril Shirt", ItemClassification.filler, 740956, ItemType.Shirt, False),
ItemData(251, "Silk Shirt", ItemClassification.filler, 741000, ItemType.Shirt, False),
ItemData(252, "Running Shirt", ItemClassification.filler, 741044, ItemType.Shirt, False),
ItemData(256, "Hyper Boots", ItemClassification.filler, 741220, ItemType.Boots, False),
ItemData(257, "Quick Boots", ItemClassification.filler, 741264, ItemType.Boots, False),
ItemData(258, "Fur Boots", ItemClassification.filler, 741308, ItemType.Boots, False),
ItemData(262, "Adept Ring", ItemClassification.filler, 741484, ItemType.Ring, False),
ItemData(263, "War Ring", ItemClassification.filler, 741528, ItemType.Ring, False),
ItemData(264, "Sleep Ring", ItemClassification.filler, 741572, ItemType.Ring, False),
ItemData(265, "Healing Ring", ItemClassification.filler, 741616, ItemType.Ring, False),
ItemData(267, "Fairy Ring", ItemClassification.filler, 741704, ItemType.Ring, False),
ItemData(268, "Cleric's Ring", ItemClassification.filler, 741748, ItemType.Ring, False),
ItemData(282, "Rune Blade", ItemClassification.filler, 742364, ItemType.Weapon, False),
ItemData(293, "Tisiphone Edge", ItemClassification.filler, 742848, ItemType.Weapon, False),
ItemData(303, "Tartarus Axe", ItemClassification.filler, 743288, ItemType.Weapon, False),
ItemData(310, "Rising Mace", ItemClassification.filler, 743596, ItemType.Weapon, False),
ItemData(321, "Atropos' Rod", ItemClassification.filler, 744080, ItemType.Weapon, False),
ItemData(322, "Lachesis' Rule", ItemClassification.filler, 744124, ItemType.Weapon, False),
ItemData(323, "Clotho's Distaff", ItemClassification.filler, 744168, ItemType.Weapon, False),
ItemData(324, "Staff of Anubis", ItemClassification.filler, 744212, ItemType.Weapon, False),
ItemData(345, "Triton's Ward", ItemClassification.filler, 745136, ItemType.Armor, False),
ItemData(350, "Aeolian Cassock", ItemClassification.filler, 745356, ItemType.Armor, False),
ItemData(365, "Riot Gloves", ItemClassification.filler, 746016, ItemType.Shield, False),
ItemData(372, "Leda's Bracelet", ItemClassification.filler, 746324, ItemType.Shield, False),
ItemData(379, "Gloria Helm", ItemClassification.filler, 746632, ItemType.Helm, False),
ItemData(385, "Otafuku Mask", ItemClassification.filler, 746896, ItemType.Helm, False),
ItemData(386, "Hiotoko Mask", ItemClassification.filler, 746940, ItemType.Helm, False),
ItemData(396, "Berserker Band", ItemClassification.filler, 747380, ItemType.Helm, False),
ItemData(398, "Divine Camisole", ItemClassification.filler, 747468, ItemType.Shirt, False),
ItemData(399, "Herbed Shirt", ItemClassification.filler, 747512, ItemType.Shirt, False),
ItemData(400, "Golden Shirt", ItemClassification.filler, 747556, ItemType.Shirt, False),
ItemData(401, "Casual Shirt", ItemClassification.filler, 747600, ItemType.Shirt, False),
ItemData(405, "Knight's Greave", ItemClassification.filler, 747776, ItemType.Boots, False),
ItemData(406, "Silver Greave", ItemClassification.filler, 747820, ItemType.Boots, False),
ItemData(407, "Ninja Sandals", ItemClassification.filler, 747864, ItemType.Boots, False),
ItemData(408, "Golden Boots", ItemClassification.filler, 747908, ItemType.Boots, False),
ItemData(411, "Aroma Ring", ItemClassification.filler, 748040, ItemType.Ring, False),
ItemData(412, "Rainbow Ring", ItemClassification.filler, 748084, ItemType.Ring, False),
ItemData(413, "Soul Ring", ItemClassification.filler, 748128, ItemType.Ring, False),
ItemData(415, "Golden Ring", ItemClassification.filler, 748216, ItemType.Ring, False),

]

vanilla_coins: List[ItemData] = [
ItemData(32771, "Coins 3", ItemClassification.filler, 991840, ItemType.Consumable, False),
ItemData(32780, "Coins 12", ItemClassification.filler, 993540, ItemType.Consumable, False),
ItemData(32783, "Coins 15", ItemClassification.filler, 991976, ItemType.Consumable, False),
ItemData(33083, "Coins 315", ItemClassification.filler, 992128, ItemType.Consumable, False),
ItemData(32800, "Coins 32", ItemClassification.filler, 993192, ItemType.Consumable, False),
ItemData(32891, "Coins 123", ItemClassification.filler, 992324, ItemType.Consumable, False),
ItemData(33545, "Coins 777", ItemClassification.filler, 992360, ItemType.Consumable, False),
ItemData(32850, "Coins 82", ItemClassification.filler, 992388, ItemType.Consumable, False),
ItemData(33434, "Coins 666", ItemClassification.filler, 992644, ItemType.Consumable, False),
ItemData(32786, "Coins 18", ItemClassification.filler, 992712, ItemType.Consumable, False),
ItemData(32784, "Coins 16", ItemClassification.filler, 993048, ItemType.Consumable, False),
ItemData(32950, "Coins 182", ItemClassification.filler, 993180, ItemType.Consumable, False),
ItemData(32978, "Coins 210", ItemClassification.filler, 993632, ItemType.Consumable, False),
ItemData(33133, "Coins 365", ItemClassification.filler, 993788, ItemType.Consumable, False),
ItemData(32934, "Coins 166", ItemClassification.filler, 993960, ItemType.Consumable, False),
ItemData(32929, "Coins 161", ItemClassification.filler, 994108, ItemType.Consumable, False),
ItemData(33679, "Coins 911", ItemClassification.filler, 994208, ItemType.Consumable, False),
ItemData(33074, "Coins 306", ItemClassification.filler, 994412, ItemType.Consumable, False),
ItemData(33151, "Coins 383", ItemClassification.filler, 994460, ItemType.Consumable, False),

]

misc: List[ItemData] = [
    ItemData(0, "Empty", ItemClassification.filler, 729956, ItemType.Consumable, False),
    ItemData(231, "Bone", ItemClassification.filler, 740120, ItemType.Consumable, False),
    ItemData(449, "Laughing Fungus", ItemClassification.filler, 749712, ItemType.Consumable, False),
    
]

remainder: List[ItemData] = [
    ItemData(180, "Herb", ItemClassification.filler, 737876, ItemType.Consumable, False),
    ItemData(181, "Nut", ItemClassification.filler, 737920, ItemType.Consumable, False),
    ItemData(182, "Vial", ItemClassification.filler, 737964, ItemType.Consumable, False),
    ItemData(187, "Antidote", ItemClassification.filler, 738184, ItemType.Consumable, False),
    ItemData(188, "Elixir", ItemClassification.filler, 738228, ItemType.Consumable, False),
    ItemData(226, "Smoke Bomb", ItemClassification.filler, 739900, ItemType.Consumable, False),
    ItemData(227, "Sleep Bomb", ItemClassification.filler, 739944, ItemType.Consumable, False),
    ItemData(229, "Lucky Medal", ItemClassification.progression_skip_balancing, 740032, ItemType.Consumable, False),
    ItemData(233, "Corn", ItemClassification.filler, 740208, ItemType.Consumable, False),
    ItemData(236, "Sacred Feather", ItemClassification.filler, 740340, ItemType.Consumable, False),
    ItemData(238, "Oil Drop", ItemClassification.filler, 740428, ItemType.Consumable, False),
    ItemData(239, "Weasel's Claw", ItemClassification.filler, 740472, ItemType.Consumable, False),
    ItemData(240, "Bramble Seed", ItemClassification.filler, 740516, ItemType.Consumable, False),
    ItemData(241, "Crystal Powder", ItemClassification.filler, 740560, ItemType.Consumable, False),
    
]



all_items: List[ItemData] = djinn_items + psyenergy_as_item_list + psyenergy_list + summon_list + events + characters + mimics + other_progression + other_useful + shop_only + forge_only + lucky_only + non_vanilla + vanilla_coins + misc + remainder 
assert len(all_items) == len({x.id for x in all_items})
item_table: Dict[str, ItemData] = {item.name: item for item in all_items}
items_by_id: Dict[int, ItemData] = {item.id: item for item in all_items}