# Анализ кода модуля `app.py`

**Качество кода**
7
- Плюсы
    - Код структурирован и разделен на логические блоки.
    - Используется FastAPI для создания веб-сервиса.
    - Присутствует логика для случайного выбора вопроса.
    - Используется Jinja2 для рендеринга HTML шаблонов.
    - Браузер открывается автоматически в отдельном потоке.
- Минусы
    - Отсутствует docstring для модуля в начале файла.
    - Комментарии не соответствуют стандарту RST.
    - Не используются `j_loads` или `j_loads_ns` для чтения файлов.
    - Отсутствует обработка ошибок с помощью `logger.error`.
    - Есть дублирование комментариев и пустые комментарии.
    - Переменная `MODE` не используется.

**Рекомендации по улучшению**

1.  Добавить docstring в начале файла, описывающий назначение модуля.
2.  Переписать все комментарии в формате RST, включая docstring для функций.
3.  Использовать `from src.utils.jjson import j_loads` для загрузки данных, если это необходимо.
4.  Добавить обработку ошибок с помощью `logger.error`, особенно при работе с внешними ресурсами.
5.  Удалить избыточные и пустые комментарии.
6.  Удалить неиспользуемую переменную `MODE`.
7.  Добавить логирование для отладки и мониторинга работы приложения.
8.  Добавить try-except для обработки возможных ошибок при чтении файлов.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
"""
Модуль для запуска веб-интерфейса чата с использованием модели Kazarinov.
==========================================================================

Этот модуль создает веб-приложение с использованием FastAPI, которое позволяет пользователю взаимодействовать с моделью Kazarinov через HTML интерфейс.

Пример использования
--------------------

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
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from src.ai.gooogle_generativeai.kazarinov import Kazarinov
import random
from pathlib import Path
from src import gs
from src.logger.logger import logger # импорт для логирования


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
    # Код исполняет чтение файлов с вопросами
    questions_list = [
        q_file.read_text()
        for q_file in (Path(gs.path.google_drive / 'kazarinov' / 'prompts' / 'q').rglob('*.*'))
    ]
except Exception as e:
    # Логирование ошибки в случае неудачи загрузки вопросов
    logger.error(f'Ошибка при чтении файлов с вопросами: {e}')


# Модель для данных из формы (вопрос пользователя)
class Question(BaseModel):
    """
     Модель для представления вопроса пользователя.

     :param question: Вопрос пользователя в виде строки.
    """
    question: str


@app.get("/")
async def get_chat(request: Request):
    """
    Обрабатывает GET запрос для главной страницы чата.

    :param request: Объект запроса FastAPI.
    :return: HTML страница чата с шаблоном "chat.html".
    """
    #  Код возвращает HTML страницу чата с шаблоном "chat.html"
    return templates.TemplateResponse("chat.html", {"request": request, "response": ""})


@app.post("/ask")
async def ask_question(question: Question, request: Request):
    """
    Обрабатывает POST запрос для отправки вопроса и получения ответа от модели.

    :param question: Объект вопроса пользователя типа Question.
    :param request: Объект запроса FastAPI.
    :return: HTML страница чата с ответом от модели.
    """
    user_question = question.question

    # Если вопрос "--next", выбираем случайный вопрос из списка
    if user_question.lower() == "--next":
        try:
            # Код выбирает случайный вопрос из списка
            q_list = questions_list[random.randint(0, len(questions_list) - 1)].split('\n')
            user_question = q_list[random.randint(0, len(q_list) - 1)]
        except ValueError as e:
             # Логирование ошибки в случае если список вопросов пуст
             logger.error(f'Ошибка при выборе случайного вопроса: {e}')
             user_question = 'Не удалось загрузить вопрос'
    
    # Отправляем вопрос модели Kazarinov
    try:
        # Код отправляет вопрос модели и получает ответ
        response = k.ask(user_question, no_log=False, with_pretrain=False)
    except Exception as e:
       # Логирование ошибки в случае если модель не отвечает
       logger.error(f'Ошибка при запросе к модели: {e}')
       response = 'Ошибка при получении ответа от модели'

    # Возвращаем шаблон с ответом
    return templates.TemplateResponse("chat.html", {"request": request, "response": response})


def open_browser():
    """
    Открывает браузер по адресу http://127.0.0.1:8000.
    """
    # Код открывает браузер
    webbrowser.open("http://127.0.0.1:8000")

# Запуск приложения FastAPI и браузера
if __name__ == "__main__":
    # Запуск браузера в отдельном потоке
    threading.Timer(1.5, open_browser).start()
    
    # Запуск приложения с uvicorn
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)