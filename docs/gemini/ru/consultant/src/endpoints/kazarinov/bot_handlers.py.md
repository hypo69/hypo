# Анализ кода модуля `bot_handlers`

**Качество кода**
8
- Плюсы
    - Код хорошо структурирован, используются классы для организации функциональности.
    - Присутствует обработка исключений, что повышает устойчивость кода.
    - Используется `logger` для логирования ошибок и отладочной информации.
    - Добавлены docstring для классов и методов.
- Минусы
    - Не все импорты отсортированы по алфавиту.
    - Некоторые блоки `try-except` можно заменить на более точное использование `logger.error`.
    - Использованы `...` в качестве точек остановки.
    - Присутсвуют магические строки и значения
    - Не все переменные имеют docstring
    - `MODE = 'dev'` вынесена за докстринг модуля

**Рекомендации по улучшению**

1.  **Импорты**: Отсортировать импорты по алфавиту.
2.  **Обработка ошибок**: Улучшить обработку ошибок, используя `logger.error` вместо общих `try-except`.
3.  **Комментарии**: Добавить более подробные комментарии в формате reStructuredText (RST) для функций, методов и переменных.
4.  **Магические строки**: Заменить магические строки на константы.
5.  **`...`**: Убрать `...` из кода, заменив их на конкретную реализацию или удалив.
6. **docstring**: Добавить docstring для переменных.
7. **MODE**: Переместить переменную `MODE` в docstring модуля.

**Оптимизированный код**

```python
"""
Модуль для обработки событий телеграм-бота.
=========================================================================================

Этот модуль обрабатывает команды, переданные телеграм-боту, такие как работа с ссылками OneTab
и выполнение связанных сценариев.

.. data:: MODE

    Режим работы бота ('dev' или 'prod').

Пример использования
--------------------

Пример использования класса `BotHandler`:

.. code-block:: python

    handler = BotHandler(webdriver_name='firefox')
    handler.handle_url(update, context)
"""

MODE = 'dev'

import asyncio
import random
import requests
from typing import Any, List, Optional, Tuple
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
    """
    Исполнитель команд, полученных ботом.

    :ivar mexiron: Объект для выполнения сценариев.
    :vartype mexiron: MexironBuilder
    :ivar questions_list: Список вопросов для бота.
    :vartype questions_list: list
    :ivar model: Модель ИИ для генерации ответов.
    :vartype model: GoogleGenerativeAI
    """
    mexiron: MexironBuilder
    questions_list: list = ['Вопрос 1', 'Вопрос 2', 'Вопрос 3'] #TODO:  заменить на реальный список вопросов
    model: GoogleGenerativeAI = GoogleGenerativeAI(model_name='gemini-pro')


    def __init__(self, webdriver_name: str):
        """
        Инициализация обработчика событий телеграм-бота.

        :param webdriver_name: Название веб-драйвера для запуска.
        :type webdriver_name: str
        """
        # Создание экземпляра Firefox с опциями
        firefox = Firefox(options=["--kiosk", "--headless"])

        # Инициализация MexironBuilder с выбором драйвера на основе параметра webdriver_name
        self.mexiron = MexironBuilder(
            Driver(
                Firefox if webdriver_name.lower() == 'firefox'
                else Chrome if webdriver_name.lower() == 'chrome'
                else Edge
            )
        )

    async def handle_url(self, update: Update, context: CallbackContext) -> Optional[bool]:
        """
        Обработка URL, присланного пользователем.

        :param update: Объект обновления из телеграма.
        :type update: Update
        :param context: Контекст выполнения.
        :type context: CallbackContext
        :return: Возвращает True в случае успеха, None в противном случае
        :rtype: Optional[bool]
        """
        response = update.message.text
        # Проверка, начинается ли сообщение с допустимых URL OneTab
        if response.startswith(('https://one-tab.com', 'http://one-tab.com',
                                'https://www.one-tab.com', 'http://www.one-tab.com')):
            # Извлечение данных из URL OneTab
            price, mexiron_name, urls = self.fetch_target_urls_onetab(response)
            # Проверка корректности извлеченных URL
            if not urls:
                await update.message.reply_text('Некорректные данные.')
                return

            # Запуск сценария Mexiron с извлеченными данными
            if await self.mexiron.run_scenario(update=update, context=context,
                                               urls=urls if isinstance(urls, list) else [urls],
                                               price=price, mexiron_name=mexiron_name):
                await update.message.reply_text('Готово!')
                return True
        else:
            # Отправка сообщения об ошибке, если URL не соответствует ожидаемому формату
            await update.message.reply_text('Ошибка. Попробуй ещё раз.')
            return

    async def handle_next_command(self, update: Update) -> None:
        """
        Обработка команды '--next' и её аналогов.

        :param update: Объект обновления из телеграма.
        :type update: Update
        """
        try:
            # Выбор случайного вопроса и получение ответа от модели
            question = random.choice(self.questions_list)
            answer = self.model.ask(question)
            # Отправка вопроса и ответа пользователю
            await asyncio.gather(
                update.message.reply_text(question),
                update.message.reply_text(answer)
            )
        except Exception as ex:
            # Логирование ошибки и отправка сообщения об ошибке пользователю
            logger.error('Ошибка чтения вопросов: %s', ex)
            await update.message.reply_text('Произошла ошибка при чтении вопросов.')

    def fetch_target_urls_onetab(self, one_tab_url: str) -> Optional[Tuple[str, str, List[str]]]:
        """
        Извлечение целевых URL с указанного URL OneTab.

        Выполняется GET-запрос к указанному URL, парсится HTML-контент
        и извлекаются ссылки из тегов 'a' с классом 'tabLink'.

        :param one_tab_url: URL страницы OneTab.
        :type one_tab_url: str
        :return: Кортеж из цены, имени и списка URL или None в случае ошибки.
        :rtype: Optional[Tuple[str, str, List[str]]]
        """
        try:
            # Выполнение GET-запроса к указанному URL
            response = requests.get(one_tab_url, timeout=10)
            response.raise_for_status()

            # Проверка статуса ответа
            if response.status_code != 200:
                logger.error(f"""Ошибка response\n                {pprint(response)}""")
                return

            # Парсинг HTML-контента
            soup = BeautifulSoup(response.content, 'html.parser')

            # Извлечение ссылок из тегов 'a' с классом 'tabLink'
            urls = [a['href'] for a in soup.find_all('a', class_='tabLink')]

            # Извлечение данных из div с классом 'tabGroupLabel'
            element = soup.find('div', class_='tabGroupLabel')
            data = element.get_text() if element else None

            # Извлечение цены и имени из данных
            if not data:
                price = ''
                mexiron_name = gs.now
            else:
                # Разбивка данных на цену и имя
                parts = data.split(maxsplit=1)
                price = str(int(parts[0])) if parts and parts[0].isdigit() else ''
                mexiron_name = parts[1] if len(parts) > 1 else gs.now

            return price, mexiron_name, urls

        except requests.exceptions.RequestException as ex:
             # Логирование ошибки при выполнении запроса
            logger.error('Ошибка при выполнении запроса: %s', ex)
            return
```