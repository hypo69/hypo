# Анализ кода модуля `bot_handlers`

**Качество кода**
7/10
-  Плюсы
    - Код содержит базовую структуру для обработки команд телеграм-бота.
    - Используются асинхронные операции.
    - Присутствует логирование ошибок.
    - Код соответствует PEP8.
-  Минусы
    -  Отсутствует документация в формате reStructuredText.
    -  Использование `json.load` вместо `j_loads`.
    -  Не везде используется `logger.error` для обработки ошибок.
    -  Присутствует неиспользуемый импорт `header`.

**Рекомендации по улучшению**
1. Добавить reStructuredText документацию для модуля, классов и методов.
2. Заменить `json.load` на `j_loads` или `j_loads_ns` там, где это требуется.
3. Использовать `logger.error` для обработки исключений вместо `try-except`, где это возможно.
4. Удалить неиспользуемый импорт `header`.
5. Добавить обработку ошибок в `fetch_target_urls_onetab` и в других местах, где это необходимо.
6. Улучшить форматирование и добавить больше комментариев в формате RST для сложных блоков.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12
"""
Модуль для обработки событий телеграм-бота `kazarinov_bot`
=========================================================================================

Этот модуль обрабатывает команды, переданные телеграм-боту, такие как работа с ссылками OneTab
и выполнение связанных сценариев.

Пример использования
--------------------

Пример использования класса `BotHandler`:

.. code-block:: python

    handler = BotHandler(webdriver_name='firefox')
    handler.handle_url(update, context)
"""


# import header # Удален неиспользуемый импорт
import random
import asyncio
import requests
from typing import Optional, Any
from bs4 import BeautifulSoup
from src import gs
from src.logger.logger import logger
from src.webdriver.driver import Driver
from src.webdriver.chrome import Chrome
from src.webdriver.firefox import Firefox
from src.webdriver.edge import Edge
from src.ai.gemini import GoogleGenerativeAI
from src.endpoints.kazarinov.scenarios.scenario_pricelist import MexironBuilder
from src.utils.url import is_url
from src.utils.printer import pprint
from telegram import Update
from telegram.ext import CallbackContext


class BotHandler:
    """
    Исполнитель команд, полученных ботом.

    :ivar mexiron: Экземпляр класса MexironBuilder для запуска сценариев.
    """
    mexiron: MexironBuilder

    def __init__(self, webdriver_name: str):
        """
        Инициализация обработчика событий телеграм-бота.

        :param webdriver_name: Название веб-драйвера для запуска ('firefox', 'chrome', 'edge').
        :type webdriver_name: str
        """
        # Инициализация веб-драйвера в режиме kiosk и headless
        firefox = Firefox(options=["--kiosk", "--headless"])

        # Инициализация MexironBuilder с выбранным веб-драйвером
        self.mexiron = MexironBuilder(
            Driver(
                Firefox if webdriver_name.lower() == 'firefox'
                else Chrome if webdriver_name.lower() == 'chrome'
                else Edge
            )
        )

    async def handle_url(self, update: Update, context: CallbackContext) -> Any:
        """
        Обработка URL, присланного пользователем.

        Код проверяет, начинается ли сообщение с URL OneTab.
        Если да, то извлекаются целевые URL и запускается сценарий.

        :param update: Объект обновления из телеграма.
        :type update: Update
        :param context: Контекст выполнения.
        :type context: CallbackContext
        :return: Результат выполнения.
        :rtype: Any
        """
        # Код извлекает текст сообщения
        response = update.message.text
        # Код проверяет, начинается ли сообщение с URL OneTab
        if response.startswith(('https://one-tab.com', 'http://one-tab.com',
                                'https://www.one-tab.com', 'http://www.one-tab.com')):
            # Код получает данные по URL
            price, mexiron_name, urls = self.fetch_target_urls_onetab(response)
            # Код проверяет валидность данных
            if not urls:
                await update.message.reply_text('Некорректные данные.')
                return

            # Код запускает сценарий
            if await self.mexiron.run_scenario(update=update, context=context, urls=urls if isinstance(urls, list) else [urls], price=price, mexiron_name=mexiron_name):
                await update.message.reply_text('Готово!')
                return True
        else:
            await update.message.reply_text('Ошибка. Попробуй ещё раз.')
            return

    async def handle_next_command(self, update: Update) -> None:
        """
        Обработка команды '--next' и её аналогов.

        Код выбирает случайный вопрос, запрашивает ответ у модели и отправляет
        вопрос и ответ пользователю.

        :param update: Объект обновления из телеграма.
        :type update: Update
        """
        try:
            # Код выбирает случайный вопрос из списка
            question = random.choice(self.questions_list)
            # Код запрашивает ответ у модели
            answer = self.model.ask(question)
            # Код отправляет вопрос и ответ пользователю
            await asyncio.gather(
                update.message.reply_text(question),
                update.message.reply_text(answer)
            )
        except Exception as ex:
            # Логирование ошибки с использованием logger.error
            logger.error('Ошибка чтения вопросов: %s', ex)
            await update.message.reply_text('Произошла ошибка при чтении вопросов.')

    def fetch_target_urls_onetab(self, one_tab_url: str) -> tuple[str, str, list[str]] | None:
        """
        Извлечение целевых URL с указанного URL OneTab.

        Выполняется GET-запрос к указанному URL, парсится HTML-контент
        и извлекаются ссылки из тегов 'a' с классом 'tabLink'.

        :param one_tab_url: URL страницы OneTab.
        :type one_tab_url: str
        :return: Кортеж, содержащий цену, имя и список целевых URL, или None в случае ошибки.
        :rtype: tuple[str, str, list[str]] | None
        """
        try:
            # Код выполняет GET-запрос к URL
            response = requests.get(one_tab_url, timeout=10)
            # Код обрабатывает HTTP-ошибки
            response.raise_for_status()
            
            # Код проверяет статус ответа, при статусе не 200 - ошибка
            if response.status_code != 200:
                logger.debug(f"""Ошибка response
                {pprint(response)}""")
                return

            # Код парсит HTML-контент
            soup = BeautifulSoup(response.content, 'html.parser')

            # Извлечение ссылок
            urls = [a['href'] for a in soup.find_all('a', class_='tabLink')]

            # Извлечение данных из div с классом 'tabGroupLabel'
            element = soup.find('div', class_='tabGroupLabel')
            data = element.get_text() if element else None

            # Код проверяет наличие данных
            if not data:
                price = ''
                mexiron_name = gs.now
            else:
                # Разбивка данных на цену и имя
                parts = data.split(maxsplit=1)
                price = parts[0] if parts else ''
                try:
                    price = int(price)
                except ValueError:
                    price = ''
                mexiron_name = parts[1] if len(parts) > 1 else gs.now

            # Код возвращает цену, имя и список URL
            return price, mexiron_name, urls

        except requests.exceptions.RequestException as ex:
            # Логирование ошибки с использованием logger.error
            logger.error('Ошибка при выполнении запроса: %s', ex)
            return
```