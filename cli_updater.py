import argparse
import requests
import json


def load_config():
    try:
        with open('config.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Error: config.json not found. Please make sure it exists.")
        return None
    except json.JSONDecodeError:
        print("Error: config.json is malformed. Please check its format.")
        return None


def update_status(status, custom_status):
    config = load_config()
    if not config or 'token' not in config:
        return

    if status:
        url = "https://discord.com/api/v8/users/@me/settings"
        headers = {"Authorization": config['token']}
        jsondata = {
            "status": status,
            "custom_status": {"text": custom_status}
        }

        try:
            response = requests.patch(url, headers=headers, json=jsondata)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            print("Success: Your status has been updated!")
        except requests.RequestException as e:
            print(f"Error: Failed to update status: {str(e)}")
    else:
        print("Warning: Please specify a status before updating.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Update Discord Status')
    parser.add_argument('--status',
                        choices=['online', 'invisible', 'dnd', 'idle'],
                        required=True,
                        help='The main status to set (online, invisible, dnd, idle)')
    parser.add_argument('--custom_status', type=str, default='',
                        help='Custom text for the Discord status (optional)')

    args = parser.parse_args()
    update_status(args.status, args.custom_status)
