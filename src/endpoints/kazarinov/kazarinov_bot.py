
## \file /src/endpoints/kazarinov/kazarinov_bot.py
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12
"""
Telegram-бот для проекта Kazarinov
====================================================
Бот взаимодействует 
с парсером Mexiron и моделью Google Generative AI, поддерживает обработку текстовых сообщений, документов и URL.

.. module:: src.endpoints.kazarinov.kazarinov_bot 
	:platform: Windows, Unix
	:synopsis: KazarinovTelegramBot

"""
import asyncio
from pathlib import Path
from typing import List, Optional, Dict, Self
from types import SimpleNamespace
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

import header
"""
.. header.py:
    ```mermaid
    flowchart TD
        Start --> Header[<code>header.py</code><br> Determine Project Root]
    
        Header --> import[Import Global Settings: <br><code>from src import gs</code>] 
```
"""    
import header
from src import gs
from src.endpoints.bots.telegram import TelegramWebHooksBot, TelegamLongPoolingBot

from src.endpoints.kazarinov.bot_handlers import BotHandler
from src.ai.openai import OpenAIModel
from src.ai.gemini import GoogleGenerativeAI
from src.utils.file import recursively_read_text_files, save_text_file
from src.utils.url import is_url
from src.utils.jjson import j_loads, j_loads_ns, j_dumps
from src.logger.logger import logger

import argparse


class KazarinovTelegramBot(TelegramWebHooksBot, BotHandler):
    """Telegram bot with custom behavior for Kazarinov."""

    token: str
    config = j_loads_ns(gs.path.endpoints / 'kazarinov' / 'kazarinov.json')
    model:GoogleGenerativeAI = GoogleGenerativeAI(api_key = gs.credentials.gemini.kazarinov, generation_config = {"response_mime_type": "text/plain"})
    """Эта модель используется для диалога с пользователем. Для обработки сценариев используется модель, определяемая в классе `BotHandler`"""

    def __init__(self, mode: Optional[str] = None, webdriver_name: Optional[str] = 'firefox'):
        """
        Initialize the KazarinovTelegramBot instance.

        Args:
            mode (Optional[str]): Operating mode, 'test' or 'production'. Defaults to 'test'.
            webdriver_name (Optional[str]): Webdriver to use with BotHandler. Defaults to 'firefox'.
        """
        # Set the mode
        mode = mode or self.config.mode
        # Initialize the token based on mode
        self.token = (
            gs.credentials.telegram.hypo69_test_bot
            if mode == 'test'
            else gs.credentials.telegram.hypo69_kazarinov_bot
        )
        
        # Call parent initializers
        TelegramWebHooksBot.__init__(self, 
                                     token = self.token, 
                                     port = self.config.telegram.port)
        #self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_log))
        BotHandler.__init__(self, getattr(self.config , 'webdriver_name' ,'firefox') )


    async def handle_message(self, update: Update, context: CallbackContext) -> None:
        """Handle text messages with URL-based routing."""
        q = update.message.text
        if q == '?':
            await update.message.reply_photo(gs.path.endpoints / 'kazarinov' / 'assets' / 'user_flowchart.png' )
            return
        user_id = update.effective_user.id
        if is_url(q):
            await self.handle_url(update, context)
            # <- add logic after url scenario ended
            ...
            return # <- 


        if q in ('--next', '-next', '__next', '-n', '-q'):
            return await self.handle_next_command(update)

        answer = self.model.chat(q)
        await update.message.reply_text(answer)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Kazarinov Telegram Bot with specified mode.")
    parser.add_argument('-m', '--mode', type=str, default='prod', help="Operating mode: 'test' or 'production'")
    args = parser.parse_args()

    mode = args.mode

    if gs.host_name == 'Vostro-3888':
        mode = 'prod'
        #mode = 'test' # <- comment to prod

    kt = KazarinovTelegramBot(mode)
    asyncio.run(kt.application.run_polling())
