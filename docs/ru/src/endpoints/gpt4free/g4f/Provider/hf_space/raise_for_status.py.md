# Модуль для обработки статуса ответа

## Обзор

Модуль `raise_for_status` предназначен для проверки статуса HTTP-ответа и выброса исключения в случае, если ответ не успешен (не `200 OK`). Он обрабатывает различные типы контента, такие как JSON и HTML, чтобы предоставить более информативное сообщение об ошибке.

## Подробней

Этот модуль используется для централизованной обработки ошибок, возникающих при выполнении HTTP-запросов. Он проверяет статус ответа и, если статус указывает на ошибку, извлекает детали ошибки из тела ответа (если это возможно, например, для JSON-ответов) или предоставляет общее описание ошибки. Это позволяет упростить обработку ошибок в других частях кодовой базы, где выполняются HTTP-запросы.

## Функции

### `raise_for_status`

```python
async def raise_for_status(response: Union[StreamResponse, ClientResponse], message: str = None) -> None:
    """Проверяет статус HTTP-ответа и выбрасывает исключение, если ответ не успешен.

    Args:
        response (Union[StreamResponse, ClientResponse]): Объект ответа, который нужно проверить. Может быть `StreamResponse` или `ClientResponse` из `aiohttp`.
        message (str, optional): Пользовательское сообщение об ошибке. По умолчанию `None`.

    Returns:
        None: Функция ничего не возвращает, если ответ успешен.

    Raises:
        ResponseStatusError: Выбрасывается, если статус ответа не `200 OK`. Содержит сообщение об ошибке, извлеченное из ответа или предоставленное пользователем.
    """
```

**Как работает функция**:

1.  **Проверка статуса ответа**: Функция начинает с проверки, является ли ответ успешным (`response.ok`). Если ответ успешен, функция немедленно завершается, ничего не возвращая.

2.  **Обработка JSON-ответов**: Если ответ не успешен, функция пытается определить тип контента ответа. Если тип контента – `application/json`, функция пытается извлечь сообщение об ошибке из JSON-тела ответа.

3.  **Извлечение сообщения из JSON**: Если тип контента – `application/json`, функция пытается проанализировать JSON-тело ответа и извлечь сообщение об ошибке из полей `error` или `message`. Если извлечение удается, сообщение об ошибке обновляется.

4.  **Обработка текстовых/HTML-ответов**: Если тип контента не `application/json` или не удалось извлечь сообщение из JSON, функция пытается получить текстовое содержимое ответа.  Если тип контента – `text/html` или текст начинается с `<!DOCTYPE`, сообщение устанавливается как `"HTML content"`; в противном случае, сообщение устанавливается как текст ответа.

5.  **Выброс исключения**: Если ответ не успешен, функция создает исключение `ResponseStatusError` с сообщением об ошибке, которое было извлечено из тела ответа или предоставлено пользователем.

```ascii
Проверка статуса ответа (response.ok)
│
├─── True: Завершение функции
│
└─── False: Определение типа контента
    │
    ├─── content_type.startswith("application/json")
    │   │
    │   ├─── True: Попытка извлечения сообщения об ошибке из JSON
    │   │   │
    │   │   └─── Успешно: Обновление сообщения об ошибке
    │   │   │
    │   │   └─── Неуспешно: Пропуск обработки JSON
    │   │
    │   └─── False: Проверка на HTML или извлечение текста
    │       │
    │       ├─── content_type.startswith("text/html") или text.startswith("<!DOCTYPE")
    │       │   │
    │       │   ├─── True: Сообщение = "HTML content"
    │       │   │
    │       │   └─── False: Сообщение = text
    │       │
    │       └─── Выброс исключения ResponseStatusError с сообщением об ошибке
    │
    └─── Выброс исключения ResponseStatusError с сообщением об ошибке
```

**Примеры**:

```python
import aiohttp
from src.endpoints.gpt4free.g4f.Provider.hf_space.raise_for_status import raise_for_status

async def test_raise_for_status_ok():
    # Мокируем успешный ответ
    class MockResponse:
        def __init__(self):
            self.ok = True
            self.status = 200

    response = MockResponse()
    # Не должно быть исключения
    await raise_for_status(response)

async def test_raise_for_status_json_error():
    # Мокируем ошибочный ответ с JSON-сообщением об ошибке
    class MockResponse:
        def __init__(self):
            self.ok = False
            self.status = 400
            self.headers = {"content-type": "application/json"}

        async def json(self):
            return {"error": "Тестовая ошибка"}

    response = MockResponse()
    try:
        await raise_for_status(response)
    except ResponseStatusError as ex:
        print(f"Исключение: {ex}")

async def test_raise_for_status_html_error():
    # Мокируем ошибочный ответ с HTML-сообщением об ошибке
    class MockResponse:
        def __init__(self):
            self.ok = False
            self.status = 404
            self.headers = {"content-type": "text/html"}

        async def text(self):
            return "<!DOCTYPE html><html><body><h1>Страница не найдена</h1></body></html>"
        
        def get(self, param, param1):
            return ''

    response = MockResponse()
    try:
        await raise_for_status(response)
    except ResponseStatusError as ex:
        print(f"Исключение: {ex}")

async def test_raise_for_status_text_error():
    # Мокируем ошибочный ответ с текстовым сообщением об ошибке
    class MockResponse:
        def __init__(self):
            self.ok = False
            self.status = 500
            self.headers = {"content-type": "text/plain"}

        async def text(self):
            return "Внутренняя ошибка сервера"
        
        def get(self, param, param1):
            return ''
            

    response = MockResponse()
    try:
        await raise_for_status(response)
    except ResponseStatusError as ex:
        print(f"Исключение: {ex}")