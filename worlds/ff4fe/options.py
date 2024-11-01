# options.py
from dataclasses import dataclass

from Options import Toggle, Range, Choice, PerGameCommonOptions, ItemSet, DefaultOnToggle

class ForgeTheCrystal(Toggle):
    """Bring the Adamant and Legend Sword to clear this objective.
    Forces the objective reward to be the Crystal."""
    display_name = "Forge the Crystal"

class ConquerTheGiant(Toggle):
    """Clear the Giant of Bab-il to clear this objective.
    No character will be available from the Giant with this objective."""
    display_name = "Conquer the Giant"

class DefeatTheFiends(Toggle):
    """Defeat every elemental fiend to clear this objective.
    Your targets are Milon, Milon Z., Kainazzo, Valvalis, Rubicant, and the Elements bosses. Good hunting."""
    display_name = "Defeat The Fiends"

class FindTheDarkMatter(Toggle):
    """Find thirty Dark Matters and deliver them to Kory in Agart to clear this objective.
    There are forty-five Dark Matters in total."""
    display_name = "Find The Dark Matter"

class AdditionalObjectives(Range):
    """The number of additional objectives on top of the primary one."""
    display_name = "Additional Objectives"
    range_start = 0
    range_end = 32
    default = 0

class ObjectiveReward(Choice):
    """The reward for clearing all objectives. Note that this is ignored when no objectives are set,
    and Forge the Crystal forces this to the Crystal setting"""
    option_crystal = 0
    option_win = 1
    default = 0

class NoFreeCharacters(Toggle):
    display_name = "No Free Characters"

class NoEarnedCharacters(Toggle):
    display_name = "No Earned Characters"

class HeroChallenge(Choice):
    display_name = "Hero Challenge"
    option_none = 0
    option_cecil = 1
    option_kain = 2
    option_rydia = 3
    option_tellah = 4
    option_edward = 5
    option_rosa = 6
    option_yang = 7
    option_palom = 8
    option_porom = 9
    option_cid = 10
    option_edge = 11
    option_fusoya = 12
    option_random_character = 13
    default = 0

class PassEnabled(Toggle):
    display_name = "Pass In Key Item Pool"

class UsefulPercentage(Range):
    display_name = "Useful Item Percentage"
    range_start = 25
    range_end = 100
    default = 35

class UnsafeKeyItemPlacement(Toggle):
    """Normally, underground access is guaranteed to be available without taking a trip to the moon.
    Toggling this on disables this check."""
    display_name = "Unsafe Key Item Placement"

class PassInShops(Toggle):
    """Can the pass show up in shops? This is a convenience feature and will never be required by the logic."""
    display_name = "Enable Pass in Shops"

class AllowedCharacters(ItemSet):
    """Pool of characters allowed to show up. Note that if Hero Challenge is enabled, your hero will still appear."""
    display_name = "Allowed Characters"
    default = ["Cecil", "Kain", "Rydia", "Tellah", "Edward", "Rosa", "Yang", "Palom", "Porom", "Cid", "Edge", "Fusoya"]

class EnsureAllCharacters(DefaultOnToggle):
    """Ensure at least one instance of each allowed character is available, if possible."""
    display_name = "Ensure All Characters"

class AllowDuplicateCharacters(DefaultOnToggle):
    """Allows multiple instances of the same character to join your party."""
    display_name = "Allow Duplicate Characters"

class RestrictedCharacters(ItemSet):
    """List of characters that can't appear in the easiest to access locations if possible."""
    display_name = "Restricted Characters"
    default = ["Edge", "Fusoya"]

class PartySize(Range):
    """Maximum party size."""
    display_name = "Party Size"
    range_start = 1
    range_end = 5
    default = 5

class CharactersPermajoin(Toggle):
    """If enabled, characters may not be dismissed from the party."""
    display_name = "Characters Permanently Join"

class CharactersPermadie(Choice):
    """If enabled, characters petrified or dead at the end of battle will be removed from your party forever.
    On Extreme difficulty, this also includes "cutscene" fights (Mist, Dark Elf, etc.)"""
    display_name = "Characters Permanently Die"
    option_no = 0
    option_yes = 1
    option_extreme = 2
    default = 0

class MinTier(Range):
    """The minimum tier of items that can appear in the item pool."""
    display_name = "Minimum Treasure Tier"
    range_start = 1
    range_end = 4
    default = 1

class MaxTier(Range):
    """The maximum tier of items that can appear in the item pool."""
    display_name = "Maximum Treasure Tier"
    range_start = 5
    range_end = 8
    default = 8

class JunkTier(Range):
    """Items of this tier or below will automatically be sold for cold hard cash."""
    display_name = "Junk Tier"
    range_start = 0
    range_end = 8
    default = 1

class ShopRandomization(Choice):
    """Affects the placement of items in shops. See FE documentation for more for now."""
    display_name = "Shop Randomization"
    option_vanilla = 0
    option_shuffle = 1
    option_standard = 2
    option_pro = 3
    option_wild = 4
    option_cabins = 5
    default = 4

class FreeShops(Toggle):
    """Everything must go!"""
    display_name = "Free Shops"

class StarterKitOne(Choice):
    """FE Starter Kit 1"""
    display_name = "Starter Kit One"
    option_none = 0
    option_basic = 1
    option_better = 2
    option_loaded = 3
    option_cata = 4
    option_freedom = 5
    option_cid = 6
    option_yang = 7
    option_money = 8
    option_grab_Bag = 9
    option_MIAB = 10
    option_archer = 11
    option_fabul = 12
    option_castlevania = 13
    option_summon = 14
    option_not_Deme = 15
    option_meme = 16
    option_defense = 17
    option_mist = 18
    option_mysidia = 19
    option_baron = 20
    option_dwarf = 21
    option_eblan = 22
    option_libra = 23
    option_99 = 24
    option_green_names = 25
    option_random_kit = 26
    default = 0

class StarterKitTwo(Choice):
    """FE Starter Kit 2"""
    display_name = "Starter Kit Two"
    option_none = 0
    option_basic = 1
    option_better = 2
    option_loaded = 3
    option_cata = 4
    option_freedom = 5
    option_cid = 6
    option_yang = 7
    option_money = 8
    option_grab_Bag = 9
    option_MIAB = 10
    option_archer = 11
    option_fabul = 12
    option_castlevania = 13
    option_summon = 14
    option_not_Deme = 15
    option_meme = 16
    option_defense = 17
    option_mist = 18
    option_mysidia = 19
    option_baron = 20
    option_dwarf = 21
    option_eblan = 22
    option_libra = 23
    option_99 = 24
    option_green_names = 25
    option_random_kit = 26
    default = 0

class StarterKitThree(Choice):
    """FE Starter Kit 3"""
    display_name = "Starter Kit Three"
    option_none = 0
    option_basic = 1
    option_better = 2
    option_loaded = 3
    option_cata = 4
    option_freedom = 5
    option_cid = 6
    option_yang = 7
    option_money = 8
    option_grab_bag = 9
    option_MIAB = 10
    option_archer = 11
    option_fabul = 12
    option_castlevania = 13
    option_summon = 14
    option_not_deme = 15
    option_meme = 16
    option_defense = 17
    option_mist = 18
    option_mysidia = 19
    option_baron = 20
    option_dwarf = 21
    option_eblan = 22
    option_libra = 23
    option_99 = 24
    option_green_names = 25
    option_random_kit = 26
    default = 0

@dataclass
class FF4FEOptions(PerGameCommonOptions):
    ForgeTheCrystal: ForgeTheCrystal
    ConquerTheGiant: ConquerTheGiant
    DefeatTheFiends: DefeatTheFiends
    FindTheDarkMatter: FindTheDarkMatter
    AdditionalObjectives: AdditionalObjectives
    ObjectiveReward: ObjectiveReward
    NoFreeCharacters: NoFreeCharacters
    NoEarnedCharacters: NoEarnedCharacters
    HeroChallenge: HeroChallenge
    PassEnabled: PassEnabled
    UsefulPercentage: UsefulPercentage
    UnsafeKeyItemPlacement: UnsafeKeyItemPlacement
    PassInShops: PassInShops
    AllowedCharacters: AllowedCharacters
    EnsureAllCharacters: EnsureAllCharacters
    AllowDuplicateCharacters: AllowDuplicateCharacters
    RestrictedCharacters: RestrictedCharacters
    PartySize: PartySize
    CharactersPermajoin: CharactersPermajoin
    CharactersPermadie: CharactersPermadie
    MinTier: MinTier
    MaxTier: MaxTier
    JunkTier: JunkTier
    ShopRandomization: ShopRandomization
    FreeShops: FreeShops
    StarterKitOne: StarterKitOne
    StarterKitTwo: StarterKitTwo
    StarterKitThree: StarterKitThree
