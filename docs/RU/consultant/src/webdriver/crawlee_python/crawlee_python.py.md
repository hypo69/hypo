# Анализ кода модуля `crawlee_python`

**Качество кода**

7
-  Плюсы
    - Код хорошо структурирован и читаем.
    - Используется асинхронность, что хорошо для веб-скрейпинга.
    - Есть документация для класса и методов.
    - Присутствует пример использования.
-  Минусы
    - Не все функции и методы имеют подробную документацию.
    - Используются двойные кавычки вместо одинарных в коде.
    - Не все комментарии соответствуют стандарту RST.
    - Обработка ошибок не всегда оптимальна, можно использовать `logger.error` вместо `try-except`.
    - Отсутствует описание модуля в начале файла.

**Рекомендации по улучшению**

1.  **Документация**:
    - Добавить описание модуля в начале файла в формате RST.
    - Уточнить документацию для всех функций, методов и параметров.
    - Использовать одинарные кавычки для строк в коде.
    - Использовать стиль RST для комментариев в docstring.

2.  **Импорты**:
    - Проверить и добавить отсутствующие импорты, если необходимо.

3.  **Обработка ошибок**:
    -  Использовать `logger.error` для обработки исключений вместо `try-except`.

4.  **Конфигурация**:
    - `options` должен быть с типом `Optional[List[str]] = None`.
5.  **Форматирование**:
   - Использовать `logger.info(f'Extracted data: {data}')` вместо `logger.info(f'Extracted data: {data.items()}')`

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12
"""
Модуль для реализации кастомного веб-краулера на основе библиотеки Crawlee.
========================================================================

Этот модуль предоставляет класс :class:`CrawleePython`, который является кастомной реализацией `PlaywrightCrawler`
с использованием библиотеки Crawlee. Он позволяет настраивать параметры браузера, обрабатывать запросы и извлекать
данные с веб-страниц.

Пример использования:
--------------------

.. code-block:: python

    if __name__ == "__main__":
        async def main():
            crawler = CrawleePython(max_requests=5, headless=False, browser_type='firefox')
            await crawler.run(['https://www.example.com'])

        asyncio.run(main())
"""

from pathlib import Path
from typing import Optional, List, Dict, Any
from src import gs
import asyncio
from crawlee.playwright_crawler import PlaywrightCrawler, PlaywrightCrawlingContext
from src.logger.logger import logger
from src.utils.jjson import j_loads_ns


class CrawleePython:
    """
    Кастомная реализация `PlaywrightCrawler` с использованием библиотеки Crawlee.

    :param max_requests: Максимальное количество запросов для выполнения во время обхода.
    :type max_requests: int
    :param headless: Запускать ли браузер в безголовом режиме.
    :type headless: bool
    :param browser_type: Тип используемого браузера ('chromium', 'firefox', 'webkit').
    :type browser_type: str
    :param options: Список пользовательских опций для передачи в браузер.
    :type options: Optional[List[str]]
    :ivar crawler: Экземпляр PlaywrightCrawler.
    :vartype crawler: PlaywrightCrawler
    """

    def __init__(self, max_requests: int = 5, headless: bool = False, browser_type: str = 'firefox', options: Optional[List[str]] = None):
        """
        Инициализирует краулер CrawleePython с указанными параметрами.

        :param max_requests: Максимальное количество запросов для выполнения во время обхода.
        :type max_requests: int
        :param headless: Запускать ли браузер в безголовом режиме.
        :type headless: bool
        :param browser_type: Тип используемого браузера ('chromium', 'firefox', 'webkit').
        :type browser_type: str
        :param options: Список пользовательских опций для передачи в браузер.
        :type options: Optional[List[str]]
        """
        self.max_requests = max_requests
        self.headless = headless
        self.browser_type = browser_type
        self.options = options or []
        self.crawler = None

    async def setup_crawler(self):
        """
        Настраивает экземпляр PlaywrightCrawler с указанной конфигурацией.
        """
        #  Инициализация экземпляра PlaywrightCrawler с заданными параметрами
        self.crawler = PlaywrightCrawler(
            max_requests_per_crawl=self.max_requests,
            headless=self.headless,
            browser_type=self.browser_type,
            launch_options={'args': self.options}
        )

        @self.crawler.router.default_handler
        async def request_handler(context: PlaywrightCrawlingContext) -> None:
            """
            Обработчик запросов по умолчанию для обработки веб-страниц.

            :param context: Контекст обхода.
            :type context: PlaywrightCrawlingContext
            """
            # Логирование обрабатываемого URL
            context.log.info(f'Processing {context.request.url} ...')

            # Добавление найденных ссылок в очередь
            await context.enqueue_links()

            # Извлечение данных со страницы с помощью API Playwright
            data = {
                'url': context.request.url,
                'title': await context.page.title(),
                'content': (await context.page.content())[:100],
            }

            #  Отправка извлеченных данных в набор данных по умолчанию
            await context.push_data(data)

    async def run_crawler(self, urls: List[str]):
        """
        Запускает краулер с начальным списком URL-адресов.

        :param urls: Список URL-адресов для запуска обхода.
        :type urls: List[str]
        """
        # Запуск обхода с указанными URL-адресами
        await self.crawler.run(urls)

    async def export_data(self, file_path: str):
        """
        Экспортирует весь набор данных в JSON-файл.

        :param file_path: Путь для сохранения экспортированного JSON-файла.
        :type file_path: str
        """
        # Экспорт данных в JSON-файл
        await self.crawler.export_data(file_path)

    async def get_data(self) -> Dict[str, Any]:
        """
        Получает извлеченные данные.

        :return: Извлеченные данные в виде словаря.
        :rtype: Dict[str, Any]
        """
        # Получение извлеченных данных
        data = await self.crawler.get_data()
        return data

    async def run(self, urls: List[str]):
        """
        Основной метод для настройки, запуска краулера и экспорта данных.

        :param urls: Список URL-адресов для запуска обхода.
        :type urls: List[str]
        """
        #  Код выполняет настройку, запуск краулера и экспорт данных.
        try:
            await self.setup_crawler()
            await self.run_crawler(urls)
            await self.export_data(str(Path(gs.path.tmp / 'results.json')))
            data = await self.get_data()
            logger.info(f'Extracted data: {data}')
        except Exception as ex:
            logger.error('Crawler failed with an error:', ex)


# Пример использования
if __name__ == '__main__':
    async def main():
        crawler = CrawleePython(max_requests=5, headless=False, browser_type='firefox', options=["--headless"])
        await crawler.run(['https://www.example.com'])

    asyncio.run(main())
```