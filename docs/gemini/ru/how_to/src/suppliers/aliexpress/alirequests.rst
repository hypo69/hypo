Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код реализует класс `AliRequests`, предназначенный для отправки HTTP-запросов к сайту AliExpress.  Класс загружает куки с диска, обновляет сессию и осуществляет GET-запросы, включая куки.  Ключевой функционал – загрузка и использование куки для аутентификации на сайте.  Также, присутствует функция для получения короткой аффилиатной ссылки.

Шаги выполнения
-------------------------
1. **Инициализация класса `AliRequests`**: Создается экземпляр класса `AliRequests`, опционально указывая имя драйвера браузера (`webdriver_for_cookies`), для загрузки куки.
2. **Загрузка куки**: Метод `_load_webdriver_cookies_file` загружает куки из файла на диске, используя `pickle`.  Путь к файлу формируется по заданному шаблону.  Он итерирует по списку куки и устанавливает их в `RequestsCookieJar`.  Обработка ошибок (например, `FileNotFoundError`) позволяет программе корректно завершаться.
3. **Обновление сессии**: Метод `_refresh_session_cookies` обновляет сессию, используя полученные куки.  Он отправляет GET-запрос на страницу AliExpress, для обновления сессии.  
4. **Обработка JSESSIONID**: Метод `_handle_session_id` обрабатывает куки `JSESSIONID` в ответе от сервера.  Если `JSESSIONID` найден, он обновляет `self.session_id` и обновляет куки `self.cookies_jar`.
5. **Отправка GET-запроса**: Метод `make_get_request` отправляет GET-запрос на заданный URL, используя текущие куки.  В случае успеха возвращает объект `requests.Response`, иначе - `False`.
6. **Получение короткой аффилиатной ссылки**: Метод `short_affiliate_link` формирует URL для генерации короткой аффилиатной ссылки и использует `make_get_request` для её получения.


Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.alirequests import AliRequests

    # Инициализация
    aliexpress_requests = AliRequests(webdriver_for_cookies='chrome')

    # Проверка загрузки куки
    if aliexpress_requests._load_webdriver_cookies_file():
        # Отправка запроса
        url = "https://www.aliexpress.com"  # Замените на нужный URL
        response = aliexpress_requests.make_get_request(url)

        if response:
            # Обработка ответа
            print(response.status_code)
            print(response.text)
        else:
            print("Ошибка при отправке запроса")


    # Получение короткой ссылки
    short_link_response = aliexpress_requests.short_affiliate_link("https://example.com")
    if short_link_response:
        print("Короткая ссылка:", short_link_response.url)
    else:
        print("Ошибка при получении короткой ссылки")