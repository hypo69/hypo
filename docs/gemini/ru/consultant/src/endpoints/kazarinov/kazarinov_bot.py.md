# Анализ кода модуля `kazarinov_bot`

**Качество кода**
**7/10**
- Плюсы
    - Код имеет базовую структуру, понятную логику работы с Telegram ботом.
    - Используется reStructuredText (RST) для docstring.
    - Присутствует логирование ошибок.
- Минусы
    -  Использование `json.load` не заменено на `j_loads` или `j_loads_ns`.
    -  Не хватает комментариев в формате reStructuredText (RST) для всех функций и переменных.
    -  Используются try-except, которые можно заменить на `logger.error`.
    -  Не все импорты отсортированы и соответствуют общепринятому стилю.
    -  Не все docstring достаточно подробные.
    -  Некоторые константы, такие как `\'dev\'` можно вынести в `gs` или сделать переменными окружения.
    -  Не везде есть явное указание типов переменных.

**Рекомендации по улучшению**

1.  Заменить `json.load` на `j_loads` или `j_loads_ns`.
2.  Добавить reStructuredText (RST) комментарии ко всем функциям, методам и переменным.
3.  Использовать `logger.error` для обработки ошибок вместо `try-except`.
4.  Упорядочить импорты и привести их в соответствие с общим стилем.
5.  Уточнить docstring, добавив более подробные описания и типы.
6.  Убрать константу `\'dev\'` и использовать переменные окружения или `gs`.
7.  Добавить явное указание типов для переменных где это возможно.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
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
from typing import List, Optional, Dict, Any
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
from src import gs
from src.endpoints.bots.telegram import TelegramBot
from src.endpoints.kazarinov.bot_handlers import BotHandler
from src.ai.openai import OpenAIModel
from src.ai.gemini import GoogleGenerativeAI
from src.utils.file import recursively_read_text_files, save_text_file
from src.utils.url import is_url
from src.utils.jjson import j_loads, j_loads_ns, j_dumps
from src.logger.logger import logger


class KazarinovTelegramBot(TelegramBot, BotHandler):
    """
    Telegram bot with custom behavior for Kazarinov.

    This class inherits from :class:`TelegramBot` and :class:`BotHandler`
    and provides specific functionality for the Kazarinov project.
    """
    mode: str
    """Operating mode of the bot ('test' or 'production')."""
    token: str
    """Telegram bot token."""
    config: SimpleNamespace = j_loads_ns(gs.path.endpoints / 'kazarinov' / 'kazarinov.json')
    """Configuration loaded from 'kazarinov.json'."""
    model: GoogleGenerativeAI = GoogleGenerativeAI(
        api_key=gs.credentials.gemini.kazarinov,
        generation_config={"response_mime_type": "text/plain"},
    )
    """Model for interacting with users, `GoogleGenerativeAI`."""

    def __init__(self, mode: Optional[str] = None, webdriver_name: Optional[str] = 'firefox'):
        """
        Initialize the KazarinovTelegramBot instance.

        :param mode: Operating mode, 'test' or 'production'. Defaults to 'test'.
        :type mode: Optional[str]
        :param webdriver_name: Webdriver to use with BotHandler. Defaults to 'firefox'.
        :type webdriver_name: Optional[str]
        """
        # Set the mode
        self.mode = mode or self.config.mode
        # Initialize the token based on mode
        self.token = (
            gs.credentials.telegram.hypo69_test_bot
            if self.mode == 'test'
            else gs.credentials.telegram.hypo69_kazarinov_bot
        )
        # Call parent initializers
        TelegramBot.__init__(self, self.token)
        # BotHandler.__init__(self, getattr(self.config, 'webdriver_name', 'firefox')) #FIXME разобраться почему ломаеться
        BotHandler.__init__(self, self.config.webdriver_name if hasattr(self.config, 'webdriver_name') else 'firefox')


    async def handle_message(self, update: Update, context: CallbackContext) -> None:
        """
        Handle incoming text messages and route them based on their content.

        :param update: The incoming update.
        :type update: telegram.Update
        :param context: The context.
        :type context: telegram.ext.CallbackContext
        """
        q = update.message.text
        if q == '?':
            await update.message.reply_photo(gs.path.endpoints / 'kazarinov' / 'assets' / 'user_flowchart.png')
            return
        user_id = update.effective_user.id #TODO не используется
        if is_url(q):
            await self.handle_url(update, context)
            # <- add logic after url scenario ended
            ...
            return  # <-

        if q in ('--next', '-next', '__next', '-n', '-q'):
            return await self.handle_next_command(update)

        answer = self.model.chat(q)
        await update.message.reply_text(answer)


if __name__ == "__main__":
    if gs.host_name == 'Vostro-3888':
        kt = KazarinovTelegramBot(mode='test')
    else:
        kt = KazarinovTelegramBot()

    asyncio.run(kt.application.run_polling())
```