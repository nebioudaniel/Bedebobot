# Student Networking & AI Feedback Bot

A modern, asynchronous Telegram bot built with `python-telegram-bot` (v20+). This tool is designed to gather qualitative research and feedback from students to help build the future of AI-driven networking.

---

##  Features
* **Modern UI:** Uses `InlineKeyboardMarkup` for a clean, button-based interface.
* **Dual-Track Feedback:** Specifically collects "Study Struggles" and "Dream AI Solutions."
* **Live Admin Alerts:** Automatically forwards user responses and metadata (Name/Username) to a specified Admin ID.
* **HTML Formatting:** Fully supports bold and italic text for a professional look.
* **State Management:** Tracks whether a user is reporting a problem or a solution using `user_data`.

---

##  Setup & Installation

### 1. Requirements
* Python 3.10 or higher
* A Telegram Bot Token (from [@BotFather](https://t.me/botfather))

### 2. Install Dependencies

pip install python-telegram-bot

3. Configuration

Open the script and update the configuration section with your credentials:
Python

# --- CONFIGURATION ---
TOKEN = "YOUR_BOT_TOKEN_HERE"
ADMIN_ID = "YOUR_TELEGRAM_ID_HERE" 
# ---------------------

4. Run the Bot
Bash

python bot.py

 Project Logic

    /start: Greets the user and presents two options.

    Callback Handlers: Captures the button click and updates the user's "mode" (Problem vs. Solution).

    Message Handler: Captures the user's text input and forwards it to the Admin.

    Error Handling: Includes a basic try/except block to ensure messages are delivered even if HTML parsing fails.

 Security Warning

Important: Your TOKEN and ADMIN_ID are sensitive information.

    Never commit your token directly to a public GitHub repository.

    Recommendation: Use environment variables or a .env file to store these values securely.

 Contributing

If you want to add features like database integration or AI-powered auto-replies, feel free to fork this repo and submit a pull request!




### 💡 Pro-Tip for your Code
In your current code, you have a **hidden character** (a non-breaking space) after `ADMIN_ID = "7173564024"`. If you get an error when running it, make sure there are no invisible spaces at the end of that line!

Would you like me to help you set up a `requirements.txt` file for this project as
