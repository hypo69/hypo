
## \file /src/endpoints/kazarinov/minibot.py
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3

"""
.. module:: src.endpoints.kazarinov.minibot 
	:platform: Windows, Unix
	:synopsis: минибот для обслуживания запросов от казаринова

"""

import telebot
import os
import datetime
import random
from pathlib import Path
import asyncio

import header
from header import __root__
from src import gs
from src.logger import logger
from src.ai.gemini import GoogleGenerativeAI
from src.endpoints.math_challenges.scenarios.scenario import Scenario
from src.utils.url import is_url
from src.utils.printer import pprint as print

##############################################################

ENDPOINT = 'math_challenges'
from src import USE_ENV # <- Определает откуда брать ключи. Если False - то из базы данных с паролями, иначе из .env
MODE:str = 'PRODUCTION' # <- Определяет режим разработчика. Если MODE=='PRODUCTION' будет запущен kazarionaov бот, иначе тестбот
MODE:str = 'DEV'
#############################################################

if USE_ENV:
    from dotenv import load_dotenv
    load_dotenv()
    

class BotHandler:
    """Исполнитель команд, полученных ботом."""

    base_dir: Path = __root__ / 'src' / 'endpoints' / 'math_challenges'
    scenario: Scenario

    def __init__(self, api_key:str):
        """Инициализация обработчика событий телеграм-бота."""
        ...
        self.scenario = Scenario(api_key, 'math_challenges')

    def handle_message(self, bot:telebot, message:'message'):
        """Обработка текстовых сообщений."""
        text = message.text
        if text == '?':
            self._send_user_flowchart(bot, message.chat.id)
        else:
            try:
                answer = self.scenario.ask_question(text)
                bot.send_message(message.chat.id, answer)
            except Exception as ex:
                logger.error(f"Error during model interaction: {ex}")
                bot.send_message(message.chat.id, "Произошла ошибка при обработке сообщения.")



    def help_command(self, bot, message):
        """Обработка команды /help."""
        bot.send_message(
            message.chat.id,
            'Available commands:\n'
            '/start - Start the bot\n'
            '/help - Show this help message\n'
            '/sendpdf - Send a PDF file'
        )


    def handle_voice(self, bot, message):
        """Обработка голосовых сообщений."""
        try:
            file_info = bot.get_file(message.voice.file_id)
            file = bot.download_file(file_info.file_path)
            file_path = gs.path.temp / f'{message.voice.file_id}.ogg'
            with open(file_path, 'wb') as f:
                f.write(file)
            transcribed_text = self._transcribe_voice(file_path)
            bot.send_message(message.chat.id, f'Распознанный текст: {transcribed_text}')
        except Exception as ex:
            logger.error(f'Ошибка при обработке голосового сообщения: {ex}')
            bot.send_message(message.chat.id, 'Произошла ошибка при обработке голосового сообщения. Попробуй ещё раз.')


    def _transcribe_voice(self, file_path):
        """Транскрибирование голосового сообщения (заглушка)."""
        return 'Распознавание голоса ещё не реализовано.'


    def handle_document(self, bot, message):
        """Обработка полученных документов."""
        try:
            file_info = bot.get_file(message.document.file_id)
            file = bot.download_file(file_info.file_path)
            tmp_file_path = gs.path.temp / message.document.file_name
            with open(tmp_file_path, 'wb') as f:
                f.write(file)
            bot.send_message(message.chat.id, f'Файл сохранен в {tmp_file_path}')
            return True
        except Exception as ex:
            logger.error(f'Ошибка при обработке документа: {ex}')
            bot.send_message(message.chat.id, 'Произошла ошибка при обработке документа. Попробуй ещё раз.')
            return False

# --- config.py -----------------

class Config:
    GEMINI_API:str = os.getenv('GEMINI_API') if USE_ENV else gs.credentials.gemini.teacher
    if MODE=='PRODUCTION':
        BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN') if USE_ENV else gs.credentials.telegram.hypo69_kazarinov_bot
    else:
        BOT_TOKEN = os.getenv('TEST_BOT_TOKEN') if USE_ENV else gs.credentials.telegram.hypo69_test_bot

    CHANNEL_ID = '@onela'
    PHOTO_DIR = Path(__root__ / 'endpoints' / 'kazarinov' / 'assets')
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
handler = BotHandler(api_key = config.GEMINI_API)
bot = telebot.TeleBot(config.BOT_TOKEN)

@bot.message_handler(commands=['start'])
def command_start(message):
    logger.info(f"User {message.from_user.username} send /start command")
    bot.send_message(message.chat.id, config.START_MESSAGE)

@bot.message_handler(commands=['help'])
def command_help(message):
    logger.info(f"User {message.from_user.username} send /help command")
    handler.help_command(bot, message)

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

@bot.message_handler(content_types=['voice'])
def handle_voice_message(message):
    logger.info(f"User {message.from_user.username} send voice message")
    handler.handle_voice(bot, message)

@bot.message_handler(content_types=['document'])
def handle_document_message(message):
    logger.info(f"User {message.from_user.username} send document message")
    handler.handle_document(bot, message)

@bot.message_handler(func=lambda message: message.text and not message.text.startswith('/'))
def handle_text_message(message):
    logger.info(f"User {message.from_user.username} sent message: {message.text}")
    handler.handle_message(bot, message )

@bot.message_handler(func=lambda message: message.text and message.text.startswith('/'))
def handle_unknown_command(message):
    logger.info(f"User {message.from_user.username} send unknown command: {message.text}")
    bot.send_message(message.chat.id, config.UNKNOWN_COMMAND_MESSAGE)

def main():

    try:
        bot.polling(none_stop=True)
        
    except Exception as ex:
        logger.error(f"Error during bot polling: ", ex)
        ...
        main()

if __name__ == '__main__':
    main()
   