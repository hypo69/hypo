import pywhatkit
import pyautogui
from pynput.keyboard import Key, Controller
import emoji
import random
import time

def send_whatsapp_message(phone_number, message, hour, minutes):
    """Sends a WhatsApp message using pywhatkit and pyautogui."""
    try:
        pywhatkit.sendwhatmsg(phone_number, message, hour, minutes, wait_time=25, tab_close=True)
        time.sleep(20)  # Give time for WhatsApp Web to load
        keyboard = Controller()
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        print("Message sent successfully!")
    except Exception as e:
        print(f"Error sending message: {e}")


# Message bank with emojis
messages = [
    "Hello! How are you? :slightly_smiling_face:",
    "Thinking of you! :heart:",
    "Just wanted to say hi! :waving_hand:",
    "I love you :heart_exclamation:",
    emoji.emojize("Have a wonderful day! :sun:")
]

# Get user inputs
phone_number = input("Enter the phone number with country code: ")
num_messages = int(input("Enter the number of messages to send: "))
start_hour = int(input("Enter the start hour (0-23): "))
end_hour = int(input("Enter the end hour (0-23): "))

message_count = 0
while message_count < num_messages:
    random_hour = random.randint(start_hour, end_hour)
    random_minutes = random.randint(0, 59)
    random_message = random.choice(messages)

    send_whatsapp_message(phone_number, random_message, random_hour, random_minutes)
    message_count += 1