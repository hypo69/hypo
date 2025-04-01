# Модуль для обработки статуса ответа

## Обзор

Модуль `raise_for_status.py` предназначен для проверки статуса HTTP-ответа и генерации исключения, если статус указывает на ошибку. Он используется для обработки ответов от API, чтобы убедиться, что запросы были успешно обработаны.

## Подробнее

Этот модуль содержит функцию `raise_for_status`, которая проверяет, успешен ли HTTP-ответ. Если ответ не успешен (т.е. статус код не 2xx), функция пытается извлечь сообщение об ошибке из тела ответа (если это JSON) или возвращает текстовое содержимое ответа. Затем генерируется исключение `ResponseStatusError` с соответствующим сообщением.

## Функции

### `raise_for_status`

```python
async def raise_for_status(response: Union[StreamResponse, ClientResponse], message: str = None) -> None:
    """
    Проверяет статус HTTP-ответа и вызывает исключение, если ответ не успешен.

    Args:
        response (Union[StreamResponse, ClientResponse]): Объект ответа, который может быть `StreamResponse` или `ClientResponse`.
        message (str, optional): Сообщение об ошибке. По умолчанию `None`.

    Returns:
        None

    Raises:
        ResponseStatusError: Если статус ответа не является успешным (не 2xx).

    """
```

**Назначение**: Проверка статуса HTTP-ответа и вызов исключения `ResponseStatusError` в случае неудачи.

**Параметры**:
- `response` (Union[StreamResponse, ClientResponse]): Объект ответа, который может быть типа `StreamResponse` или `ClientResponse` из библиотеки `aiohttp`.
- `message` (str, optional): Необязательное сообщение об ошибке, которое может быть передано. По умолчанию `None`.

**Возвращает**:
- `None`: Функция ничего не возвращает, но вызывает исключение, если ответ не успешен.

**Вызывает исключения**:
- `ResponseStatusError`: Вызывается, если статус ответа не является успешным (не 2xx).

**Как работает функция**:

1. **Проверка статуса**:
   - Проверяется, является ли статус ответа успешным (`response.ok`). Если это так, функция завершается без каких-либо действий.

2. **Обработка ошибок**:
   - Если статус ответа не успешен, функция пытается извлечь сообщение об ошибке из тела ответа.

3. **Определение типа контента**:
   - Определяется тип контента ответа (`content_type`) из заголовков ответа.

4. **Обработка JSON-ответа**:
   - Если тип контента начинается с `application/json`, функция пытается десериализовать JSON-ответ и извлечь сообщение об ошибке из полей `error` или `message`.

5. **Обработка не-JSON-ответа**:
   - Если не удается извлечь сообщение об ошибке из JSON-ответа или если ответ не является JSON, функция пытается получить текстовое содержимое ответа.
   - Проверяется, является ли ответ HTML-страницей, и устанавливает сообщение об ошибке в `HTML content`, если это так.

6. **Вызов исключения**:
   - Вызывается исключение `ResponseStatusError` с сообщением об ошибке, включающим статус ответа и извлеченное сообщение.

**Внутренние функции**: Нет

**ASCII flowchart**:

```
    Проверка статуса ответа (response.ok)
    |
    Успешно?
    |
    Нет -- Определение типа контента (content_type)
    |
    JSON?
    |
    Да -- Извлечение сообщения об ошибке из JSON (data.get("error", data.get("message", message)))
    |                                                                                                     
    Нет -- Получение текстового содержимого (response.text()) и проверка HTML
    |
    Вызов исключения ResponseStatusError(f"Response {response.status}: {message}")
```

**Примеры**:

Пример 1: Успешный ответ

```python
from aiohttp import ClientResponse
from unittest.mock import AsyncMock
import pytest
from src.endpoints.gpt4free.g4f.Provider.hf_space.raise_for_status import raise_for_status
from ...errors import ResponseStatusError

@pytest.mark.asyncio
async def test_raise_for_status_ok():
    response = AsyncMock(spec=ClientResponse)
    response.ok = True
    await raise_for_status(response)
    assert True  # Если выполнение дошло сюда, значит исключение не было вызвано

```

Пример 2: Ошибка в JSON-ответе

```python
from aiohttp import ClientResponse
from unittest.mock import AsyncMock
import pytest
from src.endpoints.gpt4free.g4f.Provider.hf_space.raise_for_status import raise_for_status
from ...errors import ResponseStatusError

@pytest.mark.asyncio
async def test_raise_for_status_json_error():
    response = AsyncMock(spec=ClientResponse)
    response.ok = False
    response.headers = {"content-type": "application/json"}
    response.json.return_value = {"error": "Test error message"}
    with pytest.raises(ResponseStatusError) as ex:
        await raise_for_status(response)
    assert "Test error message" in str(ex.value)
```

Пример 3: HTML-ответ с ошибкой

```python
from aiohttp import ClientResponse
from unittest.mock import AsyncMock
import pytest
from src.endpoints.gpt4free.g4f.Provider.hf_space.raise_for_status import raise_for_status
from ...errors import ResponseStatusError

@pytest.mark.asyncio
async def test_raise_for_status_html_content():
    response = AsyncMock(spec=ClientResponse)
    response.ok = False
    response.headers = {"content-type": "text/html"}
    response.text.return_value = "<!DOCTYPE html><html><body><h1>Error</h1></body></html>"
    with pytest.raises(ResponseStatusError) as ex:
        await raise_for_status(response)
    assert "HTML content" in str(ex.value)