from typing import Dict
from BaseClasses import MultiWorld, Region
from ..Locations import TPLocation, LOCATION_TABLE
from ..options import SkipArbitersGroundsEntrance


def create_regions(world: MultiWorld, player: int) -> Dict[str, Region]:
    regions = {}

    # Create Menu region
    menu = Region("Menu", player, world)
    regions["Menu"] = menu
    world.regions.append(menu)

    arbiters_grounds_entrance = Region("Arbiters Grounds Entrance", player, world)
    regions["Arbiters Grounds Entrance"] = arbiters_grounds_entrance
    world.regions.append(arbiters_grounds_entrance)

    arbiters_grounds_entrance.locations.append(
        TPLocation(
            player,
            "Arbiters Grounds Entrance Chest",
            arbiters_grounds_entrance,
            LOCATION_TABLE["Arbiters Grounds Entrance Chest"],
        )
    )

    arbiters_grounds_lobby = Region("Arbiters Grounds Lobby", player, world)
    regions["Arbiters Grounds Lobby"] = arbiters_grounds_lobby
    world.regions.append(arbiters_grounds_lobby)

    arbiters_grounds_lobby.locations.append(
        TPLocation(
            player,
            "Arbiters Grounds Torch Room East Chest",
            arbiters_grounds_lobby,
            LOCATION_TABLE["Arbiters Grounds Torch Room East Chest"],
        )
    )

    arbiters_grounds_lobby.locations.append(
        TPLocation(
            player,
            "Arbiters Grounds Torch Room West Chest",
            arbiters_grounds_lobby,
            LOCATION_TABLE["Arbiters Grounds Torch Room West Chest"],
        )
    )

    arbiters_grounds_lobby.locations.append(
        TPLocation(
            player,
            "Arbiters Grounds Torch Room Poe",
            arbiters_grounds_lobby,
            LOCATION_TABLE["Arbiters Grounds Torch Room Poe"],
        )
    )

    arbiters_grounds_east_wing = Region("Arbiters Grounds East Wing", player, world)
    regions["Arbiters Grounds East Wing"] = arbiters_grounds_east_wing
    world.regions.append(arbiters_grounds_east_wing)

    arbiters_grounds_east_wing.locations.append(
        TPLocation(
            player,
            "Arbiters Grounds East Lower Turnable Redead Chest",
            arbiters_grounds_east_wing,
            LOCATION_TABLE["Arbiters Grounds East Lower Turnable Redead Chest"],
        )
    )

    arbiters_grounds_east_wing.locations.append(
        TPLocation(
            player,
            "Arbiters Grounds East Upper Turnable Chest",
            arbiters_grounds_east_wing,
            LOCATION_TABLE["Arbiters Grounds East Upper Turnable Chest"],
        )
    )

    arbiters_grounds_east_wing.locations.append(
        TPLocation(
            player,
            "Arbiters Grounds East Upper Turnable Redead Chest",
            arbiters_grounds_east_wing,
            LOCATION_TABLE["Arbiters Grounds East Upper Turnable Redead Chest"],
        )
    )

    arbiters_grounds_east_wing.locations.append(
        TPLocation(
            player,
            "Arbiters Grounds Ghoul Rat Room Chest",
            arbiters_grounds_east_wing,
            LOCATION_TABLE["Arbiters Grounds Ghoul Rat Room Chest"],
        )
    )

    arbiters_grounds_east_wing.locations.append(
        TPLocation(
            player,
            "Arbiters Grounds East Turning Room Poe",
            arbiters_grounds_east_wing,
            LOCATION_TABLE["Arbiters Grounds East Turning Room Poe"],
        )
    )

    arbiters_grounds_east_wing.locations.append(
        TPLocation(
            player,
            "Arbiters Grounds Hidden Wall Poe",
            arbiters_grounds_east_wing,
            LOCATION_TABLE["Arbiters Grounds Hidden Wall Poe"],
        )
    )

    arbiters_grounds_west_wing = Region("Arbiters Grounds West Wing", player, world)
    regions["Arbiters Grounds West Wing"] = arbiters_grounds_west_wing
    world.regions.append(arbiters_grounds_west_wing)

    arbiters_grounds_west_wing.locations.append(
        TPLocation(
            player,
            "Arbiters Grounds West Small Chest Behind Block",
            arbiters_grounds_west_wing,
            LOCATION_TABLE["Arbiters Grounds West Small Chest Behind Block"],
        )
    )

    arbiters_grounds_west_wing.locations.append(
        TPLocation(
            player,
            "Arbiters Grounds West Chandelier Chest",
            arbiters_grounds_west_wing,
            LOCATION_TABLE["Arbiters Grounds West Chandelier Chest"],
        )
    )

    arbiters_grounds_west_wing.locations.append(
        TPLocation(
            player,
            "Arbiters Grounds West Stalfos West Chest",
            arbiters_grounds_west_wing,
            LOCATION_TABLE["Arbiters Grounds West Stalfos West Chest"],
        )
    )

    arbiters_grounds_west_wing.locations.append(
        TPLocation(
            player,
            "Arbiters Grounds West Stalfos Northeast Chest",
            arbiters_grounds_west_wing,
            LOCATION_TABLE["Arbiters Grounds West Stalfos Northeast Chest"],
        )
    )

    arbiters_grounds_west_wing.locations.append(
        TPLocation(
            player,
            "Arbiters Grounds West Poe",
            arbiters_grounds_west_wing,
            LOCATION_TABLE["Arbiters Grounds West Poe"],
        )
    )

    arbiters_grounds_after_poe_gate = Region(
        "Arbiters Grounds After Poe Gate", player, world
    )
    regions["Arbiters Grounds After Poe Gate"] = arbiters_grounds_after_poe_gate
    world.regions.append(arbiters_grounds_after_poe_gate)

    arbiters_grounds_after_poe_gate.locations.append(
        TPLocation(
            player,
            "Arbiters Grounds Big Key Chest",
            arbiters_grounds_after_poe_gate,
            LOCATION_TABLE["Arbiters Grounds Big Key Chest"],
        )
    )

    arbiters_grounds_after_poe_gate.locations.append(
        TPLocation(
            player,
            "Arbiters Grounds North Turning Room Chest",
            arbiters_grounds_after_poe_gate,
            LOCATION_TABLE["Arbiters Grounds North Turning Room Chest"],
        )
    )

    arbiters_grounds_after_poe_gate.locations.append(
        TPLocation(
            player,
            "Arbiters Grounds Death Sword Chest",
            arbiters_grounds_after_poe_gate,
            LOCATION_TABLE["Arbiters Grounds Death Sword Chest"],
        )
    )

    arbiters_grounds_after_poe_gate.locations.append(
        TPLocation(
            player,
            "Arbiters Grounds Spinner Room First Small Chest",
            arbiters_grounds_after_poe_gate,
            LOCATION_TABLE["Arbiters Grounds Spinner Room First Small Chest"],
        )
    )

    arbiters_grounds_after_poe_gate.locations.append(
        TPLocation(
            player,
            "Arbiters Grounds Spinner Room Second Small Chest",
            arbiters_grounds_after_poe_gate,
            LOCATION_TABLE["Arbiters Grounds Spinner Room Second Small Chest"],
        )
    )

    arbiters_grounds_after_poe_gate.locations.append(
        TPLocation(
            player,
            "Arbiters Grounds Spinner Room Lower Central Small Chest",
            arbiters_grounds_after_poe_gate,
            LOCATION_TABLE["Arbiters Grounds Spinner Room Lower Central Small Chest"],
        )
    )

    arbiters_grounds_after_poe_gate.locations.append(
        TPLocation(
            player,
            "Arbiters Grounds Spinner Room Stalfos Alcove Chest",
            arbiters_grounds_after_poe_gate,
            LOCATION_TABLE["Arbiters Grounds Spinner Room Stalfos Alcove Chest"],
        )
    )

    arbiters_grounds_after_poe_gate.locations.append(
        TPLocation(
            player,
            "Arbiters Grounds Spinner Room Lower North Chest",
            arbiters_grounds_after_poe_gate,
            LOCATION_TABLE["Arbiters Grounds Spinner Room Lower North Chest"],
        )
    )

    arbiters_grounds_boss_room = Region("Arbiters Grounds Boss Room", player, world)
    regions["Arbiters Grounds Boss Room"] = arbiters_grounds_boss_room
    world.regions.append(arbiters_grounds_boss_room)

    arbiters_grounds_boss_room.locations.append(
        TPLocation(
            player,
            "Arbiters Grounds Stallord Heart Container",
            arbiters_grounds_boss_room,
            LOCATION_TABLE["Arbiters Grounds Stallord Heart Container"],
        )
    )

    arbiters_grounds_boss_room.locations.append(
        TPLocation(
            player,
            "Arbiters Grounds Dungeon Reward",
            arbiters_grounds_boss_room,
            LOCATION_TABLE["Arbiters Grounds Dungeon Reward"],
        )
    )

    arbiters_grounds_boss_room.locations.append(
        TPLocation(
            player,
            "Arbiters Grounds Stallord",
            arbiters_grounds_boss_room,
            LOCATION_TABLE["Arbiters Grounds Stallord"],
        )
    )

    city_in_the_sky_boss_room = Region("City in The Sky Boss Room", player, world)
    regions["City in The Sky Boss Room"] = city_in_the_sky_boss_room
    world.regions.append(city_in_the_sky_boss_room)

    city_in_the_sky_boss_room.locations.append(
        TPLocation(
            player,
            "City in The Sky Argorok Heart Container",
            city_in_the_sky_boss_room,
            LOCATION_TABLE["City in The Sky Argorok Heart Container"],
        )
    )

    city_in_the_sky_boss_room.locations.append(
        TPLocation(
            player,
            "City in The Sky Dungeon Reward",
            city_in_the_sky_boss_room,
            LOCATION_TABLE["City in The Sky Dungeon Reward"],
        )
    )

    city_in_the_sky_boss_room.locations.append(
        TPLocation(
            player,
            "City in The Sky Argorok",
            city_in_the_sky_boss_room,
            LOCATION_TABLE["City in The Sky Argorok"],
        )
    )

    city_in_the_sky_central_tower_second_floor = Region(
        "City in The Sky Central Tower Second Floor", player, world
    )
    regions["City in The Sky Central Tower Second Floor"] = (
        city_in_the_sky_central_tower_second_floor
    )
    world.regions.append(city_in_the_sky_central_tower_second_floor)

    city_in_the_sky_central_tower_second_floor.locations.append(
        TPLocation(
            player,
            "City in The Sky Central Outside Ledge Chest",
            city_in_the_sky_central_tower_second_floor,
            LOCATION_TABLE["City in The Sky Central Outside Ledge Chest"],
        )
    )

    city_in_the_sky_central_tower_second_floor.locations.append(
        TPLocation(
            player,
            "City in The Sky Central Outside Poe Island Chest",
            city_in_the_sky_central_tower_second_floor,
            LOCATION_TABLE["City in The Sky Central Outside Poe Island Chest"],
        )
    )

    city_in_the_sky_central_tower_second_floor.locations.append(
        TPLocation(
            player,
            "City in The Sky Big Key Chest",
            city_in_the_sky_central_tower_second_floor,
            LOCATION_TABLE["City in The Sky Big Key Chest"],
        )
    )

    city_in_the_sky_central_tower_second_floor.locations.append(
        TPLocation(
            player,
            "City in The Sky Chest Below Big Key Chest",
            city_in_the_sky_central_tower_second_floor,
            LOCATION_TABLE["City in The Sky Chest Below Big Key Chest"],
        )
    )

    city_in_the_sky_central_tower_second_floor.locations.append(
        TPLocation(
            player,
            "City in The Sky Poe Above Central Fan",
            city_in_the_sky_central_tower_second_floor,
            LOCATION_TABLE["City in The Sky Poe Above Central Fan"],
        )
    )

    city_in_the_sky_east_wing = Region("City in The Sky East Wing", player, world)
    regions["City in The Sky East Wing"] = city_in_the_sky_east_wing
    world.regions.append(city_in_the_sky_east_wing)

    city_in_the_sky_east_wing.locations.append(
        TPLocation(
            player,
            "City in The Sky East First Wing Chest After Fans",
            city_in_the_sky_east_wing,
            LOCATION_TABLE["City in The Sky East First Wing Chest After Fans"],
        )
    )

    city_in_the_sky_east_wing.locations.append(
        TPLocation(
            player,
            "City in The Sky East Wing Lower Level Chest",
            city_in_the_sky_east_wing,
            LOCATION_TABLE["City in The Sky East Wing Lower Level Chest"],
        )
    )

    city_in_the_sky_east_wing.locations.append(
        TPLocation(
            player,
            "City in The Sky East Tile Worm Small Chest",
            city_in_the_sky_east_wing,
            LOCATION_TABLE["City in The Sky East Tile Worm Small Chest"],
        )
    )

    city_in_the_sky_east_wing.locations.append(
        TPLocation(
            player,
            "City in The Sky East Wing After Dinalfos Alcove Chest",
            city_in_the_sky_east_wing,
            LOCATION_TABLE["City in The Sky East Wing After Dinalfos Alcove Chest"],
        )
    )

    city_in_the_sky_east_wing.locations.append(
        TPLocation(
            player,
            "City in The Sky East Wing After Dinalfos Ledge Chest",
            city_in_the_sky_east_wing,
            LOCATION_TABLE["City in The Sky East Wing After Dinalfos Ledge Chest"],
        )
    )

    city_in_the_sky_east_wing.locations.append(
        TPLocation(
            player,
            "City in The Sky Aeralfos Chest",
            city_in_the_sky_east_wing,
            LOCATION_TABLE["City in The Sky Aeralfos Chest"],
        )
    )

    city_in_the_sky_entrance = Region("City in The Sky Entrance", player, world)
    regions["City in The Sky Entrance"] = city_in_the_sky_entrance
    world.regions.append(city_in_the_sky_entrance)

    city_in_the_sky_entrance.locations.append(
        TPLocation(
            player,
            "City in The Sky Underwater West Chest",
            city_in_the_sky_entrance,
            LOCATION_TABLE["City in The Sky Underwater West Chest"],
        )
    )

    city_in_the_sky_entrance.locations.append(
        TPLocation(
            player,
            "City in The Sky Underwater East Chest",
            city_in_the_sky_entrance,
            LOCATION_TABLE["City in The Sky Underwater East Chest"],
        )
    )

    city_in_the_sky_lobby = Region("City in The Sky Lobby", player, world)
    regions["City in The Sky Lobby"] = city_in_the_sky_lobby
    world.regions.append(city_in_the_sky_lobby)

    city_in_the_sky_north_wing = Region("City in The Sky North Wing", player, world)
    regions["City in The Sky North Wing"] = city_in_the_sky_north_wing
    world.regions.append(city_in_the_sky_north_wing)

    city_in_the_sky_north_wing.locations.append(
        TPLocation(
            player,
            "City in The Sky Chest Behind North Fan",
            city_in_the_sky_north_wing,
            LOCATION_TABLE["City in The Sky Chest Behind North Fan"],
        )
    )

    city_in_the_sky_west_wing = Region("City in The Sky West Wing", player, world)
    regions["City in The Sky West Wing"] = city_in_the_sky_west_wing
    world.regions.append(city_in_the_sky_west_wing)

    city_in_the_sky_west_wing.locations.append(
        TPLocation(
            player,
            "City in The Sky West Wing First Chest",
            city_in_the_sky_west_wing,
            LOCATION_TABLE["City in The Sky West Wing First Chest"],
        )
    )

    city_in_the_sky_west_wing.locations.append(
        TPLocation(
            player,
            "City in The Sky West Wing Baba Balcony Chest",
            city_in_the_sky_west_wing,
            LOCATION_TABLE["City in The Sky West Wing Baba Balcony Chest"],
        )
    )

    city_in_the_sky_west_wing.locations.append(
        TPLocation(
            player,
            "City in The Sky West Wing Narrow Ledge Chest",
            city_in_the_sky_west_wing,
            LOCATION_TABLE["City in The Sky West Wing Narrow Ledge Chest"],
        )
    )

    city_in_the_sky_west_wing.locations.append(
        TPLocation(
            player,
            "City in The Sky West Wing Tile Worm Chest",
            city_in_the_sky_west_wing,
            LOCATION_TABLE["City in The Sky West Wing Tile Worm Chest"],
        )
    )

    city_in_the_sky_west_wing.locations.append(
        TPLocation(
            player,
            "City in The Sky Baba Tower Top Small Chest",
            city_in_the_sky_west_wing,
            LOCATION_TABLE["City in The Sky Baba Tower Top Small Chest"],
        )
    )

    city_in_the_sky_west_wing.locations.append(
        TPLocation(
            player,
            "City in The Sky Baba Tower Narrow Ledge Chest",
            city_in_the_sky_west_wing,
            LOCATION_TABLE["City in The Sky Baba Tower Narrow Ledge Chest"],
        )
    )

    city_in_the_sky_west_wing.locations.append(
        TPLocation(
            player,
            "City in The Sky Baba Tower Alcove Chest",
            city_in_the_sky_west_wing,
            LOCATION_TABLE["City in The Sky Baba Tower Alcove Chest"],
        )
    )

    city_in_the_sky_west_wing.locations.append(
        TPLocation(
            player,
            "City in The Sky West Garden Corner Chest",
            city_in_the_sky_west_wing,
            LOCATION_TABLE["City in The Sky West Garden Corner Chest"],
        )
    )

    city_in_the_sky_west_wing.locations.append(
        TPLocation(
            player,
            "City in The Sky West Garden Lone Island Chest",
            city_in_the_sky_west_wing,
            LOCATION_TABLE["City in The Sky West Garden Lone Island Chest"],
        )
    )

    city_in_the_sky_west_wing.locations.append(
        TPLocation(
            player,
            "City in The Sky West Garden Lower Chest",
            city_in_the_sky_west_wing,
            LOCATION_TABLE["City in The Sky West Garden Lower Chest"],
        )
    )

    city_in_the_sky_west_wing.locations.append(
        TPLocation(
            player,
            "City in The Sky West Garden Ledge Chest",
            city_in_the_sky_west_wing,
            LOCATION_TABLE["City in The Sky West Garden Ledge Chest"],
        )
    )

    city_in_the_sky_west_wing.locations.append(
        TPLocation(
            player,
            "City in The Sky Garden Island Poe",
            city_in_the_sky_west_wing,
            LOCATION_TABLE["City in The Sky Garden Island Poe"],
        )
    )

    forest_temple_boss_room = Region("Forest Temple Boss Room", player, world)
    regions["Forest Temple Boss Room"] = forest_temple_boss_room
    world.regions.append(forest_temple_boss_room)

    forest_temple_boss_room.locations.append(
        TPLocation(
            player,
            "Forest Temple Diababa Heart Container",
            forest_temple_boss_room,
            LOCATION_TABLE["Forest Temple Diababa Heart Container"],
        )
    )

    forest_temple_boss_room.locations.append(
        TPLocation(
            player,
            "Forest Temple Dungeon Reward",
            forest_temple_boss_room,
            LOCATION_TABLE["Forest Temple Dungeon Reward"],
        )
    )

    forest_temple_boss_room.locations.append(
        TPLocation(
            player,
            "Forest Temple Diababa",
            forest_temple_boss_room,
            LOCATION_TABLE["Forest Temple Diababa"],
        )
    )

    forest_temple_east_wing = Region("Forest Temple East Wing", player, world)
    regions["Forest Temple East Wing"] = forest_temple_east_wing
    world.regions.append(forest_temple_east_wing)

    forest_temple_east_wing.locations.append(
        TPLocation(
            player,
            "Forest Temple Second Monkey Under Bridge Chest",
            forest_temple_east_wing,
            LOCATION_TABLE["Forest Temple Second Monkey Under Bridge Chest"],
        )
    )

    forest_temple_east_wing.locations.append(
        TPLocation(
            player,
            "Forest Temple Big Key Chest",
            forest_temple_east_wing,
            LOCATION_TABLE["Forest Temple Big Key Chest"],
        )
    )

    forest_temple_east_wing.locations.append(
        TPLocation(
            player,
            "Forest Temple East Water Cave Chest",
            forest_temple_east_wing,
            LOCATION_TABLE["Forest Temple East Water Cave Chest"],
        )
    )

    forest_temple_entrance = Region("Forest Temple Entrance", player, world)
    regions["Forest Temple Entrance"] = forest_temple_entrance
    world.regions.append(forest_temple_entrance)

    forest_temple_entrance.locations.append(
        TPLocation(
            player,
            "Forest Temple Entrance Vines Chest",
            forest_temple_entrance,
            LOCATION_TABLE["Forest Temple Entrance Vines Chest"],
        )
    )

    forest_temple_lobby = Region("Forest Temple Lobby", player, world)
    regions["Forest Temple Lobby"] = forest_temple_lobby
    world.regions.append(forest_temple_lobby)

    forest_temple_lobby.locations.append(
        TPLocation(
            player,
            "Forest Temple Central Chest Behind Stairs",
            forest_temple_lobby,
            LOCATION_TABLE["Forest Temple Central Chest Behind Stairs"],
        )
    )

    forest_temple_lobby.locations.append(
        TPLocation(
            player,
            "Forest Temple Central North Chest",
            forest_temple_lobby,
            LOCATION_TABLE["Forest Temple Central North Chest"],
        )
    )

    forest_temple_lobby.locations.append(
        TPLocation(
            player,
            "Forest Temple Central Chest Hanging From Web",
            forest_temple_lobby,
            LOCATION_TABLE["Forest Temple Central Chest Hanging From Web"],
        )
    )

    forest_temple_north_wing = Region("Forest Temple North Wing", player, world)
    regions["Forest Temple North Wing"] = forest_temple_north_wing
    world.regions.append(forest_temple_north_wing)

    forest_temple_north_wing.locations.append(
        TPLocation(
            player,
            "Forest Temple Windless Bridge Chest",
            forest_temple_north_wing,
            LOCATION_TABLE["Forest Temple Windless Bridge Chest"],
        )
    )

    forest_temple_north_wing.locations.append(
        TPLocation(
            player,
            "Forest Temple North Deku Like Chest",
            forest_temple_north_wing,
            LOCATION_TABLE["Forest Temple North Deku Like Chest"],
        )
    )

    forest_temple_north_wing.locations.append(
        TPLocation(
            player,
            "Forest Temple East Tile Worm Chest",
            forest_temple_north_wing,
            LOCATION_TABLE["Forest Temple East Tile Worm Chest"],
        )
    )

    forest_temple_west_wing = Region("Forest Temple West Wing", player, world)
    regions["Forest Temple West Wing"] = forest_temple_west_wing
    world.regions.append(forest_temple_west_wing)

    forest_temple_west_wing.locations.append(
        TPLocation(
            player,
            "Forest Temple West Deku Like Chest",
            forest_temple_west_wing,
            LOCATION_TABLE["Forest Temple West Deku Like Chest"],
        )
    )

    forest_temple_west_wing.locations.append(
        TPLocation(
            player,
            "Forest Temple Totem Pole Chest",
            forest_temple_west_wing,
            LOCATION_TABLE["Forest Temple Totem Pole Chest"],
        )
    )

    forest_temple_west_wing.locations.append(
        TPLocation(
            player,
            "Forest Temple West Tile Worm Room Vines Chest",
            forest_temple_west_wing,
            LOCATION_TABLE["Forest Temple West Tile Worm Room Vines Chest"],
        )
    )

    forest_temple_west_wing.locations.append(
        TPLocation(
            player,
            "Forest Temple West Tile Worm Chest Behind Stairs",
            forest_temple_west_wing,
            LOCATION_TABLE["Forest Temple West Tile Worm Chest Behind Stairs"],
        )
    )

    forest_temple_west_wing.locations.append(
        TPLocation(
            player,
            "Forest Temple Big Baba Key",
            forest_temple_west_wing,
            LOCATION_TABLE["Forest Temple Big Baba Key"],
        )
    )

    ook = Region("Ook", player, world)
    regions["Ook"] = ook
    world.regions.append(ook)

    ook.locations.append(
        TPLocation(
            player,
            "Forest Temple Gale Boomerang",
            ook,
            LOCATION_TABLE["Forest Temple Gale Boomerang"],
        )
    )

    goron_mines_boss_room = Region("Goron Mines Boss Room", player, world)
    regions["Goron Mines Boss Room"] = goron_mines_boss_room
    world.regions.append(goron_mines_boss_room)

    goron_mines_boss_room.locations.append(
        TPLocation(
            player,
            "Goron Mines Fyrus Heart Container",
            goron_mines_boss_room,
            LOCATION_TABLE["Goron Mines Fyrus Heart Container"],
        )
    )

    goron_mines_boss_room.locations.append(
        TPLocation(
            player,
            "Goron Mines Dungeon Reward",
            goron_mines_boss_room,
            LOCATION_TABLE["Goron Mines Dungeon Reward"],
        )
    )

    goron_mines_boss_room.locations.append(
        TPLocation(
            player,
            "Goron Mines Fyrus",
            goron_mines_boss_room,
            LOCATION_TABLE["Goron Mines Fyrus"],
        )
    )

    goron_mines_crystal_switch_room = Region(
        "Goron Mines Crystal Switch Room", player, world
    )
    regions["Goron Mines Crystal Switch Room"] = goron_mines_crystal_switch_room
    world.regions.append(goron_mines_crystal_switch_room)

    goron_mines_crystal_switch_room.locations.append(
        TPLocation(
            player,
            "Goron Mines Crystal Switch Room Underwater Chest",
            goron_mines_crystal_switch_room,
            LOCATION_TABLE["Goron Mines Crystal Switch Room Underwater Chest"],
        )
    )

    goron_mines_crystal_switch_room.locations.append(
        TPLocation(
            player,
            "Goron Mines Crystal Switch Room Small Chest",
            goron_mines_crystal_switch_room,
            LOCATION_TABLE["Goron Mines Crystal Switch Room Small Chest"],
        )
    )

    goron_mines_crystal_switch_room.locations.append(
        TPLocation(
            player,
            "Goron Mines After Crystal Switch Room Magnet Wall Chest",
            goron_mines_crystal_switch_room,
            LOCATION_TABLE["Goron Mines After Crystal Switch Room Magnet Wall Chest"],
        )
    )

    goron_mines_entrance = Region("Goron Mines Entrance", player, world)
    regions["Goron Mines Entrance"] = goron_mines_entrance
    world.regions.append(goron_mines_entrance)

    goron_mines_entrance.locations.append(
        TPLocation(
            player,
            "Goron Mines Entrance Chest",
            goron_mines_entrance,
            LOCATION_TABLE["Goron Mines Entrance Chest"],
        )
    )

    goron_mines_lower_west_wing = Region("Goron Mines Lower West Wing", player, world)
    regions["Goron Mines Lower West Wing"] = goron_mines_lower_west_wing
    world.regions.append(goron_mines_lower_west_wing)

    goron_mines_lower_west_wing.locations.append(
        TPLocation(
            player,
            "Goron Mines Magnet Maze Chest",
            goron_mines_lower_west_wing,
            LOCATION_TABLE["Goron Mines Magnet Maze Chest"],
        )
    )

    goron_mines_lower_west_wing.locations.append(
        TPLocation(
            player,
            "Goron Mines Gor Amato Chest",
            goron_mines_lower_west_wing,
            LOCATION_TABLE["Goron Mines Gor Amato Chest"],
        )
    )

    goron_mines_lower_west_wing.locations.append(
        TPLocation(
            player,
            "Goron Mines Gor Amato Small Chest",
            goron_mines_lower_west_wing,
            LOCATION_TABLE["Goron Mines Gor Amato Small Chest"],
        )
    )

    goron_mines_lower_west_wing.locations.append(
        TPLocation(
            player,
            "Goron Mines Gor Amato Key Shard",
            goron_mines_lower_west_wing,
            LOCATION_TABLE["Goron Mines Gor Amato Key Shard"],
        )
    )

    goron_mines_magnet_room = Region("Goron Mines Magnet Room", player, world)
    regions["Goron Mines Magnet Room"] = goron_mines_magnet_room
    world.regions.append(goron_mines_magnet_room)

    goron_mines_magnet_room.locations.append(
        TPLocation(
            player,
            "Goron Mines Main Magnet Room Bottom Chest",
            goron_mines_magnet_room,
            LOCATION_TABLE["Goron Mines Main Magnet Room Bottom Chest"],
        )
    )

    goron_mines_magnet_room.locations.append(
        TPLocation(
            player,
            "Goron Mines Main Magnet Room Top Chest",
            goron_mines_magnet_room,
            LOCATION_TABLE["Goron Mines Main Magnet Room Top Chest"],
        )
    )

    goron_mines_north_wing = Region("Goron Mines North Wing", player, world)
    regions["Goron Mines North Wing"] = goron_mines_north_wing
    world.regions.append(goron_mines_north_wing)

    goron_mines_north_wing.locations.append(
        TPLocation(
            player,
            "Goron Mines Outside Beamos Chest",
            goron_mines_north_wing,
            LOCATION_TABLE["Goron Mines Outside Beamos Chest"],
        )
    )

    goron_mines_north_wing.locations.append(
        TPLocation(
            player,
            "Goron Mines Outside Underwater Chest",
            goron_mines_north_wing,
            LOCATION_TABLE["Goron Mines Outside Underwater Chest"],
        )
    )

    goron_mines_north_wing.locations.append(
        TPLocation(
            player,
            "Goron Mines Outside Clawshot Chest",
            goron_mines_north_wing,
            LOCATION_TABLE["Goron Mines Outside Clawshot Chest"],
        )
    )

    goron_mines_upper_east_wing = Region("Goron Mines Upper East Wing", player, world)
    regions["Goron Mines Upper East Wing"] = goron_mines_upper_east_wing
    world.regions.append(goron_mines_upper_east_wing)

    goron_mines_upper_east_wing.locations.append(
        TPLocation(
            player,
            "Goron Mines Gor Ebizo Chest",
            goron_mines_upper_east_wing,
            LOCATION_TABLE["Goron Mines Gor Ebizo Chest"],
        )
    )

    goron_mines_upper_east_wing.locations.append(
        TPLocation(
            player,
            "Goron Mines Chest Before Dangoro",
            goron_mines_upper_east_wing,
            LOCATION_TABLE["Goron Mines Chest Before Dangoro"],
        )
    )

    goron_mines_upper_east_wing.locations.append(
        TPLocation(
            player,
            "Goron Mines Gor Ebizo Key Shard",
            goron_mines_upper_east_wing,
            LOCATION_TABLE["Goron Mines Gor Ebizo Key Shard"],
        )
    )

    goron_mines_upper_east_wing.locations.append(
        TPLocation(
            player,
            "Goron Mines Dangoro Chest",
            goron_mines_upper_east_wing,
            LOCATION_TABLE["Goron Mines Dangoro Chest"],
        )
    )

    goron_mines_upper_east_wing.locations.append(
        TPLocation(
            player,
            "Goron Mines Beamos Room Chest",
            goron_mines_upper_east_wing,
            LOCATION_TABLE["Goron Mines Beamos Room Chest"],
        )
    )

    goron_mines_upper_east_wing.locations.append(
        TPLocation(
            player,
            "Goron Mines Gor Liggs Chest",
            goron_mines_upper_east_wing,
            LOCATION_TABLE["Goron Mines Gor Liggs Chest"],
        )
    )

    goron_mines_upper_east_wing.locations.append(
        TPLocation(
            player,
            "Goron Mines Gor Liggs Key Shard",
            goron_mines_upper_east_wing,
            LOCATION_TABLE["Goron Mines Gor Liggs Key Shard"],
        )
    )

    ganondorf_castle = Region("Ganondorf Castle", player, world)
    regions["Ganondorf Castle"] = ganondorf_castle
    world.regions.append(ganondorf_castle)

    ganondorf_castle.locations.append(
        TPLocation(
            player,
            "Hyrule Castle Ganondorf",
            ganondorf_castle,
            LOCATION_TABLE["Hyrule Castle Ganondorf"],
        )
    )

    hyrule_castle_entrance = Region("Hyrule Castle Entrance", player, world)
    regions["Hyrule Castle Entrance"] = hyrule_castle_entrance
    world.regions.append(hyrule_castle_entrance)

    hyrule_castle_graveyard = Region("Hyrule Castle Graveyard", player, world)
    regions["Hyrule Castle Graveyard"] = hyrule_castle_graveyard
    world.regions.append(hyrule_castle_graveyard)

    hyrule_castle_graveyard.locations.append(
        TPLocation(
            player,
            "Hyrule Castle Graveyard Grave Switch Room Right Chest",
            hyrule_castle_graveyard,
            LOCATION_TABLE["Hyrule Castle Graveyard Grave Switch Room Right Chest"],
        )
    )

    hyrule_castle_graveyard.locations.append(
        TPLocation(
            player,
            "Hyrule Castle Graveyard Grave Switch Room Front Left Chest",
            hyrule_castle_graveyard,
            LOCATION_TABLE[
                "Hyrule Castle Graveyard Grave Switch Room Front Left Chest"
            ],
        )
    )

    hyrule_castle_graveyard.locations.append(
        TPLocation(
            player,
            "Hyrule Castle Graveyard Grave Switch Room Back Left Chest",
            hyrule_castle_graveyard,
            LOCATION_TABLE["Hyrule Castle Graveyard Grave Switch Room Back Left Chest"],
        )
    )

    hyrule_castle_graveyard.locations.append(
        TPLocation(
            player,
            "Hyrule Castle Graveyard Owl Statue Chest",
            hyrule_castle_graveyard,
            LOCATION_TABLE["Hyrule Castle Graveyard Owl Statue Chest"],
        )
    )

    hyrule_castle_inside_east_wing = Region(
        "Hyrule Castle Inside East Wing", player, world
    )
    regions["Hyrule Castle Inside East Wing"] = hyrule_castle_inside_east_wing
    world.regions.append(hyrule_castle_inside_east_wing)

    hyrule_castle_inside_west_wing = Region(
        "Hyrule Castle Inside West Wing", player, world
    )
    regions["Hyrule Castle Inside West Wing"] = hyrule_castle_inside_west_wing
    world.regions.append(hyrule_castle_inside_west_wing)

    hyrule_castle_main_hall = Region("Hyrule Castle Main Hall", player, world)
    regions["Hyrule Castle Main Hall"] = hyrule_castle_main_hall
    world.regions.append(hyrule_castle_main_hall)

    hyrule_castle_main_hall.locations.append(
        TPLocation(
            player,
            "Hyrule Castle Main Hall Northeast Chest",
            hyrule_castle_main_hall,
            LOCATION_TABLE["Hyrule Castle Main Hall Northeast Chest"],
        )
    )

    hyrule_castle_main_hall.locations.append(
        TPLocation(
            player,
            "Hyrule Castle Main Hall Southwest Chest",
            hyrule_castle_main_hall,
            LOCATION_TABLE["Hyrule Castle Main Hall Southwest Chest"],
        )
    )

    hyrule_castle_main_hall.locations.append(
        TPLocation(
            player,
            "Hyrule Castle Main Hall Northwest Chest",
            hyrule_castle_main_hall,
            LOCATION_TABLE["Hyrule Castle Main Hall Northwest Chest"],
        )
    )

    hyrule_castle_main_hall.locations.append(
        TPLocation(
            player,
            "Hyrule Castle Lantern Staircase Chest",
            hyrule_castle_main_hall,
            LOCATION_TABLE["Hyrule Castle Lantern Staircase Chest"],
        )
    )

    hyrule_castle_outside_east_wing = Region(
        "Hyrule Castle Outside East Wing", player, world
    )
    regions["Hyrule Castle Outside East Wing"] = hyrule_castle_outside_east_wing
    world.regions.append(hyrule_castle_outside_east_wing)

    hyrule_castle_outside_east_wing.locations.append(
        TPLocation(
            player,
            "Hyrule Castle East Wing Boomerang Puzzle Chest",
            hyrule_castle_outside_east_wing,
            LOCATION_TABLE["Hyrule Castle East Wing Boomerang Puzzle Chest"],
        )
    )

    hyrule_castle_outside_east_wing.locations.append(
        TPLocation(
            player,
            "Hyrule Castle East Wing Balcony Chest",
            hyrule_castle_outside_east_wing,
            LOCATION_TABLE["Hyrule Castle East Wing Balcony Chest"],
        )
    )

    hyrule_castle_outside_west_wing = Region(
        "Hyrule Castle Outside West Wing", player, world
    )
    regions["Hyrule Castle Outside West Wing"] = hyrule_castle_outside_west_wing
    world.regions.append(hyrule_castle_outside_west_wing)

    hyrule_castle_outside_west_wing.locations.append(
        TPLocation(
            player,
            "Hyrule Castle West Courtyard North Small Chest",
            hyrule_castle_outside_west_wing,
            LOCATION_TABLE["Hyrule Castle West Courtyard North Small Chest"],
        )
    )

    hyrule_castle_outside_west_wing.locations.append(
        TPLocation(
            player,
            "Hyrule Castle West Courtyard Central Small Chest",
            hyrule_castle_outside_west_wing,
            LOCATION_TABLE["Hyrule Castle West Courtyard Central Small Chest"],
        )
    )

    hyrule_castle_outside_west_wing.locations.append(
        TPLocation(
            player,
            "Hyrule Castle King Bulblin Key",
            hyrule_castle_outside_west_wing,
            LOCATION_TABLE["Hyrule Castle King Bulblin Key"],
        )
    )

    hyrule_castle_third_floor_balcony = Region(
        "Hyrule Castle Third Floor Balcony", player, world
    )
    regions["Hyrule Castle Third Floor Balcony"] = hyrule_castle_third_floor_balcony
    world.regions.append(hyrule_castle_third_floor_balcony)

    hyrule_castle_third_floor_balcony.locations.append(
        TPLocation(
            player,
            "Hyrule Castle Southeast Balcony Tower Chest",
            hyrule_castle_third_floor_balcony,
            LOCATION_TABLE["Hyrule Castle Southeast Balcony Tower Chest"],
        )
    )

    hyrule_castle_third_floor_balcony.locations.append(
        TPLocation(
            player,
            "Hyrule Castle Big Key Chest",
            hyrule_castle_third_floor_balcony,
            LOCATION_TABLE["Hyrule Castle Big Key Chest"],
        )
    )

    hyrule_castle_tower_climb = Region("Hyrule Castle Tower Climb", player, world)
    regions["Hyrule Castle Tower Climb"] = hyrule_castle_tower_climb
    world.regions.append(hyrule_castle_tower_climb)

    hyrule_castle_treasure_room = Region("Hyrule Castle Treasure Room", player, world)
    regions["Hyrule Castle Treasure Room"] = hyrule_castle_treasure_room
    world.regions.append(hyrule_castle_treasure_room)

    hyrule_castle_treasure_room.locations.append(
        TPLocation(
            player,
            "Hyrule Castle Treasure Room Eighth Small Chest",
            hyrule_castle_treasure_room,
            LOCATION_TABLE["Hyrule Castle Treasure Room Eighth Small Chest"],
        )
    )

    hyrule_castle_treasure_room.locations.append(
        TPLocation(
            player,
            "Hyrule Castle Treasure Room Seventh Small Chest",
            hyrule_castle_treasure_room,
            LOCATION_TABLE["Hyrule Castle Treasure Room Seventh Small Chest"],
        )
    )

    hyrule_castle_treasure_room.locations.append(
        TPLocation(
            player,
            "Hyrule Castle Treasure Room Sixth Small Chest",
            hyrule_castle_treasure_room,
            LOCATION_TABLE["Hyrule Castle Treasure Room Sixth Small Chest"],
        )
    )

    hyrule_castle_treasure_room.locations.append(
        TPLocation(
            player,
            "Hyrule Castle Treasure Room Fifth Small Chest",
            hyrule_castle_treasure_room,
            LOCATION_TABLE["Hyrule Castle Treasure Room Fifth Small Chest"],
        )
    )

    hyrule_castle_treasure_room.locations.append(
        TPLocation(
            player,
            "Hyrule Castle Treasure Room Fourth Small Chest",
            hyrule_castle_treasure_room,
            LOCATION_TABLE["Hyrule Castle Treasure Room Fourth Small Chest"],
        )
    )

    hyrule_castle_treasure_room.locations.append(
        TPLocation(
            player,
            "Hyrule Castle Treasure Room Third Small Chest",
            hyrule_castle_treasure_room,
            LOCATION_TABLE["Hyrule Castle Treasure Room Third Small Chest"],
        )
    )

    hyrule_castle_treasure_room.locations.append(
        TPLocation(
            player,
            "Hyrule Castle Treasure Room Second Small Chest",
            hyrule_castle_treasure_room,
            LOCATION_TABLE["Hyrule Castle Treasure Room Second Small Chest"],
        )
    )

    hyrule_castle_treasure_room.locations.append(
        TPLocation(
            player,
            "Hyrule Castle Treasure Room First Small Chest",
            hyrule_castle_treasure_room,
            LOCATION_TABLE["Hyrule Castle Treasure Room First Small Chest"],
        )
    )

    hyrule_castle_treasure_room.locations.append(
        TPLocation(
            player,
            "Hyrule Castle Treasure Room Fifth Chest",
            hyrule_castle_treasure_room,
            LOCATION_TABLE["Hyrule Castle Treasure Room Fifth Chest"],
        )
    )

    hyrule_castle_treasure_room.locations.append(
        TPLocation(
            player,
            "Hyrule Castle Treasure Room Fourth Chest",
            hyrule_castle_treasure_room,
            LOCATION_TABLE["Hyrule Castle Treasure Room Fourth Chest"],
        )
    )

    hyrule_castle_treasure_room.locations.append(
        TPLocation(
            player,
            "Hyrule Castle Treasure Room Third Chest",
            hyrule_castle_treasure_room,
            LOCATION_TABLE["Hyrule Castle Treasure Room Third Chest"],
        )
    )

    hyrule_castle_treasure_room.locations.append(
        TPLocation(
            player,
            "Hyrule Castle Treasure Room Second Chest",
            hyrule_castle_treasure_room,
            LOCATION_TABLE["Hyrule Castle Treasure Room Second Chest"],
        )
    )

    hyrule_castle_treasure_room.locations.append(
        TPLocation(
            player,
            "Hyrule Castle Treasure Room First Chest",
            hyrule_castle_treasure_room,
            LOCATION_TABLE["Hyrule Castle Treasure Room First Chest"],
        )
    )

    lakebed_temple_boss_room = Region("Lakebed Temple Boss Room", player, world)
    regions["Lakebed Temple Boss Room"] = lakebed_temple_boss_room
    world.regions.append(lakebed_temple_boss_room)

    lakebed_temple_boss_room.locations.append(
        TPLocation(
            player,
            "Lakebed Temple Morpheel Heart Container",
            lakebed_temple_boss_room,
            LOCATION_TABLE["Lakebed Temple Morpheel Heart Container"],
        )
    )

    lakebed_temple_boss_room.locations.append(
        TPLocation(
            player,
            "Lakebed Temple Dungeon Reward",
            lakebed_temple_boss_room,
            LOCATION_TABLE["Lakebed Temple Dungeon Reward"],
        )
    )

    lakebed_temple_boss_room.locations.append(
        TPLocation(
            player,
            "Lakebed Temple Morpheel",
            lakebed_temple_boss_room,
            LOCATION_TABLE["Lakebed Temple Morpheel"],
        )
    )

    lakebed_temple_central_room = Region("Lakebed Temple Central Room", player, world)
    regions["Lakebed Temple Central Room"] = lakebed_temple_central_room
    world.regions.append(lakebed_temple_central_room)

    lakebed_temple_central_room.locations.append(
        TPLocation(
            player,
            "Lakebed Temple Central Room Small Chest",
            lakebed_temple_central_room,
            LOCATION_TABLE["Lakebed Temple Central Room Small Chest"],
        )
    )

    lakebed_temple_central_room.locations.append(
        TPLocation(
            player,
            "Lakebed Temple Central Room Chest",
            lakebed_temple_central_room,
            LOCATION_TABLE["Lakebed Temple Central Room Chest"],
        )
    )

    lakebed_temple_central_room.locations.append(
        TPLocation(
            player,
            "Lakebed Temple Chandelier Chest",
            lakebed_temple_central_room,
            LOCATION_TABLE["Lakebed Temple Chandelier Chest"],
        )
    )

    lakebed_temple_central_room.locations.append(
        TPLocation(
            player,
            "Lakebed Temple Central Room Spire Chest",
            lakebed_temple_central_room,
            LOCATION_TABLE["Lakebed Temple Central Room Spire Chest"],
        )
    )

    lakebed_temple_east_wing_first_floor = Region(
        "Lakebed Temple East Wing First Floor", player, world
    )
    regions["Lakebed Temple East Wing First Floor"] = (
        lakebed_temple_east_wing_first_floor
    )
    world.regions.append(lakebed_temple_east_wing_first_floor)

    lakebed_temple_east_wing_first_floor.locations.append(
        TPLocation(
            player,
            "Lakebed Temple East Lower Waterwheel Stalactite Chest",
            lakebed_temple_east_wing_first_floor,
            LOCATION_TABLE["Lakebed Temple East Lower Waterwheel Stalactite Chest"],
        )
    )

    lakebed_temple_east_wing_first_floor.locations.append(
        TPLocation(
            player,
            "Lakebed Temple East Lower Waterwheel Bridge Chest",
            lakebed_temple_east_wing_first_floor,
            LOCATION_TABLE["Lakebed Temple East Lower Waterwheel Bridge Chest"],
        )
    )

    lakebed_temple_east_wing_first_floor.locations.append(
        TPLocation(
            player,
            "Lakebed Temple Before Deku Toad Alcove Chest",
            lakebed_temple_east_wing_first_floor,
            LOCATION_TABLE["Lakebed Temple Before Deku Toad Alcove Chest"],
        )
    )

    lakebed_temple_east_wing_first_floor.locations.append(
        TPLocation(
            player,
            "Lakebed Temple Before Deku Toad Underwater Left Chest",
            lakebed_temple_east_wing_first_floor,
            LOCATION_TABLE["Lakebed Temple Before Deku Toad Underwater Left Chest"],
        )
    )

    lakebed_temple_east_wing_first_floor.locations.append(
        TPLocation(
            player,
            "Lakebed Temple Before Deku Toad Underwater Right Chest",
            lakebed_temple_east_wing_first_floor,
            LOCATION_TABLE["Lakebed Temple Before Deku Toad Underwater Right Chest"],
        )
    )

    lakebed_temple_east_wing_first_floor.locations.append(
        TPLocation(
            player,
            "Lakebed Temple Deku Toad Chest",
            lakebed_temple_east_wing_first_floor,
            LOCATION_TABLE["Lakebed Temple Deku Toad Chest"],
        )
    )

    lakebed_temple_east_wing_second_floor = Region(
        "Lakebed Temple East Wing Second Floor", player, world
    )
    regions["Lakebed Temple East Wing Second Floor"] = (
        lakebed_temple_east_wing_second_floor
    )
    world.regions.append(lakebed_temple_east_wing_second_floor)

    lakebed_temple_east_wing_second_floor.locations.append(
        TPLocation(
            player,
            "Lakebed Temple East Second Floor Southwest Chest",
            lakebed_temple_east_wing_second_floor,
            LOCATION_TABLE["Lakebed Temple East Second Floor Southwest Chest"],
        )
    )

    lakebed_temple_east_wing_second_floor.locations.append(
        TPLocation(
            player,
            "Lakebed Temple East Second Floor Southeast Chest",
            lakebed_temple_east_wing_second_floor,
            LOCATION_TABLE["Lakebed Temple East Second Floor Southeast Chest"],
        )
    )

    lakebed_temple_east_wing_second_floor.locations.append(
        TPLocation(
            player,
            "Lakebed Temple East Water Supply Small Chest",
            lakebed_temple_east_wing_second_floor,
            LOCATION_TABLE["Lakebed Temple East Water Supply Small Chest"],
        )
    )

    lakebed_temple_east_wing_second_floor.locations.append(
        TPLocation(
            player,
            "Lakebed Temple East Water Supply Clawshot Chest",
            lakebed_temple_east_wing_second_floor,
            LOCATION_TABLE["Lakebed Temple East Water Supply Clawshot Chest"],
        )
    )

    lakebed_temple_entrance = Region("Lakebed Temple Entrance", player, world)
    regions["Lakebed Temple Entrance"] = lakebed_temple_entrance
    world.regions.append(lakebed_temple_entrance)

    lakebed_temple_entrance.locations.append(
        TPLocation(
            player,
            "Lakebed Temple Lobby Left Chest",
            lakebed_temple_entrance,
            LOCATION_TABLE["Lakebed Temple Lobby Left Chest"],
        )
    )

    lakebed_temple_entrance.locations.append(
        TPLocation(
            player,
            "Lakebed Temple Lobby Rear Chest",
            lakebed_temple_entrance,
            LOCATION_TABLE["Lakebed Temple Lobby Rear Chest"],
        )
    )

    lakebed_temple_entrance.locations.append(
        TPLocation(
            player,
            "Lakebed Temple Stalactite Room Chest",
            lakebed_temple_entrance,
            LOCATION_TABLE["Lakebed Temple Stalactite Room Chest"],
        )
    )

    lakebed_temple_west_wing = Region("Lakebed Temple West Wing", player, world)
    regions["Lakebed Temple West Wing"] = lakebed_temple_west_wing
    world.regions.append(lakebed_temple_west_wing)

    lakebed_temple_west_wing.locations.append(
        TPLocation(
            player,
            "Lakebed Temple West Lower Small Chest",
            lakebed_temple_west_wing,
            LOCATION_TABLE["Lakebed Temple West Lower Small Chest"],
        )
    )

    lakebed_temple_west_wing.locations.append(
        TPLocation(
            player,
            "Lakebed Temple West Second Floor Central Small Chest",
            lakebed_temple_west_wing,
            LOCATION_TABLE["Lakebed Temple West Second Floor Central Small Chest"],
        )
    )

    lakebed_temple_west_wing.locations.append(
        TPLocation(
            player,
            "Lakebed Temple Underwater Maze Small Chest",
            lakebed_temple_west_wing,
            LOCATION_TABLE["Lakebed Temple Underwater Maze Small Chest"],
        )
    )

    lakebed_temple_west_wing.locations.append(
        TPLocation(
            player,
            "Lakebed Temple Big Key Chest",
            lakebed_temple_west_wing,
            LOCATION_TABLE["Lakebed Temple Big Key Chest"],
        )
    )

    lakebed_temple_west_wing.locations.append(
        TPLocation(
            player,
            "Lakebed Temple West Second Floor Southwest Underwater Chest",
            lakebed_temple_west_wing,
            LOCATION_TABLE[
                "Lakebed Temple West Second Floor Southwest Underwater Chest"
            ],
        )
    )

    lakebed_temple_west_wing.locations.append(
        TPLocation(
            player,
            "Lakebed Temple West Second Floor Northeast Chest",
            lakebed_temple_west_wing,
            LOCATION_TABLE["Lakebed Temple West Second Floor Northeast Chest"],
        )
    )

    lakebed_temple_west_wing.locations.append(
        TPLocation(
            player,
            "Lakebed Temple West Second Floor Southeast Chest",
            lakebed_temple_west_wing,
            LOCATION_TABLE["Lakebed Temple West Second Floor Southeast Chest"],
        )
    )

    lakebed_temple_west_wing.locations.append(
        TPLocation(
            player,
            "Lakebed Temple West Water Supply Small Chest",
            lakebed_temple_west_wing,
            LOCATION_TABLE["Lakebed Temple West Water Supply Small Chest"],
        )
    )

    lakebed_temple_west_wing.locations.append(
        TPLocation(
            player,
            "Lakebed Temple West Water Supply Chest",
            lakebed_temple_west_wing,
            LOCATION_TABLE["Lakebed Temple West Water Supply Chest"],
        )
    )

    palace_of_twilight_entrance = Region("Palace of Twilight Entrance", player, world)
    regions["Palace of Twilight Entrance"] = palace_of_twilight_entrance
    world.regions.append(palace_of_twilight_entrance)

    palace_of_twilight_entrance.locations.append(
        TPLocation(
            player,
            "Palace of Twilight Collect Both Sols",
            palace_of_twilight_entrance,
            LOCATION_TABLE["Palace of Twilight Collect Both Sols"],
        )
    )

    palace_of_twilight_west_wing = Region("Palace of Twilight West Wing", player, world)
    regions["Palace of Twilight West Wing"] = palace_of_twilight_west_wing
    world.regions.append(palace_of_twilight_west_wing)

    palace_of_twilight_west_wing.locations.append(
        TPLocation(
            player,
            "Palace of Twilight West Wing First Room Central Chest",
            palace_of_twilight_west_wing,
            LOCATION_TABLE["Palace of Twilight West Wing First Room Central Chest"],
        )
    )

    palace_of_twilight_west_wing.locations.append(
        TPLocation(
            player,
            "Palace of Twilight West Wing Chest Behind Wall of Darkness",
            palace_of_twilight_west_wing,
            LOCATION_TABLE[
                "Palace of Twilight West Wing Chest Behind Wall of Darkness"
            ],
        )
    )

    palace_of_twilight_west_wing.locations.append(
        TPLocation(
            player,
            "Palace of Twilight West Wing Second Room Central Chest",
            palace_of_twilight_west_wing,
            LOCATION_TABLE["Palace of Twilight West Wing Second Room Central Chest"],
        )
    )

    palace_of_twilight_west_wing.locations.append(
        TPLocation(
            player,
            "Palace of Twilight West Wing Second Room Lower South Chest",
            palace_of_twilight_west_wing,
            LOCATION_TABLE[
                "Palace of Twilight West Wing Second Room Lower South Chest"
            ],
        )
    )

    palace_of_twilight_west_wing.locations.append(
        TPLocation(
            player,
            "Palace of Twilight West Wing Second Room Southeast Chest",
            palace_of_twilight_west_wing,
            LOCATION_TABLE["Palace of Twilight West Wing Second Room Southeast Chest"],
        )
    )

    palace_of_twilight_east_wing = Region("Palace of Twilight East Wing", player, world)
    regions["Palace of Twilight East Wing"] = palace_of_twilight_east_wing
    world.regions.append(palace_of_twilight_east_wing)

    palace_of_twilight_east_wing.locations.append(
        TPLocation(
            player,
            "Palace of Twilight East Wing First Room North Small Chest",
            palace_of_twilight_east_wing,
            LOCATION_TABLE["Palace of Twilight East Wing First Room North Small Chest"],
        )
    )

    palace_of_twilight_east_wing.locations.append(
        TPLocation(
            player,
            "Palace of Twilight East Wing First Room Zant Head Chest",
            palace_of_twilight_east_wing,
            LOCATION_TABLE["Palace of Twilight East Wing First Room Zant Head Chest"],
        )
    )

    palace_of_twilight_east_wing.locations.append(
        TPLocation(
            player,
            "Palace of Twilight East Wing First Room East Alcove Chest",
            palace_of_twilight_east_wing,
            LOCATION_TABLE["Palace of Twilight East Wing First Room East Alcove Chest"],
        )
    )

    palace_of_twilight_east_wing.locations.append(
        TPLocation(
            player,
            "Palace of Twilight East Wing First Room West Alcove Chest",
            palace_of_twilight_east_wing,
            LOCATION_TABLE["Palace of Twilight East Wing First Room West Alcove Chest"],
        )
    )

    palace_of_twilight_east_wing.locations.append(
        TPLocation(
            player,
            "Palace of Twilight East Wing Second Room Northeast Chest",
            palace_of_twilight_east_wing,
            LOCATION_TABLE["Palace of Twilight East Wing Second Room Northeast Chest"],
        )
    )

    palace_of_twilight_east_wing.locations.append(
        TPLocation(
            player,
            "Palace of Twilight East Wing Second Room Northwest Chest",
            palace_of_twilight_east_wing,
            LOCATION_TABLE["Palace of Twilight East Wing Second Room Northwest Chest"],
        )
    )

    palace_of_twilight_east_wing.locations.append(
        TPLocation(
            player,
            "Palace of Twilight East Wing Second Room Southwest Chest",
            palace_of_twilight_east_wing,
            LOCATION_TABLE["Palace of Twilight East Wing Second Room Southwest Chest"],
        )
    )

    palace_of_twilight_east_wing.locations.append(
        TPLocation(
            player,
            "Palace of Twilight East Wing Second Room Southeast Chest",
            palace_of_twilight_east_wing,
            LOCATION_TABLE["Palace of Twilight East Wing Second Room Southeast Chest"],
        )
    )

    palace_of_twilight_central_first_room = Region(
        "Palace of Twilight Central First Room", player, world
    )
    regions["Palace of Twilight Central First Room"] = (
        palace_of_twilight_central_first_room
    )
    world.regions.append(palace_of_twilight_central_first_room)

    palace_of_twilight_central_first_room.locations.append(
        TPLocation(
            player,
            "Palace of Twilight Central First Room Chest",
            palace_of_twilight_central_first_room,
            LOCATION_TABLE["Palace of Twilight Central First Room Chest"],
        )
    )

    palace_of_twilight_outside_room = Region(
        "Palace of Twilight Outside Room", player, world
    )
    regions["Palace of Twilight Outside Room"] = palace_of_twilight_outside_room
    world.regions.append(palace_of_twilight_outside_room)

    palace_of_twilight_outside_room.locations.append(
        TPLocation(
            player,
            "Palace of Twilight Big Key Chest",
            palace_of_twilight_outside_room,
            LOCATION_TABLE["Palace of Twilight Big Key Chest"],
        )
    )

    palace_of_twilight_outside_room.locations.append(
        TPLocation(
            player,
            "Palace of Twilight Central Outdoor Chest",
            palace_of_twilight_outside_room,
            LOCATION_TABLE["Palace of Twilight Central Outdoor Chest"],
        )
    )

    palace_of_twilight_north_tower = Region(
        "Palace of Twilight North Tower", player, world
    )
    regions["Palace of Twilight North Tower"] = palace_of_twilight_north_tower
    world.regions.append(palace_of_twilight_north_tower)

    palace_of_twilight_north_tower.locations.append(
        TPLocation(
            player,
            "Palace of Twilight Central Tower Chest",
            palace_of_twilight_north_tower,
            LOCATION_TABLE["Palace of Twilight Central Tower Chest"],
        )
    )

    palace_of_twilight_boss_room = Region("Palace of Twilight Boss Room", player, world)
    regions["Palace of Twilight Boss Room"] = palace_of_twilight_boss_room
    world.regions.append(palace_of_twilight_boss_room)

    palace_of_twilight_boss_room.locations.append(
        TPLocation(
            player,
            "Palace of Twilight Zant Heart Container",
            palace_of_twilight_boss_room,
            LOCATION_TABLE["Palace of Twilight Zant Heart Container"],
        )
    )

    palace_of_twilight_boss_room.locations.append(
        TPLocation(
            player,
            "Palace of Twilight Zant",
            palace_of_twilight_boss_room,
            LOCATION_TABLE["Palace of Twilight Zant"],
        )
    )

    snowpeak_ruins_left_door = Region("Snowpeak Ruins Left Door", player, world)
    regions["Snowpeak Ruins Left Door"] = snowpeak_ruins_left_door
    world.regions.append(snowpeak_ruins_left_door)

    snowpeak_ruins_right_door = Region("Snowpeak Ruins Right Door", player, world)
    regions["Snowpeak Ruins Right Door"] = snowpeak_ruins_right_door
    world.regions.append(snowpeak_ruins_right_door)

    snowpeak_ruins_boss_room = Region("Snowpeak Ruins Boss Room", player, world)
    regions["Snowpeak Ruins Boss Room"] = snowpeak_ruins_boss_room
    world.regions.append(snowpeak_ruins_boss_room)

    snowpeak_ruins_boss_room.locations.append(
        TPLocation(
            player,
            "Snowpeak Ruins Blizzeta Heart Container",
            snowpeak_ruins_boss_room,
            LOCATION_TABLE["Snowpeak Ruins Blizzeta Heart Container"],
        )
    )

    snowpeak_ruins_boss_room.locations.append(
        TPLocation(
            player,
            "Snowpeak Ruins Dungeon Reward",
            snowpeak_ruins_boss_room,
            LOCATION_TABLE["Snowpeak Ruins Dungeon Reward"],
        )
    )

    snowpeak_ruins_boss_room.locations.append(
        TPLocation(
            player,
            "Snowpeak Ruins Blizzeta",
            snowpeak_ruins_boss_room,
            LOCATION_TABLE["Snowpeak Ruins Blizzeta"],
        )
    )

    snowpeak_ruins_caged_freezard_room = Region(
        "Snowpeak Ruins Caged Freezard Room", player, world
    )
    regions["Snowpeak Ruins Caged Freezard Room"] = snowpeak_ruins_caged_freezard_room
    world.regions.append(snowpeak_ruins_caged_freezard_room)

    snowpeak_ruins_caged_freezard_room.locations.append(
        TPLocation(
            player,
            "Snowpeak Ruins Broken Floor Chest",
            snowpeak_ruins_caged_freezard_room,
            LOCATION_TABLE["Snowpeak Ruins Broken Floor Chest"],
        )
    )

    snowpeak_ruins_chapel = Region("Snowpeak Ruins Chapel", player, world)
    regions["Snowpeak Ruins Chapel"] = snowpeak_ruins_chapel
    world.regions.append(snowpeak_ruins_chapel)

    snowpeak_ruins_chapel.locations.append(
        TPLocation(
            player,
            "Snowpeak Ruins Chapel Chest",
            snowpeak_ruins_chapel,
            LOCATION_TABLE["Snowpeak Ruins Chapel Chest"],
        )
    )

    snowpeak_ruins_darkhammer_room = Region(
        "Snowpeak Ruins Darkhammer Room", player, world
    )
    regions["Snowpeak Ruins Darkhammer Room"] = snowpeak_ruins_darkhammer_room
    world.regions.append(snowpeak_ruins_darkhammer_room)

    snowpeak_ruins_darkhammer_room.locations.append(
        TPLocation(
            player,
            "Snowpeak Ruins Ball and Chain",
            snowpeak_ruins_darkhammer_room,
            LOCATION_TABLE["Snowpeak Ruins Ball and Chain"],
        )
    )

    snowpeak_ruins_darkhammer_room.locations.append(
        TPLocation(
            player,
            "Snowpeak Ruins Chest After Darkhammer",
            snowpeak_ruins_darkhammer_room,
            LOCATION_TABLE["Snowpeak Ruins Chest After Darkhammer"],
        )
    )

    snowpeak_ruins_east_courtyard = Region(
        "Snowpeak Ruins East Courtyard", player, world
    )
    regions["Snowpeak Ruins East Courtyard"] = snowpeak_ruins_east_courtyard
    world.regions.append(snowpeak_ruins_east_courtyard)

    snowpeak_ruins_east_courtyard.locations.append(
        TPLocation(
            player,
            "Snowpeak Ruins East Courtyard Buried Chest",
            snowpeak_ruins_east_courtyard,
            LOCATION_TABLE["Snowpeak Ruins East Courtyard Buried Chest"],
        )
    )

    snowpeak_ruins_east_courtyard.locations.append(
        TPLocation(
            player,
            "Snowpeak Ruins East Courtyard Chest",
            snowpeak_ruins_east_courtyard,
            LOCATION_TABLE["Snowpeak Ruins East Courtyard Chest"],
        )
    )

    snowpeak_ruins_entrance = Region("Snowpeak Ruins Entrance", player, world)
    regions["Snowpeak Ruins Entrance"] = snowpeak_ruins_entrance
    world.regions.append(snowpeak_ruins_entrance)

    snowpeak_ruins_entrance.locations.append(
        TPLocation(
            player,
            "Snowpeak Ruins Lobby Chandelier Chest",
            snowpeak_ruins_entrance,
            LOCATION_TABLE["Snowpeak Ruins Lobby Chandelier Chest"],
        )
    )

    snowpeak_ruins_entrance.locations.append(
        TPLocation(
            player,
            "Snowpeak Ruins Lobby West Armor Chest",
            snowpeak_ruins_entrance,
            LOCATION_TABLE["Snowpeak Ruins Lobby West Armor Chest"],
        )
    )

    snowpeak_ruins_entrance.locations.append(
        TPLocation(
            player,
            "Snowpeak Ruins Lobby East Armor Chest",
            snowpeak_ruins_entrance,
            LOCATION_TABLE["Snowpeak Ruins Lobby East Armor Chest"],
        )
    )

    snowpeak_ruins_entrance.locations.append(
        TPLocation(
            player,
            "Snowpeak Ruins Lobby Armor Poe",
            snowpeak_ruins_entrance,
            LOCATION_TABLE["Snowpeak Ruins Lobby Armor Poe"],
        )
    )

    snowpeak_ruins_entrance.locations.append(
        TPLocation(
            player,
            "Snowpeak Ruins Lobby Poe",
            snowpeak_ruins_entrance,
            LOCATION_TABLE["Snowpeak Ruins Lobby Poe"],
        )
    )

    snowpeak_ruins_northeast_chilfos_room_first_floor = Region(
        "Snowpeak Ruins Northeast Chilfos Room First Floor", player, world
    )
    regions["Snowpeak Ruins Northeast Chilfos Room First Floor"] = (
        snowpeak_ruins_northeast_chilfos_room_first_floor
    )
    world.regions.append(snowpeak_ruins_northeast_chilfos_room_first_floor)

    snowpeak_ruins_northeast_chilfos_room_first_floor.locations.append(
        TPLocation(
            player,
            "Snowpeak Ruins Ordon Pumpkin Chest",
            snowpeak_ruins_northeast_chilfos_room_first_floor,
            LOCATION_TABLE["Snowpeak Ruins Ordon Pumpkin Chest"],
        )
    )

    snowpeak_ruins_northeast_chilfos_room_second_floor = Region(
        "Snowpeak Ruins Northeast Chilfos Room Second Floor", player, world
    )
    regions["Snowpeak Ruins Northeast Chilfos Room Second Floor"] = (
        snowpeak_ruins_northeast_chilfos_room_second_floor
    )
    world.regions.append(snowpeak_ruins_northeast_chilfos_room_second_floor)

    snowpeak_ruins_northeast_chilfos_room_second_floor.locations.append(
        TPLocation(
            player,
            "Snowpeak Ruins Northeast Chandelier Chest",
            snowpeak_ruins_northeast_chilfos_room_second_floor,
            LOCATION_TABLE["Snowpeak Ruins Northeast Chandelier Chest"],
        )
    )

    snowpeak_ruins_second_floor_mini_freezard_room = Region(
        "Snowpeak Ruins Second Floor Mini Freezard Room", player, world
    )
    regions["Snowpeak Ruins Second Floor Mini Freezard Room"] = (
        snowpeak_ruins_second_floor_mini_freezard_room
    )
    world.regions.append(snowpeak_ruins_second_floor_mini_freezard_room)

    snowpeak_ruins_second_floor_mini_freezard_room.locations.append(
        TPLocation(
            player,
            "Snowpeak Ruins Ice Room Poe",
            snowpeak_ruins_second_floor_mini_freezard_room,
            LOCATION_TABLE["Snowpeak Ruins Ice Room Poe"],
        )
    )

    snowpeak_ruins_west_cannon_room = Region(
        "Snowpeak Ruins West Cannon Room", player, world
    )
    regions["Snowpeak Ruins West Cannon Room"] = snowpeak_ruins_west_cannon_room
    world.regions.append(snowpeak_ruins_west_cannon_room)

    snowpeak_ruins_west_cannon_room.locations.append(
        TPLocation(
            player,
            "Snowpeak Ruins West Cannon Room Central Chest",
            snowpeak_ruins_west_cannon_room,
            LOCATION_TABLE["Snowpeak Ruins West Cannon Room Central Chest"],
        )
    )

    snowpeak_ruins_west_cannon_room.locations.append(
        TPLocation(
            player,
            "Snowpeak Ruins West Cannon Room Corner Chest",
            snowpeak_ruins_west_cannon_room,
            LOCATION_TABLE["Snowpeak Ruins West Cannon Room Corner Chest"],
        )
    )

    snowpeak_ruins_west_courtyard = Region(
        "Snowpeak Ruins West Courtyard", player, world
    )
    regions["Snowpeak Ruins West Courtyard"] = snowpeak_ruins_west_courtyard
    world.regions.append(snowpeak_ruins_west_courtyard)

    snowpeak_ruins_west_courtyard.locations.append(
        TPLocation(
            player,
            "Snowpeak Ruins West Courtyard Buried Chest",
            snowpeak_ruins_west_courtyard,
            LOCATION_TABLE["Snowpeak Ruins West Courtyard Buried Chest"],
        )
    )

    snowpeak_ruins_west_courtyard.locations.append(
        TPLocation(
            player,
            "Snowpeak Ruins Courtyard Central Chest",
            snowpeak_ruins_west_courtyard,
            LOCATION_TABLE["Snowpeak Ruins Courtyard Central Chest"],
        )
    )

    snowpeak_ruins_wooden_beam_room = Region(
        "Snowpeak Ruins Wooden Beam Room", player, world
    )
    regions["Snowpeak Ruins Wooden Beam Room"] = snowpeak_ruins_wooden_beam_room
    world.regions.append(snowpeak_ruins_wooden_beam_room)

    snowpeak_ruins_wooden_beam_room.locations.append(
        TPLocation(
            player,
            "Snowpeak Ruins Wooden Beam Central Chest",
            snowpeak_ruins_wooden_beam_room,
            LOCATION_TABLE["Snowpeak Ruins Wooden Beam Central Chest"],
        )
    )

    snowpeak_ruins_wooden_beam_room.locations.append(
        TPLocation(
            player,
            "Snowpeak Ruins Wooden Beam Northwest Chest",
            snowpeak_ruins_wooden_beam_room,
            LOCATION_TABLE["Snowpeak Ruins Wooden Beam Northwest Chest"],
        )
    )

    snowpeak_ruins_wooden_beam_room.locations.append(
        TPLocation(
            player,
            "Snowpeak Ruins Wooden Beam Chandelier Chest",
            snowpeak_ruins_wooden_beam_room,
            LOCATION_TABLE["Snowpeak Ruins Wooden Beam Chandelier Chest"],
        )
    )

    snowpeak_ruins_yeto_and_yeta = Region("Snowpeak Ruins Yeto and Yeta", player, world)
    regions["Snowpeak Ruins Yeto and Yeta"] = snowpeak_ruins_yeto_and_yeta
    world.regions.append(snowpeak_ruins_yeto_and_yeta)

    snowpeak_ruins_yeto_and_yeta.locations.append(
        TPLocation(
            player,
            "Snowpeak Ruins Mansion Map",
            snowpeak_ruins_yeto_and_yeta,
            LOCATION_TABLE["Snowpeak Ruins Mansion Map"],
        )
    )

    temple_of_time_armos_antechamber = Region(
        "Temple of Time Armos Antechamber", player, world
    )
    regions["Temple of Time Armos Antechamber"] = temple_of_time_armos_antechamber
    world.regions.append(temple_of_time_armos_antechamber)

    temple_of_time_armos_antechamber.locations.append(
        TPLocation(
            player,
            "Temple of Time Armos Antechamber East Chest",
            temple_of_time_armos_antechamber,
            LOCATION_TABLE["Temple of Time Armos Antechamber East Chest"],
        )
    )

    temple_of_time_armos_antechamber.locations.append(
        TPLocation(
            player,
            "Temple of Time Armos Antechamber North Chest",
            temple_of_time_armos_antechamber,
            LOCATION_TABLE["Temple of Time Armos Antechamber North Chest"],
        )
    )

    temple_of_time_armos_antechamber.locations.append(
        TPLocation(
            player,
            "Temple of Time Armos Antechamber Statue Chest",
            temple_of_time_armos_antechamber,
            LOCATION_TABLE["Temple of Time Armos Antechamber Statue Chest"],
        )
    )

    temple_of_time_boss_room = Region("Temple of Time Boss Room", player, world)
    regions["Temple of Time Boss Room"] = temple_of_time_boss_room
    world.regions.append(temple_of_time_boss_room)

    temple_of_time_boss_room.locations.append(
        TPLocation(
            player,
            "Temple of Time Armogohma Heart Container",
            temple_of_time_boss_room,
            LOCATION_TABLE["Temple of Time Armogohma Heart Container"],
        )
    )

    temple_of_time_boss_room.locations.append(
        TPLocation(
            player,
            "Temple of Time Dungeon Reward",
            temple_of_time_boss_room,
            LOCATION_TABLE["Temple of Time Dungeon Reward"],
        )
    )

    temple_of_time_boss_room.locations.append(
        TPLocation(
            player,
            "Temple of Time Armogohma",
            temple_of_time_boss_room,
            LOCATION_TABLE["Temple of Time Armogohma"],
        )
    )

    temple_of_time_central_mechanical_platform = Region(
        "Temple of Time Central Mechanical Platform", player, world
    )
    regions["Temple of Time Central Mechanical Platform"] = (
        temple_of_time_central_mechanical_platform
    )
    world.regions.append(temple_of_time_central_mechanical_platform)

    temple_of_time_central_mechanical_platform.locations.append(
        TPLocation(
            player,
            "Temple of Time Poe Behind Gate",
            temple_of_time_central_mechanical_platform,
            LOCATION_TABLE["Temple of Time Poe Behind Gate"],
        )
    )

    temple_of_time_connecting_corridors = Region(
        "Temple of Time Connecting Corridors", player, world
    )
    regions["Temple of Time Connecting Corridors"] = temple_of_time_connecting_corridors
    world.regions.append(temple_of_time_connecting_corridors)

    temple_of_time_connecting_corridors.locations.append(
        TPLocation(
            player,
            "Temple of Time First Staircase Gohma Gate Chest",
            temple_of_time_connecting_corridors,
            LOCATION_TABLE["Temple of Time First Staircase Gohma Gate Chest"],
        )
    )

    temple_of_time_connecting_corridors.locations.append(
        TPLocation(
            player,
            "Temple of Time First Staircase Window Chest",
            temple_of_time_connecting_corridors,
            LOCATION_TABLE["Temple of Time First Staircase Window Chest"],
        )
    )

    temple_of_time_connecting_corridors.locations.append(
        TPLocation(
            player,
            "Temple of Time First Staircase Armos Chest",
            temple_of_time_connecting_corridors,
            LOCATION_TABLE["Temple of Time First Staircase Armos Chest"],
        )
    )

    temple_of_time_crumbling_corridor = Region(
        "Temple of Time Crumbling Corridor", player, world
    )
    regions["Temple of Time Crumbling Corridor"] = temple_of_time_crumbling_corridor
    world.regions.append(temple_of_time_crumbling_corridor)

    temple_of_time_darknut_arena = Region("Temple of Time Darknut Arena", player, world)
    regions["Temple of Time Darknut Arena"] = temple_of_time_darknut_arena
    world.regions.append(temple_of_time_darknut_arena)

    temple_of_time_darknut_arena.locations.append(
        TPLocation(
            player,
            "Temple of Time Darknut Chest",
            temple_of_time_darknut_arena,
            LOCATION_TABLE["Temple of Time Darknut Chest"],
        )
    )

    temple_of_time_entrance = Region("Temple of Time Entrance", player, world)
    regions["Temple of Time Entrance"] = temple_of_time_entrance
    world.regions.append(temple_of_time_entrance)

    temple_of_time_entrance.locations.append(
        TPLocation(
            player,
            "Temple of Time Lobby Lantern Chest",
            temple_of_time_entrance,
            LOCATION_TABLE["Temple of Time Lobby Lantern Chest"],
        )
    )

    temple_of_time_floor_switch_puzzle_room = Region(
        "Temple of Time Floor Switch Puzzle Room", player, world
    )
    regions["Temple of Time Floor Switch Puzzle Room"] = (
        temple_of_time_floor_switch_puzzle_room
    )
    world.regions.append(temple_of_time_floor_switch_puzzle_room)

    temple_of_time_floor_switch_puzzle_room.locations.append(
        TPLocation(
            player,
            "Temple of Time Big Key Chest",
            temple_of_time_floor_switch_puzzle_room,
            LOCATION_TABLE["Temple of Time Big Key Chest"],
        )
    )

    temple_of_time_floor_switch_puzzle_room.locations.append(
        TPLocation(
            player,
            "Temple of Time Floor Switch Puzzle Room Upper Chest",
            temple_of_time_floor_switch_puzzle_room,
            LOCATION_TABLE["Temple of Time Floor Switch Puzzle Room Upper Chest"],
        )
    )

    temple_of_time_moving_wall_hallways = Region(
        "Temple of Time Moving Wall Hallways", player, world
    )
    regions["Temple of Time Moving Wall Hallways"] = temple_of_time_moving_wall_hallways
    world.regions.append(temple_of_time_moving_wall_hallways)

    temple_of_time_moving_wall_hallways.locations.append(
        TPLocation(
            player,
            "Temple of Time Moving Wall Beamos Room Chest",
            temple_of_time_moving_wall_hallways,
            LOCATION_TABLE["Temple of Time Moving Wall Beamos Room Chest"],
        )
    )

    temple_of_time_moving_wall_hallways.locations.append(
        TPLocation(
            player,
            "Temple of Time Moving Wall Dinalfos Room Chest",
            temple_of_time_moving_wall_hallways,
            LOCATION_TABLE["Temple of Time Moving Wall Dinalfos Room Chest"],
        )
    )

    temple_of_time_scales_of_time = Region(
        "Temple of Time Scales of Time", player, world
    )
    regions["Temple of Time Scales of Time"] = temple_of_time_scales_of_time
    world.regions.append(temple_of_time_scales_of_time)

    temple_of_time_scales_of_time.locations.append(
        TPLocation(
            player,
            "Temple of Time Scales Gohma Chest",
            temple_of_time_scales_of_time,
            LOCATION_TABLE["Temple of Time Scales Gohma Chest"],
        )
    )

    temple_of_time_scales_of_time.locations.append(
        TPLocation(
            player,
            "Temple of Time Scales Upper Chest",
            temple_of_time_scales_of_time,
            LOCATION_TABLE["Temple of Time Scales Upper Chest"],
        )
    )

    temple_of_time_scales_of_time.locations.append(
        TPLocation(
            player,
            "Temple of Time Poe Above Scales",
            temple_of_time_scales_of_time,
            LOCATION_TABLE["Temple of Time Poe Above Scales"],
        )
    )

    temple_of_time_upper_spike_trap_corridor = Region(
        "Temple of Time Upper Spike Trap Corridor", player, world
    )
    regions["Temple of Time Upper Spike Trap Corridor"] = (
        temple_of_time_upper_spike_trap_corridor
    )
    world.regions.append(temple_of_time_upper_spike_trap_corridor)

    temple_of_time_upper_spike_trap_corridor.locations.append(
        TPLocation(
            player,
            "Temple of Time Gilloutine Chest",
            temple_of_time_upper_spike_trap_corridor,
            LOCATION_TABLE["Temple of Time Gilloutine Chest"],
        )
    )

    temple_of_time_upper_spike_trap_corridor.locations.append(
        TPLocation(
            player,
            "Temple of Time Chest Before Darknut",
            temple_of_time_upper_spike_trap_corridor,
            LOCATION_TABLE["Temple of Time Chest Before Darknut"],
        )
    )

    death_mountain_near_kakariko = Region("Death Mountain Near Kakariko", player, world)
    regions["Death Mountain Near Kakariko"] = death_mountain_near_kakariko
    world.regions.append(death_mountain_near_kakariko)

    death_mountain_trail = Region("Death Mountain Trail", player, world)
    regions["Death Mountain Trail"] = death_mountain_trail
    world.regions.append(death_mountain_trail)

    death_mountain_trail.locations.append(
        TPLocation(
            player,
            "Death Mountain Alcove Chest",
            death_mountain_trail,
            LOCATION_TABLE["Death Mountain Alcove Chest"],
        )
    )

    death_mountain_trail.locations.append(
        TPLocation(
            player,
            "Death Mountain Trail Poe",
            death_mountain_trail,
            LOCATION_TABLE["Death Mountain Trail Poe"],
        )
    )

    death_mountain_volcano = Region("Death Mountain Volcano", player, world)
    regions["Death Mountain Volcano"] = death_mountain_volcano
    world.regions.append(death_mountain_volcano)

    death_mountain_outside_sumo_hall = Region(
        "Death Mountain Outside Sumo Hall", player, world
    )
    regions["Death Mountain Outside Sumo Hall"] = death_mountain_outside_sumo_hall
    world.regions.append(death_mountain_outside_sumo_hall)

    death_mountain_elevator_lower = Region(
        "Death Mountain Elevator Lower", player, world
    )
    regions["Death Mountain Elevator Lower"] = death_mountain_elevator_lower
    world.regions.append(death_mountain_elevator_lower)

    death_mountain_sumo_hall = Region("Death Mountain Sumo Hall", player, world)
    regions["Death Mountain Sumo Hall"] = death_mountain_sumo_hall
    world.regions.append(death_mountain_sumo_hall)

    death_mountain_sumo_hall_elevator = Region(
        "Death Mountain Sumo Hall Elevator", player, world
    )
    regions["Death Mountain Sumo Hall Elevator"] = death_mountain_sumo_hall_elevator
    world.regions.append(death_mountain_sumo_hall_elevator)

    death_mountain_sumo_hall_goron_mines_tunnel = Region(
        "Death Mountain Sumo Hall Goron Mines Tunnel", player, world
    )
    regions["Death Mountain Sumo Hall Goron Mines Tunnel"] = (
        death_mountain_sumo_hall_goron_mines_tunnel
    )
    world.regions.append(death_mountain_sumo_hall_goron_mines_tunnel)

    hidden_village = Region("Hidden Village", player, world)
    regions["Hidden Village"] = hidden_village
    world.regions.append(hidden_village)

    hidden_village.locations.append(
        TPLocation(
            player,
            "Cats Hide and Seek Minigame",
            hidden_village,
            LOCATION_TABLE["Cats Hide and Seek Minigame"],
        )
    )

    hidden_village.locations.append(
        TPLocation(
            player,
            "Ilia Charm",
            hidden_village,
            LOCATION_TABLE["Ilia Charm"],
        )
    )

    hidden_village.locations.append(
        TPLocation(
            player,
            "Hidden Village Poe",
            hidden_village,
            LOCATION_TABLE["Hidden Village Poe"],
        )
    )

    hidden_village_impaz_house = Region("Hidden Village Impaz House", player, world)
    regions["Hidden Village Impaz House"] = hidden_village_impaz_house
    world.regions.append(hidden_village_impaz_house)

    hidden_village_impaz_house.locations.append(
        TPLocation(
            player,
            "Skybook From Impaz",
            hidden_village_impaz_house,
            LOCATION_TABLE["Skybook From Impaz"],
        )
    )

    kakariko_gorge = Region("Kakariko Gorge", player, world)
    regions["Kakariko Gorge"] = kakariko_gorge
    world.regions.append(kakariko_gorge)

    kakariko_gorge.locations.append(
        TPLocation(
            player,
            "Kakariko Gorge Owl Statue Chest",
            kakariko_gorge,
            LOCATION_TABLE["Kakariko Gorge Owl Statue Chest"],
        )
    )

    kakariko_gorge.locations.append(
        TPLocation(
            player,
            "Kakariko Gorge Double Clawshot Chest",
            kakariko_gorge,
            LOCATION_TABLE["Kakariko Gorge Double Clawshot Chest"],
        )
    )

    kakariko_gorge.locations.append(
        TPLocation(
            player,
            "Kakariko Gorge Spire Heart Piece",
            kakariko_gorge,
            LOCATION_TABLE["Kakariko Gorge Spire Heart Piece"],
        )
    )

    kakariko_gorge.locations.append(
        TPLocation(
            player,
            "Kakariko Gorge Owl Statue Sky Character",
            kakariko_gorge,
            LOCATION_TABLE["Kakariko Gorge Owl Statue Sky Character"],
        )
    )

    kakariko_gorge.locations.append(
        TPLocation(
            player,
            "Kakariko Gorge Male Pill Bug",
            kakariko_gorge,
            LOCATION_TABLE["Kakariko Gorge Male Pill Bug"],
        )
    )

    kakariko_gorge.locations.append(
        TPLocation(
            player,
            "Kakariko Gorge Female Pill Bug",
            kakariko_gorge,
            LOCATION_TABLE["Kakariko Gorge Female Pill Bug"],
        )
    )

    kakariko_gorge.locations.append(
        TPLocation(
            player,
            "Kakariko Gorge Poe",
            kakariko_gorge,
            LOCATION_TABLE["Kakariko Gorge Poe"],
        )
    )

    kakariko_gorge_cave_entrance = Region("Kakariko Gorge Cave Entrance", player, world)
    regions["Kakariko Gorge Cave Entrance"] = kakariko_gorge_cave_entrance
    world.regions.append(kakariko_gorge_cave_entrance)

    kakariko_gorge_behind_gate = Region("Kakariko Gorge Behind Gate", player, world)
    regions["Kakariko Gorge Behind Gate"] = kakariko_gorge_behind_gate
    world.regions.append(kakariko_gorge_behind_gate)

    eldin_lantern_cave = Region("Eldin Lantern Cave", player, world)
    regions["Eldin Lantern Cave"] = eldin_lantern_cave
    world.regions.append(eldin_lantern_cave)

    eldin_lantern_cave.locations.append(
        TPLocation(
            player,
            "Eldin Lantern Cave First Chest",
            eldin_lantern_cave,
            LOCATION_TABLE["Eldin Lantern Cave First Chest"],
        )
    )

    eldin_lantern_cave.locations.append(
        TPLocation(
            player,
            "Eldin Lantern Cave Lantern Chest",
            eldin_lantern_cave,
            LOCATION_TABLE["Eldin Lantern Cave Lantern Chest"],
        )
    )

    eldin_lantern_cave.locations.append(
        TPLocation(
            player,
            "Eldin Lantern Cave Second Chest",
            eldin_lantern_cave,
            LOCATION_TABLE["Eldin Lantern Cave Second Chest"],
        )
    )

    eldin_lantern_cave.locations.append(
        TPLocation(
            player,
            "Eldin Lantern Cave Poe",
            eldin_lantern_cave,
            LOCATION_TABLE["Eldin Lantern Cave Poe"],
        )
    )

    kakariko_gorge_keese_grotto = Region("Kakariko Gorge Keese Grotto", player, world)
    regions["Kakariko Gorge Keese Grotto"] = kakariko_gorge_keese_grotto
    world.regions.append(kakariko_gorge_keese_grotto)

    eldin_field = Region("Eldin Field", player, world)
    regions["Eldin Field"] = eldin_field
    world.regions.append(eldin_field)

    eldin_field.locations.append(
        TPLocation(
            player,
            "Eldin Field Bomb Rock Chest",
            eldin_field,
            LOCATION_TABLE["Eldin Field Bomb Rock Chest"],
        )
    )

    eldin_field.locations.append(
        TPLocation(
            player,
            "Bridge of Eldin Owl Statue Chest",
            eldin_field,
            LOCATION_TABLE["Bridge of Eldin Owl Statue Chest"],
        )
    )

    eldin_field.locations.append(
        TPLocation(
            player,
            "Goron Springwater Rush",
            eldin_field,
            LOCATION_TABLE["Goron Springwater Rush"],
        )
    )

    eldin_field.locations.append(
        TPLocation(
            player,
            "Bridge of Eldin Owl Statue Sky Character",
            eldin_field,
            LOCATION_TABLE["Bridge of Eldin Owl Statue Sky Character"],
        )
    )

    eldin_field.locations.append(
        TPLocation(
            player,
            "Eldin Field Male Grasshopper",
            eldin_field,
            LOCATION_TABLE["Eldin Field Male Grasshopper"],
        )
    )

    eldin_field.locations.append(
        TPLocation(
            player,
            "Eldin Field Female Grasshopper",
            eldin_field,
            LOCATION_TABLE["Eldin Field Female Grasshopper"],
        )
    )

    eldin_field.locations.append(
        TPLocation(
            player,
            "Bridge of Eldin Male Phasmid",
            eldin_field,
            LOCATION_TABLE["Bridge of Eldin Male Phasmid"],
        )
    )

    eldin_field.locations.append(
        TPLocation(
            player,
            "Bridge of Eldin Female Phasmid",
            eldin_field,
            LOCATION_TABLE["Bridge of Eldin Female Phasmid"],
        )
    )

    eldin_field_near_castle_town = Region("Eldin Field Near Castle Town", player, world)
    regions["Eldin Field Near Castle Town"] = eldin_field_near_castle_town
    world.regions.append(eldin_field_near_castle_town)

    eldin_field_lava_cave_ledge = Region("Eldin Field Lava Cave Ledge", player, world)
    regions["Eldin Field Lava Cave Ledge"] = eldin_field_lava_cave_ledge
    world.regions.append(eldin_field_lava_cave_ledge)

    eldin_field_from_lava_cave_lower = Region(
        "Eldin Field From Lava Cave Lower", player, world
    )
    regions["Eldin Field From Lava Cave Lower"] = eldin_field_from_lava_cave_lower
    world.regions.append(eldin_field_from_lava_cave_lower)

    north_eldin_field = Region("North Eldin Field", player, world)
    regions["North Eldin Field"] = north_eldin_field
    world.regions.append(north_eldin_field)

    eldin_field_outside_hidden_village = Region(
        "Eldin Field Outside Hidden Village", player, world
    )
    regions["Eldin Field Outside Hidden Village"] = eldin_field_outside_hidden_village
    world.regions.append(eldin_field_outside_hidden_village)

    eldin_field_grotto_platform = Region("Eldin Field Grotto Platform", player, world)
    regions["Eldin Field Grotto Platform"] = eldin_field_grotto_platform
    world.regions.append(eldin_field_grotto_platform)

    eldin_field_lava_cave_upper = Region("Eldin Field Lava Cave Upper", player, world)
    regions["Eldin Field Lava Cave Upper"] = eldin_field_lava_cave_upper
    world.regions.append(eldin_field_lava_cave_upper)

    eldin_field_lava_cave_upper.locations.append(
        TPLocation(
            player,
            "Eldin Stockcave Upper Chest",
            eldin_field_lava_cave_upper,
            LOCATION_TABLE["Eldin Stockcave Upper Chest"],
        )
    )

    eldin_field_lava_cave_lower = Region("Eldin Field Lava Cave Lower", player, world)
    regions["Eldin Field Lava Cave Lower"] = eldin_field_lava_cave_lower
    world.regions.append(eldin_field_lava_cave_lower)

    eldin_field_lava_cave_lower.locations.append(
        TPLocation(
            player,
            "Eldin Stockcave Lantern Chest",
            eldin_field_lava_cave_lower,
            LOCATION_TABLE["Eldin Stockcave Lantern Chest"],
        )
    )

    eldin_field_lava_cave_lower.locations.append(
        TPLocation(
            player,
            "Eldin Stockcave Lowest Chest",
            eldin_field_lava_cave_lower,
            LOCATION_TABLE["Eldin Stockcave Lowest Chest"],
        )
    )

    eldin_field_bomskit_grotto = Region("Eldin Field Bomskit Grotto", player, world)
    regions["Eldin Field Bomskit Grotto"] = eldin_field_bomskit_grotto
    world.regions.append(eldin_field_bomskit_grotto)

    eldin_field_bomskit_grotto.locations.append(
        TPLocation(
            player,
            "Eldin Field Bomskit Grotto Left Chest",
            eldin_field_bomskit_grotto,
            LOCATION_TABLE["Eldin Field Bomskit Grotto Left Chest"],
        )
    )

    eldin_field_bomskit_grotto.locations.append(
        TPLocation(
            player,
            "Eldin Field Bomskit Grotto Lantern Chest",
            eldin_field_bomskit_grotto,
            LOCATION_TABLE["Eldin Field Bomskit Grotto Lantern Chest"],
        )
    )

    eldin_field_water_bomb_fish_grotto = Region(
        "Eldin Field Water Bomb Fish Grotto", player, world
    )
    regions["Eldin Field Water Bomb Fish Grotto"] = eldin_field_water_bomb_fish_grotto
    world.regions.append(eldin_field_water_bomb_fish_grotto)

    eldin_field_water_bomb_fish_grotto.locations.append(
        TPLocation(
            player,
            "Eldin Field Water Bomb Fish Grotto Chest",
            eldin_field_water_bomb_fish_grotto,
            LOCATION_TABLE["Eldin Field Water Bomb Fish Grotto Chest"],
        )
    )

    eldin_field_stalfos_grotto = Region("Eldin Field Stalfos Grotto", player, world)
    regions["Eldin Field Stalfos Grotto"] = eldin_field_stalfos_grotto
    world.regions.append(eldin_field_stalfos_grotto)

    eldin_field_stalfos_grotto.locations.append(
        TPLocation(
            player,
            "Eldin Field Stalfos Grotto Right Small Chest",
            eldin_field_stalfos_grotto,
            LOCATION_TABLE["Eldin Field Stalfos Grotto Right Small Chest"],
        )
    )

    eldin_field_stalfos_grotto.locations.append(
        TPLocation(
            player,
            "Eldin Field Stalfos Grotto Left Small Chest",
            eldin_field_stalfos_grotto,
            LOCATION_TABLE["Eldin Field Stalfos Grotto Left Small Chest"],
        )
    )

    eldin_field_stalfos_grotto.locations.append(
        TPLocation(
            player,
            "Eldin Field Stalfos Grotto Stalfos Chest",
            eldin_field_stalfos_grotto,
            LOCATION_TABLE["Eldin Field Stalfos Grotto Stalfos Chest"],
        )
    )

    lower_kakariko_village = Region("Lower Kakariko Village", player, world)
    regions["Lower Kakariko Village"] = lower_kakariko_village
    world.regions.append(lower_kakariko_village)

    lower_kakariko_village.locations.append(
        TPLocation(
            player,
            "Eldin Spring Underwater Chest",
            lower_kakariko_village,
            LOCATION_TABLE["Eldin Spring Underwater Chest"],
        )
    )

    lower_kakariko_village.locations.append(
        TPLocation(
            player,
            "Kakariko Village Bomb Rock Spire Heart Piece",
            lower_kakariko_village,
            LOCATION_TABLE["Kakariko Village Bomb Rock Spire Heart Piece"],
        )
    )

    upper_kakariko_village = Region("Upper Kakariko Village", player, world)
    regions["Upper Kakariko Village"] = upper_kakariko_village
    world.regions.append(upper_kakariko_village)

    upper_kakariko_village.locations.append(
        TPLocation(
            player,
            "Kakariko Village Bomb Shop Poe",
            upper_kakariko_village,
            LOCATION_TABLE["Kakariko Village Bomb Shop Poe"],
        )
    )

    upper_kakariko_village.locations.append(
        TPLocation(
            player,
            "Kakariko Village Watchtower Poe",
            upper_kakariko_village,
            LOCATION_TABLE["Kakariko Village Watchtower Poe"],
        )
    )

    upper_kakariko_village.locations.append(
        TPLocation(
            player,
            "Kakariko Watchtower Alcove Chest",
            upper_kakariko_village,
            LOCATION_TABLE["Kakariko Watchtower Alcove Chest"],
        )
    )

    kakariko_top_of_watchtower = Region("Kakariko Top of Watchtower", player, world)
    regions["Kakariko Top of Watchtower"] = kakariko_top_of_watchtower
    world.regions.append(kakariko_top_of_watchtower)

    kakariko_top_of_watchtower.locations.append(
        TPLocation(
            player,
            "Talo Sharpshooting",
            kakariko_top_of_watchtower,
            LOCATION_TABLE["Talo Sharpshooting"],
        )
    )

    kakariko_village_behind_gate = Region("Kakariko Village Behind Gate", player, world)
    regions["Kakariko Village Behind Gate"] = kakariko_village_behind_gate
    world.regions.append(kakariko_village_behind_gate)

    kakariko_renados_sanctuary_front_left_door = Region(
        "Kakariko Renados Sanctuary Front Left Door", player, world
    )
    regions["Kakariko Renados Sanctuary Front Left Door"] = (
        kakariko_renados_sanctuary_front_left_door
    )
    world.regions.append(kakariko_renados_sanctuary_front_left_door)

    kakariko_renados_sanctuary_front_right_door = Region(
        "Kakariko Renados Sanctuary Front Right Door", player, world
    )
    regions["Kakariko Renados Sanctuary Front Right Door"] = (
        kakariko_renados_sanctuary_front_right_door
    )
    world.regions.append(kakariko_renados_sanctuary_front_right_door)

    kakariko_renados_sanctuary_back_left_door = Region(
        "Kakariko Renados Sanctuary Back Left Door", player, world
    )
    regions["Kakariko Renados Sanctuary Back Left Door"] = (
        kakariko_renados_sanctuary_back_left_door
    )
    world.regions.append(kakariko_renados_sanctuary_back_left_door)

    kakariko_renados_sanctuary_back_right_door = Region(
        "Kakariko Renados Sanctuary Back Right Door", player, world
    )
    regions["Kakariko Renados Sanctuary Back Right Door"] = (
        kakariko_renados_sanctuary_back_right_door
    )
    world.regions.append(kakariko_renados_sanctuary_back_right_door)

    kakariko_renados_sanctuary = Region("Kakariko Renados Sanctuary", player, world)
    regions["Kakariko Renados Sanctuary"] = kakariko_renados_sanctuary
    world.regions.append(kakariko_renados_sanctuary)

    kakariko_renados_sanctuary.locations.append(
        TPLocation(
            player,
            "Renados Letter",
            kakariko_renados_sanctuary,
            LOCATION_TABLE["Renados Letter"],
        )
    )

    kakariko_renados_sanctuary.locations.append(
        TPLocation(
            player,
            "Ilia Memory Reward",
            kakariko_renados_sanctuary,
            LOCATION_TABLE["Ilia Memory Reward"],
        )
    )

    kakariko_renados_sanctuary_basement = Region(
        "Kakariko Renados Sanctuary Basement", player, world
    )
    regions["Kakariko Renados Sanctuary Basement"] = kakariko_renados_sanctuary_basement
    world.regions.append(kakariko_renados_sanctuary_basement)

    kakariko_malo_mart = Region("Kakariko Malo Mart", player, world)
    regions["Kakariko Malo Mart"] = kakariko_malo_mart
    world.regions.append(kakariko_malo_mart)

    kakariko_malo_mart.locations.append(
        TPLocation(
            player,
            "Kakariko Village Malo Mart Hylian Shield",
            kakariko_malo_mart,
            LOCATION_TABLE["Kakariko Village Malo Mart Hylian Shield"],
        )
    )

    kakariko_malo_mart.locations.append(
        TPLocation(
            player,
            "Kakariko Village Malo Mart Hawkeye",
            kakariko_malo_mart,
            LOCATION_TABLE["Kakariko Village Malo Mart Hawkeye"],
        )
    )

    kakariko_malo_mart.locations.append(
        TPLocation(
            player,
            "Kakariko Village Malo Mart Red Potion",
            kakariko_malo_mart,
            LOCATION_TABLE["Kakariko Village Malo Mart Red Potion"],
        )
    )

    kakariko_malo_mart.locations.append(
        TPLocation(
            player,
            "Kakariko Village Malo Mart Wooden Shield",
            kakariko_malo_mart,
            LOCATION_TABLE["Kakariko Village Malo Mart Wooden Shield"],
        )
    )

    kakariko_elde_inn_left_door = Region("Kakariko Elde Inn Left Door", player, world)
    regions["Kakariko Elde Inn Left Door"] = kakariko_elde_inn_left_door
    world.regions.append(kakariko_elde_inn_left_door)

    kakariko_elde_inn_right_door = Region("Kakariko Elde Inn Right Door", player, world)
    regions["Kakariko Elde Inn Right Door"] = kakariko_elde_inn_right_door
    world.regions.append(kakariko_elde_inn_right_door)

    kakariko_elde_inn = Region("Kakariko Elde Inn", player, world)
    regions["Kakariko Elde Inn"] = kakariko_elde_inn
    world.regions.append(kakariko_elde_inn)

    kakariko_elde_inn.locations.append(
        TPLocation(
            player,
            "Kakariko Inn Chest",
            kakariko_elde_inn,
            LOCATION_TABLE["Kakariko Inn Chest"],
        )
    )

    kakariko_bug_house_door = Region("Kakariko Bug House Door", player, world)
    regions["Kakariko Bug House Door"] = kakariko_bug_house_door
    world.regions.append(kakariko_bug_house_door)

    kakariko_bug_house_ceiling_hole = Region(
        "Kakariko Bug House Ceiling Hole", player, world
    )
    regions["Kakariko Bug House Ceiling Hole"] = kakariko_bug_house_ceiling_hole
    world.regions.append(kakariko_bug_house_ceiling_hole)

    kakariko_bug_house = Region("Kakariko Bug House", player, world)
    regions["Kakariko Bug House"] = kakariko_bug_house
    world.regions.append(kakariko_bug_house)

    kakariko_bug_house.locations.append(
        TPLocation(
            player,
            "Kakariko Village Female Ant",
            kakariko_bug_house,
            LOCATION_TABLE["Kakariko Village Female Ant"],
        )
    )

    kakariko_barnes_bomb_shop_lower = Region(
        "Kakariko Barnes Bomb Shop Lower", player, world
    )
    regions["Kakariko Barnes Bomb Shop Lower"] = kakariko_barnes_bomb_shop_lower
    world.regions.append(kakariko_barnes_bomb_shop_lower)

    kakariko_barnes_bomb_shop_lower.locations.append(
        TPLocation(
            player,
            "Barnes Bomb Bag",
            kakariko_barnes_bomb_shop_lower,
            LOCATION_TABLE["Barnes Bomb Bag"],
        )
    )

    kakariko_barnes_bomb_shop_upper = Region(
        "Kakariko Barnes Bomb Shop Upper", player, world
    )
    regions["Kakariko Barnes Bomb Shop Upper"] = kakariko_barnes_bomb_shop_upper
    world.regions.append(kakariko_barnes_bomb_shop_upper)

    kakariko_watchtower_lower_door = Region(
        "Kakariko Watchtower Lower Door", player, world
    )
    regions["Kakariko Watchtower Lower Door"] = kakariko_watchtower_lower_door
    world.regions.append(kakariko_watchtower_lower_door)

    kakariko_watchtower_dig_spot = Region("Kakariko Watchtower Dig Spot", player, world)
    regions["Kakariko Watchtower Dig Spot"] = kakariko_watchtower_dig_spot
    world.regions.append(kakariko_watchtower_dig_spot)

    kakariko_watchtower_upper_door = Region(
        "Kakariko Watchtower Upper Door", player, world
    )
    regions["Kakariko Watchtower Upper Door"] = kakariko_watchtower_upper_door
    world.regions.append(kakariko_watchtower_upper_door)

    kakariko_watchtower = Region("Kakariko Watchtower", player, world)
    regions["Kakariko Watchtower"] = kakariko_watchtower
    world.regions.append(kakariko_watchtower)

    kakariko_watchtower.locations.append(
        TPLocation(
            player,
            "Kakariko Watchtower Chest",
            kakariko_watchtower,
            LOCATION_TABLE["Kakariko Watchtower Chest"],
        )
    )

    kakariko_graveyard = Region("Kakariko Graveyard", player, world)
    regions["Kakariko Graveyard"] = kakariko_graveyard
    world.regions.append(kakariko_graveyard)

    kakariko_graveyard.locations.append(
        TPLocation(
            player,
            "Kakariko Graveyard Lantern Chest",
            kakariko_graveyard,
            LOCATION_TABLE["Kakariko Graveyard Lantern Chest"],
        )
    )

    kakariko_graveyard.locations.append(
        TPLocation(
            player,
            "Gift From Ralis",
            kakariko_graveyard,
            LOCATION_TABLE["Gift From Ralis"],
        )
    )

    kakariko_graveyard.locations.append(
        TPLocation(
            player,
            "Rutelas Blessing",
            kakariko_graveyard,
            LOCATION_TABLE["Rutelas Blessing"],
        )
    )

    kakariko_graveyard.locations.append(
        TPLocation(
            player,
            "Kakariko Graveyard Male Ant",
            kakariko_graveyard,
            LOCATION_TABLE["Kakariko Graveyard Male Ant"],
        )
    )

    kakariko_graveyard.locations.append(
        TPLocation(
            player,
            "Kakariko Graveyard Grave Poe",
            kakariko_graveyard,
            LOCATION_TABLE["Kakariko Graveyard Grave Poe"],
        )
    )

    kakariko_graveyard.locations.append(
        TPLocation(
            player,
            "Kakariko Graveyard Open Poe",
            kakariko_graveyard,
            LOCATION_TABLE["Kakariko Graveyard Open Poe"],
        )
    )

    kakariko_graveyard.locations.append(
        TPLocation(
            player,
            "Kakariko Graveyard Golden Wolf",
            kakariko_graveyard,
            LOCATION_TABLE["Kakariko Graveyard Golden Wolf"],
        )
    )

    south_faron_woods = Region("South Faron Woods", player, world)
    regions["South Faron Woods"] = south_faron_woods
    world.regions.append(south_faron_woods)

    south_faron_woods.locations.append(
        TPLocation(
            player,
            "Coro Bottle",
            south_faron_woods,
            LOCATION_TABLE["Coro Bottle"],
        )
    )

    south_faron_woods_behind_gate = Region(
        "South Faron Woods Behind Gate", player, world
    )
    regions["South Faron Woods Behind Gate"] = south_faron_woods_behind_gate
    world.regions.append(south_faron_woods_behind_gate)

    south_faron_woods_coros_ledge = Region(
        "South Faron Woods Coros Ledge", player, world
    )
    regions["South Faron Woods Coros Ledge"] = south_faron_woods_coros_ledge
    world.regions.append(south_faron_woods_coros_ledge)

    south_faron_woods_owl_statue_area = Region(
        "South Faron Woods Owl Statue Area", player, world
    )
    regions["South Faron Woods Owl Statue Area"] = south_faron_woods_owl_statue_area
    world.regions.append(south_faron_woods_owl_statue_area)

    south_faron_woods_owl_statue_area.locations.append(
        TPLocation(
            player,
            "Faron Woods Owl Statue Sky Character",
            south_faron_woods_owl_statue_area,
            LOCATION_TABLE["Faron Woods Owl Statue Sky Character"],
        )
    )

    south_faron_woods_above_owl_statue = Region(
        "South Faron Woods Above Owl Statue", player, world
    )
    regions["South Faron Woods Above Owl Statue"] = south_faron_woods_above_owl_statue
    world.regions.append(south_faron_woods_above_owl_statue)

    faron_woods_coros_house_lower = Region(
        "Faron Woods Coros House Lower", player, world
    )
    regions["Faron Woods Coros House Lower"] = faron_woods_coros_house_lower
    world.regions.append(faron_woods_coros_house_lower)

    faron_woods_coros_house_upper = Region(
        "Faron Woods Coros House Upper", player, world
    )
    regions["Faron Woods Coros House Upper"] = faron_woods_coros_house_upper
    world.regions.append(faron_woods_coros_house_upper)

    faron_woods_cave_southern_entrance = Region(
        "Faron Woods Cave Southern Entrance", player, world
    )
    regions["Faron Woods Cave Southern Entrance"] = faron_woods_cave_southern_entrance
    world.regions.append(faron_woods_cave_southern_entrance)

    faron_woods_cave = Region("Faron Woods Cave", player, world)
    regions["Faron Woods Cave"] = faron_woods_cave
    world.regions.append(faron_woods_cave)

    faron_woods_cave.locations.append(
        TPLocation(
            player,
            "South Faron Cave Chest",
            faron_woods_cave,
            LOCATION_TABLE["South Faron Cave Chest"],
        )
    )

    mist_area_near_faron_woods_cave = Region(
        "Mist Area Near Faron Woods Cave", player, world
    )
    regions["Mist Area Near Faron Woods Cave"] = mist_area_near_faron_woods_cave
    world.regions.append(mist_area_near_faron_woods_cave)

    mist_area_inside_mist = Region("Mist Area Inside Mist", player, world)
    regions["Mist Area Inside Mist"] = mist_area_inside_mist
    world.regions.append(mist_area_inside_mist)

    mist_area_inside_mist.locations.append(
        TPLocation(
            player,
            "Faron Mist Stump Chest",
            mist_area_inside_mist,
            LOCATION_TABLE["Faron Mist Stump Chest"],
        )
    )

    mist_area_inside_mist.locations.append(
        TPLocation(
            player,
            "Faron Mist North Chest",
            mist_area_inside_mist,
            LOCATION_TABLE["Faron Mist North Chest"],
        )
    )

    mist_area_inside_mist.locations.append(
        TPLocation(
            player,
            "Faron Mist South Chest",
            mist_area_inside_mist,
            LOCATION_TABLE["Faron Mist South Chest"],
        )
    )

    mist_area_under_owl_statue_chest = Region(
        "Mist Area Under Owl Statue Chest", player, world
    )
    regions["Mist Area Under Owl Statue Chest"] = mist_area_under_owl_statue_chest
    world.regions.append(mist_area_under_owl_statue_chest)

    mist_area_near_owl_statue_chest = Region(
        "Mist Area Near Owl Statue Chest", player, world
    )
    regions["Mist Area Near Owl Statue Chest"] = mist_area_near_owl_statue_chest
    world.regions.append(mist_area_near_owl_statue_chest)

    mist_area_near_owl_statue_chest.locations.append(
        TPLocation(
            player,
            "Faron Woods Owl Statue Chest",
            mist_area_near_owl_statue_chest,
            LOCATION_TABLE["Faron Woods Owl Statue Chest"],
        )
    )

    mist_area_center_stump = Region("Mist Area Center Stump", player, world)
    regions["Mist Area Center Stump"] = mist_area_center_stump
    world.regions.append(mist_area_center_stump)

    mist_area_center_stump.locations.append(
        TPLocation(
            player,
            "Faron Mist Poe",
            mist_area_center_stump,
            LOCATION_TABLE["Faron Mist Poe"],
        )
    )

    mist_area_outside_faron_mist_cave = Region(
        "Mist Area Outside Faron Mist Cave", player, world
    )
    regions["Mist Area Outside Faron Mist Cave"] = mist_area_outside_faron_mist_cave
    world.regions.append(mist_area_outside_faron_mist_cave)

    mist_area_near_north_faron_woods = Region(
        "Mist Area Near North Faron Woods", player, world
    )
    regions["Mist Area Near North Faron Woods"] = mist_area_near_north_faron_woods
    world.regions.append(mist_area_near_north_faron_woods)

    faron_woods_cave_northern_entrance = Region(
        "Faron Woods Cave Northern Entrance", player, world
    )
    regions["Faron Woods Cave Northern Entrance"] = faron_woods_cave_northern_entrance
    world.regions.append(faron_woods_cave_northern_entrance)

    mist_area_faron_mist_cave = Region("Mist Area Faron Mist Cave", player, world)
    regions["Mist Area Faron Mist Cave"] = mist_area_faron_mist_cave
    world.regions.append(mist_area_faron_mist_cave)

    mist_area_faron_mist_cave.locations.append(
        TPLocation(
            player,
            "Faron Mist Cave Open Chest",
            mist_area_faron_mist_cave,
            LOCATION_TABLE["Faron Mist Cave Open Chest"],
        )
    )

    mist_area_faron_mist_cave.locations.append(
        TPLocation(
            player,
            "Faron Mist Cave Lantern Chest",
            mist_area_faron_mist_cave,
            LOCATION_TABLE["Faron Mist Cave Lantern Chest"],
        )
    )

    north_faron_woods = Region("North Faron Woods", player, world)
    regions["North Faron Woods"] = north_faron_woods
    world.regions.append(north_faron_woods)

    north_faron_woods.locations.append(
        TPLocation(
            player,
            "North Faron Woods Deku Baba Chest",
            north_faron_woods,
            LOCATION_TABLE["North Faron Woods Deku Baba Chest"],
        )
    )

    north_faron_woods.locations.append(
        TPLocation(
            player,
            "Faron Woods Golden Wolf",
            north_faron_woods,
            LOCATION_TABLE["Faron Woods Golden Wolf"],
        )
    )

    faron_field = Region("Faron Field", player, world)
    regions["Faron Field"] = faron_field
    world.regions.append(faron_field)

    faron_field.locations.append(
        TPLocation(
            player,
            "Faron Field Bridge Chest",
            faron_field,
            LOCATION_TABLE["Faron Field Bridge Chest"],
        )
    )

    faron_field.locations.append(
        TPLocation(
            player,
            "Faron Field Tree Heart Piece",
            faron_field,
            LOCATION_TABLE["Faron Field Tree Heart Piece"],
        )
    )

    faron_field.locations.append(
        TPLocation(
            player,
            "Faron Field Male Beetle",
            faron_field,
            LOCATION_TABLE["Faron Field Male Beetle"],
        )
    )

    faron_field.locations.append(
        TPLocation(
            player,
            "Faron Field Female Beetle",
            faron_field,
            LOCATION_TABLE["Faron Field Female Beetle"],
        )
    )

    faron_field.locations.append(
        TPLocation(
            player,
            "Faron Field Poe",
            faron_field,
            LOCATION_TABLE["Faron Field Poe"],
        )
    )

    faron_field_behind_boulder = Region("Faron Field Behind Boulder", player, world)
    regions["Faron Field Behind Boulder"] = faron_field_behind_boulder
    world.regions.append(faron_field_behind_boulder)

    faron_field_corner_grotto = Region("Faron Field Corner Grotto", player, world)
    regions["Faron Field Corner Grotto"] = faron_field_corner_grotto
    world.regions.append(faron_field_corner_grotto)

    faron_field_corner_grotto.locations.append(
        TPLocation(
            player,
            "Faron Field Corner Grotto Right Chest",
            faron_field_corner_grotto,
            LOCATION_TABLE["Faron Field Corner Grotto Right Chest"],
        )
    )

    faron_field_corner_grotto.locations.append(
        TPLocation(
            player,
            "Faron Field Corner Grotto Left Chest",
            faron_field_corner_grotto,
            LOCATION_TABLE["Faron Field Corner Grotto Left Chest"],
        )
    )

    faron_field_corner_grotto.locations.append(
        TPLocation(
            player,
            "Faron Field Corner Grotto Rear Chest",
            faron_field_corner_grotto,
            LOCATION_TABLE["Faron Field Corner Grotto Rear Chest"],
        )
    )

    faron_field_fishing_grotto = Region("Faron Field Fishing Grotto", player, world)
    regions["Faron Field Fishing Grotto"] = faron_field_fishing_grotto
    world.regions.append(faron_field_fishing_grotto)

    lost_woods = Region("Lost Woods", player, world)
    regions["Lost Woods"] = lost_woods
    world.regions.append(lost_woods)

    lost_woods.locations.append(
        TPLocation(
            player,
            "Lost Woods Lantern Chest",
            lost_woods,
            LOCATION_TABLE["Lost Woods Lantern Chest"],
        )
    )

    lost_woods.locations.append(
        TPLocation(
            player,
            "Lost Woods Waterfall Poe",
            lost_woods,
            LOCATION_TABLE["Lost Woods Waterfall Poe"],
        )
    )

    lost_woods_lower_battle_arena = Region(
        "Lost Woods Lower Battle Arena", player, world
    )
    regions["Lost Woods Lower Battle Arena"] = lost_woods_lower_battle_arena
    world.regions.append(lost_woods_lower_battle_arena)

    lost_woods_lower_battle_arena.locations.append(
        TPLocation(
            player,
            "Sacred Grove Spinner Chest",
            lost_woods_lower_battle_arena,
            LOCATION_TABLE["Sacred Grove Spinner Chest"],
        )
    )

    lost_woods_lower_battle_arena.locations.append(
        TPLocation(
            player,
            "Lost Woods Boulder Poe",
            lost_woods_lower_battle_arena,
            LOCATION_TABLE["Lost Woods Boulder Poe"],
        )
    )

    lost_woods_upper_battle_arena = Region(
        "Lost Woods Upper Battle Arena", player, world
    )
    regions["Lost Woods Upper Battle Arena"] = lost_woods_upper_battle_arena
    world.regions.append(lost_woods_upper_battle_arena)

    lost_woods_baba_serpent_grotto = Region(
        "Lost Woods Baba Serpent Grotto", player, world
    )
    regions["Lost Woods Baba Serpent Grotto"] = lost_woods_baba_serpent_grotto
    world.regions.append(lost_woods_baba_serpent_grotto)

    lost_woods_baba_serpent_grotto.locations.append(
        TPLocation(
            player,
            "Sacred Grove Baba Serpent Grotto Chest",
            lost_woods_baba_serpent_grotto,
            LOCATION_TABLE["Sacred Grove Baba Serpent Grotto Chest"],
        )
    )

    sacred_grove_before_block = Region("Sacred Grove Before Block", player, world)
    regions["Sacred Grove Before Block"] = sacred_grove_before_block
    world.regions.append(sacred_grove_before_block)

    sacred_grove_upper = Region("Sacred Grove Upper", player, world)
    regions["Sacred Grove Upper"] = sacred_grove_upper
    world.regions.append(sacred_grove_upper)

    sacred_grove_lower = Region("Sacred Grove Lower", player, world)
    regions["Sacred Grove Lower"] = sacred_grove_lower
    world.regions.append(sacred_grove_lower)

    sacred_grove_lower.locations.append(
        TPLocation(
            player,
            "Sacred Grove Male Snail",
            sacred_grove_lower,
            LOCATION_TABLE["Sacred Grove Male Snail"],
        )
    )

    sacred_grove_lower.locations.append(
        TPLocation(
            player,
            "Sacred Grove Master Sword Poe",
            sacred_grove_lower,
            LOCATION_TABLE["Sacred Grove Master Sword Poe"],
        )
    )

    sacred_grove_lower.locations.append(
        TPLocation(
            player,
            "Sacred Grove Pedestal Master Sword",
            sacred_grove_lower,
            LOCATION_TABLE["Sacred Grove Pedestal Master Sword"],
        )
    )

    sacred_grove_lower.locations.append(
        TPLocation(
            player,
            "Sacred Grove Pedestal Shadow Crystal",
            sacred_grove_lower,
            LOCATION_TABLE["Sacred Grove Pedestal Shadow Crystal"],
        )
    )

    sacred_grove_past = Region("Sacred Grove Past", player, world)
    regions["Sacred Grove Past"] = sacred_grove_past
    world.regions.append(sacred_grove_past)

    sacred_grove_past.locations.append(
        TPLocation(
            player,
            "Sacred Grove Past Owl Statue Chest",
            sacred_grove_past,
            LOCATION_TABLE["Sacred Grove Past Owl Statue Chest"],
        )
    )

    sacred_grove_past.locations.append(
        TPLocation(
            player,
            "Sacred Grove Female Snail",
            sacred_grove_past,
            LOCATION_TABLE["Sacred Grove Female Snail"],
        )
    )

    sacred_grove_past.locations.append(
        TPLocation(
            player,
            "Sacred Grove Temple of Time Owl Statue Poe",
            sacred_grove_past,
            LOCATION_TABLE["Sacred Grove Temple of Time Owl Statue Poe"],
        )
    )

    sacred_grove_past_behind_window = Region(
        "Sacred Grove Past Behind Window", player, world
    )
    regions["Sacred Grove Past Behind Window"] = sacred_grove_past_behind_window
    world.regions.append(sacred_grove_past_behind_window)

    gerudo_desert_cave_of_ordeals_floors_01_11 = Region(
        "Gerudo Desert Cave of Ordeals Floors 01-11", player, world
    )
    regions["Gerudo Desert Cave of Ordeals Floors 01-11"] = (
        gerudo_desert_cave_of_ordeals_floors_01_11
    )
    world.regions.append(gerudo_desert_cave_of_ordeals_floors_01_11)

    gerudo_desert_cave_of_ordeals_floors_12_21 = Region(
        "Gerudo Desert Cave of Ordeals Floors 12-21", player, world
    )
    regions["Gerudo Desert Cave of Ordeals Floors 12-21"] = (
        gerudo_desert_cave_of_ordeals_floors_12_21
    )
    world.regions.append(gerudo_desert_cave_of_ordeals_floors_12_21)

    gerudo_desert_cave_of_ordeals_floors_12_21.locations.append(
        TPLocation(
            player,
            "Cave of Ordeals Floor 17 Poe",
            gerudo_desert_cave_of_ordeals_floors_12_21,
            LOCATION_TABLE["Cave of Ordeals Floor 17 Poe"],
        )
    )

    gerudo_desert_cave_of_ordeals_floors_22_31 = Region(
        "Gerudo Desert Cave of Ordeals Floors 22-31", player, world
    )
    regions["Gerudo Desert Cave of Ordeals Floors 22-31"] = (
        gerudo_desert_cave_of_ordeals_floors_22_31
    )
    world.regions.append(gerudo_desert_cave_of_ordeals_floors_22_31)

    gerudo_desert_cave_of_ordeals_floors_32_41 = Region(
        "Gerudo Desert Cave of Ordeals Floors 32-41", player, world
    )
    regions["Gerudo Desert Cave of Ordeals Floors 32-41"] = (
        gerudo_desert_cave_of_ordeals_floors_32_41
    )
    world.regions.append(gerudo_desert_cave_of_ordeals_floors_32_41)

    gerudo_desert_cave_of_ordeals_floors_32_41.locations.append(
        TPLocation(
            player,
            "Cave of Ordeals Floor 33 Poe",
            gerudo_desert_cave_of_ordeals_floors_32_41,
            LOCATION_TABLE["Cave of Ordeals Floor 33 Poe"],
        )
    )

    gerudo_desert_cave_of_ordeals_floors_42_50 = Region(
        "Gerudo Desert Cave of Ordeals Floors 42-50", player, world
    )
    regions["Gerudo Desert Cave of Ordeals Floors 42-50"] = (
        gerudo_desert_cave_of_ordeals_floors_42_50
    )
    world.regions.append(gerudo_desert_cave_of_ordeals_floors_42_50)

    gerudo_desert_cave_of_ordeals_floors_42_50.locations.append(
        TPLocation(
            player,
            "Cave of Ordeals Floor 44 Poe",
            gerudo_desert_cave_of_ordeals_floors_42_50,
            LOCATION_TABLE["Cave of Ordeals Floor 44 Poe"],
        )
    )

    gerudo_desert_cave_of_ordeals_floors_42_50.locations.append(
        TPLocation(
            player,
            "Cave of Ordeals Great Fairy Reward",
            gerudo_desert_cave_of_ordeals_floors_42_50,
            LOCATION_TABLE["Cave of Ordeals Great Fairy Reward"],
        )
    )

    gerudo_desert = Region("Gerudo Desert", player, world)
    regions["Gerudo Desert"] = gerudo_desert
    world.regions.append(gerudo_desert)

    gerudo_desert.locations.append(
        TPLocation(
            player,
            "Gerudo Desert Peahat Ledge Chest",
            gerudo_desert,
            LOCATION_TABLE["Gerudo Desert Peahat Ledge Chest"],
        )
    )

    gerudo_desert.locations.append(
        TPLocation(
            player,
            "Gerudo Desert East Canyon Chest",
            gerudo_desert,
            LOCATION_TABLE["Gerudo Desert East Canyon Chest"],
        )
    )

    gerudo_desert.locations.append(
        TPLocation(
            player,
            "Gerudo Desert Lone Small Chest",
            gerudo_desert,
            LOCATION_TABLE["Gerudo Desert Lone Small Chest"],
        )
    )

    gerudo_desert.locations.append(
        TPLocation(
            player,
            "Gerudo Desert West Canyon Chest",
            gerudo_desert,
            LOCATION_TABLE["Gerudo Desert West Canyon Chest"],
        )
    )

    gerudo_desert.locations.append(
        TPLocation(
            player,
            "Gerudo Desert South Chest Behind Wooden Gates",
            gerudo_desert,
            LOCATION_TABLE["Gerudo Desert South Chest Behind Wooden Gates"],
        )
    )

    gerudo_desert.locations.append(
        TPLocation(
            player,
            "Gerudo Desert Owl Statue Chest",
            gerudo_desert,
            LOCATION_TABLE["Gerudo Desert Owl Statue Chest"],
        )
    )

    gerudo_desert.locations.append(
        TPLocation(
            player,
            "Gerudo Desert Owl Statue Sky Character",
            gerudo_desert,
            LOCATION_TABLE["Gerudo Desert Owl Statue Sky Character"],
        )
    )

    gerudo_desert.locations.append(
        TPLocation(
            player,
            "Gerudo Desert Male Dayfly",
            gerudo_desert,
            LOCATION_TABLE["Gerudo Desert Male Dayfly"],
        )
    )

    gerudo_desert.locations.append(
        TPLocation(
            player,
            "Gerudo Desert Female Dayfly",
            gerudo_desert,
            LOCATION_TABLE["Gerudo Desert Female Dayfly"],
        )
    )

    gerudo_desert.locations.append(
        TPLocation(
            player,
            "Gerudo Desert East Poe",
            gerudo_desert,
            LOCATION_TABLE["Gerudo Desert East Poe"],
        )
    )

    gerudo_desert_cave_of_ordeals_plateau = Region(
        "Gerudo Desert Cave of Ordeals Plateau", player, world
    )
    regions["Gerudo Desert Cave of Ordeals Plateau"] = (
        gerudo_desert_cave_of_ordeals_plateau
    )
    world.regions.append(gerudo_desert_cave_of_ordeals_plateau)

    gerudo_desert_cave_of_ordeals_plateau.locations.append(
        TPLocation(
            player,
            "Gerudo Desert Poe Above Cave of Ordeals",
            gerudo_desert_cave_of_ordeals_plateau,
            LOCATION_TABLE["Gerudo Desert Poe Above Cave of Ordeals"],
        )
    )

    gerudo_desert_basin = Region("Gerudo Desert Basin", player, world)
    regions["Gerudo Desert Basin"] = gerudo_desert_basin
    world.regions.append(gerudo_desert_basin)

    gerudo_desert_basin.locations.append(
        TPLocation(
            player,
            "Gerudo Desert Northeast Chest Behind Gates",
            gerudo_desert_basin,
            LOCATION_TABLE["Gerudo Desert Northeast Chest Behind Gates"],
        )
    )

    gerudo_desert_basin.locations.append(
        TPLocation(
            player,
            "Gerudo Desert Campfire North Chest",
            gerudo_desert_basin,
            LOCATION_TABLE["Gerudo Desert Campfire North Chest"],
        )
    )

    gerudo_desert_basin.locations.append(
        TPLocation(
            player,
            "Gerudo Desert Campfire East Chest",
            gerudo_desert_basin,
            LOCATION_TABLE["Gerudo Desert Campfire East Chest"],
        )
    )

    gerudo_desert_basin.locations.append(
        TPLocation(
            player,
            "Gerudo Desert Campfire West Chest",
            gerudo_desert_basin,
            LOCATION_TABLE["Gerudo Desert Campfire West Chest"],
        )
    )

    gerudo_desert_basin.locations.append(
        TPLocation(
            player,
            "Gerudo Desert Northwest Chest Behind Gates",
            gerudo_desert_basin,
            LOCATION_TABLE["Gerudo Desert Northwest Chest Behind Gates"],
        )
    )

    gerudo_desert_north_east_ledge = Region(
        "Gerudo Desert North East Ledge", player, world
    )
    regions["Gerudo Desert North East Ledge"] = gerudo_desert_north_east_ledge
    world.regions.append(gerudo_desert_north_east_ledge)

    gerudo_desert_north_east_ledge.locations.append(
        TPLocation(
            player,
            "Gerudo Desert North Peahat Poe",
            gerudo_desert_north_east_ledge,
            LOCATION_TABLE["Gerudo Desert North Peahat Poe"],
        )
    )

    gerudo_desert_outside_bulblin_camp = Region(
        "Gerudo Desert Outside Bulblin Camp", player, world
    )
    regions["Gerudo Desert Outside Bulblin Camp"] = gerudo_desert_outside_bulblin_camp
    world.regions.append(gerudo_desert_outside_bulblin_camp)

    gerudo_desert_outside_bulblin_camp.locations.append(
        TPLocation(
            player,
            "Gerudo Desert North Small Chest Before Bulblin Camp",
            gerudo_desert_outside_bulblin_camp,
            LOCATION_TABLE["Gerudo Desert North Small Chest Before Bulblin Camp"],
        )
    )

    gerudo_desert_outside_bulblin_camp.locations.append(
        TPLocation(
            player,
            "Outside Bulblin Camp Poe",
            gerudo_desert_outside_bulblin_camp,
            LOCATION_TABLE["Outside Bulblin Camp Poe"],
        )
    )

    gerudo_desert_outside_bulblin_camp.locations.append(
        TPLocation(
            player,
            "Gerudo Desert Golden Wolf",
            gerudo_desert_outside_bulblin_camp,
            LOCATION_TABLE["Gerudo Desert Golden Wolf"],
        )
    )

    gerudo_desert_skulltula_grotto = Region(
        "Gerudo Desert Skulltula Grotto", player, world
    )
    regions["Gerudo Desert Skulltula Grotto"] = gerudo_desert_skulltula_grotto
    world.regions.append(gerudo_desert_skulltula_grotto)

    gerudo_desert_skulltula_grotto.locations.append(
        TPLocation(
            player,
            "Gerudo Desert Skulltula Grotto Chest",
            gerudo_desert_skulltula_grotto,
            LOCATION_TABLE["Gerudo Desert Skulltula Grotto Chest"],
        )
    )

    gerudo_desert_chu_grotto = Region("Gerudo Desert Chu Grotto", player, world)
    regions["Gerudo Desert Chu Grotto"] = gerudo_desert_chu_grotto
    world.regions.append(gerudo_desert_chu_grotto)

    gerudo_desert_rock_grotto = Region("Gerudo Desert Rock Grotto", player, world)
    regions["Gerudo Desert Rock Grotto"] = gerudo_desert_rock_grotto
    world.regions.append(gerudo_desert_rock_grotto)

    gerudo_desert_rock_grotto.locations.append(
        TPLocation(
            player,
            "Gerudo Desert Rock Grotto Lantern Chest",
            gerudo_desert_rock_grotto,
            LOCATION_TABLE["Gerudo Desert Rock Grotto Lantern Chest"],
        )
    )

    gerudo_desert_rock_grotto.locations.append(
        TPLocation(
            player,
            "Gerudo Desert Rock Grotto First Poe",
            gerudo_desert_rock_grotto,
            LOCATION_TABLE["Gerudo Desert Rock Grotto First Poe"],
        )
    )

    gerudo_desert_rock_grotto.locations.append(
        TPLocation(
            player,
            "Gerudo Desert Rock Grotto Second Poe",
            gerudo_desert_rock_grotto,
            LOCATION_TABLE["Gerudo Desert Rock Grotto Second Poe"],
        )
    )

    bulblin_camp = Region("Bulblin Camp", player, world)
    regions["Bulblin Camp"] = bulblin_camp
    world.regions.append(bulblin_camp)

    bulblin_camp.locations.append(
        TPLocation(
            player,
            "Bulblin Camp First Chest Under Tower At Entrance",
            bulblin_camp,
            LOCATION_TABLE["Bulblin Camp First Chest Under Tower At Entrance"],
        )
    )

    bulblin_camp.locations.append(
        TPLocation(
            player,
            "Bulblin Camp Small Chest in Back of Camp",
            bulblin_camp,
            LOCATION_TABLE["Bulblin Camp Small Chest in Back of Camp"],
        )
    )

    bulblin_camp.locations.append(
        TPLocation(
            player,
            "Bulblin Camp Roasted Boar",
            bulblin_camp,
            LOCATION_TABLE["Bulblin Camp Roasted Boar"],
        )
    )

    bulblin_camp.locations.append(
        TPLocation(
            player,
            "Bulblin Camp Poe",
            bulblin_camp,
            LOCATION_TABLE["Bulblin Camp Poe"],
        )
    )

    bulblin_camp.locations.append(
        TPLocation(
            player,
            "Bulblin Guard Key",
            bulblin_camp,
            LOCATION_TABLE["Bulblin Guard Key"],
        )
    )

    outside_arbiters_grounds = Region("Outside Arbiters Grounds", player, world)
    regions["Outside Arbiters Grounds"] = outside_arbiters_grounds
    world.regions.append(outside_arbiters_grounds)

    outside_arbiters_grounds.locations.append(
        TPLocation(
            player,
            "Outside Arbiters Grounds Lantern Chest",
            outside_arbiters_grounds,
            LOCATION_TABLE["Outside Arbiters Grounds Lantern Chest"],
        )
    )

    outside_arbiters_grounds.locations.append(
        TPLocation(
            player,
            "Outside Arbiters Grounds Poe",
            outside_arbiters_grounds,
            LOCATION_TABLE["Outside Arbiters Grounds Poe"],
        )
    )

    mirror_chamber_lower = Region("Mirror Chamber Lower", player, world)
    regions["Mirror Chamber Lower"] = mirror_chamber_lower
    world.regions.append(mirror_chamber_lower)

    mirror_chamber_upper = Region("Mirror Chamber Upper", player, world)
    regions["Mirror Chamber Upper"] = mirror_chamber_upper
    world.regions.append(mirror_chamber_upper)

    mirror_chamber_portal = Region("Mirror of Twilight", player, world)
    regions["Mirror of Twilight"] = mirror_chamber_portal
    world.regions.append(mirror_chamber_portal)

    castle_town_west = Region("Castle Town West", player, world)
    regions["Castle Town West"] = castle_town_west
    world.regions.append(castle_town_west)

    castle_town_west.locations.append(
        TPLocation(
            player,
            "Charlo Donation Blessing",
            castle_town_west,
            LOCATION_TABLE["Charlo Donation Blessing"],
        )
    )

    castle_town_star_game = Region("Castle Town STAR Game", player, world)
    regions["Castle Town STAR Game"] = castle_town_star_game
    world.regions.append(castle_town_star_game)

    castle_town_star_game.locations.append(
        TPLocation(
            player,
            "STAR Prize 1",
            castle_town_star_game,
            LOCATION_TABLE["STAR Prize 1"],
        )
    )

    castle_town_star_game.locations.append(
        TPLocation(
            player,
            "STAR Prize 2",
            castle_town_star_game,
            LOCATION_TABLE["STAR Prize 2"],
        )
    )

    castle_town_center = Region("Castle Town Center", player, world)
    regions["Castle Town Center"] = castle_town_center
    world.regions.append(castle_town_center)

    castle_town_goron_house_left_door = Region(
        "Castle Town Goron House Left Door", player, world
    )
    regions["Castle Town Goron House Left Door"] = castle_town_goron_house_left_door
    world.regions.append(castle_town_goron_house_left_door)

    castle_town_goron_house_right_door = Region(
        "Castle Town Goron House Right Door", player, world
    )
    regions["Castle Town Goron House Right Door"] = castle_town_goron_house_right_door
    world.regions.append(castle_town_goron_house_right_door)

    castle_town_goron_house = Region("Castle Town Goron House", player, world)
    regions["Castle Town Goron House"] = castle_town_goron_house
    world.regions.append(castle_town_goron_house)

    castle_town_malo_mart = Region("Castle Town Malo Mart", player, world)
    regions["Castle Town Malo Mart"] = castle_town_malo_mart
    world.regions.append(castle_town_malo_mart)

    castle_town_malo_mart.locations.append(
        TPLocation(
            player,
            "Castle Town Malo Mart Magic Armor",
            castle_town_malo_mart,
            LOCATION_TABLE["Castle Town Malo Mart Magic Armor"],
        )
    )

    castle_town_north = Region("Castle Town North", player, world)
    regions["Castle Town North"] = castle_town_north
    world.regions.append(castle_town_north)

    castle_town_north_behind_first_door = Region(
        "Castle Town North Behind First Door", player, world
    )
    regions["Castle Town North Behind First Door"] = castle_town_north_behind_first_door
    world.regions.append(castle_town_north_behind_first_door)

    castle_town_north_behind_first_door.locations.append(
        TPLocation(
            player,
            "North Castle Town Golden Wolf",
            castle_town_north_behind_first_door,
            LOCATION_TABLE["North Castle Town Golden Wolf"],
        )
    )

    castle_town_north_inside_barrier = Region(
        "Castle Town North Inside Barrier", player, world
    )
    regions["Castle Town North Inside Barrier"] = castle_town_north_inside_barrier
    world.regions.append(castle_town_north_inside_barrier)

    castle_town_east = Region("Castle Town East", player, world)
    regions["Castle Town East"] = castle_town_east
    world.regions.append(castle_town_east)

    castle_town_doctors_office_balcony = Region(
        "Castle Town Doctors Office Balcony", player, world
    )
    regions["Castle Town Doctors Office Balcony"] = castle_town_doctors_office_balcony
    world.regions.append(castle_town_doctors_office_balcony)

    castle_town_doctors_office_balcony.locations.append(
        TPLocation(
            player,
            "Doctors Office Balcony Chest",
            castle_town_doctors_office_balcony,
            LOCATION_TABLE["Doctors Office Balcony Chest"],
        )
    )

    castle_town_doctors_office_left_door = Region(
        "Castle Town Doctors Office Left Door", player, world
    )
    regions["Castle Town Doctors Office Left Door"] = (
        castle_town_doctors_office_left_door
    )
    world.regions.append(castle_town_doctors_office_left_door)

    castle_town_doctors_office_right_door = Region(
        "Castle Town Doctors Office Right Door", player, world
    )
    regions["Castle Town Doctors Office Right Door"] = (
        castle_town_doctors_office_right_door
    )
    world.regions.append(castle_town_doctors_office_right_door)

    castle_town_doctors_office_entrance = Region(
        "Castle Town Doctors Office Entrance", player, world
    )
    regions["Castle Town Doctors Office Entrance"] = castle_town_doctors_office_entrance
    world.regions.append(castle_town_doctors_office_entrance)

    castle_town_doctors_office_lower = Region(
        "Castle Town Doctors Office Lower", player, world
    )
    regions["Castle Town Doctors Office Lower"] = castle_town_doctors_office_lower
    world.regions.append(castle_town_doctors_office_lower)

    castle_town_doctors_office_upper = Region(
        "Castle Town Doctors Office Upper", player, world
    )
    regions["Castle Town Doctors Office Upper"] = castle_town_doctors_office_upper
    world.regions.append(castle_town_doctors_office_upper)

    castle_town_south = Region("Castle Town South", player, world)
    regions["Castle Town South"] = castle_town_south
    world.regions.append(castle_town_south)

    castle_town_agithas_house = Region("Castle Town Agithas House", player, world)
    regions["Castle Town Agithas House"] = castle_town_agithas_house
    world.regions.append(castle_town_agithas_house)

    castle_town_agithas_house.locations.append(
        TPLocation(
            player,
            "Agitha Female Ant Reward",
            castle_town_agithas_house,
            LOCATION_TABLE["Agitha Female Ant Reward"],
        )
    )

    castle_town_agithas_house.locations.append(
        TPLocation(
            player,
            "Agitha Female Beetle Reward",
            castle_town_agithas_house,
            LOCATION_TABLE["Agitha Female Beetle Reward"],
        )
    )

    castle_town_agithas_house.locations.append(
        TPLocation(
            player,
            "Agitha Female Butterfly Reward",
            castle_town_agithas_house,
            LOCATION_TABLE["Agitha Female Butterfly Reward"],
        )
    )

    castle_town_agithas_house.locations.append(
        TPLocation(
            player,
            "Agitha Female Dayfly Reward",
            castle_town_agithas_house,
            LOCATION_TABLE["Agitha Female Dayfly Reward"],
        )
    )

    castle_town_agithas_house.locations.append(
        TPLocation(
            player,
            "Agitha Female Dragonfly Reward",
            castle_town_agithas_house,
            LOCATION_TABLE["Agitha Female Dragonfly Reward"],
        )
    )

    castle_town_agithas_house.locations.append(
        TPLocation(
            player,
            "Agitha Female Grasshopper Reward",
            castle_town_agithas_house,
            LOCATION_TABLE["Agitha Female Grasshopper Reward"],
        )
    )

    castle_town_agithas_house.locations.append(
        TPLocation(
            player,
            "Agitha Female Ladybug Reward",
            castle_town_agithas_house,
            LOCATION_TABLE["Agitha Female Ladybug Reward"],
        )
    )

    castle_town_agithas_house.locations.append(
        TPLocation(
            player,
            "Agitha Female Mantis Reward",
            castle_town_agithas_house,
            LOCATION_TABLE["Agitha Female Mantis Reward"],
        )
    )

    castle_town_agithas_house.locations.append(
        TPLocation(
            player,
            "Agitha Female Phasmid Reward",
            castle_town_agithas_house,
            LOCATION_TABLE["Agitha Female Phasmid Reward"],
        )
    )

    castle_town_agithas_house.locations.append(
        TPLocation(
            player,
            "Agitha Female Pill Bug Reward",
            castle_town_agithas_house,
            LOCATION_TABLE["Agitha Female Pill Bug Reward"],
        )
    )

    castle_town_agithas_house.locations.append(
        TPLocation(
            player,
            "Agitha Female Snail Reward",
            castle_town_agithas_house,
            LOCATION_TABLE["Agitha Female Snail Reward"],
        )
    )

    castle_town_agithas_house.locations.append(
        TPLocation(
            player,
            "Agitha Female Stag Beetle Reward",
            castle_town_agithas_house,
            LOCATION_TABLE["Agitha Female Stag Beetle Reward"],
        )
    )

    castle_town_agithas_house.locations.append(
        TPLocation(
            player,
            "Agitha Male Ant Reward",
            castle_town_agithas_house,
            LOCATION_TABLE["Agitha Male Ant Reward"],
        )
    )

    castle_town_agithas_house.locations.append(
        TPLocation(
            player,
            "Agitha Male Beetle Reward",
            castle_town_agithas_house,
            LOCATION_TABLE["Agitha Male Beetle Reward"],
        )
    )

    castle_town_agithas_house.locations.append(
        TPLocation(
            player,
            "Agitha Male Butterfly Reward",
            castle_town_agithas_house,
            LOCATION_TABLE["Agitha Male Butterfly Reward"],
        )
    )

    castle_town_agithas_house.locations.append(
        TPLocation(
            player,
            "Agitha Male Dayfly Reward",
            castle_town_agithas_house,
            LOCATION_TABLE["Agitha Male Dayfly Reward"],
        )
    )

    castle_town_agithas_house.locations.append(
        TPLocation(
            player,
            "Agitha Male Dragonfly Reward",
            castle_town_agithas_house,
            LOCATION_TABLE["Agitha Male Dragonfly Reward"],
        )
    )

    castle_town_agithas_house.locations.append(
        TPLocation(
            player,
            "Agitha Male Grasshopper Reward",
            castle_town_agithas_house,
            LOCATION_TABLE["Agitha Male Grasshopper Reward"],
        )
    )

    castle_town_agithas_house.locations.append(
        TPLocation(
            player,
            "Agitha Male Ladybug Reward",
            castle_town_agithas_house,
            LOCATION_TABLE["Agitha Male Ladybug Reward"],
        )
    )

    castle_town_agithas_house.locations.append(
        TPLocation(
            player,
            "Agitha Male Mantis Reward",
            castle_town_agithas_house,
            LOCATION_TABLE["Agitha Male Mantis Reward"],
        )
    )

    castle_town_agithas_house.locations.append(
        TPLocation(
            player,
            "Agitha Male Phasmid Reward",
            castle_town_agithas_house,
            LOCATION_TABLE["Agitha Male Phasmid Reward"],
        )
    )

    castle_town_agithas_house.locations.append(
        TPLocation(
            player,
            "Agitha Male Pill Bug Reward",
            castle_town_agithas_house,
            LOCATION_TABLE["Agitha Male Pill Bug Reward"],
        )
    )

    castle_town_agithas_house.locations.append(
        TPLocation(
            player,
            "Agitha Male Snail Reward",
            castle_town_agithas_house,
            LOCATION_TABLE["Agitha Male Snail Reward"],
        )
    )

    castle_town_agithas_house.locations.append(
        TPLocation(
            player,
            "Agitha Male Stag Beetle Reward",
            castle_town_agithas_house,
            LOCATION_TABLE["Agitha Male Stag Beetle Reward"],
        )
    )

    castle_town_seer_house = Region("Castle Town Seer House", player, world)
    regions["Castle Town Seer House"] = castle_town_seer_house
    world.regions.append(castle_town_seer_house)

    castle_town_jovanis_house = Region("Castle Town Jovanis House", player, world)
    regions["Castle Town Jovanis House"] = castle_town_jovanis_house
    world.regions.append(castle_town_jovanis_house)

    castle_town_jovanis_house.locations.append(
        TPLocation(
            player,
            "Jovani House Poe",
            castle_town_jovanis_house,
            LOCATION_TABLE["Jovani House Poe"],
        )
    )

    castle_town_jovanis_house.locations.append(
        TPLocation(
            player,
            "Jovani 20 Poe Soul Reward",
            castle_town_jovanis_house,
            LOCATION_TABLE["Jovani 20 Poe Soul Reward"],
        )
    )

    castle_town_jovanis_house.locations.append(
        TPLocation(
            player,
            "Jovani 60 Poe Soul Reward",
            castle_town_jovanis_house,
            LOCATION_TABLE["Jovani 60 Poe Soul Reward"],
        )
    )

    castle_town_telmas_bar = Region("Castle Town Telmas Bar", player, world)
    regions["Castle Town Telmas Bar"] = castle_town_telmas_bar
    world.regions.append(castle_town_telmas_bar)

    castle_town_telmas_bar.locations.append(
        TPLocation(
            player,
            "Telma Invoice",
            castle_town_telmas_bar,
            LOCATION_TABLE["Telma Invoice"],
        )
    )

    lanayru_field = Region("Lanayru Field", player, world)
    regions["Lanayru Field"] = lanayru_field
    world.regions.append(lanayru_field)

    lanayru_field.locations.append(
        TPLocation(
            player,
            "Lanayru Field Behind Gate Underwater Chest",
            lanayru_field,
            LOCATION_TABLE["Lanayru Field Behind Gate Underwater Chest"],
        )
    )

    lanayru_field.locations.append(
        TPLocation(
            player,
            "Lanayru Field Male Stag Beetle",
            lanayru_field,
            LOCATION_TABLE["Lanayru Field Male Stag Beetle"],
        )
    )

    lanayru_field.locations.append(
        TPLocation(
            player,
            "Lanayru Field Female Stag Beetle",
            lanayru_field,
            LOCATION_TABLE["Lanayru Field Female Stag Beetle"],
        )
    )

    lanayru_field.locations.append(
        TPLocation(
            player,
            "Lanayru Field Bridge Poe",
            lanayru_field,
            LOCATION_TABLE["Lanayru Field Bridge Poe"],
        )
    )

    lanayru_field_cave_entrance = Region("Lanayru Field Cave Entrance", player, world)
    regions["Lanayru Field Cave Entrance"] = lanayru_field_cave_entrance
    world.regions.append(lanayru_field_cave_entrance)

    lanayru_field_behind_boulder = Region("Lanayru Field Behind Boulder", player, world)
    regions["Lanayru Field Behind Boulder"] = lanayru_field_behind_boulder
    world.regions.append(lanayru_field_behind_boulder)

    hyrule_field_near_spinner_rails = Region(
        "Hyrule Field Near Spinner Rails", player, world
    )
    regions["Hyrule Field Near Spinner Rails"] = hyrule_field_near_spinner_rails
    world.regions.append(hyrule_field_near_spinner_rails)

    hyrule_field_near_spinner_rails.locations.append(
        TPLocation(
            player,
            "Lanayru Field Spinner Track Chest",
            hyrule_field_near_spinner_rails,
            LOCATION_TABLE["Lanayru Field Spinner Track Chest"],
        )
    )

    lanayru_ice_puzzle_cave = Region("Lanayru Ice Puzzle Cave", player, world)
    regions["Lanayru Ice Puzzle Cave"] = lanayru_ice_puzzle_cave
    world.regions.append(lanayru_ice_puzzle_cave)

    lanayru_ice_puzzle_cave.locations.append(
        TPLocation(
            player,
            "Lanayru Ice Block Puzzle Cave Chest",
            lanayru_ice_puzzle_cave,
            LOCATION_TABLE["Lanayru Ice Block Puzzle Cave Chest"],
        )
    )

    lanayru_field_chu_grotto = Region("Lanayru Field Chu Grotto", player, world)
    regions["Lanayru Field Chu Grotto"] = lanayru_field_chu_grotto
    world.regions.append(lanayru_field_chu_grotto)

    lanayru_field_skulltula_grotto = Region(
        "Lanayru Field Skulltula Grotto", player, world
    )
    regions["Lanayru Field Skulltula Grotto"] = lanayru_field_skulltula_grotto
    world.regions.append(lanayru_field_skulltula_grotto)

    lanayru_field_skulltula_grotto.locations.append(
        TPLocation(
            player,
            "Lanayru Field Skulltula Grotto Chest",
            lanayru_field_skulltula_grotto,
            LOCATION_TABLE["Lanayru Field Skulltula Grotto Chest"],
        )
    )

    lanayru_field_poe_grotto = Region("Lanayru Field Poe Grotto", player, world)
    regions["Lanayru Field Poe Grotto"] = lanayru_field_poe_grotto
    world.regions.append(lanayru_field_poe_grotto)

    lanayru_field_poe_grotto.locations.append(
        TPLocation(
            player,
            "Lanayru Field Poe Grotto Left Poe",
            lanayru_field_poe_grotto,
            LOCATION_TABLE["Lanayru Field Poe Grotto Left Poe"],
        )
    )

    lanayru_field_poe_grotto.locations.append(
        TPLocation(
            player,
            "Lanayru Field Poe Grotto Right Poe",
            lanayru_field_poe_grotto,
            LOCATION_TABLE["Lanayru Field Poe Grotto Right Poe"],
        )
    )

    outside_castle_town_west = Region("Outside Castle Town West", player, world)
    regions["Outside Castle Town West"] = outside_castle_town_west
    world.regions.append(outside_castle_town_west)

    outside_castle_town_west.locations.append(
        TPLocation(
            player,
            "Hyrule Field Amphitheater Owl Statue Chest",
            outside_castle_town_west,
            LOCATION_TABLE["Hyrule Field Amphitheater Owl Statue Chest"],
        )
    )

    outside_castle_town_west.locations.append(
        TPLocation(
            player,
            "Hyrule Field Amphitheater Owl Statue Sky Character",
            outside_castle_town_west,
            LOCATION_TABLE["Hyrule Field Amphitheater Owl Statue Sky Character"],
        )
    )

    outside_castle_town_west.locations.append(
        TPLocation(
            player,
            "West Hyrule Field Male Butterfly",
            outside_castle_town_west,
            LOCATION_TABLE["West Hyrule Field Male Butterfly"],
        )
    )

    outside_castle_town_west.locations.append(
        TPLocation(
            player,
            "West Hyrule Field Female Butterfly",
            outside_castle_town_west,
            LOCATION_TABLE["West Hyrule Field Female Butterfly"],
        )
    )

    outside_castle_town_west.locations.append(
        TPLocation(
            player,
            "Hyrule Field Amphitheater Poe",
            outside_castle_town_west,
            LOCATION_TABLE["Hyrule Field Amphitheater Poe"],
        )
    )

    outside_castle_town_west.locations.append(
        TPLocation(
            player,
            "West Hyrule Field Golden Wolf",
            outside_castle_town_west,
            LOCATION_TABLE["West Hyrule Field Golden Wolf"],
        )
    )

    outside_castle_town_west_grotto_ledge = Region(
        "Outside Castle Town West Grotto Ledge", player, world
    )
    regions["Outside Castle Town West Grotto Ledge"] = (
        outside_castle_town_west_grotto_ledge
    )
    world.regions.append(outside_castle_town_west_grotto_ledge)

    outside_castle_town_west_helmasaur_grotto = Region(
        "Outside Castle Town West Helmasaur Grotto", player, world
    )
    regions["Outside Castle Town West Helmasaur Grotto"] = (
        outside_castle_town_west_helmasaur_grotto
    )
    world.regions.append(outside_castle_town_west_helmasaur_grotto)

    outside_castle_town_west_helmasaur_grotto.locations.append(
        TPLocation(
            player,
            "West Hyrule Field Helmasaur Grotto Chest",
            outside_castle_town_west_helmasaur_grotto,
            LOCATION_TABLE["West Hyrule Field Helmasaur Grotto Chest"],
        )
    )

    outside_castle_town_east = Region("Outside Castle Town East", player, world)
    regions["Outside Castle Town East"] = outside_castle_town_east
    world.regions.append(outside_castle_town_east)

    outside_castle_town_east.locations.append(
        TPLocation(
            player,
            "East Castle Town Bridge Poe",
            outside_castle_town_east,
            LOCATION_TABLE["East Castle Town Bridge Poe"],
        )
    )

    outside_castle_town_south = Region("Outside Castle Town South", player, world)
    regions["Outside Castle Town South"] = outside_castle_town_south
    world.regions.append(outside_castle_town_south)

    outside_castle_town_south.locations.append(
        TPLocation(
            player,
            "Outside South Castle Town Tightrope Chest",
            outside_castle_town_south,
            LOCATION_TABLE["Outside South Castle Town Tightrope Chest"],
        )
    )

    outside_castle_town_south.locations.append(
        TPLocation(
            player,
            "Outside South Castle Town Fountain Chest",
            outside_castle_town_south,
            LOCATION_TABLE["Outside South Castle Town Fountain Chest"],
        )
    )

    outside_castle_town_south.locations.append(
        TPLocation(
            player,
            "Outside South Castle Town Double Clawshot Chasm Chest",
            outside_castle_town_south,
            LOCATION_TABLE["Outside South Castle Town Double Clawshot Chasm Chest"],
        )
    )

    outside_castle_town_south.locations.append(
        TPLocation(
            player,
            "Wooden Statue",
            outside_castle_town_south,
            LOCATION_TABLE["Wooden Statue"],
        )
    )

    outside_castle_town_south.locations.append(
        TPLocation(
            player,
            "Outside South Castle Town Male Ladybug",
            outside_castle_town_south,
            LOCATION_TABLE["Outside South Castle Town Male Ladybug"],
        )
    )

    outside_castle_town_south.locations.append(
        TPLocation(
            player,
            "Outside South Castle Town Female Ladybug",
            outside_castle_town_south,
            LOCATION_TABLE["Outside South Castle Town Female Ladybug"],
        )
    )

    outside_castle_town_south.locations.append(
        TPLocation(
            player,
            "Outside South Castle Town Poe",
            outside_castle_town_south,
            LOCATION_TABLE["Outside South Castle Town Poe"],
        )
    )

    outside_castle_town_south.locations.append(
        TPLocation(
            player,
            "Outside South Castle Town Golden Wolf",
            outside_castle_town_south,
            LOCATION_TABLE["Outside South Castle Town Golden Wolf"],
        )
    )

    outside_castle_town_south_inside_boulder = Region(
        "Outside Castle Town South Inside Boulder", player, world
    )
    regions["Outside Castle Town South Inside Boulder"] = (
        outside_castle_town_south_inside_boulder
    )
    world.regions.append(outside_castle_town_south_inside_boulder)

    outside_castle_town_south_tektite_grotto = Region(
        "Outside Castle Town South Tektite Grotto", player, world
    )
    regions["Outside Castle Town South Tektite Grotto"] = (
        outside_castle_town_south_tektite_grotto
    )
    world.regions.append(outside_castle_town_south_tektite_grotto)

    outside_castle_town_south_tektite_grotto.locations.append(
        TPLocation(
            player,
            "Outside South Castle Town Tektite Grotto Chest",
            outside_castle_town_south_tektite_grotto,
            LOCATION_TABLE["Outside South Castle Town Tektite Grotto Chest"],
        )
    )

    lake_hylia_bridge = Region("Lake Hylia Bridge", player, world)
    regions["Lake Hylia Bridge"] = lake_hylia_bridge
    world.regions.append(lake_hylia_bridge)

    lake_hylia_bridge.locations.append(
        TPLocation(
            player,
            "Lake Hylia Bridge Vines Chest",
            lake_hylia_bridge,
            LOCATION_TABLE["Lake Hylia Bridge Vines Chest"],
        )
    )

    lake_hylia_bridge.locations.append(
        TPLocation(
            player,
            "Lake Hylia Bridge Owl Statue Chest",
            lake_hylia_bridge,
            LOCATION_TABLE["Lake Hylia Bridge Owl Statue Chest"],
        )
    )

    lake_hylia_bridge.locations.append(
        TPLocation(
            player,
            "Lake Hylia Bridge Owl Statue Sky Character",
            lake_hylia_bridge,
            LOCATION_TABLE["Lake Hylia Bridge Owl Statue Sky Character"],
        )
    )

    lake_hylia_bridge.locations.append(
        TPLocation(
            player,
            "Lake Hylia Bridge Male Mantis",
            lake_hylia_bridge,
            LOCATION_TABLE["Lake Hylia Bridge Male Mantis"],
        )
    )

    lake_hylia_bridge.locations.append(
        TPLocation(
            player,
            "Lake Hylia Bridge Female Mantis",
            lake_hylia_bridge,
            LOCATION_TABLE["Lake Hylia Bridge Female Mantis"],
        )
    )

    lake_hylia_bridge_grotto_ledge = Region(
        "Lake Hylia Bridge Grotto Ledge", player, world
    )
    regions["Lake Hylia Bridge Grotto Ledge"] = lake_hylia_bridge_grotto_ledge
    world.regions.append(lake_hylia_bridge_grotto_ledge)

    lake_hylia_bridge_grotto_ledge.locations.append(
        TPLocation(
            player,
            "Lake Hylia Bridge Cliff Chest",
            lake_hylia_bridge_grotto_ledge,
            LOCATION_TABLE["Lake Hylia Bridge Cliff Chest"],
        )
    )

    lake_hylia_bridge_grotto_ledge.locations.append(
        TPLocation(
            player,
            "Lake Hylia Bridge Cliff Poe",
            lake_hylia_bridge_grotto_ledge,
            LOCATION_TABLE["Lake Hylia Bridge Cliff Poe"],
        )
    )

    lake_hylia_bridge_bubble_grotto = Region(
        "Lake Hylia Bridge Bubble Grotto", player, world
    )
    regions["Lake Hylia Bridge Bubble Grotto"] = lake_hylia_bridge_bubble_grotto
    world.regions.append(lake_hylia_bridge_bubble_grotto)

    lake_hylia_bridge_bubble_grotto.locations.append(
        TPLocation(
            player,
            "Lake Hylia Bridge Bubble Grotto Chest",
            lake_hylia_bridge_bubble_grotto,
            LOCATION_TABLE["Lake Hylia Bridge Bubble Grotto Chest"],
        )
    )

    lake_hylia = Region("Lake Hylia", player, world)
    regions["Lake Hylia"] = lake_hylia
    world.regions.append(lake_hylia)

    lake_hylia.locations.append(
        TPLocation(
            player,
            "Lake Hylia Underwater Chest",
            lake_hylia,
            LOCATION_TABLE["Lake Hylia Underwater Chest"],
        )
    )

    lake_hylia.locations.append(
        TPLocation(
            player,
            "Outside Lanayru Spring Left Statue Chest",
            lake_hylia,
            LOCATION_TABLE["Outside Lanayru Spring Left Statue Chest"],
        )
    )

    lake_hylia.locations.append(
        TPLocation(
            player,
            "Outside Lanayru Spring Right Statue Chest",
            lake_hylia,
            LOCATION_TABLE["Outside Lanayru Spring Right Statue Chest"],
        )
    )

    lake_hylia.locations.append(
        TPLocation(
            player,
            "Flight By Fowl Top Platform Reward",
            lake_hylia,
            LOCATION_TABLE["Flight By Fowl Top Platform Reward"],
        )
    )

    lake_hylia.locations.append(
        TPLocation(
            player,
            "Flight By Fowl Second Platform Chest",
            lake_hylia,
            LOCATION_TABLE["Flight By Fowl Second Platform Chest"],
        )
    )

    lake_hylia.locations.append(
        TPLocation(
            player,
            "Flight By Fowl Third Platform Chest",
            lake_hylia,
            LOCATION_TABLE["Flight By Fowl Third Platform Chest"],
        )
    )

    lake_hylia.locations.append(
        TPLocation(
            player,
            "Flight By Fowl Fourth Platform Chest",
            lake_hylia,
            LOCATION_TABLE["Flight By Fowl Fourth Platform Chest"],
        )
    )

    lake_hylia.locations.append(
        TPLocation(
            player,
            "Flight By Fowl Fifth Platform Chest",
            lake_hylia,
            LOCATION_TABLE["Flight By Fowl Fifth Platform Chest"],
        )
    )

    lake_hylia.locations.append(
        TPLocation(
            player,
            "Auru Gift To Fyer",
            lake_hylia,
            LOCATION_TABLE["Auru Gift To Fyer"],
        )
    )

    lake_hylia.locations.append(
        TPLocation(
            player,
            "Flight By Fowl Ledge Poe",
            lake_hylia,
            LOCATION_TABLE["Flight By Fowl Ledge Poe"],
        )
    )

    lake_hylia.locations.append(
        TPLocation(
            player,
            "Isle of Riches Poe",
            lake_hylia,
            LOCATION_TABLE["Isle of Riches Poe"],
        )
    )

    lake_hylia.locations.append(
        TPLocation(
            player,
            "Lake Hylia Alcove Poe",
            lake_hylia,
            LOCATION_TABLE["Lake Hylia Alcove Poe"],
        )
    )

    lake_hylia.locations.append(
        TPLocation(
            player,
            "Lake Hylia Dock Poe",
            lake_hylia,
            LOCATION_TABLE["Lake Hylia Dock Poe"],
        )
    )

    lake_hylia.locations.append(
        TPLocation(
            player,
            "Lake Hylia Tower Poe",
            lake_hylia,
            LOCATION_TABLE["Lake Hylia Tower Poe"],
        )
    )

    lake_hylia.locations.append(
        TPLocation(
            player,
            "Plumm Fruit Balloon Minigame",
            lake_hylia,
            LOCATION_TABLE["Plumm Fruit Balloon Minigame"],
        )
    )

    lake_hylia_cave_entrance = Region("Lake Hylia Cave Entrance", player, world)
    regions["Lake Hylia Cave Entrance"] = lake_hylia_cave_entrance
    world.regions.append(lake_hylia_cave_entrance)

    lake_hylia_lakebed_temple_entrance = Region(
        "Lake Hylia Lakebed Temple Entrance", player, world
    )
    regions["Lake Hylia Lakebed Temple Entrance"] = lake_hylia_lakebed_temple_entrance
    world.regions.append(lake_hylia_lakebed_temple_entrance)

    lake_hylia_lanayru_spring = Region("Lake Hylia Lanayru Spring", player, world)
    regions["Lake Hylia Lanayru Spring"] = lake_hylia_lanayru_spring
    world.regions.append(lake_hylia_lanayru_spring)

    lake_hylia_lanayru_spring.locations.append(
        TPLocation(
            player,
            "Lanayru Spring Underwater Left Chest",
            lake_hylia_lanayru_spring,
            LOCATION_TABLE["Lanayru Spring Underwater Left Chest"],
        )
    )

    lake_hylia_lanayru_spring.locations.append(
        TPLocation(
            player,
            "Lanayru Spring Underwater Right Chest",
            lake_hylia_lanayru_spring,
            LOCATION_TABLE["Lanayru Spring Underwater Right Chest"],
        )
    )

    lake_hylia_lanayru_spring.locations.append(
        TPLocation(
            player,
            "Lanayru Spring Back Room Left Chest",
            lake_hylia_lanayru_spring,
            LOCATION_TABLE["Lanayru Spring Back Room Left Chest"],
        )
    )

    lake_hylia_lanayru_spring.locations.append(
        TPLocation(
            player,
            "Lanayru Spring Back Room Right Chest",
            lake_hylia_lanayru_spring,
            LOCATION_TABLE["Lanayru Spring Back Room Right Chest"],
        )
    )

    lake_hylia_lanayru_spring.locations.append(
        TPLocation(
            player,
            "Lanayru Spring Back Room Lantern Chest",
            lake_hylia_lanayru_spring,
            LOCATION_TABLE["Lanayru Spring Back Room Lantern Chest"],
        )
    )

    lake_hylia_lanayru_spring.locations.append(
        TPLocation(
            player,
            "Lanayru Spring East Double Clawshot Chest",
            lake_hylia_lanayru_spring,
            LOCATION_TABLE["Lanayru Spring East Double Clawshot Chest"],
        )
    )

    lake_hylia_lanayru_spring.locations.append(
        TPLocation(
            player,
            "Lanayru Spring West Double Clawshot Chest",
            lake_hylia_lanayru_spring,
            LOCATION_TABLE["Lanayru Spring West Double Clawshot Chest"],
        )
    )

    lake_hylia_long_cave = Region("Lake Hylia Long Cave", player, world)
    regions["Lake Hylia Long Cave"] = lake_hylia_long_cave
    world.regions.append(lake_hylia_long_cave)

    lake_hylia_long_cave.locations.append(
        TPLocation(
            player,
            "Lake Lantern Cave First Chest",
            lake_hylia_long_cave,
            LOCATION_TABLE["Lake Lantern Cave First Chest"],
        )
    )

    lake_hylia_long_cave.locations.append(
        TPLocation(
            player,
            "Lake Lantern Cave Second Chest",
            lake_hylia_long_cave,
            LOCATION_TABLE["Lake Lantern Cave Second Chest"],
        )
    )

    lake_hylia_long_cave.locations.append(
        TPLocation(
            player,
            "Lake Lantern Cave Third Chest",
            lake_hylia_long_cave,
            LOCATION_TABLE["Lake Lantern Cave Third Chest"],
        )
    )

    lake_hylia_long_cave.locations.append(
        TPLocation(
            player,
            "Lake Lantern Cave Fourth Chest",
            lake_hylia_long_cave,
            LOCATION_TABLE["Lake Lantern Cave Fourth Chest"],
        )
    )

    lake_hylia_long_cave.locations.append(
        TPLocation(
            player,
            "Lake Lantern Cave Fifth Chest",
            lake_hylia_long_cave,
            LOCATION_TABLE["Lake Lantern Cave Fifth Chest"],
        )
    )

    lake_hylia_long_cave.locations.append(
        TPLocation(
            player,
            "Lake Lantern Cave Sixth Chest",
            lake_hylia_long_cave,
            LOCATION_TABLE["Lake Lantern Cave Sixth Chest"],
        )
    )

    lake_hylia_long_cave.locations.append(
        TPLocation(
            player,
            "Lake Lantern Cave Seventh Chest",
            lake_hylia_long_cave,
            LOCATION_TABLE["Lake Lantern Cave Seventh Chest"],
        )
    )

    lake_hylia_long_cave.locations.append(
        TPLocation(
            player,
            "Lake Lantern Cave Eighth Chest",
            lake_hylia_long_cave,
            LOCATION_TABLE["Lake Lantern Cave Eighth Chest"],
        )
    )

    lake_hylia_long_cave.locations.append(
        TPLocation(
            player,
            "Lake Lantern Cave Ninth Chest",
            lake_hylia_long_cave,
            LOCATION_TABLE["Lake Lantern Cave Ninth Chest"],
        )
    )

    lake_hylia_long_cave.locations.append(
        TPLocation(
            player,
            "Lake Lantern Cave Tenth Chest",
            lake_hylia_long_cave,
            LOCATION_TABLE["Lake Lantern Cave Tenth Chest"],
        )
    )

    lake_hylia_long_cave.locations.append(
        TPLocation(
            player,
            "Lake Lantern Cave Eleventh Chest",
            lake_hylia_long_cave,
            LOCATION_TABLE["Lake Lantern Cave Eleventh Chest"],
        )
    )

    lake_hylia_long_cave.locations.append(
        TPLocation(
            player,
            "Lake Lantern Cave Twelfth Chest",
            lake_hylia_long_cave,
            LOCATION_TABLE["Lake Lantern Cave Twelfth Chest"],
        )
    )

    lake_hylia_long_cave.locations.append(
        TPLocation(
            player,
            "Lake Lantern Cave Thirteenth Chest",
            lake_hylia_long_cave,
            LOCATION_TABLE["Lake Lantern Cave Thirteenth Chest"],
        )
    )

    lake_hylia_long_cave.locations.append(
        TPLocation(
            player,
            "Lake Lantern Cave Fourteenth Chest",
            lake_hylia_long_cave,
            LOCATION_TABLE["Lake Lantern Cave Fourteenth Chest"],
        )
    )

    lake_hylia_long_cave.locations.append(
        TPLocation(
            player,
            "Lake Lantern Cave End Lantern Chest",
            lake_hylia_long_cave,
            LOCATION_TABLE["Lake Lantern Cave End Lantern Chest"],
        )
    )

    lake_hylia_long_cave.locations.append(
        TPLocation(
            player,
            "Lake Lantern Cave First Poe",
            lake_hylia_long_cave,
            LOCATION_TABLE["Lake Lantern Cave First Poe"],
        )
    )

    lake_hylia_long_cave.locations.append(
        TPLocation(
            player,
            "Lake Lantern Cave Second Poe",
            lake_hylia_long_cave,
            LOCATION_TABLE["Lake Lantern Cave Second Poe"],
        )
    )

    lake_hylia_long_cave.locations.append(
        TPLocation(
            player,
            "Lake Lantern Cave Final Poe",
            lake_hylia_long_cave,
            LOCATION_TABLE["Lake Lantern Cave Final Poe"],
        )
    )

    lake_hylia_shell_blade_grotto = Region(
        "Lake Hylia Shell Blade Grotto", player, world
    )
    regions["Lake Hylia Shell Blade Grotto"] = lake_hylia_shell_blade_grotto
    world.regions.append(lake_hylia_shell_blade_grotto)

    lake_hylia_shell_blade_grotto.locations.append(
        TPLocation(
            player,
            "Lake Hylia Shell Blade Grotto Chest",
            lake_hylia_shell_blade_grotto,
            LOCATION_TABLE["Lake Hylia Shell Blade Grotto Chest"],
        )
    )

    lake_hylia_water_toadpoli_grotto = Region(
        "Lake Hylia Water Toadpoli Grotto", player, world
    )
    regions["Lake Hylia Water Toadpoli Grotto"] = lake_hylia_water_toadpoli_grotto
    world.regions.append(lake_hylia_water_toadpoli_grotto)

    lake_hylia_water_toadpoli_grotto.locations.append(
        TPLocation(
            player,
            "Lake Hylia Water Toadpoli Grotto Chest",
            lake_hylia_water_toadpoli_grotto,
            LOCATION_TABLE["Lake Hylia Water Toadpoli Grotto Chest"],
        )
    )

    upper_zoras_river = Region("Upper Zoras River", player, world)
    regions["Upper Zoras River"] = upper_zoras_river
    world.regions.append(upper_zoras_river)

    upper_zoras_river.locations.append(
        TPLocation(
            player,
            "Upper Zoras River Female Dragonfly",
            upper_zoras_river,
            LOCATION_TABLE["Upper Zoras River Female Dragonfly"],
        )
    )

    upper_zoras_river.locations.append(
        TPLocation(
            player,
            "Upper Zoras River Poe",
            upper_zoras_river,
            LOCATION_TABLE["Upper Zoras River Poe"],
        )
    )

    upper_zoras_river_izas_house = Region("Upper Zoras River Izas House", player, world)
    regions["Upper Zoras River Izas House"] = upper_zoras_river_izas_house
    world.regions.append(upper_zoras_river_izas_house)

    upper_zoras_river_izas_house.locations.append(
        TPLocation(
            player,
            "Iza Helping Hand",
            upper_zoras_river_izas_house,
            LOCATION_TABLE["Iza Helping Hand"],
        )
    )

    upper_zoras_river_izas_house.locations.append(
        TPLocation(
            player,
            "Iza Raging Rapids Minigame",
            upper_zoras_river_izas_house,
            LOCATION_TABLE["Iza Raging Rapids Minigame"],
        )
    )

    fishing_hole = Region("Fishing Hole", player, world)
    regions["Fishing Hole"] = fishing_hole
    world.regions.append(fishing_hole)

    fishing_hole.locations.append(
        TPLocation(
            player,
            "Fishing Hole Heart Piece",
            fishing_hole,
            LOCATION_TABLE["Fishing Hole Heart Piece"],
        )
    )

    fishing_hole.locations.append(
        TPLocation(
            player,
            "Fishing Hole Bottle",
            fishing_hole,
            LOCATION_TABLE["Fishing Hole Bottle"],
        )
    )

    fishing_hole_house = Region("Fishing Hole House", player, world)
    regions["Fishing Hole House"] = fishing_hole_house
    world.regions.append(fishing_hole_house)

    zoras_domain = Region("Zoras Domain", player, world)
    regions["Zoras Domain"] = zoras_domain
    world.regions.append(zoras_domain)

    zoras_domain.locations.append(
        TPLocation(
            player,
            "Zoras Domain Chest By Mother and Child Isles",
            zoras_domain,
            LOCATION_TABLE["Zoras Domain Chest By Mother and Child Isles"],
        )
    )

    zoras_domain.locations.append(
        TPLocation(
            player,
            "Zoras Domain Chest Behind Waterfall",
            zoras_domain,
            LOCATION_TABLE["Zoras Domain Chest Behind Waterfall"],
        )
    )

    zoras_domain.locations.append(
        TPLocation(
            player,
            "Zoras Domain Male Dragonfly",
            zoras_domain,
            LOCATION_TABLE["Zoras Domain Male Dragonfly"],
        )
    )

    zoras_domain.locations.append(
        TPLocation(
            player,
            "Zoras Domain Mother and Child Isle Poe",
            zoras_domain,
            LOCATION_TABLE["Zoras Domain Mother and Child Isle Poe"],
        )
    )

    zoras_domain.locations.append(
        TPLocation(
            player,
            "Zoras Domain Waterfall Poe",
            zoras_domain,
            LOCATION_TABLE["Zoras Domain Waterfall Poe"],
        )
    )

    zoras_domain_west_ledge = Region("Zoras Domain West Ledge", player, world)
    regions["Zoras Domain West Ledge"] = zoras_domain_west_ledge
    world.regions.append(zoras_domain_west_ledge)

    zoras_throne_room = Region("Zoras Domain Throne Room", player, world)
    regions["Zoras Domain Throne Room"] = zoras_throne_room
    world.regions.append(zoras_throne_room)

    zoras_throne_room.locations.append(
        TPLocation(
            player,
            "Zoras Domain Light All Torches Chest",
            zoras_throne_room,
            LOCATION_TABLE["Zoras Domain Light All Torches Chest"],
        )
    )

    zoras_throne_room.locations.append(
        TPLocation(
            player,
            "Zoras Domain Extinguish All Torches Chest",
            zoras_throne_room,
            LOCATION_TABLE["Zoras Domain Extinguish All Torches Chest"],
        )
    )

    zoras_throne_room.locations.append(
        TPLocation(
            player,
            "Zoras Domain Underwater Goron",
            zoras_throne_room,
            LOCATION_TABLE["Zoras Domain Underwater Goron"],
        )
    )

    outside_links_house = Region("Outside Links House", player, world)
    regions["Outside Links House"] = outside_links_house
    world.regions.append(outside_links_house)

    ordon_links_house = Region("Ordon Links House", player, world)
    regions["Ordon Links House"] = ordon_links_house
    world.regions.append(ordon_links_house)

    ordon_links_house.locations.append(
        TPLocation(
            player,
            "Wooden Sword Chest",
            ordon_links_house,
            LOCATION_TABLE["Wooden Sword Chest"],
        )
    )

    ordon_links_house.locations.append(
        TPLocation(
            player,
            "Links Basement Chest",
            ordon_links_house,
            LOCATION_TABLE["Links Basement Chest"],
        )
    )

    ordon_village = Region("Ordon Village", player, world)
    regions["Ordon Village"] = ordon_village
    world.regions.append(ordon_village)

    ordon_village.locations.append(
        TPLocation(
            player,
            "Uli Cradle Delivery",
            ordon_village,
            LOCATION_TABLE["Uli Cradle Delivery"],
        )
    )

    ordon_seras_shop = Region("Ordon Seras Shop", player, world)
    regions["Ordon Seras Shop"] = ordon_seras_shop
    world.regions.append(ordon_seras_shop)

    ordon_seras_shop.locations.append(
        TPLocation(
            player,
            "Ordon Cat Rescue",
            ordon_seras_shop,
            LOCATION_TABLE["Ordon Cat Rescue"],
        )
    )

    ordon_seras_shop.locations.append(
        TPLocation(
            player,
            "Sera Shop Slingshot",
            ordon_seras_shop,
            LOCATION_TABLE["Sera Shop Slingshot"],
        )
    )

    ordon_shield_house = Region("Ordon Shield House", player, world)
    regions["Ordon Shield House"] = ordon_shield_house
    world.regions.append(ordon_shield_house)

    ordon_shield_house.locations.append(
        TPLocation(
            player,
            "Ordon Shield",
            ordon_shield_house,
            LOCATION_TABLE["Ordon Shield"],
        )
    )

    ordon_sword_house = Region("Ordon Sword House", player, world)
    regions["Ordon Sword House"] = ordon_sword_house
    world.regions.append(ordon_sword_house)

    ordon_sword_house.locations.append(
        TPLocation(
            player,
            "Ordon Sword",
            ordon_sword_house,
            LOCATION_TABLE["Ordon Sword"],
        )
    )

    ordon_bos_house_left_door = Region("Ordon Bos House Left Door", player, world)
    regions["Ordon Bos House Left Door"] = ordon_bos_house_left_door
    world.regions.append(ordon_bos_house_left_door)

    ordon_bos_house_right_door = Region("Ordon Bos House Right Door", player, world)
    regions["Ordon Bos House Right Door"] = ordon_bos_house_right_door
    world.regions.append(ordon_bos_house_right_door)

    ordon_bos_house = Region("Ordon Bos House", player, world)
    regions["Ordon Bos House"] = ordon_bos_house
    world.regions.append(ordon_bos_house)

    ordon_bos_house.locations.append(
        TPLocation(
            player,
            "Wrestling With Bo",
            ordon_bos_house,
            LOCATION_TABLE["Wrestling With Bo"],
        )
    )

    ordon_ranch_entrance = Region("Ordon Ranch Entrance", player, world)
    regions["Ordon Ranch Entrance"] = ordon_ranch_entrance
    world.regions.append(ordon_ranch_entrance)

    ordon_ranch = Region("Ordon Ranch", player, world)
    regions["Ordon Ranch"] = ordon_ranch
    world.regions.append(ordon_ranch)

    ordon_ranch.locations.append(
        TPLocation(
            player,
            "Herding Goats Reward",
            ordon_ranch,
            LOCATION_TABLE["Herding Goats Reward"],
        )
    )

    ordon_ranch_stable = Region("Ordon Ranch Stable", player, world)
    regions["Ordon Ranch Stable"] = ordon_ranch_stable
    world.regions.append(ordon_ranch_stable)

    ordon_ranch_grotto = Region("Ordon Ranch Grotto", player, world)
    regions["Ordon Ranch Grotto"] = ordon_ranch_grotto
    world.regions.append(ordon_ranch_grotto)

    ordon_ranch_grotto.locations.append(
        TPLocation(
            player,
            "Ordon Ranch Grotto Lantern Chest",
            ordon_ranch_grotto,
            LOCATION_TABLE["Ordon Ranch Grotto Lantern Chest"],
        )
    )

    ordon_spring = Region("Ordon Spring", player, world)
    regions["Ordon Spring"] = ordon_spring
    world.regions.append(ordon_spring)

    ordon_spring.locations.append(
        TPLocation(
            player,
            "Ordon Spring Golden Wolf",
            ordon_spring,
            LOCATION_TABLE["Ordon Spring Golden Wolf"],
        )
    )

    ordon_bridge = Region("Ordon Bridge", player, world)
    regions["Ordon Bridge"] = ordon_bridge
    world.regions.append(ordon_bridge)

    snowpeak_climb_lower = Region("Snowpeak Climb Lower", player, world)
    regions["Snowpeak Climb Lower"] = snowpeak_climb_lower
    world.regions.append(snowpeak_climb_lower)

    snowpeak_climb_lower.locations.append(
        TPLocation(
            player,
            "Ashei Sketch",
            snowpeak_climb_lower,
            LOCATION_TABLE["Ashei Sketch"],
        )
    )

    snowpeak_climb_upper = Region("Snowpeak Climb Upper", player, world)
    regions["Snowpeak Climb Upper"] = snowpeak_climb_upper
    world.regions.append(snowpeak_climb_upper)

    snowpeak_climb_upper.locations.append(
        TPLocation(
            player,
            "Snowpeak Above Freezard Grotto Poe",
            snowpeak_climb_upper,
            LOCATION_TABLE["Snowpeak Above Freezard Grotto Poe"],
        )
    )

    snowpeak_climb_upper.locations.append(
        TPLocation(
            player,
            "Snowpeak Blizzard Poe",
            snowpeak_climb_upper,
            LOCATION_TABLE["Snowpeak Blizzard Poe"],
        )
    )

    snowpeak_climb_upper.locations.append(
        TPLocation(
            player,
            "Snowpeak Poe Among Trees",
            snowpeak_climb_upper,
            LOCATION_TABLE["Snowpeak Poe Among Trees"],
        )
    )

    snowpeak_ice_keese_grotto = Region("Snowpeak Ice Keese Grotto", player, world)
    regions["Snowpeak Ice Keese Grotto"] = snowpeak_ice_keese_grotto
    world.regions.append(snowpeak_ice_keese_grotto)

    snowpeak_freezard_grotto = Region("Snowpeak Freezard Grotto", player, world)
    regions["Snowpeak Freezard Grotto"] = snowpeak_freezard_grotto
    world.regions.append(snowpeak_freezard_grotto)

    snowpeak_freezard_grotto.locations.append(
        TPLocation(
            player,
            "Snowpeak Freezard Grotto Chest",
            snowpeak_freezard_grotto,
            LOCATION_TABLE["Snowpeak Freezard Grotto Chest"],
        )
    )

    snowpeak_summit_upper = Region("Snowpeak Summit Upper", player, world)
    regions["Snowpeak Summit Upper"] = snowpeak_summit_upper
    world.regions.append(snowpeak_summit_upper)

    snowpeak_summit_upper.locations.append(
        TPLocation(
            player,
            "Snowpeak Cave Ice Lantern Chest",
            snowpeak_summit_upper,
            LOCATION_TABLE["Snowpeak Cave Ice Lantern Chest"],
        )
    )

    snowpeak_summit_upper.locations.append(
        TPLocation(
            player,
            "Snowboard Racing Prize",
            snowpeak_summit_upper,
            LOCATION_TABLE["Snowboard Racing Prize"],
        )
    )

    snowpeak_summit_upper.locations.append(
        TPLocation(
            player,
            "Snowpeak Cave Ice Poe",
            snowpeak_summit_upper,
            LOCATION_TABLE["Snowpeak Cave Ice Poe"],
        )
    )

    snowpeak_summit_lower = Region("Snowpeak Summit Lower", player, world)
    regions["Snowpeak Summit Lower"] = snowpeak_summit_lower
    world.regions.append(snowpeak_summit_lower)

    snowpeak_summit_lower.locations.append(
        TPLocation(
            player,
            "Snowpeak Icy Summit Poe",
            snowpeak_summit_lower,
            LOCATION_TABLE["Snowpeak Icy Summit Poe"],
        )
    )
    # Connect Menu to starting region
    menu.connect(regions["Outside Links House"])


def create_portal_location(world: MultiWorld, player: int):
    if "Snowpeak Portal" in LOCATION_TABLE:
        world.get_region("Snowpeak Summit Upper", player).locations.append(
            TPLocation(
                player,
                "Snowpeak Portal",
                world.get_region("Snowpeak Summit Upper", player),
                LOCATION_TABLE["Snowpeak Portal"],
            )
        )
    if "Zoras Domain Portal" in LOCATION_TABLE:
        world.get_region("Zoras Domain Throne Room", player).locations.append(
            TPLocation(
                player,
                "Zoras Domain Portal",
                world.get_region("Zoras Domain Throne Room", player),
                LOCATION_TABLE["Zoras Domain Portal"],
            )
        )
    if "Upper Zoras River Portal" in LOCATION_TABLE:
        world.get_region("Upper Zoras River", player).locations.append(
            TPLocation(
                player,
                "Upper Zoras River Portal",
                world.get_region("Upper Zoras River", player),
                LOCATION_TABLE["Upper Zoras River Portal"],
            )
        )
    if "Lake Hylia Portal" in LOCATION_TABLE:
        world.get_region("Lake Hylia", player).locations.append(
            TPLocation(
                player,
                "Lake Hylia Portal",
                world.get_region("Lake Hylia", player),
                LOCATION_TABLE["Lake Hylia Portal"],
            )
        )
    if "Castle Town Portal" in LOCATION_TABLE:
        world.get_region("Outside Castle Town West", player).locations.append(
            TPLocation(
                player,
                "Castle Town Portal",
                world.get_region("Outside Castle Town West", player),
                LOCATION_TABLE["Castle Town Portal"],
            )
        )
    if "Gerudo Desert Portal" in LOCATION_TABLE:
        world.get_region(
            "Gerudo Desert Cave of Ordeals Plateau", player
        ).locations.append(
            TPLocation(
                player,
                "Gerudo Desert Portal",
                world.get_region("Gerudo Desert Cave of Ordeals Plateau", player),
                LOCATION_TABLE["Gerudo Desert Portal"],
            )
        )
    if "Sacred Grove Portal" in LOCATION_TABLE:
        world.get_region("Sacred Grove Lower", player).locations.append(
            TPLocation(
                player,
                "Sacred Grove Portal",
                world.get_region("Sacred Grove Lower", player),
                LOCATION_TABLE["Sacred Grove Portal"],
            )
        )
    if "North Faron Portal" in LOCATION_TABLE:
        world.get_region("North Faron Woods", player).locations.append(
            TPLocation(
                player,
                "North Faron Portal",
                world.get_region("North Faron Woods", player),
                LOCATION_TABLE["North Faron Portal"],
            )
        )
    if "South Faron Portal" in LOCATION_TABLE:
        world.get_region("South Faron Woods", player).locations.append(
            TPLocation(
                player,
                "South Faron Portal",
                world.get_region("South Faron Woods", player),
                LOCATION_TABLE["South Faron Portal"],
            )
        )
    if "Kakariko Village Portal" in LOCATION_TABLE:
        world.get_region("Lower Kakariko Village", player).locations.append(
            TPLocation(
                player,
                "Kakariko Village Portal",
                world.get_region("Lower Kakariko Village", player),
                LOCATION_TABLE["Kakariko Village Portal"],
            )
        )
    if "Bridge of Eldin Portal" in LOCATION_TABLE:
        world.get_region("Eldin Field", player).locations.append(
            TPLocation(
                player,
                "Bridge of Eldin Portal",
                world.get_region("Eldin Field", player),
                LOCATION_TABLE["Bridge of Eldin Portal"],
            )
        )
    if "Kakariko Gorge Portal" in LOCATION_TABLE:
        world.get_region("Kakariko Gorge", player).locations.append(
            TPLocation(
                player,
                "Kakariko Gorge Portal",
                world.get_region("Kakariko Gorge", player),
                LOCATION_TABLE["Kakariko Gorge Portal"],
            )
        )
    if "Death Mountain Portal" in LOCATION_TABLE:
        world.get_region("Death Mountain Volcano", player).locations.append(
            TPLocation(
                player,
                "Death Mountain Portal",
                world.get_region("Death Mountain Volcano", player),
                LOCATION_TABLE["Death Mountain Portal"],
            )
        )

    if "Mirror Chamber Portal" in LOCATION_TABLE:
        world.get_region("Mirror Chamber Upper", player).locations.append(
            TPLocation(
                player,
                "Mirror Chamber Portal",
                world.get_region("Mirror Chamber Upper", player),
                LOCATION_TABLE["Mirror Chamber Portal"],
            )
        )

    if "Ordon Spring Portal" in LOCATION_TABLE:
        world.get_region("Ordon Spring", player).locations.append(
            TPLocation(
                player,
                "Ordon Spring Portal",
                world.get_region("Ordon Spring", player),
                LOCATION_TABLE["Ordon Spring Portal"],
            )
        )
