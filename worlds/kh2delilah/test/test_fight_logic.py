from . import KH2DelilahTestBase


class TestEasy(KH2DelilahTestBase):
    options = {
        "FightLogic": 0
    }


class TestNormal(KH2DelilahTestBase):
    options = {
        "FightLogic": 1
    }


class TestHard(KH2DelilahTestBase):
    options = {
        "FightLogic": 2
    }
