#Blank options file; not ready for customization yet
from dataclasses import dataclass
from Options import Choice, Toggle, PerGameCommonOptions, StartInventoryPool, NamedRange, Range

class StartingWorlds(Range):
    """
    Number of random worlds to start with
    Defaults to 1 if value is set to 0 and Play Destiny Islands is disabled
    """
    display_name = "Starting Worlds"
    default = 1
    range_start = 0
    range_end = 10

class Character(Choice):
    """
    Determines whether to play as Sora, Riku, or Both
    """
    display_name = "Character"
    default = 0
    option_both = 0
    option_sora = 1
    option_riku = 2

class Goal(Choice):
    """
    Win Condition
    final_boss: Defeat the Final Boss (Xemnas for Sora and Young Xehanort for Riku
    superbosses: Defeat All Superbosses (Secret Portals and Julius)
    lucky_emblem_hunt: Instantly goal when obtaining all required lucky emblems
    """
    display_name = "Goal"
    default = 0
    option_final_boss = 0
    option_superbosses = 1
    option_lucky_emblem_hunt = 2

class AVN(Toggle):
    """
    If enabled, the win condition for the Final Boss goal is moved to AVN instead of Young Xehanort
    This is ignored if the goal is Superbosses or the player chooses Sora as their character
    """
    display_name = "Armored Ventus Nightmare"

class EmblemsRequired(Range):
    """
    How many Lucky Emblems are needed to beat the seed.
    This setting applies to all goals.
    """
    display_name = "Lucky Emblems Required"
    default = 0
    range_start = 0
    range_end = 99

class EmblemsInPool(Range):
    """
    Number of Lucky Emblems in the Item Pool
    """
    display_name = "Lucky Emblems in Pool"
    default = 0
    range_start = 0
    range_end = 99

class RecipeReqs(Range):
    """
    Number of Recipes needed to beat the game
    Meow Wow and Komory Bat recipes are always required
    This setting is ignored if goal is Lucky Emblem Hunt
    """
    display_name = "Recipes Required"
    default = 2
    range_start = 2
    range_end = 54

class RecipesInPool(Range):
    """
    Number of Recipes in the Item Pool
    Always includes Meow Wow and Komory Bat recipes
    """
    display_name = "Recipes in the Item Pool"
    default = 54
    range_start = 2
    range_end = 54

class Superbosses(Toggle):
    """
    Determines whether Secret Portals and Julius  are checks
    This option is ignored if the Goal is Superbosses
    """

class LordKyroo(Toggle):
    display_name = "Lord Kyroo"
    """
    Determines whether fighting Lord Kyroo is needed for checks.
    Each unique location he can be fought grants a check, as well
    as granting an additional check for defeating him.
    """
    default = True

class LevelCap(Range):
    """
    Determines how many level locations can contain non-filler items.
    Set to 1 to make all levels contain filler items.
    IF SETTING ABOVE 50, IT IS RECOMMENDED TO USE A HIGH EXP MULTIPLIER
    """
    display_name = "Level Cap"
    default = 50
    range_start = 1
    range_end = 99

class StatsOnLevels(Choice):
    """
    Determines what items level locations can have.
    Any Item: Any item can be placed in level locations.
    No Progression: Any non-progression item can be placed into level locations.
    Stats Only: Only stats will be placed in level locations (up to Level Cap).
    Vanilla Stats: Level locations are excluded and are treated as vanilla.
                   Stat increases are also removed from the item pool.
    """
    display_name = "Level Up Rewards"
    default = 0
    option_any_item = 0
    option_no_progression = 1
    option_stats_only = 2
    option_vanilla_stats = 3

#####################################
#########Quality of Life#############
#####################################
class ExpMultiplier(Range):
    """
    Determines the multiplier to apply to EXP gained
    """
    display_name = "Exp Multiplier"
    default = 2
    range_start = 1
    range_end = 10

class StartWithSuperJump(Toggle):
    """
    If enabled, adds Super Jump to starting items.
    Super Jump requires other flowmotion to use.
    """
    display_name = "Start with Super Jump"
    default = True

class StatBonusAmount(Range):
    """
    Determines how many points each stat increase grants.
    Only applies to Strength, Defense, and Magic increases.
    """
    display_name = "Stat Bonus Amount"
    default = 2
    range_start = 1
    range_end = 5

class StrengthInPool(Range):
    """
    Determines how many strength increases per character are in the item pool.
    Does nothing if Stats On Levels is enabled.
    """
    display_name = "Strength in Pool"
    default = 18
    range_start = 0
    range_end = 50

class MagicInPool(Range):
    """
    Determines how many magic increases per character are in the item pool.
    Does nothing if Stats On Levels is enabled.
    """
    display_name = "Magic in Pool"
    default = 18
    range_start = 0
    range_end = 50

class DefenseInPool(Range):
    """
    Determines how many defense increases per character are in the item pool.
    Does nothing if Stats On Levels is enabled.
    """
    display_name = "Defense in Pool"
    default = 15
    range_start = 0
    range_end = 50

class PlayDestinyIslands(Toggle):
    """
    Allows you to play the Ursula battle at the start of the run.
    This grants 5 additional checks.
    Does nothing if the player chooses Riku as their character.

    NOTE: Need to connect to the server before starting a new game
          in order for this to take effect.
    """
    display_name = "Play Ursula Battle"

class SkipLightCycle(Toggle):
    """
    Allows you to skip the Light Cycle section of Riku's Grid.
    Skipping will still grant the check for clearing the Light Cycle minigame.
    Does nothing if the player chooses Sora as their character.
    """
    display_name = "Skip Light Cycle"
    default = True

class FastGoMode(Toggle):
    """
    When enabled, the save point for Young Xehanort is
    activated after collecting the necessary key items,
    allowing you to do the final fight instantly without
    having to play the entirety of The World That Never Was.

    Does nothing if the goal is Superbosses or the player
    chooses Sora as their character.
    """
    display_name = "Fast Go Mode"

#####################################
##########Extra Features#############
#####################################
class RandomizeKeybladeStats(Toggle):
    """
    Determines if Keyblade stats should be randomized
    """
    display_name = "Randomize Keyblade Stats"

class KeybladeMinStrength(Range):
    """
    Determines the minimum Strength bonus a keyblade can have
    """
    display_name = "Keyblade Minimum Strength"
    default = 2
    range_start = 0
    range_end = 10

class KeybladeMaxStrength(Range):
    """
    Determines the maximum Strength bonus a keyblade can have
    """
    display_name = "Keyblade Maximum Strength"
    default = 18
    range_start = 11
    range_end = 18

class KeybladeMinMagic(Range):
    """
    Determines the minimum Magic bonus a keyblade can have
    """
    display_name = "Keyblade Minimum Magic"
    default = 2
    range_start = 0
    range_end = 10

class KeybladeMaxMagic(Range):
    """
    Determines the maximum Magic bonus a keyblade can have
    """
    display_name = "Keyblade Maximum Magic"
    default = 16
    range_start = 11
    range_end = 18

class InstantDropTrapChance(Range):
    """
    Determines the % chance a filler item gets replaced by an instant drop trap.
    """
    display_name = "Instant Drop Trap Chance"
    default = 0
    range_start = 0
    range_end = 25

class SingleFlowmotion(Toggle):
    """
    If enabled, all flowmotion is obtained as a single item
    """
    display_name = "Flowmotion is One Item"

class ReceivedItemNotifications(Choice):
    """
    Determine how received item notifications are handled
    0: Display a notification for every received item
    1: Display a notification for received progressive items only
    2: Do not display received item notifications
    """
    display_name = "Local Item Notifications"
    default = 0
    option_display_received_all = 0
    option_display_received_progressive = 1
    option_display_received_none = 2

class SentItemNotifications(Choice):
    """
    Determine how sent item notifications are handled
    0: Display a notification for every sent item
    1: Display a notification for sent progressive items only
    2: Do not display sent item notifications
    """
    display_name = "Sent Item Notifications"
    default = 0
    option_display_sent_all = 0
    option_display_sent_progressive = 1
    option_display_sent_none = 2

@dataclass
class KHDDDOptions(PerGameCommonOptions):
    character: Character
    goal: Goal
    armored_ventus_nightmare: AVN
    emblem_reqs: EmblemsRequired
    emblems_in_pool: EmblemsInPool
    recipe_reqs: RecipeReqs
    recipes_in_pool: RecipesInPool
    starting_worlds: StartingWorlds
    superbosses: Superbosses
    lord_kyroo: LordKyroo
    play_destiny_islands: PlayDestinyIslands
    skip_light_cycle: SkipLightCycle
    fast_go_mode: FastGoMode
    exp_multiplier: ExpMultiplier
    super_jump_start: StartWithSuperJump
    level_cap: LevelCap
    stats_on_levels: StatsOnLevels
    stat_bonus: StatBonusAmount
    strength_in_pool: StrengthInPool
    magic_in_pool: MagicInPool
    defense_in_pool: DefenseInPool
    randomize_keyblade_stats: RandomizeKeybladeStats
    keyblade_min_str: KeybladeMinStrength
    keyblade_max_str: KeybladeMaxStrength
    keyblade_min_mag: KeybladeMinMagic
    keyblade_max_mag: KeybladeMaxMagic
    instant_drop_trap_chance: InstantDropTrapChance
    single_flowmotion: SingleFlowmotion
    received_notifications: ReceivedItemNotifications
    sent_notifications: SentItemNotifications

    start_inventory_from_pool: StartInventoryPool