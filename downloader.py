from urllib.request import urlopen as uo

MAIN = "https://raw.githubusercontent.com/GabbaTK/battle-of-the-py/main/main.py"
CLIENT = "https://raw.githubusercontent.com/GabbaTK/battle-of-the-py/main/client.py"
SERVER = "https://raw.githubusercontent.com/GabbaTK/battle-of-the-py/main/server.py"

MAIN_DATA = uo(MAIN)
MAIN_CODE = MAIN_DATA.read()

with open("main.py", "w") as MAIN_FILE:
    MAIN_FILE.write(MAIN_CODE)

CLIENT_DATA = uo(CLIENT)
CLIENT_CODE = CLIENT_DATA.read()

with open("client.py", "w") as CLIENT_FILE:
    CLIENT_FILE.write(CLIENT_CODE)
                    
SERVER_DATA = uo(SERVER)
SERVER_CODE = SERVER_DATA.read()

with open("server.py", "w") as SERVER_FILE:
    SERVER_FILE.write(SERVER_CODE)