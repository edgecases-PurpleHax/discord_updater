import requests
import time
import json
authorization = {}
with open('config.json', 'r') as f:
    authorization.update(json.loads(f.read()))
url = "https://discord.com/api/v8/users/@me/settings"

header = {
    "authorization": f"{authorization['token']}"
}
message = []
with open("custom_status_messages.txt", "r", encoding="utf-8") as f:
    for line in f.readlines():
        if line not in message:
            message.append(line)
i = 0
while True:
    for i in range(0, len(message)):
        jsondata = {
            "status": "online",
            "custom_status": {
                # "text": f"{message[random.randint(0, len(message)) - 1]}"
                "text": f"{message[i]}"
            }

        }
        request = requests.patch(url, headers=header, json=jsondata)
        time.sleep(authorization['update_time']*60)
        i = i + 1
    if i >= len(message):
        i = 0
