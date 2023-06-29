import time
USER_ID = ""  # uuid
USER_PROJECT_ID = ""  # uuid
TENANT_CODE = 71000004
X_TOKEN = ""  # uuid

COOKIES = {
    "SERVERID": "",
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50",
    "x-token": X_TOKEN
}

def getTime():
    return round(time.time(),3)