# Модуль `gemini_simplechat.main`

## Обзор

Модуль `gemini_simplechat.main` предоставляет простой чат, использующий модель Google Gemini для обработки и генерации ответов на входящие сообщения. Он включает в себя FastAPI приложение, настроенное для обработки запросов чата через HTTP endpoints.

## Подробней

Этот модуль служит отправной точкой для развертывания чат-бота на основе модели Gemini. Он определяет API endpoints для взаимодействия с чат-ботом, используя FastAPI для обработки HTTP запросов и ответов. Он включает в себя настройку CORS для обеспечения безопасного взаимодействия между клиентом и сервером, а также обработку ошибок и логирование. Расположение файла в проекте `hypotez` указывает на его роль в качестве основного интерфейса для взаимодействия с чат-ботом Gemini.

## Классы

### `ChatRequest`

**Описание**: Модель запроса чата, используемая для валидации и передачи входящих сообщений.

**Как работает класс**:
Класс `ChatRequest` наследуется от `BaseModel` библиотеки `pydantic` и определяет структуру входящего запроса чата. Он содержит одно поле `message`, которое представляет собой строку сообщения, отправленную пользователем. Pydantic автоматически выполняет валидацию типа данных для этого поля.

**Параметры**:
- `message` (str): Сообщение от пользователя.

**Примеры**:
```python
from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str

# Пример использования
request = ChatRequest(message="Привет, как дела?")
print(request.message)
```

## Функции

### `root`

```python
async def root():
    """
    Returns:
        HTMLResponse: Возвращает HTML-контент из файла index.html.

    Raises:
        HTTPException: Если происходит ошибка при чтении файла index.html.

    Example:
        >>> response = await root()
        >>> print(response.status_code)
        200
    """
```

**Описание**: Обрабатывает корневой GET запрос и возвращает HTML страницу.

**Как работает функция**:
Функция `root` является асинхронным обработчиком GET запросов к корневому пути ("/"). Она пытается прочитать содержимое HTML файла, путь к которому определен в конфигурации `gs.fast_api.index_path`. В случае успеха функция возвращает HTML контент в виде объекта `HTMLResponse`. Если при чтении файла возникает исключение, функция возбуждает исключение `HTTPException` с кодом состояния 500 и детальным сообщением об ошибке.

**Возвращает**:
- `HTMLResponse`: HTML-контент для отображения в браузере.

**Вызывает исключения**:
- `HTTPException`: Если не удается прочитать HTML файл.

**Примеры**:
```python
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pathlib import Path
from src import gs

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def root():
    try:
        html_content = Path( gs.fast_api.index_path).read_text(encoding="utf-8")
        return HTMLResponse(content=html_content)
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Error reading templates:{str(ex)}" )
```

### `chat`

```python
async def chat(request: ChatRequest):
    """
    Args:
        request (ChatRequest): Объект запроса, содержащий сообщение чата.

    Returns:
        dict: Ответ от модели чата в формате JSON.

    Raises:
        HTTPException: В случае ошибки при обработке запроса или получении ответа от модели.
    
    Example:
        >>> from fastapi.testclient import TestClient
        >>> from pydantic import BaseModel
        >>> class ChatRequest(BaseModel):
        ...     message: str
        >>> from fastapi import FastAPI
        >>> app = FastAPI()
        >>> @app.post("/api/chat")
        ... async def chat(request: ChatRequest):
        ...     return {"response": "test response"}
        >>> client = TestClient(app)
        >>> response = client.post("/api/chat", json={"message": "hello"})
        >>> assert response.status_code == 200
        >>> response.json()
        {'response': 'test response'}
    """
```

**Описание**: Обрабатывает POST запросы к endpoint `/api/chat` и возвращает ответ от модели Gemini.

**Как работает функция**:
Функция `chat` принимает объект `ChatRequest`, содержащий сообщение пользователя, и передает это сообщение модели `GoogleGenerativeAI` для получения ответа. Затем она возвращает ответ модели в формате JSON. В случае возникновения ошибки в процессе обработки запроса или получения ответа от модели, функция логирует ошибку и возвращает HTTP исключение с кодом состояния 500 и детальным описанием ошибки.

**Параметры**:
- `request` (ChatRequest): Объект запроса, содержащий сообщение чата.

**Возвращает**:
- `dict`: Ответ от модели чата в формате JSON.

**Вызывает исключения**:
- `HTTPException`: В случае ошибки при обработке запроса или получении ответа от модели.

**Примеры**:
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.ai import GoogleGenerativeAI
from src.logger import logger

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

# Предположим, что model - это экземпляр GoogleGenerativeAI, настроенный ранее
@app.post("/api/chat")
async def chat(request: ChatRequest):
    global model
    try:
        response = await model.chat(request.message)
        return {"response": response}
    except Exception as ex:
        logger.error(f"Error in chat: ",ex)
        raise HTTPException(status_code=500, detail=str(ex))