# Анализ кода модуля `crawlee_python`

**Качество кода**
8
-  Плюсы
    -   Код хорошо структурирован, с четким разделением на методы.
    -   Используется асинхронное программирование для эффективной работы.
    -   Есть возможность настройки основных параметров краулера.
    -   Код имеет пример использования.
-  Минусы
    -  Отсутствует документация в формате RST для модуля и его методов.
    -  Не используется `from src.logger.logger import logger` для логирования.
    -  Некоторые блоки `try-except` можно заменить на `logger.error`.
    -  Не везде используется `j_loads` или `j_loads_ns` для работы с JSON.
    -  Отсутствует описание модуля в начале файла.
    -  Желательно добавить обработку ошибок при работе с файловой системой.

**Рекомендации по улучшению**

1.  **Добавить описание модуля**: В начале файла добавить описание модуля в формате RST.
2.  **Документирование**: Добавить docstrings в формате RST для всех функций, методов и переменных.
3.  **Использовать `src.logger.logger`**: Заменить импорт `logger` на `from src.logger.logger import logger`.
4.  **Упростить обработку ошибок**: Использовать `logger.error` для обработки исключений вместо `try-except`.
5.  **Использовать `j_loads`**: Заменить `json.load` на `j_loads` для загрузки JSON.
6.  **Обработка ошибок**: Добавить обработку ошибок при работе с файлами, например, при записи в файл.
7. **Стандартизация кавычек:** Использовать одинарные кавычки для строк в коде, двойные кавычки только в операциях вывода.

**Оптимизированный код**

```python
"""
Модуль для веб-скрейпинга с использованием Crawlee и Playwright.
=================================================================

Этот модуль содержит класс :class:`CrawleePython`, который использует библиотеку `crawlee`
и `Playwright` для выполнения веб-скрейпинга. Он позволяет настраивать краулер,
извлекать данные со страниц и экспортировать их в JSON файл.

Пример использования
--------------------

Пример использования класса `CrawleePython`:

.. code-block:: python

    crawler = CrawleePython(max_requests=10, headless=True, browser_type='chromium')
    crawler.run(['https://news.ycombinator.com/'])

"""
import asyncio
from pathlib import Path
from typing import Any, List

from crawlee import PlaywrightCrawler
# from src.logger import logger # старый импорт
from src.logger.logger import logger # импорт для логирования
from src.utils.jjson import j_loads # импорт для загрузки json
# import json # старый импорт
class CrawleePython:
    """
    Класс для веб-скрейпинга с использованием Crawlee и Playwright.

    Args:
        max_requests (int): Максимальное количество запросов для выполнения.
        headless (bool): Запуск браузера в headless режиме.
        browser_type (str): Тип браузера для использования (chromium, firefox, webkit).
    """
    def __init__(self, max_requests: int = 10, headless: bool = True, browser_type: str = 'chromium'):
        """Инициализация краулера PlaywrightCrawler."""
        self.crawler = PlaywrightCrawler(
            max_requests=max_requests,
            headless=headless,
            browser_type=browser_type,
        )
        self.data = []

    def setup_crawler(self):
        """
        Настройка краулера для обработки запросов.

        Конфигурирует краулер для извлечения данных со страницы и добавления ссылок для дальнейшего обхода.
        """
        @self.crawler.request_handler
        async def handle_request(page, request):
            """
            Обработчик запросов для извлечения данных со страницы.

            Args:
                page: Объект страницы Playwright.
                request: Объект запроса Playwright.

            Извлекает данные о постах, заголовках и рангах со страницы, формируя список словарей.
            """
            try:
                posts = await page.locator('.athing').all() # получение всех элементов постов
                for post in posts: # цикл по всем постам на странице
                    title_element = await post.locator('.titlelink').first() # получение элемента заголовка
                    rank_element = await post.locator('.rank').first()  # получение элемента ранга
                    link_element = await title_element.evaluate_handle('node => node.href') # получение ссылки

                    title = await title_element.inner_text() # получение текста заголовка
                    rank = await rank_element.inner_text() if rank_element else '' # получение текста ранга, если он существует
                    link = link_element # присваивание ссылки
                    self.data.append({'title': title, 'rank': rank, 'link': link}) # добавление данных в список
            except Exception as ex: #  если есть ошибка при парсинге
                logger.error('Ошибка при обработке запроса', exc_info=ex) # логирование ошибки

            try:
                links = await page.locator('a').evaluate_all('nodes => nodes.map(node => node.href)') # получение всех ссылок на странице
                for link in links: # цикл по ссылкам
                  if link:
                    await self.crawler.enqueue(link)  # добавление ссылки в очередь, если она существует
            except Exception as ex: # если есть ошибка при добавлении ссылок
                logger.error('Ошибка при добавлении ссылок в очередь', exc_info=ex) # логирование ошибки


    async def run_crawler(self, start_urls: List[str]):
        """
        Запуск краулера.

        Args:
            start_urls (list[str]): Список начальных URL-адресов для краулинга.
        """
        await self.crawler.run(start_urls=start_urls) # запуск краулера

    def export_data(self, file_path: str | Path = 'output.json'):
        """
        Экспорт данных в JSON файл.

        Args:
            file_path (str | Path): Путь к файлу для сохранения данных.
        """
        try:
          # код записывает данные в файл
            with open(file_path, 'w', encoding='utf-8') as f:
                # json.dump(self.data, f, indent=4, ensure_ascii=False) # старый метод
                f.write(j_loads(self.data, indent=4, ensure_ascii=False)) # запись данных с использованием j_loads
        except Exception as ex: # если есть ошибка записи в файл
            logger.error('Ошибка при экспорте данных в файл', exc_info=ex) # логирование ошибки

    def get_data(self) -> dict:
        """
        Возвращает извлеченные данные.

        Returns:
            dict: Словарь с извлеченными данными.
        """
        return {'data': self.data} # возвращает данные

    async def run(self, start_urls: List[str] = ['https://news.ycombinator.com/']):
        """
        Запускает весь процесс краулинга, включая настройку, запуск, экспорт и вывод данных.

        Args:
            start_urls (list[str]): Список начальных URL-адресов для краулинга.
        """
        self.setup_crawler() # вызов метода настройки краулера
        await self.run_crawler(start_urls=start_urls) # вызов метода запуска краулера
        self.export_data() # вызов метода экспорта данных
        print(self.get_data()) # вывод полученных данных

async def main():
    """
    Основная функция для запуска краулера.

    Пример использования класса `CrawleePython`.
    """
    crawler = CrawleePython(max_requests=10, headless=True, browser_type='chromium') # создание экземпляра класса
    await crawler.run() # запуск краулера

if __name__ == '__main__':
    """Запуск асинхронной функции main."""
    asyncio.run(main())
```