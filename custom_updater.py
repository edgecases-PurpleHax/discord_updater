import requests
import time
import json

# Load authorization data from a config file
authorization = {}
with open('config.json', 'r') as f:
    authorization.update(json.loads(f.read()))

url = "https://discord.com/api/v8/users/@me/settings"

header = {
    "Authorization": f"{authorization['token']}"
}

message = []
with open("custom_status_messages.txt", "r", encoding="utf-8") as f:
    for line in f.readlines():
        line = line.strip()  # Remove any trailing newline characters
        if len(line) > 29:  # Split the message if longer than 29 characters
            mid_point = len(line) // 2
            # Find a space near the midpoint to split at a word boundary
            space_before = line.rfind(' ', 0, mid_point)
            space_after = line.find(' ', mid_point)
            if space_before == -1 or (space_after != -1 and space_after - mid_point < mid_point - space_before):
                split_point = space_after
            else:
                split_point = space_before
            message.append(line[:split_point])
            message.append(line[split_point+1:])
        else:
            message.append(line)

def parse_time_interval(time_str):
    """Parse time interval from string with unit and convert to seconds."""
    unit = time_str
    number = int(authorization['update_time'])
    if unit == 's':
        return number
    elif unit == 'm':
        return number * 60
    elif unit == 'h':
        return number * 3600
    return number  # Default to seconds if no unit is found

# Determine the update interval in seconds
update_interval_seconds = parse_time_interval(authorization[
                                                  'update_time_interval'])

# Continuously update the Discord status in a loop
i = 0
while True:
    for i in range(len(message)):
        jsondata = {
            "status": "online",
            "custom_status": {
                "text": message[i]
            }
        }
        requests.patch(url, headers=header, json=jsondata)
        time.sleep(update_interval_seconds)
    i = 0  # Reset index after completing the loop
