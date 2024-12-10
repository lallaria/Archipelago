from . import OriBFTestBase


class TestStartLocationsAccess(OriBFTestBase):
    options = {
        "test": True
    }

    def test_sword_chests(self) -> None:
        #locations = ["GladesMapKeystone"]
        #items = [["KeyStone", 2]]
        # This tests that the provided locations aren't accessible without the provided items, but can be accessed once
        # the items are obtained.
        # This will also check that any locations not provided don't have the same dependency requirement.
        # Optionally, passing only_check_listed=True to the method will only check the locations provided.
        #self.assertAccessDependency(locations, items)

        #self.assertFalse(self.can_reach_region("GladesFirstKeyDoorOpened"))
        self.assertTrue(self.can_reach_location("FirstPickup"))
        self.assertFalse(self.can_reach_region("LowerChargeFlameArea"))
        self.assertFalse(self.can_reach_location("ChargeFlameAreaExp"))
        #self.assertAccessDependency(["ChargeFlameAreaExp"], [["Grenade"]], True)
        return