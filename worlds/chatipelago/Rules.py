from typing import Callable, TYPE_CHECKING

from BaseClasses import CollectionState

if TYPE_CHECKING:
    from . import ChatipelagoWorld

def get_tree_rule(world: "ChatipelagoWorld") -> Callable[[CollectionState], bool]:
    return lambda state: state.has_all(["Magpie Treasure","Magpie Boldness","Magpie Cooperation"], world.player)

def get_chat_rule(world: "ChatipelagoWorld") -> Callable[[CollectionState], bool]:
    return lambda state: True
