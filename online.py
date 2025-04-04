import requests
import os
import json

authorization = {}
with open('config.json', 'r') as f:
    authorization.update(json.loads(f.read()))

url = "https://discord.com/api/v8/users/@me/settings"

header = {
    "authorization":f"{authorization['token']}"
}
jsondata = {
    "status":"online",
    "custom_status": {
        "text": ""
    }
}

request = requests.patch(url, headers=header, json=jsondata)
