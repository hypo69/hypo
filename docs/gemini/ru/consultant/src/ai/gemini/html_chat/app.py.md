# Анализ кода модуля app.py

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован и следует основным принципам FastAPI.
    - Используется Jinja2 для шаблонизации HTML.
    - Присутствует разделение на статические файлы и динамические эндпоинты.
    - Используется `pydantic` для валидации данных.
    - Код логически понятен и легко читается.
- Минусы
    - Отсутствует подробная документация в формате reStructuredText.
    - Не используется `logger` для логирования ошибок и отладки.
    - Не все импорты сгруппированы в начале файла по модулям.
    - Некоторые строки docstring дублируются.
    - Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения файлов, хотя это указано в инструкции.
    - Код использует глобальные переменные `MODE`, которые не используются и не документированы.

**Рекомендации по улучшению**
1.  Добавить подробную документацию в формате reStructuredText (RST) для модуля, функций и классов.
2.  Использовать `from src.logger.logger import logger` для логирования ошибок и отладки.
3.  Сгруппировать импорты по модулям.
4.  Удалить дублирование docstring.
5.  Использовать `j_loads` или `j_loads_ns` для чтения файлов.
6.  Удалить неиспользуемые глобальные переменные.
7. Добавить обработку ошибок с помощью `try-except` и логирование с помощью `logger.error` в функции `ask_question`.
8.  Обеспечить корректную обработку ошибок при чтении файлов.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
"""
Модуль для запуска веб-приложения чата с использованием модели Gemini.
====================================================================

Этот модуль содержит FastAPI приложение, которое предоставляет интерфейс для общения с моделью Gemini.
Приложение использует HTML шаблоны для отображения чата и статические файлы для стилей.

Пример использования
--------------------

Запуск приложения:

.. code-block:: python

    if __name__ == "__main__":
        # Запуск браузера в отдельном потоке
        threading.Timer(1.5, open_browser).start()
    
        # Запуск приложения с uvicorn
        import uvicorn
        uvicorn.run(app, host="127.0.0.1", port=8000)
"""
import webbrowser
import threading
import random
from pathlib import Path
from typing import Any

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from src.ai.gooogle_generativeai.kazarinov import Kazarinov
from src import gs
from src.logger.logger import logger
from src.utils.jjson import j_loads_ns

# Инициализация FastAPI
app = FastAPI()

# Папка с HTML шаблонами
templates = Jinja2Templates(directory=gs.path.src / 'ai' / 'gooogle_generativeai' / 'chat' / 'templates')

# Подключение статики (CSS Bootstrap)
app.mount("/static", StaticFiles(directory=gs.path.src / 'ai' / 'gooogle_generativeai' / 'chat' / 'static'), name="static")


# Инициализация модели Kazarinov
k = Kazarinov(system_instruction=None, generation_config={'response_mime_type': 'text/plain'})

# Загрузка вопросов из файлов
questions_list = []
try:
    questions_path = Path(gs.path.google_drive / 'kazarinov' / 'prompts' / 'q')
    for q_file in questions_path.rglob('*.*'):
        questions_list.append(q_file.read_text(encoding='utf-8'))  # Явно указываем кодировку
except Exception as e:
    logger.error(f'Ошибка при чтении файлов с вопросами: {e}')
    questions_list = []

# Модель для данных из формы (вопрос пользователя)
class Question(BaseModel):
    """
    Модель Pydantic для представления вопроса пользователя.

    :param question: Текст вопроса пользователя.
    """
    question: str


@app.get("/")
async def get_chat(request: Request):
    """
    Обрабатывает GET-запрос к главной странице чата.

    :param request: Объект Request от FastAPI.
    :return: Ответ в виде HTML шаблона с пустым ответом.
    """
    return templates.TemplateResponse("chat.html", {"request": request, "response": ""})


@app.post("/ask")
async def ask_question(question: Question, request: Request):
    """
    Обрабатывает POST-запрос с вопросом пользователя.

    Если вопрос пользователя равен --next, выбирается случайный вопрос из списка.
    Отправляет вопрос в модель Kazarinov и возвращает HTML шаблон с ответом.

    :param question: Объект Question, содержащий вопрос пользователя.
    :param request: Объект Request от FastAPI.
    :return: Ответ в виде HTML шаблона с ответом модели.
    """
    user_question = question.question
    try:
        # Если вопрос не задан, загрузить случайный
        if user_question.lower() == "--next":
            if not questions_list:
                logger.error("Список вопросов пуст.")
                return templates.TemplateResponse("chat.html", {"request": request, "response": "Список вопросов пуст."})
            
            q_list = random.choice(questions_list).split('\n')
            user_question = random.choice(q_list)

        # Отправляем вопрос модели Kazarinov
        response = k.ask(user_question, no_log=False, with_pretrain=False)
        return templates.TemplateResponse("chat.html", {"request": request, "response": response})
    except Exception as e:
        logger.error(f"Ошибка при обработке вопроса: {e}")
        return templates.TemplateResponse("chat.html", {"request": request, "response": "Произошла ошибка при обработке запроса."})


def open_browser():
    """
    Открывает браузер по адресу http://127.0.0.1:8000.
    Используется для автоматического открытия страницы чата после запуска.
    """
    webbrowser.open("http://127.0.0.1:8000")

# Запуск приложения FastAPI и браузера
if __name__ == "__main__":
    # Запуск браузера в отдельном потоке
    threading.Timer(1.5, open_browser).start()
    
    # Запуск приложения с uvicorn
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)