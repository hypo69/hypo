```python
## file hypotez/src/bots/openai_bots/telegram_bot_trainger.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.bots.openai_bots
	:platform: Windows, Unix
	:synopsis:
	Telegram bot for interacting with an OpenAI model.
"""
MODE = 'dev'


"""
	:platform: Windows, Unix
	:synopsis:
	Configuration settings for the bot.
"""


"""
	:platform: Windows, Unix
	:synopsis:
	Module imports and necessary objects.
"""


"""
  :platform: Windows, Unix
"""
"""
  :platform: Windows, Unix
  :platform: Windows, Unix
  :synopsis:  Global configuration for the bot, specifically the mode.
"""
MODE = 'dev'

""" module: src.bots.openai_bots """


""" This script creates a simple Telegram bot using the python-telegram-bot library."""

from pathlib import Path
import tempfile
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

import header
from src import gs
from src.ai.openai.model.training import Model
from src.utils import j_loads, j_loads_ns, j_dumps
from src.logger import logger
import speech_recognition as sr  # Library for speech recognition
import requests  # For downloading files
from pydub import AudioSegment  # Library for audio conversion
from gtts import gTTS  # Library for text-to-speech
from src.utils.convertors.tts import recognizer, text_to_speech
import os

model = Model()

# Replace 'YOUR_TOKEN_HERE' with your actual bot token
TELEGRAM_TOKEN = gs.credentials.telegram.bot_token


async def start(update: Update, context: CallbackContext) -> None:
    """ Handle the /start command."""
    await update.message.reply_text(
        'Hello! I am your simple bot. Type /help to see available commands.'
    )


async def help_command(update: Update, context: CallbackContext) -> None:
    """ Handle the /help command."""
    await update.message.reply_text(
        'Available commands:\n/start - Start the bot\n/help - Show this help message'
    )


async def handle_document(update: Update, context: CallbackContext):
    try:
        file = await update.message.document.get_file()
        tmp_file_path = await file.download_to_drive()

        with open(tmp_file_path, 'r', encoding='utf-8') as f:
            file_content = f.read()

        response = model.send_message(f"Обучение модели на следующем содержимом: {file_content}")
        await update.message.reply_text(response)

        # Clean up the temporary file
        os.remove(tmp_file_path)

    except Exception as e:
        await update.message.reply_text(f"Error processing file: {e}")


async def handle_message(update: Update, context: CallbackContext) -> None:
    """ Handle any text message."""
    try:
        text_received = update.message.text
        response = model.send_message(text_received)
        await update.message.reply_text(response)

    except Exception as e:
        await update.message.reply_text(f"Error processing message: {e}")


async def handle_voice(update: Update, context: CallbackContext) -> None:
    """ Handle voice messages."""
    try:
        voice_file = await update.message.voice.get_file()
        voice_file_path = await voice_file.download_to_drive()
        message = recognizer(audio_path=voice_file_path)
        response = model.send_message(message)
        await update.message.reply_text(response)
        tts_file_path = await text_to_speech(response)
        await update.message.reply_audio(audio=open(tts_file_path, 'rb'))
        os.remove(voice_file_path)
        os.remove(tts_file_path)  # Clean up temporary file

    except Exception as e:
        await update.message.reply_text(f"Error processing voice message: {e}")


def main() -> None:
    """ Start the bot."""
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Register command handlers
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help_command))

    # Register message handlers
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.add_handler(MessageHandler(filters.VOICE, handle_voice))
    application.add_handler(MessageHandler(filters.Document, handle_document))

    # Start the bot
    application.run_polling()


if __name__ == '__main__':
    main()
```

**Improvements and explanations:**

* **Error Handling:** Added `try...except` blocks to `handle_document`, `handle_message`, and `handle_voice`. This is crucial to prevent crashes if there are issues (e.g., file not found, errors during speech recognition). The error messages are now more informative.
* **Temporary File Cleanup:** The code now removes temporary files (`tmp_file_path`, `tts_file_path`, `voice_file_path`) using `os.remove()`. This is essential for preventing disk space issues and keeping the application clean.
* **Encoding:** Added `encoding='utf-8'` to the `open()` function in `handle_document`. This is vital for handling various file encodings correctly.
* **Clearer Responses:**  Replaced placeholders with more meaningful descriptions.
* **More robust file handling:** Using `download_to_drive()` which returns the path to the downloaded file, and removing that file once it's processed, fixes a key issue where files weren't being properly handled.
* **Voice handling:** The voice handling now correctly downloads the audio file, uses `recognizer` to handle it and cleans up the temporary file created.


**How to Use:**

1.  **Install necessary libraries:**
    ```bash
    pip install python-telegram-bot pydub gtts speechrecognition requests
    ```
2.  **Replace `TELEGRAM_TOKEN`:**  Get your Telegram bot token from the Telegram Bot API settings.
3.  **Run the script:**
    ```bash
    python telegram_bot_trainger.py
    ```

This revised code is significantly more robust and reliable, addressing many of the potential issues and improving the user experience. Remember to adjust file paths and function calls as needed to match your specific application setup.