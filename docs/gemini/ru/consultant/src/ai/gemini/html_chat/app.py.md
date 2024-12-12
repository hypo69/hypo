# Анализ кода модуля `app.py`

**Качество кода**

-  **Соответствие требованиям по оформлению кода: 7/10**
    -   **Плюсы:**
        -   Используются `fastapi`, `pydantic`, `jinja2`, что соответствует современным стандартам разработки.
        -   Код разбит на логические блоки, что улучшает читаемость.
        -   Используются `threading` и `webbrowser` для автоматического открытия браузера, что удобно для пользователя.
        -   Применяется `pathlib` для работы с путями, что является хорошей практикой.
    -   **Минусы:**
        -   Отсутствуют docstring для модуля, функций и классов.
        -   Некоторые комментарии не соответствуют формату RST.
        -   Не используется `logger` для отслеживания ошибок и отладки.
        -   Не используются `j_loads` или `j_loads_ns` для чтения файлов.
        -   Дублирование комментариев, не несущие никакой смысловой нагрузки.
        -   Смешаны стили комментариев `#` и `"""`.

**Рекомендации по улучшению**

1.  **Добавить docstring:** Необходимо добавить docstring для модуля, функций и классов, используя reStructuredText (RST) формат.
2.  **Логирование:** Вместо стандартного `try-except` использовать `logger.error` для обработки ошибок.
3.  **Импорты:** Проверить и добавить отсутствующие импорты. Привести в соответствие имена функций, переменных и импортов с ранее обработанными файлами.
4.  **Комментарии:** Переписать все комментарии в формате reStructuredText (RST), сохраняя существующие `#` комментарии.
5.  **Чтение файлов:** Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения файлов.
6.  **Удалить дублирующиеся комментарии:** Убрать комментарии, не несущие смысловой нагрузки.
7.  **Унификация стиля комментариев:** Использовать только `#` для комментирования кода, а `"""` для docstring.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для запуска HTML-чата с использованием Google Gemini.
==========================================================

Этот модуль создает веб-приложение на основе FastAPI, которое предоставляет
интерфейс для общения с моделью Google Gemini. Он включает в себя
веб-страницу чата, API для отправки вопросов и получения ответов, а также
автоматическое открытие браузера при запуске.

Пример использования
--------------------

.. code-block:: python

    python app.py

"""

MODE = 'dev'

import webbrowser  #  Для автоматического открытия браузера
import threading  #  Для запуска браузера в отдельном потоке
import random # Для выбора случайного вопроса из списка
from pathlib import Path # Для работы с путями
from typing import Any # Для аннотации типов

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from src.ai.gooogle_generativeai.kazarinov import Kazarinov
from src import gs
from src.logger.logger import logger
from src.utils.jjson import j_loads  # Для загрузки JSON файлов



# Инициализация FastAPI
app = FastAPI()

# Папка с HTML шаблонами
templates = Jinja2Templates(directory=gs.path.src / 'ai' / 'gooogle_generativeai' / 'chat' / 'templates')

# Подключение статики (CSS Bootstrap)
app.mount("/static", StaticFiles(directory=gs.path.src / 'ai' / 'gooogle_generativeai' / 'chat' / 'static'), name="static")


# Инициализация модели Kazarinov
k = Kazarinov(system_instruction=None, generation_config={'response_mime_type': 'text/plain'})

# Загрузка вопросов для чата из файлов
questions_path = Path(gs.path.google_drive / 'kazarinov' / 'prompts' / 'q')
questions_list = []

for q_file in questions_path.rglob('*.*'):
    try:
        questions_list.append(q_file.read_text(encoding='utf-8'))
    except Exception as e:
        logger.error(f"Ошибка при чтении файла {q_file}: {e}")
        continue


# Модель для данных из формы (вопрос пользователя)
class Question(BaseModel):
    """
    Модель для представления вопроса пользователя.

    :param question: Текст вопроса пользователя.
    :type question: str
    """
    question: str

# Главная страница чата
@app.get("/")
async def get_chat(request: Request) -> Any:
    """
    Отображает главную страницу чата.

    :param request: Объект запроса FastAPI.
    :type request: fastapi.Request
    :return: Ответ шаблона Jinja2.
    :rtype: fastapi.templating.Jinja2Templates.TemplateResponse
    """
    return templates.TemplateResponse("chat.html", {"request": request, "response": ""})

# Эндпоинт для отправки вопросов
@app.post("/ask")
async def ask_question(question: Question, request: Request) -> Any:
    """
    Обрабатывает запрос пользователя и возвращает ответ от модели.

    :param question: Объект запроса с вопросом пользователя.
    :type question: Question
    :param request: Объект запроса FastAPI.
    :type request: fastapi.Request
    :return: Ответ шаблона Jinja2 с ответом от модели.
    :rtype: fastapi.templating.Jinja2Templates.TemplateResponse
    """
    user_question = question.question

    #  Если вопрос не задан, загрузить случайный
    if user_question.lower() == "--next":
        try:
            q_list = questions_list[random.randint(0, len(questions_list) - 1)].split('\n')
            user_question = q_list[random.randint(0, len(q_list) - 1)]
        except Exception as e:
             logger.error(f"Ошибка при выборе случайного вопроса: {e}")
             user_question = ""

    #  Отправляем вопрос модели Kazarinov
    try:
         response = k.ask(user_question, no_log=False, with_pretrain=False)
    except Exception as e:
        logger.error(f"Ошибка при запросе к модели: {e}")
        response = "Произошла ошибка при обработке запроса."

    return templates.TemplateResponse("chat.html", {"request": request, "response": response})

# Функция для открытия браузера
def open_browser() -> None:
    """
    Открывает браузер по адресу http://127.0.0.1:8000.
    """
    webbrowser.open("http://127.0.0.1:8000")

# Запуск приложения FastAPI и браузера
if __name__ == "__main__":
    #  Запуск браузера в отдельном потоке
    threading.Timer(1.5, open_browser).start()
    
    #  Запуск приложения с uvicorn
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
```