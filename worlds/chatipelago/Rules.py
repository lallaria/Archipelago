from typing import Callable, TYPE_CHECKING
from . import ItemName

from BaseClasses import CollectionState

if TYPE_CHECKING:
    from . import ChatipelagoWorld

def get_prog_rule(world: "ChatipelagoWorld") -> Callable[[CollectionState], bool]:
    return lambda state: state.has_all([ItemName.ItemNum200,ItemName.ItemNum201,ItemName.ItemNum202], world.player)

def get_chat_rule(world: "ChatipelagoWorld") -> Callable[[CollectionState], bool]:
    return lambda state: True
