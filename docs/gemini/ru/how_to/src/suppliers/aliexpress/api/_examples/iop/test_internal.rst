Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код взаимодействует с API iop, используя библиотеку `iop`. Он отправляет запрос на получение информации о товаре (itemId = 157432005) к API `https://api-pre.taobao.tw/rest`.  Код инициализирует клиент `IopClient`, создает `IopRequest` с методом GET, добавляет параметры `itemId` и `authDO`, выполняет запрос и выводит тип ответа, код ошибки, сообщение об ошибке, уникальный идентификатор запроса и полное содержимое ответа.  В конце выводится отметка времени.

Шаги выполнения
-------------------------
1. Импортирует необходимые библиотеки `iop` и `time`.
2. Инициализирует клиента `IopClient` с указанием URL API, `appKey` и `appSecret`.
3. Создает объект `IopRequest` для запроса к API с заданным методом GET и URL `/product/item/get`.
4. Добавляет параметры запроса (`itemId` и `authDO`) к объекту `IopRequest`.
5. Выполняет запрос к API с помощью метода `client.execute(request)`.
6. Выводит тип ответа (`response.type`).
7. Выводит код ответа (`response.code`).
8. Выводит сообщение об ошибке (`response.message`), если ошибка произошла.
9. Выводит уникальный идентификатор запроса (`response.request_id`).
10. Выводит полное содержимое ответа (`response.body`).
11. Выводит отметку времени в формате с миллисекундами.


Пример использования
-------------------------
.. code-block:: python

    import iop
    import time

    # ... (инициализация client как в примере) ...

    # пример использования, заменив значения по-требованию
    client = iop.IopClient('https://api-pre.taobao.tw/rest', '100240', 'hLeciS15d7UsmXKoND76sBVPpkzepxex')
    request = iop.IopRequest('/product/item/get', 'GET')
    request.add_api_param('itemId', '123456789')  # Замените на необходимый itemId
    request.add_api_param('authDO', '{\\"sellerId\\":2000000016002}') # Замените, если требуется


    response = client.execute(request)

    print(response.type)
    print(response.code)
    print(response.message)
    print(response.request_id)
    print(response.body)
    print(str(round(time.time())) + '000')