# Анализ кода модуля `crawlee_python`

**Качество кода**
7
-  Плюсы
    -  Код предоставляет базовую функциональность для веб-скрейпинга с использованием `crawlee` и `Playwright`.
    -  Использует асинхронность для эффективной обработки запросов.
    -  Экспортирует данные в JSON для удобного хранения и анализа.
    -  Структура кода организована в виде класса, что способствует повторному использованию.
-  Минусы
    -  Отсутствует обработка ошибок для различных этапов (например, при загрузке страницы).
    -  Не хватает подробных комментариев в формате reStructuredText.
    -  Используется стандартный `json.dumps` вместо `j_dumps` или `j_dumps_ns`.
    -  Жестко заданные локаторы (CSS селекторы) для извлечения данных, что делает код менее гибким.
    -  Нет логирования для отслеживания проблем.
    -  Не используется `j_loads` или `j_loads_ns` для чтения данных из JSON файла.
    -  Не хватает проверок на наличие элементов перед их извлечением.
    -  Не хватает документации в формате reStructuredText (RST).

**Рекомендации по улучшению**

1.  **Документация**:
    -   Добавить docstring в формате reStructuredText (RST) для модуля, класса и всех методов.
2.  **Обработка ошибок**:
    -   Использовать `try-except` блоки с логированием ошибок через `logger.error` вместо стандартного `print`.
3.  **JSON**:
    -   Использовать `j_dumps` или `j_dumps_ns` из `src.utils.jjson` для записи JSON.
    -   Использовать `j_loads` или `j_loads_ns` для чтения JSON файлов.
4.  **Логирование**:
    -   Добавить логирование для отслеживания работы программы, а также для отлавливания исключений.
    -   Использовать `from src.logger.logger import logger` для логирования.
5.  **Гибкость**:
    -   Сделать CSS-селекторы настраиваемыми через параметры или конфигурационный файл.
6.  **Проверки**:
    -   Проверять наличие элементов перед попыткой извлечения данных, чтобы избежать ошибок.
7.  **Импорты**:
    -   Добавить все необходимые импорты в начале файла.
8.  **Комментарии**:
    -  Добавить комментарии к коду с объяснением каждого шага, придерживаясь стиля RST.

**Оптимизированный код**

```python
"""
Модуль для веб-скрейпинга с использованием Crawlee и Playwright.
==================================================================

Этот модуль определяет класс :class:`CrawleePython`, который использует библиотеку `crawlee`
и `Playwright` для сбора данных с веб-страниц.
Модуль предоставляет функциональность для настройки, запуска, и экспорта данных.

Пример использования
--------------------

.. code-block:: python

    import asyncio
    from src.webdriver.crawlee_python.crawlee_python import CrawleePython

    async def main():
        crawler = CrawleePython(max_requests=10, headless=True, browser_type='chromium')
        await crawler.run(urls=['https://news.ycombinator.com/'], output_file='hacker_news.json')
        print(crawler.get_data())

    if __name__ == "__main__":
        asyncio.run(main())
"""
import asyncio
from typing import Any, Dict, List
from crawlee import PlaywrightCrawler, Request
from playwright.sync_api import BrowserType
from src.utils.jjson import j_dumps, j_loads
from src.logger.logger import logger

class CrawleePython:
    """
    Класс для веб-скрейпинга с использованием Crawlee и Playwright.

    :param max_requests: Максимальное количество запросов для выполнения.
    :type max_requests: int
    :param headless: Запускать браузер в режиме без графического интерфейса.
    :type headless: bool
    :param browser_type: Тип браузера для использования ('chromium', 'firefox', 'webkit').
    :type browser_type: str
    """
    def __init__(self, max_requests: int, headless: bool, browser_type: str):
        """
        Инициализирует класс CrawleePython.
        """
        self.max_requests = max_requests
        self.headless = headless
        self.browser_type = browser_type
        self.data: List[Dict[str, Any]] = []
        self.crawler = PlaywrightCrawler(
            max_requests=max_requests,
            headless=headless,
            browser_type=browser_type
        )

    def setup_crawler(self):
        """
        Настраивает обработчик запросов для краулера.
        
        Метод определяет функцию для обработки каждого запроса.
        Функция извлекает данные из веб-страницы и добавляет их во внутренний список данных.
        """
        @self.crawler.request_handler
        async def handle_request({request, page, enqueue_links}):
            """
            Обработчик для каждого запроса.

            :param request: Объект запроса.
            :type request: crawlee.request.Request
            :param page: Объект страницы Playwright.
            :type page: playwright.sync_api.Page
            :param enqueue_links: Функция для добавления новых ссылок в очередь.
            :type enqueue_links: Callable
            """
            try:
                # Код извлекает все посты со страницы.
                posts = await page.locator('.athing').all()
                for post in posts:
                   try:
                        # Код извлекает заголовок, ранг и ссылку из поста.
                        title = await post.locator('.titlelink').inner_text()
                        rank = await post.locator('.rank').inner_text()
                        link = await post.locator('.titlelink').get_attribute('href')
                        # Код добавляет извлеченные данные в список.
                        self.data.append({'title': title, 'rank': rank, 'link': link})
                        
                   except Exception as e:
                       # Код логирует ошибку, если не удалось извлечь данные из поста
                       logger.error(f'Ошибка при извлечении данных из поста: {e}', exc_info=True)
            except Exception as e:
                 # Код логирует общую ошибку при обработке запроса
                logger.error(f'Ошибка при обработке запроса {request.url}: {e}', exc_info=True)
    
    async def run_crawler(self, urls: List[str]):
        """
        Запускает процесс обхода страниц.

        :param urls: Список URL для начала обхода.
        :type urls: List[str]
        """
        # Код запускает краулер
        await self.crawler.run(urls)

    def export_data(self, output_file: str):
        """
        Экспортирует собранные данные в JSON файл.

        :param output_file: Имя файла для экспорта.
        :type output_file: str
        """
        try:
            # Код сохраняет собранные данные в JSON файл.
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(j_dumps(self.data, indent=4))
        except Exception as e:
            # Код логирует ошибку, если не удалось записать данные в файл
            logger.error(f'Ошибка при экспорте данных в файл {output_file}: {e}', exc_info=True)
            ...

    def get_data(self) -> Dict[str, Any]:
        """
        Возвращает собранные данные в виде словаря.

        :return: Словарь с собранными данными.
        :rtype: Dict[str, Any]
        """
        # Код возвращает собранные данные
        return {'data': self.data}

    async def run(self, urls: List[str], output_file: str):
         """
        Запускает весь процесс краулинга, включая настройку, запуск, экспорт и вывод данных.

        :param urls: Список URL для начала обхода.
        :type urls: List[str]
        :param output_file: Имя файла для экспорта.
        :type output_file: str
        """
         # Код настраивает краулер
         self.setup_crawler()
         # Код запускает краулер
         await self.run_crawler(urls)
         # Код экспортирует собранные данные в файл.
         self.export_data(output_file)
         # Код выводит собранные данные
         print(self.get_data())

async def main():
    """
    Пример использования класса CrawleePython.
    """
    # Код создает экземпляр класса CrawleePython
    crawler = CrawleePython(max_requests=10, headless=True, browser_type='chromium')
    # Код запускает краулер на указанных URL
    await crawler.run(urls=['https://news.ycombinator.com/'], output_file='hacker_news.json')
    # Код выводит полученные данные
    print(crawler.get_data())

if __name__ == "__main__":
    # Код запускает асинхронную функцию main
    asyncio.run(main())
```