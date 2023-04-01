from urllib.request import urlopen

MAIN = "https://raw.githubusercontent.com/GabbaTK/battle-of-the-py/main/main.py"
CLIENT = "https://raw.githubusercontent.com/GabbaTK/battle-of-the-py/main/client.py"
SERVER = "https://raw.githubusercontent.com/GabbaTK/battle-of-the-py/main/server.py"

with urlopen(MAIN) as response:
    with open("main.py", "wb") as MAIN_FILE:
        MAIN_FILE.write(response.read())

with urlopen(CLIENT) as response:
    with open("client.py", "wb") as CLIENT_FILE:
        CLIENT_FILE.write(response.read())

with urlopen(SERVER) as response:
    with open("server.py", "wb") as SERVER_FILE:
        SERVER_FILE.write(response.read())
