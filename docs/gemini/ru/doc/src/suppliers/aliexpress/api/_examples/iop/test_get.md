# Модуль `hypotez/src/suppliers/aliexpress/api/_examples/iop/test_get.py`

## Обзор

Этот модуль содержит пример использования API `iop` для получения данных с AliExpress. Он демонстрирует создание запроса GET, выполнение запроса и обработку ответа.

## Функции

### `IopClient`

**Описание**: Класс `IopClient` представляет собой клиента для работы с API `iop`.

**Параметры**:
- `gateway_url` (str): URL шлюза API.
- `appkey` (str): Ключ приложения.
- `appSecret` (str): Секрет приложения.

**Возвращает**:
- `IopClient`: Объект клиента для взаимодействия с API `iop`.

### `IopRequest`

**Описание**: Класс `IopRequest` представляет собой запрос к API `iop`.

**Параметры**:
- `api_method` (str): Наименование метода API.
- `http_method` (str, optional): Метод HTTP (по умолчанию `POST`).

**Возвращает**:
- `IopRequest`: Объект запроса к API `iop`.

### `add_api_param`

**Описание**: Метод добавляет параметр к запросу.

**Параметры**:
- `param_name` (str): Наименование параметра.
- `param_value` (Any): Значение параметра.


**Возвращает**:
- `None`

### `set_simplify`

**Описание**: Метод устанавливает упрощенный режим обработки запроса.


**Возвращает**:
- `None`


### `execute`

**Описание**: Метод выполняет запрос к API `iop`.

**Параметры**:
- `request` (`IopRequest`): Объект запроса.
- `data` (str): данные для отправки.

**Возвращает**:
- `IopResponse`: Объект ответа.


## Примеры использования

### Создание клиента

```python
client = iop.IopClient(
    'https://api-pre.aliexpress.com/sync',
    '33505222',
    'e1fed6b34feb26aabc391d187732af93'
)
```

### Создание запроса GET

```python
request = iop.IopRequest(
    'aliexpress.logistics.redefining.getlogisticsselleraddresses', 'POST'
)
request.set_simplify()
request.add_api_param('seller_address_query', 'pickup')
```


### Выполнение запроса и обработка ответа

```python
response = client.execute(request, "50000001a27l15rndYBjw6PrtFFHPGZfy09k1Cp1bd8597fsduP0RStringNormalizery0jhF6FL")

print(response.type)
print(response.code)
print(response.message)
print(response.request_id)
print(response.body)
```

В примере показано получение и вывод различных атрибутов ответа, включая тип ответа, код, сообщение об ошибке, уникальный идентификатор запроса и полное тело ответа.


```
```
```
```
```