# Discord Status Updater - User Documentation

## 1. Introduction

This application sets a user's Discord status to "online" and updates their custom status at specified intervals using predefined messages. It reads these messages from `custom_status_messages.txt` and uses the time defined in `config.json` to manage the update frequency.

**Security Warning**: Your Discord token is sensitive information. Only use this application if you trust its source, and never share your token with unauthorized parties.

## 2. Prerequisites

- **Supported Operating Systems**: Any modern version of Windows that supports Python and command line operations.

## 3. Installation Guide

1. **Extract the ZIP File**: Extract the contents of the distributed ZIP file to your preferred location.
2. **Files Included**:
   - `custom_updater.exe`: The main application executable.
   - `example_config.json`: Configuration file for setting your Discord token and message update interval.
   - `custom_status_messages.txt`: File to input custom status messages, separated by new lines.

## 4. Configuration

Before you begin, rename `example_config.json` to `config.json` and follow the steps below to configure your application:

### Obtaining the Discord Token

1. Open Discord in your web browser (Firefox or Chrome recommended).
2. Access the Developer Tools by pressing `F12` or right-clicking the page and selecting "Inspect".
3. Navigate to the "Network" tab and reload the page.
4. Look for a network request that ends with `@me`.
5. In the request details, find the `Authorization` header and copy the token value. Be careful to keep this token secure as it allows access to your Discord account.

### Editing the `config.json` File

- Open `config.json` in a text editor.
- Replace the placeholder text next to the `"token"` key with your copied Discord token.
- To set the frequency of status updates, enter the desired interval in minutes using decimals under the `"update_time"` key (e.g., `0.5` for every 30 seconds).
- Save your changes and ensure this file is kept secure to prevent unauthorized access.

### Setting Custom Status Messages

- Open `custom_status_messages.txt` in a text editor.
- Enter the messages you wish your status to display, each on a new line. The application will cycle through these messages at the interval you set.

## 5. Using the Application

Double-click `custom_updater.exe` to run the application. Your status on Discord should update according to the specified intervals and messages.

## 6. Troubleshooting

Currently, no common issues have been identified. Should you encounter problems or require assistance, please reach out via the contact methods provided below. Consider checking the following if you encounter issues:

- Ensure the `config.json` file is named correctly and located in the same directory as `custom_updater.exe`.
- Verify that your internet connection is active and stable.

## 7. FAQ

**Q: Where do I find my Discord token?**
**A**: Follow the steps in the **Obtaining the Discord Token** section.

**Q: What happens if my Discord token expires or is revoked?**
**A**: You will need to obtain a new token following the same steps and update your `config.json` file accordingly.

**Q: How can I stop the application from updating my status?**
**A**: Simply close the `custom_updater.exe` application, or remove the messages from `custom_status_messages.txt`.

## 8. Contact Information

For support or feedback:
- **Discord**: _edgecase
- **Email**: [purplehaxttv@gmail.com](mailto:purplehaxttv@gmail.com)

## ROADMAP
Please check [here](https://github.com/edgecases-PurpleHax/discord_updater/tree/develop) for current features 
in development, future releases, etc. 