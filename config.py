import os

API_ID = API_ID =  

API_HASH = os.environ.get("API_HASH", "b4495d7b9db5bb280121b4eeeb68331c")

BOT_TOKEN = os.environ.get("BOT_TOKEN", 6719287900:AAHFQ4IeEe9aC62Xh_FOnb6xUwEltq1iDEE"")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", ))

LOG = ,

# UPDATE_GRP = , # bot sat group

# auth_chats = []

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1923922961").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


