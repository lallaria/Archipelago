from BaseClasses import Location


class OriBlindForestLocation(Location):
    game: str = "Ori and the Blind Forest"


location_list = [
    "FirstPickup",
    "FirstEnergyCell",
    "FronkeyFight",
    "GladesKeystone1",
    "GladesKeystone2",
    "GladesGrenadePool",
    "GladesGrenadeTree",
    "GladesMainPool",
    "GladesMainPoolDeep",
    "FronkeyWalkRoof",
    "FourthHealthCell",
    "GladesMapKeystone",
    "WallJumpSkillTree",
    "LeftGladesHiddenExp",
    "DeathGauntletExp",
    "DeathGauntletEnergyCell",
    "GladesMap",
    "AboveFourthHealth",
    "WallJumpAreaExp",
    "WallJumpAreaEnergyCell",
    "LeftGladesExp",
    "LeftGladesKeystone",
    "LeftGladesMapstone",
    "SpiritCavernsKeystone1",
    "SpiritCavernsKeystone2",
    "SpiritCavernsTopRightKeystone",
    "SpiritCavernsTopLeftKeystone",
    "SpiritCavernsAbilityCell",
    "GladesLaser",
    "GladesLaserGrenade",
    "SpiritTreeExp",
    "ChargeFlameSkillTree",
    "ChargeFlameAreaPlant",
    "ChargeFlameAreaExp",
    "AboveChargeFlameTreeExp",
    "SpiderSacEnergyDoor",
    "SpiderSacHealthCell",
    "SpiderSacEnergyCell",
    "SpiderSacGrenadeDoor",
    "DashAreaOrbRoomExp",
    "DashAreaAbilityCell",
    "DashAreaRoofExp",
    "DashSkillTree",
    "DashAreaPlant",
    "RazielNo",
    "DashAreaMapstone",
    "BlackrootTeleporterHealthCell",
    "BlackrootMap",
    "BlackrootBoulderExp",
    "GrenadeSkillTree",
    "GrenadeAreaExp",
    "GrenadeAreaAbilityCell",
    "LowerBlackrootAbilityCell",
    "LowerBlackrootLaserAbilityCell",
    "LowerBlackrootLaserExp",
    "LowerBlackrootGrenadeThrow",
    "LostGroveAbilityCell",
    "LostGroveHiddenExp",
    "LostGroveTeleporter",
    "LostGroveLongSwim",
    "HollowGroveMapstone",
    "OuterSwampAbilityCell",
    "OuterSwampStompExp",
    "OuterSwampHealthCell",
    "HollowGroveMap",
    "HollowGroveTreeAbilityCell",
    "HollowGroveMapPlant",
    "HollowGroveTreePlant",
    "SwampEntrancePlant",
    "MoonGrottoStompPlant",
    "OuterSwampMortarPlant",
    "GroveWaterStompAbilityCell",
    "OuterSwampGrenadeExp",
    "SwampTeleporterAbilityCell",
    "GroveAboveSpiderWaterExp",
    "GroveAboveSpiderWaterHealthCell",
    "GroveAboveSpiderWaterEnergyCell",
    "GroveSpiderWaterSwim",
    "DeathGauntletSwimEnergyDoor",
    "DeathGauntletStompSwim",
    "AboveGrottoTeleporterExp",
    "GrottoLasersRoofExp",
    "IcelessExp",
    "BelowGrottoTeleporterPlant",
    "LeftGrottoTeleporterExp",
    "OuterSwampMortarAbilityCell",
    "SwampEntranceSwim",
    "BelowGrottoTeleporterHealthCell",
    "GrottoEnergyDoorSwim",
    "GrottoEnergyDoorHealthCell",
    "GrottoSwampDrainAccessExp",
    "GrottoSwampDrainAccessPlant",
    "GrottoHideoutFallAbilityCell",
    "GumoHideoutMapstone",
    "GumoHideoutMiniboss",
    "GumoHideoutCrusherExp",
    "GumoHideoutCrusherKeystone",
    "GumoHideoutRightHangingExp",
    "GumoHideoutLeftHangingExp",
    "GumoHideoutRedirectAbilityCell",
    "GumoHideoutMap",
    "DoubleJumpSkillTree",
    "DoubleJumpAreaExp",
    "GumoHideoutEnergyCell",
    "GumoHideoutRockfallExp",
    "WaterVein",
    "LeftGumoHideoutExp",
    "LeftGumoHideoutHealthCell",
    "LeftGumoHideoutLowerPlant",
    "LeftGumoHideoutUpperPlant",
    "GumoHideoutRedirectPlant",
    "LeftGumoHideoutSwim",
    "GumoHideoutRedirectEnergyCell",
    "GumoHideoutRedirectExp",
    "FarLeftGumoHideoutExp",
    "SwampEntranceAbilityCell",
    "DeathGauntletRoofHealthCell",
    "DeathGauntletRoofPlant",
    "LowerGinsoHiddenExp",
    "LowerGinsoKeystone1",
    "LowerGinsoKeystone2",
    "LowerGinsoKeystone3",
    "LowerGinsoKeystone4",
    "LowerGinsoPlant",
    "BashSkillTree",
    "BashAreaExp",
    "UpperGinsoLowerKeystone",
    "UpperGinsoRightKeystone",
    "UpperGinsoUpperRightKeystone",
    "UpperGinsoUpperLeftKeystone",
    "UpperGinsoRedirectLowerExp",
    "UpperGinsoRedirectUpperExp",
    "UpperGinsoEnergyCell",
    "TopGinsoLeftLowerExp",
    "TopGinsoLeftUpperExp",
    "TopGinsoRightPlant",
    "GinsoEscapeSpiderExp",
    "GinsoEscapeJumpPadExp",
    "GinsoEscapeProjectileExp",
    "GinsoEscapeHangingExp",
    "GinsoEscapeExit",
    "SwampMap",
    "InnerSwampDrainExp",
    "InnerSwampHiddenSwimExp",
    "InnerSwampSwimLeftKeystone",
    "InnerSwampSwimRightKeystone",
    "InnerSwampSwimMapstone",
    "InnerSwampStompExp",
    "InnerSwampEnergyCell",
    "StompSkillTree",
    "StompAreaRoofExp",
    "StompAreaExp",
    "StompAreaGrenadeExp",
    "HoruFieldsHiddenExp",
    "HoruFieldsEnergyCell",
    "HoruFieldsPlant",
    "HoruFieldsAbilityCell",
    "HoruFieldsHealthCell",
    "HoruMap",
    "HoruL4LowerExp",
    "HoruL4ChaseExp",
    "HoruLavaDrainedLeftExp",
    "HoruR1HangingExp",
    "HoruR1Mapstone",
    "HoruR1EnergyCell",
    "HoruR3Plant",
    "HoruR4StompExp",
    "HoruR4LaserExp",
    "HoruR4DrainedExp",
    "HoruLavaDrainedRightExp",
    "DoorWarpExp",
    "HoruTeleporterExp",
    "ValleyEntryAbilityCell",
    "ValleyEntryTreeExp",
    "ValleyEntryTreePlant",
    "ValleyEntryGrenadeLongSwim",
    "ValleyRightFastStomplessCell",
    "ValleyRightExp",
    "ValleyRightBirdStompCell",
    "GlideSkillFeather",
    "KuroPerchExp",
    "ValleyMap",
    "ValleyMainPlant",
    "WilhelmExp",
    "ValleyRightSwimExp",
    "ValleyMainFACS",
    "ValleyForlornApproachGrenade",
    "ValleyThreeBirdAbilityCell",
    "LowerValleyMapstone",
    "LowerValleyExp",
    "OutsideForlornTreeExp",
    "OutsideForlornWaterExp",
    "OutsideForlornCliffExp",
    "ValleyForlornApproachMapstone",
    "ForlornEntranceExp",
    "ForlornHiddenSpiderExp",
    "ForlornKeystone1",
    "ForlornKeystone2",
    "ForlornKeystone3",
    "ForlornKeystone4",
    "ForlornMap",
    "ForlornPlant",
    "RightForlornHealthCell",
    "ForlornEscape",
    "RightForlornPlant",
    "SorrowEntranceAbilityCell",
    "SorrowMainShaftKeystone",
    "SorrowSpikeKeystone",
    "SorrowHiddenKeystone",
    "SorrowLowerLeftKeystone",
    "SorrowMap",
    "SorrowMapstone",
    "SorrowHealthCell",
    "LeftSorrowAbilityCell",
    "LeftSorrowKeystone1",
    "LeftSorrowKeystone2",
    "LeftSorrowKeystone3",
    "LeftSorrowKeystone4",
    "LeftSorrowEnergyCell",
    "LeftSorrowPlant",
    "LeftSorrowGrenade",
    "UpperSorrowRightKeystone",
    "UpperSorrowFarRightKeystone",
    "UpperSorrowLeftKeystone",
    "UpperSorrowSpikeExp",
    "UpperSorrowFarLeftKeystone",
    "ChargeJumpSkillTree",
    "AboveChargeJumpAbilityCell",
    "Sunstone",
    "SunstonePlant",
    "MistyEntranceStompExp",
    "MistyEntranceTreeExp",
    "MistyFrogNookExp",
    "MistyKeystone1",
    "MistyMortarCorridorUpperExp",
    "MistyMortarCorridorHiddenExp",
    "MistyPlant",
    "ClimbSkillTree",
    "MistyKeystone3",
    "MistyPostClimbSpikeCave",
    "MistyPostClimbAboveSpikePit",
    "MistyKeystone4",
    "MistyGrenade",
    "MistyKeystone2",
    "MistyAbilityCell",
    "GumonSeal"
]

all_trees = [
    "BashSkillTree",
    "ChargeFlameSkillTree",
    "ChargeJumpSkillTree",
    "ClimbSkillTree",
    "DashSkillTree",
    "DoubleJumpSkillTree",
    "GrenadeSkillTree",
    "StompSkillTree",
    "WallJumpSkillTree"
]