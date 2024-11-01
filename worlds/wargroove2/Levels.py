from typing import List

from BaseClasses import Region, Entrance, MultiWorld
from .Locations import location_table, Wargroove2Location
from worlds.generic.Rules import set_rule

region_names: [str] = ["North 1", "East 1", "South 1", "West 1",
                       "North 2A", "North 2B", "North 2C",
                       "East 2A", "East 2B", "East 2C",
                       "South 2A", "South 2B", "South 2C",
                       "West 2A", "West 2B", "West 2C",
                       "North 3A", "North 3B", "North 3C",
                       "East 3A", "East 3B", "East 3C",
                       "South 3A", "South 3B", "South 3C",
                       "West 3A", "West 3B", "West 3C"]
FINAL_LEVEL_1 = "Northern Finale"
FINAL_LEVEL_2 = "Eastern Finale"
FINAL_LEVEL_3 = "Southern Finale"
FINAL_LEVEL_4 = "Western Finale"

LEVEL_COUNT = 28
FINAL_LEVEL_COUNT = 4


def set_region_exit_rules(region: Region, world: MultiWorld, player: int, locations: List[str], operator: str = "or"):
    if operator == "or":
        exit_rule = lambda state, world=world, player=player: any(
            world.get_location(location, player).access_rule(state) for location in locations)
    else:
        exit_rule = lambda state, world=world, player=player: all(
            world.get_location(location, player).access_rule(state) for location in locations)
    for region_exit in region.exits:
        region_exit.access_rule = exit_rule


class Wargroove2Level:
    player: int
    name: str
    file_name: str
    location_rules: dict
    region: Region
    victory_locations: List[str]
    low_victory_checks: bool
    has_ocean: bool

    def __init__(self, name: str, file_name: str, location_rules: dict, victory_locations: List[str] = [],
                 low_victory_checks: bool = True, has_ocean: bool = True):
        if victory_locations is None:
            victory_locations = []
        self.name = name
        self.file_name = file_name
        self.location_rules = location_rules
        self.low_victory_checks = low_victory_checks
        self.has_ocean = has_ocean
        if victory_locations:
            self.victory_locations = victory_locations
        else:
            self.victory_locations = [name + ': Victory']

    def define_access_rules(self, world: MultiWorld, additional_rule=lambda state: True):
        for location_name, rule in self.location_rules.items():
            set_rule(world.get_location(location_name, self.player), lambda state, rule=rule:
            state.can_reach(self.region, 'Region', self.player) and rule(state) and additional_rule(state))
        set_region_exit_rules(self.region, world, self.player, self.victory_locations, operator='and')

    def define_region(self, name: str, world: MultiWorld, exits=None) -> Region:
        self.region = Region(name, self.player, world)
        if self.location_rules.keys():
            for location in self.location_rules.keys():
                loc_id = location_table.get(location, 0)
                location = Wargroove2Location(self.player, location, loc_id, self.region)
                self.region.locations.append(location)
        if exits:
            for exit in exits:
                self.region.exits.append(Entrance(self.player, f"{name} exits to {exit}", self.region))

        return self.region


def get_level_table(player: int) -> List[Wargroove2Level]:
    levels = [
        Wargroove2Level(
            name="Spire Fire",
            file_name="Spire_Fire.json",
            location_rules={
                "Spire Fire: Victory": lambda state: state.has_any({"Mage", "Witch"}, player),
                "Spire Fire: Kill Enemy Sky Rider": lambda state: state.has("Witch", player),
                "Spire Fire: Win without losing your Dragon": lambda state: state.has_any({"Mage", "Witch"}, player)
            },
            has_ocean=False
        ),
        Wargroove2Level(
            name="Nuru's Vengeance",
            file_name="Nuru_Vengeance.json",
            location_rules={
                "Nuru's Vengeance: Victory": lambda state: state.has("Knight", player),
                "Nuru's Vengeance: Defeat all Dogs": lambda state: state.has("Knight", player),
                "Nuru's Vengeance: Spearman Destroys the Gate": lambda state: state.has_all(
                    {"Knight", "Spearman"}, player)
            },
            has_ocean=False
        ),
        Wargroove2Level(
            name="Cherrystone Landing",
            file_name="Cherrystone_Landing.json",
            location_rules={
                "Cherrystone Landing: Victory": lambda state: state.has_all({"Warship", "Barge", "Landing Event"},
                                                                            player),
                "Cherrystone Landing: Smacked a Trebuchet": lambda state: state.has_all(
                    {"Warship", "Barge", "Landing Event", "Golem"}, player),
                "Cherrystone Landing: Smacked a Fortified Village": lambda state: state.has_all(
                    {"Barge", "Landing Event", "Golem"}, player)
            },
            low_victory_checks=False
        ),
        Wargroove2Level(
            name="Slippery Bridge",
            file_name="Slippery_Bridge.json",
            location_rules={
                "Slippery Bridge: Victory": lambda state: state.has("Frog", player),
                "Slippery Bridge: Control all Sea Villages": lambda state: state.has("Merfolk", player),
            }
        ),
        Wargroove2Level(
            name="Den-Two-Away",
            file_name="Den-Two-Away.json",
            location_rules={
                "Den-Two-Away: Victory": lambda state: state.has("Harpy", player),
                "Den-Two-Away: Commander Captures the Lumbermill": lambda state: state.has_all({"Harpy", "Balloon"},
                                                                                               player),
            }
        ),
        Wargroove2Level(
            name="Skydiving",
            file_name="Skydiving.json",
            location_rules={
                "Skydiving: Victory": lambda state: state.has_all({"Balloon", "Airstrike Event"}, player),
                "Skydiving: Dragon Defeats Stronghold": lambda state: state.has_all(
                    {"Balloon", "Airstrike Event", "Dragon"}, player),
            },
            has_ocean=False
        ),
        Wargroove2Level(
            name="Sunken Forest",
            file_name="Sunken_Forest.json",
            location_rules={
                "Sunken Forest: Victory": lambda state: state.has_any({"Mage", "Harpoon Ship"}, player),
                "Sunken Forest: High Ground": lambda state: state.has("Archer", player),
                "Sunken Forest: Coastal Siege": lambda state: state.has("Warship", player) and state.has_any(
                    {"Mage", "Harpoon Ship"}, player),
            }
        ),
        Wargroove2Level(
            name="Tenri's Mistake",
            file_name="Tenris_Mistake.json",
            location_rules={
                "Tenri's Mistake: Victory": lambda state: state.has_any({"Balloon", "Air Trooper"}, player),
                "Tenri's Mistake: Mighty Barracks": lambda state: state.has_any({"Balloon", "Air Trooper"}, player),
                "Tenri's Mistake: Commander Arrives": lambda state: state.has("Balloon", player),
            }
        ),
        Wargroove2Level(
            name="Enmity Cliffs",
            file_name="Enmity_Cliffs.json",
            location_rules={
                "Enmity Cliffs: Victory": lambda state: state.has_all({"Spearman", "Bridges Event"}, player),
                "Enmity Cliffs: Spear Flood": lambda state: state.has("Spearman", player),
                "Enmity Cliffs: Across the Gap": lambda state: state.has_any({"Archer", "Rifleman"}, player),
            },
            has_ocean=False
        ),
        Wargroove2Level(
            name="Terrible Tributaries",
            file_name="Terrible_Tributaries.json",
            location_rules={
                "Terrible Tributaries: Victory": lambda state: state.has("River Boat", player),
                "Terrible Tributaries: Swimming Knights": lambda state: state.has_all({"Merfolk", "River Boat"},
                                                                                      player),
                "Terrible Tributaries: Steal Code Names": lambda state: state.has_all({"Thief", "River Boat"}, player),
            }
        ),
        Wargroove2Level(
            name="Beached",
            file_name="Beached.json",
            location_rules={
                "Beached: Victory": lambda state: state.has("Knight", player),
                "Beached: Turtle Power": lambda state: state.has_all({"Turtle", "Knight"}, player),
                "Beached: Happy Turtle": lambda state: state.has_all({"Turtle", "Knight"}, player),
            }
        ),
        Wargroove2Level(
            name="Portal Peril",
            file_name="Portal_Peril.json",
            location_rules={
                "Portal Peril: Victory": lambda state: state.has("Wagon", player),
                "Portal Peril: Unleash the Hounds": lambda state: state.has("Wagon", player),
                "Portal Peril: Overcharged": lambda state: state.has("Wagon", player),
            },
            has_ocean=False
        ),
        Wargroove2Level(
            name="Riflemen Blockade",
            file_name="Riflemen_Blockade.json",
            location_rules={
                "Riflemen Blockade: Victory": lambda state: state.has("Rifleman", player),
                "Riflemen Blockade: From the Mountains": lambda state: state.has_all({"Rifleman", "Harpy"}, player),
                "Riflemen Blockade: To the Road": lambda state: state.has_all({"Rifleman", "Dragon"}, player),
            },
            has_ocean=False
        ),
        Wargroove2Level(
            name="Towers of the Abyss",
            file_name="Towers_of_the_Abyss.json",
            location_rules={
                "Towers of the Abyss: Victory": lambda state: state.has("Ballista", player),
                "Towers of the Abyss: Siege Master": lambda state: state.has_all({"Ballista", "Trebuchet"}, player),
                "Towers of the Abyss: Perfect Defense": lambda state: state.has_all({"Ballista", "Walls Event"},
                                                                                    player),
            },
            has_ocean=False
        ),
        Wargroove2Level(
            name="Wagon Freeway",
            file_name="Wagon_Freeway.json",
            location_rules={
                "Wagon Freeway: Victory": lambda state: state.has_all({"Wagon", "Spearman"}, player),
                "Wagon Freeway: All Mine Now": lambda state: True,
                "Wagon Freeway: Pigeon Carrier": lambda state: state.has("Air Trooper", player),
            },
            has_ocean=False
        ),
        Wargroove2Level(
            name="Kraken Strait",
            file_name="Kraken_Strait.json",
            location_rules={
                "Kraken Strait: Victory": lambda state: state.has_all({"Frog", "Kraken"}, player),
                "Kraken Strait: Well Defended": lambda state: state.has_all({"Frog", "Kraken"}, player),
                "Kraken Strait: Clipped Wings": lambda state: state.has("Harpoon Ship", player),
            }
        ),
        Wargroove2Level(
            name="Gnarled Mountaintop",
            file_name="Gnarled_Mountaintop.json",
            location_rules={
                "Gnarled Mountaintop: Victory": lambda state: state.has("Harpy", player),
                "Gnarled Mountaintop: Watch the Watchtower": lambda state: state.has("Harpy", player),
                "Gnarled Mountaintop: Vine Skip": lambda state: state.has("Air Trooper", player),
            },
            has_ocean=False
        ),
        Wargroove2Level(
            name="Gold Rush",
            file_name="Gold_Rush.json",
            location_rules={
                "Gold Rush: Victory": lambda state: state.has("Thief", player) and
                                                    state.has_any({"Rifleman", "Merfolk", "Warship"}, player),
                "Gold Rush: Lumber Island": lambda state: state.has_any({"Merfolk", "River Boat", "Barge"}, player),
                "Gold Rush: Starglass Rush": lambda state: state.has_any({"River Boat", "Barge"}, player),
            }
        ),
        Wargroove2Level(
            name="Finishing Blow",
            file_name="Finishing_Blow.json",
            location_rules={
                "Finishing Blow: Victory": lambda state: state.has("Witch", player),
                "Finishing Blow: Mass Destruction": lambda state: state.has("Witch", player),
                "Finishing Blow: Defortification": lambda state: state.has("Thief", player),
            }
        ),
        Wargroove2Level(
            name="Frantic Inlet",
            file_name="Frantic_Inlet.json",
            location_rules={
                "Frantic Inlet: Victory": lambda state: state.has("Turtle", player) and
                                                        state.has_any({"Barge", "Knight"}, player),
                "Frantic Inlet: Plug the Gap": lambda state: state.has("Spearman", player),
                "Frantic Inlet: Portal Detour": lambda state: state.has_all({"Turtle", "Barge"}, player),
            }
        ),
        Wargroove2Level(
            name="Operation Seagull",
            file_name="Operation_Seagull.json",
            location_rules={
                "Operation Seagull: Victory": lambda state: state.has("Merfolk", player) and
                                                            state.has_any({"Harpoon Ship", "Witch"}, player) and
                                                            state.has_any({"Turtle", "Harpy"}, player),
                "Operation Seagull: Crack the Crystal": lambda state: state.has_any({"Warship", "Kraken"}, player),
                "Operation Seagull: Counter Break": lambda state: state.has("Dragon", player) and
                                                                  state.has_all({"Harpoon Ship", "Witch"}, player),
            }
        ),
        Wargroove2Level(
            name="Air Support",
            file_name="Air_Support.json",
            location_rules={
                "Air Support: Victory": lambda state: state.has_all({"Dragon", "Bridges Event"}, player),
                "Air Support: Roadkill": lambda state: state.has_all({"Dragon", "Bridges Event"}, player),
                "Air Support: Flight Economy": lambda state: state.has_all({"Air Trooper", "Bridges Event"}, player),
            }
        ),
        Wargroove2Level(
            name="Fortification",
            file_name="Fortification.json",
            location_rules={
                "Fortification: Victory": lambda state: state.has_all({"Golem", "Walls Event"}, player) and
                                                        state.has_any({"Archer", "Trebuchet"}, player),
                "Fortification: Hyper Repair": lambda state: state.has_all({"Golem", "Walls Event"}, player),
                "Fortification: Defensive Artillery": lambda state: state.has("Trebuchet", player),
            },
            has_ocean=False
        ),
        Wargroove2Level(
            name="A Ribbitting Time",
            file_name="A_Ribbitting_Time.json",
            location_rules={
                "A Ribbitting Time: Victory": lambda state: state.has("Frog", player),
                "A Ribbitting Time: Leap Frog": lambda state: state.has("Frog", player),
                "A Ribbitting Time: Frogway Robbery": lambda state: state.has_all({"Frog", "Thief"}, player),
            }
        ),
        Wargroove2Level(
            name="Precarious Cliffs",
            file_name="Precarious_Cliffs.json",
            location_rules={
                "Precarious Cliffs: Victory": lambda state: state.has_all({"Airstrike Event", "Archer"}, player),
                "Precarious Cliffs: No Crit for You": lambda state: state.has("Airstrike Event", player),
                "Precarious Cliffs: Out Ranged": lambda state: state.has_all({"Airstrike Event", "Archer"}, player),
            },
            has_ocean=False
        ),
        Wargroove2Level(
            name="Split Valley",
            file_name="Split_Valley.json",
            location_rules={
                "Split Valley: Victory": lambda state: state.has("Trebuchet", player) and
                                                       state.has_any({"Bridges Event", "Air Trooper"}, player),
                "Split Valley: Longshot": lambda state: state.has("Trebuchet", player),
                "Split Valley: Ranged Trinity": lambda state: state.has_all({"Trebuchet", "Archer", "Ballista"},
                                                                            player),
            }
        ),
        Wargroove2Level(
            name="Grand Theft Village",
            file_name="Grand_Theft_Village.json",
            location_rules={
                "Grand Theft Village: Victory": lambda state: state.has("Thief", player) and
                                                              state.has_any({"Mage", "Ballista"}, player),
                "Grand Theft Village: Stand Tall": lambda state: state.has("Golem", player),
                "Grand Theft Village: Pillager": lambda state: True,
            },
            has_ocean=False
        ),
        Wargroove2Level(
            name="Bridge Brigade",
            file_name="Bridge_Brigade.json",
            location_rules={
                "Bridge Brigade: Victory": lambda state: state.has_all({"Warship", "Spearman"}, player),
                "Bridge Brigade: From the Depths": lambda state: state.has("Kraken", player),
                "Bridge Brigade: Back to the Depths": lambda state:
                state.has_all({"Warship", "Spearman", "Kraken"}, player),
            },
            has_ocean=False
        ),
    ]
    for level in levels:
        level.player = player
    return levels


def get_final_levels(player: int) -> List[Wargroove2Level]:
    levels = [
        Wargroove2Level(
            name="Disastrous Crossing",
            file_name="Disastrous_Crossing.json",
            location_rules={"Disastrous Crossing: Victory":
                                lambda state: state.has_any({"Merfolk", "River Boat"}, player) and
                                              state.has_any({"Knight", "Kraken"}, player)}
        ),
        Wargroove2Level(
            name="Dark Mirror",
            file_name="Dark_Mirror.json",
            location_rules={"Dark Mirror: Victory": lambda state: state.has("Archer", player) and
                                                                  state.has_any({"Mage", "Ballista"}, player) and
                                                                  state.has_any({"Harpy", "Dragon"}, player)},
            has_ocean=False
        ),
        Wargroove2Level(
            name="Doomed Metropolis",
            file_name="Doomed_Metropolis.json",
            location_rules={"Doomed Metropolis: Victory": lambda state: state.has_all({"Mage", "Knight"}, player)},
            has_ocean=False
        ),
        Wargroove2Level(
            name="Dementia Castle",
            file_name="Dementia_Castle.json",
            location_rules={"Dementia Castle: Victory":
                                lambda state: state.has_all({"Merfolk", "Mage", "Golem", "Harpy"}, player)}
        ),
    ]
    for level in levels:
        level.player = player
    return levels


def get_first_level(player: int) -> Wargroove2Level:
    first_level = Wargroove2Level(
        name="Humble Beginnings Rebirth",
        file_name="",
        location_rules={
            "Humble Beginnings Rebirth: Victory": lambda state: True,
            "Humble Beginnings Rebirth: Talk to Nadia": lambda state: True,
            "Humble Beginnings Rebirth: Good Dog": lambda state: True
        }
    )
    first_level.player = player
    return first_level
