# `main.py`

## Обзор

Этот файл содержит основной код для запуска FastAPI приложения, которое предоставляет API для чата с использованием модели Google Gemini, а также для загрузки локализованных ресурсов. Приложение также предоставляет статический контент из директории `templates`.

## Содержание

- [Обзор](#обзор)
- [Импорты](#импорты)
- [Конфигурация](#конфигурация)
- [Модели](#модели)
- [Переменные](#переменные)
- [Маршруты](#маршруты)
    - [`root`](#root)
    - [`chat`](#chat)
    - [`locales`](#locales)
- [Функции](#функции)
    - [`get_locale_file`](#get_locale_file)
- [Запуск сервера](#запуск-сервера)

## Импорты

```python
from __future__ import annotations
import sys
from pathlib import Path
from types import SimpleNamespace
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import uvicorn
import json

import header
from src import gs
from src.logger import logger
from src.ai import GoogleGenerativeAI
```

## Конфигурация

```python
base_path: Path = gs.path.endpoints / 'hypo69' / 'desktop_assistant'
templates_path : Path = base_path / 'templates'
locales_path: Path = base_path / 'translations'

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

Здесь определяются пути к каталогам `templates` и `translations`, создается экземпляр FastAPI, и настраивается CORS для разрешения запросов с любых источников.

## Модели

### `ChatRequest`

```python
class ChatRequest(BaseModel):
    message: str
```

**Описание**: Модель данных для запроса чата, содержащая поле `message` типа `str`.

**Параметры**:
- `message` (str): Сообщение для чата.

## Переменные

```python
model: GoogleGenerativeAI | None = None
api_key:str = gs.credentials.gemini.games
system_instruction:str = ""
```

- `model` (GoogleGenerativeAI | None): Экземпляр модели Google Generative AI, инициализируется как `None`.
- `api_key` (str): API ключ для доступа к Google Gemini.
- `system_instruction` (str): Системная инструкция для модели.

## Маршруты

### `root`

```python
@app.get("/", response_class=HTMLResponse)
async def root():
    """
    Args:

    Returns:
        HTMLResponse: HTML-страница из index.html.

    Raises:
        HTTPException: В случае ошибки при чтении HTML или если файл не найден.
    """
    try:
        index_file =  templates_path /  'index.html'
        if not index_file.exists():
            raise FileNotFoundError(f"Could not find index.html at path: {index_file}")
        html_content = index_file.read_text(encoding="utf-8")
        return HTMLResponse(content=html_content)
    except Exception as ex:
        logger.error(f"Error in root: {ex}")
        raise HTTPException(status_code=500, detail=f"Error reading templates: {str(ex)}")
```

**Описание**: Обрабатывает GET-запрос к корневому пути `/`, возвращает содержимое файла `index.html` в качестве HTML-ответа.

**Возвращает**:
- `HTMLResponse`: HTML-страница.

**Вызывает исключения**:
- `HTTPException`: В случае ошибки при чтении HTML или если файл не найден.

### `chat`

```python
@app.post("/api/chat")
async def chat(request: ChatRequest):
    """
    Args:
        request (ChatRequest): Запрос чата, содержащий сообщение.

    Returns:
        dict: Ответ модели Gemini.

    Raises:
        HTTPException: В случае ошибки при обращении к модели.
    """
    global model
    try:
        if not model:
            model = GoogleGenerativeAI(api_key=api_key, model_name='gemini-2.0-flash-exp')
        response = await model.chat(request.message)
        return {"response": response}
    except Exception as ex:
        logger.error(f"Error in chat: {ex}")
        raise HTTPException(status_code=500, detail=str(ex))
```

**Описание**: Обрабатывает POST-запрос к пути `/api/chat`, принимает сообщение пользователя, отправляет его в модель Gemini и возвращает ответ.

**Параметры**:
- `request` (ChatRequest): Запрос чата, содержащий сообщение.

**Возвращает**:
- `dict`: Ответ модели Gemini.

**Вызывает исключения**:
- `HTTPException`: В случае ошибки при обращении к модели.

### `locales`

```python
@app.get("/locales/{lang}.json")
async def locales(lang:str):
    """
    Args:
        lang (str): Языковой код для загрузки локализации.

    Returns:
        dict: Локализация.

    Raises:
         HTTPException: В случае ошибки при загрузки файла локали или не нахождения файла.
    """
    return get_locale_file(lang)
```

**Описание**: Обрабатывает GET-запрос к пути `/locales/{lang}.json`, возвращает файл локализации для указанного языка.

**Параметры**:
- `lang` (str): Языковой код для загрузки локализации.

**Возвращает**:
- `dict`: Локализация.

**Вызывает исключения**:
- `HTTPException`: В случае ошибки при загрузки файла локали или не нахождения файла.

## Функции

### `get_locale_file`

```python
def get_locale_file(lang: str):
    """
    Args:
        lang (str): Языковой код.

    Returns:
        dict: Данные локализации.

    Raises:
        HTTPException: В случае ошибки при чтении файла локализации.
    """
    locale_file = locales_path / f'{lang}.json'
    try:
        with open(locale_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError as ex:
        logger.error(f"Error reading locale: {ex}")
        raise HTTPException(status_code=404, detail="Locale not found")
    except json.JSONDecodeError as ex:
        logger.error(f"Error decoding json: {ex}")
        raise HTTPException(status_code=500, detail="Invalid locale file")
    except Exception as ex:
        logger.error(f"Error reading locale: {ex}")
        raise HTTPException(status_code=500, detail="Error reading locales")
```

**Описание**: Загружает файл локализации для указанного языка.

**Параметры**:
- `lang` (str): Языковой код.

**Возвращает**:
- `dict`: Данные локализации.

**Вызывает исключения**:
- `HTTPException`: В случае ошибки при чтении файла локализации, не нахождения файла или не верного формата файла.

## Запуск сервера

```python
# Local server execution
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
```

Запускает локальный сервер uvicorn на хосте `127.0.0.1` и порту `8000`.