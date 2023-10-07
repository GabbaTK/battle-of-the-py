import socket
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
WARNING = """

░██╗░░░░░░░██╗░█████╗░██████╗░███╗░░██╗██╗███╗░░██╗░██████╗░
░██║░░██╗░░██║██╔══██╗██╔══██╗████╗░██║██║████╗░██║██╔════╝░
░╚██╗████╗██╔╝███████║██████╔╝██╔██╗██║██║██╔██╗██║██║░░██╗░
░░████╔═████║░██╔══██║██╔══██╗██║╚████║██║██║╚████║██║░░╚██╗
░░╚██╔╝░╚██╔╝░██║░░██║██║░░██║██║░╚███║██║██║░╚███║╚██████╔╝
░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝╚═╝░░╚══╝░╚═════╝░

THIS SERVER IS RUNNING IN DEV MODE, THE SERVER WILL BE ABLE TO SEE
               THE POSITION OF YOUR SHIPS!!

             ARE YOU SURE YOU WANT TO CONNECT?

                        [y] Yes
                        [n] No
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
PLAYER_HIT_BOARD = [[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
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
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT!"
HEADER = 64

CLIENT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def sendData(MESSAGE):
    MESSAGE = MESSAGE.encode(FORMAT)
    MESSAGE_LENGHT = str(len(MESSAGE)).encode(FORMAT) + b" " * (HEADER - (len(str(len(MESSAGE)).encode(FORMAT))))
    CLIENT.send(MESSAGE_LENGHT)
    CLIENT.send(MESSAGE)

def receiveData():
    LENGHT = CLIENT.recv(HEADER).decode(FORMAT)
    DATA = CLIENT.recv(int(LENGHT)).decode(FORMAT)

    return DATA

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

def printBoardPosition():
    print("    1   2   3   4   5   6   7   8   9   10")
    print("  -----------------------------------------")
    for LINE in range(10):
        print(f"{LETTER_SET[LINE]} | ", end="")
        for SQUARE in range(10):
            COLOR_PRINT = PLAYER_POSITION_BOARD[LINE][SQUARE]

            if PLAYER_POSITION_BOARD[LINE][SQUARE] == "+":
                COLOR_PRINT = "\033[34m+\033[37m"
            elif PLAYER_POSITION_BOARD[LINE][SQUARE] == "X":
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
            COLOR_PRINT = PLAYER_HIT_BOARD[LINE][SQUARE]

            if PLAYER_HIT_BOARD[LINE][SQUARE] == "+":
                COLOR_PRINT = "\033[34m+\033[37m"
            elif PLAYER_HIT_BOARD[LINE][SQUARE] == "X":
                COLOR_PRINT = "\033[31mX\033[37m"

            print(f"{COLOR_PRINT} | ", end="")
        print()
        print("  -----------------------------------------")

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
                if PLAYER_POSITION_BOARD[LETTER_SET.index(POSITION[CHECK_INDEX][0])][POSITION[CHECK_INDEX][1] - 1] != " ":
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
                    PLAYER_POSITION_BOARD[LETTER_SET.index(POSITION[SPACE][0])][POSITION[SPACE][1] - 1] = "+"
            else:
                print("Invalid position, please try again")
        printBoardPosition()

def tableToDataTransmit(TABLE):
    TRANSMIT_DATA = ""

    for ROW in TABLE:
        TRANSMIT_DATA += "".join(ROW)
        TRANSMIT_DATA += "-"

    return TRANSMIT_DATA

def getInput():
    INPUT_SQUARE = list(input("Where do you want to shoot? >>>"))
    SQUARE = [INPUT_SQUARE[0], int("".join(INPUT_SQUARE[1:len(INPUT_SQUARE)]))]

    if SQUARE[0] in LETTER_SET and SQUARE[1] > 0 and SQUARE[1] < 11:
        return SQUARE
    else:
        print("Invalid square!")
        return getInput()

def playerTurn(HIT = False):
    system("cls")

    DATA = receiveData()

    if DATA == "GAME_END_CLIENT":
        system("cls")
        print(LOGO_WIN)
        return "END"
    if DATA == "GAME_END_SERVER":
        system("cls")
        print(LOGO_LOSE)
        return "END"

    print(LOGO_HIT_BOARD)
    printBoardHit()
    print(LOGO_POSITION_BOARD)
    printBoardPosition()

    if HIT:
        print(f"\033[31m{LOGO_HIT_SHIP}\033[37m")

    SQUARE = getInput()
    SQUARE[0] = str(LETTER_SET.index(SQUARE[0]))
    SQUARE[1] = str(SQUARE[1] - 1)

    sendData("SHOOT_" + "-".join(SQUARE))

    DATA = receiveData()

    if DATA == "SHOOT_MISS":
        print(f"\033[31m{LOGO_MISS_SHIP}\033[37m")
        PLAYER_HIT_BOARD[int(SQUARE[0])][int(SQUARE[1])] = "#"
    elif DATA == "SHOOT_HIT":
        print(f"\033[31m{LOGO_HIT_SHIP}\033[37m")
        PLAYER_HIT_BOARD[int(SQUARE[0])][int(SQUARE[1])] = "X"
        playerTurn(True)

def startClient():
    print(LOGO_NORMAL)
    print()
    IP = input("Enter the ip of the server >>>")
    ADDRESS = (IP, PORT)
    CLIENT.connect(ADDRESS)
    system("cls")

    
    DATA = receiveData()

    if DATA == "DEV_MODE_TRUE":
        print(WARNING)
        OPTION = input()
        if OPTION == "y":
            sendData("CONNECT")
            setupLoop()
        else:
            sendData(DISCONNECT_MESSAGE)
            exit()
    else:
        sendData("CONNECT")
        setupLoop()
            
def setupLoop():
    print("GAME IS STARTING, HOPEFULLY")
    DATA = receiveData()
    system("cls")

    if DATA == "SETUP":
        print("SETUP POSITION")
        printBoardPosition()
        setupShips()

        print("Waiting for other person...")

        sendData("SETUP_READY")
        receiveData()
        sendData("GAME_BEGIN")
        receiveData()

        system("cls")

        print(LOGO_HIT_BOARD)
        printBoardHit()
        print(LOGO_POSITION_BOARD)
        printBoardPosition()

        gameLoop()

def gameLoop():
    while True:
        DATA = receiveData()

        if DATA == "GAME_END_CLIENT":
            system("cls")
            print(LOGO_WIN)
            return "END"
        if DATA == "GAME_END_SERVER":
            system("cls")
            print(LOGO_LOSE)
            return "END"
        
        if DATA == "TABLE_POSITION_GET":
            sendData(tableToDataTransmit(PLAYER_POSITION_BOARD))
        elif DATA.startswith("SHOOT_"):
            SQUARE = DATA.split("_")
            SQUARE = SQUARE[1].split("-")
            
            if PLAYER_POSITION_BOARD[int(SQUARE[0])][int(SQUARE[1])] == " " or PLAYER_POSITION_BOARD[int(SQUARE[0])][int(SQUARE[1])] == "#":
                PLAYER_POSITION_BOARD[int(SQUARE[0])][int(SQUARE[1])] = "#"
                sendData("SHOOT_MISS")
                system("cls")
                print(LOGO_POSITION_BOARD)
                printBoardPosition()
            elif PLAYER_POSITION_BOARD[int(SQUARE[0])][int(SQUARE[1])] == "+" or PLAYER_POSITION_BOARD[int(SQUARE[0])][int(SQUARE[1])] == "X":
                PLAYER_POSITION_BOARD[int(SQUARE[0])][int(SQUARE[1])] = "X"
                sendData("SHOOT_HIT")
                system("cls")
                print(f"\033[31m{LOGO_HIT}\033[37m")
                print(LOGO_POSITION_BOARD)
                printBoardPosition()
        elif DATA == "TURN_NEXT":
            if playerTurn() == "END":
                return 0
            sendData("TURN_NEXT")

if __name__ == "__main__":
    startClient()
