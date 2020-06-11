#Ramaswamy, Anuj
DungeonDict = dict()
playerInv = []



class Room:
    '''This is the class Room which helps create and maintain the Dungeon dictionary.'''
    def __init__(self, roomNumber, desc, north, south, east, west):
        '''This is the constructor which initializes the class Room.'''
        self.desc = desc
        self.north = int(north)
        self.south = int(south)
        self.east = int(east)
        self.west = int(west)
        self.roomNumber = int(roomNumber)
        self.roomInv = []


def loaddungeon(filename):
    '''This function loads the layout of allrooms and places the player in the first room.'''
    f = open(filename)
    flag = 1
    roomNumberList = []
    fileContent = f.readlines()
    for line in fileContent:
        lineItems = line.split()
        roomNumberList.append(lineItems[0])
        room = Room(lineItems[0], getDesc(line), lineItems[-4], lineItems[-3], lineItems[-2], lineItems[-1])
        if flag == 1:
            playerStartPosition = room.roomNumber
            flag = 0
        DungeonDict[room.roomNumber] = room
    print(getDesc(fileContent[0]))
    return int(playerStartPosition)


def getDesc(line):
    '''This function helps in extracting the description for each room.'''
    res = ""
    i = 0
    while i < len(line):
        if line[i] == "\"":
            i += 1
            while line[i] != "\"":
                res += line[i]
                i += 1
            break
        else:
            i += 1
    return res

def north(playerPosition):
    '''This function moves the player to the room immediately to its north.'''
    if DungeonDict[playerPosition].north == -1:
        print("You can't go there")
        return playerPosition
    else:
        playerPosition = DungeonDict[playerPosition].north
        print(DungeonDict[playerPosition].desc)
        return playerPosition

def south(playerPosition):
    '''This function moves the player to the room immediately to its south.'''
    if DungeonDict[playerPosition].south == -1:
        print("You can't go there")
        return playerPosition
    else:
        playerPosition = DungeonDict[playerPosition].south
        print(DungeonDict[playerPosition].desc)
        return playerPosition


def east(playerPosition):
    '''This function moves the player to the room immediately to its east.'''
    if DungeonDict[playerPosition].east == -1:
        print("You can't go there")
        return playerPosition
    else:
        playerPosition = DungeonDict[playerPosition].east
        print(DungeonDict[playerPosition].desc)
        return playerPosition

def west(playerPosition):
    '''This function moves the player to the room immediately to its west.'''
    if DungeonDict[playerPosition].west == -1:
        print("You can't go there")
        return playerPosition
    else:
        playerPosition = DungeonDict[playerPosition].west
        print(DungeonDict[playerPosition].desc)
        return playerPosition


def loaditems(filename):
    '''This function loads the items and adds them to the players inventory.'''
    f = open(filename)
    fileContent = f.read()
    global playerInv
    playerInv = fileContent.split(',')
    playerInv[-1] = playerInv[-1][0:-1]
    for i in range(len(playerInv)):
        playerInv[i] = playerInv[i].strip()
    
def pinventory():
    '''This function displays what the player holds in his/her inventory.'''
    pItems = ''
    global playerInv
    for item in playerInv:
        pItems += item +', '
    if pItems == '':
        print("You have: nothing")
    else:
        print(f"You have: {pItems[:-2]}.")

def rinventory(playerPosition):
    '''This function displays the items in the room that the player is currently in.'''
    rItems = ''
    for item in DungeonDict[playerPosition].roomInv:
        rItems += item + ', '
    if rItems == '':
        print("This room contains: nothing")
    else:
        print(f"This room contains: {rItems[:-2]}.")


def take(item, playerPosition):
    '''This function helps the player take the item he/she wishes to take and adds it to his inventory.'''
    global playerInv
    if item in DungeonDict[playerPosition].roomInv:
        DungeonDict[playerPosition].roomInv.remove(item)
        playerInv.append(item)
    else:
        print("That item is not in this room.")

def drop(item, playerPosition):
    '''This function drops the item that is given as the argument and removes it from the player inventory and adds to the room's inventory.'''
    global playerInv
    if item in playerInv:
        playerInv.remove(item)
        DungeonDict[playerPosition].roomInv.append(item)
    else:
        print("You don't have that item.")


def adventure():
    '''This function is the main function which takes the user input and processes it.'''
    program = 1
    playerPosition = None
    allCommandsList = []
    while program == 1:
        userInput = input("$ ")
        commandList = userInput.split()
        if len(commandList)>1:
            allCommandsList.append(commandList[0])
            
        if commandList[0] == "loaddungeon":
            if len(commandList) == 1:
                    continue
            else:
                if allCommandsList.count("loaddungeon")>1:
                    print("Dungeon already loaded")
                else:
                    playerPosition = loaddungeon(commandList[1])

        elif commandList[0] == "loaditems":
            if len(commandList) == 1:
                    continue
            else:
                if allCommandsList.count("loaditems")>1:
                    print("Items already loaded")
                else:
                    loaditems(commandList[1])
                

        elif commandList[0] == "north":
            playerPosition = north(playerPosition)

        elif commandList[0] == "south":
            playerPosition = south(playerPosition)

        elif commandList[0] == "east":
            playerPosition = east(playerPosition)

        elif commandList[0] == "west":
            playerPosition = west(playerPosition)

        elif commandList[0] == "pinventory":
            pinventory()

        elif commandList[0] == "rinventory":
            rinventory(playerPosition)

        elif commandList[0] == "take":
            if len(commandList) == 1:
                continue
            else:
                take(commandList[1], playerPosition)

        elif commandList[0] == "drop":
            if len(commandList) == 1:
                continue
            else:
                drop(commandList[1], playerPosition)

        elif commandList[0] == "quit":
            program = 0
            print("you ended the program")


adventure()
