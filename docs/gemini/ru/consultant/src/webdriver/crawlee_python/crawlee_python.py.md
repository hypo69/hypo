# Анализ кода модуля `crawlee_python`

**Качество кода**
8
-  Плюсы
    - Код хорошо структурирован, используется объектно-ориентированный подход.
    - Присутствуют docstring для классов и методов, описывающие их назначение.
    - Используется `asyncio` для асинхронных операций, что подходит для веб-скрейпинга.
    - Применяется `PlaywrightCrawler` из библиотеки `crawlee`.
    - Включен пример использования в `if __name__ == '__main__':`.

-  Минусы
    - Не все docstring соответствуют стандарту reStructuredText (RST).
    - Отсутствует описание модуля в формате RST.
    - Не используется `j_loads` или `j_loads_ns`.
    - Отсутствует обработка ошибок с помощью `logger.error`.
    - Комментарии `#` не всегда содержат подробное описание следующего блока кода.
    - Присутствует дублирование имени класса `CrawleeExperiment` в примере использования (должен быть `CrawleePython`).
    - Не все импорты используются.

**Рекомендации по улучшению**
1. Добавить описание модуля в формате RST.
2. Переписать все docstring в формате RST.
3. Заменить стандартный `json.load` на `j_loads` или `j_loads_ns`, если требуется чтение json файлов.
4. Использовать `logger.error` для обработки исключений.
5. Добавить более подробные комментарии `#` для каждого блока кода.
6. Исправить дублирование имени класса в примере использования.
7. Убрать неиспользуемые импорты.
8. Добавить логирование ошибок и исключений.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для веб-скрейпинга с использованием Crawlee и Playwright.
=========================================================================================

Этот модуль содержит класс :class:`CrawleePython`, который используется для настройки и запуска веб-скрейпинга.
Он использует библиотеку `crawlee` для управления асинхронным сбором данных.

Пример использования
--------------------

Пример использования класса `CrawleePython`:

.. code-block:: python

    experiment = CrawleePython(max_requests=5, headless=False, browser_type='firefox')
    asyncio.run(experiment.run(['https://ksp.co.il']))
"""
MODE = 'dev'

from pathlib import Path
import asyncio
from crawlee.playwright_crawler import PlaywrightCrawler, PlaywrightCrawlingContext
from src.logger.logger import logger

class CrawleePython:
    """
    Класс для настройки и запуска веб-скрейпинга с использованием Crawlee и Playwright.

    :param max_requests: Максимальное количество запросов для сбора данных.
    :param headless: Запускать ли браузер в фоновом режиме.
    :param browser_type: Тип используемого браузера ('firefox', 'chromium', 'webkit').
    """
    def __init__(self, max_requests: int = 5, headless: bool = False, browser_type: str = 'firefox'):
        """
        Инициализирует класс CrawleePython с указанными параметрами.
        """
        self.max_requests = max_requests
        self.headless = headless
        self.browser_type = browser_type
        self.crawler = None

    async def setup_crawler(self):
        """
        Настраивает экземпляр PlaywrightCrawler.
        """
        self.crawler = PlaywrightCrawler(
            max_requests_per_crawl=self.max_requests,
            headless=self.headless,
            browser_type=self.browser_type,
        )

        @self.crawler.router.default_handler
        async def request_handler(context: PlaywrightCrawlingContext) -> None:
            """
            Обработчик запросов по умолчанию, вызывается для каждой страницы.

            :param context: Контекст обхода Playwright.
            """
            context.log.info(f'Processing {context.request.url} ...')

            # Код ставит в очередь все ссылки, найденные на странице.
            await context.enqueue_links()

            # Код извлекает данные со страницы с помощью API Playwright.
            data = {
                'url': context.request.url,
                'title': await context.page.title(),
                'content': (await context.page.content())[:100],
            }

            # Код отправляет извлеченные данные в набор данных по умолчанию.
            await context.push_data(data)

    async def run_crawler(self, urls: list[str]):
        """
        Запускает сканер с начальным списком URL-адресов.

        :param urls: Список URL-адресов для запуска обхода.
        """
        try:
            await self.crawler.run(urls)
        except Exception as e:
            logger.error(f"Ошибка при запуске сканера: {e}")

    async def export_data(self, file_path: str):
        """
        Экспортирует весь набор данных в JSON-файл.

        :param file_path: Путь для сохранения экспортированного JSON-файла.
        """
        try:
            await self.crawler.export_data(file_path)
        except Exception as e:
            logger.error(f"Ошибка при экспорте данных: {e}")

    async def get_data(self) -> dict:
        """
        Получает извлеченные данные.

        :return: Извлеченные данные в виде словаря.
        """
        try:
            data = await self.crawler.get_data()
            return data
        except Exception as e:
             logger.error(f"Ошибка при получении данных: {e}")
             return {}

    async def run(self, urls: list[str]):
        """
        Основной метод для настройки, запуска сканера и экспорта данных.

        :param urls: Список URL-адресов для запуска обхода.
        """
        try:
            await self.setup_crawler()
            await self.run_crawler(urls)
            await self.export_data(str(Path(gs.path.tmp / 'results.json')))
            data = await self.get_data()
            logger.info(f'Extracted data: {data.items()}')
        except Exception as e:
            logger.error(f"Общая ошибка при выполнении: {e}")


# Пример использования
if __name__ == '__main__':
    async def main():
        # Код создает экземпляр класса CrawleePython
        experiment = CrawleePython(max_requests=5, headless=False, browser_type='firefox')
        # Код запускает процесс сканирования
        await experiment.run(['https://ksp.co.il'])

    # Код запускает асинхронную функцию main
    asyncio.run(main())
```