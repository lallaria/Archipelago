from typing import Any, Dict
from Options import StartInventoryPool
from .Options import (ItemShuffle, MajorMinorSplit, RevealHiddenItem, OmitLocations, AddGs1Items, AddDummyItems,
                      StartWithShip, ShipWings, AnemosAccess, CharacterShuffle, SecondStartingCharacter,
                      CharStatShuffle, CharEleShuffle, NoLearningUtilPsy, RandomizeClassStatBoosts,
                      ClassPsynergy, ClassPsynergyLevels, AdjustPsyPower, AdjustPsyCost, RandomizePsyAoe,
                      AdjustEnemyPsyPower, RandomizeEnemyPsyAoe, EnemyEResShuffle, StartWithHealPsynergy,
                      StartWithRevivePsynergy, StartWithRevealPsynergy, DjinnShuffle, DjinnLogic,
                      ShuffleDjinnStats, AdjustDjinnPower, RandomizeDjinnAoe, ScaleDjinnBattleDifficulty,
                      RandomizeSummonCosts, AdjustSummonPower, RandomizeEqCompatibility, AdjustEqPrices,
                      AdjustEqStats, ShuffleAttack, ShuffleWpnEffects, ShuffleDefense, ShuffleArmEffect,
                      RandomizeEqCurses, RemoveCurses, VisibleItems, FreeAvoid, FreeRetreat, ScaleExpGained,
                      ScaleCoinsGained, StartingLevels, SanctuaryReviveCost, AvoidPatch, EnableHardMode,
                      HalveEncounterRate, EasierBosses, NamedPuzzles, ManualRetreatGlitch, MusicShuffle,
                      TelportEverywhere, TrapChance, MimicTrapWeight, ForgeMaterialsFillerWeight,
                      RustyMaterialsFillerWeight, StatBoostFillerWeight, UncommonConsumableFillerWeight,
                      ForgedEquipmentFillerWeight, LuckyFountainEquipmentFillerWeight, ShopEquipmentFillerWeight,
                      CoinsFillerWeight, CommonConsumablesFillerWeight)

easy = {
    ItemShuffle.internal_name: ItemShuffle.option_all_chests_and_tablets,
    MajorMinorSplit.internal_name: MajorMinorSplit.option_false,
    RevealHiddenItem.internal_name: RevealHiddenItem.option_true,
    OmitLocations.internal_name: OmitLocations.option_omit_superbosses_and_inner_sanctum,
    AddGs1Items.internal_name: AddGs1Items.option_false,
    AddDummyItems.internal_name: AddDummyItems.option_false,
    StartWithShip.internal_name: StartWithShip.option_ship_door_unlocked,
    ShipWings.internal_name: ShipWings.option_false,
    AnemosAccess.internal_name: AnemosAccess.option_vanilla,
    CharacterShuffle.internal_name: CharacterShuffle.option_vanilla,
    SecondStartingCharacter.internal_name: SecondStartingCharacter.option_jenna,
    CharStatShuffle.internal_name: CharStatShuffle.option_vanilla,
    CharEleShuffle.internal_name: CharEleShuffle.option_vanilla,
    NoLearningUtilPsy.internal_name: NoLearningUtilPsy.option_true,
    RandomizeClassStatBoosts.internal_name: RandomizeClassStatBoosts.option_false,
    ClassPsynergy.internal_name: ClassPsynergy.option_vanilla,
    ClassPsynergyLevels.internal_name: ClassPsynergyLevels.option_vanilla,
    AdjustPsyPower.internal_name: AdjustPsyPower.option_false,
    AdjustPsyCost.internal_name: AdjustPsyCost.option_false,
    RandomizePsyAoe.internal_name: RandomizePsyAoe.option_false,
    AdjustEnemyPsyPower.internal_name: AdjustEnemyPsyPower.option_false,
    RandomizeEnemyPsyAoe.internal_name: RandomizeEnemyPsyAoe.option_false,
    EnemyEResShuffle.internal_name: EnemyEResShuffle.option_vanilla,
    StartWithHealPsynergy.internal_name: StartWithHealPsynergy.option_true,
    StartWithRevivePsynergy.internal_name: StartWithRevivePsynergy.option_true,
    StartWithRevealPsynergy.internal_name: StartWithRevealPsynergy.option_false,
    DjinnShuffle.internal_name: DjinnShuffle.option_vanilla_shuffled,
    DjinnLogic.internal_name: 100,
    ShuffleDjinnStats.internal_name: ShuffleDjinnStats.option_false,
    AdjustDjinnPower.internal_name: AdjustDjinnPower.option_false,
    RandomizeDjinnAoe.internal_name: RandomizeDjinnAoe.option_false,
    ScaleDjinnBattleDifficulty.internal_name: ScaleDjinnBattleDifficulty.option_true,
    RandomizeSummonCosts.internal_name: RandomizeSummonCosts.option_false,
    AdjustSummonPower.internal_name: AdjustSummonPower.option_false,
    RandomizeEqCompatibility.internal_name: RandomizeEqCompatibility.option_false,
    AdjustEqPrices.internal_name: AdjustEqPrices.option_false,
    AdjustEqStats.internal_name: AdjustEqStats.option_false,
    ShuffleAttack.internal_name: ShuffleAttack.option_false,
    ShuffleWpnEffects.internal_name: ShuffleWpnEffects.option_false,
    ShuffleDefense.internal_name: ShuffleDefense.option_false,
    ShuffleArmEffect.internal_name: ShuffleArmEffect.option_false,
    RandomizeEqCurses.internal_name: RandomizeEqCurses.option_false,
    RemoveCurses.internal_name: RemoveCurses.option_true,
    VisibleItems.internal_name: VisibleItems.option_true,
    FreeAvoid.internal_name: FreeAvoid.option_true,
    FreeRetreat.internal_name: FreeRetreat.option_true,
    ScaleExpGained.internal_name: 3,
    ScaleCoinsGained.internal_name: 4,
    StartingLevels.internal_name: 5,
    SanctuaryReviveCost.internal_name: SanctuaryReviveCost.option_reduced,
    AvoidPatch.internal_name: AvoidPatch.option_true,
    EnableHardMode.internal_name: EnableHardMode.option_false,
    HalveEncounterRate.internal_name: HalveEncounterRate.option_false,
    EasierBosses.internal_name: EasierBosses.option_true,
    NamedPuzzles.internal_name: NamedPuzzles.option_vanilla,
    ManualRetreatGlitch.internal_name: ManualRetreatGlitch.option_false,
    MusicShuffle.internal_name: MusicShuffle.option_false,
    TelportEverywhere.internal_name: TelportEverywhere.option_true
}

open_mode= {
    ItemShuffle.internal_name: ItemShuffle.option_all_chests_and_tablets,
    MajorMinorSplit.internal_name: MajorMinorSplit.option_false,
    RevealHiddenItem.internal_name: RevealHiddenItem.option_true,
    OmitLocations.internal_name: OmitLocations.option_omit_anemos_inner_sanctum,
    AddGs1Items.internal_name: AddGs1Items.option_true,
    AddDummyItems.internal_name: AddDummyItems.option_true,
    StartWithShip.internal_name: StartWithShip.option_available_from_start,
    ShipWings.internal_name: ShipWings.option_false,
    AnemosAccess.internal_name: AnemosAccess.option_vanilla,
    CharacterShuffle.internal_name: CharacterShuffle.option_vanilla,
    SecondStartingCharacter.internal_name: SecondStartingCharacter.option_jenna,
    CharStatShuffle.internal_name: CharStatShuffle.option_adjust_character_stats,
    CharEleShuffle.internal_name: CharEleShuffle.option_shuffle_character_elements,
    NoLearningUtilPsy.internal_name: NoLearningUtilPsy.option_true,
    RandomizeClassStatBoosts.internal_name: RandomizeClassStatBoosts.option_true,
    ClassPsynergy.internal_name: ClassPsynergy.option_randomize_by_psynergy_group,
    ClassPsynergyLevels.internal_name: ClassPsynergyLevels.option_adjust_learning_levels,
    AdjustPsyPower.internal_name: AdjustPsyPower.option_false,
    AdjustPsyCost.internal_name: AdjustPsyCost.option_false,
    RandomizePsyAoe.internal_name: RandomizePsyAoe.option_false,
    AdjustEnemyPsyPower.internal_name: AdjustEnemyPsyPower.option_false,
    RandomizeEnemyPsyAoe.internal_name: RandomizeEnemyPsyAoe.option_false,
    EnemyEResShuffle.internal_name: EnemyEResShuffle.option_vanilla,
    StartWithHealPsynergy.internal_name: StartWithHealPsynergy.option_false,
    StartWithRevivePsynergy.internal_name: StartWithRevivePsynergy.option_false,
    StartWithRevealPsynergy.internal_name: StartWithRevealPsynergy.option_false,
    DjinnShuffle.internal_name: DjinnShuffle.option_vanilla_shuffled,
    DjinnLogic.internal_name: 100,
    ShuffleDjinnStats.internal_name: ShuffleDjinnStats.option_true,
    AdjustDjinnPower.internal_name: AdjustDjinnPower.option_false,
    RandomizeDjinnAoe.internal_name: RandomizeDjinnAoe.option_false,
    ScaleDjinnBattleDifficulty.internal_name: ScaleDjinnBattleDifficulty.option_true,
    RandomizeSummonCosts.internal_name: RandomizeSummonCosts.option_false,
    AdjustSummonPower.internal_name: AdjustSummonPower.option_false,
    RandomizeEqCompatibility.internal_name: RandomizeEqCompatibility.option_true,
    AdjustEqPrices.internal_name: AdjustEqPrices.option_false,
    AdjustEqStats.internal_name: AdjustEqStats.option_true,
    ShuffleAttack.internal_name: ShuffleAttack.option_false,
    ShuffleWpnEffects.internal_name: ShuffleWpnEffects.option_true,
    ShuffleDefense.internal_name: ShuffleDefense.option_false,
    ShuffleArmEffect.internal_name: ShuffleArmEffect.option_true,
    RandomizeEqCurses.internal_name: RandomizeEqCurses.option_false,
    RemoveCurses.internal_name: RemoveCurses.option_false,
    VisibleItems.internal_name: VisibleItems.option_true,
    FreeAvoid.internal_name: FreeAvoid.option_true,
    FreeRetreat.internal_name: FreeRetreat.option_true,
    ScaleExpGained.internal_name: 3,
    ScaleCoinsGained.internal_name: 4,
    StartingLevels.internal_name: 18,
    SanctuaryReviveCost.internal_name: SanctuaryReviveCost.option_vanilla,
    AvoidPatch.internal_name: AvoidPatch.option_true,
    EnableHardMode.internal_name: EnableHardMode.option_false,
    HalveEncounterRate.internal_name: HalveEncounterRate.option_false,
    EasierBosses.internal_name: EasierBosses.option_false,
    NamedPuzzles.internal_name: NamedPuzzles.option_vanilla,
    ManualRetreatGlitch.internal_name: ManualRetreatGlitch.option_false,
    MusicShuffle.internal_name: MusicShuffle.option_false,
    TelportEverywhere.internal_name: TelportEverywhere.option_true
}

gstla_options_presets: Dict[str, Dict[str, Any]] = {
    "Easy": easy,
    "Open Mode": open_mode
}