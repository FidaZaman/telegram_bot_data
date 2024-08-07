import requests
import time
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Dictionary of merit positions with corresponding email addresses
merit_positions = {
    0: "www.fidazaman@gmail.com",
    79: "jhosnaranidey1980@gmail.com",
    85: "mdhasnatislam708@gmail.com",
    97: "tanmay20278@gmail.com",
    99: "junaidbagdady1@gmail.com",
    117: "zonaid.rony22@gmail.com",
    128: "smanika691@gmail.com",
    138: "abdulmuhitsiyam@gmail.com",
    139: "rabiulawal.bd6340@gmail.com",
    159: "mdmeharabuddinchowdhury@gmail.com",
    167: "salehsadmansami@gmail.com",
    188: "ziaulhaque2304@gmail.com",
    213: "azmayenapip@gmail.com",
    217: "saadbinakter009@gmail.com",
    219: "hakimazizul18582@gmail.com",
    220: "mdtamji2003@gmail.com",
    228: "asadurrahmanko@gmail.com",
    232: "azharul151965@gmail.com",
    254: "famanamra1@gmail.com",
    259: "farihazannat03@gmail.com",
    272 : "mdrahatbinsijan@gmail.com",
    276: "tanvir004006@gmail.com",
    299: "saracupric2127@gmail.com",
    300: "nafistahmid0@gmail.com",
    301: "shovon018199@gmail.com"
}


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

def send_email(receiver_email, otp):
    """Sends an OTP email to the user."""
    # Replace with your actual email credentials
    sender_email = "fidazaman99@gmail.com"  # Your email address
    sender_password = "ggwq fnbl lmdj sisj"  # Your email password or app-specific password

    # Use the appropriate SMTP server and port for your email provider
    smtp_server = "smtp.gmail.com"  # Replace with your email provider's SMTP server
    smtp_port = 587  # Use 587 for TLS, 465 for SSL if necessary

       # Create the HTML content
    html_content = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f9;
                margin: 0;
                padding: 0;
            }}
            .container {{
                width: 100%;
                max-width: 600px;
                margin: 0 auto;
                background-color: #ffffff;
                padding: 20px;
                box-shadow: 0 2px 3px rgba(0, 0, 0, 0.1);
            }}
            h1 {{
                color: #4CAF50;
            }}
            p {{
                font-size: 16px;
                color: #333333;
            }}
            .otp {{
                font-size: 24px;
                font-weight: bold;
                color: #FF5722;
                padding: 10px 0;
                background-color: #f9f9f9;
                border-radius: 5px;
                display: inline-block;
            }}
            .footer {{
                margin-top: 20px;
                font-size: 12px;
                color: #999999;
                text-align: center;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <img src="https://i.ibb.co/zxJbj56/6a5f23b9-de12-48ec-9134-192d4a40b97a-removebg-preview.png" width="150px">
            <h1>Verification Code</h1>
            <p>Dear Polapan,</p>
            <p>আমি জানি তোদের একটু প্যারা দিতেসি। বাট কি করার, ইনফর্মেশন গুলা সেন্সিটিভ। এই OTP (One-Time Password) টা ইউস কর ভেরিফিকেশনের জন্য : </p>
            <div class="otp">{otp}</div>
            <p>If you did not request this code, please ignore this email.</p>
            <div class="footer">
                <p>&copy; 2024 Fida Zaman. All rights reserved.</p>
            </div>
        </div>
    </body>
    </html>
    """

    # Create a MIMEText object with HTML content
    msg = MIMEMultipart("alternative")
    msg["Subject"] = "Your OTP Verification Code"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    # Attach the HTML content to the message
    msg.attach(MIMEText(html_content, "html"))

    try:
        # Connect to the SMTP server using TLS
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            print(f"OTP email sent successfully to {receiver_email}")
    except Exception as e:
        print(f"Error sending email: {e}")

def get_email_hint(email):
    """Returns a hint of the email address for security."""
    local, domain = email.split('@')
    # Show the first and last character of the local part, with asterisks in between
    email_hint = f"{local[0]}{local[1]}{'*' * (len(local) - 3)}{local[-1]}@{domain}"
    return email_hint

def is_valid_merit_position(merit_position):
    """Checks if the merit position is a valid integer within the expected range."""
    try:
        position = int(merit_position)
        return 0 <= position <= 301
    except ValueError:
        return False

def generate_otp():
    """Generates a 6-digit OTP."""
    return random.randint(100000, 999999)

def main():
    """Main function to run the Telegram bot."""
    # Replace with your actual bot token (DO NOT SHARE THIS PUBLICLY)
    bot_token = "7298476252:AAHVL2Tlyq3nFyqw-fQCbLgIO1efRnnRq3E"

    offset = None
    awaiting_position = {}
    otp_storage = {}

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
                        user_name = message["chat"]["first_name"]+ " "+ message["chat"]["last_name"]
                        send_message(bot_token, chat_id, f"Hello,{user_name}\nPlease enter your Technology Unit merit position.")
                        awaiting_position[chat_id] = "awaiting_position"
                    elif chat_id in awaiting_position:
                        if awaiting_position[chat_id] == "awaiting_position":
                            merit_position = text

                            if is_valid_merit_position(merit_position):
                                position = int(merit_position)
                                if position in merit_positions:
                                    if position==301:
                                        user_name = message["chat"]["first_name"]+ " "+ message["chat"]["last_name"]
                                        send_message(bot_token, chat_id, f"sorry {user_name}!\nregular student 2 jon komse tai scholership er jonno o ekjon kome gese. tai tor nam bad pore gese list theke.\nmon kharap koris na.")
                                    else:
                                        # Generate OTP and send email
                                        otp = generate_otp()
                                        email = merit_positions[position]
                                        send_email(email, otp)
                                        otp_storage[chat_id] = otp
                                        """Sends a notification about the OTP."""
                                        email_hint = get_email_hint(email)
                                        message_otp = f"An OTP has been sent to your registered email ({email_hint}). Please enter the OTP to verify. if this mail is not available at you please contact me at https://t.me/fidazaman"
                                        send_message(bot_token, chat_id, message_otp)
                                        awaiting_position[chat_id] = "awaiting_otp"
                                else:
                                    send_message(bot_token, chat_id, "Merit position not found.")
                                    del awaiting_position[chat_id]
                            else:
                                send_message(bot_token, chat_id, "Invalid merit position. Please enter a number between 0 and 301.")
                                del awaiting_position[chat_id]
                        elif awaiting_position[chat_id] == "awaiting_otp":
                            entered_otp = text

                            if entered_otp.isdigit() and int(entered_otp) == otp_storage.get(chat_id):
                                send_message(bot_token, chat_id, "OTP verified successfully.")
                                # Send the image
                                position = next((pos for pos, email in merit_positions.items() if email == merit_positions[position]), None)
                                image_url = f"https://raw.githubusercontent.com/FidaZaman/telegram_bot_data/main/images/image02/{position}.png"
                                send_image(bot_token, chat_id, image_url)
                            else:
                                send_message(bot_token, chat_id, "Invalid OTP. Please try again.")

                            # Clear storage after OTP attempt
                            del otp_storage[chat_id]
                            del awaiting_position[chat_id]
                    else:
                        send_message(bot_token, chat_id, "Please start with /check to enter a merit position.")

            offset = update_id + 1

        time.sleep(1)

if __name__ == "__main__":
    main()
