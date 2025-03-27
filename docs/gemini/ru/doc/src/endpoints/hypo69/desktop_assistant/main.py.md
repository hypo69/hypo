# Название модуля: `main.py`

## Обзор

Этот модуль представляет собой основной файл FastAPI-приложения, которое выполняет роль десктопного ассистента. Он содержит API для обработки запросов чата с использованием модели Google Gemini, предоставляет статические файлы шаблонов и локализации, а также настраивает CORS для обеспечения взаимодействия с другими источниками.

## Подробней

Модуль расположен в `hypotez/src/endpoints/hypo69/desktop_assistant/main.py` и отвечает за создание и запуск FastAPI-приложения, которое служит интерфейсом для взаимодействия с Google Gemini AI. Он обрабатывает HTTP-запросы, предоставляет статические файлы (HTML, JSON) и обеспечивает возможность общения с AI через API.

## Классы

### `ChatRequest`

**Описание**: Модель запроса чата, используемая для валидации входящих сообщений.

**Параметры**:
- `message` (str): Сообщение от пользователя.

**Примеры**:
```python
from pydantic import BaseModel

class ChatRequest(BaseModel):\n    message: str
```

## Функции

### `root`

```python
async def root():
    """
    Обрабатывает корневой URL ("/"), возвращая HTML-страницу.

    Returns:
        HTMLResponse: HTML-контент главной страницы.

    Raises:
        HTTPException: В случае, если не удается найти или прочитать файл `index.html`.

    Example:
        Примеры вызовов
    """
```

**Описание**: Обрабатывает корневой URL ("/"), возвращая HTML-страницу.
Если файл `index.html` не найден, возвращает HTTP-ошибку 500.

**Возвращает**:
- `HTMLResponse`: HTML-контент главной страницы.

**Вызывает исключения**:
- `HTTPException`: В случае, если не удается найти или прочитать файл `index.html`.

**Примеры**:
```python
# Пример вызова корневого URL
# (В данном контексте, функция вызывается автоматически FastAPI при обращении к корневому URL)
```

### `chat`

```python
async def chat(request: ChatRequest):
    """
    Обрабатывает POST-запросы к эндпоинту "/api/chat", взаимодействуя с моделью Google Gemini AI.

    Args:
        request (ChatRequest): Объект `ChatRequest`, содержащий сообщение от пользователя.

    Returns:
        dict: Ответ от модели AI в формате JSON.

    Raises:
        HTTPException: В случае ошибки при взаимодействии с моделью AI.

    Example:
        Примеры вызовов
    """
```

**Описание**: Обрабатывает POST-запросы к эндпоинту "/api/chat", взаимодействуя с моделью Google Gemini AI. При первом вызове инициализирует модель.

**Параметры**:
- `request` (ChatRequest): Объект `ChatRequest`, содержащий сообщение от пользователя.

**Возвращает**:
- `dict`: Ответ от модели AI в формате JSON.

**Вызывает исключения**:
- `HTTPException`: В случае ошибки при взаимодействии с моделью AI.

**Примеры**:
```python
# Пример вызова эндпоинта /api/chat с использованием requests
import requests
import json

url = "http://127.0.0.1:8000/api/chat"
data = {"message": "Hello, Gemini!"}
headers = {'Content-type': 'application/json'}
response = requests.post(url, data=json.dumps(data), headers=headers)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code}, {response.text}")
```

### `get_locale_file`

```python
def get_locale_file(lang: str):
    """
    Получает файл локализации для указанного языка.

    Args:
        lang (str): Код языка (например, "en", "ru").

    Returns:
        dict: Словарь с данными локализации.

    Raises:
        HTTPException: Если файл локализации не найден или содержит ошибки.

    Example:
        Примеры вызовов
    """
```

**Описание**: Получает файл локализации для указанного языка.

**Параметры**:
- `lang` (str): Код языка (например, "en", "ru").

**Возвращает**:
- `dict`: Словарь с данными локализации.

**Вызывает исключения**:
- `HTTPException`: Если файл локализации не найден или содержит ошибки JSON.

**Примеры**:
```python
# Пример вызова функции get_locale_file
import requests

lang = "ru"
url = f"http://127.0.0.1:8000/locales/{lang}.json"
response = requests.get(url)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code}, {response.text}")
```

### `locales`

```python
async def locales(lang:str):
    """
    Эндпоинт для получения локализации по коду языка.

    Args:
        lang (str): Код языка.

    Returns:
        dict: Данные локализации в формате JSON.

    Raises:
        HTTPException: Если файл локализации не найден или не может быть прочитан.

    Example:
        Примеры вызовов
    """
```

**Описание**: Эндпоинт для получения локализации по коду языка.

**Параметры**:
- `lang` (str): Код языка.

**Возвращает**:
- `dict`: Данные локализации в формате JSON.

**Вызывает исключения**:
- `HTTPException`: Если файл локализации не найден или не может быть прочитан.

**Примеры**:
```python
# Пример вызова эндпоинта /locales/{lang}.json
# (В данном контексте, функция вызывается автоматически FastAPI при запросе к эндпоинту)
```