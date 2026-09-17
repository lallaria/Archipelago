from ..Items import item_data_table
from . import KHDDDTestBase

# Options of a 3-player seed that failed remaining_fill when world unlocks were classified as filler.
LUCKY_EMBLEM_HUNT_OPTIONS = {
    "character": "both",
    "goal": "lucky_emblem_hunt",
    "armored_ventus_nightmare": False,
    "emblem_reqs": 50,
    "emblems_in_pool": 40,
    "recipe_reqs": 2,
    "recipes_in_pool": 54,
    "starting_worlds": 1,
    "superbosses": False,
    "lord_kyroo": False,
    "play_destiny_islands": False,
    "skip_light_cycle": True,
    "fast_go_mode": False,
    "exp_multiplier": 5,
    "super_jump_start": True,
    "level_cap": 50,
    "stats_on_levels": "any_item",
    "stat_bonus": 3,
    "strength_in_pool": 27,
    "magic_in_pool": 27,
    "defense_in_pool": 26,
    "randomize_keyblade_stats": True,
    "keyblade_min_str": 4,
    "keyblade_max_str": 18,
    "keyblade_min_mag": 4,
    "keyblade_max_mag": 18,
    "instant_drop_trap_chance": 3,
    "single_flowmotion": False,
}


class TestLuckyEmblemHuntFill(KHDDDTestBase):
    options = LUCKY_EMBLEM_HUNT_OPTIONS

    def test_logic_items_are_progression(self):
        logic_items = ["High Jump", "Air Slide", "Glide", "Superglide", "Double Flight"]
        logic_items += [name for name, data in item_data_table.items() if data.category in ("World", "Flowmotion")]
        for name in logic_items:
            self.assertTrue(self.world.create_item(name).advancement, name)

    def test_pool_has_filler_for_capped_levels(self):
        filler_probe = self.world.create_item("Potion")
        useful_probe = self.world.create_item("HP Increase [Sora]")
        filler_only = [location for location in self.multiworld.get_unfilled_locations(self.player)
                       if location.item_rule(filler_probe) and not location.item_rule(useful_probe)]
        filler = [item for item in self.multiworld.itempool
                  if item.player == self.player and not (item.advancement or item.useful or item.trap)]
        self.assertGreaterEqual(len(filler), len(filler_only))
