from random import Random
from typing import List, Tuple
from .options import OuterWildsGameOptions


# we use lists instead of sets here to ensure determinism
warp_platforms = [
    "SS",  # Sun Station
    "ST",  # Sun Tower on Ash Twin
    "ET",  # Ember Twin
    "ETT",  # Ember Twin Tower
    "ATP",  # inside Ash Twin Project
    "ATT",  # Ash Twin Tower on Ash Twin's surface
    "TH",  # Timber Hearth
    "THT",  # Timber Hearth Tower on Ash Twin
    "BHNG",  # Brittle Hollow Northern Glacier
    "WHS",  # White Hole Station
    "BHF",  # the pad on the Hanging City ceiling used to access Black Hole Forge
    "BHT",  # Brittle Hollow Tower on Ash Twin
    "GD",  # Giant's Deep
    "GDT",  # Giant's Deep Tower on Ash Twin
]

# These are the warp platforms which (logically) can only be reached via another warp platform
dead_end_platforms = [
    "SS",
    "ATP",
    "BHF",
]

platforms_reachable_by_ship = [p for p in warp_platforms if p not in dead_end_platforms]


# The vanilla warp mapping is:
# [("SS", "ST"), ("ET", "ETT"), ("ATP", "ATT"), ("TH", "THT"), ("BHNG", "WHS"), ("BHF", "BHT"), ("GD", "GDT")]
def generate_random_warp_platform_mapping(random: Random, options: OuterWildsGameOptions) -> List[Tuple[str, str]]:
    unmapped_platforms = warp_platforms.copy()
    mappings = []

    # Astral Codec requires a shipless warp path from the Hourglass Twins to Timber Hearth.
    # For simplicity, we connect HGT to TH directly, only randomizing which HGT pad gets used.
    if options.enable_ac_mod:
        available_hgt_platforms = ["ST", "ETT", "ATT", "THT", "BHT", "GDT", "ET"]  # all the towers plus Ember Twin
        hgt_platform = random.choice(available_hgt_platforms)
        mappings.append(("TH", hgt_platform))
        unmapped_platforms.remove("TH")
        unmapped_platforms.remove(hgt_platform)

    # Handle dead ends first to avoid pairing dead ends with other dead ends (e.g. Sun Station <-> ATP)
    for dead_end_platform in dead_end_platforms:
        available_platforms = [p for p in unmapped_platforms if p in platforms_reachable_by_ship]

        # Sun Station is the only warp platform that disappears about halfway through the loop.
        # Technically every other platform is exposed by then, but for some the margin is just too small.
        if dead_end_platform == 'SS':  # actually falls into the sun at 11:30 - 11:40
            available_platforms.remove('THT')  # exposed at ~10:30
            available_platforms.remove('BHT')  # exposed at ~10:30
            available_platforms.remove('GDT')  # exposed at ~11:00

        destination = random.choice(available_platforms)
        mappings.append((dead_end_platform, destination))
        unmapped_platforms.remove(dead_end_platform)
        unmapped_platforms.remove(destination)

    random.shuffle(unmapped_platforms)
    it = iter(unmapped_platforms)
    mappings.extend(list(zip(it, it)))

    return mappings


warp_platform_to_logical_region = {
    "SS": "Sun Station",
    "ST": "Hourglass Twins",
    "ET": "Hourglass Twins",
    "ETT": "Hourglass Twins",
    "ATP": "Ash Twin Interior",
    "ATT": "Hourglass Twins",
    "TH": "Timber Hearth",
    "THT": "Hourglass Twins",
    "BHNG": "Brittle Hollow",
    "WHS": "White Hole Station",
    "BHF": "Hanging City Ceiling",
    "BHT": "Hourglass Twins",
    "GD": "Giant's Deep",
    "GDT": "Hourglass Twins",
}

warp_platform_required_items = {
    "SS": ["Spacesuit"]
}
