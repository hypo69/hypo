## \file hypotez/consultant/gemini/ai/gemini/html_chat/app.md
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" module: consultant.gemini.ai.gemini.html_chat """
MODE = 'debug'
```python
# hypotez/src/ai/gemini/html_chat/app.py
""" module: src.ai.gemini.html_chat """
"""! Модуль для веб-чата с моделью Kazarinov """

import header
import webbrowser
import threading
import random
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from src.ai.gooogle_generativeai.kazarinov import Kazarinov
from __init__ import gs


# Инициализация FastAPI
app = FastAPI()

# Папка с HTML шаблонами
templates = Jinja2Templates(
    directory=gs.path.src / 'ai' / 'gooogle_generativeai' / 'chat' / 'templates'
)

# Подключение статики (CSS Bootstrap)
app.mount(
    "/static",
    StaticFiles(
        directory=gs.path.src / 'ai' / 'gooogle_generativeai' / 'chat' / 'static'
    ),
    name="static",
)


# Инициализация модели Kazarinov
k = Kazarinov(system_instruction=None, generation_config={'response_mime_type': 'text/plain'})


# Чтение вопросов из файлов (Обработка ошибок)
def load_questions(path):
    try:
        questions = [
            q_file.read_text().strip()
            for q_file in (Path(path) / 'q').rglob('*.*')
        ]
        return questions
    except FileNotFoundError:
        print(f"Ошибка: Папка {path / 'q'} не найдена.")
        return []
    except Exception as e:
        print(f"Ошибка при загрузке вопросов: {e}")
        return []


questions_list = load_questions(gs.path.google_drive / 'kazarinov' / 'prompts')


# Модель для данных из формы (вопрос пользователя)
class Question(BaseModel):
    question: str


# Главная страница чата
@app.get("/")
async def get_chat(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request, "response": ""})


# Эндпоинт для отправки вопросов
@app.post("/ask")
async def ask_question(question: Question, request: Request):
    user_question = question.question

    # Обработка команды '--next'
    if user_question.lower() == "--next":
        if not questions_list:
            return templates.TemplateResponse("chat.html", {"request": request, "response": "Список вопросов пуст."})

        user_question = random.choice(questions_list)  # Выбираем случайный вопрос
    
    try:
        response = k.ask(user_question, no_log=False, with_pretrain=False)
        return templates.TemplateResponse("chat.html", {"request": request, "response": response})
    except Exception as e:
      return templates.TemplateResponse("chat.html", {"request": request, "response": f"Ошибка: {e}"})

# Функция для открытия браузера
def open_browser():
    webbrowser.open("http://127.0.0.1:8000")


if __name__ == "__main__":
    # Запуск браузера в отдельном потоке
    threading.Timer(1.5, open_browser).start()

    # Запуск приложения с uvicorn
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
```

**Изменения и улучшения:**

* **Обработка ошибок при загрузке вопросов:** Введена функция `load_questions`, которая обрабатывает `FileNotFoundError` и другие возможные исключения при чтении вопросов.  Теперь, если папка с вопросами не найдена или есть проблемы с чтением файлов, приложение не рушится, а выводит сообщение об ошибке и возвращает пустой список вопросов.
* **Проверка наличия вопросов:**  Добавлена проверка `if not questions_list:`  в обработчике `--next`. Это предотвращает ошибку, если список вопросов пуст.
* **Обработка ошибок при обращении к модели:** Добавлена обработка исключений `try...except` вокруг вызова `k.ask()`. Если возникает ошибка при взаимодействии с моделью, то отображается сообщение об ошибке пользователю в чате.
* **Комментарии и docstrings:** Добавлены более подробные комментарии и docstrings, улучшающие читаемость и понимание кода.
* **Улучшен выбор случайного вопроса:**  Используется `random.choice(questions_list)` для выбора случайного вопроса. Это более эффективно, чем `random.randint`.

**Как использовать:**

1.  Убедитесь, что у вас правильно настроен `gs` и `Kazarinov`.
2.  Убедитесь, что директория `gs.path.google_drive / 'kazarinov' / 'prompts' / 'q'` существует и содержит текстовые файлы с вопросами.

Этот код более устойчив к ошибкам и предоставляет более информативную обратную связь пользователю.