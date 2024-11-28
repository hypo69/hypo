Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код реализует класс `AliRequests`, предназначенный для отправки запросов на AliExpress с использованием библиотеки `requests`. Класс загружает куки из файла, обновляет сессию и позволяет делать GET-запросы с учетом куки.  Код также содержит метод для генерации коротких аффилированных ссылок.

Шаги выполнения
-------------------------
1. **Инициализация класса `AliRequests`:** Создается экземпляр класса `AliRequests`, принимая необязательный параметр `webdriver_for_cookies`, который определяет название драйвера для загрузки куки. Этот параметр указывает, откуда брать куки (например, для Chrome).

2. **Загрузка куки из файла:** Метод `_load_webdriver_cookies_file` загружает куки из файла, путь к которому вычисляется с помощью `gs.dir_cookies`. Этот метод ищет файл куки в определенной папке, а если его не находит, то записывает сообщение об ошибке в лог и возвращает `False`.

3. **Обновление сессии с куки:** Метод `_refresh_session_cookies` обновляет куки текущей сессии на основе загруженных данных.  Он отправляет GET-запрос на `https://portals.aliexpress.com` и обновляет куки сессии. Если куки не найдены, это не влияет на работу программы.

4. **Обработка JSESSIONID:** Метод `_handle_session_id` обрабатывает полученные куки, обновляя `session_id` и куки класса, если найден `JSESSIONID`. Если `JSESSIONID` не найден, записывается предупреждение в лог.

5. **Отправка GET-запроса:** Метод `make_get_request` отправляет GET-запрос на указанный `url` с использованием текущих куки.  Он проверяет статус ответа и если запрос успешен, обрабатывает полученные куки (`_handle_session_id`). В противном случае записывает ошибку в лог и возвращает `False`.

6. **Генерация короткой аффилированной ссылки:** Метод `short_affiliate_link` генерирует короткую аффилированную ссылку из исходного `link_url`. Он формирует URL для запроса к AliExpress и вызывает метод `make_get_request` для получения ответа.


Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.alirequests import AliRequests
    import gs  # Предполагается, что gs содержит необходимые настройки

    # Установите переменную gs.dir_cookies
    gs.dir_cookies = '/path/to/cookies/' 

    aliexpress_requests = AliRequests()

    # Проверка загрузки куки
    if aliexpress_requests._load_webdriver_cookies_file():
        url_to_request = "https://www.aliexpress.com"
        response = aliexpress_requests.make_get_request(url_to_request)

        if response:
            print(response.status_code)
            print(response.text)
        else:
            print("Ошибка при запросе.")


    short_link_result = aliexpress_requests.short_affiliate_link("https://www.example.com")
    if short_link_result:
        print(short_link_result.url)
    else:
        print("Ошибка при генерации короткой ссылки.")