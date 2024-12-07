Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код осуществляет запрос к API iop для получения данных товара (itemId = 157432005).  Код использует библиотеку `iop` для взаимодействия с API, задает параметры запроса и обрабатывает ответ.  Он выводит тип ответа, код ошибки, сообщение об ошибке, уникальный идентификатор запроса и полное тело ответа.  Код также выводит отметку времени в миллисекундах.

Шаги выполнения
-------------------------
1. **Импортирование библиотек:** Код импортирует необходимые библиотеки `iop` и `time`.

2. **Инициализация клиента API:** Создается экземпляр класса `IopClient`, который связывается с API (`https://api-pre.taobao.tw/rest`), используя `appkey` и `appSecret`.

3. **Создание объекта запроса:** Создается объект `IopRequest` для запроса к API. Устанавливается метод запроса как `GET`.

4. **Добавление параметров запроса:** Методом `add_api_param` добавляются параметры `itemId` и `authDO` в запрос.

5. **Выполнение запроса:** Методом `execute` выполняется запрос к API.

6. **Обработка ответа:**  Код получает ответ от API и сохраняет его в переменной `response`.

7. **Вывод информации о статусе ответа:**  Выводятся тип ответа (`response.type`), код ошибки (`response.code`), сообщение об ошибке (`response.message`), уникальный идентификатор запроса (`response.request_id`) и полное тело ответа (`response.body`).

8. **Вывод отметки времени:** Выводится текущее время в миллисекундах.


Пример использования
-------------------------
.. code-block:: python

    import iop
    import time

    # параметры подключения к API
    gateway_url = 'https://api-pre.taobao.tw/rest'
    appkey = '100240'
    appSecret = 'hLeciS15d7UsmXKoND76sBVPpkzepxex'

    # инициализация клиента API
    client = iop.IopClient(gateway_url, appkey, appSecret)

    # параметры запроса
    item_id = '157432005'
    auth_do = '{"sellerId":2000000016002}'

    # создание запроса
    request = iop.IopRequest('/product/item/get', 'GET')
    request.add_api_param('itemId', item_id)
    request.add_api_param('authDO', auth_do)

    # выполнение запроса
    response = client.execute(request)

    # обработка ответа и вывод информации
    print(response.type)
    print(response.code)
    print(response.message)
    print(response.request_id)
    print(response.body)
    print(str(round(time.time())) + '000')