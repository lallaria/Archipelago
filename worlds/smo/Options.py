from dataclasses import dataclass

from Options import Toggle, Range, Choice, PerGameCommonOptions, NamedRange, TextChoice, FreeText, OptionDict

class Goal(Choice):
    """Sets the completion goal. This is the kingdom you must get the last story multi moon in to win the game.
    Valid options: Metro (A Traditional Festival), Luncheon (Cookatiel Showdown), Moon (Beat the game), Dark (Arrival at Rabbit Ridge), Darker (A Long Journey's End)"""
    display_name = "Goal"
    option_lake = 5
    option_sand = 4
    option_metro = 9
    option_luncheon = 12
    option_moon = 15
    option_dark = 16
    option_darker = 17
    default = 15  # default to moon

@dataclass
class SMOOptions(PerGameCommonOptions):
    goal: Goal
