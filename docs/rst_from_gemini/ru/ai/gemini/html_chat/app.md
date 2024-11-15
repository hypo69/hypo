```python
## \file hypotez/src/ai/gemini/html_chat/app.py
# -*- coding: utf-8 -*-
 # <- venv win
## ~~~~~~~~~~~~~
""" module: src.ai.gemini.html_chat

This module implements a simple HTML-based chat application using FastAPI.
It allows users to input questions, which are then sent to the Kazarinov
model for processing. The results are displayed in a web browser.
The application also handles loading questions from a file and provides
a mechanism for loading the next question in the list.
"""

import header
import webbrowser  # Для автоматического открытия браузера
import threading  # Для запуска браузера в отдельном потоке
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


# Список вопросов для чата. Загружает вопросы из файлов в каталоге prompts/q.
def load_questions():
    """Загружает вопросы из файлов в каталоге prompts/q."""
    q_files = list(Path(gs.path.google_drive / 'kazarinov' / 'prompts' / 'q').rglob('*.*'))
    return [q_file.read_text() for q_file in q_files]


questions_list = load_questions()


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

    # Обработка запроса "--next" для случайного вопроса
    if user_question.lower() == "--next":
        if not questions_list:
            return templates.TemplateResponse("chat.html", {"request": request, "response": "Нет доступных вопросов."})

        q_list = random.choice(questions_list).split('\n')  # Выбираем случайный вопрос
        user_question = random.choice(q_list)  # Выбираем случайную строку из выбранного вопроса

    # Отправляем вопрос модели Kazarinov
    try:
        response = k.ask(user_question, no_log=False, with_pretrain=False)
    except Exception as e:
        return templates.TemplateResponse("chat.html", {"request": request, "response": f"Ошибка: {e}"})
    
    return templates.TemplateResponse("chat.html", {"request": request, "response": response})

# Функция для открытия браузера
def open_browser():
    webbrowser.open("http://127.0.0.1:8000")

# Запуск приложения FastAPI и браузера
if __name__ == "__main__":
    # Запуск браузера в отдельном потоке
    threading.Timer(1.5, open_browser).start()
    
    # Запуск приложения с uvicorn
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
```

**Изменения и улучшения:**

* **Документация:** Добавлена подробная документация к модулю, описывающая его функциональность.
* **Обработка ошибок:**  Введен блок `try...except` для перехвата и обработки возможных исключений при обращении к модели Kazarinov.  Теперь приложение не упадет, а выведет сообщение об ошибке.
* **Обработка пустого списка вопросов:** Проверка на пустой список вопросов `questions_list`.  Если список пустой, возвращает соответствующее сообщение об ошибке.
* **Выбор случайного вопроса:**  Вместо случайного выбора всего вопроса, теперь выбирается случайная строка из случайно выбранного вопроса. Это позволяет получать более разнообразные вопросы.
* **Загрузка вопросов:** Введена функция `load_questions()` для загрузки вопросов. Это делает код более организованным.
* **Стиль кода:**  Небольшие улучшения стиля (использование `random.choice()`).

**Как использовать:**

1.  Убедитесь, что вы настроили `gs.path` в файле `__init__.py`.
2.  Убедитесь, что файлы `chat.html`, `static/`, и `style.css` (из примера) находятся в указанном каталоге.
3.  Запустите приложение: `uvicorn hypotez.src.ai.gemini.html_chat.app:app --reload`


Эти изменения делают код более надежным, читаемым и удобным в использовании.  Теперь он способен обрабатывать потенциальные ошибки и предоставляет пользователю более информативные сообщения.  Обратите внимание на  важность правильной настройки путей к файлам и данных в `__init__.py`.