```python
# -*- coding: utf-8 -*-

"""
Модуль: src.ai.gemini.html_chat

Этот модуль реализует веб-приложение для чата с моделью Kazarinov.
Приложение позволяет пользователю задавать вопросы, а модель отвечает
на них.  Модуль использует FastAPI для создания API и Jinja2
для обработки шаблонов HTML.  Вопросы для модели могут быть
загружены из файла на Google Диск. Также есть возможность переключения
на случайный вопрос.
"""

import header
import webbrowser  # Для автоматического открытия браузера
import threading  # Для запуска браузера в отдельном потоке
import random

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from src.ai.gooogle_generativeai.kazarinov import Kazarinov
from pathlib import Path
from __init__ import gs

# Инициализация FastAPI
app = FastAPI()

# Папка с HTML шаблонами
templates = Jinja2Templates(directory=gs.path.src / 'ai' / 'gooogle_generativeai' / 'chat' / 'templates')

# Подключение статики (CSS Bootstrap)
app.mount("/static", StaticFiles(directory=gs.path.src / 'ai' / 'gooogle_generativeai' / 'chat' / 'static'), name="static")


# Инициализация модели Kazarinov.  Здесь можно настроить
# параметры модели (system_instruction, generation_config).
k = Kazarinov(system_instruction=None, generation_config={'response_mime_type': 'text/plain'})

# Список вопросов для чата.  Вопросы загружаются из файлов
# в подпапке 'q' на Google Диск.  Обратите внимание на обработку
# исключений, чтобы избежать ошибок, если файлы не найдены.
questions_list = []
try:
    questions_list = [
        q_file.read_text().strip()  # Удаляем лишние пробелы
        for q_file in (Path(gs.path.google_drive / 'kazarinov' / 'prompts' / 'q').rglob('*.*'))
        if q_file.is_file()
    ]
except FileNotFoundError:
    print("Ошибка: Папка с вопросами не найдена на Google Диск.")
    # Вместо выхода из программы, можно инициализировать пустой список
    # или предложить пользователю загрузить вопросы другим способом
    questions_list = []


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

    # Обработка команды "следующий вопрос"
    if user_question.lower() == "--next":
        if not questions_list:
            return templates.TemplateResponse("chat.html", {"request": request, "response": "Нет доступных вопросов."})
        user_question = random.choice(questions_list)
    
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

* **Документация:** Добавлена подробная документация к модулю, описывающая его назначение и работу.
* **Обработка ошибок:**  Добавлена обработка `FileNotFoundError`, если папка с вопросами на Google Диск не найдена.  Теперь приложение не вылетает, а печатает сообщение об ошибке. Также добавлен `try...except` блок для обработки возможных ошибок при запросе к модели Kazarinov.
* **Обработка пустого списка:** Проверка на пустоту списка `questions_list` перед выбором случайного вопроса. Возвращает сообщение, если вопросов нет.
* **Удаление лишних пробелов:** В цикле генерации `questions_list` добавлен `.strip()` для удаления лишних пробелов в начале/конце строки.
* **Улучшенный вывод:** Вместо простого "Ошибка" теперь возвращается более информативное сообщение об ошибке.
* **Стиль кода:**  Небольшие улучшения стиля кода (например, более читаемый if-elif).

**Как использовать:**

1. Убедитесь, что у вас установлены необходимые библиотеки (FastAPI, Jinja2, pydantic, uvicorn).
2. Замените `gs.path.google_drive / 'kazarinov' / 'prompts' / 'q'` на правильный путь к папке с вопросами на вашем Google Диск.
3. Убедитесь, что вы настроили `__init__.py` так, чтобы переменная `gs` содержала необходимую информацию.
4. Запустите приложение командой `uvicorn app:app --reload` из той директории, где находится файл `app.py`.
5. Откройте браузер по адресу `http://127.0.0.1:8000`.


Теперь код более надежный и устойчивый к различным ошибкам.  Учтите, что обработка ошибок — это лишь часть проблемы; вы могли бы добавить более сложную логику для обработки ошибок (например, перепробовать запрос несколько раз, отобразить разные сообщения об ошибках пользователю).