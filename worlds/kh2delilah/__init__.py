import logging
import os
from typing import List

from BaseClasses import Tutorial, ItemClassification
from worlds.LauncherComponents import Component, components, icon_paths, Type, launch_subprocess
from worlds.AutoWorld import World, WebWorld
from Utils import local_path, user_path
from .Items import *
from .Locations import *
from .Names import ItemName, LocationName, RegionName
from .OpenKH import patch_kh2
from .Options import KingdomHearts2DelilahOptions
from .Regions import create_regions, connect_regions
from .Rules import *
from .Subclasses import KH2DelilahItem


def launch_client():
    from .Client import launch
    launch_subprocess(launch, name="KH2DelilahClient")


components.append(Component("KH2 Delilah Client", "KH2DelilahClient", func=launch_client, component_type=Type.CLIENT, icon='khapicon'))
icon_paths['khapicon'] = local_path('data', 'khapicon.png')


class KingdomHearts2DelilahWeb(WebWorld):
    tutorials = [Tutorial(
            "Multiworld Setup Guide",
            "A guide to playing Kingdom Hearts 2 Final Mix with Archipelago.",
            "English",
            "setup_en.md",
            "setup/en",
            ["JaredWeakStrike"]
    )]


class KH2DelilahWorld(World):
    """
    Kingdom Hearts II is an action role-playing game developed and published by Square Enix and released in 2005.
    It is the sequel to Kingdom Hearts and Kingdom Hearts: Chain of Memories, and like the two previous games,
    focuses on Sora and his friends' continued battle against the Darkness.
    """
    game = "Kingdom Hearts 2 Delilah"
    web = KingdomHearts2DelilahWeb()

    required_client_version = (0, 4, 4)
    options_dataclass = KingdomHearts2DelilahOptions
    options: KingdomHearts2DelilahOptions
    item_name_to_id = {item: item_id
                       for item_id, item in enumerate(item_dictionary_table.keys(), 0x130000)}
    location_name_to_id = {item: location
                           for location, item in enumerate(all_locations.keys(), 0x130000)}

    item_name_groups = item_groups
    location_name_groups = location_groups

    visitlocking_dict: Dict[str, int]
    plando_locations: Dict[str, str]
    lucky_emblem_amount: int
    lucky_emblem_required: int
    bounties_required: int
    bounties_amount: int
    bounties_difficulty: int
    filler_items: List[str]
    item_quantity_dict: Dict[str, int]
    local_items: Dict[int, int]
    sora_ability_dict: Dict[str, int]
    goofy_ability_dict: Dict[str, int]
    donald_ability_dict: Dict[str, int]
    total_locations: int
    misc_progression_items: List[Item]
    # growth_list: list[str]

    def __init__(self, multiworld: "MultiWorld", player: int):
        super().__init__(multiworld, player)
        # random_super_boss_list Dict[str]
        # has to be in __init__ or else other players affect each other's bounties
        self.random_bounty_dict = dict()
        self.growth_list = list()
        # lists of KH2Item
        self.keyblade_ability_pool = list()

        self.goofy_get_bonus_abilities = list()
        self.goofy_weapon_abilities = list()
        self.donald_get_bonus_abilities = list()
        self.donald_weapon_abilities = list()
        self.all_weapon_items = list()

        self.slot_data_goofy_weapon = dict()
        self.slot_data_sora_weapon = dict()
        self.slot_data_donald_weapon = dict()

        self.misc_progression_items = list()

    def fill_slot_data(self) -> dict:
        for ability in self.slot_data_sora_weapon:
            if ability in self.sora_ability_dict and self.sora_ability_dict[ability] >= 1:
                self.sora_ability_dict[ability] -= 1
        self.donald_ability_dict = {k: v.quantity for k, v in DonaldAbility_Table.items()}
        for ability in self.slot_data_donald_weapon:
            if ability in self.donald_ability_dict and self.donald_ability_dict[ability] >= 1:
                self.donald_ability_dict[ability] -= 1
        self.goofy_ability_dict = {k: v.quantity for k, v in GoofyAbility_Table.items()}
        for ability in self.slot_data_goofy_weapon:
            if ability in self.goofy_ability_dict and self.goofy_ability_dict[ability] >= 1:
                self.goofy_ability_dict[ability] -= 1

        slot_data = self.options.as_dict("Goal", "FinalXemnas", "LuckyEmblemsRequired", "BountyRequired")
        slot_data.update({
            "hitlist":                [],  # remove this after next update
            "PoptrackerVersionCheck": 4.3,
            "KeybladeAbilities":      self.sora_ability_dict,
            "StaffAbilities":         self.donald_ability_dict,
            "ShieldAbilities":        self.goofy_ability_dict,
        })
        return slot_data

    def create_item(self, name: str) -> Item:
        """
        Returns created KH2Item
        """
        # data = item_dictionary_table[name]
        if name in progression_set or name in self.misc_progression_items:
            item_classification = ItemClassification.progression
        elif name in useful_set:
            item_classification = ItemClassification.useful
        elif name in Trap_Table:
            item_classification = ItemClassification.trap
        else:
            item_classification = ItemClassification.filler
        created_item = KH2DelilahItem(name, item_classification, self.item_name_to_id[name], self.player)

        return created_item

    def create_event_item(self, name: str) -> Item:
        item_classification = ItemClassification.progression
        created_item = KH2DelilahItem(name, item_classification, None, self.player)
        return created_item

    def create_items(self) -> None:
        """
        Fills ItemPool and manages schmovement, random growth, visit locking and random starting visit locking.
        """
        self.visitlocking_dict = visit_locking_dict["AllVisitLocking"].copy()
        if self.options.Schmovement != "level_0":
            for _ in range(self.options.Schmovement.value):
                for name in Movement_Table.keys():
                    self.item_quantity_dict[name] -= 1
                    self.growth_list.remove(name)
                    self.multiworld.push_precollected(self.create_item(name))

        if self.options.RandomGrowth:
            max_growth = min(self.options.RandomGrowth.value, len(self.growth_list))
            for _ in range(max_growth):
                random_growth = self.random.choice(self.growth_list)
                self.item_quantity_dict[random_growth] -= 1
                self.growth_list.remove(random_growth)
                self.multiworld.push_precollected(self.create_item(random_growth))

        if self.options.Visitlocking == "no_visit_locking":
            for item, amount in visit_locking_dict["AllVisitLocking"].items():
                for _ in range(amount):
                    self.multiworld.push_precollected(self.create_item(item))
                    self.item_quantity_dict[item] -= 1
                    self.visitlocking_dict[item] -= 1
                    if self.visitlocking_dict[item] == 0:
                        self.visitlocking_dict.pop(item)

        elif self.options.Visitlocking == "second_visit_locking":
            for item in visit_locking_dict["2VisitLocking"]:
                self.item_quantity_dict[item] -= 1
                self.visitlocking_dict[item] -= 1
                if self.visitlocking_dict[item] == 0:
                    self.visitlocking_dict.pop(item)
                self.multiworld.push_precollected(self.create_item(item))

        for _ in range(self.options.RandomVisitLockingItem.value):
            if sum(self.visitlocking_dict.values()) <= 0:
                break
            visitlocking_set = list(self.visitlocking_dict.keys())
            item = self.random.choice(visitlocking_set)
            self.item_quantity_dict[item] -= 1
            self.visitlocking_dict[item] -= 1
            if self.visitlocking_dict[item] == 0:
                self.visitlocking_dict.pop(item)
            self.multiworld.push_precollected(self.create_item(item))

        itempool = [self.create_item(item) for item, data in self.item_quantity_dict.items() for _ in range(data)]

        # Creating filler for unfilled locations
        itempool += [self.create_filler() for _ in range(self.total_locations - len(itempool))]

        self.multiworld.itempool += itempool

    def generate_early(self) -> None:
        """
        Determines the quantity of items and maps plando locations to items.
        This happens first.  Nothing is placed here.
        """
        # Item: Quantity Map
        # Example. Quick Run: 4
        self.total_locations = len(all_locations.keys())
        for x in range(4):
            self.growth_list.extend(Movement_Table.keys())

        self.item_quantity_dict = {item: data.quantity for item, data in item_dictionary_table.items()}
        self.sora_ability_dict = {k: v.quantity for dic in [
                GreatActionAbility_Table, UsefulActionAbility_Table, JunkActionAbility_Table, 
                GreatSupportAbility_Table, UsefulSupportAbility_Table, JunkSupportAbility_Table
                ] 
            for k, v in dic.items()}

        for k in self.sora_ability_dict.keys():
            if k in [ItemName.AutoValor, ItemName.AutoWisdom, 
                     ItemName.AutoMaster, ItemName.AutoFinal] and self.options.AutoFormLogic.value:
                self.misc_progression_items.append(k)
        # Dictionary to mark locations with their plandoed item
        # Example. Final Xemnas: Victory

        self.plando_locations = dict()
        self.starting_invo_verify()

        for k, v in self.options.CustomItemPoolQuantity.value.items():
            # kh2's items cannot hold more than a byte
            if 255 > v > self.item_quantity_dict[k] and k in default_itempool_option.keys():
                self.item_quantity_dict[k] = v
            elif 255 <= v:
                logging.warning(
                        f"{self.player} has too many {k} in their CustomItemPool setting. Setting to default quantity")
        # Option to turn off Promise Charm Item
        if not self.options.Promise_Charm:
            del self.item_quantity_dict[ItemName.PromiseCharm]

        if not self.options.AntiForm:
            del self.item_quantity_dict[ItemName.AntiForm]

        self.set_excluded_locations()

        if self.options.Goal not in ["hitlist", "three_proofs"]:
            self.lucky_emblem_amount = self.options.LuckyEmblemsAmount.value
            self.lucky_emblem_required = self.options.LuckyEmblemsRequired.value
            self.emblem_verify()

        # hitlist
        if self.options.Goal not in ["lucky_emblem_hunt", "three_proofs"]:
            self.random_bounty_dict = dict(exclusion_table["Hitlist"])
            self.bounties_amount = self.options.BountyAmount.value
            self.bounties_required = self.options.BountyRequired.value
            self.bounties_difficulty = self.options.BountyLevel.value

            # make a range to pull bounties from - do not go beyond AS level unless requested
            # also don't give first visit bounties to people looking for higher ranked challenges

            difficulty_high = self.bounties_difficulty if self.bounties_difficulty >=7 else max(min(self.bounties_difficulty + 2, 7), 4)
            difficulty_low = max(self.bounties_difficulty - 3 , 1)

            difficulty_scope = [location for location, rank in self.random_bounty_dict.items()
                                if not (difficulty_low <= rank <= difficulty_high)]
            for bounty_loc in difficulty_scope:
                del self.random_bounty_dict[bounty_loc]

            self.hitlist_verify()

            prio_hitlist = [location for location in self.options.priority_locations.value if
                            location in self.random_bounty_dict]
            similar_boss = ""  # super ugly but prevents both as and data of a bounty, yoinks it out before the
            similar_boss_loc = "" # next iteration through the loop
            for _ in range(self.options.BountyAmount.value):           
                if prio_hitlist:
                    if similar_boss: 
                        similar_boss_loc = "".join([boss for boss in prio_hitlist if similar_boss in boss])
                        if similar_boss_loc: prio_hitlist.remove(similar_boss_loc)
                    random_boss = self.random.choice(prio_hitlist)
                    prio_hitlist.remove(random_boss)
                else:
                    if similar_boss: 
                        similar_boss_loc = "".join([boss for boss in [*self.random_bounty_dict] if similar_boss in boss])
                        if similar_boss_loc: del self.random_bounty_dict[similar_boss_loc]
                    random_boss = self.random.choice([*self.random_bounty_dict])
                self.plando_locations[random_boss] = ItemName.Bounty
                del self.random_bounty_dict[random_boss]
                self.total_locations -= 1
                #Grabs the last 5 characters of the location string if it matches AS/Data, which should be the boss name
                if any(_ in random_boss for _ in ['Larxene', 'Lexaeus', 'Zexion', 'Marluxia', 'Vexen']):
                    similar_boss = "".join(random_boss[-5:])
                else: 
                    similar_boss = ""

        # self.weaponitem_gen_early()

        self.donald_gen_early()
        self.goofy_gen_early()
        self.keyblade_gen_early()

        # final xemnas isn't a location anymore
        # self.total_locations -= 1

        if self.options.WeaponSlotStartHint:
            for location in all_weapon_slot:
                self.options.start_location_hints.value.add(location)

        if self.options.FillerItemsLocal:
            for item in filler_items:
                self.options.local_items.value.add(item)
        # By imitating remote this doesn't have to be plandoded filler anymore
        #  for location in {LocationName.JunkMedal, LocationName.JunkMedal}:
        #    self.plando_locations[location] = random_stt_item
        if not self.options.SummonLevelLocationToggle:
            self.total_locations -= 6

        self.total_locations -= self.level_subtraction()

    def pre_fill(self):
        """
        Plandoing Events and Fill_Restrictive for donald,goofy and sora

        Abilities on weapons need to be placed first so that the location is tangible
        """

        self.donald_pre_fill()
        self.goofy_pre_fill()
        self.keyblade_pre_fill()

        for location, item in self.plando_locations.items():
            self.multiworld.get_location(location, self.player).place_locked_item(
                    self.create_item(item))

    def create_regions(self):
        """
        Creates the Regions and Connects them.
        """
        create_regions(self)
        connect_regions(self)

    def set_rules(self):
        """
        Sets the Logic for the Regions and Locations.
        """
        universal_logic = Rules.KH2DelilahWorldRules(self)
        form_logic = Rules.KH2FormRules(self)
        fight_rules = Rules.KH2FightRules(self)
        fight_rules.set_kh2_fight_rules()
        universal_logic.set_kh2_rules()
        form_logic.set_kh2_form_rules()

    def generate_output(self, output_directory: str):
        """
        Generates the .zip for OpenKH (The KH Mod Manager)
        """
        patch_kh2(self, output_directory)

    def donald_gen_early(self):
        donald_master_ability = [donald_ability for donald_ability in staff_set.keys() for _ in
                                 range(self.item_quantity_dict[donald_ability])]
        self.donald_weapon_abilities = []
        self.donald_get_bonus_abilities = []
        # fill weapons first, 9 shuffled staves, one starter staff, 5 shop
        for _ in range(15):
            random_ability = self.random.choice(donald_master_ability)
            donald_master_ability.remove(random_ability)
            self.donald_weapon_abilities += [self.create_item(random_ability)]
            self.item_quantity_dict[random_ability] -= 1
            self.total_locations -= 1

        self.slot_data_donald_weapon = [item_name.name for item_name in self.donald_weapon_abilities]

        if not self.options.DonaldGoofyStatsanity:
            # pre plando donald get bonuses
            for item_name in donald_master_ability:
                self.donald_get_bonus_abilities += [self.create_item(item_name)]
                self.item_quantity_dict[item_name] -= 1
                self.total_locations -= 1

    def goofy_gen_early(self):
        goofy_master_ability = [goofy_ability for goofy_ability in shield_set.keys() for _ in
                                range(self.item_quantity_dict[goofy_ability])]
        self.goofy_weapon_abilities = []
        self.goofy_get_bonus_abilities = []
        # fill weapons first, 9 shuffled shields, one starter shield, 5 shop
        for _ in range(15):
            random_ability = self.random.choice(goofy_master_ability)
            goofy_master_ability.remove(random_ability)
            self.goofy_weapon_abilities += [self.create_item(random_ability)]
            self.item_quantity_dict[random_ability] -= 1
            self.total_locations -= 1

        self.slot_data_goofy_weapon = [item_name.name for item_name in self.goofy_weapon_abilities]

        if not self.options.DonaldGoofyStatsanity:
            # pre plando goofy get bonuses
            for item_name in goofy_master_ability:
                self.goofy_get_bonus_abilities += [self.create_item(item_name)]
                self.item_quantity_dict[item_name] -= 1
                self.total_locations -= 1

    def keyblade_gen_early(self):
        # need to have enough abilities to slot into keyblade locations
        keyblade_master_ability = [sora_ability for sora_ability in default_keyblade_pool.keys() 
                                   for _ in range(self.item_quantity_dict[sora_ability])]

        if len(Keyblade_Slots) >= sum(self.options.CustomKeybladePool.value.values()):
            logging.warning(
                    f"{self.player} has more Keyblades than Keyblade Abilities. Setting to default quantities.")
            for k, v in default_keyblade_pool.items():
                if v < self.item_quantity_dict[k]:
                    for _ in range(v,self.item_quantity_dict[k]):
                        keyblade_master_ability.remove(k)
        else:
            for k, v in self.options.CustomKeybladePool.value.items():
                if v > self.item_quantity_dict[k]:
                    logging.warning(
                        f"{self.player} put more of {k} in keyblades than exist in the pool, setting to default quantity {v}")
                    v = default_keyblade_pool[k]
                if v < self.item_quantity_dict[k]:
                    for _ in range(v,self.item_quantity_dict[k]):
                        keyblade_master_ability.remove(k)

        self.keyblade_ability_pool = []

        for _ in range(len(Keyblade_Slots)):
            random_ability = self.random.choice(keyblade_master_ability)
            keyblade_master_ability.remove(random_ability)
            self.keyblade_ability_pool += [self.create_item(random_ability)]
            self.item_quantity_dict[random_ability] -= 1
            self.total_locations -= 1
        self.slot_data_sora_weapon = [item_name.name for item_name in self.keyblade_ability_pool]

    def goofy_pre_fill(self):
        """
        Removes goofy locations from the location pool maps random goofy items to be plandoded.
        """
        goofy_weapon_location_list = [self.multiworld.get_location(location, self.player) for location in
                                      Goofy_Checks.keys() if Goofy_Checks[location].yml == "Keyblade"]
        # randomize the list with only
        for location in goofy_weapon_location_list:
            random_ability = self.random.choice(self.goofy_weapon_abilities)
            location.place_locked_item(random_ability)
            self.goofy_weapon_abilities.remove(random_ability)
            if location not in starter_weapon_slot and random_ability.advancement:
                self.set_weapon_prog(location)
        if not self.options.DonaldGoofyStatsanity:
            # plando goofy get bonuses
            goofy_get_bonus_location_pool = [self.multiworld.get_location(location, self.player) for location in
                                             Goofy_Checks.keys() if Goofy_Checks[location].yml != "Keyblade"]
            for location in goofy_get_bonus_location_pool:
                self.random.choice(self.goofy_get_bonus_abilities)
                random_ability = self.random.choice(self.goofy_get_bonus_abilities)
                location.place_locked_item(random_ability)
                self.goofy_get_bonus_abilities.remove(random_ability)


    def donald_pre_fill(self):
        donald_weapon_location_list = [self.multiworld.get_location(location, self.player) for location in
                                       Donald_Checks.keys() if Donald_Checks[location].yml == "Keyblade"]
        # randomize the list with only
        for location in donald_weapon_location_list:
            random_ability = self.random.choice(self.donald_weapon_abilities)
            location.place_locked_item(random_ability)
            self.donald_weapon_abilities.remove(random_ability)
            if location not in starter_weapon_slot and random_ability.advancement:
                self.set_weapon_prog(location)

        if not self.options.DonaldGoofyStatsanity:
            # plando goofy get bonuses
            donald_get_bonus_location_pool = [self.multiworld.get_location(location, self.player) for location in
                                              Donald_Checks.keys() if Donald_Checks[location].yml != "Keyblade"]
            for location in donald_get_bonus_location_pool:
                random_ability = self.random.choice(self.donald_get_bonus_abilities)
                location.place_locked_item(random_ability)
                self.donald_get_bonus_abilities.remove(random_ability)

    def keyblade_pre_fill(self):
        """
        Fills keyblade slots with abilities determined on player's setting
        """   

        keyblade_locations = [self.multiworld.get_location(location, self.player) for location in Keyblade_Slots.keys()]
        for location in keyblade_locations:
            random_ability = self.random.choice(self.keyblade_ability_pool)
            location.place_locked_item(random_ability)
            self.keyblade_ability_pool.remove(random_ability)
            if location not in starter_weapon_slot and random_ability.advancement:
                self.set_weapon_prog(location)

    def set_weapon_prog(self, loc: Location) -> None:
        for kbslot, kbitem in exclusion_table["WeaponSlots"].items():
            if loc.name == kbslot:
                keyblade = [i for i in self.multiworld.itempool if i.name == kbitem and i.player == self.player].pop()
                keyblade.classification = ItemClassification.progression
                
    def starting_invo_verify(self):
        """
        Making sure the player doesn't put too many abilities in their starting inventory.
        """
        for item, value in self.options.start_inventory.value.items():
            if item in GreatActionAbility_Table or item in UsefulActionAbility_Table \
                    or item in JunkActionAbility_Table or item in GreatSupportAbility_Table \
                    or item in UsefulSupportAbility_Table or item in JunkSupportAbility_Table \
                    or item in exclusion_item_table["StatUps"] \
                    or item in DonaldAbility_Table or item in GoofyAbility_Table:
                # cannot have more than the quantity for abilties
                if value > item_dictionary_table[item].quantity:
                    logging.info(
                            f"{self.multiworld.get_file_safe_player_name(self.player)} cannot have more than {item_dictionary_table[item].quantity} of {item}."
                            f" Changing the amount to the max amount")
                    value = item_dictionary_table[item].quantity
                self.item_quantity_dict[item] -= value

    def emblem_verify(self):
        """
        Making sure lucky emblems have amount>=required.
        """
        if self.lucky_emblem_amount < self.lucky_emblem_required:
            logging.info(
                    f"Lucky Emblem Amount {self.options.LuckyEmblemsAmount.value} is less than required "
                    f"{self.options.LuckyEmblemsRequired.value} for player {self.multiworld.get_file_safe_player_name(self.player)}."
                    f" Setting amount to {self.options.LuckyEmblemsRequired.value}")
            luckyemblemamount = max(self.lucky_emblem_amount, self.lucky_emblem_required)
            self.options.LuckyEmblemsAmount.value = luckyemblemamount

        self.item_quantity_dict[ItemName.LuckyEmblem] = self.options.LuckyEmblemsAmount.value
        # give this proof to unlock the final door once the player has the amount of lucky emblem required
        if ItemName.ProofofNonexistence in self.item_quantity_dict:
            del self.item_quantity_dict[ItemName.ProofofNonexistence]

    def hitlist_verify(self):
        """
        Making sure hitlist have amount>=required.
        """
        for location in self.options.exclude_locations.value:
            if location in self.random_bounty_dict:
                del self.random_bounty_dict[location]

        if not self.options.SummonLevelLocationToggle and LocationName.Summonlvl7 in self.random_bounty_dict:
            del self.random_bounty_dict[LocationName.Summonlvl7]

        #  Testing if the player has the right amount of Bounties for Completion.
        if len(self.random_bounty_dict) < self.bounties_amount:
            logging.info(
                    f"{self.multiworld.get_file_safe_player_name(self.player)} has more bounties than bosses."
                    f" Setting total bounties to {len(self.random_bounty_dict)}")
            self.bounties_amount = len(self.random_bounty_dict)
            self.options.BountyAmount.value = self.bounties_amount

        if len(self.random_bounty_dict) < self.bounties_required:
            logging.info(f"{self.multiworld.get_file_safe_player_name(self.player)} has too many required bounties."
                         f" Setting required bounties to {len(self.random_bounty_dict)}")
            self.bounties_required = len(self.random_bounty_dict)
            self.options.BountyRequired.value = self.bounties_required

        if self.bounties_amount < self.bounties_required:
            logging.info(
                    f"Bounties Amount is less than required for player {self.multiworld.get_file_safe_player_name(self.player)}."
                    f" Swapping Amount and Required")
            temp = self.options.BountyRequired.value
            self.options.BountyRequired.value = self.options.BountyAmount.value
            self.options.BountyAmount.value = temp

        if self.options.BountyStartingHintToggle:
            self.options.start_hints.value.add(ItemName.Bounty)

        if ItemName.ProofofNonexistence in self.item_quantity_dict:
            del self.item_quantity_dict[ItemName.ProofofNonexistence]

    def set_excluded_locations(self):
        """
        Fills excluded_locations from player's settings.
        """
        # Option to turn off all superbosses. Can do this individually but its like 20+ checks
        if not self.options.SuperBosses:
            for superboss in exclusion_table["SuperBosses"]:
                self.options.exclude_locations.value.add(superboss)

        # Option to turn off Olympus Colosseum Cups.
        if self.options.Cups == "no_cups":
            for cup in exclusion_table["Cups"]:
                self.options.exclude_locations.value.add(cup)
        # exclude only hades paradox. If cups and hades paradox then nothing is excluded
        elif self.options.Cups == "cups":
            self.misc_progression_items.append(ItemName.HadesCupTrophy)
            self.options.exclude_locations.value.add(LocationName.HadesCupTrophyParadoxCups)

        if not self.options.AtlanticaToggle:
            for loc in exclusion_table["Atlantica"]:
                self.options.exclude_locations.value.add(loc)

    def level_subtraction(self):
        """
       Determine how many locations are on sora's levels.
       """
        if self.options.LevelDepth == "level_50_sanity":
            # level 50 sanity
            return 49
        elif self.options.LevelDepth == "level_1":
            # level 1. No checks on levels
            return 98
        elif self.options.LevelDepth in ["level_50", "level_99"]:
            # could be if leveldepth!= 99 sanity but this reads better imo
            return 75
        else:
            return 0

    def get_filler_item_name(self) -> str:
        """
        Returns random filler item name.
        """
        return self.random.choice(filler_items)
    