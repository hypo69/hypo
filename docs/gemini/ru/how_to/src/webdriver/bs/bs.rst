Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код предоставляет класс `BS` для работы с HTML-контентом, загруженным из файла или URL. Он использует библиотеки `BeautifulSoup` и `lxml` для парсинга HTML и поиска элементов по XPath.  Код умеет загружать как локальные файлы, так и удаленные страницы.  Он содержит методы для получения HTML-контента и поиска элементов по разным селекторам (ID, CSS-классу, атрибуту).

Шаги выполнения
-------------------------
1. **Инициализация класса `BS`**:  Создается экземпляр класса `BS`, при необходимости передавая URL в конструктор. Это инициализирует переменную `html_content` для хранения содержимого.
2. **Получение HTML-контента (`get_url`):**
    - Метод `get_url` принимает строку `url`, представляющую собой путь к файлу или URL-адрес.
    - Он проверяет, является ли URL путем к файлу (начинается с 'file://'). Если да, то:
        - Очищает префикс 'file://'.
        - Парсит путь, пытаясь определить Windows-путь ('c:/...' или 'C:/...').
        - Проверяет существование файла.
        - Если файл существует, то открывает его, читает содержимое и сохраняет в `html_content`.
        - Возвращает True, если чтение прошло успешно, и логгирует ошибку в случае проблемы с файлом.
    - Если URL начинается с 'https://', обрабатывается как веб-страница, используя `requests.get()`.
    - В противном случае логгирует ошибку и возвращает `False`.
3. **Выполнение локейтора (`execute_locator`):**
    - Метод `execute_locator` принимает объект `locator` (представленный как `SimpleNamespace` или `dict`) и, опционально, URL.
    - При необходимости, если был передан URL, то загружает HTML-контент с помощью `get_url`.
    - Преобразует `BeautifulSoup` объект в `lxml` дерево `etree`.
    - Использует XPath для поиска элементов, основываясь на `locator.attribute`, `locator.by` и `locator.selector`.
    - Возвращает найденные элементы (`elements`).

Пример использования
-------------------------
.. code-block:: python

    from src.webdriver import Driver
    from hypotez.src.webdriver.bs import BS
    import pathlib

    # Предполагая, что у вас есть locator как SimpleNamespace
    locator = SimpleNamespace(attribute='my-element-id', by='id', selector='//div[@class="my-class"]')

    # Создаем экземпляр класса BS
    bs_parser = BS()

    # Загрузка HTML из файла
    file_path = pathlib.Path("path/to/your/file.html")
    if file_path.exists():
        success = bs_parser.get_url(f"file:///{file_path}")
        if success:
            elements = bs_parser.execute_locator(locator)
            if elements:
                for element in elements:
                    print(element.text)
            else:
                print("Элементов не найдено")
        else:
            print("Ошибка при загрузке файла.")
    else:
        print("Файл не найден.")

    # Загрузка HTML с URL
    url = "https://example.com"
    success = bs_parser.get_url(url)
    if success:
        elements = bs_parser.execute_locator(locator, url)
        # Обработка результатов поиска
        if elements:
            for element in elements:
                print(element.text)
        else:
            print("Элементов не найдено")
    else:
        print("Ошибка при загрузке страницы.")