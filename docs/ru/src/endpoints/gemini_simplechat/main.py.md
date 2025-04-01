# Модуль для простого чата Gemini

## Обзор

Этот модуль предоставляет простой API для взаимодействия с моделью Google Gemini AI. Он включает в себя FastAPI приложение с поддержкой CORS, которое позволяет отправлять запросы чата и получать ответы от модели Gemini.

## Подробнее

Модуль использует FastAPI для создания API, который принимает текстовые запросы и отправляет их в модель Google Gemini AI. Ответ модели возвращается клиенту. Конфигурация API, такая как разрешенные домены и заголовки, настраивается через параметры CORS. Для обработки запросов используется модель `GoogleGenerativeAI`, которая инициализируется с использованием ключа API и имени модели из настроек, а также системной инструкции.

## Классы

### `ChatRequest`

**Описание**: Модель запроса для чата, определяющая структуру входящих сообщений.

**Атрибуты**:
- `message` (str): Текст сообщения, отправляемого в чат.

## Функции

### `root`

```python
async def root() -> HTMLResponse:
    """
    Возвращает HTML-контент главной страницы.

    Returns:
        HTMLResponse: HTML-контент главной страницы.

    Raises:
        HTTPException: Если возникает ошибка при чтении шаблона.

    Example:
        >>> response = await root()
        >>> print(response.status_code)
        200
    """
```

**Назначение**: Функция возвращает HTML-контент главной страницы для FastAPI приложения.

**Как работает функция**:

1.  **Чтение HTML-файла**: Пытается прочитать содержимое HTML-файла, путь к которому берется из конфигурации (`gs.fast_api.index_path`).
2.  **Возврат HTMLResponse**: Если чтение файла прошло успешно, возвращает `HTMLResponse` с содержимым файла.
3.  **Обработка исключений**: Если во время чтения файла возникает исключение, перехватывает его и возбуждает `HTTPException` с кодом состояния 500 и детальным сообщением об ошибке.

**ASCII flowchart**:

```
Чтение HTML-файла (Path(...).read_text()) --> Успешно?
  |
  Да: --> Возврат HTMLResponse
  |
  Нет: --> Обработка исключения --> Возврат HTTPException
```

**Примеры**:

```python
from fastapi.responses import HTMLResponse
from fastapi import HTTPException
from pathlib import Path
from types import SimpleNamespace

# Mock-объекты для имитации конфигурации и файла
class MockGS:
    class fast_api:
        index_path = "index.html"
        host = "127.0.0.1"
        port = "8000"

gs = MockGS()

__root__ = Path(".")  # Укажите текущую директорию или путь к вашему проекту

# Создаем фиктивный HTML-файл для чтения
with open("index.html", "w", encoding="utf-8") as f:
    f.write("<html><body><h1>Hello, world!</h1></body></html>")

async def test_root():
    try:
        response = await root()
        assert isinstance(response, HTMLResponse)
        assert response.status_code == 200
        content = str(response.body, encoding='utf-8')
        assert "Hello, world!" in content
    except HTTPException as ex:
        assert False, f"HTTPException был вызван: {ex.detail}"
    finally:
        # Удаляем созданный файл
        Path("index.html").unlink()

# Запускаем тест
import asyncio
asyncio.run(test_root())
```

### `chat`

```python
async def chat(request: ChatRequest) -> dict:
    """
    Обрабатывает запрос чата и возвращает ответ от модели Gemini.

    Args:
        request (ChatRequest): Запрос чата, содержащий сообщение.

    Returns:
        dict: Ответ от модели Gemini.

    Raises:
        HTTPException: Если возникает ошибка во время обработки запроса.

    Example:
        >>> request = ChatRequest(message="Hello")
        >>> response = await chat(request)
        >>> print(response)
        {'response': 'Some response from Gemini'}
    """
```

**Назначение**: Функция обрабатывает POST-запросы к эндпоинту `/api/chat`. Она принимает сообщение от клиента, отправляет его в модель Gemini AI и возвращает ответ.

**Как работает функция**:

1.  **Прием запроса**: Функция принимает объект `ChatRequest`, содержащий сообщение.
2.  **Отправка сообщения в модель**: Использует глобальный экземпляр модели `GoogleGenerativeAI` для отправки сообщения в чат.
3.  **Получение ответа**: Получает ответ от модели Gemini.
4.  **Возврат ответа**: Возвращает ответ в формате JSON.
5.  **Обработка исключений**: Если во время обработки запроса возникает исключение, перехватывает его, логирует ошибку и возбуждает `HTTPException` с кодом состояния 500 и детальным сообщением об ошибке.

**ASCII flowchart**:

```
Прием запроса (ChatRequest) --> Отправка сообщения в модель (model.chat(request.message)) --> Получение ответа
  |
  Успешно?
  |
  Да: --> Возврат ответа
  |
  Нет: --> Обработка исключения --> Логирование ошибки --> Возврат HTTPException
```

**Примеры**:

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pytest
from unittest.mock import AsyncMock

# Модель запроса для чата
class ChatRequest(BaseModel):
    message: str

# Mock-объект для имитации модели GoogleGenerativeAI
class MockGoogleGenerativeAI:
    async def chat(self, message: str) -> str:
        return f"Response for: {message}"

# Создаем FastAPI приложение
app = FastAPI()

# Определяем эндпоинт /api/chat
@app.post("/api/chat")
async def chat(request: ChatRequest):
    global model
    try:
        response = await model.chat(request.message)
        return {"response": response}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))

# Фикстура для подмены модели GoogleGenerativeAI
@pytest.fixture
def mock_google_generative_ai(monkeypatch):
    mock = MockGoogleGenerativeAI()
    monkeypatch.setattr("main.model", mock)
    return mock

# Тест для эндпоинта /api/chat
@pytest.mark.asyncio
async def test_chat_endpoint(mock_google_generative_ai):
    from fastapi.testclient import TestClient
    client = TestClient(app)
    message = "Test message"
    response = client.post("/api/chat", json={"message": message})
    assert response.status_code == 200
    assert response.json() == {"response": f"Response for: {message}"}
```

## Локальный запуск сервера

В блоке `if __name__ == "__main__":` код запускает Uvicorn сервер, используя хост и порт, указанные в конфигурации (`gs.fast_api`). Это позволяет запускать API локально для тестирования и разработки.