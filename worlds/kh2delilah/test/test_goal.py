from . import KH2DelilahTestBase
from ..Names import ItemName


class TestDefault(KH2DelilahTestBase):
    options = {}


class TestThreeProofs(KH2DelilahTestBase):
    options = {
        "Goal": 0,
    }


class TestLuckyEmblem(KH2DelilahTestBase):
    options = {
        "Goal": 1,
    }


class TestHitList(KH2DelilahTestBase):
    options = {
        "Goal": 2,
    }


class TestLuckyEmblemHitlist(KH2DelilahTestBase):
    options = {
        "Goal": 3,
    }


class TestThreeProofsNoXemnas(KH2DelilahTestBase):
    options = {
        "Goal":        0,
        "FinalXemnas": False,
    }


class TestLuckyEmblemNoXemnas(KH2DelilahTestBase):
    options = {
        "Goal":        1,
        "FinalXemnas": False,
    }


class TestHitListNoXemnas(KH2DelilahTestBase):
    options = {
        "Goal":        2,
        "FinalXemnas": False,
    }


class TestLuckyEmblemHitlistNoXemnas(KH2DelilahTestBase):
    options = {
        "Goal":        3,
        "FinalXemnas": False,
    }

