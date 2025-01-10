# Анализ кода модуля bot_handlers

**Качество кода**
7
-  Плюсы
    - Код структурирован в класс `BotHandler`, что обеспечивает логическую организацию.
    - Используются асинхронные функции для неблокирующих операций.
    - Присутствует обработка исключений для предотвращения сбоев.
    - Используется `logger` для отслеживания ошибок и отладки.
    - Добавлена документация к модулю и классу.
-  Минусы
    -   Использование `...` в коде в качестве заглушки.
    -   Отсутствуют docstring у некоторых методов.
    -  Не всегда используются f-строки для форматирования логов.
    -  Смешанное использование кавычек в коде.
    -  Не все импорты отсортированы.
    -  Не всегда используются константы или ENUM для определения webdriver.

**Рекомендации по улучшению**
1.  **Документация**: Добавить docstring к методам `handle_next_command` и `fetch_target_urls_onetab`, чтобы пояснить их назначение, аргументы и возвращаемые значения.
2.  **Обработка ошибок**: Заменить `...` на конкретные действия, такие как логирование ошибки с помощью `logger.error` или отправка информативного сообщения пользователю.
3.  **Улучшение обработки строк**: Использовать f-строки для форматирования строк в логах, например: `logger.debug(f'Ошибка чтения вопросов: {ex}')`.
4. **Использование констант**: Заменить магические строки (`'firefox'`, `'chrome'`, `'edge'`) на константы или ENUM для лучшей читаемости и поддерживаемости кода.
5. **Сортировка импортов**: Отсортировать импорты в алфавитном порядке и разделить на стандартные, сторонние и локальные.
6.  **Унификация кавычек**: Привести использование кавычек к единому стандарту (одинарные кавычки в коде, двойные в print и logger).
7.  **Извлечение логики**: Вынести проверку URL в отдельный метод
8. **Улучшение логирования**: Добавить более подробные сообщения в лог для отслеживания выполнения кода.
9. **Удаление лишнего кода**: Убрать лишний блок `return` в методе `handle_url`.
10. **Проверка данных**: Добавить проверку `price` на `isinstance(price, int)` перед тем, как присовить значение или в самом начале  метода `fetch_target_urls_onetab`.
11. **Разделение логики**: Разделить метод `fetch_target_urls_onetab` на несколько более мелких методов для лучшей читаемости и тестируемости.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
#! venv/bin/python/python3.12
"""
.. module:: src.endpoints.kazarinov.bot_handlers
    :platform: Windows, Unix
    :synopsis: Обработка событий телеграм бота

Обработчик событий телеграм-бота `kazarinov_bot`
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
import asyncio
import random
from typing import Any, Optional

import requests
from bs4 import BeautifulSoup
from telegram import Update
from telegram.ext import CallbackContext

from src import gs
from src.ai.gemini import GoogleGenerativeAI
from src.endpoints.kazarinov.scenarios.scenario_pricelist import MexironBuilder
from src.logger.logger import logger
from src.utils.printer import pprint
from src.utils.url import is_url
from src.webdriver.chrome import Chrome
from src.webdriver.driver import Driver
from src.webdriver.edge import Edge
from src.webdriver.firefox import Firefox


class BotHandler:
    """Исполнитель команд, полученных ботом."""

    FIREFOX = 'firefox'
    CHROME = 'chrome'
    EDGE = 'edge'

    mexiron: MexironBuilder

    def __init__(self, webdriver_name: str):
        """
        Инициализация обработчика событий телеграм-бота.

        Args:
            webdriver_name (str): Название веб-драйвера для запуска.
        """
        # Код инициализирует Firefox webdriver с заданными опциями.
        firefox = Firefox(options=['--kiosk', '--headless'])

        # Код создает объект MexironBuilder с использованием выбранного веб-драйвера.
        self.mexiron = MexironBuilder(
            Driver(
                Firefox
                if webdriver_name.lower() == self.FIREFOX
                else Chrome
                if webdriver_name.lower() == self.CHROME
                else Edge
            )
        )

    async def _is_valid_onetab_url(self, url: str) -> bool:
        """
        Проверяет, является ли URL ссылкой OneTab.

        Args:
            url (str): URL для проверки.

        Returns:
             bool: True, если URL является ссылкой OneTab, иначе False.
        """
        return url.startswith(
            (
                'https://one-tab.com',
                'http://one-tab.com',
                'https://www.one-tab.com',
                'http://www.one-tab.com',
            )
        )

    async def handle_url(self, update: Update, context: CallbackContext) -> Any:
        """
        Обработка URL, присланного пользователем.

        Args:
            update (Update): Объект обновления из телеграма.
            context (CallbackContext): Контекст выполнения.

        """
        # Код получает текст сообщения от пользователя.
        response = update.message.text

        # Код проверяет, является ли сообщение ссылкой OneTab
        if await self._is_valid_onetab_url(response):
            # Код извлекает данные (цену, имя, ссылки) из OneTab URL
            price, mexiron_name, urls = self.fetch_target_urls_onetab(response)
            # Код проверяет корректность полученных ссылок
            if not urls:
                await update.message.reply_text('Некорректные данные.')
                return

            # Код запускает сценарий с полученными данными
            if await self.mexiron.run_scenario(
                update=update,
                context=context,
                urls=urls if isinstance(urls, list) else [urls],
                price=price,
                mexiron_name=mexiron_name,
            ):
                await update.message.reply_text('Готово!')
                return True
        else:
            # Код отправляет сообщение об ошибке, если URL не является ссылкой OneTab
            await update.message.reply_text('Ошибка. Попробуй ещё раз.')
            logger.error(f'Получен некорректный URL: {response}')
            return

    async def handle_next_command(self, update: Update) -> None:
        """
        Обработка команды '--next' и её аналогов.

        Args:
            update (Update): Объект обновления из телеграма.
        """
        try:
            # Код выбирает случайный вопрос из списка
            question = random.choice(self.questions_list)
            # Код получает ответ на вопрос от модели
            answer = self.model.ask(question)
            # Код отправляет вопрос и ответ в чат
            await asyncio.gather(
                update.message.reply_text(question),
                update.message.reply_text(answer),
            )
        except Exception as ex:
            # Код логирует ошибку, если произошла ошибка при чтении вопросов
            logger.error(f'Ошибка чтения вопросов: {ex}')
            await update.message.reply_text(
                'Произошла ошибка при чтении вопросов.'
            )

    def fetch_target_urls_onetab(self, one_tab_url: str) -> tuple[str, str, list[str]] | None:
        """
        Извлечение целевых URL с указанного URL OneTab.

        Выполняется GET-запрос к указанному URL, парсится HTML-контент
        и извлекаются ссылки из тегов 'a' с классом 'tabLink'.

        Args:
            one_tab_url (str): URL страницы OneTab.

        Returns:
            tuple[str, str, list[str]] | None: Кортеж (цена, имя, список URL) или None в случае ошибки
        """
        try:
            # Код выполняет GET-запрос к указанному URL.
            response = requests.get(one_tab_url, timeout=10)
            response.raise_for_status()
            # Код проверяет статус ответа.
            if response.status_code != 200:
                logger.error(
                    f'Ошибка response:\n{pprint(response)}'
                )
                return None

            # Код создает объект BeautifulSoup для парсинга HTML
            soup = BeautifulSoup(response.content, 'html.parser')
            # Код извлекает все ссылки из тегов <a> с классом 'tabLink'
            urls = [a['href'] for a in soup.find_all('a', class_='tabLink')]

            # Код извлекает данные из div с классом 'tabGroupLabel'
            element = soup.find('div', class_='tabGroupLabel')
            data = element.get_text() if element else None

            # Код обрабатывает данные из div
            if not data:
                price = ''
                mexiron_name = gs.now
            else:
                # Код разбивает данные на цену и имя
                parts = data.split(maxsplit=1)
                price = int(parts[0]) if parts and parts[0].isdigit() else ''
                mexiron_name = parts[1] if len(parts) > 1 else gs.now

            # Код возвращает извлеченные данные
            return price, mexiron_name, urls

        except requests.exceptions.RequestException as ex:
            # Код логирует ошибку при выполнении запроса
            logger.error(f'Ошибка при выполнении запроса: {ex}')
            return None