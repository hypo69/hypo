import telebot
import os
import datetime
import random
from pathlib import Path

from dotenv import load_dotenv
load_dotenv()

import header
from header import __root__
base_dir:Path = __root__ / 'endpoints' / 'kazarinov'

from src import gs
from src.endpoints.kazarinov.kazarinov_bot_handlers_telebot import BotHandler()
from src.logger import logger

# --- config.py -----------------
class Config:
    BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    CHANNEL_ID = '@onela'
    PHOTO_DIR = base_dir / 'assets' # создайте папку photos и добавьте туда фотографии
    COMMAND_INFO = 'This is a simple bot. Use /help to see commands.'
    UNKNOWN_COMMAND_MESSAGE = 'Unknown command. Use /help to see available commands.'
    START_MESSAGE = "Howdy, how are you doing?"
    HELP_MESSAGE = """
    Here are the available commands:
    /start - Starts the bot.
    /help - Shows this help message.
    /info - Shows information about the bot.
    /time - Shows the current time.
    /photo - Sends a random photo.
    """
# --- config.py end -----------------

# --- bot.py ---
config = Config()
handler = BotHandler()
bot = telebot.TeleBot(config.BOT_TOKEN)
#chat = bot.get_chat(config.CHANNEL_ID)



@bot.message_handler(commands=['start'])
def command_start(message):
    logger.info(f"User {message.from_user.username} send /start command")
    bot.send_message(message.chat.id, config.START_MESSAGE)


@bot.message_handler(commands=['help'])
def command_help(message):
    logger.info(f"User {message.from_user.username} send /help command")
    bot.send_message(message.chat.id, config.HELP_MESSAGE)

@bot.message_handler(commands=['info'])
def command_info(message):
    logger.info(f"User {message.from_user.username} send /info command")
    bot.send_message(message.chat.id, config.COMMAND_INFO)

@bot.message_handler(commands=['time'])
def command_time(message):
    logger.info(f"User {message.from_user.username} send /time command")
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    bot.send_message(message.chat.id, f"Current time: {current_time}")


@bot.message_handler(commands=['photo'])
def command_photo(message):
    logger.info(f"User {message.from_user.username} send /photo command")
    try:
        photo_files = os.listdir(config.PHOTO_DIR)
        if photo_files:
            random_photo = random.choice(photo_files)
            photo_path = os.path.join(config.PHOTO_DIR, random_photo)
            with open(photo_path, 'rb') as photo:
                bot.send_photo(message.chat.id, photo)
        else:
             bot.send_message(message.chat.id, "No photos in the folder.")
    except FileNotFoundError:
        bot.send_message(message.chat.id, "Photo directory not found.")


@bot.message_handler(func=lambda message: message.text and not message.text.startswith('/'))
def handle_text_message(message):
    logger.info(f"User {message.from_user.username} sent message: {message.text}")
    handler.handle_message(bot,message)


@bot.message_handler(func=lambda message: message.text and message.text.startswith('/'))
def handle_unknown_command(message):
     logger.info(f"User {message.from_user.username} send unknown command: {message.text}")
     bot.send_message(message.chat.id, config.UNKNOWN_COMMAND_MESSAGE)

bot.polling(none_stop=True)
# --- bot.py end ---