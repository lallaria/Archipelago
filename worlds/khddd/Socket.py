from enum import IntEnum
import asyncio
from re import S
import socket
import ast
from CommonClient import logger
from worlds.khddd.Items import get_item_category
from worlds.khddd.Locations import get_location_type


class MessageType(IntEnum):
    Invalid = -1
    Test = 0
    ChestChecked = 1
    LevelChecked = 2
    ReceiveAllItems = 3
    RequestAllItems = 4
    ReceiveSingleItem = 5
    StoryChecked = 6
    ClientCommand = 7
    Deathlink = 8
    PortalChecked = 9
    SendSlotData = 10
    Victory = 11
    Handshake = 12
    GetCurrentIndex = 13
    ItemPrompt = 14
    DataStorage = 15
    HasSlotData = 16
    Closed = 20

class DDDCommand(IntEnum):
    DROP = 0
    UNSTUCK = 1
    DEATH_LINK = 3

# using slot data keys for the enum values
class SlotDataType(IntEnum):
    keyblade_stats = 0
    character = 1
    play_destiny_islands = 2
    exp_multiplier = 3
    skip_light_cycle = 4
    fast_go_mode = 5
    recipe_reqs = 6
    win_con = 7
    stat_bonus = 8
    lord_kyroo = 9
    local_item_notifs = 10
    remote_item_notifs = 11
    non_remote_ids = 12
    use_vanilla_levels = 13
    emblem_reqs = 14

class KHDDDSocket():
    @property
    def isConnected(self) -> bool:
        if self.client:
            return self.client.connectedToDDD
        else:
            return False
    @isConnected.setter
    def isConnected(self, value: bool):
        if self.client:
            self.client.connectedToDDD = value

    def __init__(self, client, host: str = "127.0.0.1", port:int = 13713):
        self.client: KHDDDContext = client
        self.host: str = host
        self.port: int = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setblocking(False)
        self.client_socket = None
        self.deathTime = ""
        self.goaled = False
        self.client_item_index = 0
        self.hasSlotData = False

    async def start_server(self):
        logger.debug("Starting server... waiting for game.")
        self.loop = asyncio.get_event_loop()
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(1)
        await self._accept_client()

    async def _accept_client(self):
        """Wait for a client to connect and start a listener task."""
        logger.info("Waiting for KHDDD game connection...")
        while True:
            try:
                self.client_socket, addr = await self.loop.sock_accept(self.server_socket)
                logger.info("KHDDD game client connected.")
                self.isConnected = True
                self.loop.create_task(self.listen())
                self.send_client_cmd(DDDCommand.DEATH_LINK, str(self.client.death_link)) 
                # Reapply deathlink to game after ddd websocket reconnect
                self.client.get_items()

                # Queue up a request for slot data
                self.client.get_slot_data()
                # Resend all items to game after ddd websocket reconnect 
                return
            except OSError as e:
                logger.debug(f"Socket accept failed ({e}); retrying in 5s")
                self.isConnected = False
                await asyncio.sleep(5)

    def _safe_close_client(self):
        """Close the current client socket without killing the server socket."""
        try:
            if self.client_socket:
                self.client_socket.close()
        finally:
            self.client_socket = None
            self.isConnected = False


    async def listen(self):
        while True:
            try:
                message = await self.loop.sock_recv(self.client_socket, 1024)
                if not message:
                    raise ConnectionResetError("Client disconnected")
                msgStr = message.decode("utf-8").replace("\n", "")
                values = msgStr.split(";")
                logger.debug("Received message: "+msgStr)
                self.handle_message(values)
            except (ConnectionResetError, OSError) as e:
                logger.info(f"Connection to game lost, reconnecting...")
                self.client.dddPatched = False
                self._safe_close_client()
                self.hasSlotData = False
                await self._accept_client()
                return

    def send(self, msgId: int, values: list):
        if not self.isConnected or self.client_socket is None:
            return
        try:
            msg = str(msgId)
            for val in values:
                msg += ";" + str(val)
            msg += "\n"
            self.client_socket.send(msg.encode("utf-8"))
            logger.debug("Sent message: "+msg)
        except (OSError, ConnectionResetError, BrokenPipeError) as e:
            logger.debug(f"Error sending message {msgId}: {e}; connection may be lost")
            self.isConnected = False
        except Exception as e:
            logger.debug(f"Error sending message {msgId}: {e}")

    def handle_message(self, message: list[str]):
        if message[0] == '':
            return

        logger.debug("Handling message: "+str(message))
        msgType = MessageType(int(message[0]))

        if msgType == MessageType.ChestChecked:
            locid = int(message[1])
            if locid not in self.client.locations_checked:
                self.client.check_location_IDs.append(locid)
            logger.debug("Chest location checked: "+str(locid))

        elif msgType == MessageType.LevelChecked:
            logger.debug("Level checked")
            locid = int(message[1])
            if locid not in self.client.locations_checked:
                self.client.check_location_IDs.append(locid)

        elif msgType == MessageType.StoryChecked:
            for x in message:
                if len(x) > 1:
                    locid = int(x)
                    if locid not in self.client.locations_checked:
                        self.client.check_location_IDs.append(locid)
                    logger.debug("Story location checked: " + str(locid))

        elif msgType == MessageType.PortalChecked:
            for x in message:
                if len(x) > 1:
                    locid = int(x)
                    if locid not in self.client.locations_checked:
                        self.client.check_location_IDs.append(locid)
                    logger.debug("Secret portal location checked: " + str(locid))

        elif msgType == MessageType.Deathlink:
            self.deathTime = message[1]

        elif msgType == MessageType.Victory:
            self.goaled = True

        elif msgType == MessageType.RequestAllItems:
            self.client.get_items()

        elif msgType == MessageType.Handshake:
            logger.debug("Attempting to respond to handshake")
            self.send(MessageType.Handshake, [str(self.client.connectedToAp)])
            logger.debug("Responded to Handshake")

        elif msgType == MessageType.HasSlotData:
            if message[0] == "0":
                self.hasSlotData = False
            else:
                self.hasSlotData = True

        elif msgType == MessageType.GetCurrentIndex:
            self.client_item_index = int(message[1])

        elif msgType == MessageType.DataStorage:
            self.client.set_data_storage(message[1], message[2], message[3])

    def send_singleItem(self, item, itemCnt, isLocal):
        msgCont = [str(item.item), str(itemCnt)]
        if isLocal:
            if not self.is_slot_location(item):
                msgCont.append("local")
        self.send(MessageType.ReceiveSingleItem, msgCont)


    def send_multipleItems(self, items, itemCnt):
        logger.debug(f"Sending multiple items {len(items)}")
        values = []

        msgLimit = 1 #Need to cap how long each message can be to prevent data from being lost

        currItemCount = 0
        currMsg = 0

        sendCnt = 0
        for item in items:
            if currItemCount == 0:
                values.append([])
            values[currMsg].append(item.item)

            #Local item check
            if item.player == self.client.slot:
                if self.is_local_location(item.location):
                    if not self.is_slot_location(item):
                        values[currMsg].append("local")

            currItemCount += 1
            sendCnt += 1
            if currItemCount > msgLimit:
                currItemCount = 0
                currMsg = currMsg + 1


        sendMsg = 0
        for msg in values:
            msg.append(itemCnt-(sendCnt-(msgLimit*sendMsg)))
            sendCnt -= 1
            sendMsg += 1
            self.send(MessageType.ReceiveAllItems, msg)

    def is_local_location(self, loc:int) -> bool:
        location_ids = ast.literal_eval(self.client.slot_data_info["non_remote_ids"])
        for id_set in location_ids:
            if id_set[0] == loc:
                return True

        return False

    #Commands in a slot location still need to be treated as remote, among other items
    def is_slot_location(self, item):
        return get_location_type(item.location) == "Slot"

    def send_slot_data(self, slotType, data):
        if self.hasSlotData:
            return

        if slotType == SlotDataType.keyblade_stats:
            splitNums = data.split(",")
            sendVal = [str(slotType)]
            currStat = 1

            sendLimit = 10

            for x in splitNums:
                sendVal.append(x)
                if currStat >= sendLimit:
                    self.send(MessageType.SendSlotData, sendVal)
                    sendVal = [str(slotType)]
                    currStat = 0
                currStat = currStat + 1
        elif slotType == SlotDataType.non_remote_ids:
            splitIndexes = data.split("[")
            sendVal = [str(slotType)]
            currId = 1

            sendLimit = 4
            for ind in splitIndexes:
                if len(ind) > 1:
                    splitVals = ind.split(" ")
                    for val in splitVals:
                        if len(val) > 1:
                            sendVal.append(val.replace(",","").replace("]",""))
                            if currId >= sendLimit:
                                self.send(MessageType.SendSlotData, sendVal)
                                sendVal = [str(slotType)]
                                currId = 0
                            currId = currId + 1
            #Send remaining location data
            if len(sendVal) > 1:
                self.send(MessageType.SendSlotData, sendVal)
            self.client.dddPatched = True
        else:
            self.send(MessageType.SendSlotData, [str(slotType), str(data)])

    def send_client_cmd(self, cmdId, extParam):
        values = [str(cmdId)]
        if extParam != "":
            values.append(extParam)
        logger.debug(f"Sending client command to player: {cmdId}")
        self.send(MessageType.ClientCommand, values)

    def item_msg(self, itemName:str, owningPlayer:str, itemCategory:str):
        self.send(MessageType.ItemPrompt, [itemName, owningPlayer, itemCategory])

    def shutdown_server(self):
        self.client_socket.close()
        self.server_socket.close()