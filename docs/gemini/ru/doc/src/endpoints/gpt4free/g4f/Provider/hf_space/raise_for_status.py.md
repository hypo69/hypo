# Модуль для обработки статуса ответа

## Обзор

Модуль предназначен для проверки статуса HTTP-ответа и генерации исключения `ResponseStatusError` в случае, если ответ не является успешным (т.е. `response.ok` возвращает `False`). Он анализирует тип контента ответа (`content-type`) и пытается извлечь сообщение об ошибке из JSON-ответа, если это возможно. В противном случае, он извлекает текст ответа и использует его в качестве сообщения об ошибке.

## Подробней

Этот модуль важен для обработки ошибок, связанных с HTTP-запросами, и предоставляет информацию о статусе и содержании ответа в случае неудачи. Он используется для обеспечения надежной обработки API-ответов, особенно при работе с JSON-форматом данных.

## Функции

### `raise_for_status`

```python
async def raise_for_status(response: Union[StreamResponse, ClientResponse], message: str = None) -> None:
    """
    Проверяет статус HTTP-ответа и вызывает исключение в случае ошибки.

    Args:
        response (Union[StreamResponse, ClientResponse]): Объект ответа, который может быть `StreamResponse` или `ClientResponse` из `aiohttp`.
        message (str, optional): Дополнительное сообщение об ошибке. По умолчанию `None`.

    Raises:
        ResponseStatusError: Если статус ответа не `200 OK`.

    Как работает функция:
    1. Проверяет, является ли ответ успешным (`response.ok`). Если да, функция завершается.
    2. Получает тип контента (`content-type`) из заголовков ответа.
    3. Если тип контента начинается с `application/json`, пытается извлечь сообщение об ошибке из JSON-ответа.
    4. Если не удается извлечь сообщение из JSON или тип контента не JSON, извлекает текст ответа.
    5. Если тип контента указывает на HTML или текст начинается с "<!DOCTYPE", присваивает сообщению значение "HTML content", иначе использует текст ответа.
    6. Генерирует исключение `ResponseStatusError` с сообщением, включающим статус ответа и сообщение об ошибке.
    """
```

**Как работает функция**:

```ascii
Проверка статуса ответа --> Извлечение типа контента --> Анализ JSON (если применимо) --> Извлечение текста ответа (если необходимо) --> Генерация исключения (если ответ не успешен)
```

```ascii
A -- Является ли ответ "OK"?
|   Да: Конец
|   Нет: B
B -- Получение Content-Type
|
C -- Content-Type начинается с "application/json"?
|   Да: D
|   Нет: E
D -- Попытка извлечения JSON-данных и сообщения об ошибке
|
E -- Получение текста ответа
|
F -- Content-Type начинается с "text/html" или текст начинается с "<!DOCTYPE"?
|   Да: G
|   Нет: H
G -- Сообщение = "HTML content"
|
H -- Сообщение = текст ответа
|
I -- Вызов ResponseStatusError с сообщением об ошибке и статусом
```

**Примеры**:

```python
# Пример успешного ответа
response = StreamResponse()
response.status = 200
await raise_for_status(response)  # Ничего не произойдет

# Пример ответа с ошибкой и JSON-контентом
response = StreamResponse()
response.status = 400
response.headers["content-type"] = "application/json"
response._body = b'{"error": "Bad Request"}'
try:
    await raise_for_status(response)
except ResponseStatusError as ex:
    print(ex)  # Вывод: Response 400: Bad Request

# Пример ответа с ошибкой и HTML-контентом
response = StreamResponse()
response.status = 500
response.headers["content-type"] = "text/html"
response._body = b'<!DOCTYPE html><html><body><h1>Internal Server Error</h1></body></html>'
try:
    await raise_for_status(response)
except ResponseStatusError as ex:
    print(ex)  # Вывод: Response 500: HTML content
```