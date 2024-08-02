import requests
import time

merit_positions = [79, 85, 99, 117, 128, 139, 159, 167, 188, 213, 219, 220, 228, 232, 254, 276, 300, 301, 217, 259, 97, 138, 299]

def get_updates(bot_token, offset=None):
    """Fetches new updates from the Telegram Bot API."""
    base_url = f"https://api.telegram.org/bot{bot_token}/getUpdates"
    params = {"offset": offset, "timeout": 60}

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching updates: {e}")
        return None

def send_message(bot_token, chat_id, text):
    """Sends a message to a Telegram chat."""
    base_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {"chat_id": chat_id, "text": text}

    try:
        response = requests.post(base_url, json=data)
        response.raise_for_status()
        print(f"Message sent successfully: {response.json()}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending message: {e}")

def send_image(bot_token, chat_id, image_url):
    """Sends an image to a Telegram chat."""
    base_url = f"https://api.telegram.org/bot{bot_token}/sendPhoto"
    data = {"chat_id": chat_id, "photo": image_url}

    try:
        response = requests.post(base_url, data=data)  # Use data instead of json for form-data
        response.raise_for_status()
        print(f"Image sent successfully: {response.json()}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending image: {e}")
        print(f"Image URL: {image_url}")
        # Print response content for debugging
        if response is not None:
            print("Response content:", response.content)

def is_valid_merit_position(merit_position):
    """Checks if the merit position is a valid integer within the expected range."""
    try:
        position = int(merit_position)
        return 1 <= position <= 301
    except ValueError:
        return False

def main():
    """Main function to run the Telegram bot."""
    # Replace with your actual bot token (DO NOT SHARE THIS PUBLICLY)
    bot_token = "your_bot_tocken_here"

    offset = None
    awaiting_position = {}

    while True:
        updates = get_updates(bot_token, offset)

        if updates is None or not updates["ok"]:
            time.sleep(1)
            continue

        for update in updates["result"]:
            update_id = update["update_id"]

            if "message" in update:
                message = update["message"]
                chat_id = message["chat"]["id"]

                if "text" in message:
                    text = message["text"].strip().lower()

                    if text.startswith("/check"):
                        send_message(bot_token, chat_id, "Please enter the merit position you wish to check.")
                        awaiting_position[chat_id] = True
                    elif chat_id in awaiting_position:
                        merit_position = text

                        if is_valid_merit_position(merit_position):
                            position = int(merit_position)

                            if position in merit_positions:
                                image_url = f"https://raw.githubusercontent.com/FidaZaman/telegram_bot_data/main/images/image02/{position}.png"
                                send_image(bot_token, chat_id, image_url)
                            else:
                                send_message(bot_token, chat_id, "Merit position not found.")
                        else:
                            send_message(bot_token, chat_id, "Invalid merit position. Please enter a number between 1 and 301.")

                        del awaiting_position[chat_id]
                    else:
                        send_message(bot_token, chat_id, "Please start with /check to enter a merit position.")

            offset = update_id + 1

        time.sleep(1)

if __name__ == "__main__":
    main()
