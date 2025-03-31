## Анализ кода модуля `crawlee_python`

**Качество кода:**
- **Соответствие стандартам**: 7/10
- **Плюсы**:
  - Использование асинхронности для неблокирующих операций.
  - Четкая структура класса `CrawleePython`, облегчающая настройку и запуск краулера.
  - Использование библиотеки `crawlee` для управления браузером.
  - Наличие документации к основным методам и классам.
- **Минусы**:
  - Не все методы и атрибуты класса полностью документированы.
  - Используются устаревшие конструкции, такие как `List[str]` вместо `list[str]`.
  - Не хватает обработки исключений в некоторых местах.
  - Не используется `j_loads_ns` для загрузки конфигурационных файлов.

**Рекомендации по улучшению:**

1. **Документация**:
   - Дополнить документацию для всех методов и атрибутов класса, включая типы данных и возвращаемые значения.
   - Улучшить примеры использования в документации, чтобы они были более понятными и полными.
   - В документации к модулю добавить описание каждого класса и его назначения.

2. **Типизация**:
   - Использовать сокращенную запись для указания типов: `list`, `dict` вместо `List`, `Dict`.
   - Добавить аннотации типов для локальных переменных, где это необходимо.

3. **Обработка исключений**:
   - Добавить обработку исключений в методы `setup_crawler`, `run_crawler`, `export_data` и `get_data`.
   - Использовать `logger.error` с передачей информации об исключении (`exc_info=True`) для более подробного логирования ошибок.

4. **Конфигурация**:
   - Если используются конфигурационные файлы, заменить `json.load` на `j_loads_ns` для загрузки конфигурации как объектов `SimpleNamespace`.

5. **Форматирование**:
   - Привести код в соответствие со стандартами PEP8, включая добавление пробелов вокруг операторов.

6. **Логирование**:
   - Добавить логирование на разных уровнях (`info`, `debug`, `warning`) для более полного мониторинга работы краулера.

7. **Использование констант**:
   - Вынести магические значения, такие как `'firefox'`, `'results.json'` и `100` в константы для повышения читаемости и упрощения изменения.

**Оптимизированный код:**

```python
## \file /src/webdriver/crawlee_python/crawlee_python.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
Модуль для Crawlee Python Crawler
=================================================

Этот модуль предоставляет пользовательскую реализацию `PlaywrightCrawler` с использованием библиотеки Crawlee.
Он позволяет настраивать параметры браузера, обрабатывать запросы и извлекать данные с веб-страниц.

Классы
-------
- `CrawleePython`: Основной класс для запуска и управления веб-краулером.

Пример использования
----------------------

>>> if __name__ == "__main__":
>>>     async def main():
>>>         crawler = CrawleePython(max_requests=5, headless=False, browser_type='firefox')
>>>         await crawler.run(['https://www.example.com'])
>>>
>>>     asyncio.run(main())
"""

from pathlib import Path
from typing import Optional, List, Dict, Any
import asyncio

from crawlee.playwright_crawler import PlaywrightCrawler, PlaywrightCrawlingContext

from src import gs
from src.logger.logger import logger
from src.utils.jjson import j_loads_ns

# Define constants
DEFAULT_BROWSER_TYPE = 'firefox'
RESULTS_FILE_NAME = 'results.json'
CONTENT_PREVIEW_LENGTH = 100


class CrawleePython:
    """
    Пользовательская реализация `PlaywrightCrawler` с использованием библиотеки Crawlee.

    Attributes:
        max_requests (int): Максимальное количество запросов для выполнения во время обхода.
        headless (bool): Запускать ли браузер в безголовом режиме.
        browser_type (str): Тип браузера для использования ('chromium', 'firefox', 'webkit').
        options (list[str] | None): Список пользовательских параметров для передачи в браузер.
        crawler (PlaywrightCrawler | None): Экземпляр PlaywrightCrawler.
    """

    def __init__(self, max_requests: int = 5, headless: bool = False,
                 browser_type: str = DEFAULT_BROWSER_TYPE, options: Optional[list[str]] = None) -> None:
        """
        Инициализирует CrawleePython crawler с указанными параметрами.

        Args:
            max_requests (int): Максимальное количество запросов для выполнения во время обхода.
            headless (bool): Запускать ли браузер в безголовом режиме.
            browser_type (str): Тип браузера для использования ('chromium', 'firefox', 'webkit').
            options (list[str] | None): Список пользовательских параметров для передачи в браузер.

        Example:
            >>> crawler = CrawleePython(max_requests=10, headless=True, browser_type='chromium')
        """
        self.max_requests: int = max_requests
        self.headless: bool = headless
        self.browser_type: str = browser_type
        self.options: list[str] = options or []
        self.crawler: Optional[PlaywrightCrawler] = None

    async def setup_crawler(self) -> None:
        """
        Настраивает экземпляр PlaywrightCrawler с указанной конфигурацией.
        """
        try:
            self.crawler = PlaywrightCrawler(
                max_requests_per_crawl=self.max_requests,
                headless=self.headless,
                browser_type=self.browser_type,
                launch_options={"args": self.options}
            )

            @self.crawler.router.default_handler
            async def request_handler(context: PlaywrightCrawlingContext) -> None:
                """
                Обработчик запросов по умолчанию для обработки веб-страниц.

                Args:
                    context (PlaywrightCrawlingContext): Контекст обхода.
                """
                logger.info(f'Processing {context.request.url} ...')

                try:
                    # Enqueue all links found on the page.
                    await context.enqueue_links()

                    # Extract data from the page using Playwright API.
                    data: dict[str, Any] = {
                        'url': context.request.url,
                        'title': await context.page.title(),
                        'content': (await context.page.content())[:CONTENT_PREVIEW_LENGTH],
                    }

                    # Push the extracted data to the default dataset.
                    await context.push_data(data)

                except Exception as ex:
                    logger.error(f'Error processing {context.request.url}', ex, exc_info=True)
        except Exception as ex:
            logger.error('Error setting up crawler', ex, exc_info=True)

    async def run_crawler(self, urls: list[str]) -> None:
        """
        Запускает crawler с начальным списком URL-адресов.

        Args:
            urls (list[str]): Список URL-адресов для начала обхода.
        """
        try:
            await self.crawler.run(urls)
        except Exception as ex:
            logger.error('Error running crawler', ex, exc_info=True)

    async def export_data(self, file_path: str) -> None:
        """
        Экспортирует весь набор данных в JSON-файл.

        Args:
            file_path (str): Путь для сохранения экспортированного JSON-файла.
        """
        try:
            await self.crawler.export_data(file_path)
        except Exception as ex:
            logger.error('Error exporting data', ex, exc_info=True)

    async def get_data(self) -> dict[str, Any]:
        """
        Извлекает извлеченные данные.

        Returns:
            dict[str, Any]: Извлеченные данные в виде словаря.
        """
        try:
            data: dict[str, Any] = await self.crawler.get_data()
            return data
        except Exception as ex:
            logger.error('Error getting data', ex, exc_info=True)
            return {}

    async def run(self, urls: list[str]) -> None:
        """
        Основной метод для настройки, запуска crawler и экспорта данных.

        Args:
            urls (list[str]): Список URL-адресов для начала обхода.
        """
        try:
            await self.setup_crawler()
            await self.run_crawler(urls)
            await self.export_data(str(Path(gs.path.tmp / RESULTS_FILE_NAME)))
            data: dict[str, Any] = await self.get_data()
            logger.info(f'Extracted data: {data.items()}')
        except Exception as ex:
            logger.critical('Crawler failed with an error:', ex, exc_info=True)


# Example usage
if __name__ == '__main__':
    async def main():
        crawler = CrawleePython(max_requests=5, headless=False, browser_type='firefox', options=["--headless"])
        await crawler.run(['https://www.example.com'])

    asyncio.run(main())