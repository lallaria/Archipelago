from dataclasses import dataclass

from schema import Schema, And, Optional

from Options import OptionGroup, Choice, Range, DefaultOnToggle, Toggle, DeathLink, OptionSet, OptionDict
from Options import PerGameCommonOptions
from .Enums import level_areas, pascal_to_space


class GoalRequiresLevels(DefaultOnToggle):
    """If enabled, you have to complete action stages to unlock the last fight."""
    display_name = "Goal Requires Levels"


class LevelPercentage(Range):
    """If Levels are part of the goal, Percentage of the available levels that needed to be completed to unlock the final story."""
    display_name = "Level Requirement Percentage"
    range_start = 25
    range_end = 100
    default = 100


class GoalRequiresChaosEmeralds(Toggle):
    """
    If enabled, you have to collect all the Chaos Emeralds to unlock the last fight.
    Keep in mind selecting emerald hunt will require enough checks to add the 7 emeralds to the pool.
    """
    display_name = "Goal Requires Chaos Emeralds"


class GoalRequiresEmblems(Toggle):
    """
    If enabled, you have to collect a certain number of emblems to unlock the last fight.
    Enabling this will require at least 5 checks to add the 5 emblems to the pool.
    """
    display_name = "Goal Requires Emblems"


class EmblemPercentage(Range):
    """If Emblems are part of the goal, percentage of the available emblems needed to unlock the final story."""
    display_name = "Emblem Requirement Percentage"
    range_start = 1
    range_end = 80
    default = 80


class GoalRequiresMissions(Toggle):
    """If enabled, you have to complete missions to unlock the last fight."""
    display_name = "Goal Requires Missions"


class MissionPercentage(Range):
    """If Missions are part of the goal, Percentage of the available missions that needed to be completed to unlock the final story."""
    display_name = "Mission Requirement Percentage"
    range_start = 25
    range_end = 100
    default = 100


class GoalRequiresBosses(Toggle):
    """If enabled, you have to beat all the bosses to unlock the last fight."""
    display_name = "Goal Requires Bosses"


class GoalRequiresChaoRaces(Toggle):
    """If enabled, you have to beat all the chao races to unlock the last fight."""
    display_name = "Goal Requires Chao Races"


class LogicLevel(Choice):
    """
    Determines the logic the randomizer will use.
    Normal Logic (0): Very forgiving, ideal if you are not used to this game or its location checks.
    Hard Logic (1): Less forgiving logic, some checks require performing spindash jumps or dying to get the check.
    Expert Logic (2): The most unforgiving logic, some checks require performing out-of-bounds jumps.
    """
    display_name = "Logic Level"
    option_normal_logic = 0
    option_hard_logic = 1
    option_expert_logic = 2
    default = 0


class RandomStartingLocation(DefaultOnToggle):
    """Randomize starting location. If false, you will start at Station Square."""
    display_name = "Random Starting Location"


class RandomStartingLocationPerCharacter(DefaultOnToggle):
    """If randomize starting location is enabled, each character will start in a random location."""
    display_name = "Random Starting Location Per Character"


class GuaranteedLevel(Toggle):
    """Ensures access to a level from the start, even if it means giving you an item."""
    display_name = "Guaranteed Level Access"


class GuaranteedStartingChecks(Range):
    """Ensures at least this many checks in your starting location if possible."""
    display_name = "Guaranteed Starting Checks"
    range_start = 1
    range_end = 10
    default = 2


class EntranceRandomizer(Toggle):
    """
    Randomizes the entrances to action stages.
    This means that the entrance to an action stage could be different from the original game.
    If a given entrance is closed (e.g., doors not opening), it indicates that the level behind that entrance is not accessible.
    For example, if Hot Shelter is inside the Emerald Coast entrance, the beach entrance will appear closed for Sonic but open for Amy.
    Depending on the character, the entrance may be Sonic's or Knuckles'. Big, for example, can't use the Speed Highway elevator.
    """
    display_name = "Entrance Randomizer"


class LevelEntrancePlando(OptionDict):
    """
    Plando for level entrance. Only works if Entrance Randomizer is enabled.
    The level name should be Capitalized with no spaces.
    For example, {'Emerald Coast': 'Final Egg'} will place Final Egg behind the Emerald Coast entrance and randomize the rest.
    """
    display_name = "Level Entrance Plando"
    valid_keys = {pascal_to_space(area.name): area.name for area in level_areas}
    schema = Schema(
        {Optional(pascal_to_space(area.name)): And(str, lambda n: n in [pascal_to_space(a.name) for a in level_areas])
         for area in level_areas})


class SendDeathLinkChance(Range):
    """When dying, the chance of sending a death link to another player."""
    display_name = "Send Death Link Chance"
    range_start = 1
    range_end = 100
    default = 100


class ReceiveDeathLinkChance(Range):
    """When receiving a death link, the chance of dying."""
    display_name = "Receive Death Link Chance"
    range_start = 1
    range_end = 100
    default = 100


class RingLink(Toggle):
    """
    Whether your in-level ring gain/loss is linked to other players.
    """
    display_name = "Ring Link"


class CasinopolisRingLink(Toggle):
    """
    Whether Ring Link is enabled while playing Sonic's Casinopolis.
    """
    display_name = "Enable Ring Link while playing Sonic's Casinopolis"


class HardRingLink(Toggle):
    """
    If Ring Link is enabled, sends and receives rings in more situations.
    Particularly, it will subtract rings when finishing a level and during the Perfect Chaos fight.
    """
    display_name = "Hard Ring Link"


class RingLoss(Choice):
    """
    How taking damage is handled.
    Classic (0): You lose all of your rings when hit.
    Modern (1): You lose 20 rings when hit.
    One Hit K.O. (2): You die immediately when hit.
    """
    display_name = "Ring Loss"
    option_classic = 0
    option_modern = 1
    option_one_hit_k_o = 2
    default = 0


class PlayableSonic(DefaultOnToggle):
    """Determines whether Sonic is playable."""
    display_name = "Playable Sonic"


class PlayableTails(DefaultOnToggle):
    """Determines whether Tails is playable."""
    display_name = "Playable Tails"


class PlayableKnuckles(DefaultOnToggle):
    """Determines whether Knuckles is playable."""
    display_name = "Playable Knuckles"


class PlayableAmy(DefaultOnToggle):
    """Determines whether Amy is playable."""
    display_name = "Playable Amy"


class PlayableGamma(DefaultOnToggle):
    """Determines whether Gamma is playable."""
    display_name = "Playable Gamma"


class PlayableBig(DefaultOnToggle):
    """Determines whether Big is playable."""
    display_name = "Playable Big"


class BaseActionStageMissionChoice(Choice):
    """
        For missions, the options range from 3 to 0.
        3 means Missions A, B, and C.
        2 means Missions B and C.
        1 means Mission C.
        0 means no missions at all (You can still play the character if they are enabled).
    """
    option_none = 0
    option_c = 1
    option_c_b = 2
    option_c_b_a = 3
    default = 1


class SonicActionStageMissions(BaseActionStageMissionChoice):
    """Choose what action stage missions will be a location check for Sonic."""
    display_name = "Sonic's Action Stage Missions"


class TailsActionStageMissions(BaseActionStageMissionChoice):
    """Choose what action stage missions will be a location check for Tails."""
    display_name = "Tails' Action Stage Missions"


class KnucklesActionStageMissions(BaseActionStageMissionChoice):
    """Choose what action stage missions will be a location check for Knuckles."""
    display_name = "Knuckles' Action Stage Missions"


class AmyActionStageMissions(BaseActionStageMissionChoice):
    """Choose what action stage missions will be a location check for Amy."""
    display_name = "Amy's Action Stage Missions"


class GammaActionStageMissions(BaseActionStageMissionChoice):
    """Choose what action stage missions will be a location check for Gamma."""
    display_name = "Gamma's Action Stage Missions"


class BigActionStageMissions(BaseActionStageMissionChoice):
    """Choose what action stage missions will be a location check for Big."""
    display_name = "Big's Action Stage Missions"


class RandomizedSonicUpgrades(DefaultOnToggle):
    """Determines whether Sonic's upgrades are randomized and sent to the item pool."""
    display_name = "Randomize Sonic's Upgrades"


class RandomizedTailsUpgrades(DefaultOnToggle):
    """Determines whether Tails' upgrades are randomized and sent to the item pool."""
    display_name = "Randomize Tails' Upgrades"


class RandomizedKnucklesUpgrades(DefaultOnToggle):
    """Determines whether Knuckles' upgrades are randomized and sent to the item pool."""
    display_name = "Randomize Knuckles' Upgrades"


class RandomizedAmyUpgrades(DefaultOnToggle):
    """Determines whether Amy's upgrades are randomized and sent to the item pool."""
    display_name = "Randomize Amy's Upgrades"


class RandomizedBigUpgrades(DefaultOnToggle):
    """Determines whether Big's upgrades are randomized and sent to the item pool."""
    display_name = "Randomize Big's Upgrades"


class RandomizedGammaUpgrades(DefaultOnToggle):
    """Determines whether Gamma's upgrades are randomized and sent to the item pool."""
    display_name = "Randomize Gamma's Upgrades"


class BossChecks(DefaultOnToggle):
    """Determines whether beating a boss grants a check (15 Locations)."""
    display_name = "Boss Checks"


class UnifyChaos4(DefaultOnToggle):
    """Determines whether the Chaos 4 fight counts as a single location or three (Sonic, Tails, and Knuckles)."""
    display_name = "Unify Chaos 4"


class UnifyChaos6(Toggle):
    """Determines whether the Chaos 6 fight counts as a single location or three (Sonic, Big, and Knuckles)."""
    display_name = "Unify Chaos 6"


class UnifyEggHornet(Toggle):
    """Determines whether the Egg Hornet fight counts as a single location or two (Sonic, Tails)."""
    display_name = "Unify Egg Hornet"


class FieldEmblemsChecks(DefaultOnToggle):
    """Determines whether collecting field emblems grants checks (12 Locations)."""
    display_name = "Field Emblems Checks"


class SecretChaoEggs(DefaultOnToggle):
    """Determines whether getting the 3 secret chao eggs grants checks (3 Locations)."""
    display_name = "Secret Chao Egg Checks"


class ChaoRacesChecks(DefaultOnToggle):
    """Determines whether winning the chao races grants checks (5 Locations)."""
    display_name = "Chao Races Checks"


class ChaoRacesLevelsToAccessPercentage(Range):
    """
    Percentage of the available levels accessible for the chao races to be in logic.
    Higher values means races are required later in the game.
    """
    display_name = "Level Access Percentage for Chao Races"
    range_start = 25
    range_end = 100
    default = 100


class MissionChecks(Toggle):
    """Determines whether completing missions grants checks (60 Locations)."""
    display_name = "Enable Mission Checks"


class AutoStartMissions(Toggle):
    """Determines whether missions will start already activated."""
    display_name = "Auto Start Missions"


class MissionBlackList(OptionSet):
    """Determines what missions are blacklisted. The default are:
    Mission 49 (Flags in the Kart section of Twinkle Park).
    Mission 53 (Triple Jump in the Snowboard section of Ice Cap).
    Mission 54 (Flags in the Snowboard section of Ice Cap).
    Mission 58 (Flags in the rolling bounce section of Lost World).
    """
    display_name = "Mission Blacklist"
    default = {'49', '53', '54', '58'}
    valid_keys = [str(i) for i in range(1, 61)]


class SubLevelChecks(DefaultOnToggle):
    """Determines whether beating Twinkle Circuit and Sand Hill grants checks (2 Locations)."""
    display_name = "Sub-Level Checks"


class SubLevelChecksHard(Toggle):
    """
    Determines whether beating the harder (points-based) Twinkle Circuit and Sand Hill missions grants checks (2 Locations).
    Only works if sublevel checks are enabled.
    """
    display_name = "Hard Sub-Level Checks"


class SkyChaseChecks(DefaultOnToggle):
    """Determines whether beating Sky Chase Act 1 and 2 grants checks (2 Locations)."""
    display_name = "Sky Chase Checks"


class SkyChaseChecksHard(Toggle):
    """
    Determines whether beating the harder (points-based) Sky Chase Act 1 and 2 missions grants checks (2 Locations).
    Only works if Sky Chase checks are enabled.
    """
    display_name = "Hard Sky Chase Checks"


class LifeSanity(Toggle):
    """Determines whether collecting life capsules grants checks (102 Locations)."""
    display_name = "Life Sanity"


class PinballLifeCapsules(Toggle):
    """Determines whether pinball's life capsules grant checks (2 Locations)."""
    display_name = "Include Pinball's Life Capsules"


class SonicLifeSanity(DefaultOnToggle):
    """If life-sanity is on, determines whether Sonic's life capsules are part of the randomizer."""
    display_name = "Sonic's Life Sanity"


class TailsLifeSanity(DefaultOnToggle):
    """If life-sanity is on, determines whether Tails' life capsules are part of the randomizer."""
    display_name = "Tails' Life Sanity"


class KnucklesLifeSanity(DefaultOnToggle):
    """If life-sanity is on, determines whether Knuckles' life capsules are part of the randomizer."""
    display_name = "Knuckles' Life Sanity"


class AmyLifeSanity(DefaultOnToggle):
    """If life-sanity is on, determines whether Amy's life capsules are part of the randomizer."""
    display_name = "Amy's Life Sanity"


class BigLifeSanity(DefaultOnToggle):
    """If life-sanity is on, determines whether Big's life capsules are part of the randomizer."""
    display_name = "Big's Life Sanity"


class GammaLifeSanity(DefaultOnToggle):
    """If life-sanity is on, determines whether Gamma's life capsules are part of the randomizer."""
    display_name = "Gamma's Life Sanity"


class JunkFillPercentage(Range):
    """
    Replace a percentage of non-required emblems in the item pool with random junk items.
    """
    display_name = "Junk Fill Percentage"
    range_start = 0
    range_end = 100
    default = 50


class TrapFillPercentage(Range):
    """
    Replace a percentage of junk items in the item pool with random traps.
    """
    display_name = "Trap Fill Percentage"
    range_start = 0
    range_end = 100
    default = 0


class BaseTrapWeight(Choice):
    """
    Base class for trap weights.
    The available options are 0 (off), 1 (low), 2 (medium), and 4 (high).
    """
    option_none = 0
    option_low = 1
    option_medium = 2
    option_high = 4
    default = 2


class IceTrapWeight(BaseTrapWeight):
    """
    Likelihood of receiving a trap that freezes the player in place.
    """
    display_name = "Ice Trap Weight"


class SpringTrapWeight(BaseTrapWeight):
    """
    Likelihood of receiving a trap that spawns a spring that sends the player flying in the opposite direction.
    """
    display_name = "Spring Trap Weight"


class PoliceTrapWeight(BaseTrapWeight):
    """
    Likelihood of receiving a trap that spawns a lot of Cop Speeder enemies.
    """
    display_name = "Police Trap Weight"


class BuyonTrapWeight(BaseTrapWeight):
    """
    Likelihood of receiving a trap that spawns a lot of Buyon enemies.
    """
    display_name = "Buyon Trap Weight"


class ReverseTrapWeight(BaseTrapWeight):
    """
    Likelihood of receiving a trap that reverses your controls.
    """
    display_name = "Reverse Controls Trap Weight"


class GravityTrapWeight(BaseTrapWeight):
    """
    Likelihood of receiving a trap that increments your gravity.
    """
    display_name = "Gravity Trap Weight"


class ReverseControlTrapDuration(Range):
    """
    How many seconds the reverse control trap will last. If set to 0, the trap will last until you die or change level.
    """
    display_name = "Reverse Control Trap Duration"
    range_start = 0
    range_end = 60
    default = 10


class TrapsAndFillerOnAdventureFields(DefaultOnToggle):
    """If enabled, traps and filler can activate in the adventure field."""
    display_name = "Traps and filler on Adventure Fields"


class TrapsAndFillerOnBossFights(DefaultOnToggle):
    """If enabled, traps and filler can activate during boss fights."""
    display_name = "Traps and filler on Boss Fights"


class TrapsAndFillerOnPerfectChaosFight(Toggle):
    """
    If enabled, traps and filler can activate during the Perfect Chaos fight.
    Keep in mind that enemy traps will subtract rings from the player.
    """
    display_name = "Traps and filler on Perfect Chaos Fight"


@dataclass
class SonicAdventureDXOptions(PerGameCommonOptions):
    goal_requires_levels: GoalRequiresLevels
    levels_percentage: LevelPercentage
    goal_requires_chaos_emeralds: GoalRequiresChaosEmeralds
    goal_requires_emblems: GoalRequiresEmblems
    emblems_percentage: EmblemPercentage
    goal_requires_missions: GoalRequiresMissions
    mission_percentage: MissionPercentage
    goal_requires_bosses: GoalRequiresBosses
    goal_requires_chao_races: GoalRequiresChaoRaces

    logic_level: LogicLevel
    random_starting_location: RandomStartingLocation
    random_starting_location_per_character: RandomStartingLocationPerCharacter
    guaranteed_level: GuaranteedLevel
    guaranteed_starting_checks: GuaranteedStartingChecks
    entrance_randomizer: EntranceRandomizer
    level_entrance_plando: LevelEntrancePlando

    death_link: DeathLink
    send_death_link_chance: SendDeathLinkChance
    receive_death_link_chance: ReceiveDeathLinkChance
    ring_link: RingLink
    casinopolis_ring_link: CasinopolisRingLink
    hard_ring_link: HardRingLink
    ring_loss: RingLoss

    playable_sonic: PlayableSonic
    playable_tails: PlayableTails
    playable_knuckles: PlayableKnuckles
    playable_amy: PlayableAmy
    playable_big: PlayableBig
    playable_gamma: PlayableGamma

    sonic_action_stage_missions: SonicActionStageMissions
    tails_action_stage_missions: TailsActionStageMissions
    knuckles_action_stage_missions: KnucklesActionStageMissions
    amy_action_stage_missions: AmyActionStageMissions
    big_action_stage_missions: BigActionStageMissions
    gamma_action_stage_missions: GammaActionStageMissions

    randomized_sonic_upgrades: RandomizedSonicUpgrades
    randomized_tails_upgrades: RandomizedTailsUpgrades
    randomized_knuckles_upgrades: RandomizedKnucklesUpgrades
    randomized_amy_upgrades: RandomizedAmyUpgrades
    randomized_big_upgrades: RandomizedBigUpgrades
    randomized_gamma_upgrades: RandomizedGammaUpgrades

    boss_checks: BossChecks
    unify_chaos4: UnifyChaos4
    unify_chaos6: UnifyChaos6
    unify_egg_hornet: UnifyEggHornet

    field_emblems_checks: FieldEmblemsChecks
    chao_egg_checks: SecretChaoEggs
    chao_races_checks: ChaoRacesChecks
    chao_races_levels_to_access_percentage: ChaoRacesLevelsToAccessPercentage
    mission_mode_checks: MissionChecks
    auto_start_missions: AutoStartMissions
    mission_blacklist: MissionBlackList
    sub_level_checks: SubLevelChecks
    sub_level_checks_hard: SubLevelChecksHard
    sky_chase_checks: SkyChaseChecks
    sky_chase_checks_hard: SkyChaseChecksHard

    life_sanity: LifeSanity
    pinball_life_capsules: PinballLifeCapsules
    sonic_life_sanity: SonicLifeSanity
    tails_life_sanity: TailsLifeSanity
    knuckles_life_sanity: KnucklesLifeSanity
    amy_life_sanity: AmyLifeSanity
    big_life_sanity: BigLifeSanity
    gamma_life_sanity: GammaLifeSanity

    junk_fill_percentage: JunkFillPercentage
    trap_fill_percentage: TrapFillPercentage
    ice_trap_weight: IceTrapWeight
    spring_trap_weight: SpringTrapWeight
    police_trap_weight: PoliceTrapWeight
    buyon_trap_weight: BuyonTrapWeight
    reverse_trap_weight: ReverseTrapWeight
    gravity_trap_weight: GravityTrapWeight

    reverse_trap_duration: ReverseControlTrapDuration
    traps_and_filler_on_adventure_fields: TrapsAndFillerOnAdventureFields
    traps_and_filler_on_boss_fights: TrapsAndFillerOnBossFights
    traps_and_filler_on_perfect_chaos_fight: TrapsAndFillerOnPerfectChaosFight


sadx_option_groups = [
    OptionGroup("General Options", [
        GoalRequiresLevels,
        LevelPercentage,
        GoalRequiresChaosEmeralds,
        GoalRequiresEmblems,
        EmblemPercentage,
        GoalRequiresMissions,
        MissionPercentage,
        GoalRequiresBosses,
        GoalRequiresChaoRaces,
        LogicLevel,
        RandomStartingLocation,
        RandomStartingLocationPerCharacter,
        GuaranteedLevel,
        GuaranteedStartingChecks,
        EntranceRandomizer,
        LevelEntrancePlando,
        SendDeathLinkChance,
        ReceiveDeathLinkChance,
        RingLink,
        CasinopolisRingLink,
        HardRingLink,
        RingLoss,
    ]),
    OptionGroup("Characters Options", [
        PlayableSonic,
        PlayableTails,
        PlayableKnuckles,
        PlayableAmy,
        PlayableBig,
        PlayableGamma,
    ]),
    OptionGroup("Stage Options", [
        SonicActionStageMissions,
        TailsActionStageMissions,
        KnucklesActionStageMissions,
        AmyActionStageMissions,
        BigActionStageMissions,
        GammaActionStageMissions
    ]),
    OptionGroup("Upgrade Options", [
        RandomizedSonicUpgrades,
        RandomizedTailsUpgrades,
        RandomizedKnucklesUpgrades,
        RandomizedAmyUpgrades,
        RandomizedBigUpgrades,
        RandomizedGammaUpgrades,
    ]),
    OptionGroup("Bosses Options", [
        BossChecks,
        UnifyChaos4,
        UnifyChaos6,
        UnifyEggHornet,
    ]),
    OptionGroup("Extra locations", [
        FieldEmblemsChecks,
        SecretChaoEggs,
        ChaoRacesChecks,
        ChaoRacesLevelsToAccessPercentage,
        MissionChecks,
        AutoStartMissions,
        MissionBlackList,
        SubLevelChecks,
        SubLevelChecksHard,
        SkyChaseChecks,
        SkyChaseChecksHard,
        LifeSanity,
        PinballLifeCapsules,
        SonicLifeSanity,
        TailsLifeSanity,
        KnucklesLifeSanity,
        AmyLifeSanity,
        BigLifeSanity,
        GammaLifeSanity,
    ]),
    OptionGroup("Junk Options", [
        JunkFillPercentage,
        TrapFillPercentage,
        IceTrapWeight,
        SpringTrapWeight,
        PoliceTrapWeight,
        BuyonTrapWeight,
        ReverseTrapWeight,
        GravityTrapWeight,
        ReverseControlTrapDuration,
        TrapsAndFillerOnAdventureFields,
        TrapsAndFillerOnBossFights,
        TrapsAndFillerOnPerfectChaosFight
    ]),

]
