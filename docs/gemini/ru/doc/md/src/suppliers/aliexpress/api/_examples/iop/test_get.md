# Модуль `hypotez/src/suppliers/aliexpress/api/_examples/iop/test_get.py`

## Обзор

Модуль `test_get.py` содержит пример использования библиотеки `iop` для отправки запроса GET к API AliExpress.  Он демонстрирует создание клиента, настройку запроса, выполнение запроса и обработку ответа.


## Функции

### `client`

**Описание**:  Создаёт экземпляр `IopClient` для взаимодействия с API AliExpress.

**Параметры**:
- `'https://api-pre.aliexpress.com/sync'` (str): URL API-шлюза.
- `'33505222'` (str): Ключ приложения (appkey).
- `'e1fed6b34feb26aabc391d187732af93'` (str): Секрет приложения (appSecret).

**Возвращает**:
- `IopClient`: Экземпляр класса `IopClient`.


### `request`

**Описание**: Создает экземпляр `IopRequest` для запроса данных о seller addresses.

**Параметры**:
- `'aliexpress.logistics.redefining.getlogisticsselleraddresses'` (str): Имя метода API.
- `'POST'` (str): Метод HTTP запроса.

**Возвращает**:
- `IopRequest`: Объект запроса `IopRequest`.



### `client.execute`

**Описание**: Выполняет запрос к API.

**Параметры**:
- `request`: `IopRequest`: Объект запроса.
- `"50000001a27l15rndYBjw6PrtFFHPGZfy09k1Cp1bd8597fsduP0RStringNormalizery0jhF6FL"` (str): Параметр запроса.


**Возвращает**:
- `IopResponse`: Объект ответа `IopResponse`.

**Вызывает исключения**:
- Любое исключение, которое может быть вызвано при выполнении запроса к API или в самой библиотеке `iop`.


### `print(response.type)`

**Описание**: Выводит тип ответа.

**Параметры**:
- `response`: `IopResponse`: Объект ответа.

**Возвращает**:
- Возвращаемое значение не определено.


### `print(response.code)`

**Описание**: Выводит код ответа.

**Параметры**:
- `response`: `IopResponse`: Объект ответа.

**Возвращает**:
- Возвращаемое значение не определено.


### `print(response.message)`

**Описание**: Выводит сообщение об ошибке (если ошибка произошла).

**Параметры**:
- `response`: `IopResponse`: Объект ответа.

**Возвращает**:
- Возвращаемое значение не определено.


### `print(response.request_id)`

**Описание**: Выводит уникальный идентификатор запроса.

**Параметры**:
- `response`: `IopResponse`: Объект ответа.

**Возвращает**:
- Возвращаемое значение не определено.


### `print(response.body)`

**Описание**: Выводит полное тело ответа.

**Параметры**:
- `response`: `IopResponse`: Объект ответа.

**Возвращает**:
- Возвращаемое значение не определено.