# Анализ кода модуля `crawlee_python`

**Качество кода**
8
-  Плюсы
    - Код хорошо структурирован и использует классы для организации функциональности.
    - Присутствует документация в формате docstring для классов и методов.
    - Используется `PlaywrightCrawler` из библиотеки `crawlee` для управления браузером.
    - Код содержит пример использования в `if __name__ == '__main__'`
 -  Минусы
    - Не все комментарии соответствуют стандарту reStructuredText (RST).
    - Используется стандартный блок `try-except` вместо `logger.error`.
    - Отсутствуют проверки на типы данных в методах `run_crawler`, `export_data`, `get_data`, `run`.

**Рекомендации по улучшению**

1.  Привести все комментарии к формату reStructuredText (RST), особенно описания модулей, классов и методов.
2.  Использовать `logger.error` для обработки ошибок вместо стандартного блока `try-except`.
3.  Добавить проверки типов данных в методы, которые принимают параметры, чтобы предотвратить ошибки времени выполнения.
4.  Переименовать `file_path` в `export_path` в методе `export_data`, чтобы более точно отражать его назначение.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль для запуска и настройки веб-скрапера с использованием Crawlee и Playwright.
=================================================================================

Этот модуль предоставляет класс :class:`CrawleePython`, который инкапсулирует
функциональность для настройки и запуска веб-скрапера с использованием
библиотек `crawlee` и `playwright`.

Пример использования
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
# Добавлен импорт logger
from src.logger.logger import logger
# Добавлен импорт j_loads_ns
from src.utils.jjson import j_loads_ns


class CrawleePython:
    """
    Класс для настройки и запуска веб-скрапера с использованием Crawlee и Playwright.

    :ivar max_requests: Максимальное количество запросов для выполнения во время обхода.
    :vartype max_requests: int
    :ivar headless: Запускать ли браузер в режиме без графического интерфейса.
    :vartype headless: bool
    :ivar browser_type: Тип используемого браузера ('chromium', 'firefox', 'webkit').
    :vartype browser_type: str
    :ivar crawler: Экземпляр PlaywrightCrawler.
    :vartype crawler: PlaywrightCrawler
    """

    def __init__(self, max_requests: int = 5, headless: bool = False, browser_type: str = 'firefox', options: Optional[List[str]] = None):
        """
        Инициализирует класс CrawleePython с заданными параметрами.

        :param max_requests: Максимальное количество запросов для выполнения во время обхода.
        :type max_requests: int
        :param headless: Запускать ли браузер в режиме без графического интерфейса.
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
        Настраивает экземпляр PlaywrightCrawler с заданной конфигурацией.
        """
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

            :param context: Контекст обхода.
            :type context: PlaywrightCrawlingContext
            """
            context.log.info(f'Processing {context.request.url} ...')

            # Добавляет все найденные на странице ссылки в очередь.
            await context.enqueue_links()

            # Извлекает данные со страницы с использованием Playwright API.
            data = {
                'url': context.request.url,
                'title': await context.page.title(),
                'content': (await context.page.content())[:100],
            }

            # Отправляет извлеченные данные в набор данных по умолчанию.
            await context.push_data(data)

    async def run_crawler(self, urls: List[str]):
        """
        Запускает обход с начальным списком URL-адресов.

        :param urls: Список URL-адресов для начала обхода.
        :type urls: List[str]
        """
        # Проверка типа данных для `urls`
        if not isinstance(urls, list):
            logger.error(f'Ожидается список URL, получен {type(urls)}')
            return
        await self.crawler.run(urls)

    async def export_data(self, export_path: str):
        """
        Экспортирует весь набор данных в JSON-файл.

        :param export_path: Путь для сохранения экспортированного JSON-файла.
        :type export_path: str
        """
        # Проверка типа данных для `export_path`
        if not isinstance(export_path, str):
             logger.error(f'Ожидается строка для пути экспорта, получен {type(export_path)}')
             return
        await self.crawler.export_data(export_path)

    async def get_data(self) -> Dict[str, Any]:
        """
        Возвращает извлеченные данные.

        :return: Извлеченные данные в виде словаря.
        :rtype: Dict[str, Any]
        """
        data = await self.crawler.get_data()
        return data

    async def run(self, urls: List[str]):
        """
        Основной метод для настройки, запуска обхода и экспорта данных.

        :param urls: Список URL-адресов для начала обхода.
        :type urls: List[str]
        """
        try:
            # Настройка и запуск краулера
            await self.setup_crawler()
            await self.run_crawler(urls)
            # Экспорт данных в файл
            await self.export_data(str(Path(gs.path.tmp / 'results.json')))
            # Получение данных
            data = await self.get_data()
            logger.info(f'Extracted data: {data.items()}')
        except Exception as ex:
            # Логирование ошибки
            logger.critical('Crawler failed with an error:', exc_info=ex)


# Пример использования
if __name__ == '__main__':
    async def main():
        # Пример запуска краулера
        crawler = CrawleePython(max_requests=5, headless=False, browser_type='firefox', options=["--headless"])
        await crawler.run(['https://www.example.com'])

    asyncio.run(main())
```