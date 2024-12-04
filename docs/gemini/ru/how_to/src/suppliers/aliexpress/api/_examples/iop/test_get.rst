Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код демонстрирует использование библиотеки `iop` для отправки запроса к API AliExpress.  Код инициализирует клиент `IopClient`, создает запрос `IopRequest` с методом GET, добавляет параметры и выполняет запрос.  Затем он выводит тип ответа, код, сообщение об ошибке, идентификатор запроса и полное тело ответа.

Шаги выполнения
-------------------------
1. **Импорт необходимой библиотеки:** Код импортирует модуль `iop`.
2. **Инициализация клиента:**  Создает экземпляр класса `IopClient`, передавая URL API, ключ приложения (`appkey`) и секретный ключ приложения (`appSecret`).
3. **Создание запроса:** Создает объект `IopRequest`,  устанавливает тип запроса на `GET` (по умолчанию `POST`) и метод `aliexpress.logistics.redefining.getlogisticsselleraddresses`.  Устанавливает упрощенное форматирование (`request.set_simplify()`).
4. **Добавление параметров:**  Добавляет параметр `seller_address_query` со значением `pickup` к запросу.
5. **Выполнение запроса:** Выполняет запрос к API с помощью метода `client.execute()`, передавая объект запроса и  дополнительные данные `50000001a27l15rndYBjw6PrtFFHPGZfy09k1Cp1bd8597fsduP0RStringNormalizery0jhF6FL`.
6. **Обработка ответа:**  Извлекает и выводит тип ответа (`response.type`), код ответа (`response.code`), сообщение об ошибке (`response.message`), идентификатор запроса (`response.request_id`) и полное тело ответа (`response.body`).


Пример использования
-------------------------
.. code-block:: python

    import iop

    # Замените на ваши значения
    client = iop.IopClient('https://api-pre.aliexpress.com/sync', '33505222', 'e1fed6b34feb26aabc391d187732af93')

    request = iop.IopRequest('aliexpress.logistics.redefining.getlogisticsselleraddresses', 'GET')  # ВАЖНО! Установите метод GET
    request.set_simplify()
    request.add_api_param('seller_address_query', 'pickup')

    response = client.execute(request, "YOUR_ADDITIONAL_DATA")

    print(response.type)
    print(response.code)
    print(response.message)
    print(response.request_id)
    print(response.body)