from BaseClasses import CollectionState

def count_moons(self, state: CollectionState, kingdom : str, player: int) -> int:
    """Returns the cumulative count of items from an item group present in state."""
    amt = 0
    player_prog_items = state.prog_items[player].keys()
    for item in self.multiworld.get_items():
        if item.name in player_prog_items and item.name in self.multiworld.worlds[player].item_name_groups[kingdom]:
            amt += item.moon_value
    return amt


def total_moons(self, state: CollectionState, player: int) -> int:
    """Returns the cumulative count of items from an item group present in state."""
    amt = 0
    player_prog_items = list(state.prog_items[player].keys())
    for item in self.multiworld.get_items():
        if item.name in player_prog_items:
            amt += item.moon_value

    return amt


