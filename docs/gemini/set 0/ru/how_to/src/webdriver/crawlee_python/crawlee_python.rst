Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код представляет класс `CrawleePython`, предназначенный для веб-скрапинга с использованием библиотеки Playwright.  Класс управляет настройкой, запуском и экспортом данных, полученных с заданных URL-адресов.  Он предоставляет методы для инициализации, настройки, запуска процесса сбора данных, экспорта результатов в JSON-файл и получения собранных данных.

Шаги выполнения
-------------------------
1. **Инициализация:** Класс `CrawleePython` инициализируется с параметрами:
   - `max_requests`: Максимальное количество запросов для каждого сайта.
   - `headless`: Флаг, указывающий, запущен ли браузер в режиме без отображения.
   - `browser_type`: Тип браузера (например, 'firefox').

2. **Настройка сканера (`setup_crawler`):**
   - Создается экземпляр класса `PlaywrightCrawler` с указанными параметрами.
   - Определяется обработчик запросов (`request_handler`).  В этом обработчике:
     - Выводится информация о текущей обрабатываемой ссылке.
     - Запрашиваются все ссылки на странице.
     - Извлекаются данные с помощью Playwright (URL, заголовок страницы, содержимое).
     - Данные сохраняются в хранилище данных.

3. **Запуск сканера (`run_crawler`):**
   - Запускается сканер с заданным списком URL-адресов.

4. **Экспорт данных (`export_data`):**
   - Экспортирует собранные данные в JSON-файл по указанному пути.

5. **Получение данных (`get_data`):**
   - Возвращает собранные данные в виде словаря.

6. **Главный метод (`run`):**
   - Вызывает `setup_crawler` для настройки сканера.
   - Вызывает `run_crawler` для запуска сканера с заданными URL-адресами.
   - Вызывает `export_data` для сохранения результатов в файл.
   - Вызывает `get_data` для получения собранных данных.
   - Выводит собранные данные в лог.


Пример использования
-------------------------
.. code-block:: python

    import asyncio
    from hypotez.src.webdriver.crawlee_python.crawlee_python import CrawleePython
    from pathlib import Path
    from src import gs # Подключаем необходимый модуль


    async def main():
        experiment = CrawleePython(max_requests=5, headless=False, browser_type='firefox')
        await experiment.run(['https://ksp.co.il'])

    asyncio.run(main())