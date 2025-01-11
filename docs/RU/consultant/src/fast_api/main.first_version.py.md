# Анализ кода модуля `main.first_version.py`

**Качество кода**
9
-  Плюсы
    - Код структурирован и разбит на функции.
    - Используются FastAPI для создания API.
    - Обработка ошибок с помощью `HTTPException`.
    - Использование статических файлов.
-  Минусы
    - Отсутствует импорт `logger` из `src.logger`.
    - Есть закомментированный код, который можно удалить.
    - Не все функции и методы имеют docstring.
    - Использование `webbrowser.open` без обработки ошибок в самом начале.
    - Жестко заданный путь к `script.py`.

**Рекомендации по улучшению**

1. **Добавить `logger`**: Импортировать `logger` из `src.logger.logger` для логирования ошибок и отладочных сообщений.
2. **Удалить закомментированный код**: Удалить неиспользуемый закомментированный код.
3. **Добавить docstring**: Добавить docstring к функциям и методам для лучшего понимания кода и генерации документации.
4. **Обработка ошибок `webbrowser.open`**:  Обернуть `webbrowser.open` в блок `try-except` с логированием ошибок.
5. **Путь к скрипту**:  Лучше сделать путь к скрипту `script.py` настраиваемым или вынести его в переменные окружения для гибкости.
6. **Проверка `subprocess.Popen`**: Улучшить проверку ошибок при выполнении subprocess.
7. **Комментарии**: Добавить комментарии в стиле RST для функций и методов.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для запуска FastAPI приложения.
====================================================

Этот модуль создает FastAPI приложение для обработки данных из HTML-формы
и выполнения Python скрипта.

Пример использования:
--------------------

Запустите FastAPI приложение, используя команду:

.. code-block:: bash

    uvicorn main:app --reload

После запуска приложения, перейдите по адресу http://localhost:8000/html/index.html в браузере.
"""
#! venv/bin/python/python3.12

import os
import subprocess
import webbrowser
from pathlib import Path
from fastapi import FastAPI, Form, Request, HTTPException
from subprocess import Popen, PIPE
from fastapi.staticfiles import StaticFiles
from src.logger.logger import logger  # Импорт logger

app = FastAPI()

# Mount the 'html' folder as static files
app.mount("/", StaticFiles(directory="html"), name="html")

# Открытие index.html в браузере при запуске приложения
try:
    webbrowser.open("http://localhost:8000/html/index.html")
except Exception as e:
    logger.error(f"Ошибка при открытии браузера: {e}") # Логирование ошибки открытия браузера

@app.post("/process_data")
async def process_data(request: Request, first_name: str = Form(...), last_name: str = Form(...)):
    """
    Обрабатывает данные, отправленные из HTML-формы.

    Args:
        request (Request): Объект запроса FastAPI.
        first_name (str): Имя, полученное из формы.
        last_name (str): Фамилия, полученная из формы.

    Returns:
         dict: JSON-ответ с результатом выполнения скрипта или сообщением об ошибке.

    Raises:
         HTTPException: Если имя или фамилия не предоставлены, или если выполнение скрипта завершилось с ошибкой.

    Example:
      Отправляет данные формы в Python скрипт и возвращает результат.
    """
    # Проверка наличия имени и фамилии
    if not first_name or not last_name:
        raise HTTPException(status_code=400, detail="Имя и фамилия должны быть предоставлены")

    # Формирование строки входных данных
    input_data = f"{first_name} {last_name}"

    # Определение пути к скрипту
    script_path = Path(__file__).resolve().parent.parent / 'script.py'
    # Запуск скрипта и передача входных данных
    try:
        process = Popen(['python', str(script_path)], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate(input=input_data.encode())
    except Exception as e:
          logger.error(f"Ошибка при выполнении скрипта: {e}")
          raise HTTPException(status_code=500, detail=f"Ошибка при выполнении скрипта: {e}")

    # Проверка кода возврата скрипта
    if process.returncode != 0:
        logger.error(f"Скрипт завершился с ошибкой, код возврата: {process.returncode}, сообщение об ошибке: {stderr.decode()}") # Логирование ошибки выполнения скрипта
        raise HTTPException(status_code=500, detail=f"Ошибка выполнения скрипта: {stderr.decode()}")

    return {"output": stdout.decode()}


@app.get("/")
async def open_index():
    """
    Перенаправляет пользователя на index.html.

    Returns:
        dict: Сообщение о перенаправлении.

    Example:
        При обращении к корневому пути, возвращает сообщение о перенаправлении.
    """
    return {"message": "Перенаправление на index.html..."}
```