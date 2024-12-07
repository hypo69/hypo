Как использовать класс CrawleePython для веб-скрейпинга
==========================================================================================

Описание
-------------------------
Класс `CrawleePython` используется для выполнения задач веб-скрейпинга с помощью библиотеки `crawlee` и Playwright. Он предоставляет методы для настройки, запуска и обработки результатов процесса сбора данных.  Класс обрабатывает запросы, извлекает данные с веб-страниц и сохраняет результаты в JSON-файл.  Он поддерживает асинхронное выполнение для повышения эффективности.

Шаги выполнения
-------------------------
1. **Инициализация:** Создайте экземпляр класса `CrawleePython`, передавая необходимые параметры, такие как `max_requests` (максимальное количество запросов), `headless` (запуск браузера без графического интерфейса), и `browser_type` (тип браузера).

2. **Настройка краулера:** Вызовите метод `setup_crawler`. Этот метод настраивает обработчик запросов, который определяет, как обрабатывать каждый запрос.  Обработчик извлекает необходимые данные с веб-страниц (например, заголовки, рейтинги и ссылки).

3. **Запуск краулера:** Вызовите метод `run_crawler`, передав список начальных URL-адресов для сбора данных.

4. **Экспорт данных:** Вызовите метод `export_data`, передав путь к файлу, в который необходимо сохранить собранные данные в формате JSON.

5. **Получение данных:** Вызовите метод `get_data` для получения собранных данных в виде словаря.

6. **Основной метод запуска (run):** Метод `run` объединяет шаги 1-5, обеспечивая запуск, настройку, сбор данных и экспорт результатов.

Пример использования
-------------------------
.. code-block:: python

    import asyncio
    from crawlee import PlaywrightCrawler
    from your_module import CrawleePython

    async def main():
        crawler = CrawleePython(max_requests=10, headless=True, browser_type='chromium')
        await crawler.setup_crawler()
        initial_urls = ['https://news.ycombinator.com/']
        await crawler.run_crawler(initial_urls)
        await crawler.export_data('data.json')
        data = await crawler.get_data()
        print(data)

    asyncio.run(main())