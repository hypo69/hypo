# <input code>

```python
## \file hypotez/src/endpoints/kazarinov/bot_handlers_parser.py
# -*- coding: utf-8 -*-\

#! venv/bin/python/python3.12
"""
.. module: src.endpoints.kazarinov.bot_handlers 
	:platform: Windows, Unix
	:synopsis: Обработка событий телеграм бота

Модуль для работы с событиями телеграм-бота
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



import header
import random
import asyncio
import requests
from typing import Optional, Any
from bs4 import BeautifulSoup
from src import gs
from src.logger import logger
from src.webdriver.driver import Driver
from src.webdriver.chrome import Chrome
from src.webdriver.firefox import Firefox
from src.webdriver.edge import Edge
from src.ai.gemini import GoogleGenerativeAI
from src.endpoints.kazarinov.scenarios.scenario_pricelist import Mexiron
from src.utils.url import is_url
from src.utils.printer import pprint
from telegram import Update
from telegram.ext import CallbackContext


class BotHandler:
    """Исполнитель команд, полученных ботом."""

    mexiron: Mexiron

    def __init__(self, webdriver_name: Optional[str] = 'firefox'):
        """
        Инициализация обработчика событий телеграм-бота.

        Args:
            webdriver_name (Optional[str]): Название веб-драйвера для запуска.
        """

        self.mexiron = Mexiron(
            Driver(
                Firefox if webdriver_name.lower() == 'firefox'
                else Chrome if webdriver_name.lower() == 'chrome'
                else Edge
            )
        )

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
            price, mexiron_name, urls = self.get_data_from_onetab(response)
            if not all([price, mexiron_name, urls]):
                await update.message.reply_text('Некорректные данные.')

            if await self.mexiron.run_scenario(price=price, mexiron_name=mexiron_name, urls=urls, update=update):
                await update.message.reply_text('Готово!\\nСсылку я вышлю на WhatsApp')
                return True
        else:
            await update.message.reply_text('Ошибка. Попробуй ещё раз.')
            ...
            return

    # ... (other methods)
```

# <algorithm>

**Шаг 1:** Получение URL от пользователя.
* **Вход:** `update.message.text` (текст сообщения).
* **Пример:** `https://one-tab.com/some-url`

**Шаг 2:** Проверка URL.
* **Вход:** URL.
* **Условие:** Проверка на соответствие шаблону `https://one-tab.com` и т.п.
* **Пример:** `https://one-tab.com` - проходит проверку. `https://example.com` - не проходит.
* **Выход:** Если соответствует -  переходит к следующему шагу, иначе отправляет сообщение об ошибке.

**Шаг 3:** Извлечение данных.
* **Вход:** Соответствующий URL.
* **Функция:** `get_data_from_onetab(response)`.  Парсит URL одной страницы и получает данные о цене, названии и списке ссылок.
* **Пример:** Извлекает `price=100`, `mexiron_name='some_name'`, `urls=['url1', 'url2']` из `https://one-tab.com/some-url`
* **Выход:**  `price`, `mexiron_name`, `urls`.  Возвращает `False` при ошибке парсинга.


**Шаг 4:** Проверка наличия данных.
* **Вход:** `price`, `mexiron_name`, `urls`.
* **Условие:** Все значения должны быть не `False`.
* **Выход:** Если не все значения присутствуют, отправляется сообщение об ошибке.

**Шаг 5:** Запуск сценария.
* **Вход:** `price`, `mexiron_name`, `urls`, `update`.
* **Функция:** `self.mexiron.run_scenario()`. Выполнение сценария, связанного с `Mexiron` (цена, название, ссылки).
* **Пример:** На основе полученных данных выполняется какой-то сценарий, связанный с обработкой данных о цене.
* **Выход:**  `True` или `False`. `True` - сценарий успешно выполнен.

**Шаг 6:** Ответ пользователю.
* **Вход:** Результат `self.mexiron.run_scenario()`.
* **Выход:**
    * Если сценарий выполнен успешно (`True`), отправляется сообщение "Готово!" и дальнейшая обработка (отправка данных на WhatsApp).
    * Если сценарий выполнен неуспешно (`False`), отправляется сообщение об ошибке.


# <mermaid>

```mermaid
graph TD
    A[Пользователь вводит URL] --> B{Проверка URL на соответствие};
    B -- Соответствует --> C[get_data_from_onetab];
    B -- Не соответствует --> D[Ошибка, Отправка сообщения];
    C --> E{Проверка наличия price, mexiron_name, urls};
    E -- Все значения присутствуют --> F[mexiron.run_scenario];
    E -- Отсутствуют значения --> G[Ошибка, Отправка сообщения];
    F -- Успех --> H[Отправка сообщения "Готово!"];
    F -- Ошибка --> I[Ошибка, Отправка сообщения];
    D --> I;
    H --> J[Отправка данных на WhatsApp];
    I --> J;

    subgraph BotHandler
        C --> C1[Формирование данных];
        C1 --> C2[Передача данных в Mexiron];
        C2 --> C3[Mexiron.run_scenario];
        C3 --> C4[Возврат результата];
    end
```

# <explanation>

**Импорты:**

* `header`: Вероятно, файл с общими заголовками и константами.
* `random`: Для случайного выбора (например, в handle_next_command).
* `asyncio`: Для асинхронных операций.
* `requests`: Для выполнения HTTP-запросов к OneTab.
* `typing`: Для аннотаций типов.
* `bs4`: Для парсинга HTML.
* `gs`: Вероятно, содержит глобальные настройки или переменные (gs.now).
* `logger`: Для логирования.
* `Driver`: Базовый класс для веб-драйверов.
* `Chrome`, `Firefox`, `Edge`: Классы для работы с конкретными веб-драйверами.
* `GoogleGenerativeAI`: Возможно, класс для работы с AI.
* `Mexiron`: Класс для работы со сценарием.
* `is_url`, `pprint`:  Функции для проверки URL и красивой печати.
* `telegram`: Для работы с Telegram ботом.
* `CallbackContext`: Для работы с контекстом Telegram.


**Классы:**

* `BotHandler`: Обрабатывает команды пользователя, в том числе извлекает данные из OneTab и запускает сценарий `Mexiron`. Имеет атрибут `mexiron` для взаимодействия со сценарием.
* `Mexiron`:  Вероятно, реализует сценарий обработки данных (из `scenario_pricelist`).

**Функции:**

* `handle_url`: Обрабатывает URL, полученный от пользователя, извлекает данные, запускает сценарий и отправляет ответ в Telegram.
* `get_data_from_onetab`: Извлекает данные о цене, имени и URL из HTML страницы OneTab. Возвращает `False` при ошибке.
* `fetch_target_urls_onetab`:  Парсит HTML страницу onetab и извлекает ссылки, цена и имя.
* `handle_next_command`: Обрабатывает команду '--next' и её аналоги (получение ответа от AI, вероятно).


**Переменные:**

* `MODE`: Вероятно, режим работы (dev/prod).
* `response`: Содержит текст сообщения пользователя.


**Возможные ошибки и улучшения:**

* **Обработка исключений:**  В коде есть обработка исключений (`try...except`), но её можно улучшить, например, добавление более подробных сообщений об ошибках в лог, чтобы упростить отладку.
* **Уменьшение кода:** Можно оптимизировать `get_data_from_onetab` и `fetch_target_urls_onetab` для уменьшения повторяющихся кодов.
* **Добавить проверку статуса ответа `requests`:**  В `fetch_target_urls_onetab` надо проверить статус кода `response.status_code`, чтобы избежать ошибок при некорректных ответах от сервера.
* **Проверка валидности данных:** Более тщательная проверка валидности полученных данных (например, проверка, является ли price числом и т.д.).


**Связь с другими частями проекта:**

* `BotHandler` использует `Mexiron`, `Driver`, `Firefox`, `Chrome` или `Edge` (вероятно, из `src.webdriver`).
* `BotHandler` использует логирование из `src.logger`.
* `BotHandler` использует  `src.utils` (is_url, pprint)
* Вероятно, существует зависимость от `gs` для конфигурации (например, для настроек отправки сообщений на WhatsApp).


В целом код хорошо структурирован и читаем.  Обработка ошибок и логирование реализованы, что положительно сказывается на надежности кода.