from ..Locations import location_data_table
from . import KHDDDTestBase

PORTALS = {name for name in location_data_table if "Secret Portal" in name}
JULIUS = {"Traverse Town 2 Ultima Weapon Reward [Sora]", "Traverse Town 2 Ultima Weapon Reward [Riku]",
          "Unbound Keyblade Reward [Sora]", "Unbound Keyblade Reward [Riku]"}
GOAL = {"All Superbosses Defeated [Sora] [Riku]"}


class TestSuperbossesOffLuckyEmblemHunt(KHDDDTestBase):
    options = {"goal": "lucky_emblem_hunt", "superbosses": False}

    def test_no_superboss_locations(self):
        names = {location.name for location in self.multiworld.get_locations(self.player)}
        self.assertFalse(names & (PORTALS | JULIUS | GOAL))


class TestSuperbossesOnLuckyEmblemHunt(KHDDDTestBase):
    options = {"goal": "lucky_emblem_hunt", "superbosses": True}

    def test_superboss_checks_without_goal_location(self):
        names = {location.name for location in self.multiworld.get_locations(self.player)}
        self.assertTrue(PORTALS | JULIUS <= names)
        self.assertFalse(names & GOAL)


class TestSuperbossGoalForcesSuperbosses(KHDDDTestBase):
    options = {"goal": "superbosses", "superbosses": False}

    def test_all_superboss_locations_present(self):
        names = {location.name for location in self.multiworld.get_locations(self.player)}
        self.assertTrue(PORTALS | JULIUS | GOAL <= names)
