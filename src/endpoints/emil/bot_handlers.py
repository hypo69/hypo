## \file /src/endpoints/emil/bot_handlers.py
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12
"""
.. module:: src.endpoints.emil.bot_handlers 
	:platform: Windows, Unix
	:synopsis: Обработка событий телеграм бота

Обработчик собтий телеграм-бота  `emil_bot`
=========================================================================================

Этот модуль обрабатывает команды, переданные телеграм-боту, такие как работа с ссылками OneTab
и выполнение связанных сценариев.

Пример использования
--------------------

Пример использования класса `BotHandler`:                                                                           а

.. code-block:: python

    handler = BotHandler(webdriver_name='firefox')
    handler.handle_url(update, context)
"""



import header
import random
import asyncio
import requests
from typing import Optional, Any
from bs4 import BeautifulSoup
from telegram import Update
from telegram.ext import CallbackContext

from src import gs
from src.webdriver.driver import Driver
from src.webdriver.chrome import Chrome
from src.webdriver.firefox import Firefox
from src.webdriver.edge import Edge
from src.ai.gemini import GoogleGenerativeAI
from src.suppliers.get_graber_by_supplier import get_graber_by_supplier_url
from src.utils.url import is_url
from src.utils.printer import pprint
from src.logger.logger import logger


class BotHandler:
    """Исполнитель команд, полученных ботом."""


    def __init__(self, webdriver_name: str ):
        """
        Инициализация обработчика событий телеграм-бота.

        Args:
            webdriver_name (Optional[str]): Название веб-драйвера для запуска.
        """
        firefox = Firefox(options=["--kiosk", "--headless"])

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

    async def handle_url(self, update: Update, context: CallbackContext) -> Any:
        """
        Обработка URL, присланного пользователем.

        Args:
            update (Update): Объект обновления из телеграма.
            context (CallbackContext): Контекст выполнения.
        """
        ...
        response = update.message.text
        if response.startswith(('https://one-tab.com', 'http://one-tab.com',
                                'https://www.one-tab.com', 'http://www.one-tab.com')):

            urls = self.fetch_target_urls_onetab(response)

            if not urls:
                await update.message.reply_text('Некорректные данные.')
        
        graber = get_graber_by_supplier_url(response)


    async def handle_next_command(self, update: Update) -> None:
        """
        Обработка команды '--next' и её аналогов.

        Args:
            update (Update): Объект обновления из телеграма.
        """
        try:
            question = random.choice(self.questions_list)
            answer = self.model.ask(question)
            await asyncio.gather(
                update.message.reply_text(question),
                update.message.reply_text(answer)
            )
        except Exception as ex:
            logger.debug('Ошибка чтения вопросов: %s', ex)
            ...
            await update.message.reply_text('Произошла ошибка при чтении вопросов.')

    def fetch_target_urls_onetab(self, one_tab_url: str) -> list[str] | bool:
        """
        Извлечение целевых URL с указанного URL OneTab.

        Выполняется GET-запрос к указанному URL, парсится HTML-контент
        и извлекаются ссылки из тегов 'a' с классом 'tabLink'.

        Args:
            one_tab_url (str): URL страницы OneTab.

        Returns:
            list[str] | bool: Список целевых URL или False при ошибке.
        """
        try:
            response = requests.get(one_tab_url, timeout=10)
            response.raise_for_status()

            if response.status_code != 200:
                logger.debug(f"""Ошибка response
                {pprint(response)}""")
                ...
                return

            soup = BeautifulSoup(response.content, 'html.parser')

            # Извлечение ссылок
            urls = [a['href'] for a in soup.find_all('a', class_='tabLink')]
            return urls

            # # Извлечение данных из div с классом 'tabGroupLabel'
            # element = soup.find('div', class_='tabGroupLabel')
            # data = element.get_text() if element else None

            # if not data:
            #     ...
            #     price = ''
            #     mexiron_name = gs.now
            # else:
            #     # Разбивка данных на цену и имя
            #     parts = data.split(maxsplit=1)
            #     price = int(parts[0]) or ''
            #     mexiron_name = parts[1] if len(parts) > 1 else gs.now
            # return price, mexiron_name, urls

        except requests.exceptions.RequestException as ex:
            logger.error('Ошибка при выполнении запроса: %s', ex)
            ...
            return
