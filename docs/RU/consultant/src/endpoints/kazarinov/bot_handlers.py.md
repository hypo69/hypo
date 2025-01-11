# Анализ кода модуля `bot_handlers`

**Качество кода**
8
 -  Плюсы
    - Код имеет чёткую структуру и разбит на логические блоки, что облегчает его понимание и поддержку.
    - Используется асинхронность для неблокирующих операций, что способствует лучшей производительности.
    - Присутствует базовая обработка ошибок с использованием `try-except` и логирование.
    - Код соответствует PEP 8 по наименованию переменных и функций.
    - Имеется описание модуля и документация для класса `BotHandler` и его методов в формате docstring.

 -  Минусы
    -  Некоторые блоки кода используют многоточие (`...`) в качестве заглушки, что может затруднить понимание и отладку.
    -  Не везде используются константы для магических строк и чисел (например, типы вебдрайверов).
    -  Логирование ошибок не всегда информативно, не хватает контекста для некоторых ошибок.
    -  В некоторых местах, таких как обработка `price`, используется `or ''` что может привести к неожиданным результатам.
    -  Импорт `header` и `random` не используется, их следует удалить.
    -  В обработчике ошибок, не всегда возвращается значение, это может привести к проблемам в работе программы.

**Рекомендации по улучшению**

1.  **Импорты**:
    -   Удалить неиспользуемые импорты `header` и `random`.

2.  **Комментарии и документация**:
    -   Добавить комментарии к блокам кода, где не очевидно их назначение.
    -   Добавить более подробные docstring к функциям и методам.

3.  **Обработка ошибок**:
    -   Вместо `...` использовать более информативные обработки исключений и логирование с контекстом ошибки.
    -   В блоках `try-except` всегда возвращать какое-либо значение, чтобы обработка ошибок была корректной.

4.  **Использование констант**:
    -   Определить константы для типов вебдрайверов (`'firefox'`, `'chrome'`, `'edge'`) для улучшения читаемости и поддержки.

5.  **Обработка данных**:
    -   Проверить и исправить логику обработки `price` и `mexiron_name`, чтобы избежать некорректного присвоения пустых значений.
    -   Добавить проверки на тип данных, где это необходимо, чтобы избежать неожиданных ошибок.

6.  **Логирование**:
    -   Добавить больше контекста в логи для облегчения отладки (например, имя функции, значения переменных).
    -   Использовать `logger.error` вместо `logger.debug` для ошибок, которые должны быть обязательно замечены.

7.  **Рефакторинг**:
    -   Разбить функцию `fetch_target_urls_onetab` на более мелкие функции для повышения читаемости и переиспользования кода.
    -   Упростить логику выбора вебдрайвера, вынеся её в отдельную функцию или используя словарь соответствий.

**Оптимизированный код**

```python
"""
.. module:: src.endpoints.kazarinov.bot_handlers
    :platform: Windows, Unix
    :synopsis: Обработка событий телеграм бота

Обработчик событий телеграм-бота  `kazarinov_bot`
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
import requests
from typing import Optional, Any, List, Tuple
from bs4 import BeautifulSoup
from src import gs
from src.logger.logger import logger
from src.webdriver.driver import Driver
from src.webdriver.chrome import Chrome
from src.webdriver.firefox import Firefox
from src.webdriver.edge import Edge
from src.endpoints.kazarinov.scenarios.scenario_pricelist import MexironBuilder
from src.utils.url import is_url
from src.utils.printer import pprint
from telegram import Update
from telegram.ext import CallbackContext


WEBDRIVER_MAPPING = {
    'firefox': Firefox,
    'chrome': Chrome,
    'edge': Edge
}
"""Словарь для сопоставления имен вебдрайверов с их классами."""


class BotHandler:
    """Исполнитель команд, полученных ботом."""

    mexiron: MexironBuilder

    def __init__(self, webdriver_name: str):
        """
        Инициализация обработчика событий телеграм-бота.

        Args:
            webdriver_name (str): Название веб-драйвера для запуска.
        """
        #  Инициализирует объект MexironBuilder с выбранным веб-драйвером.
        webdriver_class = WEBDRIVER_MAPPING.get(webdriver_name.lower(), Firefox)
        driver = Driver(webdriver_class(options=["--kiosk", "--headless"]))
        self.mexiron = MexironBuilder(driver)

    async def handle_url(self, update: Update, context: CallbackContext) -> Optional[bool]:
        """
        Обработка URL, присланного пользователем.

        Args:
            update (Update): Объект обновления из телеграма.
            context (CallbackContext): Контекст выполнения.

        Returns:
             Optional[bool]: True если обработка прошла успешно, иначе None
        """
        #  Извлекает текст сообщения от пользователя
        response = update.message.text
        #  Проверяет, начинается ли сообщение с URL OneTab
        if response.startswith(('https://one-tab.com', 'http://one-tab.com',
                                'https://www.one-tab.com', 'http://www.one-tab.com')):
            #  Извлекает данные (цену, имя, URL-ы) из OneTab
            price, mexiron_name, urls = self.fetch_target_urls_onetab(response)

            #  Проверяет, что URL-ы извлечены
            if not urls:
                await update.message.reply_text('Некорректные данные.')
                return

            #  Запускает сценарий Mexiron с полученными данными
            if await self.mexiron.run_scenario(update=update, context=context, urls=urls if isinstance(urls, list) else [urls], price=price, mexiron_name=mexiron_name):
                await update.message.reply_text('Готово!')
                return True
        else:
            await update.message.reply_text('Ошибка. Попробуй ещё раз.')
            return

    async def handle_next_command(self, update: Update) -> None:
        """
        Обработка команды '--next' и её аналогов.

        Args:
            update (Update): Объект обновления из телеграма.
        """
        try:
            #  Выбирает случайный вопрос из списка и задаёт его пользователю
            question = random.choice(self.questions_list)
            #  Получает ответ на вопрос от модели ИИ
            answer = self.model.ask(question)
            #  Отправляет вопрос и ответ пользователю
            await asyncio.gather(
                update.message.reply_text(question),
                update.message.reply_text(answer)
            )
        except Exception as ex:
            #  Логирует ошибку, если не удалось прочитать вопросы
            logger.error('Ошибка чтения вопросов: %s', ex, exc_info=True)
            await update.message.reply_text('Произошла ошибка при чтении вопросов.')

    def fetch_target_urls_onetab(self, one_tab_url: str) -> Tuple[str, str, Optional[List[str]]]:
        """
        Извлечение целевых URL с указанного URL OneTab.

        Выполняется GET-запрос к указанному URL, парсится HTML-контент
        и извлекаются ссылки из тегов 'a' с классом 'tabLink'.

        Args:
            one_tab_url (str): URL страницы OneTab.

        Returns:
            Tuple[str, str, Optional[List[str]]]: Кортеж, содержащий цену, имя и список целевых URL.
            Возвращает пустые строки и None в случае ошибки.
        """
        try:
            #  Выполняет GET-запрос к OneTab
            response = requests.get(one_tab_url, timeout=10)
            #  Проверяет статус ответа, в случае ошибки выбрасывает исключение
            response.raise_for_status()

            # Проверка на успешный статус код
            if response.status_code != 200:
                logger.error(f'Ошибка при запросе к {one_tab_url}, статус код: {response.status_code}')
                return '', '', None

            #  Разбирает HTML-содержимое страницы
            soup = BeautifulSoup(response.content, 'html.parser')

            #  Извлекает все URL из тегов 'a' с классом 'tabLink'
            urls = [a['href'] for a in soup.find_all('a', class_='tabLink')]
            #  Извлекает данные из div с классом 'tabGroupLabel'
            element = soup.find('div', class_='tabGroupLabel')
            data = element.get_text() if element else None

            #  Проверка на наличие данных в элементе div
            if not data:
                price = ''
                mexiron_name = gs.now
            else:
                #  Разделяет данные на цену и имя
                parts = data.split(maxsplit=1)
                price = str(parts[0]) if parts else ''
                mexiron_name = parts[1] if len(parts) > 1 else gs.now
            return price, mexiron_name, urls

        except requests.exceptions.RequestException as ex:
            #  Логирует ошибку запроса
            logger.error(f'Ошибка при выполнении запроса к {one_tab_url}: %s', ex, exc_info=True)
            return '', '', None
```