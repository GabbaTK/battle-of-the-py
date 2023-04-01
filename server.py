import socket
from time import sleep
from os import system

LOGO_HIT = """

▀█▀ █░█ █▀▀   █▀█ █▀█ █▀█ █▀█ █▄░█ █▀▀ █▄░█ ▀█▀   █░█ █ ▀█▀   █▄█ █▀█ █░█ █
░█░ █▀█ ██▄   █▄█ █▀▀ █▀▀ █▄█ █░▀█ ██▄ █░▀█ ░█░   █▀█ █ ░█░   ░█░ █▄█ █▄█ ▄
"""
LOGO_HIT_SHIP = """
█░█ █ ▀█▀ █
█▀█ █ ░█░ ▄
"""
LOGO_MISS_SHIP = """

█▀▄▀█ █ █▀ █▀ █
█░▀░█ █ ▄█ ▄█ ▄
"""
LOGO_WIN = """

██╗░░░██╗░█████╗░██╗░░░██╗  ░██╗░░░░░░░██╗░█████╗░███╗░░██╗  ██╗██╗
╚██╗░██╔╝██╔══██╗██║░░░██║  ░██║░░██╗░░██║██╔══██╗████╗░██║  ██║██║
░╚████╔╝░██║░░██║██║░░░██║  ░╚██╗████╗██╔╝██║░░██║██╔██╗██║  ██║██║
░░╚██╔╝░░██║░░██║██║░░░██║  ░░████╔═████║░██║░░██║██║╚████║  ╚═╝╚═╝
░░░██║░░░╚█████╔╝╚██████╔╝  ░░╚██╔╝░╚██╔╝░╚█████╔╝██║░╚███║  ██╗██╗
░░░╚═╝░░░░╚════╝░░╚═════╝░  ░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚══╝  ╚═╝╚═╝
"""
LOGO_LOSE = """
██╗░░░██╗░█████╗░██╗░░░██╗  ██╗░░░░░░█████╗░░██████╗████████╗██╗██╗
╚██╗░██╔╝██╔══██╗██║░░░██║  ██║░░░░░██╔══██╗██╔════╝╚══██╔══╝██║██║
░╚████╔╝░██║░░██║██║░░░██║  ██║░░░░░██║░░██║╚█████╗░░░░██║░░░██║██║
░░╚██╔╝░░██║░░██║██║░░░██║  ██║░░░░░██║░░██║░╚═══██╗░░░██║░░░╚═╝╚═╝
░░░██║░░░╚█████╔╝╚██████╔╝  ███████╗╚█████╔╝██████╔╝░░░██║░░░██╗██╗
░░░╚═╝░░░░╚════╝░░╚═════╝░  ╚══════╝░╚════╝░╚═════╝░░░░╚═╝░░░╚═╝╚═╝
"""
LOGO_NORMAL = """
██████╗░░█████╗░████████╗████████╗██╗░░░░░███████╗  ░██████╗██╗░░██╗██╗██████╗░
██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║░░░░░██╔════╝  ██╔════╝██║░░██║██║██╔══██╗
██████╦╝███████║░░░██║░░░░░░██║░░░██║░░░░░█████╗░░  ╚█████╗░███████║██║██████╔╝
██╔══██╗██╔══██║░░░██║░░░░░░██║░░░██║░░░░░██╔══╝░░  ░╚═══██╗██╔══██║██║██╔═══╝░
██████╦╝██║░░██║░░░██║░░░░░░██║░░░███████╗███████╗  ██████╔╝██║░░██║██║██║░░░░░
╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░╚══════╝╚══════╝  ╚═════╝░╚═╝░░╚═╝╚═╝╚═╝░░░░░
"""
LOGO_DEV = """
██████╗░░█████╗░████████╗████████╗██╗░░░░░███████╗  ░██████╗██╗░░██╗██╗██████╗░
██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║░░░░░██╔════╝  ██╔════╝██║░░██║██║██╔══██╗
██████╦╝███████║░░░██║░░░░░░██║░░░██║░░░░░█████╗░░  ╚█████╗░███████║██║██████╔╝
██╔══██╗██╔══██║░░░██║░░░░░░██║░░░██║░░░░░██╔══╝░░  ░╚═══██╗██╔══██║██║██╔═══╝░
██████╦╝██║░░██║░░░██║░░░░░░██║░░░███████╗███████╗  ██████╔╝██║░░██║██║██║░░░░░
╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░╚══════╝╚══════╝  ╚═════╝░╚═╝░░╚═╝╚═╝╚═╝░░░░░
                                                                        ──╔╗──────────────╔╗
                                                                        ──║║──────────────║║
                                                                        ╔═╝╠══╦╗╔╗╔╗╔╦══╦═╝╠══╗
                                                                        ║╔╗║║═╣╚╝║║╚╝║╔╗║╔╗║║═╣
                                                                        ║╚╝║║═╬╗╔╝║║║║╚╝║╚╝║║═╣
                                                                        ╚══╩══╝╚╝─╚╩╩╩══╩══╩══╝
"""
LOGO_PLAYER_BOARD = """

▒█▀▀▀█ ▀▀█▀▀ ▒█░▒█ ▒█▀▀▀ ▒█▀▀█ 　 ▒█▀▀█ ▒█░░░ ░█▀▀█ ▒█░░▒█ ▒█▀▀▀ ▒█▀▀█ ▒█▀▀▀█ 　 ▒█▀▀█ ▒█▀▀▀█ ░█▀▀█ ▒█▀▀█ ▒█▀▀▄ 
▒█░░▒█ ░▒█░░ ▒█▀▀█ ▒█▀▀▀ ▒█▄▄▀ 　 ▒█▄▄█ ▒█░░░ ▒█▄▄█ ▒█▄▄▄█ ▒█▀▀▀ ▒█▄▄▀ ░▀▀▀▄▄ 　 ▒█▀▀▄ ▒█░░▒█ ▒█▄▄█ ▒█▄▄▀ ▒█░▒█ 
▒█▄▄▄█ ░▒█░░ ▒█░▒█ ▒█▄▄▄ ▒█░▒█ 　 ▒█░░░ ▒█▄▄█ ▒█░▒█ ░░▒█░░ ▒█▄▄▄ ▒█░▒█ ▒█▄▄▄█ 　 ▒█▄▄█ ▒█▄▄▄█ ▒█░▒█ ▒█░▒█ ▒█▄▄▀
"""
LOGO_HIT_BOARD = """

▒█░▒█ ▀█▀ ▀▀█▀▀ 　 ▒█▀▀█ ▒█▀▀▀█ ░█▀▀█ ▒█▀▀█ ▒█▀▀▄ 
▒█▀▀█ ▒█░ ░▒█░░ 　 ▒█▀▀▄ ▒█░░▒█ ▒█▄▄█ ▒█▄▄▀ ▒█░▒█ 
▒█░▒█ ▄█▄ ░▒█░░ 　 ▒█▄▄█ ▒█▄▄▄█ ▒█░▒█ ▒█░▒█ ▒█▄▄▀
"""
LOGO_POSITION_BOARD = """

▒█▀▀█ ▒█▀▀▀█ ▒█▀▀▀█ ▀█▀ ▀▀█▀▀ ▀█▀ ▒█▀▀▀█ ▒█▄░▒█ 　 ▒█▀▀█ ▒█▀▀▀█ ░█▀▀█ ▒█▀▀█ ▒█▀▀▄ 
▒█▄▄█ ▒█░░▒█ ░▀▀▀▄▄ ▒█░ ░▒█░░ ▒█░ ▒█░░▒█ ▒█▒█▒█ 　 ▒█▀▀▄ ▒█░░▒█ ▒█▄▄█ ▒█▄▄▀ ▒█░▒█ 
▒█░░░ ▒█▄▄▄█ ▒█▄▄▄█ ▄█▄ ░▒█░░ ▄█▄ ▒█▄▄▄█ ▒█░░▀█ 　 ▒█▄▄█ ▒█▄▄▄█ ▒█░▒█ ▒█░▒█ ▒█▄▄▀
"""
# + - ship
# x - hit
# # - miss
#   - null

# First number (Y) then letter (X)

SERVER_POSITION_BOARD = [[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]]
SERVER_HIT_BOARD = [[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]]

PLAYER_POSITION_BOARD = [[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]]
LETTER_SET = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

PORT = 8651
IP = socket.gethostbyname(socket.gethostname())
SERVER_ADDRESS = (IP, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT!"
HEADER = 64

SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER.bind(SERVER_ADDRESS)

def printBoardPosition(BOARD):
    print("    1   2   3   4   5   6   7   8   9   10")
    print("  -----------------------------------------")
    for LINE in range(10):
        print(f"{LETTER_SET[LINE]} | ", end="")
        for SQUARE in range(10):
            COLOR_PRINT = BOARD[LINE][SQUARE]

            if BOARD[LINE][SQUARE] == "+":
                COLOR_PRINT = "\033[34m+\033[37m"
            elif BOARD[LINE][SQUARE] == "X":
                COLOR_PRINT = "\033[31mX\033[37m"

            print(f"{COLOR_PRINT} | ", end="")
        print()
        print("  -----------------------------------------")

def printBoardHit():
    print("    1   2   3   4   5   6   7   8   9   10")
    print("  -----------------------------------------")
    for LINE in range(10):
        print(f"{LETTER_SET[LINE]} | ", end="")
        for SQUARE in range(10):
            COLOR_PRINT = SERVER_HIT_BOARD[LINE][SQUARE]

            if SERVER_HIT_BOARD[LINE][SQUARE] == "X":
                COLOR_PRINT = "\033[31mX\033[37m"

            print(f"{COLOR_PRINT} | ", end="")
        print()
        print("  -----------------------------------------")

def positionClose(POSITION_A, POSITION_B, DIRECTION): # DIRECTION - [H]orizontaly [V]erticaly
    ROW_DIFFERENCE = abs(LETTER_SET.index(POSITION_A[0]) - LETTER_SET.index(POSITION_B[0]))
    COL_DIFFERENCE = abs(POSITION_A[1] - POSITION_B[1])

    if ROW_DIFFERENCE != COL_DIFFERENCE:
        if DIRECTION == "H":
            if ROW_DIFFERENCE == 0 and COL_DIFFERENCE == 1:
                return True
        if DIRECTION == "V":
            if COL_DIFFERENCE == 0 and ROW_DIFFERENCE == 1:
                return True

    return False

def positionToInt(POSITION):
    NEW_POSITION = []
    
    for INDEX in range(len(POSITION)):
        NEW_POSITION.append([list(POSITION[INDEX])[0], int("".join(list(POSITION[INDEX])[1:len(list(POSITION[INDEX]))]))])

    return NEW_POSITION

def setupShips():
    for SHIP in [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]:
        VALID = False
        while not VALID:
            VALID = True
            POSITION = input(f"Enter the position for the piece of lenght {SHIP}, first letter then number (C8), must have all the spaces it occupies, so for 3 space it will be (G4-G5-G6) >>>").split("-")
            if len(POSITION) != SHIP:
                VALID = False
            POSITION = positionToInt(POSITION)
            for CHECK_INDEX in range(len(POSITION)):
                if SERVER_POSITION_BOARD[LETTER_SET.index(POSITION[CHECK_INDEX][0])][POSITION[CHECK_INDEX][1] - 1] != " ":
                    VALID = False
            if SHIP != 1:
                DIRECTION = "H"
                if (POSITION[0][0] != POSITION[1][0]) and (POSITION[0][1] == POSITION[1][1]):
                    DIRECTION = "V"
                for CHECK_INDEX in range(len(POSITION) - 1):
                    if not positionClose(POSITION[CHECK_INDEX], POSITION[CHECK_INDEX + 1], DIRECTION):
                        VALID = False

            if VALID:
                for SPACE in range(SHIP):
                    SERVER_POSITION_BOARD[LETTER_SET.index(POSITION[SPACE][0])][POSITION[SPACE][1] - 1] = "+"
            else:
                print("Invalid position, please try again")
        printBoardPosition(SERVER_POSITION_BOARD)

def sendData(PLAYER, MESSAGE):
    MESSAGE = MESSAGE.encode(FORMAT)
    MESSAGE_LENGHT = str(len(MESSAGE)).encode(FORMAT) + b" " * (HEADER - (len(str(len(MESSAGE)).encode(FORMAT))))
    PLAYER.send(MESSAGE_LENGHT)
    PLAYER.send(MESSAGE)

def receiveData(PLAYER):
    LENGHT = PLAYER.recv(HEADER).decode(FORMAT)
    DATA = PLAYER.recv(int(LENGHT)).decode(FORMAT)

    return DATA

def receivedDataToTable(DATA):
    TABLE = []
    DATA = DATA.split("-")

    for ROW in DATA:
        TABLE.append(list(ROW))

    return TABLE

def getInput():
    INPUT_SQUARE = list(input("Where do you want to shoot? >>>"))
    SQUARE = [INPUT_SQUARE[0], int("".join(INPUT_SQUARE[1:len(INPUT_SQUARE)]))]

    if SQUARE[0] in LETTER_SET and SQUARE[1] > 0 and SQUARE[1] < 11:
        return SQUARE
    else:
        print("Invalid square!")
        return getInput()

def checkWin(BOARD):
    WON = True

    for ROW in BOARD:
        for SQUARE in ROW:
            if SQUARE == "+":
                WON = False

    return WON

def serverTurn(PLAYER, DEV_MODE, HIT = False):
    system("cls")

    sendData(PLAYER, "TABLE_POSITION_GET")
    DATA = receiveData(PLAYER)
    PLAYER_POSITION_BOARD = receivedDataToTable(DATA)

    if DEV_MODE:
        print(LOGO_PLAYER_BOARD)
        printBoardPosition(PLAYER_POSITION_BOARD)

    if checkWin(PLAYER_POSITION_BOARD):
        sendData(PLAYER, "GAME_END_SERVER")
        system("cls")
        print(LOGO_WIN)
        return "END"

    print(LOGO_HIT_BOARD)
    printBoardHit()
    print(LOGO_POSITION_BOARD)
    printBoardPosition(SERVER_POSITION_BOARD)

    if HIT:
        print(f"\033[31m{LOGO_HIT_SHIP}\033[37m")

    SQUARE = getInput()
    SQUARE[0] = str(LETTER_SET.index(SQUARE[0]))
    SQUARE[1] = str(SQUARE[1] - 1)

    sendData(PLAYER, "SHOOT_" + "-".join(SQUARE))

    DATA = receiveData(PLAYER)

    if DATA == "SHOOT_MISS":
        print(f"\033[31m{LOGO_MISS_SHIP}\033[37m")
        SERVER_HIT_BOARD[int(SQUARE[0])][int(SQUARE[1])] = "#"
    if DATA == "SHOOT_HIT":
        SERVER_HIT_BOARD[int(SQUARE[0])][int(SQUARE[1])] = "X"
        serverTurn(PLAYER, DEV_MODE, True)

def startServer(DEV_MODE):
    if DEV_MODE:
        LOGO = LOGO_DEV
    else:
        LOGO = LOGO_NORMAL

    print(f"""
{LOGO}

STARTING SERVER
    """)

    SERVER.listen()
    print(f"SERVER IS LISTENING ON {IP}")
    PLAYER, ADDRESS = SERVER.accept()
    print(f"NEW CONNECTION FROM {ADDRESS[0]}")

    if DEV_MODE:
        sendData(PLAYER, "DEV_MODE_TRUE")
    else:
        sendData(PLAYER, "DEV_MODE_FALSE")

    DATA = receiveData(PLAYER)
    if DATA != DISCONNECT_MESSAGE:
        setupLoop(PLAYER, DEV_MODE)
        return 0
    else:
        print("CLIENT SENT DISCONNECT REQUEST")
        startServer(DEV_MODE)

def setupLoop(PLAYER, DEV_MODE):
    print("STARTING GAME")

    print("...5", end="\r")
    sleep(1)
    print("...4", end="\r")
    sleep(1)
    print("...3", end="\r")
    sleep(1)
    print("...2", end="\r")
    sleep(1)
    print("...1")
    sleep(1)

    sendData(PLAYER, "SETUP")
    system("cls")
    print("SETUP POSITION")
    
    printBoardPosition(SERVER_POSITION_BOARD)
    setupShips()

    print("Waiting for other person...")

    sendData(PLAYER, "SETUP_READY")
    receiveData(PLAYER)
    sendData(PLAYER, "GAME_BEGIN")
    receiveData(PLAYER)
    sleep(0.1)

    system("cls")

    gameLoop(PLAYER, DEV_MODE)

def gameLoop(PLAYER, DEV_MODE):
    TURN = "S"
    while True:
        if TURN == "S":
            sendData(PLAYER, "TABLE_POSITION_GET")
            DATA = receiveData(PLAYER)
            PLAYER_POSITION_BOARD = receivedDataToTable(DATA)

            if DEV_MODE:
                print(LOGO_PLAYER_BOARD)
                printBoardPosition(PLAYER_POSITION_BOARD)

            if serverTurn(PLAYER, DEV_MODE) == "END":
                return 0
            sendData(PLAYER, "TURN_NEXT")
            sendData(PLAYER, "GAME_CONTINUE")
            TURN = "C"
        elif TURN == "C":
            while True:
                DATA = receiveData(PLAYER)
                
                if DATA == "TURN_NEXT":
                    break
                elif DATA.startswith("SHOOT_"):
                    SQUARE = DATA.split("_")
                    SQUARE = SQUARE[1].split("-")

                    if SERVER_POSITION_BOARD[int(SQUARE[0])][int(SQUARE[1])] == " " or SERVER_POSITION_BOARD[int(SQUARE[0])][int(SQUARE[1])] == "#":
                        SERVER_POSITION_BOARD[int(SQUARE[0])][int(SQUARE[1])] = "#"
                        sendData(PLAYER, "SHOOT_MISS")
                        system("cls")
                        print(LOGO_POSITION_BOARD)
                        printBoardPosition(SERVER_POSITION_BOARD)
                    elif SERVER_POSITION_BOARD[int(SQUARE[0])][int(SQUARE[1])] == "+":
                        SERVER_POSITION_BOARD[int(SQUARE[0])][int(SQUARE[1])] = "X"

                        sendData(PLAYER, "SHOOT_HIT")
                        system("cls")
                        print(f"\033[31m{LOGO_HIT}\033[37m")
                        print(LOGO_POSITION_BOARD)
                        printBoardPosition(SERVER_POSITION_BOARD)
                        
                        if checkWin(SERVER_POSITION_BOARD):
                            sendData(PLAYER, "GAME_END_CLIENT")
                            system("cls")
                            print(LOGO_LOSE)
                            return 0
                        else:
                            sendData(PLAYER, "GAME_CONTINUE")

            TURN = "S"
