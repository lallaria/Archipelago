import typing

from BaseClasses import Location, Item


class KH2DelilahLocation(Location):
    game: str = "Kingdom Hearts 2 Delilah"


class LocationData(typing.NamedTuple):
    locid: int
    yml: str
    charName: str = "Sora"
    charNumber: int = 1


class KH2DelilahItem(Item):
    game: str = "Kingdom Hearts 2 Delilah"


class ItemData(typing.NamedTuple):
    quantity: int = 0
    kh2delilahid: int = 0
    # Save+ mem addr
    memaddr: int = 0
    # some items have bitmasks. if bitmask>0 bitor to give item else
    bitmask: int = 0
    # if ability then
    ability: bool = False
