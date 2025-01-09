# Анализ кода модуля `main.py`

**Качество кода**
-  Соответствие требованиям к формату кода (1-10):
    -   **Преимущества:**
        -   Использование `CORSMiddleware` для обработки запросов CORS.
        -   Использование `fastapi.Depends` для управления авторизацией пользователей.
        -   Применение `pydantic` для валидации данных запросов.
        -   Разделение логики авторизации и бизнес-логики чата.
        -   Обработка ошибок с использованием `try-except` и `logger.error`.
        -   Использование `Path` из `pathlib` для работы с файлами.
    -   **Недостатки:**
        -   Отсутствует документация в формате reStructuredText (RST).
        -   Используется `json.load` вместо `j_loads` или `j_loads_ns`.
        -   Не все функции и переменные имеют описания.
        -   Логика обработки сессий реализована не полностью (например, нет механизма продления сессии).
        -   Некоторые `try-except` блоки можно переписать, используя `logger.error` для обработки ошибок.
        -   Слишком большое количество импортов, некоторые из них могут быть лишними.
        -   Не используется `j_loads` или `j_loads_ns`.

**Рекомендации по улучшению**

1.  **Документирование кода**:
    -   Добавить docstring в формате RST для всех модулей, функций и классов.
    -   Включить описания параметров и возвращаемых значений.
2.  **Использование `j_loads`**:
    -   Заменить `json.load` на `j_loads` из `src.utils.jjson` для чтения файлов.
3.  **Улучшение обработки ошибок**:
    -   Использовать `logger.error` для обработки ошибок в блоках `try-except`, избегать `raise HTTPException` там, где это не критично.
4.  **Оптимизация импортов**:
    -   Удалить неиспользуемые импорты.
5.  **Улучшение управления сессиями**:
    -   Включить механизм продления сессии.
    -   Добавить обработку ошибок при управлении сессиями.
6.  **Улучшение структуры**:
    -   Перенести константы в начало файла.
7.  **Стандартизация кода**:
    -   Использовать одинарные кавычки для всех строк.

**Улучшенный код**

```python
"""
Модуль для реализации чат-бота с использованием Google Gemini.
=========================================================================================

Модуль предоставляет API для общения с чат-ботом, аутентификации пользователей
и загрузки локализованных данных.

Пример использования
--------------------

Пример запуска сервера:

.. code-block:: python

    if __name__ == "__main__":
        uvicorn.run(app, host="127.0.0.1", port=8000, log_level="debug")
"""
from __future__ import annotations

import sys  # Импорт sys
from pathlib import Path  # Импорт Path
from typing import Any, Annotated # Импорт Any, Annotated
import uuid  # Импорт uuid
from datetime import datetime, timedelta # Импорт datetime, timedelta

from fastapi import FastAPI, HTTPException, status, Depends, Request, Form, Cookie # Импорт необходимых компонентов FastAPI
from fastapi.middleware.cors import CORSMiddleware # Импорт CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse # Импорт типов ответов
from fastapi.staticfiles import StaticFiles # Импорт StaticFiles
from pydantic import BaseModel  # Импорт BaseModel
import uvicorn # Импорт uvicorn

from src import gs  # Импорт gs
from src.logger import logger # Импорт logger
from src.ai import GoogleGenerativeAI # Импорт GoogleGenerativeAI
from src.utils.file import recursively_get_file_path # Импорт recursively_get_file_path
from src.utils.jjson import j_loads  # Импорт j_loads # Изменено на j_loads

# ===========================================================================
# Константы
# ===========================================================================

BASE_PATH: Path = gs.path.endpoints / 'ai_games' / '101_basic_computer_games' / 'ru' / 'chat' # Путь к базовой директории
LOCALES_PATH: Path = BASE_PATH /  'html' / 'locales' # Путь к директории с локалями
HTML_PATH: Path = BASE_PATH / 'html' # Путь к директории с HTML
USERS = { # Список пользователей
    'user': 'password123'
}
SESSION_DATA = {} # Данные сессий
SESSION_COOKIE_NAME = 'session_id' # Имя куки для сессии
SESSION_TTL = timedelta(hours=1) # Время жизни сессии

# ===========================================================================
# Инициализация приложения
# ===========================================================================

app = FastAPI()

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# ===========================================================================
# Аутентификация
# ===========================================================================

async def get_current_user(session_id: Annotated[str | None, Cookie()] = None) -> str | None:
    """
    Получает текущего пользователя из сессии.

    :param session_id: Идентификатор сессии пользователя.
    :type session_id: str | None
    :return: Имя пользователя или None, если сессия недействительна.
    :rtype: str | None
    """
    if session_id is None or session_id not in SESSION_DATA: # Проверка наличия сессии
        return None # Если нет, возвращаем None
    data = SESSION_DATA[session_id] # Получаем данные сессии
    if data['expires'] < datetime.utcnow(): # Проверяем, не истекла ли сессия
        logger.warning('Session expired. Remove session') # Предупреждение об истечении сессии
        del SESSION_DATA[session_id] # Удаление данных истекшей сессии
        return None # Возвращаем None
    data['expires'] = datetime.utcnow() + SESSION_TTL # Продление времени жизни сессии
    return data['user'] # Возвращаем имя пользователя


@app.post('/api/login')
async def login(username: str = Form(), password: str = Form()) -> RedirectResponse:
    """
    Обрабатывает запрос на вход пользователя.

    :param username: Имя пользователя.
    :type username: str
    :param password: Пароль пользователя.
    :type password: str
    :raises HTTPException: Если учетные данные недействительны.
    :return: Перенаправление на главную страницу.
    :rtype: RedirectResponse
    """
    if username not in USERS or USERS[username] != password: # Проверка учетных данных
        logger.warning('Login failed: Invalid username or password') # Предупреждение о неверных учетных данных
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid credentials') # Возврат ошибки 401

    session_id: str = str(uuid.uuid4()) # Создание уникального идентификатора сессии
    SESSION_DATA[session_id] = { # Сохранение данных сессии
        'user': username,
        'expires': datetime.utcnow() + SESSION_TTL
    }
    logger.info(f'Login successful for user {username}') # Сообщение об успешном входе
    response: RedirectResponse = RedirectResponse(url='/', status_code=303) # Перенаправление после входа
    response.set_cookie(key=SESSION_COOKIE_NAME, value=session_id, httponly=True, samesite='none', secure=True) # Установка куки сессии
    return response # Возврат ответа


@app.post('/api/logout')
async def logout(session_id: Annotated[str | None, Cookie()] = None) -> JSONResponse:
    """
    Обрабатывает запрос на выход пользователя.

    :param session_id: Идентификатор сессии пользователя.
    :type session_id: str | None
    :raises HTTPException: Если сессия недействительна.
    :return: Сообщение об успешном выходе.
    :rtype: JSONResponse
    """
    if session_id is None or session_id not in SESSION_DATA: # Проверка наличия сессии
        logger.warning('Logout failed: session_id is not valid') # Предупреждение о неверном session_id
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Unauthorized') # Возврат ошибки 401

    del SESSION_DATA[session_id] # Удаление данных сессии
    logger.info(f'Logout successful for user with session_id {session_id}') # Сообщение об успешном выходе
    response: JSONResponse = JSONResponse(content={'message': 'Logout successful'}) # Создание JSON ответа
    response.delete_cookie(SESSION_COOKIE_NAME) # Удаление куки сессии
    return response # Возврат ответа


# ===========================================================================
# Основное приложение
# ===========================================================================

class ChatRequest(BaseModel):
    """
    Модель запроса чата.

    :param message: Сообщение пользователя.
    :type message: str
    """
    message: str # Сообщение пользователя


MODEL: GoogleGenerativeAI | None = None # Модель GoogleGenerativeAI
API_KEY: str = gs.credentials.gemini.games # API ключ
SYSTEM_INSTRUCTION: str = '' # Системная инструкция


@app.get('/', response_class=HTMLResponse)
async def root(request: Request, current_user: str | None = Depends(get_current_user)) -> HTMLResponse:
    """
    Обрабатывает корневой запрос и возвращает HTML-страницу.

    :param request: Объект запроса.
    :type request: Request
    :param current_user: Текущий пользователь.
    :type current_user: str | None
    :raises HTTPException: Если файл не найден или произошла другая ошибка.
    :return: HTML-контент.
    :rtype: HTMLResponse
    """
    try:
        if current_user:  # Проверка, авторизован ли пользователь
            index_file: Path = HTML_PATH / 'index.html' # Путь к файлу index.html
            if not index_file.exists(): # Проверка существования файла
                logger.error(f'Could not find index.html at path: {index_file}', exc_info=True) # Запись ошибки в лог
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'index.html not found: {index_file}') # Возврат ошибки 404
            html_content: str = index_file.read_text(encoding='utf-8') # Чтение HTML контента
            return HTMLResponse(content=html_content)  # Возврат HTML контента
        else: # Если пользователь не авторизован
            login_file: Path = HTML_PATH / 'login.html' # Путь к файлу login.html
            if not login_file.exists(): # Проверка существования файла
                logger.error(f'Could not find login.html at path: {login_file}', exc_info=True)  # Запись ошибки в лог
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'login.html not found: {login_file}') # Возврат ошибки 404
            html_content: str = login_file.read_text(encoding='utf-8') # Чтение HTML контента
            return HTMLResponse(content=html_content) # Возврат HTML контента
    except FileNotFoundError as e: # Обработка ошибки FileNotFoundError
        logger.error(f'Error in root: File not found: {e}', exc_info=True) # Запись ошибки в лог
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'index.html not found: {e}') # Возврат ошибки 404
    except Exception as e: # Обработка других ошибок
        logger.error(f'Error in root: {e}', exc_info=True) # Запись ошибки в лог
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f'Error reading templates: {str(e)}') # Возврат ошибки 500


@app.post('/api/chat')
async def chat(request: ChatRequest, current_user: str = Depends(get_current_user)) -> dict[str, Any]:
    """
    Обрабатывает запрос чата и возвращает ответ бота.

    :param request: Объект запроса чата.
    :type request: ChatRequest
    :param current_user: Текущий пользователь.
    :type current_user: str
    :raises HTTPException: Если произошла ошибка при обработке запроса.
    :return: Ответ бота.
    :rtype: dict[str, Any]
    """
    global MODEL # Использование глобальной переменной MODEL
    try:
        if not MODEL: # Инициализация модели, если она не была инициализирована
            MODEL = GoogleGenerativeAI(api_key=API_KEY, model_name='gemini-2.0-flash-exp') # Создание экземпляра модели
        response: str = await MODEL.chat(request.message) # Получение ответа от модели
        return {'response': response} # Возврат ответа
    except Exception as ex: # Обработка ошибок
        logger.error(f'Error in chat: {ex}', exc_info=True) # Запись ошибки в лог
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(ex)) # Возврат ошибки 500


def get_locale_file(lang: str) -> dict[str, str]:
    """
    Читает файл локализации для заданного языка.

    :param lang: Код языка.
    :type lang: str
    :raises HTTPException: Если файл не найден или произошла ошибка.
    :return: Словарь с локализацией.
    :rtype: dict[str, str]
    """
    locale_file: Path = LOCALES_PATH / f'{lang}.json' # Формирование пути к файлу локализации
    try:
        with open(locale_file, 'r', encoding='utf-8') as f:  # Открытие файла
            return j_loads(f)  # Использование j_loads # Изменено на j_loads
    except FileNotFoundError as ex: # Обработка ошибки FileNotFoundError
        logger.error(f'Error reading locale: {ex}', exc_info=True) # Запись ошибки в лог
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Locale not found') # Возврат ошибки 404
    except Exception as ex: # Обработка других ошибок
        logger.error(f'Error reading locale: {ex}', exc_info=True) # Запись ошибки в лог
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Error reading locales') # Возврат ошибки 500


@app.get('/locales/{lang}.json')
async def locales(lang: str, current_user: str = Depends(get_current_user)) -> dict[str, str]:
    """
    Возвращает файл локализации.

    :param lang: Код языка.
    :type lang: str
    :param current_user: Текущий пользователь.
    :type current_user: str
    :return: Словарь с локализацией.
    :rtype: dict[str, str]
    """
    return get_locale_file(lang) # Возврат файла локализации


@app.get('/api/rules')
async def rules(current_user: str = Depends(get_current_user)) -> list[dict[str, str]]:
    """
    Возвращает список правил.

    :param current_user: Текущий пользователь.
    :type current_user: str
    :return: Список правил.
    :rtype: list[dict[str, str]]
    """
    rules_list: list[Path] = recursively_get_file_path(gs.path.endpoints / 'ai_games' / '101_basic_computer_games' / 'ru' / 'rules' ) # Получение списка файлов с правилами
    rules_list = [rule.name for rule in rules_list] # Извлечение имен файлов из списка
    return rules_list # Возврат списка правил


# Локальный запуск сервера
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000, log_level='debug')
```