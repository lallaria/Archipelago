import typing
from enum import Enum

from BaseClasses import MultiWorld, Region, Entrance, Location
#from .Options import SMOOptions
from .Locations import SMOLocation, loc_Cap, loc_Cascade, loc_Cascade_Revisit,  \
    loc_Sand, loc_Lake, loc_Wooded, loc_Cloud, loc_Lost, loc_Metro, loc_Snow, \
    loc_Seaside, loc_Luncheon, loc_Ruined, loc_Bowser, loc_Moon, locations_table, \
    post_game_locations_table, loc_Dark, loc_Darker, special_locations_table

from .Logic import count_moons, total_moons

class SMORegion(Region):
    subregions: typing.List[Region] = []

def create_regions(self, world, player):
    # Cascade Regions
    regCascade = Region("Menu", player, world, "Cascade Kingdom")
    create_locs(regCascade, *loc_Cascade.keys())
    world.regions.append(regCascade)

    regCascadeRe = Region("Cascade Revisit", player, world, "Cascade Kingdom 2")
    create_locs(regCascadeRe, *loc_Cascade_Revisit.keys())
    world.regions.append(regCascadeRe)

    # Cap
    regCap = Region("Cap", player, world, "Cap Kingdom")
    create_locs(regCap, *loc_Cap.keys())
    world.regions.append(regCap)

    # Sand Regions
    regSand = Region("Sand", player, world, "Sand Kingdom")
    create_locs(regSand, *loc_Sand.keys())
    world.regions.append(regSand)

    # Lake Regions
    regLake = Region("Lake", player, world, "Lake Kingdom")
    create_locs(regLake, *loc_Lake.keys())
    world.regions.append(regLake)

    # Wooded
    regWooded = Region("Wooded" , player, world, "Wooded Kingdom")
    create_locs(regWooded, *loc_Wooded.keys())
    world.regions.append(regWooded)

    # Cloud
    regCloud = Region("Cloud", player, world, "Cloud Kingdom")
    create_locs(regCloud, *loc_Cloud.keys())
    world.regions.append(regCloud)

    # Lost
    regLost = Region("Lost", player, world, "Lost Kingdom")
    create_locs(regLost, *loc_Lost.keys())
    world.regions.append(regLost)

    # Metro
    regMetro = Region("Metro", player, world, "Metro Kingdom")
    create_locs(regMetro, *loc_Metro.keys())
    world.regions.append(regMetro)

    # Snow
    regSnow = Region("Snow", player, world, "Snow Kingdom")
    create_locs(regSnow, *loc_Snow.keys())
    world.regions.append(regSnow)

    # Seaside
    regSeaside = Region("Seaside", player, world, "Seaside Kingdom")
    create_locs(regSeaside, *loc_Seaside.keys())
    world.regions.append(regSeaside)

    # Luncheon
    regLuncheon = Region("Luncheon", player, world, "Luncheon Kingdom")
    create_locs(regLuncheon, *loc_Luncheon.keys())
    world.regions.append(regLuncheon)

    # Ruined
    regRuined = Region("Ruined", player, world, "Ruined Kingdom")
    create_locs(regRuined, *loc_Ruined.keys())
    world.regions.append(regRuined)

    # Bowser
    regBowser = Region("Bowser", player, world, "Bowser Kingdom")
    create_locs(regBowser, *loc_Bowser.keys())
    world.regions.append(regBowser)

    # Moon
    regMoon = Region("Moon", player, world, "Moon Kingdom")
    create_locs(regMoon, *loc_Moon.keys())
    world.regions.append(regMoon)

    # Post Game
    regPostGame = Region("Post Game", player, world, "Post Game Moons")
    create_locs(regPostGame, *post_game_locations_table.keys(), locs_table= post_game_locations_table)
    world.regions.append(regPostGame)

    # Dark Side
    regDark = Region("Dark", player, world, "Dark Side")
    create_locs(regDark, *loc_Dark,  locs_table= special_locations_table)
    world.regions.append(regDark)

    # Darker Side
    regDarker = Region("Darker", player, world, "Darker Side")
    create_locs(regDarker, *loc_Darker, locs_table=special_locations_table)
    world.regions.append(regDarker)

    # Progression Connections
    regCascade.connect(regSand, "Sand Enter", lambda state: count_moons(self, state, "Cascade", player) >= 5)
    regSand.connect(regCap)
    regSand.connect(regCascadeRe)
    regSand.connect(regLake, "Lake Enter", lambda state: count_moons(self, state, "Sand", player) >= 16)
    regLake.connect(regWooded, "Wooded Enter", lambda state: count_moons(self, state, "Lake", player) >= 8)
    regWooded.connect(regLost, "Lost Enter", lambda state: count_moons(self, state, "Wooded", player) >= 16)
    regLost.connect(regCloud, "Cloud Available", lambda state: count_moons(self, state, "Lost", player) >= 10)
    regLost.connect(regMetro, "Metro Enter", lambda state: count_moons(self, state, "Lost", player) >= 10)
    regMetro.connect(regSnow, "Snow Enter", lambda state: count_moons(self, state, "Metro", player) >= 20)
    regSnow.connect(regSeaside, "Seaside Enter", lambda state: count_moons(self, state, "Snow", player) >= 10)
    regSeaside.connect(regLuncheon, "Enter Luncheon", lambda state: count_moons(self, state, "Seaside", player) >= 10)
    regLuncheon.connect(regRuined, "Enter Ruined", lambda state: count_moons(self, state, "Luncheon", player) >= 18)
    regRuined.connect(regBowser,"Enter Bowser", lambda state: count_moons(self, state, "Ruined", player) >= 3)
    regBowser.connect(regMoon, "Enter Moon", lambda state: count_moons(self, state, "Bowser", player) >= 8)
    regMoon.connect(regPostGame)
    regPostGame.connect(regDark, "Dark Access", lambda state: total_moons(self, state, player) >= 250)
    regPostGame.connect(regDarker, "Darker Access", lambda state: total_moons(self, state, player) >= 500)

def create_locs(reg: Region, *locs: str, locs_table = locations_table):
    reg.locations += ([SMOLocation(reg.player, loc_name, locs_table[loc_name], reg) for loc_name in locs])

