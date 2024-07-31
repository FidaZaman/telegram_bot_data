# Telegram Merit Bot

A simple Telegram bot that provides specific images based on the user's merit position.

## Features

- Responds to the `/check` command.
- Validates merit positions from 1 to 301.
- Sends relevant images based on the user's merit position.

## Setup

1. **Create a Bot:**
   - Visit [@BotFather](https://t.me/BotFather) on Telegram and create a new bot to get your bot token.

2. **Clone the Repository:**
   ```bash
   git clone https://github.com/FidaZaman/telegram_bot_data.git
   cd telegram_bot_data
3. Install Dependencies:
```python
pip install requests
```

4. Configure Bot Token:
Replace `"YOUR_BOT_TOKEN"` in `main.py` with your actual token.

## Usage
Run the bot:
```python
python main.py
```
The bot will prompt users for their merit position using the `/check` command and send back relevant images if available.

## License
This project is licensed under the MIT License.