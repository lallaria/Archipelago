from dataclasses import dataclass
from Options import Toggle, DefaultOnToggle, DeathLink, Choice, Range, PerGameCommonOptions, StartInventoryPool, OptionGroup


class GiygasRequired(DefaultOnToggle):
    """If enabled, your goal will be to defeat Giygas at the Cave of the Past.
       If disabled, your goal will either complete automatically upon completing
       enough Sanctuaries, or completing Magicant if it is required."""
    display_name = "Giygas Required"


class SanctuariesRequired(Range):
    """How many of the eight "Your Sanctuary" locations are required to be cleared."""
    display_name = "Required Sanctuaries"
    range_start = 1
    range_end = 8
    default = 4


class SanctuaryAltGoal(Toggle):
    """If enabled, you will be able to win by completing 2 more Sanctuaries than are required.
       Does nothing if 7 or more Sanctuaries are required, or if Magicant and Giygas are not required."""
    display_name = "Sanctuary Alternate Goal"


class MagicantMode(Choice):
    """PSI Location: You will be able to find a Magicant teleport item. Ness's Nightmare contains a PSI location, and no stat boost.
       Required: You will unlock the Magicant Teleport upon reaching your Sanctuary goal. If Giygas is required, beating Ness's Nightmare will unlock the Cave of the Past and grant a party-wide stat boost. Otherwise, Ness's Nightmare will finish your game.
       Alternate Goal: You will unlock the Magicant Teleport upon reaching one more Sanctuary than required. Beating Ness's Nightmare will finish your game. Does nothing if Giygas is not required, or if 8 Sanctuaries are required. Magicant locations are removed from the multiworld, but contain random junk for yourself.
       Optional Boost: You will be able to find a Magicant teleport item. Beating Ness's Nightmare will grant a party-wide stat boost. Magicant locations are removed from the multiworld, but contain random junk for yourself.
       Removed: Magicant will be completely inacessible."""
    display_name = "Magicant Mode"
    option_psi_location = 0
    option_required = 1
    option_alternate_goal = 2
    option_optional_boost = 3
    option_removed = 4
    default = 0


class MonkeyCavesMode(Choice):
    """Chests: Items required to finish the Monkey Caves will be forcibly placed on the chests that can be found in-between rooms of the monkey caves. The "reward" locations, usually found at the end of a branch, are still random. If you waste chest items, they will need to be replaced via the methods in hunt mode.
       Hunt: Items required to finish the Monkey Caves will need to be found outside. They can be obtained from the Dusty Dunes drugstore, the Fourside department store, and the pizza shop in either Twoson or Threed.
       Shop: The monkey outside the Monkey Caves will sell you every minor item needed to complete the caves for 500$.
       Solved: The Monkey Caves monkeys will already be moved out of the way and not require any items."""
    display_name = "Monkey Caves Mode"
    option_chests = 0
    option_hunt = 1
    option_shop = 2
    option_solved = 3
    default = 1
    

class ShortenPrayers(DefaultOnToggle):
    """If enabled, the Prayer cutscenes while fighting Giygas will be skipped, excluding the final one."""
    display_name = "Skip Prayer Sequences"


class RandomStartLocation(Toggle):
    """If disabled, you will always start at Ness's house with no teleports unlocked.
       If enabled, you will start at a random teleport destination with one teleport unlocked.
       Additionally, you will need to fight Captain Strong to access the north part of Onett if this is enabled."""
    display_name = "Random Starting Location"


class TeleportShuffle(Choice):
    """Shuffled: Teleports and Starstorm will be shuffled amongst the PSI locations. A few redundant Teleports may not be available.
       Anywhere: Teleports and Starstorm will be placed anywhere in the multiworld, and PSI locations will have regular checks.
       See the Game Page for more information on PSI Locations."""
    display_name = "Teleport Shuffle"
    option_shuffled = 0
    option_anywhere = 1
    default = 0


class CharacterShuffle(Choice):
    """Shuffled: Characters will be shuffled amongst Character Locations. Extra locations will have Flying Man, a Teddy Bear, or a Super Plush Bear.
       Anywhere: Characters can be found anywhere in the multiworld, and character locations will have regular checks.
       See the Game Page for more information on Character Locations."""
    display_name = "Character Shuffle"
    option_shuffled = 0
    option_anywhere = 1
    default = 0


class PSIShuffle(Choice):
    """None: Characters will learn their normal PSI skills.
       Basic: Offensive and Assist PSI will be shuffled. Recovery PSI is not modified. Ness's Favorite Thing will be named Wave in other slots.
       Extended: Basic shuffle, but includes Jeff gadgets and some combat items.
       See the Game Page for more information."""
    display_name = "PSI Shuffle"
    option_none = 0
    option_basic = 1
    option_extended = 2

class BossShuffle(Toggle):
    """Shuffles boss encounters amongst each other."""
    display_name = "Boss Shuffle"

class DecoupleDiamondDog(Toggle):
    """Shuffles Diamond Dog as a boss separate from Carbon Dog. Carbon Dog will transform into a random boss.
       Does nothing if Boss Shuffle is disabled."""
    display_name = "Decouple Diamond Dog"

class ShuffleGiygas(Toggle):
    """Adds the standalone Giygas fight to the shuffled boss pool.
       This only applies to the second phase Giygas. The prayer fight is not affected.
       Does nothing if Boss Shuffle is disabled."""
    display_name = "Add Giygas to Boss Pool"


class BanFlashFavorite(Toggle):
    """If enabled, allows PSI Flash to be shuffled onto the Favorite Thing PSI slot. Can be quite annoying early-game. 
       Does nothing if PSI Shuffle is set to None."""
    display_name = "Flash as Favorite"


class PreFixItems(Toggle):
    """If enabled, broken items in the multiworld pool will be replaced with their fixed versions.
       This does not affect any items that are not placed by the multiworld."""
    display_name = "Prefixed Items"


class AutoscaleParty(Toggle):
    """If enabled, joining party members will be scaled to roughly the level of the sphere they were obtained in."""
    display_name = "Autoscale Party Members"

class ProgressiveWeapons(Toggle):
    """If enabled, Bats, Fry Pans, and Guns will be progressive. Does not apply to items dropped by enemies or found in shops."""
    display_name = "Progressive Weapons"


class ProgressiveArmor(Toggle):
    """If enabled, Bracelets and items for the Other slot besides Ribbons will be progressive. Does not apply to items dropped by enemies or found in shops."""
    display_name = "Progressive Weapons"


class PresentSprites(DefaultOnToggle):
    """If enabled, Presents, Trash cans, and chests will have their appearance modified to be indicative of the item they contain."""
    display_name = "Match Present Sprites"


class ShuffleDrops(Toggle):
    """If enabled, enemies will drop random filler items. This does not put checks on enemy drops.
       Drop rates are unchanged."""
    display_name = "Shuffle Drops"


class RandomFranklinBadge(Toggle):
    """If enabled, the Franklin Badge will reflect a randomly selected attack type. The type can be determined from the item's name, as well as the help
       text for it. The badge's function outside of battle will not change, and neither will its name outside of the game itself."""
    display_name = "Franklin Badge Protection"


class CommonWeight(Range):
    """Weight for placing a common filler item."""
    display_name = "Common Filler Weight"
    range_start = 1
    range_end = 100
    default = 80


class UncommonWeight(Range):
    """Weight for placing an uncommon filler item."""
    display_name = "Uncommon Filler Weight"
    range_start = 1
    range_end = 100
    default = 30


class RareWeight(Range):
    """Weight for placing a rare filler item."""
    display_name = "Rare Filler Weight"
    range_start = 0
    range_end = 100
    default = 5


class ExperienceModifier(Range):
    """Percentage of EXP enemies give you. 100 is vanilla, after scaling, and 300 is x3."""
    display_name = "Experience Percentage"
    range_start = 100
    range_end = 300
    default = 150


class StartingMoney(Range):
    """How much money you start with."""
    display_name = "Starting Money"
    range_start = 0
    range_end = 99999
    default = 20


class EasyDeaths(DefaultOnToggle):
    """Fully revives and heals all party members after death. If off, only Ness will be healed with 0 PP."""
    display_name = "Easy Deaths"


class RandomFlavors(DefaultOnToggle):
    """Randomizes the non-plain window color options."""
    display_name = "Random Flavors"


class DeathLinkMode(Choice):
    """Controls how receiving a Deathlink functions in battle.
       Instant: The player will be instantly defeated.
       Mortal: All characters will receieve mortal damage. The player will not be able to heal until the battle is finished.
       Mortal Mercy: All characters will receieve mortal damage, but the player will be able to heal it before they die.
       Regardless of this setting, receiving a deathlink outside of battle will always instantly defeat the player."""
    display_name = "Death Link Mode"
    option_instant = 0
    option_mortal = 1
    option_mortal_mercy = 2
    default = 1

class RandomBattleBG(Toggle):
    """Generates random battle backgrounds."""
    display_name = "Randomize Battle Backgrounds"

class RandomSwirlColors(Toggle):
    """Generates random colors for pre-battle swirls."""
    display_name = "Randomize Swirl Colors"

class RemoteItems(Toggle):
    """If enabled, you will receive your own items from the server upon collecting them, rather than locally.
       This allows co-op within the same game, and protects against loss of save data.
       However, you will not be able to play offline if this is enabled."""
    display_name = "Remote Items"

class SoundStoneShuffle(Toggle):
    """Randomizes the Sound Stone. It will need to be found before Sanctuary guardians can be challenged."""
    display_name = "Sound Stone Shuffle"


@dataclass
class EBOptions(PerGameCommonOptions):
    giygas_required: GiygasRequired
    sanctuaries_required: SanctuariesRequired
    skip_prayer_sequences: ShortenPrayers
    random_start_location: RandomStartLocation
    alternate_sanctuary_goal: SanctuaryAltGoal
    magicant_mode: MagicantMode
    monkey_caves_mode: MonkeyCavesMode
    shuffle_teleports: TeleportShuffle# Better name?
    character_shuffle: CharacterShuffle
    psi_shuffle: PSIShuffle
    allow_flash_as_favorite_thing: BanFlashFavorite
    boss_shuffle: BossShuffle
    decouple_diamond_dog: DecoupleDiamondDog
    boss_shuffle_add_giygas: ShuffleGiygas
    #shuffle_sound_stone: SoundStoneShuffle
    experience_modifier: ExperienceModifier
    starting_money: StartingMoney
    easy_deaths: EasyDeaths
    progressive_weapons: ProgressiveWeapons
    progressive_armor: ProgressiveArmor
    auto_scale_party_members: AutoscaleParty
    remote_items: RemoteItems
    random_flavors: RandomFlavors
    random_battle_backgrounds: RandomBattleBG
    random_swirl_colors: RandomSwirlColors
    presents_match_contents: PresentSprites
    prefixed_items: PreFixItems
    #excluded_teleports: ExcludedTeleports
    randomize_franklinbadge_protection: RandomFranklinBadge
    shuffle_enemy_drops: ShuffleDrops
    common_filler_weight: CommonWeight
    uncommon_filler_weight: UncommonWeight
    rare_filler_weight: RareWeight
    start_inventory_from_pool: StartInventoryPool
    death_link: DeathLink
    death_link_mode: DeathLinkMode


eb_option_groups = [
    OptionGroup("Goal Settings", [
        GiygasRequired,
        SanctuariesRequired,
        SanctuaryAltGoal
    ]),
    
    OptionGroup("Item Settings", [
        TeleportShuffle,
        CharacterShuffle,
        ProgressiveWeapons,
        ProgressiveArmor,
        RandomFranklinBadge,
        CommonWeight,
        UncommonWeight,
        RareWeight,
        PreFixItems
    ]),

    OptionGroup("World Modes", [
        RandomStartLocation,
        MagicantMode,
        MonkeyCavesMode
    ]),

    OptionGroup("PSI Randomization", [
        PSIShuffle,
        BanFlashFavorite
    ]),

    OptionGroup("Enemy Randomization", [
        BossShuffle,
        DecoupleDiamondDog,
        ShuffleGiygas,
        ExperienceModifier,
        ShuffleDrops
    ]),

    OptionGroup("Convenience Settings", [
        ShortenPrayers,
        EasyDeaths,
        StartingMoney,
        RemoteItems,
        AutoscaleParty
    ]),

    OptionGroup("Aesthetic Settings", [
        RandomSwirlColors,
        RandomBattleBG,
        PresentSprites,
        RandomFlavors
    ]),

    OptionGroup("Deathlink", [
        DeathLink,
        DeathLinkMode
    ])
]
