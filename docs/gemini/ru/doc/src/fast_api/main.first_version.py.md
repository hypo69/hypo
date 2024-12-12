# Модуль `main.first_version.py`

## Обзор

Данный модуль представляет собой FastAPI приложение, которое обрабатывает данные, отправленные через HTML-форму, и взаимодействует с внешним Python-скриптом для их обработки. Также предоставляет статический доступ к HTML-файлам и открывает `index.html` в браузере при запуске.

## Оглавление

- [Константы](#константы)
- [Импорты](#импорты)
- [Инициализация FastAPI](#инициализация-fastapi)
- [Монтирование статических файлов](#монтирование-статических-файлов)
- [Обработчик POST-запроса `/process_data`](#обработчик-post-запроса-process_data)
- [Обработчик GET-запроса `/`](#обработчик-get-запроса)

## Константы

### `MODE`

**Описание**: Указывает режим работы приложения. В данном случае используется значение `'dev'`.
```python
MODE = 'dev'
```

## Импорты

Модуль импортирует следующие библиотеки:

- `os`: Для работы с операционной системой.
- `subprocess`: Для запуска внешних процессов.
- `webbrowser`: Для открытия веб-страниц в браузере.
- `pathlib.Path`: Для удобной работы с путями к файлам.
- `fastapi.FastAPI`: Основной класс для создания FastAPI приложения.
- `fastapi.Form`: Для получения данных из HTML-форм.
- `fastapi.Request`: Для работы с запросами.
- `fastapi.HTTPException`: Для формирования HTTP-исключений.
- `subprocess.Popen`: Для создания дочерних процессов.
- `subprocess.PIPE`: Для управления потоками ввода/вывода дочернего процесса.
- `fastapi.staticfiles.StaticFiles`: Для обслуживания статических файлов.

```python
import os
import subprocess
import webbrowser
from pathlib import Path
from fastapi import FastAPI, Form, Request, HTTPException
from subprocess import Popen, PIPE
from fastapi.staticfiles import StaticFiles
```

## Инициализация FastAPI

Создается экземпляр класса FastAPI для работы с HTTP-запросами.

```python
app = FastAPI()
```

## Монтирование статических файлов

Подключает каталог `html` как источник статических файлов, чтобы приложение могло их обслуживать.

```python
app.mount("/", StaticFiles(directory="html"), name="html")
```
Открывает браузер со страницей `index.html` при запуске приложения.
```python
webbrowser.open("http://localhost:8000/html/index.html")
```

## Функции

### `process_data`

**Описание**: Обрабатывает POST-запрос `/process_data` для получения данных из HTML-формы.

**Параметры**:
- `request` (Request): Объект запроса FastAPI.
- `first_name` (str): Имя, полученное из формы.
- `last_name` (str): Фамилия, полученная из формы.

**Возвращает**:
- `dict`: Словарь с выходными данными скрипта.

**Вызывает исключения**:
- `HTTPException`: Возникает, если не указано имя или фамилия, или при ошибке выполнения скрипта.
```python
@app.post("/process_data")
async def process_data(request: Request, first_name: str = Form(...), last_name: str = Form(...)) -> dict:
    """
    Args:
        request (Request): Объект запроса FastAPI.
        first_name (str, optional): Имя, полученное из формы. По умолчанию `Form(...)`.
        last_name (str, optional): Фамилия, полученная из формы. По умолчанию `Form(...)`.

    Returns:
        dict: Словарь с выходными данными скрипта.

    Raises:
        HTTPException: Возникает, если не указано имя или фамилия, или при ошибке выполнения скрипта.
    """
    # Check if first name and last name are provided
    if not first_name or not last_name:
        raise HTTPException(status_code=400, detail="First name and last name must be provided")
    
    # Formulate the input data string
    input_data = f"{first_name} {last_name}"
    
    # Execute the script with the input data and get the result
    script_path = Path(__file__).resolve().parent.parent / 'script.py'
    process = Popen(['python', str(script_path)], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate(input=input_data.encode())
    
    # Check for errors during script execution
    if process.returncode != 0:
        raise HTTPException(status_code=500, detail=f"Error executing the script: {stderr.decode()}")
    
    return {"output": stdout.decode()}
```

### `open_index`

**Описание**: Обрабатывает GET-запрос `/`. Перенаправляет на страницу `index.html`.

**Возвращает**:
- `dict`: Сообщение о перенаправлении.

```python
@app.get("/")
async def open_index() -> dict:
    """
    Returns:
        dict: Сообщение о перенаправлении.
    """
    # Redirect to index.html
    return {"message": "Redirecting to index.html..."}