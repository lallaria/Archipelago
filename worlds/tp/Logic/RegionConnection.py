from BaseClasses import MultiWorld


def connect_regions(world: MultiWorld, player: int) -> None:
    """Connect all regions according to the world layout"""

    world.get_region("Arbiters Grounds Entrance", player).connect(
        world.get_region("Outside Arbiters Grounds", player),
        f"{"Arbiters Grounds Entrance"} -> {"Outside Arbiters Grounds"}",
    )

    world.get_region("Arbiters Grounds Entrance", player).connect(
        world.get_region("Arbiters Grounds Lobby", player),
        f"{"Arbiters Grounds Entrance"} -> {"Arbiters Grounds Lobby"}",
    )

    world.get_region("Arbiters Grounds Lobby", player).connect(
        world.get_region("Arbiters Grounds Entrance", player),
        f"{"Arbiters Grounds Lobby"} -> {"Arbiters Grounds Entrance"}",
    )

    world.get_region("Arbiters Grounds Lobby", player).connect(
        world.get_region("Arbiters Grounds East Wing", player),
        f"{"Arbiters Grounds Lobby"} -> {"Arbiters Grounds East Wing"}",
    )

    world.get_region("Arbiters Grounds Lobby", player).connect(
        world.get_region("Arbiters Grounds West Wing", player),
        f"{"Arbiters Grounds Lobby"} -> {"Arbiters Grounds West Wing"}",
    )

    world.get_region("Arbiters Grounds Lobby", player).connect(
        world.get_region("Arbiters Grounds After Poe Gate", player),
        f"{"Arbiters Grounds Lobby"} -> {"Arbiters Grounds After Poe Gate"}",
    )

    world.get_region("Arbiters Grounds East Wing", player).connect(
        world.get_region("Arbiters Grounds Lobby", player),
        f"{"Arbiters Grounds East Wing"} -> {"Arbiters Grounds Lobby"}",
    )

    world.get_region("Arbiters Grounds West Wing", player).connect(
        world.get_region("Arbiters Grounds Lobby", player),
        f"{"Arbiters Grounds West Wing"} -> {"Arbiters Grounds Lobby"}",
    )

    world.get_region("Arbiters Grounds After Poe Gate", player).connect(
        world.get_region("Arbiters Grounds Lobby", player),
        f"{"Arbiters Grounds After Poe Gate"} -> {"Arbiters Grounds Lobby"}",
    )

    world.get_region("Arbiters Grounds After Poe Gate", player).connect(
        world.get_region("Arbiters Grounds Boss Room", player),
        f"{"Arbiters Grounds After Poe Gate"} -> {"Arbiters Grounds Boss Room"}",
    )

    world.get_region("Arbiters Grounds Boss Room", player).connect(
        world.get_region("Mirror Chamber Lower", player),
        f"{"Arbiters Grounds Boss Room"} -> {"Mirror Chamber Lower"}",
    )

    world.get_region("City in The Sky Boss Room", player).connect(
        world.get_region("City in The Sky Entrance", player),
        f"{"City in The Sky Boss Room"} -> {"City in The Sky Entrance"}",
    )

    world.get_region(
        "City in The Sky Central Tower Second Floor", player
    ).connect(
        world.get_region("City in The Sky West Wing", player),
        f"{"City in The Sky Central Tower Second Floor"} -> {"City in The Sky West Wing"}",
    )

    world.get_region(
        "City in The Sky Central Tower Second Floor", player
    ).connect(
        world.get_region("City in The Sky Lobby", player),
        f"{"City in The Sky Central Tower Second Floor"} -> {"City in The Sky Lobby"}",
    )

    world.get_region("City in The Sky East Wing", player).connect(
        world.get_region("City in The Sky Lobby", player),
        f"{"City in The Sky East Wing"} -> {"City in The Sky Lobby"}",
    )

    world.get_region("City in The Sky Entrance", player).connect(
        world.get_region("Lake Hylia", player),
        f"{"City in The Sky Entrance"} -> {"Lake Hylia"}",
    )

    world.get_region("City in The Sky Entrance", player).connect(
        world.get_region("City in The Sky Lobby", player),
        f"{"City in The Sky Entrance"} -> {"City in The Sky Lobby"}",
    )

    world.get_region("City in The Sky Lobby", player).connect(
        world.get_region("City in The Sky Entrance", player),
        f"{"City in The Sky Lobby"} -> {"City in The Sky Entrance"}",
    )

    world.get_region("City in The Sky Lobby", player).connect(
        world.get_region("City in The Sky East Wing", player),
        f"{"City in The Sky Lobby"} -> {"City in The Sky East Wing"}",
    )

    world.get_region("City in The Sky Lobby", player).connect(
        world.get_region("City in The Sky West Wing", player),
        f"{"City in The Sky Lobby"} -> {"City in The Sky West Wing"}",
    )

    world.get_region("City in The Sky Lobby", player).connect(
        world.get_region("City in The Sky North Wing", player),
        f"{"City in The Sky Lobby"} -> {"City in The Sky North Wing"}",
    )

    world.get_region("City in The Sky North Wing", player).connect(
        world.get_region("City in The Sky Lobby", player),
        f"{"City in The Sky North Wing"} -> {"City in The Sky Lobby"}",
    )

    world.get_region("City in The Sky North Wing", player).connect(
        world.get_region("City in The Sky Boss Room", player),
        f"{"City in The Sky North Wing"} -> {"City in The Sky Boss Room"}",
    )

    world.get_region("City in The Sky West Wing", player).connect(
        world.get_region("City in The Sky Lobby", player),
        f"{"City in The Sky West Wing"} -> {"City in The Sky Lobby"}",
    )

    world.get_region("City in The Sky West Wing", player).connect(
        world.get_region("City in The Sky Central Tower Second Floor", player),
        f"{"City in The Sky West Wing"} -> {"City in The Sky Central Tower Second Floor"}",
    )

    world.get_region("Forest Temple Boss Room", player).connect(
        world.get_region("South Faron Woods", player),
        f"{"Forest Temple Boss Room"} -> {"South Faron Woods"}",
    )

    world.get_region("Forest Temple East Wing", player).connect(
        world.get_region("Forest Temple Lobby", player),
        f"{"Forest Temple East Wing"} -> {"Forest Temple Lobby"}",
    )

    world.get_region("Forest Temple East Wing", player).connect(
        world.get_region("Forest Temple North Wing", player),
        f"{"Forest Temple East Wing"} -> {"Forest Temple North Wing"}",
    )

    world.get_region("Forest Temple Entrance", player).connect(
        world.get_region("North Faron Woods", player),
        f"{"Forest Temple Entrance"} -> {"North Faron Woods"}",
    )

    world.get_region("Forest Temple Entrance", player).connect(
        world.get_region("Forest Temple Lobby", player),
        f"{"Forest Temple Entrance"} -> {"Forest Temple Lobby"}",
    )

    world.get_region("Forest Temple Lobby", player).connect(
        world.get_region("Forest Temple Entrance", player),
        f"{"Forest Temple Lobby"} -> {"Forest Temple Entrance"}",
    )

    world.get_region("Forest Temple Lobby", player).connect(
        world.get_region("Forest Temple East Wing", player),
        f"{"Forest Temple Lobby"} -> {"Forest Temple East Wing"}",
    )

    world.get_region("Forest Temple Lobby", player).connect(
        world.get_region("Forest Temple West Wing", player),
        f"{"Forest Temple Lobby"} -> {"Forest Temple West Wing"}",
    )

    world.get_region("Forest Temple Lobby", player).connect(
        world.get_region("Ook", player),
        f"{"Forest Temple Lobby"} -> {"Ook"}",
    )

    world.get_region("Forest Temple North Wing", player).connect(
        world.get_region("Forest Temple East Wing", player),
        f"{"Forest Temple North Wing"} -> {"Forest Temple East Wing"}",
    )

    world.get_region("Forest Temple North Wing", player).connect(
        world.get_region("Forest Temple Boss Room", player),
        f"{"Forest Temple North Wing"} -> {"Forest Temple Boss Room"}",
    )

    world.get_region("Forest Temple West Wing", player).connect(
        world.get_region("Forest Temple Lobby", player),
        f"{"Forest Temple West Wing"} -> {"Forest Temple Lobby"}",
    )

    world.get_region("Forest Temple West Wing", player).connect(
        world.get_region("Ook", player),
        f"{"Forest Temple West Wing"} -> {"Ook"}",
    )

    world.get_region("Ook", player).connect(
        world.get_region("Forest Temple West Wing", player),
        f"{"Ook"} -> {"Forest Temple West Wing"}",
    )

    world.get_region("Goron Mines Boss Room", player).connect(
        world.get_region("Lower Kakariko Village", player),
        f"{"Goron Mines Boss Room"} -> {"Lower Kakariko Village"}",
    )

    world.get_region("Goron Mines Crystal Switch Room", player).connect(
        world.get_region("Goron Mines Magnet Room", player),
        f"{"Goron Mines Crystal Switch Room"} -> {"Goron Mines Magnet Room"}",
    )

    world.get_region("Goron Mines Crystal Switch Room", player).connect(
        world.get_region("Goron Mines North Wing", player),
        f"{"Goron Mines Crystal Switch Room"} -> {"Goron Mines North Wing"}",
    )

    world.get_region("Goron Mines Entrance", player).connect(
        world.get_region("Death Mountain Sumo Hall Goron Mines Tunnel", player),
        f"{"Goron Mines Entrance"} -> {"Death Mountain Sumo Hall Goron Mines Tunnel"}",
    )

    world.get_region("Goron Mines Entrance", player).connect(
        world.get_region("Goron Mines Magnet Room", player),
        f"{"Goron Mines Entrance"} -> {"Goron Mines Magnet Room"}",
    )

    world.get_region("Goron Mines Lower West Wing", player).connect(
        world.get_region("Goron Mines Magnet Room", player),
        f"{"Goron Mines Lower West Wing"} -> {"Goron Mines Magnet Room"}",
    )

    world.get_region("Goron Mines Magnet Room", player).connect(
        world.get_region("Goron Mines Entrance", player),
        f"{"Goron Mines Magnet Room"} -> {"Goron Mines Entrance"}",
    )

    world.get_region("Goron Mines Magnet Room", player).connect(
        world.get_region("Goron Mines Lower West Wing", player),
        f"{"Goron Mines Magnet Room"} -> {"Goron Mines Lower West Wing"}",
    )

    world.get_region("Goron Mines Magnet Room", player).connect(
        world.get_region("Goron Mines Crystal Switch Room", player),
        f"{"Goron Mines Magnet Room"} -> {"Goron Mines Crystal Switch Room"}",
    )

    world.get_region("Goron Mines North Wing", player).connect(
        world.get_region("Goron Mines Crystal Switch Room", player),
        f"{"Goron Mines North Wing"} -> {"Goron Mines Crystal Switch Room"}",
    )

    world.get_region("Goron Mines North Wing", player).connect(
        world.get_region("Goron Mines Upper East Wing", player),
        f"{"Goron Mines North Wing"} -> {"Goron Mines Upper East Wing"}",
    )

    world.get_region("Goron Mines North Wing", player).connect(
        world.get_region("Goron Mines Boss Room", player),
        f"{"Goron Mines North Wing"} -> {"Goron Mines Boss Room"}",
    )

    world.get_region("Goron Mines Upper East Wing", player).connect(
        world.get_region("Goron Mines North Wing", player),
        f"{"Goron Mines Upper East Wing"} -> {"Goron Mines North Wing"}",
    )

    world.get_region("Goron Mines Upper East Wing", player).connect(
        world.get_region("Goron Mines Magnet Room", player),
        f"{"Goron Mines Upper East Wing"} -> {"Goron Mines Magnet Room"}",
    )

    world.get_region("Ganondorf Castle", player).connect(
        world.get_region("Hyrule Castle Tower Climb", player),
        f"{"Ganondorf Castle"} -> {"Hyrule Castle Tower Climb"}",
    )

    world.get_region("Hyrule Castle Entrance", player).connect(
        world.get_region("Castle Town North Inside Barrier", player),
        f"{"Hyrule Castle Entrance"} -> {"Castle Town North Inside Barrier"}",
    )

    world.get_region("Hyrule Castle Entrance", player).connect(
        world.get_region("Hyrule Castle Main Hall", player),
        f"{"Hyrule Castle Entrance"} -> {"Hyrule Castle Main Hall"}",
    )

    world.get_region("Hyrule Castle Entrance", player).connect(
        world.get_region("Hyrule Castle Outside West Wing", player),
        f"{"Hyrule Castle Entrance"} -> {"Hyrule Castle Outside West Wing"}",
    )

    world.get_region("Hyrule Castle Entrance", player).connect(
        world.get_region("Hyrule Castle Outside East Wing", player),
        f"{"Hyrule Castle Entrance"} -> {"Hyrule Castle Outside East Wing"}",
    )

    world.get_region("Hyrule Castle Graveyard", player).connect(
        world.get_region("Hyrule Castle Outside East Wing", player),
        f"{"Hyrule Castle Graveyard"} -> {"Hyrule Castle Outside East Wing"}",
    )

    world.get_region("Hyrule Castle Inside East Wing", player).connect(
        world.get_region("Hyrule Castle Main Hall", player),
        f"{"Hyrule Castle Inside East Wing"} -> {"Hyrule Castle Main Hall"}",
    )

    world.get_region("Hyrule Castle Inside East Wing", player).connect(
        world.get_region("Hyrule Castle Third Floor Balcony", player),
        f"{"Hyrule Castle Inside East Wing"} -> {"Hyrule Castle Third Floor Balcony"}",
    )

    world.get_region("Hyrule Castle Inside West Wing", player).connect(
        world.get_region("Hyrule Castle Main Hall", player),
        f"{"Hyrule Castle Inside West Wing"} -> {"Hyrule Castle Main Hall"}",
    )

    world.get_region("Hyrule Castle Inside West Wing", player).connect(
        world.get_region("Hyrule Castle Third Floor Balcony", player),
        f"{"Hyrule Castle Inside West Wing"} -> {"Hyrule Castle Third Floor Balcony"}",
    )

    world.get_region("Hyrule Castle Main Hall", player).connect(
        world.get_region("Hyrule Castle Entrance", player),
        f"{"Hyrule Castle Main Hall"} -> {"Hyrule Castle Entrance"}",
    )

    world.get_region("Hyrule Castle Main Hall", player).connect(
        world.get_region("Hyrule Castle Inside East Wing", player),
        f"{"Hyrule Castle Main Hall"} -> {"Hyrule Castle Inside East Wing"}",
    )

    world.get_region("Hyrule Castle Main Hall", player).connect(
        world.get_region("Hyrule Castle Inside West Wing", player),
        f"{"Hyrule Castle Main Hall"} -> {"Hyrule Castle Inside West Wing"}",
    )

    world.get_region("Hyrule Castle Outside East Wing", player).connect(
        world.get_region("Hyrule Castle Entrance", player),
        f"{"Hyrule Castle Outside East Wing"} -> {"Hyrule Castle Entrance"}",
    )

    world.get_region("Hyrule Castle Outside East Wing", player).connect(
        world.get_region("Hyrule Castle Graveyard", player),
        f"{"Hyrule Castle Outside East Wing"} -> {"Hyrule Castle Graveyard"}",
    )

    world.get_region("Hyrule Castle Outside West Wing", player).connect(
        world.get_region("Hyrule Castle Entrance", player),
        f"{"Hyrule Castle Outside West Wing"} -> {"Hyrule Castle Entrance"}",
    )

    world.get_region("Hyrule Castle Third Floor Balcony", player).connect(
        world.get_region("Hyrule Castle Inside West Wing", player),
        f"{"Hyrule Castle Third Floor Balcony"} -> {"Hyrule Castle Inside West Wing"}",
    )

    world.get_region("Hyrule Castle Third Floor Balcony", player).connect(
        world.get_region("Hyrule Castle Inside East Wing", player),
        f"{"Hyrule Castle Third Floor Balcony"} -> {"Hyrule Castle Inside East Wing"}",
    )

    world.get_region("Hyrule Castle Third Floor Balcony", player).connect(
        world.get_region("Hyrule Castle Tower Climb", player),
        f"{"Hyrule Castle Third Floor Balcony"} -> {"Hyrule Castle Tower Climb"}",
    )

    world.get_region("Hyrule Castle Tower Climb", player).connect(
        world.get_region("Hyrule Castle Third Floor Balcony", player),
        f"{"Hyrule Castle Tower Climb"} -> {"Hyrule Castle Third Floor Balcony"}",
    )

    world.get_region("Hyrule Castle Tower Climb", player).connect(
        world.get_region("Hyrule Castle Treasure Room", player),
        f"{"Hyrule Castle Tower Climb"} -> {"Hyrule Castle Treasure Room"}",
    )

    world.get_region("Hyrule Castle Tower Climb", player).connect(
        world.get_region("Ganondorf Castle", player),
        f"{"Hyrule Castle Tower Climb"} -> {"Ganondorf Castle"}",
    )

    world.get_region("Hyrule Castle Treasure Room", player).connect(
        world.get_region("Hyrule Castle Tower Climb", player),
        f"{"Hyrule Castle Treasure Room"} -> {"Hyrule Castle Tower Climb"}",
    )

    world.get_region("Lakebed Temple Boss Room", player).connect(
        world.get_region("Lake Hylia Lanayru Spring", player),
        f"{"Lakebed Temple Boss Room"} -> {"Lake Hylia Lanayru Spring"}",
    )

    world.get_region("Lakebed Temple Central Room", player).connect(
        world.get_region("Lakebed Temple Entrance", player),
        f"{"Lakebed Temple Central Room"} -> {"Lakebed Temple Entrance"}",
    )

    world.get_region("Lakebed Temple Central Room", player).connect(
        world.get_region("Lakebed Temple East Wing Second Floor", player),
        f"{"Lakebed Temple Central Room"} -> {"Lakebed Temple East Wing Second Floor"}",
    )

    world.get_region("Lakebed Temple Central Room", player).connect(
        world.get_region("Lakebed Temple East Wing First Floor", player),
        f"{"Lakebed Temple Central Room"} -> {"Lakebed Temple East Wing First Floor"}",
    )

    world.get_region("Lakebed Temple Central Room", player).connect(
        world.get_region("Lakebed Temple West Wing", player),
        f"{"Lakebed Temple Central Room"} -> {"Lakebed Temple West Wing"}",
    )

    world.get_region("Lakebed Temple Central Room", player).connect(
        world.get_region("Lakebed Temple Boss Room", player),
        f"{"Lakebed Temple Central Room"} -> {"Lakebed Temple Boss Room"}",
    )

    world.get_region("Lakebed Temple East Wing First Floor", player).connect(
        world.get_region("Lakebed Temple Central Room", player),
        f"{"Lakebed Temple East Wing First Floor"} -> {"Lakebed Temple Central Room"}",
    )

    world.get_region("Lakebed Temple East Wing Second Floor", player).connect(
        world.get_region("Lakebed Temple Central Room", player),
        f"{"Lakebed Temple East Wing Second Floor"} -> {"Lakebed Temple Central Room"}",
    )

    world.get_region("Lakebed Temple East Wing Second Floor", player).connect(
        world.get_region("Lakebed Temple East Wing First Floor", player),
        f"{"Lakebed Temple East Wing Second Floor"} -> {"Lakebed Temple East Wing First Floor"}",
    )

    world.get_region("Lakebed Temple Entrance", player).connect(
        world.get_region("Lake Hylia Lakebed Temple Entrance", player),
        f"{"Lakebed Temple Entrance"} -> {"Lake Hylia Lakebed Temple Entrance"}",
    )

    world.get_region("Lakebed Temple Entrance", player).connect(
        world.get_region("Lakebed Temple Central Room", player),
        f"{"Lakebed Temple Entrance"} -> {"Lakebed Temple Central Room"}",
    )

    world.get_region("Lakebed Temple West Wing", player).connect(
        world.get_region("Lakebed Temple Central Room", player),
        f"{"Lakebed Temple West Wing"} -> {"Lakebed Temple Central Room"}",
    )

    world.get_region("Palace of Twilight Entrance", player).connect(
        world.get_region("Mirror Chamber Upper", player),
        f"{"Palace of Twilight Entrance"} -> {"Mirror Chamber Upper"}",
    )

    world.get_region("Palace of Twilight Entrance", player).connect(
        world.get_region("Palace of Twilight West Wing", player),
        f"{"Palace of Twilight Entrance"} -> {"Palace of Twilight West Wing"}",
    )

    world.get_region("Palace of Twilight Entrance", player).connect(
        world.get_region("Palace of Twilight East Wing", player),
        f"{"Palace of Twilight Entrance"} -> {"Palace of Twilight East Wing"}",
    )

    world.get_region("Palace of Twilight Entrance", player).connect(
        world.get_region("Palace of Twilight Central First Room", player),
        f"{"Palace of Twilight Entrance"} -> {"Palace of Twilight Central First Room"}",
    )

    world.get_region("Palace of Twilight West Wing", player).connect(
        world.get_region("Palace of Twilight Entrance", player),
        f"{"Palace of Twilight West Wing"} -> {"Palace of Twilight Entrance"}",
    )

    world.get_region("Palace of Twilight East Wing", player).connect(
        world.get_region("Palace of Twilight Entrance", player),
        f"{"Palace of Twilight East Wing"} -> {"Palace of Twilight Entrance"}",
    )

    world.get_region("Palace of Twilight Central First Room", player).connect(
        world.get_region("Palace of Twilight Entrance", player),
        f"{"Palace of Twilight Central First Room"} -> {"Palace of Twilight Entrance"}",
    )

    world.get_region("Palace of Twilight Central First Room", player).connect(
        world.get_region("Palace of Twilight Outside Room", player),
        f"{"Palace of Twilight Central First Room"} -> {"Palace of Twilight Outside Room"}",
    )

    world.get_region("Palace of Twilight Outside Room", player).connect(
        world.get_region("Palace of Twilight Central First Room", player),
        f"{"Palace of Twilight Outside Room"} -> {"Palace of Twilight Central First Room"}",
    )

    world.get_region("Palace of Twilight Outside Room", player).connect(
        world.get_region("Palace of Twilight North Tower", player),
        f"{"Palace of Twilight Outside Room"} -> {"Palace of Twilight North Tower"}",
    )

    world.get_region("Palace of Twilight North Tower", player).connect(
        world.get_region("Palace of Twilight Outside Room", player),
        f"{"Palace of Twilight North Tower"} -> {"Palace of Twilight Outside Room"}",
    )

    world.get_region("Palace of Twilight North Tower", player).connect(
        world.get_region("Palace of Twilight Boss Room", player),
        f"{"Palace of Twilight North Tower"} -> {"Palace of Twilight Boss Room"}",
    )

    world.get_region("Palace of Twilight Boss Room", player).connect(
        world.get_region("Palace of Twilight Entrance", player),
        f"{"Palace of Twilight Boss Room"} -> {"Palace of Twilight Entrance"}",
    )

    world.get_region("Snowpeak Ruins Left Door", player).connect(
        world.get_region("Snowpeak Ruins Entrance", player),
        f"{"Snowpeak Ruins Left Door"} -> {"Snowpeak Ruins Entrance"}",
    )

    world.get_region("Snowpeak Ruins Left Door", player).connect(
        world.get_region("Snowpeak Summit Lower", player),
        f"{"Snowpeak Ruins Left Door"} -> {"Snowpeak Summit Lower"}",
    )

    world.get_region("Snowpeak Ruins Right Door", player).connect(
        world.get_region("Snowpeak Ruins Entrance", player),
        f"{"Snowpeak Ruins Right Door"} -> {"Snowpeak Ruins Entrance"}",
    )

    world.get_region("Snowpeak Ruins Right Door", player).connect(
        world.get_region("Snowpeak Summit Lower", player),
        f"{"Snowpeak Ruins Right Door"} -> {"Snowpeak Summit Lower"}",
    )

    world.get_region("Snowpeak Ruins Boss Room", player).connect(
        world.get_region("Snowpeak Summit Lower", player),
        f"{"Snowpeak Ruins Boss Room"} -> {"Snowpeak Summit Lower"}",
    )

    world.get_region("Snowpeak Ruins Caged Freezard Room", player).connect(
        world.get_region("Snowpeak Ruins Yeto and Yeta", player),
        f"{"Snowpeak Ruins Caged Freezard Room"} -> {"Snowpeak Ruins Yeto and Yeta"}",
    )

    world.get_region("Snowpeak Ruins Caged Freezard Room", player).connect(
        world.get_region(
            "Snowpeak Ruins Second Floor Mini Freezard Room", player
        ),
        f"{"Snowpeak Ruins Caged Freezard Room"} -> {"Snowpeak Ruins Second Floor Mini Freezard Room"}",
    )

    world.get_region("Snowpeak Ruins Caged Freezard Room", player).connect(
        world.get_region("Snowpeak Ruins Wooden Beam Room", player),
        f"{"Snowpeak Ruins Caged Freezard Room"} -> {"Snowpeak Ruins Wooden Beam Room"}",
    )

    world.get_region("Snowpeak Ruins Caged Freezard Room", player).connect(
        world.get_region("Snowpeak Ruins West Courtyard", player),
        f"{"Snowpeak Ruins Caged Freezard Room"} -> {"Snowpeak Ruins West Courtyard"}",
    )

    world.get_region("Snowpeak Ruins Chapel", player).connect(
        world.get_region("Snowpeak Ruins West Courtyard", player),
        f"{"Snowpeak Ruins Chapel"} -> {"Snowpeak Ruins West Courtyard"}",
    )

    world.get_region("Snowpeak Ruins Darkhammer Room", player).connect(
        world.get_region("Snowpeak Ruins West Courtyard", player),
        f"{"Snowpeak Ruins Darkhammer Room"} -> {"Snowpeak Ruins West Courtyard"}",
    )

    world.get_region("Snowpeak Ruins East Courtyard", player).connect(
        world.get_region("Snowpeak Ruins Yeto and Yeta", player),
        f"{"Snowpeak Ruins East Courtyard"} -> {"Snowpeak Ruins Yeto and Yeta"}",
    )

    world.get_region("Snowpeak Ruins East Courtyard", player).connect(
        world.get_region("Snowpeak Ruins West Courtyard", player),
        f"{"Snowpeak Ruins East Courtyard"} -> {"Snowpeak Ruins West Courtyard"}",
    )

    world.get_region("Snowpeak Ruins East Courtyard", player).connect(
        world.get_region(
            "Snowpeak Ruins Northeast Chilfos Room First Floor", player
        ),
        f"{"Snowpeak Ruins East Courtyard"} -> {"Snowpeak Ruins Northeast Chilfos Room First Floor"}",
    )

    world.get_region("Snowpeak Ruins Entrance", player).connect(
        world.get_region("Snowpeak Ruins Left Door", player),
        f"{"Snowpeak Ruins Entrance"} -> {"Snowpeak Ruins Left Door"}",
    )

    world.get_region("Snowpeak Ruins Entrance", player).connect(
        world.get_region("Snowpeak Ruins Right Door", player),
        f"{"Snowpeak Ruins Entrance"} -> {"Snowpeak Ruins Right Door"}",
    )

    world.get_region("Snowpeak Ruins Entrance", player).connect(
        world.get_region("Snowpeak Ruins Yeto and Yeta", player),
        f"{"Snowpeak Ruins Entrance"} -> {"Snowpeak Ruins Yeto and Yeta"}",
    )

    world.get_region(
        "Snowpeak Ruins Northeast Chilfos Room First Floor", player
    ).connect(
        world.get_region("Snowpeak Ruins East Courtyard", player),
        f"{"Snowpeak Ruins Northeast Chilfos Room First Floor"} -> {"Snowpeak Ruins East Courtyard"}",
    )

    world.get_region(
        "Snowpeak Ruins Northeast Chilfos Room First Floor", player
    ).connect(
        world.get_region("Snowpeak Ruins Yeto and Yeta", player),
        f"{"Snowpeak Ruins Northeast Chilfos Room First Floor"} -> {"Snowpeak Ruins Yeto and Yeta"}",
    )

    world.get_region(
        "Snowpeak Ruins Northeast Chilfos Room Second Floor", player
    ).connect(
        world.get_region(
            "Snowpeak Ruins Northeast Chilfos Room First Floor", player
        ),
        f"{"Snowpeak Ruins Northeast Chilfos Room Second Floor"} -> {"Snowpeak Ruins Northeast Chilfos Room First Floor"}",
    )

    world.get_region(
        "Snowpeak Ruins Northeast Chilfos Room Second Floor", player
    ).connect(
        world.get_region("Snowpeak Ruins Yeto and Yeta", player),
        f"{"Snowpeak Ruins Northeast Chilfos Room Second Floor"} -> {"Snowpeak Ruins Yeto and Yeta"}",
    )

    world.get_region(
        "Snowpeak Ruins Second Floor Mini Freezard Room", player
    ).connect(
        world.get_region("Snowpeak Ruins Entrance", player),
        f"{"Snowpeak Ruins Second Floor Mini Freezard Room"} -> {"Snowpeak Ruins Entrance"}",
    )

    world.get_region(
        "Snowpeak Ruins Second Floor Mini Freezard Room", player
    ).connect(
        world.get_region("Snowpeak Ruins East Courtyard", player),
        f"{"Snowpeak Ruins Second Floor Mini Freezard Room"} -> {"Snowpeak Ruins East Courtyard"}",
    )

    world.get_region(
        "Snowpeak Ruins Second Floor Mini Freezard Room", player
    ).connect(
        world.get_region(
            "Snowpeak Ruins Northeast Chilfos Room Second Floor", player
        ),
        f"{"Snowpeak Ruins Second Floor Mini Freezard Room"} -> {"Snowpeak Ruins Northeast Chilfos Room Second Floor"}",
    )

    world.get_region(
        "Snowpeak Ruins Second Floor Mini Freezard Room", player
    ).connect(
        world.get_region("Snowpeak Ruins Caged Freezard Room", player),
        f"{"Snowpeak Ruins Second Floor Mini Freezard Room"} -> {"Snowpeak Ruins Caged Freezard Room"}",
    )

    world.get_region("Snowpeak Ruins West Cannon Room", player).connect(
        world.get_region("Snowpeak Ruins West Courtyard", player),
        f"{"Snowpeak Ruins West Cannon Room"} -> {"Snowpeak Ruins West Courtyard"}",
    )

    world.get_region("Snowpeak Ruins West Cannon Room", player).connect(
        world.get_region("Snowpeak Ruins Wooden Beam Room", player),
        f"{"Snowpeak Ruins West Cannon Room"} -> {"Snowpeak Ruins Wooden Beam Room"}",
    )

    world.get_region("Snowpeak Ruins West Courtyard", player).connect(
        world.get_region("Snowpeak Ruins Yeto and Yeta", player),
        f"{"Snowpeak Ruins West Courtyard"} -> {"Snowpeak Ruins Yeto and Yeta"}",
    )

    world.get_region("Snowpeak Ruins West Courtyard", player).connect(
        world.get_region("Snowpeak Ruins East Courtyard", player),
        f"{"Snowpeak Ruins West Courtyard"} -> {"Snowpeak Ruins East Courtyard"}",
    )

    world.get_region("Snowpeak Ruins West Courtyard", player).connect(
        world.get_region("Snowpeak Ruins West Cannon Room", player),
        f"{"Snowpeak Ruins West Courtyard"} -> {"Snowpeak Ruins West Cannon Room"}",
    )

    world.get_region("Snowpeak Ruins West Courtyard", player).connect(
        world.get_region("Snowpeak Ruins Chapel", player),
        f"{"Snowpeak Ruins West Courtyard"} -> {"Snowpeak Ruins Chapel"}",
    )

    world.get_region("Snowpeak Ruins West Courtyard", player).connect(
        world.get_region("Snowpeak Ruins Darkhammer Room", player),
        f"{"Snowpeak Ruins West Courtyard"} -> {"Snowpeak Ruins Darkhammer Room"}",
    )

    world.get_region("Snowpeak Ruins West Courtyard", player).connect(
        world.get_region("Snowpeak Ruins Boss Room", player),
        f"{"Snowpeak Ruins West Courtyard"} -> {"Snowpeak Ruins Boss Room"}",
    )

    world.get_region("Snowpeak Ruins Wooden Beam Room", player).connect(
        world.get_region("Snowpeak Ruins West Cannon Room", player),
        f"{"Snowpeak Ruins Wooden Beam Room"} -> {"Snowpeak Ruins West Cannon Room"}",
    )

    world.get_region("Snowpeak Ruins Yeto and Yeta", player).connect(
        world.get_region("Snowpeak Ruins Entrance", player),
        f"{"Snowpeak Ruins Yeto and Yeta"} -> {"Snowpeak Ruins Entrance"}",
    )

    world.get_region("Snowpeak Ruins Yeto and Yeta", player).connect(
        world.get_region("Snowpeak Ruins Caged Freezard Room", player),
        f"{"Snowpeak Ruins Yeto and Yeta"} -> {"Snowpeak Ruins Caged Freezard Room"}",
    )

    world.get_region("Snowpeak Ruins Yeto and Yeta", player).connect(
        world.get_region("Snowpeak Ruins West Courtyard", player),
        f"{"Snowpeak Ruins Yeto and Yeta"} -> {"Snowpeak Ruins West Courtyard"}",
    )

    world.get_region("Snowpeak Ruins Yeto and Yeta", player).connect(
        world.get_region("Snowpeak Ruins East Courtyard", player),
        f"{"Snowpeak Ruins Yeto and Yeta"} -> {"Snowpeak Ruins East Courtyard"}",
    )

    world.get_region("Temple of Time Armos Antechamber", player).connect(
        world.get_region("Temple of Time Central Mechanical Platform", player),
        f"{"Temple of Time Armos Antechamber"} -> {"Temple of Time Central Mechanical Platform"}",
    )

    world.get_region("Temple of Time Boss Room", player).connect(
        world.get_region("Sacred Grove Past", player),
        f"{"Temple of Time Boss Room"} -> {"Sacred Grove Past"}",
    )

    world.get_region(
        "Temple of Time Central Mechanical Platform", player
    ).connect(
        world.get_region("Temple of Time Connecting Corridors", player),
        f"{"Temple of Time Central Mechanical Platform"} -> {"Temple of Time Connecting Corridors"}",
    )

    world.get_region(
        "Temple of Time Central Mechanical Platform", player
    ).connect(
        world.get_region("Temple of Time Armos Antechamber", player),
        f"{"Temple of Time Central Mechanical Platform"} -> {"Temple of Time Armos Antechamber"}",
    )

    world.get_region(
        "Temple of Time Central Mechanical Platform", player
    ).connect(
        world.get_region("Temple of Time Moving Wall Hallways", player),
        f"{"Temple of Time Central Mechanical Platform"} -> {"Temple of Time Moving Wall Hallways"}",
    )

    world.get_region("Temple of Time Connecting Corridors", player).connect(
        world.get_region("Temple of Time Entrance", player),
        f"{"Temple of Time Connecting Corridors"} -> {"Temple of Time Entrance"}",
    )

    world.get_region("Temple of Time Connecting Corridors", player).connect(
        world.get_region("Temple of Time Central Mechanical Platform", player),
        f"{"Temple of Time Connecting Corridors"} -> {"Temple of Time Central Mechanical Platform"}",
    )

    world.get_region("Temple of Time Crumbling Corridor", player).connect(
        world.get_region("Temple of Time Entrance", player),
        f"{"Temple of Time Crumbling Corridor"} -> {"Temple of Time Entrance"}",
    )

    world.get_region("Temple of Time Crumbling Corridor", player).connect(
        world.get_region("Temple of Time Boss Room", player),
        f"{"Temple of Time Crumbling Corridor"} -> {"Temple of Time Boss Room"}",
    )

    world.get_region("Temple of Time Darknut Arena", player).connect(
        world.get_region("Temple of Time Upper Spike Trap Corridor", player),
        f"{"Temple of Time Darknut Arena"} -> {"Temple of Time Upper Spike Trap Corridor"}",
    )

    world.get_region("Temple of Time Entrance", player).connect(
        world.get_region("Sacred Grove Past Behind Window", player),
        f"{"Temple of Time Entrance"} -> {"Sacred Grove Past Behind Window"}",
    )

    world.get_region("Temple of Time Entrance", player).connect(
        world.get_region("Temple of Time Connecting Corridors", player),
        f"{"Temple of Time Entrance"} -> {"Temple of Time Connecting Corridors"}",
    )

    world.get_region("Temple of Time Entrance", player).connect(
        world.get_region("Temple of Time Crumbling Corridor", player),
        f"{"Temple of Time Entrance"} -> {"Temple of Time Crumbling Corridor"}",
    )

    world.get_region("Temple of Time Floor Switch Puzzle Room", player).connect(
        world.get_region("Temple of Time Scales of Time", player),
        f"{"Temple of Time Floor Switch Puzzle Room"} -> {"Temple of Time Scales of Time"}",
    )

    world.get_region("Temple of Time Moving Wall Hallways", player).connect(
        world.get_region("Temple of Time Central Mechanical Platform", player),
        f"{"Temple of Time Moving Wall Hallways"} -> {"Temple of Time Central Mechanical Platform"}",
    )

    world.get_region("Temple of Time Moving Wall Hallways", player).connect(
        world.get_region("Temple of Time Scales of Time", player),
        f"{"Temple of Time Moving Wall Hallways"} -> {"Temple of Time Scales of Time"}",
    )

    world.get_region("Temple of Time Scales of Time", player).connect(
        world.get_region("Temple of Time Moving Wall Hallways", player),
        f"{"Temple of Time Scales of Time"} -> {"Temple of Time Moving Wall Hallways"}",
    )

    world.get_region("Temple of Time Scales of Time", player).connect(
        world.get_region("Temple of Time Floor Switch Puzzle Room", player),
        f"{"Temple of Time Scales of Time"} -> {"Temple of Time Floor Switch Puzzle Room"}",
    )

    world.get_region("Temple of Time Scales of Time", player).connect(
        world.get_region("Temple of Time Upper Spike Trap Corridor", player),
        f"{"Temple of Time Scales of Time"} -> {"Temple of Time Upper Spike Trap Corridor"}",
    )

    world.get_region("Temple of Time Upper Spike Trap Corridor", player).connect(
        world.get_region("Temple of Time Scales of Time", player),
        f"{"Temple of Time Upper Spike Trap Corridor"} -> {"Temple of Time Scales of Time"}",
    )

    world.get_region("Temple of Time Upper Spike Trap Corridor", player).connect(
        world.get_region("Temple of Time Darknut Arena", player),
        f"{"Temple of Time Upper Spike Trap Corridor"} -> {"Temple of Time Darknut Arena"}",
    )

    world.get_region("Death Mountain Near Kakariko", player).connect(
        world.get_region("Lower Kakariko Village", player),
        f"{"Death Mountain Near Kakariko"} -> {"Lower Kakariko Village"}",
    )

    world.get_region("Death Mountain Near Kakariko", player).connect(
        world.get_region("Death Mountain Trail", player),
        f"{"Death Mountain Near Kakariko"} -> {"Death Mountain Trail"}",
    )

    world.get_region("Death Mountain Trail", player).connect(
        world.get_region("Death Mountain Near Kakariko", player),
        f"{"Death Mountain Trail"} -> {"Death Mountain Near Kakariko"}",
    )

    world.get_region("Death Mountain Trail", player).connect(
        world.get_region("Death Mountain Volcano", player),
        f"{"Death Mountain Trail"} -> {"Death Mountain Volcano"}",
    )

    world.get_region("Death Mountain Volcano", player).connect(
        world.get_region("Death Mountain Trail", player),
        f"{"Death Mountain Volcano"} -> {"Death Mountain Trail"}",
    )

    world.get_region("Death Mountain Volcano", player).connect(
        world.get_region("Death Mountain Outside Sumo Hall", player),
        f"{"Death Mountain Volcano"} -> {"Death Mountain Outside Sumo Hall"}",
    )

    world.get_region("Death Mountain Volcano", player).connect(
        world.get_region("Death Mountain Elevator Lower", player),
        f"{"Death Mountain Volcano"} -> {"Death Mountain Elevator Lower"}",
    )

    world.get_region("Death Mountain Outside Sumo Hall", player).connect(
        world.get_region("Death Mountain Volcano", player),
        f"{"Death Mountain Outside Sumo Hall"} -> {"Death Mountain Volcano"}",
    )

    world.get_region("Death Mountain Outside Sumo Hall", player).connect(
        world.get_region("Death Mountain Sumo Hall", player),
        f"{"Death Mountain Outside Sumo Hall"} -> {"Death Mountain Sumo Hall"}",
    )

    world.get_region("Death Mountain Elevator Lower", player).connect(
        world.get_region("Death Mountain Volcano", player),
        f"{"Death Mountain Elevator Lower"} -> {"Death Mountain Volcano"}",
    )

    world.get_region("Death Mountain Elevator Lower", player).connect(
        world.get_region("Death Mountain Sumo Hall Elevator", player),
        f"{"Death Mountain Elevator Lower"} -> {"Death Mountain Sumo Hall Elevator"}",
    )

    world.get_region("Death Mountain Sumo Hall", player).connect(
        world.get_region("Death Mountain Outside Sumo Hall", player),
        f"{"Death Mountain Sumo Hall"} -> {"Death Mountain Outside Sumo Hall"}",
    )

    world.get_region("Death Mountain Sumo Hall", player).connect(
        world.get_region("Death Mountain Sumo Hall Elevator", player),
        f"{"Death Mountain Sumo Hall"} -> {"Death Mountain Sumo Hall Elevator"}",
    )

    world.get_region("Death Mountain Sumo Hall", player).connect(
        world.get_region("Death Mountain Sumo Hall Goron Mines Tunnel", player),
        f"{"Death Mountain Sumo Hall"} -> {"Death Mountain Sumo Hall Goron Mines Tunnel"}",
    )

    world.get_region("Death Mountain Sumo Hall Elevator", player).connect(
        world.get_region("Death Mountain Elevator Lower", player),
        f"{"Death Mountain Sumo Hall Elevator"} -> {"Death Mountain Elevator Lower"}",
    )

    world.get_region("Death Mountain Sumo Hall Elevator", player).connect(
        world.get_region("Death Mountain Sumo Hall", player),
        f"{"Death Mountain Sumo Hall Elevator"} -> {"Death Mountain Sumo Hall"}",
    )

    world.get_region(
        "Death Mountain Sumo Hall Goron Mines Tunnel", player
    ).connect(
        world.get_region("Death Mountain Sumo Hall", player),
        f"{"Death Mountain Sumo Hall Goron Mines Tunnel"} -> {"Death Mountain Sumo Hall"}",
    )

    world.get_region(
        "Death Mountain Sumo Hall Goron Mines Tunnel", player
    ).connect(
        world.get_region("Goron Mines Entrance", player),
        f"{"Death Mountain Sumo Hall Goron Mines Tunnel"} -> {"Goron Mines Entrance"}",
    )

    world.get_region("Hidden Village", player).connect(
        world.get_region("Eldin Field Outside Hidden Village", player),
        f"{"Hidden Village"} -> {"Eldin Field Outside Hidden Village"}",
    )

    world.get_region("Hidden Village", player).connect(
        world.get_region("Hidden Village Impaz House", player),
        f"{"Hidden Village"} -> {"Hidden Village Impaz House"}",
    )

    world.get_region("Hidden Village Impaz House", player).connect(
        world.get_region("Hidden Village", player),
        f"{"Hidden Village Impaz House"} -> {"Hidden Village"}",
    )

    world.get_region("Kakariko Gorge", player).connect(
        world.get_region("Kakariko Gorge Cave Entrance", player),
        f"{"Kakariko Gorge"} -> {"Kakariko Gorge Cave Entrance"}",
    )

    world.get_region("Kakariko Gorge", player).connect(
        world.get_region("Kakariko Gorge Behind Gate", player),
        f"{"Kakariko Gorge"} -> {"Kakariko Gorge Behind Gate"}",
    )

    world.get_region("Kakariko Gorge", player).connect(
        world.get_region("Faron Field", player),
        f"{"Kakariko Gorge"} -> {"Faron Field"}",
    )

    world.get_region("Kakariko Gorge", player).connect(
        world.get_region("Eldin Field", player),
        f"{"Kakariko Gorge"} -> {"Eldin Field"}",
    )

    world.get_region("Kakariko Gorge", player).connect(
        world.get_region("Kakariko Gorge Keese Grotto", player),
        f"{"Kakariko Gorge"} -> {"Kakariko Gorge Keese Grotto"}",
    )

    world.get_region("Kakariko Gorge Cave Entrance", player).connect(
        world.get_region("Kakariko Gorge", player),
        f"{"Kakariko Gorge Cave Entrance"} -> {"Kakariko Gorge"}",
    )

    world.get_region("Kakariko Gorge Cave Entrance", player).connect(
        world.get_region("Eldin Lantern Cave", player),
        f"{"Kakariko Gorge Cave Entrance"} -> {"Eldin Lantern Cave"}",
    )

    world.get_region("Kakariko Gorge Behind Gate", player).connect(
        world.get_region("Kakariko Gorge", player),
        f"{"Kakariko Gorge Behind Gate"} -> {"Kakariko Gorge"}",
    )

    world.get_region("Kakariko Gorge Behind Gate", player).connect(
        world.get_region("Lower Kakariko Village", player),
        f"{"Kakariko Gorge Behind Gate"} -> {"Lower Kakariko Village"}",
    )

    world.get_region("Eldin Lantern Cave", player).connect(
        world.get_region("Kakariko Gorge Cave Entrance", player),
        f"{"Eldin Lantern Cave"} -> {"Kakariko Gorge Cave Entrance"}",
    )

    world.get_region("Kakariko Gorge Keese Grotto", player).connect(
        world.get_region("Kakariko Gorge", player),
        f"{"Kakariko Gorge Keese Grotto"} -> {"Kakariko Gorge"}",
    )

    world.get_region("Eldin Field", player).connect(
        world.get_region("Eldin Field Near Castle Town", player),
        f"{"Eldin Field"} -> {"Eldin Field Near Castle Town"}",
    )

    world.get_region("Eldin Field", player).connect(
        world.get_region("Eldin Field Lava Cave Ledge", player),
        f"{"Eldin Field"} -> {"Eldin Field Lava Cave Ledge"}",
    )

    world.get_region("Eldin Field", player).connect(
        world.get_region("Kakariko Gorge", player),
        f"{"Eldin Field"} -> {"Kakariko Gorge"}",
    )

    world.get_region("Eldin Field", player).connect(
        world.get_region("Kakariko Village Behind Gate", player),
        f"{"Eldin Field"} -> {"Kakariko Village Behind Gate"}",
    )

    world.get_region("Eldin Field", player).connect(
        world.get_region("North Eldin Field", player),
        f"{"Eldin Field"} -> {"North Eldin Field"}",
    )

    world.get_region("Eldin Field", player).connect(
        world.get_region("Eldin Field Bomskit Grotto", player),
        f"{"Eldin Field"} -> {"Eldin Field Bomskit Grotto"}",
    )

    world.get_region("Eldin Field", player).connect(
        world.get_region("Eldin Field Water Bomb Fish Grotto", player),
        f"{"Eldin Field"} -> {"Eldin Field Water Bomb Fish Grotto"}",
    )

    world.get_region("Eldin Field Near Castle Town", player).connect(
        world.get_region("Eldin Field", player),
        f"{"Eldin Field Near Castle Town"} -> {"Eldin Field"}",
    )

    world.get_region("Eldin Field Near Castle Town", player).connect(
        world.get_region("Outside Castle Town East", player),
        f"{"Eldin Field Near Castle Town"} -> {"Outside Castle Town East"}",
    )

    world.get_region("Eldin Field Lava Cave Ledge", player).connect(
        world.get_region("Eldin Field", player),
        f"{"Eldin Field Lava Cave Ledge"} -> {"Eldin Field"}",
    )

    world.get_region("Eldin Field Lava Cave Ledge", player).connect(
        world.get_region("Eldin Field Lava Cave Upper", player),
        f"{"Eldin Field Lava Cave Ledge"} -> {"Eldin Field Lava Cave Upper"}",
    )

    world.get_region("Eldin Field From Lava Cave Lower", player).connect(
        world.get_region("Eldin Field", player),
        f"{"Eldin Field From Lava Cave Lower"} -> {"Eldin Field"}",
    )

    world.get_region("Eldin Field From Lava Cave Lower", player).connect(
        world.get_region("Eldin Field Lava Cave Lower", player),
        f"{"Eldin Field From Lava Cave Lower"} -> {"Eldin Field Lava Cave Lower"}",
    )

    world.get_region("North Eldin Field", player).connect(
        world.get_region("Eldin Field", player),
        f"{"North Eldin Field"} -> {"Eldin Field"}",
    )

    world.get_region("North Eldin Field", player).connect(
        world.get_region("Eldin Field Outside Hidden Village", player),
        f"{"North Eldin Field"} -> {"Eldin Field Outside Hidden Village"}",
    )

    world.get_region("North Eldin Field", player).connect(
        world.get_region("Eldin Field Grotto Platform", player),
        f"{"North Eldin Field"} -> {"Eldin Field Grotto Platform"}",
    )

    world.get_region("North Eldin Field", player).connect(
        world.get_region("Lanayru Field", player),
        f"{"North Eldin Field"} -> {"Lanayru Field"}",
    )

    world.get_region("Eldin Field Outside Hidden Village", player).connect(
        world.get_region("North Eldin Field", player),
        f"{"Eldin Field Outside Hidden Village"} -> {"North Eldin Field"}",
    )

    world.get_region("Eldin Field Outside Hidden Village", player).connect(
        world.get_region("Hidden Village", player),
        f"{"Eldin Field Outside Hidden Village"} -> {"Hidden Village"}",
    )

    world.get_region("Eldin Field Grotto Platform", player).connect(
        world.get_region("North Eldin Field", player),
        f"{"Eldin Field Grotto Platform"} -> {"North Eldin Field"}",
    )

    world.get_region("Eldin Field Grotto Platform", player).connect(
        world.get_region("Eldin Field Stalfos Grotto", player),
        f"{"Eldin Field Grotto Platform"} -> {"Eldin Field Stalfos Grotto"}",
    )

    world.get_region("Eldin Field Lava Cave Upper", player).connect(
        world.get_region("Eldin Field Lava Cave Ledge", player),
        f"{"Eldin Field Lava Cave Upper"} -> {"Eldin Field Lava Cave Ledge"}",
    )

    world.get_region("Eldin Field Lava Cave Upper", player).connect(
        world.get_region("Eldin Field Lava Cave Lower", player),
        f"{"Eldin Field Lava Cave Upper"} -> {"Eldin Field Lava Cave Lower"}",
    )

    world.get_region("Eldin Field Lava Cave Lower", player).connect(
        world.get_region("Eldin Field From Lava Cave Lower", player),
        f"{"Eldin Field Lava Cave Lower"} -> {"Eldin Field From Lava Cave Lower"}",
    )

    world.get_region("Eldin Field Bomskit Grotto", player).connect(
        world.get_region("Eldin Field", player),
        f"{"Eldin Field Bomskit Grotto"} -> {"Eldin Field"}",
    )

    world.get_region("Eldin Field Water Bomb Fish Grotto", player).connect(
        world.get_region("Eldin Field", player),
        f"{"Eldin Field Water Bomb Fish Grotto"} -> {"Eldin Field"}",
    )

    world.get_region("Eldin Field Stalfos Grotto", player).connect(
        world.get_region("Eldin Field Grotto Platform", player),
        f"{"Eldin Field Stalfos Grotto"} -> {"Eldin Field Grotto Platform"}",
    )

    world.get_region("Lower Kakariko Village", player).connect(
        world.get_region("Upper Kakariko Village", player),
        f"{"Lower Kakariko Village"} -> {"Upper Kakariko Village"}",
    )

    world.get_region("Lower Kakariko Village", player).connect(
        world.get_region("Kakariko Village Behind Gate", player),
        f"{"Lower Kakariko Village"} -> {"Kakariko Village Behind Gate"}",
    )

    world.get_region("Lower Kakariko Village", player).connect(
        world.get_region("Kakariko Gorge Behind Gate", player),
        f"{"Lower Kakariko Village"} -> {"Kakariko Gorge Behind Gate"}",
    )

    world.get_region("Lower Kakariko Village", player).connect(
        world.get_region("Kakariko Graveyard", player),
        f"{"Lower Kakariko Village"} -> {"Kakariko Graveyard"}",
    )

    world.get_region("Lower Kakariko Village", player).connect(
        world.get_region("Death Mountain Near Kakariko", player),
        f"{"Lower Kakariko Village"} -> {"Death Mountain Near Kakariko"}",
    )

    world.get_region("Lower Kakariko Village", player).connect(
        world.get_region("Kakariko Renados Sanctuary Front Left Door", player),
        f"{"Lower Kakariko Village"} -> {"Kakariko Renados Sanctuary Front Left Door"}",
    )

    world.get_region("Lower Kakariko Village", player).connect(
        world.get_region("Kakariko Renados Sanctuary Front Right Door", player),
        f"{"Lower Kakariko Village"} -> {"Kakariko Renados Sanctuary Front Right Door"}",
    )

    world.get_region("Lower Kakariko Village", player).connect(
        world.get_region("Kakariko Renados Sanctuary Back Left Door", player),
        f"{"Lower Kakariko Village"} -> {"Kakariko Renados Sanctuary Back Left Door"}",
    )

    world.get_region("Lower Kakariko Village", player).connect(
        world.get_region("Kakariko Renados Sanctuary Back Right Door", player),
        f"{"Lower Kakariko Village"} -> {"Kakariko Renados Sanctuary Back Right Door"}",
    )

    world.get_region("Lower Kakariko Village", player).connect(
        world.get_region("Kakariko Malo Mart", player),
        f"{"Lower Kakariko Village"} -> {"Kakariko Malo Mart"}",
    )

    world.get_region("Lower Kakariko Village", player).connect(
        world.get_region("Kakariko Elde Inn Left Door", player),
        f"{"Lower Kakariko Village"} -> {"Kakariko Elde Inn Left Door"}",
    )

    world.get_region("Lower Kakariko Village", player).connect(
        world.get_region("Kakariko Elde Inn Right Door", player),
        f"{"Lower Kakariko Village"} -> {"Kakariko Elde Inn Right Door"}",
    )

    world.get_region("Lower Kakariko Village", player).connect(
        world.get_region("Kakariko Bug House Door", player),
        f"{"Lower Kakariko Village"} -> {"Kakariko Bug House Door"}",
    )

    world.get_region("Lower Kakariko Village", player).connect(
        world.get_region("Kakariko Bug House Ceiling Hole", player),
        f"{"Lower Kakariko Village"} -> {"Kakariko Bug House Ceiling Hole"}",
    )

    world.get_region("Lower Kakariko Village", player).connect(
        world.get_region("Kakariko Barnes Bomb Shop Lower", player),
        f"{"Lower Kakariko Village"} -> {"Kakariko Barnes Bomb Shop Lower"}",
    )

    world.get_region("Upper Kakariko Village", player).connect(
        world.get_region("Lower Kakariko Village", player),
        f"{"Upper Kakariko Village"} -> {"Lower Kakariko Village"}",
    )

    world.get_region("Upper Kakariko Village", player).connect(
        world.get_region("Kakariko Top of Watchtower", player),
        f"{"Upper Kakariko Village"} -> {"Kakariko Top of Watchtower"}",
    )

    world.get_region("Upper Kakariko Village", player).connect(
        world.get_region("Kakariko Barnes Bomb Shop Upper", player),
        f"{"Upper Kakariko Village"} -> {"Kakariko Barnes Bomb Shop Upper"}",
    )

    world.get_region("Upper Kakariko Village", player).connect(
        world.get_region("Kakariko Watchtower Lower Door", player),
        f"{"Upper Kakariko Village"} -> {"Kakariko Watchtower Lower Door"}",
    )

    world.get_region("Upper Kakariko Village", player).connect(
        world.get_region("Kakariko Watchtower Dig Spot", player),
        f"{"Upper Kakariko Village"} -> {"Kakariko Watchtower Dig Spot"}",
    )

    world.get_region("Kakariko Top of Watchtower", player).connect(
        world.get_region("Upper Kakariko Village", player),
        f"{"Kakariko Top of Watchtower"} -> {"Upper Kakariko Village"}",
    )

    world.get_region("Kakariko Top of Watchtower", player).connect(
        world.get_region("Kakariko Watchtower Upper Door", player),
        f"{"Kakariko Top of Watchtower"} -> {"Kakariko Watchtower Upper Door"}",
    )

    world.get_region("Kakariko Village Behind Gate", player).connect(
        world.get_region("Lower Kakariko Village", player),
        f"{"Kakariko Village Behind Gate"} -> {"Lower Kakariko Village"}",
    )

    world.get_region("Kakariko Village Behind Gate", player).connect(
        world.get_region("Eldin Field", player),
        f"{"Kakariko Village Behind Gate"} -> {"Eldin Field"}",
    )

    world.get_region(
        "Kakariko Renados Sanctuary Front Left Door", player
    ).connect(
        world.get_region("Lower Kakariko Village", player),
        f"{"Kakariko Renados Sanctuary Front Left Door"} -> {"Lower Kakariko Village"}",
    )

    world.get_region(
        "Kakariko Renados Sanctuary Front Left Door", player
    ).connect(
        world.get_region("Kakariko Renados Sanctuary", player),
        f"{"Kakariko Renados Sanctuary Front Left Door"} -> {"Kakariko Renados Sanctuary"}",
    )

    world.get_region(
        "Kakariko Renados Sanctuary Front Right Door", player
    ).connect(
        world.get_region("Lower Kakariko Village", player),
        f"{"Kakariko Renados Sanctuary Front Right Door"} -> {"Lower Kakariko Village"}",
    )

    world.get_region(
        "Kakariko Renados Sanctuary Front Right Door", player
    ).connect(
        world.get_region("Kakariko Renados Sanctuary", player),
        f"{"Kakariko Renados Sanctuary Front Right Door"} -> {"Kakariko Renados Sanctuary"}",
    )

    world.get_region(
        "Kakariko Renados Sanctuary Back Left Door", player
    ).connect(
        world.get_region("Lower Kakariko Village", player),
        f"{"Kakariko Renados Sanctuary Back Left Door"} -> {"Lower Kakariko Village"}",
    )

    world.get_region(
        "Kakariko Renados Sanctuary Back Left Door", player
    ).connect(
        world.get_region("Kakariko Renados Sanctuary", player),
        f"{"Kakariko Renados Sanctuary Back Left Door"} -> {"Kakariko Renados Sanctuary"}",
    )

    world.get_region(
        "Kakariko Renados Sanctuary Back Right Door", player
    ).connect(
        world.get_region("Lower Kakariko Village", player),
        f"{"Kakariko Renados Sanctuary Back Right Door"} -> {"Lower Kakariko Village"}",
    )

    world.get_region(
        "Kakariko Renados Sanctuary Back Right Door", player
    ).connect(
        world.get_region("Kakariko Renados Sanctuary", player),
        f"{"Kakariko Renados Sanctuary Back Right Door"} -> {"Kakariko Renados Sanctuary"}",
    )

    world.get_region("Kakariko Renados Sanctuary", player).connect(
        world.get_region("Kakariko Renados Sanctuary Front Left Door", player),
        f"{"Kakariko Renados Sanctuary"} -> {"Kakariko Renados Sanctuary Front Left Door"}",
    )

    world.get_region("Kakariko Renados Sanctuary", player).connect(
        world.get_region("Kakariko Renados Sanctuary Front Right Door", player),
        f"{"Kakariko Renados Sanctuary"} -> {"Kakariko Renados Sanctuary Front Right Door"}",
    )

    world.get_region("Kakariko Renados Sanctuary", player).connect(
        world.get_region("Kakariko Renados Sanctuary Back Left Door", player),
        f"{"Kakariko Renados Sanctuary"} -> {"Kakariko Renados Sanctuary Back Left Door"}",
    )

    world.get_region("Kakariko Renados Sanctuary", player).connect(
        world.get_region("Kakariko Renados Sanctuary Back Right Door", player),
        f"{"Kakariko Renados Sanctuary"} -> {"Kakariko Renados Sanctuary Back Right Door"}",
    )

    world.get_region("Kakariko Renados Sanctuary", player).connect(
        world.get_region("Kakariko Renados Sanctuary Basement", player),
        f"{"Kakariko Renados Sanctuary"} -> {"Kakariko Renados Sanctuary Basement"}",
    )

    world.get_region("Kakariko Renados Sanctuary Basement", player).connect(
        world.get_region("Kakariko Renados Sanctuary", player),
        f"{"Kakariko Renados Sanctuary Basement"} -> {"Kakariko Renados Sanctuary"}",
    )

    world.get_region("Kakariko Malo Mart", player).connect(
        world.get_region("Lower Kakariko Village", player),
        f"{"Kakariko Malo Mart"} -> {"Lower Kakariko Village"}",
    )

    world.get_region("Kakariko Elde Inn Left Door", player).connect(
        world.get_region("Lower Kakariko Village", player),
        f"{"Kakariko Elde Inn Left Door"} -> {"Lower Kakariko Village"}",
    )

    world.get_region("Kakariko Elde Inn Left Door", player).connect(
        world.get_region("Kakariko Elde Inn", player),
        f"{"Kakariko Elde Inn Left Door"} -> {"Kakariko Elde Inn"}",
    )

    world.get_region("Kakariko Elde Inn Right Door", player).connect(
        world.get_region("Lower Kakariko Village", player),
        f"{"Kakariko Elde Inn Right Door"} -> {"Lower Kakariko Village"}",
    )

    world.get_region("Kakariko Elde Inn Right Door", player).connect(
        world.get_region("Kakariko Elde Inn", player),
        f"{"Kakariko Elde Inn Right Door"} -> {"Kakariko Elde Inn"}",
    )

    world.get_region("Kakariko Elde Inn", player).connect(
        world.get_region("Kakariko Elde Inn Left Door", player),
        f"{"Kakariko Elde Inn"} -> {"Kakariko Elde Inn Left Door"}",
    )

    world.get_region("Kakariko Elde Inn", player).connect(
        world.get_region("Kakariko Elde Inn Right Door", player),
        f"{"Kakariko Elde Inn"} -> {"Kakariko Elde Inn Right Door"}",
    )

    world.get_region("Kakariko Bug House Door", player).connect(
        world.get_region("Lower Kakariko Village", player),
        f"{"Kakariko Bug House Door"} -> {"Lower Kakariko Village"}",
    )

    world.get_region("Kakariko Bug House Door", player).connect(
        world.get_region("Kakariko Bug House", player),
        f"{"Kakariko Bug House Door"} -> {"Kakariko Bug House"}",
    )

    world.get_region("Kakariko Bug House Ceiling Hole", player).connect(
        world.get_region("Kakariko Bug House", player),
        f"{"Kakariko Bug House Ceiling Hole"} -> {"Kakariko Bug House"}",
    )

    world.get_region("Kakariko Bug House Ceiling Hole", player).connect(
        world.get_region("Lower Kakariko Village", player),
        f"{"Kakariko Bug House Ceiling Hole"} -> {"Lower Kakariko Village"}",
    )

    world.get_region("Kakariko Bug House", player).connect(
        world.get_region("Kakariko Bug House Door", player),
        f"{"Kakariko Bug House"} -> {"Kakariko Bug House Door"}",
    )

    world.get_region("Kakariko Bug House", player).connect(
        world.get_region("Kakariko Bug House Ceiling Hole", player),
        f"{"Kakariko Bug House"} -> {"Kakariko Bug House Ceiling Hole"}",
    )

    world.get_region("Kakariko Barnes Bomb Shop Lower", player).connect(
        world.get_region("Lower Kakariko Village", player),
        f"{"Kakariko Barnes Bomb Shop Lower"} -> {"Lower Kakariko Village"}",
    )

    world.get_region("Kakariko Barnes Bomb Shop Lower", player).connect(
        world.get_region("Kakariko Barnes Bomb Shop Upper", player),
        f"{"Kakariko Barnes Bomb Shop Lower"} -> {"Kakariko Barnes Bomb Shop Upper"}",
    )

    world.get_region("Kakariko Barnes Bomb Shop Upper", player).connect(
        world.get_region("Upper Kakariko Village", player),
        f"{"Kakariko Barnes Bomb Shop Upper"} -> {"Upper Kakariko Village"}",
    )

    world.get_region("Kakariko Barnes Bomb Shop Upper", player).connect(
        world.get_region("Kakariko Barnes Bomb Shop Lower", player),
        f"{"Kakariko Barnes Bomb Shop Upper"} -> {"Kakariko Barnes Bomb Shop Lower"}",
    )

    world.get_region("Kakariko Watchtower Lower Door", player).connect(
        world.get_region("Upper Kakariko Village", player),
        f"{"Kakariko Watchtower Lower Door"} -> {"Upper Kakariko Village"}",
    )

    world.get_region("Kakariko Watchtower Lower Door", player).connect(
        world.get_region("Kakariko Watchtower", player),
        f"{"Kakariko Watchtower Lower Door"} -> {"Kakariko Watchtower"}",
    )

    world.get_region("Kakariko Watchtower Dig Spot", player).connect(
        world.get_region("Upper Kakariko Village", player),
        f"{"Kakariko Watchtower Dig Spot"} -> {"Upper Kakariko Village"}",
    )

    world.get_region("Kakariko Watchtower Dig Spot", player).connect(
        world.get_region("Kakariko Watchtower", player),
        f"{"Kakariko Watchtower Dig Spot"} -> {"Kakariko Watchtower"}",
    )

    world.get_region("Kakariko Watchtower Upper Door", player).connect(
        world.get_region("Kakariko Top of Watchtower", player),
        f"{"Kakariko Watchtower Upper Door"} -> {"Kakariko Top of Watchtower"}",
    )

    world.get_region("Kakariko Watchtower Upper Door", player).connect(
        world.get_region("Kakariko Watchtower", player),
        f"{"Kakariko Watchtower Upper Door"} -> {"Kakariko Watchtower"}",
    )

    world.get_region("Kakariko Watchtower", player).connect(
        world.get_region("Kakariko Watchtower Lower Door", player),
        f"{"Kakariko Watchtower"} -> {"Kakariko Watchtower Lower Door"}",
    )

    world.get_region("Kakariko Watchtower", player).connect(
        world.get_region("Kakariko Watchtower Dig Spot", player),
        f"{"Kakariko Watchtower"} -> {"Kakariko Watchtower Dig Spot"}",
    )

    world.get_region("Kakariko Watchtower", player).connect(
        world.get_region("Kakariko Watchtower Upper Door", player),
        f"{"Kakariko Watchtower"} -> {"Kakariko Watchtower Upper Door"}",
    )

    world.get_region("Kakariko Graveyard", player).connect(
        world.get_region("Lower Kakariko Village", player),
        f"{"Kakariko Graveyard"} -> {"Lower Kakariko Village"}",
    )

    world.get_region("Kakariko Graveyard", player).connect(
        world.get_region("Lake Hylia", player),
        f"{"Kakariko Graveyard"} -> {"Lake Hylia"}",
    )

    world.get_region("South Faron Woods", player).connect(
        world.get_region("South Faron Woods Behind Gate", player),
        f"{"South Faron Woods"} -> {"South Faron Woods Behind Gate"}",
    )

    world.get_region("South Faron Woods", player).connect(
        world.get_region("South Faron Woods Owl Statue Area", player),
        f"{"South Faron Woods"} -> {"South Faron Woods Owl Statue Area"}",
    )

    world.get_region("South Faron Woods", player).connect(
        world.get_region("Ordon Bridge", player),
        f"{"South Faron Woods"} -> {"Ordon Bridge"}",
    )

    world.get_region("South Faron Woods", player).connect(
        world.get_region("Faron Field", player),
        f"{"South Faron Woods"} -> {"Faron Field"}",
    )

    world.get_region("South Faron Woods", player).connect(
        world.get_region("Faron Woods Coros House Lower", player),
        f"{"South Faron Woods"} -> {"Faron Woods Coros House Lower"}",
    )

    world.get_region("South Faron Woods Behind Gate", player).connect(
        world.get_region("South Faron Woods", player),
        f"{"South Faron Woods Behind Gate"} -> {"South Faron Woods"}",
    )

    world.get_region("South Faron Woods Behind Gate", player).connect(
        world.get_region("Faron Woods Cave Southern Entrance", player),
        f"{"South Faron Woods Behind Gate"} -> {"Faron Woods Cave Southern Entrance"}",
    )

    world.get_region("South Faron Woods Coros Ledge", player).connect(
        world.get_region("South Faron Woods", player),
        f"{"South Faron Woods Coros Ledge"} -> {"South Faron Woods"}",
    )

    world.get_region("South Faron Woods Coros Ledge", player).connect(
        world.get_region("Faron Woods Coros House Upper", player),
        f"{"South Faron Woods Coros Ledge"} -> {"Faron Woods Coros House Upper"}",
    )

    world.get_region("South Faron Woods Owl Statue Area", player).connect(
        world.get_region("South Faron Woods", player),
        f"{"South Faron Woods Owl Statue Area"} -> {"South Faron Woods"}",
    )

    world.get_region("South Faron Woods Owl Statue Area", player).connect(
        world.get_region("South Faron Woods Above Owl Statue", player),
        f"{"South Faron Woods Owl Statue Area"} -> {"South Faron Woods Above Owl Statue"}",
    )

    world.get_region("South Faron Woods Above Owl Statue", player).connect(
        world.get_region("South Faron Woods Owl Statue Area", player),
        f"{"South Faron Woods Above Owl Statue"} -> {"South Faron Woods Owl Statue Area"}",
    )

    world.get_region("South Faron Woods Above Owl Statue", player).connect(
        world.get_region("Mist Area Near Owl Statue Chest", player),
        f"{"South Faron Woods Above Owl Statue"} -> {"Mist Area Near Owl Statue Chest"}",
    )

    world.get_region("Faron Woods Coros House Lower", player).connect(
        world.get_region("Faron Woods Coros House Upper", player),
        f"{"Faron Woods Coros House Lower"} -> {"Faron Woods Coros House Upper"}",
    )

    world.get_region("Faron Woods Coros House Lower", player).connect(
        world.get_region("South Faron Woods", player),
        f"{"Faron Woods Coros House Lower"} -> {"South Faron Woods"}",
    )

    world.get_region("Faron Woods Coros House Upper", player).connect(
        world.get_region("Faron Woods Coros House Lower", player),
        f"{"Faron Woods Coros House Upper"} -> {"Faron Woods Coros House Lower"}",
    )

    world.get_region("Faron Woods Coros House Upper", player).connect(
        world.get_region("South Faron Woods Coros Ledge", player),
        f"{"Faron Woods Coros House Upper"} -> {"South Faron Woods Coros Ledge"}",
    )

    world.get_region("Faron Woods Cave Southern Entrance", player).connect(
        world.get_region("South Faron Woods Behind Gate", player),
        f"{"Faron Woods Cave Southern Entrance"} -> {"South Faron Woods Behind Gate"}",
    )

    world.get_region("Faron Woods Cave Southern Entrance", player).connect(
        world.get_region("Faron Woods Cave", player),
        f"{"Faron Woods Cave Southern Entrance"} -> {"Faron Woods Cave"}",
    )

    world.get_region("Faron Woods Cave", player).connect(
        world.get_region("Faron Woods Cave Southern Entrance", player),
        f"{"Faron Woods Cave"} -> {"Faron Woods Cave Southern Entrance"}",
    )

    world.get_region("Faron Woods Cave", player).connect(
        world.get_region("Faron Woods Cave Northern Entrance", player),
        f"{"Faron Woods Cave"} -> {"Faron Woods Cave Northern Entrance"}",
    )

    world.get_region("Mist Area Near Faron Woods Cave", player).connect(
        world.get_region("Mist Area Inside Mist", player),
        f"{"Mist Area Near Faron Woods Cave"} -> {"Mist Area Inside Mist"}",
    )

    world.get_region("Mist Area Near Faron Woods Cave", player).connect(
        world.get_region("Mist Area Under Owl Statue Chest", player),
        f"{"Mist Area Near Faron Woods Cave"} -> {"Mist Area Under Owl Statue Chest"}",
    )

    world.get_region("Mist Area Near Faron Woods Cave", player).connect(
        world.get_region("Faron Woods Cave Northern Entrance", player),
        f"{"Mist Area Near Faron Woods Cave"} -> {"Faron Woods Cave Northern Entrance"}",
    )

    world.get_region("Mist Area Inside Mist", player).connect(
        world.get_region("Mist Area Near Faron Woods Cave", player),
        f"{"Mist Area Inside Mist"} -> {"Mist Area Near Faron Woods Cave"}",
    )

    world.get_region("Mist Area Inside Mist", player).connect(
        world.get_region("Mist Area Under Owl Statue Chest", player),
        f"{"Mist Area Inside Mist"} -> {"Mist Area Under Owl Statue Chest"}",
    )

    world.get_region("Mist Area Inside Mist", player).connect(
        world.get_region("Mist Area Outside Faron Mist Cave", player),
        f"{"Mist Area Inside Mist"} -> {"Mist Area Outside Faron Mist Cave"}",
    )

    world.get_region("Mist Area Inside Mist", player).connect(
        world.get_region("Mist Area Near North Faron Woods", player),
        f"{"Mist Area Inside Mist"} -> {"Mist Area Near North Faron Woods"}",
    )

    world.get_region("Mist Area Under Owl Statue Chest", player).connect(
        world.get_region("Mist Area Inside Mist", player),
        f"{"Mist Area Under Owl Statue Chest"} -> {"Mist Area Inside Mist"}",
    )

    world.get_region("Mist Area Under Owl Statue Chest", player).connect(
        world.get_region("Mist Area Center Stump", player),
        f"{"Mist Area Under Owl Statue Chest"} -> {"Mist Area Center Stump"}",
    )

    world.get_region("Mist Area Near Owl Statue Chest", player).connect(
        world.get_region("Mist Area Under Owl Statue Chest", player),
        f"{"Mist Area Near Owl Statue Chest"} -> {"Mist Area Under Owl Statue Chest"}",
    )

    world.get_region("Mist Area Near Owl Statue Chest", player).connect(
        world.get_region("South Faron Woods Above Owl Statue", player),
        f"{"Mist Area Near Owl Statue Chest"} -> {"South Faron Woods Above Owl Statue"}",
    )

    world.get_region("Mist Area Center Stump", player).connect(
        world.get_region("Mist Area Inside Mist", player),
        f"{"Mist Area Center Stump"} -> {"Mist Area Inside Mist"}",
    )

    world.get_region("Mist Area Center Stump", player).connect(
        world.get_region("Mist Area Near North Faron Woods", player),
        f"{"Mist Area Center Stump"} -> {"Mist Area Near North Faron Woods"}",
    )

    world.get_region("Mist Area Outside Faron Mist Cave", player).connect(
        world.get_region("Mist Area Inside Mist", player),
        f"{"Mist Area Outside Faron Mist Cave"} -> {"Mist Area Inside Mist"}",
    )

    world.get_region("Mist Area Outside Faron Mist Cave", player).connect(
        world.get_region("Mist Area Faron Mist Cave", player),
        f"{"Mist Area Outside Faron Mist Cave"} -> {"Mist Area Faron Mist Cave"}",
    )

    world.get_region("Mist Area Near North Faron Woods", player).connect(
        world.get_region("Mist Area Inside Mist", player),
        f"{"Mist Area Near North Faron Woods"} -> {"Mist Area Inside Mist"}",
    )

    world.get_region("Mist Area Near North Faron Woods", player).connect(
        world.get_region("Mist Area Near Faron Woods Cave", player),
        f"{"Mist Area Near North Faron Woods"} -> {"Mist Area Near Faron Woods Cave"}",
    )

    world.get_region("Mist Area Near North Faron Woods", player).connect(
        world.get_region("North Faron Woods", player),
        f"{"Mist Area Near North Faron Woods"} -> {"North Faron Woods"}",
    )

    world.get_region("Faron Woods Cave Northern Entrance", player).connect(
        world.get_region("Mist Area Near Faron Woods Cave", player),
        f"{"Faron Woods Cave Northern Entrance"} -> {"Mist Area Near Faron Woods Cave"}",
    )

    world.get_region("Faron Woods Cave Northern Entrance", player).connect(
        world.get_region("Faron Woods Cave", player),
        f"{"Faron Woods Cave Northern Entrance"} -> {"Faron Woods Cave"}",
    )

    world.get_region("Mist Area Faron Mist Cave", player).connect(
        world.get_region("Mist Area Outside Faron Mist Cave", player),
        f"{"Mist Area Faron Mist Cave"} -> {"Mist Area Outside Faron Mist Cave"}",
    )

    world.get_region("North Faron Woods", player).connect(
        world.get_region("Mist Area Near North Faron Woods", player),
        f"{"North Faron Woods"} -> {"Mist Area Near North Faron Woods"}",
    )

    world.get_region("North Faron Woods", player).connect(
        world.get_region("Lost Woods", player),
        f"{"North Faron Woods"} -> {"Lost Woods"}",
    )

    world.get_region("North Faron Woods", player).connect(
        world.get_region("Forest Temple Entrance", player),
        f"{"North Faron Woods"} -> {"Forest Temple Entrance"}",
    )

    world.get_region("Faron Field", player).connect(
        world.get_region("Faron Field Behind Boulder", player),
        f"{"Faron Field"} -> {"Faron Field Behind Boulder"}",
    )

    world.get_region("Faron Field", player).connect(
        world.get_region("South Faron Woods", player),
        f"{"Faron Field"} -> {"South Faron Woods"}",
    )

    world.get_region("Faron Field", player).connect(
        world.get_region("Kakariko Gorge", player),
        f"{"Faron Field"} -> {"Kakariko Gorge"}",
    )

    world.get_region("Faron Field", player).connect(
        world.get_region("Lake Hylia Bridge", player),
        f"{"Faron Field"} -> {"Lake Hylia Bridge"}",
    )

    world.get_region("Faron Field", player).connect(
        world.get_region("Faron Field Corner Grotto", player),
        f"{"Faron Field"} -> {"Faron Field Corner Grotto"}",
    )

    world.get_region("Faron Field", player).connect(
        world.get_region("Faron Field Fishing Grotto", player),
        f"{"Faron Field"} -> {"Faron Field Fishing Grotto"}",
    )

    world.get_region("Faron Field Behind Boulder", player).connect(
        world.get_region("Faron Field", player),
        f"{"Faron Field Behind Boulder"} -> {"Faron Field"}",
    )

    world.get_region("Faron Field Behind Boulder", player).connect(
        world.get_region("Outside Castle Town South Inside Boulder", player),
        f"{"Faron Field Behind Boulder"} -> {"Outside Castle Town South Inside Boulder"}",
    )

    world.get_region("Faron Field Corner Grotto", player).connect(
        world.get_region("Faron Field", player),
        f"{"Faron Field Corner Grotto"} -> {"Faron Field"}",
    )

    world.get_region("Faron Field Fishing Grotto", player).connect(
        world.get_region("Faron Field", player),
        f"{"Faron Field Fishing Grotto"} -> {"Faron Field"}",
    )

    world.get_region("Lost Woods", player).connect(
        world.get_region("Lost Woods Lower Battle Arena", player),
        f"{"Lost Woods"} -> {"Lost Woods Lower Battle Arena"}",
    )

    world.get_region("Lost Woods", player).connect(
        world.get_region("Lost Woods Upper Battle Arena", player),
        f"{"Lost Woods"} -> {"Lost Woods Upper Battle Arena"}",
    )

    world.get_region("Lost Woods", player).connect(
        world.get_region("North Faron Woods", player),
        f"{"Lost Woods"} -> {"North Faron Woods"}",
    )

    world.get_region("Lost Woods Lower Battle Arena", player).connect(
        world.get_region("Lost Woods", player),
        f"{"Lost Woods Lower Battle Arena"} -> {"Lost Woods"}",
    )

    world.get_region("Lost Woods Lower Battle Arena", player).connect(
        world.get_region("Sacred Grove Lower", player),
        f"{"Lost Woods Lower Battle Arena"} -> {"Sacred Grove Lower"}",
    )

    world.get_region("Lost Woods Lower Battle Arena", player).connect(
        world.get_region("Lost Woods Baba Serpent Grotto", player),
        f"{"Lost Woods Lower Battle Arena"} -> {"Lost Woods Baba Serpent Grotto"}",
    )

    world.get_region("Lost Woods Upper Battle Arena", player).connect(
        world.get_region("Sacred Grove Before Block", player),
        f"{"Lost Woods Upper Battle Arena"} -> {"Sacred Grove Before Block"}",
    )

    world.get_region("Lost Woods Baba Serpent Grotto", player).connect(
        world.get_region("Lost Woods Lower Battle Arena", player),
        f"{"Lost Woods Baba Serpent Grotto"} -> {"Lost Woods Lower Battle Arena"}",
    )

    world.get_region("Sacred Grove Before Block", player).connect(
        world.get_region("Lost Woods Upper Battle Arena", player),
        f"{"Sacred Grove Before Block"} -> {"Lost Woods Upper Battle Arena"}",
    )

    world.get_region("Sacred Grove Before Block", player).connect(
        world.get_region("Sacred Grove Upper", player),
        f"{"Sacred Grove Before Block"} -> {"Sacred Grove Upper"}",
    )

    world.get_region("Sacred Grove Upper", player).connect(
        world.get_region("Sacred Grove Lower", player),
        f"{"Sacred Grove Upper"} -> {"Sacred Grove Lower"}",
    )

    world.get_region("Sacred Grove Upper", player).connect(
        world.get_region("Sacred Grove Past", player),
        f"{"Sacred Grove Upper"} -> {"Sacred Grove Past"}",
    )

    world.get_region("Sacred Grove Lower", player).connect(
        world.get_region("Lost Woods Lower Battle Arena", player),
        f"{"Sacred Grove Lower"} -> {"Lost Woods Lower Battle Arena"}",
    )

    world.get_region("Sacred Grove Lower", player).connect(
        world.get_region("Sacred Grove Upper", player),
        f"{"Sacred Grove Lower"} -> {"Sacred Grove Upper"}",
    )

    world.get_region("Sacred Grove Past", player).connect(
        world.get_region("Sacred Grove Past Behind Window", player),
        f"{"Sacred Grove Past"} -> {"Sacred Grove Past Behind Window"}",
    )

    world.get_region("Sacred Grove Past", player).connect(
        world.get_region("Sacred Grove Upper", player),
        f"{"Sacred Grove Past"} -> {"Sacred Grove Upper"}",
    )

    world.get_region("Sacred Grove Past Behind Window", player).connect(
        world.get_region("Sacred Grove Past", player),
        f"{"Sacred Grove Past Behind Window"} -> {"Sacred Grove Past"}",
    )

    world.get_region("Sacred Grove Past Behind Window", player).connect(
        world.get_region("Temple of Time Entrance", player),
        f"{"Sacred Grove Past Behind Window"} -> {"Temple of Time Entrance"}",
    )

    world.get_region(
        "Gerudo Desert Cave of Ordeals Floors 01-11", player
    ).connect(
        world.get_region("Gerudo Desert Cave of Ordeals Plateau", player),
        f"{"Gerudo Desert Cave of Ordeals Floors 01-11"} -> {"Gerudo Desert Cave of Ordeals Plateau"}",
    )

    world.get_region(
        "Gerudo Desert Cave of Ordeals Floors 01-11", player
    ).connect(
        world.get_region("Gerudo Desert Cave of Ordeals Floors 12-21", player),
        f"{"Gerudo Desert Cave of Ordeals Floors 01-11"} -> {"Gerudo Desert Cave of Ordeals Floors 12-21"}",
    )

    world.get_region(
        "Gerudo Desert Cave of Ordeals Floors 12-21", player
    ).connect(
        world.get_region("Gerudo Desert Cave of Ordeals Floors 22-31", player),
        f"{"Gerudo Desert Cave of Ordeals Floors 12-21"} -> {"Gerudo Desert Cave of Ordeals Floors 22-31"}",
    )

    world.get_region(
        "Gerudo Desert Cave of Ordeals Floors 22-31", player
    ).connect(
        world.get_region("Gerudo Desert Cave of Ordeals Floors 32-41", player),
        f"{"Gerudo Desert Cave of Ordeals Floors 22-31"} -> {"Gerudo Desert Cave of Ordeals Floors 32-41"}",
    )

    world.get_region(
        "Gerudo Desert Cave of Ordeals Floors 32-41", player
    ).connect(
        world.get_region("Gerudo Desert Cave of Ordeals Floors 42-50", player),
        f"{"Gerudo Desert Cave of Ordeals Floors 32-41"} -> {"Gerudo Desert Cave of Ordeals Floors 42-50"}",
    )

    world.get_region(
        "Gerudo Desert Cave of Ordeals Floors 42-50", player
    ).connect(
        world.get_region("Lake Hylia Lanayru Spring", player),
        f"{"Gerudo Desert Cave of Ordeals Floors 42-50"} -> {"Lake Hylia Lanayru Spring"}",
    )

    world.get_region("Gerudo Desert", player).connect(
        world.get_region("Gerudo Desert Cave of Ordeals Plateau", player),
        f"{"Gerudo Desert"} -> {"Gerudo Desert Cave of Ordeals Plateau"}",
    )

    world.get_region("Gerudo Desert", player).connect(
        world.get_region("Gerudo Desert Basin", player),
        f"{"Gerudo Desert"} -> {"Gerudo Desert Basin"}",
    )

    world.get_region("Gerudo Desert", player).connect(
        world.get_region("Gerudo Desert Skulltula Grotto", player),
        f"{"Gerudo Desert"} -> {"Gerudo Desert Skulltula Grotto"}",
    )

    world.get_region("Gerudo Desert Cave of Ordeals Plateau", player).connect(
        world.get_region("Gerudo Desert", player),
        f"{"Gerudo Desert Cave of Ordeals Plateau"} -> {"Gerudo Desert"}",
    )

    world.get_region("Gerudo Desert Cave of Ordeals Plateau", player).connect(
        world.get_region("Gerudo Desert Cave of Ordeals Floors 01-11", player),
        f"{"Gerudo Desert Cave of Ordeals Plateau"} -> {"Gerudo Desert Cave of Ordeals Floors 01-11"}",
    )

    world.get_region("Gerudo Desert Basin", player).connect(
        world.get_region("Gerudo Desert", player),
        f"{"Gerudo Desert Basin"} -> {"Gerudo Desert"}",
    )

    world.get_region("Gerudo Desert Basin", player).connect(
        world.get_region("Gerudo Desert North East Ledge", player),
        f"{"Gerudo Desert Basin"} -> {"Gerudo Desert North East Ledge"}",
    )

    world.get_region("Gerudo Desert Basin", player).connect(
        world.get_region("Gerudo Desert Outside Bulblin Camp", player),
        f"{"Gerudo Desert Basin"} -> {"Gerudo Desert Outside Bulblin Camp"}",
    )

    world.get_region("Gerudo Desert Basin", player).connect(
        world.get_region("Gerudo Desert Chu Grotto", player),
        f"{"Gerudo Desert Basin"} -> {"Gerudo Desert Chu Grotto"}",
    )

    world.get_region("Gerudo Desert North East Ledge", player).connect(
        world.get_region("Gerudo Desert Basin", player),
        f"{"Gerudo Desert North East Ledge"} -> {"Gerudo Desert Basin"}",
    )

    world.get_region("Gerudo Desert North East Ledge", player).connect(
        world.get_region("Gerudo Desert Rock Grotto", player),
        f"{"Gerudo Desert North East Ledge"} -> {"Gerudo Desert Rock Grotto"}",
    )

    world.get_region("Gerudo Desert Outside Bulblin Camp", player).connect(
        world.get_region("Gerudo Desert Basin", player),
        f"{"Gerudo Desert Outside Bulblin Camp"} -> {"Gerudo Desert Basin"}",
    )

    world.get_region("Gerudo Desert Outside Bulblin Camp", player).connect(
        world.get_region("Bulblin Camp", player),
        f"{"Gerudo Desert Outside Bulblin Camp"} -> {"Bulblin Camp"}",
    )

    world.get_region("Gerudo Desert Skulltula Grotto", player).connect(
        world.get_region("Gerudo Desert", player),
        f"{"Gerudo Desert Skulltula Grotto"} -> {"Gerudo Desert"}",
    )

    world.get_region("Gerudo Desert Chu Grotto", player).connect(
        world.get_region("Gerudo Desert Basin", player),
        f"{"Gerudo Desert Chu Grotto"} -> {"Gerudo Desert Basin"}",
    )

    world.get_region("Gerudo Desert Rock Grotto", player).connect(
        world.get_region("Gerudo Desert North East Ledge", player),
        f"{"Gerudo Desert Rock Grotto"} -> {"Gerudo Desert North East Ledge"}",
    )

    world.get_region("Bulblin Camp", player).connect(
        world.get_region("Gerudo Desert Outside Bulblin Camp", player),
        f"{"Bulblin Camp"} -> {"Gerudo Desert Outside Bulblin Camp"}",
    )

    world.get_region("Bulblin Camp", player).connect(
        world.get_region("Outside Arbiters Grounds", player),
        f"{"Bulblin Camp"} -> {"Outside Arbiters Grounds"}",
    )

    world.get_region("Outside Arbiters Grounds", player).connect(
        world.get_region("Bulblin Camp", player),
        f"{"Outside Arbiters Grounds"} -> {"Bulblin Camp"}",
    )

    world.get_region("Outside Arbiters Grounds", player).connect(
        world.get_region("Arbiters Grounds Entrance", player),
        f"{"Outside Arbiters Grounds"} -> {"Arbiters Grounds Entrance"}",
    )

    world.get_region("Mirror Chamber Lower", player).connect(
        world.get_region("Arbiters Grounds Boss Room", player),
        f"{"Mirror Chamber Lower"} -> {"Arbiters Grounds Boss Room"}",
    )

    world.get_region("Mirror Chamber Lower", player).connect(
        world.get_region("Mirror Chamber Upper", player),
        f"{"Mirror Chamber Lower"} -> {"Mirror Chamber Upper"}",
    )

    world.get_region("Mirror Chamber Upper", player).connect(
        world.get_region("Mirror Chamber Lower", player),
        f"{"Mirror Chamber Upper"} -> {"Mirror Chamber Lower"}",
    )

    world.get_region("Mirror Chamber Upper", player).connect(
        world.get_region("Mirror of Twilight", player),
        f"{"Mirror Chamber Upper"} -> {"Mirror of Twilight"}",
    )

    world.get_region("Mirror of Twilight", player).connect(
        world.get_region("Mirror Chamber Upper", player),
        f"{"Mirror of Twilight"} -> {"Mirror Chamber Upper"}",
    )

    world.get_region("Mirror of Twilight", player).connect(
        world.get_region("Palace of Twilight Entrance", player),
        f"{"Mirror of Twilight"} -> {"Palace of Twilight Entrance"}",
    )

    world.get_region("Castle Town West", player).connect(
        world.get_region("Outside Castle Town West", player),
        f"{"Castle Town West"} -> {"Outside Castle Town West"}",
    )

    world.get_region("Castle Town West", player).connect(
        world.get_region("Castle Town Center", player),
        f"{"Castle Town West"} -> {"Castle Town Center"}",
    )

    world.get_region("Castle Town West", player).connect(
        world.get_region("Castle Town South", player),
        f"{"Castle Town West"} -> {"Castle Town South"}",
    )

    world.get_region("Castle Town West", player).connect(
        world.get_region("Castle Town STAR Game", player),
        f"{"Castle Town West"} -> {"Castle Town STAR Game"}",
    )

    world.get_region("Castle Town STAR Game", player).connect(
        world.get_region("Castle Town West", player),
        f"{"Castle Town STAR Game"} -> {"Castle Town West"}",
    )

    world.get_region("Castle Town Center", player).connect(
        world.get_region("Castle Town West", player),
        f"{"Castle Town Center"} -> {"Castle Town West"}",
    )

    world.get_region("Castle Town Center", player).connect(
        world.get_region("Castle Town North", player),
        f"{"Castle Town Center"} -> {"Castle Town North"}",
    )

    world.get_region("Castle Town Center", player).connect(
        world.get_region("Castle Town East", player),
        f"{"Castle Town Center"} -> {"Castle Town East"}",
    )

    world.get_region("Castle Town Center", player).connect(
        world.get_region("Castle Town South", player),
        f"{"Castle Town Center"} -> {"Castle Town South"}",
    )

    world.get_region("Castle Town Center", player).connect(
        world.get_region("Castle Town Goron House Left Door", player),
        f"{"Castle Town Center"} -> {"Castle Town Goron House Left Door"}",
    )

    world.get_region("Castle Town Center", player).connect(
        world.get_region("Castle Town Goron House Right Door", player),
        f"{"Castle Town Center"} -> {"Castle Town Goron House Right Door"}",
    )

    world.get_region("Castle Town Center", player).connect(
        world.get_region("Castle Town Malo Mart", player),
        f"{"Castle Town Center"} -> {"Castle Town Malo Mart"}",
    )

    world.get_region("Castle Town Goron House Left Door", player).connect(
        world.get_region("Castle Town Center", player),
        f"{"Castle Town Goron House Left Door"} -> {"Castle Town Center"}",
    )

    world.get_region("Castle Town Goron House Left Door", player).connect(
        world.get_region("Castle Town Goron House", player),
        f"{"Castle Town Goron House Left Door"} -> {"Castle Town Goron House"}",
    )

    world.get_region("Castle Town Goron House Right Door", player).connect(
        world.get_region("Castle Town Center", player),
        f"{"Castle Town Goron House Right Door"} -> {"Castle Town Center"}",
    )

    world.get_region("Castle Town Goron House Right Door", player).connect(
        world.get_region("Castle Town Goron House", player),
        f"{"Castle Town Goron House Right Door"} -> {"Castle Town Goron House"}",
    )

    world.get_region("Castle Town Goron House", player).connect(
        world.get_region("Castle Town Goron House Left Door", player),
        f"{"Castle Town Goron House"} -> {"Castle Town Goron House Left Door"}",
    )

    world.get_region("Castle Town Goron House", player).connect(
        world.get_region("Castle Town Goron House Right Door", player),
        f"{"Castle Town Goron House"} -> {"Castle Town Goron House Right Door"}",
    )

    world.get_region("Castle Town Malo Mart", player).connect(
        world.get_region("Castle Town Center", player),
        f"{"Castle Town Malo Mart"} -> {"Castle Town Center"}",
    )

    world.get_region("Castle Town North", player).connect(
        world.get_region("Castle Town North Behind First Door", player),
        f"{"Castle Town North"} -> {"Castle Town North Behind First Door"}",
    )

    world.get_region("Castle Town North", player).connect(
        world.get_region("Castle Town Center", player),
        f"{"Castle Town North"} -> {"Castle Town Center"}",
    )

    world.get_region("Castle Town North Behind First Door", player).connect(
        world.get_region("Castle Town North", player),
        f"{"Castle Town North Behind First Door"} -> {"Castle Town North"}",
    )

    world.get_region("Castle Town North Behind First Door", player).connect(
        world.get_region("Castle Town North Inside Barrier", player),
        f"{"Castle Town North Behind First Door"} -> {"Castle Town North Inside Barrier"}",
    )

    world.get_region("Castle Town North Inside Barrier", player).connect(
        world.get_region("Castle Town North Behind First Door", player),
        f"{"Castle Town North Inside Barrier"} -> {"Castle Town North Behind First Door"}",
    )

    world.get_region("Castle Town North Inside Barrier", player).connect(
        world.get_region("Hyrule Castle Entrance", player),
        f"{"Castle Town North Inside Barrier"} -> {"Hyrule Castle Entrance"}",
    )

    world.get_region("Castle Town East", player).connect(
        world.get_region("Castle Town Center", player),
        f"{"Castle Town East"} -> {"Castle Town Center"}",
    )

    world.get_region("Castle Town East", player).connect(
        world.get_region("Outside Castle Town East", player),
        f"{"Castle Town East"} -> {"Outside Castle Town East"}",
    )

    world.get_region("Castle Town East", player).connect(
        world.get_region("Castle Town South", player),
        f"{"Castle Town East"} -> {"Castle Town South"}",
    )

    world.get_region("Castle Town East", player).connect(
        world.get_region("Castle Town Doctors Office Left Door", player),
        f"{"Castle Town East"} -> {"Castle Town Doctors Office Left Door"}",
    )

    world.get_region("Castle Town East", player).connect(
        world.get_region("Castle Town Doctors Office Right Door", player),
        f"{"Castle Town East"} -> {"Castle Town Doctors Office Right Door"}",
    )

    world.get_region("Castle Town Doctors Office Balcony", player).connect(
        world.get_region("Castle Town East", player),
        f"{"Castle Town Doctors Office Balcony"} -> {"Castle Town East"}",
    )

    world.get_region("Castle Town Doctors Office Balcony", player).connect(
        world.get_region("Castle Town Doctors Office Upper", player),
        f"{"Castle Town Doctors Office Balcony"} -> {"Castle Town Doctors Office Upper"}",
    )

    world.get_region("Castle Town Doctors Office Left Door", player).connect(
        world.get_region("Castle Town East", player),
        f"{"Castle Town Doctors Office Left Door"} -> {"Castle Town East"}",
    )

    world.get_region("Castle Town Doctors Office Left Door", player).connect(
        world.get_region("Castle Town Doctors Office Entrance", player),
        f"{"Castle Town Doctors Office Left Door"} -> {"Castle Town Doctors Office Entrance"}",
    )

    world.get_region("Castle Town Doctors Office Right Door", player).connect(
        world.get_region("Castle Town East", player),
        f"{"Castle Town Doctors Office Right Door"} -> {"Castle Town East"}",
    )

    world.get_region("Castle Town Doctors Office Right Door", player).connect(
        world.get_region("Castle Town Doctors Office Entrance", player),
        f"{"Castle Town Doctors Office Right Door"} -> {"Castle Town Doctors Office Entrance"}",
    )

    world.get_region("Castle Town Doctors Office Entrance", player).connect(
        world.get_region("Castle Town Doctors Office Left Door", player),
        f"{"Castle Town Doctors Office Entrance"} -> {"Castle Town Doctors Office Left Door"}",
    )

    world.get_region("Castle Town Doctors Office Entrance", player).connect(
        world.get_region("Castle Town Doctors Office Right Door", player),
        f"{"Castle Town Doctors Office Entrance"} -> {"Castle Town Doctors Office Right Door"}",
    )

    world.get_region("Castle Town Doctors Office Entrance", player).connect(
        world.get_region("Castle Town Doctors Office Lower", player),
        f"{"Castle Town Doctors Office Entrance"} -> {"Castle Town Doctors Office Lower"}",
    )

    world.get_region("Castle Town Doctors Office Lower", player).connect(
        world.get_region("Castle Town Doctors Office Entrance", player),
        f"{"Castle Town Doctors Office Lower"} -> {"Castle Town Doctors Office Entrance"}",
    )

    world.get_region("Castle Town Doctors Office Lower", player).connect(
        world.get_region("Castle Town Doctors Office Upper", player),
        f"{"Castle Town Doctors Office Lower"} -> {"Castle Town Doctors Office Upper"}",
    )

    world.get_region("Castle Town Doctors Office Upper", player).connect(
        world.get_region("Castle Town Doctors Office Lower", player),
        f"{"Castle Town Doctors Office Upper"} -> {"Castle Town Doctors Office Lower"}",
    )

    world.get_region("Castle Town Doctors Office Upper", player).connect(
        world.get_region("Castle Town Doctors Office Balcony", player),
        f"{"Castle Town Doctors Office Upper"} -> {"Castle Town Doctors Office Balcony"}",
    )

    world.get_region("Castle Town South", player).connect(
        world.get_region("Castle Town West", player),
        f"{"Castle Town South"} -> {"Castle Town West"}",
    )

    world.get_region("Castle Town South", player).connect(
        world.get_region("Castle Town Center", player),
        f"{"Castle Town South"} -> {"Castle Town Center"}",
    )

    world.get_region("Castle Town South", player).connect(
        world.get_region("Castle Town East", player),
        f"{"Castle Town South"} -> {"Castle Town East"}",
    )

    world.get_region("Castle Town South", player).connect(
        world.get_region("Outside Castle Town South", player),
        f"{"Castle Town South"} -> {"Outside Castle Town South"}",
    )

    world.get_region("Castle Town South", player).connect(
        world.get_region("Castle Town Agithas House", player),
        f"{"Castle Town South"} -> {"Castle Town Agithas House"}",
    )

    world.get_region("Castle Town South", player).connect(
        world.get_region("Castle Town Seer House", player),
        f"{"Castle Town South"} -> {"Castle Town Seer House"}",
    )

    world.get_region("Castle Town South", player).connect(
        world.get_region("Castle Town Jovanis House", player),
        f"{"Castle Town South"} -> {"Castle Town Jovanis House"}",
    )

    world.get_region("Castle Town South", player).connect(
        world.get_region("Castle Town Telmas Bar", player),
        f"{"Castle Town South"} -> {"Castle Town Telmas Bar"}",
    )

    world.get_region("Castle Town Agithas House", player).connect(
        world.get_region("Castle Town South", player),
        f"{"Castle Town Agithas House"} -> {"Castle Town South"}",
    )

    world.get_region("Castle Town Seer House", player).connect(
        world.get_region("Castle Town South", player),
        f"{"Castle Town Seer House"} -> {"Castle Town South"}",
    )

    world.get_region("Castle Town Jovanis House", player).connect(
        world.get_region("Castle Town South", player),
        f"{"Castle Town Jovanis House"} -> {"Castle Town South"}",
    )

    world.get_region("Castle Town Telmas Bar", player).connect(
        world.get_region("Castle Town South", player),
        f"{"Castle Town Telmas Bar"} -> {"Castle Town South"}",
    )

    world.get_region("Lanayru Field", player).connect(
        world.get_region("Lanayru Field Cave Entrance", player),
        f"{"Lanayru Field"} -> {"Lanayru Field Cave Entrance"}",
    )

    world.get_region("Lanayru Field", player).connect(
        world.get_region("Lanayru Field Behind Boulder", player),
        f"{"Lanayru Field"} -> {"Lanayru Field Behind Boulder"}",
    )

    world.get_region("Lanayru Field", player).connect(
        world.get_region("Hyrule Field Near Spinner Rails", player),
        f"{"Lanayru Field"} -> {"Hyrule Field Near Spinner Rails"}",
    )

    world.get_region("Lanayru Field", player).connect(
        world.get_region("North Eldin Field", player),
        f"{"Lanayru Field"} -> {"North Eldin Field"}",
    )

    world.get_region("Lanayru Field", player).connect(
        world.get_region("Outside Castle Town West", player),
        f"{"Lanayru Field"} -> {"Outside Castle Town West"}",
    )

    world.get_region("Lanayru Field", player).connect(
        world.get_region("Lanayru Field Chu Grotto", player),
        f"{"Lanayru Field"} -> {"Lanayru Field Chu Grotto"}",
    )

    world.get_region("Lanayru Field", player).connect(
        world.get_region("Lanayru Field Skulltula Grotto", player),
        f"{"Lanayru Field"} -> {"Lanayru Field Skulltula Grotto"}",
    )

    world.get_region("Lanayru Field", player).connect(
        world.get_region("Lanayru Field Poe Grotto", player),
        f"{"Lanayru Field"} -> {"Lanayru Field Poe Grotto"}",
    )

    world.get_region("Lanayru Field Cave Entrance", player).connect(
        world.get_region("Lanayru Field", player),
        f"{"Lanayru Field Cave Entrance"} -> {"Lanayru Field"}",
    )

    world.get_region("Lanayru Field Cave Entrance", player).connect(
        world.get_region("Lanayru Ice Puzzle Cave", player),
        f"{"Lanayru Field Cave Entrance"} -> {"Lanayru Ice Puzzle Cave"}",
    )

    world.get_region("Lanayru Field Behind Boulder", player).connect(
        world.get_region("Lanayru Field", player),
        f"{"Lanayru Field Behind Boulder"} -> {"Lanayru Field"}",
    )

    world.get_region("Lanayru Field Behind Boulder", player).connect(
        world.get_region("Zoras Domain West Ledge", player),
        f"{"Lanayru Field Behind Boulder"} -> {"Zoras Domain West Ledge"}",
    )

    world.get_region("Hyrule Field Near Spinner Rails", player).connect(
        world.get_region("Lanayru Field", player),
        f"{"Hyrule Field Near Spinner Rails"} -> {"Lanayru Field"}",
    )

    world.get_region("Hyrule Field Near Spinner Rails", player).connect(
        world.get_region("Lake Hylia Bridge", player),
        f"{"Hyrule Field Near Spinner Rails"} -> {"Lake Hylia Bridge"}",
    )

    world.get_region("Lanayru Ice Puzzle Cave", player).connect(
        world.get_region("Lanayru Field Cave Entrance", player),
        f"{"Lanayru Ice Puzzle Cave"} -> {"Lanayru Field Cave Entrance"}",
    )

    world.get_region("Lanayru Field Chu Grotto", player).connect(
        world.get_region("Lanayru Field", player),
        f"{"Lanayru Field Chu Grotto"} -> {"Lanayru Field"}",
    )

    world.get_region("Lanayru Field Skulltula Grotto", player).connect(
        world.get_region("Lanayru Field", player),
        f"{"Lanayru Field Skulltula Grotto"} -> {"Lanayru Field"}",
    )

    world.get_region("Lanayru Field Poe Grotto", player).connect(
        world.get_region("Lanayru Field", player),
        f"{"Lanayru Field Poe Grotto"} -> {"Lanayru Field"}",
    )

    world.get_region("Outside Castle Town West", player).connect(
        world.get_region("Outside Castle Town West Grotto Ledge", player),
        f"{"Outside Castle Town West"} -> {"Outside Castle Town West Grotto Ledge"}",
    )

    world.get_region("Outside Castle Town West", player).connect(
        world.get_region("Lanayru Field", player),
        f"{"Outside Castle Town West"} -> {"Lanayru Field"}",
    )

    world.get_region("Outside Castle Town West", player).connect(
        world.get_region("Castle Town West", player),
        f"{"Outside Castle Town West"} -> {"Castle Town West"}",
    )

    world.get_region("Outside Castle Town West", player).connect(
        world.get_region("Lake Hylia Bridge", player),
        f"{"Outside Castle Town West"} -> {"Lake Hylia Bridge"}",
    )

    world.get_region("Outside Castle Town West Grotto Ledge", player).connect(
        world.get_region("Outside Castle Town West", player),
        f"{"Outside Castle Town West Grotto Ledge"} -> {"Outside Castle Town West"}",
    )

    world.get_region("Outside Castle Town West Grotto Ledge", player).connect(
        world.get_region("Outside Castle Town West Helmasaur Grotto", player),
        f"{"Outside Castle Town West Grotto Ledge"} -> {"Outside Castle Town West Helmasaur Grotto"}",
    )

    world.get_region(
        "Outside Castle Town West Helmasaur Grotto", player
    ).connect(
        world.get_region("Outside Castle Town West Grotto Ledge", player),
        f"{"Outside Castle Town West Helmasaur Grotto"} -> {"Outside Castle Town West Grotto Ledge"}",
    )

    world.get_region("Outside Castle Town East", player).connect(
        world.get_region("Eldin Field Near Castle Town", player),
        f"{"Outside Castle Town East"} -> {"Eldin Field Near Castle Town"}",
    )

    world.get_region("Outside Castle Town East", player).connect(
        world.get_region("Castle Town East", player),
        f"{"Outside Castle Town East"} -> {"Castle Town East"}",
    )

    world.get_region("Outside Castle Town South", player).connect(
        world.get_region("Castle Town South", player),
        f"{"Outside Castle Town South"} -> {"Castle Town South"}",
    )

    world.get_region("Outside Castle Town South", player).connect(
        world.get_region("Faron Field Behind Boulder", player),
        f"{"Outside Castle Town South"} -> {"Faron Field Behind Boulder"}",
    )

    world.get_region("Outside Castle Town South", player).connect(
        world.get_region("Lake Hylia", player),
        f"{"Outside Castle Town South"} -> {"Lake Hylia"}",
    )

    world.get_region("Outside Castle Town South", player).connect(
        world.get_region("Outside Castle Town South Tektite Grotto", player),
        f"{"Outside Castle Town South"} -> {"Outside Castle Town South Tektite Grotto"}",
    )

    world.get_region("Outside Castle Town South Inside Boulder", player).connect(
        world.get_region("Outside Castle Town South", player),
        f"{"Outside Castle Town South Inside Boulder"} -> {"Outside Castle Town South"}",
    )

    world.get_region("Outside Castle Town South Tektite Grotto", player).connect(
        world.get_region("Outside Castle Town South", player),
        f"{"Outside Castle Town South Tektite Grotto"} -> {"Outside Castle Town South"}",
    )

    world.get_region("Lake Hylia Bridge", player).connect(
        world.get_region("Lake Hylia Bridge Grotto Ledge", player),
        f"{"Lake Hylia Bridge"} -> {"Lake Hylia Bridge Grotto Ledge"}",
    )

    world.get_region("Lake Hylia Bridge", player).connect(
        world.get_region("Hyrule Field Near Spinner Rails", player),
        f"{"Lake Hylia Bridge"} -> {"Hyrule Field Near Spinner Rails"}",
    )

    world.get_region("Lake Hylia Bridge", player).connect(
        world.get_region("Outside Castle Town West", player),
        f"{"Lake Hylia Bridge"} -> {"Outside Castle Town West"}",
    )

    world.get_region("Lake Hylia Bridge", player).connect(
        world.get_region("Lake Hylia", player),
        f"{"Lake Hylia Bridge"} -> {"Lake Hylia"}",
    )

    world.get_region("Lake Hylia Bridge", player).connect(
        world.get_region("Faron Field", player),
        f"{"Lake Hylia Bridge"} -> {"Faron Field"}",
    )

    world.get_region("Lake Hylia Bridge Grotto Ledge", player).connect(
        world.get_region("Lake Hylia Bridge", player),
        f"{"Lake Hylia Bridge Grotto Ledge"} -> {"Lake Hylia Bridge"}",
    )

    world.get_region("Lake Hylia Bridge Grotto Ledge", player).connect(
        world.get_region("Lake Hylia Bridge Bubble Grotto", player),
        f"{"Lake Hylia Bridge Grotto Ledge"} -> {"Lake Hylia Bridge Bubble Grotto"}",
    )

    world.get_region("Lake Hylia Bridge Bubble Grotto", player).connect(
        world.get_region("Lake Hylia Bridge Grotto Ledge", player),
        f"{"Lake Hylia Bridge Bubble Grotto"} -> {"Lake Hylia Bridge Grotto Ledge"}",
    )

    world.get_region("Lake Hylia", player).connect(
        world.get_region("Lake Hylia Cave Entrance", player),
        f"{"Lake Hylia"} -> {"Lake Hylia Cave Entrance"}",
    )

    world.get_region("Lake Hylia", player).connect(
        world.get_region("Lake Hylia Lakebed Temple Entrance", player),
        f"{"Lake Hylia"} -> {"Lake Hylia Lakebed Temple Entrance"}",
    )

    world.get_region("Lake Hylia", player).connect(
        world.get_region("Lake Hylia Bridge", player),
        f"{"Lake Hylia"} -> {"Lake Hylia Bridge"}",
    )

    world.get_region("Lake Hylia", player).connect(
        world.get_region("Gerudo Desert", player),
        f"{"Lake Hylia"} -> {"Gerudo Desert"}",
    )

    world.get_region("Lake Hylia", player).connect(
        world.get_region("Upper Zoras River", player),
        f"{"Lake Hylia"} -> {"Upper Zoras River"}",
    )

    world.get_region("Lake Hylia", player).connect(
        world.get_region("Lake Hylia Lanayru Spring", player),
        f"{"Lake Hylia"} -> {"Lake Hylia Lanayru Spring"}",
    )

    world.get_region("Lake Hylia", player).connect(
        world.get_region("Lake Hylia Shell Blade Grotto", player),
        f"{"Lake Hylia"} -> {"Lake Hylia Shell Blade Grotto"}",
    )

    world.get_region("Lake Hylia", player).connect(
        world.get_region("Lake Hylia Water Toadpoli Grotto", player),
        f"{"Lake Hylia"} -> {"Lake Hylia Water Toadpoli Grotto"}",
    )

    world.get_region("Lake Hylia", player).connect(
        world.get_region("City in The Sky Entrance", player),
        f"{"Lake Hylia"} -> {"City in The Sky Entrance"}",
    )

    world.get_region("Lake Hylia Cave Entrance", player).connect(
        world.get_region("Lake Hylia", player),
        f"{"Lake Hylia Cave Entrance"} -> {"Lake Hylia"}",
    )

    world.get_region("Lake Hylia Cave Entrance", player).connect(
        world.get_region("Lake Hylia Long Cave", player),
        f"{"Lake Hylia Cave Entrance"} -> {"Lake Hylia Long Cave"}",
    )

    world.get_region("Lake Hylia Lakebed Temple Entrance", player).connect(
        world.get_region("Lake Hylia", player),
        f"{"Lake Hylia Lakebed Temple Entrance"} -> {"Lake Hylia"}",
    )

    world.get_region("Lake Hylia Lakebed Temple Entrance", player).connect(
        world.get_region("Lakebed Temple Entrance", player),
        f"{"Lake Hylia Lakebed Temple Entrance"} -> {"Lakebed Temple Entrance"}",
    )

    world.get_region("Lake Hylia Lanayru Spring", player).connect(
        world.get_region("Lake Hylia", player),
        f"{"Lake Hylia Lanayru Spring"} -> {"Lake Hylia"}",
    )

    world.get_region("Lake Hylia Long Cave", player).connect(
        world.get_region("Lake Hylia Cave Entrance", player),
        f"{"Lake Hylia Long Cave"} -> {"Lake Hylia Cave Entrance"}",
    )

    world.get_region("Lake Hylia Shell Blade Grotto", player).connect(
        world.get_region("Lake Hylia", player),
        f"{"Lake Hylia Shell Blade Grotto"} -> {"Lake Hylia"}",
    )

    world.get_region("Lake Hylia Water Toadpoli Grotto", player).connect(
        world.get_region("Lake Hylia", player),
        f"{"Lake Hylia Water Toadpoli Grotto"} -> {"Lake Hylia"}",
    )

    world.get_region("Upper Zoras River", player).connect(
        world.get_region("Lanayru Field", player),
        f"{"Upper Zoras River"} -> {"Lanayru Field"}",
    )

    world.get_region("Upper Zoras River", player).connect(
        world.get_region("Fishing Hole", player),
        f"{"Upper Zoras River"} -> {"Fishing Hole"}",
    )

    world.get_region("Upper Zoras River", player).connect(
        world.get_region("Zoras Domain", player),
        f"{"Upper Zoras River"} -> {"Zoras Domain"}",
    )

    world.get_region("Upper Zoras River", player).connect(
        world.get_region("Upper Zoras River Izas House", player),
        f"{"Upper Zoras River"} -> {"Upper Zoras River Izas House"}",
    )

    world.get_region("Upper Zoras River Izas House", player).connect(
        world.get_region("Upper Zoras River", player),
        f"{"Upper Zoras River Izas House"} -> {"Upper Zoras River"}",
    )

    world.get_region("Upper Zoras River Izas House", player).connect(
        world.get_region("Lake Hylia", player),
        f"{"Upper Zoras River Izas House"} -> {"Lake Hylia"}",
    )

    world.get_region("Fishing Hole", player).connect(
        world.get_region("Upper Zoras River", player),
        f"{"Fishing Hole"} -> {"Upper Zoras River"}",
    )

    world.get_region("Fishing Hole", player).connect(
        world.get_region("Fishing Hole House", player),
        f"{"Fishing Hole"} -> {"Fishing Hole House"}",
    )

    world.get_region("Fishing Hole House", player).connect(
        world.get_region("Fishing Hole", player),
        f"{"Fishing Hole House"} -> {"Fishing Hole"}",
    )

    world.get_region("Zoras Domain", player).connect(
        world.get_region("Zoras Domain West Ledge", player),
        f"{"Zoras Domain"} -> {"Zoras Domain West Ledge"}",
    )

    world.get_region("Zoras Domain", player).connect(
        world.get_region("Upper Zoras River", player),
        f"{"Zoras Domain"} -> {"Upper Zoras River"}",
    )

    world.get_region("Zoras Domain", player).connect(
        world.get_region("Zoras Domain Throne Room", player),
        f"{"Zoras Domain"} -> {"Zoras Domain Throne Room"}",
    )

    world.get_region("Zoras Domain", player).connect(
        world.get_region("Snowpeak Climb Lower", player),
        f"{"Zoras Domain"} -> {"Snowpeak Climb Lower"}",
    )

    world.get_region("Zoras Domain West Ledge", player).connect(
        world.get_region("Zoras Domain", player),
        f"{"Zoras Domain West Ledge"} -> {"Zoras Domain"}",
    )

    world.get_region("Zoras Domain West Ledge", player).connect(
        world.get_region("Lanayru Field Behind Boulder", player),
        f"{"Zoras Domain West Ledge"} -> {"Lanayru Field Behind Boulder"}",
    )

    world.get_region("Zoras Domain Throne Room", player).connect(
        world.get_region("Zoras Domain", player),
        f"{"Zoras Domain Throne Room"} -> {"Zoras Domain"}",
    )

    world.get_region("Outside Links House", player).connect(
        world.get_region("Ordon Village", player),
        f"{"Outside Links House"} -> {"Ordon Village"}",
    )

    world.get_region("Outside Links House", player).connect(
        world.get_region("Ordon Spring", player),
        f"{"Outside Links House"} -> {"Ordon Spring"}",
    )

    world.get_region("Outside Links House", player).connect(
        world.get_region("Ordon Links House", player),
        f"{"Outside Links House"} -> {"Ordon Links House"}",
    )

    world.get_region("Ordon Links House", player).connect(
        world.get_region("Outside Links House", player),
        f"{"Ordon Links House"} -> {"Outside Links House"}",
    )

    world.get_region("Ordon Village", player).connect(
        world.get_region("Outside Links House", player),
        f"{"Ordon Village"} -> {"Outside Links House"}",
    )

    world.get_region("Ordon Village", player).connect(
        world.get_region("Ordon Ranch Entrance", player),
        f"{"Ordon Village"} -> {"Ordon Ranch Entrance"}",
    )

    world.get_region("Ordon Village", player).connect(
        world.get_region("Ordon Seras Shop", player),
        f"{"Ordon Village"} -> {"Ordon Seras Shop"}",
    )

    world.get_region("Ordon Village", player).connect(
        world.get_region("Ordon Shield House", player),
        f"{"Ordon Village"} -> {"Ordon Shield House"}",
    )

    world.get_region("Ordon Village", player).connect(
        world.get_region("Ordon Sword House", player),
        f"{"Ordon Village"} -> {"Ordon Sword House"}",
    )

    world.get_region("Ordon Village", player).connect(
        world.get_region("Ordon Bos House Left Door", player),
        f"{"Ordon Village"} -> {"Ordon Bos House Left Door"}",
    )

    world.get_region("Ordon Village", player).connect(
        world.get_region("Ordon Bos House Right Door", player),
        f"{"Ordon Village"} -> {"Ordon Bos House Right Door"}",
    )

    world.get_region("Ordon Seras Shop", player).connect(
        world.get_region("Ordon Village", player),
        f"{"Ordon Seras Shop"} -> {"Ordon Village"}",
    )

    world.get_region("Ordon Shield House", player).connect(
        world.get_region("Ordon Village", player),
        f"{"Ordon Shield House"} -> {"Ordon Village"}",
    )

    world.get_region("Ordon Sword House", player).connect(
        world.get_region("Ordon Village", player),
        f"{"Ordon Sword House"} -> {"Ordon Village"}",
    )

    world.get_region("Ordon Bos House Left Door", player).connect(
        world.get_region("Ordon Village", player),
        f"{"Ordon Bos House Left Door"} -> {"Ordon Village"}",
    )

    world.get_region("Ordon Bos House Left Door", player).connect(
        world.get_region("Ordon Bos House", player),
        f"{"Ordon Bos House Left Door"} -> {"Ordon Bos House"}",
    )

    world.get_region("Ordon Bos House Right Door", player).connect(
        world.get_region("Ordon Village", player),
        f"{"Ordon Bos House Right Door"} -> {"Ordon Village"}",
    )

    world.get_region("Ordon Bos House Right Door", player).connect(
        world.get_region("Ordon Bos House", player),
        f"{"Ordon Bos House Right Door"} -> {"Ordon Bos House"}",
    )

    world.get_region("Ordon Bos House", player).connect(
        world.get_region("Ordon Bos House Left Door", player),
        f"{"Ordon Bos House"} -> {"Ordon Bos House Left Door"}",
    )

    world.get_region("Ordon Bos House", player).connect(
        world.get_region("Ordon Bos House Right Door", player),
        f"{"Ordon Bos House"} -> {"Ordon Bos House Right Door"}",
    )

    world.get_region("Ordon Ranch Entrance", player).connect(
        world.get_region("Ordon Ranch", player),
        f"{"Ordon Ranch Entrance"} -> {"Ordon Ranch"}",
    )

    world.get_region("Ordon Ranch Entrance", player).connect(
        world.get_region("Ordon Village", player),
        f"{"Ordon Ranch Entrance"} -> {"Ordon Village"}",
    )

    world.get_region("Ordon Ranch", player).connect(
        world.get_region("Ordon Ranch Entrance", player),
        f"{"Ordon Ranch"} -> {"Ordon Ranch Entrance"}",
    )

    world.get_region("Ordon Ranch", player).connect(
        world.get_region("Ordon Ranch Stable", player),
        f"{"Ordon Ranch"} -> {"Ordon Ranch Stable"}",
    )

    world.get_region("Ordon Ranch Stable", player).connect(
        world.get_region("Ordon Ranch", player),
        f"{"Ordon Ranch Stable"} -> {"Ordon Ranch"}",
    )

    world.get_region("Ordon Ranch Stable", player).connect(
        world.get_region("Ordon Ranch Grotto", player),
        f"{"Ordon Ranch Stable"} -> {"Ordon Ranch Grotto"}",
    )

    world.get_region("Ordon Ranch Grotto", player).connect(
        world.get_region("Ordon Ranch Stable", player),
        f"{"Ordon Ranch Grotto"} -> {"Ordon Ranch Stable"}",
    )

    world.get_region("Ordon Spring", player).connect(
        world.get_region("Outside Links House", player),
        f"{"Ordon Spring"} -> {"Outside Links House"}",
    )

    world.get_region("Ordon Spring", player).connect(
        world.get_region("Ordon Bridge", player),
        f"{"Ordon Spring"} -> {"Ordon Bridge"}",
    )

    world.get_region("Ordon Bridge", player).connect(
        world.get_region("Ordon Spring", player),
        f"{"Ordon Bridge"} -> {"Ordon Spring"}",
    )

    world.get_region("Ordon Bridge", player).connect(
        world.get_region("South Faron Woods", player),
        f"{"Ordon Bridge"} -> {"South Faron Woods"}",
    )

    world.get_region("Snowpeak Climb Lower", player).connect(
        world.get_region("Snowpeak Climb Upper", player),
        f"{"Snowpeak Climb Lower"} -> {"Snowpeak Climb Upper"}",
    )

    world.get_region("Snowpeak Climb Lower", player).connect(
        world.get_region("Zoras Domain", player),
        f"{"Snowpeak Climb Lower"} -> {"Zoras Domain"}",
    )

    world.get_region("Snowpeak Climb Upper", player).connect(
        world.get_region("Snowpeak Climb Lower", player),
        f"{"Snowpeak Climb Upper"} -> {"Snowpeak Climb Lower"}",
    )

    world.get_region("Snowpeak Climb Upper", player).connect(
        world.get_region("Snowpeak Summit Upper", player),
        f"{"Snowpeak Climb Upper"} -> {"Snowpeak Summit Upper"}",
    )

    world.get_region("Snowpeak Climb Upper", player).connect(
        world.get_region("Snowpeak Ice Keese Grotto", player),
        f"{"Snowpeak Climb Upper"} -> {"Snowpeak Ice Keese Grotto"}",
    )

    world.get_region("Snowpeak Climb Upper", player).connect(
        world.get_region("Snowpeak Freezard Grotto", player),
        f"{"Snowpeak Climb Upper"} -> {"Snowpeak Freezard Grotto"}",
    )

    world.get_region("Snowpeak Ice Keese Grotto", player).connect(
        world.get_region("Snowpeak Climb Upper", player),
        f"{"Snowpeak Ice Keese Grotto"} -> {"Snowpeak Climb Upper"}",
    )

    world.get_region("Snowpeak Freezard Grotto", player).connect(
        world.get_region("Snowpeak Climb Upper", player),
        f"{"Snowpeak Freezard Grotto"} -> {"Snowpeak Climb Upper"}",
    )

    world.get_region("Snowpeak Summit Upper", player).connect(
        world.get_region("Snowpeak Summit Lower", player),
        f"{"Snowpeak Summit Upper"} -> {"Snowpeak Summit Lower"}",
    )

    world.get_region("Snowpeak Summit Upper", player).connect(
        world.get_region("Snowpeak Climb Upper", player),
        f"{"Snowpeak Summit Upper"} -> {"Snowpeak Climb Upper"}",
    )

    world.get_region("Snowpeak Summit Lower", player).connect(
        world.get_region("Snowpeak Ruins Left Door", player),
        f"{"Snowpeak Summit Lower"} -> {"Snowpeak Ruins Left Door"}",
    )

    world.get_region("Snowpeak Summit Lower", player).connect(
        world.get_region("Snowpeak Ruins Right Door", player),
        f"{"Snowpeak Summit Lower"} -> {"Snowpeak Ruins Right Door"}",
    )
