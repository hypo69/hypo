Как использовать функцию crawl_categories_async
========================================================================================

Описание
-------------------------
Функция `crawl_categories_async` асинхронно обходит категории на веб-сайте, рекурсивно собирая иерархическую структуру данных. Она принимает URL страницы, глубину обхода, драйвер Selenium, локатор для нахождения ссылок на категории, файл для сохранения данных и ID категории по умолчанию.  Результат – словарь, представляющий структуру категорий и их URL-адреса. Функция обрабатывает ошибки и предотвращает повторное сканирование уже посещенных ссылок.

Шаги выполнения
-------------------------
1. **Инициализация**: Проверяет, задан ли словарь `category`. Если нет, создаёт новый словарь с базовыми данными (URL, имя, словарь для данных PrestaShop, словарь для дочерних категорий).

2. **Проверка глубины**: Если глубина обхода достигла нуля, возвращает текущий словарь `category`.

3. **Загрузка страницы**: Загружает страницу по указанному `url` с помощью `driver.get(url)` и ожидает загрузки (`await asyncio.sleep(1)`).

4. **Поиск ссылок**: Находит ссылки на дочерние категории с помощью `driver.execute_locator(locator)`.  Проверяет, не пуст ли результат. Если список пуст, выводит ошибку и возвращает `category`.

5. **Рекурсивный вызов**: Для каждой найденной ссылки `link_url` и имени `name`  выполняется асинхронный рекурсивный вызов функции `crawl_categories_async` с уменьшенной глубиной.  Создается новый словарь `new_category` с URL, именем и данными PrestaShop для каждой найденной категории.  Включается проверка на дубликаты ссылок (`self._is_duplicate_url`).

6. **Обработка ошибок**: Если возникает ошибка во время обхода, записывается сообщение об ошибке в лог (`logger.error`) и возвращается текущий словарь `category`.

7. **Объединение результатов**: После асинхронного сбора данных от всех дочерних категорий, результаты объединяются в словарь `category`.

8. **Возврат результата**: Функция возвращает заполненный иерархический словарь `category`.

Пример использования
-------------------------
.. code-block:: python

    import asyncio
    from selenium import webdriver
    # ... (import other necessary modules)

    # ... (Initialization of driver and other variables)

    url = "https://your-website.com/categories"
    depth = 2
    driver = webdriver.Chrome()
    locator = "//a[@class='category-link']"  # Example locator
    dump_file = "categories.json"
    id_category_default = 123

    category_instance = Category(api_credentials)

    result = asyncio.run(category_instance.crawl_categories_async(url, depth, driver, locator, dump_file, id_category_default))

    # Print or process the 'result' dictionary (containing the hierarchical structure of categories)
    print(result)
    driver.quit()