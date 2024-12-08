# Модуль для работы с запросами к API

## Обзор

Этот модуль предоставляет инструменты для отправки и обработки запросов к внешним API.  Он позволяет задавать параметры запроса, обрабатывать ответы и управлять возможными ошибками.

## Функции

### `send_request`

**Описание**: Отправляет запрос к указанному API.

**Параметры**:
- `url` (str): URL запроса.
- `method` (str, optional): Метод запроса (GET, POST, PUT, DELETE, etc.). По умолчанию GET.
- `params` (dict, optional): Параметры запроса. По умолчанию пустой словарь.
- `headers` (dict, optional): Заголовки запроса. По умолчанию пустой словарь.
- `timeout` (float, optional): Время ожидания запроса в секундах. По умолчанию 10 секунд.

**Возвращает**:
- `Response` (object): Объект ответа от API.
- `None` (None): В случае ошибки при отправке запроса.

**Вызывает исключения**:
- `RequestError`: При возникновении проблем с отправкой запроса.
- `APIError`: При получении некорректного ответа от API.


**Пример использования**:

```python
from api_client import send_request

url = "https://api.example.com/data"
params = {"param1": "value1", "param2": 2}
response = send_request(url, method="POST", params=params, headers={"Content-Type": "application/json"})

if response:
    print(response.status_code)
    print(response.content)
else:
    print("Ошибка отправки запроса")
```

### `process_response`

**Описание**: Обрабатывает ответ от API, извлекает данные и возвращает результат.

**Параметры**:
- `response` (Response): Объект ответа от API.

**Возвращает**:
- `dict`: Словарь с данными из ответа.
- `None`: В случае ошибки при обработке ответа.

**Вызывает исключения**:
- `APIError`: При возникновении проблем с десериализацией данных.


**Пример использования**:

```python
from api_client import process_response
from api_client import send_request

url = "https://api.example.com/data"
response = send_request(url)

if response:
    data = process_response(response)
    if data:
        print(data)
    else:
        print("Ошибка обработки ответа")
else:
   print("Ошибка отправки запроса")
```

##  Исключения

### `RequestError`

**Описание**:  Возникает при проблемах с отправкой запроса.

**Параметры**:
- `message` (str): Сообщение об ошибке.

### `APIError`

**Описание**: Возникает при некорректном ответе от API.

**Параметры**:
- `status_code` (int): Код состояния ответа.
- `message` (str): Сообщение об ошибке.


```
```