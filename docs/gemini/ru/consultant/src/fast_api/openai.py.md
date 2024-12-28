# Анализ кода модуля `openai.py`

**Качество кода**
6
- Плюсы
    - Используется FastAPI для создания API, что обеспечивает высокую производительность и удобство разработки.
    - Присутствует логирование ошибок с использованием кастомного логгера.
    -  Код разбит на логические блоки.
    - Используется `pydantic` для валидации запросов.
- Минусы
    - Не все комментарии в формате reStructuredText (RST).
    - Обработка ошибок не везде использует логгер `logger.error`.
    - Стандартный `open()` используется для чтения HTML файла, что может вызвать проблемы с кодировкой.
    - Имя файла index.html захардкожено.
    - Нет обработки ошибок при чтении `config.json`
    - Отсутствуют докстринги для всех функций и классов.

**Рекомендации по улучшению**

1.  Добавить docstring в формате reStructuredText (RST) для всех классов, функций и методов.
2.  Использовать `j_loads_ns` из `src.utils.jjson` для чтения файлов `config.json`
3.  Заменить `open()` на использование `Path` и `read_text()` для более безопасного и гибкого чтения файлов.
4.  Обработку ошибок в `root` и `ask_model` переделать на использование `logger.error` и логирование.
5.  Вынести значения для хоста и порта в `config.json`.
6.  Добавить проверку существования файла перед открытием.
7. Убрать хардкод имени html файла.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12
"""
Модуль для взаимодействия с моделью OpenAI через FastAPI.
=========================================================================================
Этот модуль предоставляет FastAPI приложение для взаимодействия с моделью OpenAI.
Включает API endpoints для запроса к модели и обучения на основе предоставленных данных.

Пример использования
--------------------

Пример запуска FastAPI приложения:

.. code-block:: python

    if __name__ == "__main__":
        uvicorn.run(app, host="127.0.0.1", port=8000)
"""

import header

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from pathlib import Path
import uvicorn

from src import gs
from src.utils.jjson import j_loads_ns
from src.logger.logger import logger
from src.ai.openai.model.training import OpenAIModel
# from src.gui.openai_trаigner import AssistantMainWindow #TODO удалить при ненадобности

app = FastAPI()

# Монтирование статических файлов для HTML-страниц
app.mount("/static", StaticFiles(directory=gs.path.src / 'fast_api' / 'html' / 'openai_training'), name="static")

# Настройка middleware для CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = OpenAIModel()


class AskRequest(BaseModel):
    """
    Модель данных для запроса к эндпоинту `/ask`.

    :param message: Сообщение пользователя.
    :type message: str
    :param system_instruction: Системные инструкции для модели.
    :type system_instruction: str, optional
    """
    message: str
    system_instruction: str = None


@app.get("/", response_class=HTMLResponse)
async def root():
    """
    Возвращает HTML-страницу index.html при запросе к корневому URL.
    """
    try:
        # # Чтение конфигурации из config.json
        # # Проверка наличия файла
        config_path = gs.path.src / "fast_api" / 'config.json'
        if not config_path.exists():
              logger.error(f'Файл конфигурации не найден: {config_path}')
              raise HTTPException(status_code=500, detail=f"Файл конфигурации не найден")
        config_data = j_loads_ns(config_path)
        # Получение имени HTML файла из конфига
        html_file_name = config_data.get("html_file", "index.html")  # Значение по умолчанию 'index.html'

        html_file_path = gs.path.src / "fast_api" / 'html' / 'openai' / html_file_name
        if not html_file_path.exists():
            logger.error(f'Файл  HTML не найден: {html_file_path}')
            raise HTTPException(status_code=404, detail="HTML файл не найден")
        # Чтение содержимого HTML-файла
        html_content = html_file_path.read_text(encoding="utf-8")
        return HTMLResponse(html_content)
    except Exception as ex:
        logger.error(f"Ошибка при обработке запроса: {str(ex)}")
        raise HTTPException(status_code=500, detail=f"Ошибка при обработке запроса\\n{ex}")



@app.post("/ask")
async def ask_model(request: AskRequest):
    """
    Обрабатывает запрос пользователя и возвращает ответ от модели.

    :param request: Запрос пользователя.
    :type request: AskRequest
    :return: Ответ от модели.
    :rtype: dict
    """
    try:
        response = model.ask(request.message, request.system_instruction)
        return {"response": response}
    except Exception as ex:
        logger.error(f"Ошибка при обработке запроса: {str(ex)}")
        raise HTTPException(status_code=500, detail=f"Ошибка при обработке запроса\\n{ex}")


# Запуск приложения
if __name__ == "__main__":
    # Чтение конфигурации из config.json
    config_path = gs.path.src / "fast_api" / 'config.json'
    if not config_path.exists():
              logger.error(f'Файл конфигурации не найден: {config_path}')
              exit()
    config_data = j_loads_ns(config_path)

    # Получение хоста и порта из конфига
    host = config_data.get("host", "127.0.0.1")
    port = config_data.get("port", 8000)
    uvicorn.run(app, host=host, port=port)
```