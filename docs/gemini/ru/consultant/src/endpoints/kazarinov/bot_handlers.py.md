# Анализ кода модуля bot_handlers

**Качество кода**
8
 -  Плюсы
    - Код хорошо структурирован, использует классы и функции для разделения логики.
    - Присутствует логирование ошибок и отладочная информация.
    - Используются асинхронные операции, что подходит для телеграм-ботов.
    -  Есть базовая документация в виде docstring.
 -  Минусы
    - Не хватает подробных комментариев в формате reStructuredText (RST) для функций и переменных.
    - Используется избыточный `try-except` блок в `handle_next_command`.
    -  Не используется `j_loads` или `j_loads_ns` для загрузки JSON данных.
    - Отсутствуют проверки на типы в некоторых местах.
    -  Не всегда обрабатываются возможные ошибки при парсинге HTML.
    - Не все переменные и функции имеют docstring.

**Рекомендации по улучшению**

1.  **Документация**: Добавить более подробную документацию в формате RST для всех функций, методов и переменных.
2.  **Импорты**: Проверить и добавить отсутствующие импорты, если они необходимы.
3.  **Логирование**: Использовать `logger.error` вместо `try-except` для обработки ошибок там, где это уместно.
4.  **Обработка JSON**: Заменить стандартный `json.load` на `j_loads` или `j_loads_ns` из `src.utils.jjson`, если работа с JSON предполагается.
5.  **Обработка ошибок**: Улучшить обработку ошибок, например, в `fetch_target_urls_onetab` добавить проверки на None.
6.  **Форматирование**: Привести в соответствие имена переменных и функций с другими файлами проекта.
7.  **Типизация**: Добавить аннотации типов там, где это необходимо для повышения читаемости и надежности кода.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12
"""
Модуль обработки событий телеграм-бота
=========================================================================================

Этот модуль содержит класс :class:`BotHandler`, который используется для обработки
сообщений и команд, отправленных телеграм-боту.

Пример использования
--------------------

Пример создания и использования :class:`BotHandler`:

.. code-block:: python

    handler = BotHandler(webdriver_name=\'firefox\')
    await handler.handle_url(update, context)
"""

MODE = 'dev'

import random
import asyncio
import requests
from typing import Optional, Any, List, Tuple
from bs4 import BeautifulSoup
from src import gs
from src.logger.logger import logger
from src.webdriver.driver import Driver
from src.webdriver.chrome import Chrome
from src.webdriver.firefox import Firefox
from src.webdriver.edge import Edge
# from src.ai.gemini import GoogleGenerativeAI  # TODO: добавить в будующем, если нужно
from src.endpoints.kazarinov.scenarios.scenario_pricelist import MexironBuilder
from src.utils.url import is_url # TODO: возможно пригодится в будущем
# from src.utils.printer import pprint # TODO: возможно пригодится в будущем
from telegram import Update
from telegram.ext import CallbackContext


class BotHandler:
    """
    Класс для обработки команд, полученных от телеграм-бота.

    :param webdriver_name: Название веб-драйвера для запуска.
    :type webdriver_name: str
    """
    mexiron: MexironBuilder

    def __init__(self, webdriver_name: str):
        """
        Инициализация обработчика событий телеграм-бота.

        :param webdriver_name: Название веб-драйвера (firefox, chrome, edge).
        :type webdriver_name: str
        """
        # Код инициализирует MexironBuilder с выбранным веб-драйвером.
        self.mexiron = MexironBuilder(
            Driver(
                Firefox if webdriver_name.lower() == 'firefox'
                else Chrome if webdriver_name.lower() == 'chrome'
                else Edge
            )
        )

    async def handle_url(self, update: Update, context: CallbackContext) -> Any:
        """
        Обрабатывает URL, полученный от пользователя.

        Проверяет, является ли сообщение URL-адресом OneTab, извлекает данные и запускает сценарий.

        :param update: Объект обновления из Telegram.
        :type update: telegram.Update
        :param context: Контекст обратного вызова.
        :type context: telegram.ext.CallbackContext
        :return: True в случае успешной обработки, иначе None.
        :rtype: bool or None
        """
        # Код обрабатывает сообщение от пользователя, проверяет, является ли оно ссылкой OneTab
        response = update.message.text
        if response.startswith(('https://one-tab.com', 'http://one-tab.com',
                                'https://www.one-tab.com', 'http://www.one-tab.com')):
            # Код извлекает данные из ссылки OneTab
            price, mexiron_name, urls = self.fetch_target_urls_onetab(response)
            if not urls:
                # Код отправляет сообщение об ошибке, если не удалось извлечь URL
                await update.message.reply_text('Некорректные данные.')
                return

            # Код запускает сценарий Mexiron с полученными данными
            if await self.mexiron.run_scenario(update=update, context=context,
                                            urls=urls if isinstance(urls, list) else [urls],
                                            price=price, mexiron_name=mexiron_name):
                await update.message.reply_text('Готово!')
                return True
        else:
            # Код отправляет сообщение об ошибке, если сообщение не является ссылкой OneTab
            await update.message.reply_text('Ошибка. Попробуй ещё раз.')
            return

    async def handle_next_command(self, update: Update) -> None:
        """
        Обрабатывает команду '--next' и аналогичные.

        Отправляет пользователю случайный вопрос и ответ, полученный от модели.
        В случае ошибки логирует её и отправляет сообщение об ошибке.

        :param update: Объект обновления из Telegram.
        :type update: telegram.Update
        """
        #  Код обрабатывает команду '--next' и её аналоги
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
            # Код логирует ошибку, если возникла проблема при обработке вопроса
            logger.error('Ошибка чтения вопросов: %s', ex)
            await update.message.reply_text('Произошла ошибка при чтении вопросов.')

    def fetch_target_urls_onetab(self, one_tab_url: str) -> Tuple[str, str, List[str]] | None:
        """
        Извлекает целевые URL из URL OneTab.

        Выполняет GET-запрос к указанному URL, парсит HTML-контент и извлекает ссылки из тегов 'a'
        с классом 'tabLink', а также цену и имя из элемента 'div' с классом 'tabGroupLabel'.

        :param one_tab_url: URL страницы OneTab.
        :type one_tab_url: str
        :return: Кортеж, содержащий цену, имя и список URL или None в случае ошибки.
        :rtype: tuple[str, str, list[str]] or None
        """
        # Код извлекает целевые URL с указанного URL OneTab
        try:
            response = requests.get(one_tab_url, timeout=10)
            response.raise_for_status()

            if response.status_code != 200:
                logger.debug(f"""Ошибка response\n
                {response}""")
                return None
            # Код парсит HTML-контент
            soup = BeautifulSoup(response.content, 'html.parser')

            # Код извлекает ссылки
            urls = [a['href'] for a in soup.find_all('a', class_='tabLink')]

            # Код извлекает данные из div с классом 'tabGroupLabel'
            element = soup.find('div', class_='tabGroupLabel')
            data = element.get_text() if element else None

            if not data:
                 # Код устанавливает пустую цену и текущую дату и время, если нет данных
                price = ''
                mexiron_name = gs.now
            else:
                # Код разбивает данные на цену и имя
                parts = data.split(maxsplit=1)
                price = parts[0] if parts[0].isdigit() else ''
                mexiron_name = parts[1] if len(parts) > 1 else gs.now

            return price, mexiron_name, urls

        except requests.exceptions.RequestException as ex:
            # Код логирует ошибку, если возникла проблема при выполнении запроса
            logger.error('Ошибка при выполнении запроса: %s', ex)
            return None