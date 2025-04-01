# Модуль для обработки статуса ответа

## Обзор

Модуль `raise_for_status.py` предназначен для проверки статуса HTTP-ответа и, в случае ошибки,
вызывает исключение `ResponseStatusError` с информативным сообщением об ошибке. Он обрабатывает как `StreamResponse`, так и `ClientResponse` объекты, проверяя, был ли запрос успешным. В случае неуспешного запроса, модуль пытается извлечь сообщение об ошибке из JSON-ответа, если таковой имеется, или возвращает содержимое ответа в виде текста.

## Подробней

Этот модуль играет важную роль в обработке ответов от API, позволяя централизованно обрабатывать ошибки и предоставлять детальную информацию о причинах сбоев. Он используется для обеспечения надежности и предсказуемости работы с внешними сервисами, логируя ошибки и уведомляя разработчиков о проблемах.

## Функции

### `raise_for_status`

```python
async def raise_for_status(response: Union[StreamResponse, ClientResponse], message: str = None) -> None:
    """Проверяет статус HTTP-ответа и вызывает исключение `ResponseStatusError` в случае ошибки.

    Args:
        response (Union[StreamResponse, ClientResponse]): Объект ответа, который может быть как `StreamResponse`, так и `ClientResponse`.
        message (str, optional): Пользовательское сообщение об ошибке. По умолчанию `None`.

    Returns:
        None: Функция ничего не возвращает в случае успешного выполнения.

    Raises:
        ResponseStatusError: Если статус ответа не OK (не 2xx), вызывается исключение с сообщением об ошибке.

    """
```

**Назначение**: Функция `raise_for_status` асинхронно проверяет, является ли HTTP-ответ успешным (код состояния 2xx). Если ответ не успешен, она пытается извлечь сообщение об ошибке из тела ответа (предпочтительно в формате JSON) и генерирует исключение `ResponseStatusError` с этим сообщением. Если извлечь сообщение об ошибке не удается, используется стандартное сообщение или содержимое ответа в виде текста.

**Параметры**:

-   `response` (Union[StreamResponse, ClientResponse]): Объект ответа, который может быть как `StreamResponse`, так и `ClientResponse`.
-   `message` (str, optional): Пользовательское сообщение об ошибке. По умолчанию `None`.

**Возвращает**:

-   `None`: Функция ничего не возвращает в случае успешного выполнения.

**Вызывает исключения**:

-   `ResponseStatusError`: Если статус ответа не OK (не 2xx), вызывается исключение с сообщением об ошибке.

**Как работает функция**:

1.  **Проверка статуса**: Сначала проверяется, является ли статус ответа успешным (`response.ok`). Если это так, функция завершается, ничего не делая.
2.  **Определение типа содержимого**: Если статус ответа не успешен, функция пытается определить тип содержимого ответа, чтобы извлечь сообщение об ошибке.
3.  **Обработка JSON**: Если тип содержимого - `application/json`, функция пытается извлечь данные JSON из ответа и получить сообщение об ошибке из полей `error` или `message`.
4.  **Обработка текста**: Если тип содержимого не `application/json` или извлечение JSON не удалось, функция пытается получить текст ответа и определить, является ли это HTML-контент.
5.  **Генерация исключения**: В конце, функция генерирует исключение `ResponseStatusError` с сообщением об ошибке, включающим статус ответа и извлеченное или сгенерированное сообщение.

```text
Проверка статуса ответа (response.ok)
│
├─── True: Выход из функции
│
└─── False:
     │
     Определение типа содержимого (content_type)
     │
     ├─── application/json: Попытка извлечения данных JSON и сообщения об ошибке
     │   │
     │   └─── Успешно: Извлечение сообщения об ошибке из JSON
     │   │
     │   └─── Ошибка: Обработка как обычный текст
     │
     └─── Другой тип: Получение текста ответа
         │
         └─── Определение HTML-контента
             │
             └─── True: Сообщение "HTML content"
             │
             └─── False: Использование текста ответа
     │
     Генерация исключения ResponseStatusError с сообщением об ошибке

```

**Примеры**:

1.  Успешный ответ:

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
    # Функция не должна вызывать исключение

```

2.  Неуспешный ответ с JSON:

```python

@pytest.mark.asyncio
async def test_raise_for_status_json_error():
    response = AsyncMock(spec=ClientResponse)
    response.ok = False
    response.headers = {"content-type": "application/json"}
    response.json.return_value = {"error": "Ошибка сервера"}
    with pytest.raises(ResponseStatusError) as ex:
        await raise_for_status(response)
    assert "Ошибка сервера" in str(ex.value)
```

3.  Неуспешный ответ с HTML:

```python
@pytest.mark.asyncio
async def test_raise_for_status_html_error():
    response = AsyncMock(spec=ClientResponse)
    response.ok = False
    response.headers = {"content-type": "text/html"}
    response.text.return_value = "<!DOCTYPE html><html><body><h1>Ошибка</h1></body></html>"
    with pytest.raises(ResponseStatusError) as ex:
        await raise_for_status(response)
    assert "HTML content" in str(ex.value)