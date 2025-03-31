import tkinter as tk
from tkinter import messagebox
import requests
import json


def load_config():
    try:
        with open('config.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        messagebox.showerror("Error",
                             "config.json not found. Please make sure it exists.")
        return None
    except json.JSONDecodeError:
        messagebox.showerror("Error",
                             "config.json is malformed. Please check its format.")
        return None


def update_status():
    config = load_config()
    if not config or 'token' not in config:
        return

    status_text = custom_status_entry.get()
    selected_status = status_var.get()

    if selected_status:
        url = "https://discord.com/api/v8/users/@me/settings"
        headers = {"Authorization": config['token']}
        jsondata = {
            "status": selected_status,
            "custom_status": {"text": status_text}
        }

        try:
            response = requests.patch(url, headers=headers, json=jsondata)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            messagebox.showinfo("Success", "Your status has been updated!")
        except requests.RequestException as e:
            messagebox.showerror("Error", f"Failed to update status: {str(e)}")
    else:
        messagebox.showwarning("Warning",
                               "Please select a status before updating.")


# Create the main window
root = tk.Tk()
root.title("Discord Status Updater")

# Variable to hold the status selection
status_var = tk.StringVar(value="online")  # Default to "online"

# Radio buttons for status selection
statuses = ["online", "invisible", "dnd", "idle"]
status_label = tk.Label(root, text="Select your status:")
status_label.pack(pady=10)

for status in statuses:
    radio = tk.Radiobutton(root, text=status, value=status,
                           variable=status_var)
    radio.pack(anchor=tk.W)

# Entry for custom status
custom_status_label = tk.Label(root,
                               text="Enter your custom status (optional):")
custom_status_label.pack(pady=10)

custom_status_entry = tk.Entry(root, width=50)
custom_status_entry.pack(pady=10)

# Update button
update_button = tk.Button(root, text="Update Status", command=update_status)
update_button.pack(pady=20)

# Start the application
root.mainloop()
