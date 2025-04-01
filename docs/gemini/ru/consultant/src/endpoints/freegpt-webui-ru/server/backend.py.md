### **Анализ кода модуля `backend.py`**

**Качество кода:**

- **Соответствие стандартам**: 6/10
- **Плюсы**:
    - Код разбит на функции, что улучшает читаемость.
    - Используется `threading` для обновления прокси в фоновом режиме.
    - Есть обработка исключений.
- **Минусы**:
    - Отсутствует подробная документация для большинства функций и классов.
    - Не все переменные аннотированы типами.
    - Не используется модуль `logger` для логирования ошибок и информации.
    - Есть закомментированный код, который следует удалить.
    - Используются двойные кавычки вместо одинарных.
    - Не используются конструкции `with` для управления контекстом (например, при работе с прокси).

**Рекомендации по улучшению:**

1.  **Добавить документацию**:
    - Добавить docstring к классам и функциям, описывающие их назначение, аргументы, возвращаемые значения и возможные исключения.
    - Документация должна быть на русском языке в формате UTF-8.

2.  **Использовать `logger` для логирования**:
    - Заменить `print` на `logger.info` и `logger.error` для логирования информации и ошибок.
    - В случае ошибок передавать исключение в `logger.error` с `exc_info=True`.

3.  **Удалить закомментированный код**:
    - Удалить закомментированные строки кода, такие как `#random_proxy = get_random_proxy()` и `#proxies = {"http": random_proxy, "https": random_proxy}`.

4.  **Использовать одинарные кавычки**:
    - Заменить все двойные кавычки на одинарные, если это не влияет на функциональность.

5.  **Аннотировать типы переменных и параметров**:
    - Добавить аннотации типов для всех переменных и параметров функций.

6.  **Улучшить обработку исключений**:
    - Добавить логирование ошибок с использованием `logger.error` и `exc_info=True`.
    - Использовать `ex` вместо `e` в блоках `except`.

7. **Использовать конструкции `with` для управления контекстом**:
   - Это обеспечит корректное закрытие ресурсов и обработку ошибок.

8.  **Улучшить читаемость кода**:
    - Добавить пробелы вокруг операторов присваивания.
    - Переименовать переменные и функции для большей ясности.

**Оптимизированный код:**

```python
import os
import time
import json
import random
import threading
import re
import g4f
from g4f import ChatCompletion
from googletrans import Translator
from flask import request, Response
from datetime import datetime
from requests import get
from typing import Optional, List, Dict
from pathlib import Path

from src.logger import logger
from server.auto_proxy import get_random_proxy, update_working_proxies
from server.config import special_instructions


class Backend_Api:
    """
    Класс для обработки API-запросов бэкенда.
    ==============================================

    Инициализирует API-эндпоинты и управляет прокси-серверами.
    """

    def __init__(self, app, config: dict) -> None:
        """
        Инициализирует экземпляр класса Backend_Api.

        Args:
            app: Flask-приложение.
            config (dict): Конфигурация приложения.
        """
        self.app = app
        self.use_auto_proxy: bool = config['use_auto_proxy']
        self.routes: dict = {
            '/backend-api/v2/conversation': {
                'function': self._conversation,
                'methods': ['POST']
            }
        }

        if self.use_auto_proxy:
            update_proxies: threading.Thread = threading.Thread(
                target=update_working_proxies, daemon=True)
            update_proxies.start()

    def _conversation(self) -> Response | tuple[dict, int]:
        """
        Обрабатывает запрос на разговор с моделью.

        Returns:
            Response | tuple[dict, int]: Объект Response в случае успеха, либо кортеж (dict, int) в случае ошибки.
        """
        try:
            streaming: bool = request.json.get('stream', True)
            jailbreak: str = request.json['jailbreak']
            model: str = request.json['model']
            messages: list[dict] = build_messages(jailbreak)

            response = ChatCompletion.create(model=model, messages=messages)

            return self.app.response_class(generate_stream(response, jailbreak), mimetype='text/event-stream')

        except Exception as ex:
            logger.error('Произошла ошибка при обработке запроса conversation', ex, exc_info=True)
            return {
                '_action': '_ask',
                'success': False,
                "error": f"Произошла ошибка: {str(ex)}"
            }, 400


def build_messages(jailbreak: str) -> list[dict]:
    """
    Строит список сообщений для conversation.

    Args:
        jailbreak (str): Тип jailbreak.

    Returns:
        list[dict]: Список сообщений для conversation.
    """
    _conversation: list[dict] = request.json['meta']['content']['conversation']
    internet_access: bool = request.json['meta']['content']['internet_access']
    prompt: dict = request.json['meta']['content']['parts'][0]

    current_date: str = datetime.now().strftime("%Y-%m-%d")
    system_message: str = (
        f'You are ChatGPT also known as ChatGPT, a large language model trained by OpenAI. '
        f'Strictly follow the users instructions. '
        f'Current date: {current_date}. '
        f'{set_response_language(prompt)}'
    )

    conversation: list[dict] = [{'role': 'system', 'content': system_message}]

    conversation += _conversation

    conversation += fetch_search_results(
        prompt["content"]) if internet_access else []

    if jailbreak_instructions := isJailbreak(jailbreak):
        conversation += jailbreak_instructions

    conversation += [prompt]

    conversation: list[dict] = conversation[-13:] if len(
        conversation) > 12 else conversation

    return conversation


def fetch_search_results(query: str) -> list[dict]:
    """
    Получает результаты поиска из DuckDuckGo API.

    Args:
        query (str): Поисковый запрос.

    Returns:
        list[dict]: Список результатов поиска.
    """
    try:
        search = get(
            'https://ddg-api.herokuapp.com/search',
            params={
                'query': query,
                'limit': 5,
            })

        search.raise_for_status()  # Проверка на ошибки HTTP

        results: list[dict] = []
        snippets: str = ""

        for index, result in enumerate(search.json()):
            snippet = f'[{index + 1}] "{result["snippet"]}" URL:{result["link"]}.'
            snippets += snippet

        results.append({'role': 'system', 'content': snippets})
        return results

    except Exception as ex:
        logger.error(f'Ошибка при получении результатов поиска для запроса: {query}', ex, exc_info=True)
        return []


def generate_stream(response, jailbreak: str):
    """
    Генерирует поток сообщений.

    Args:
        response: Ответ от API.
        jailbreak (str): Тип jailbreak.

    Yields:
        str: Сообщение из потока.
    """
    if isJailbreak(jailbreak):
        response_jailbreak: str = ''
        jailbroken_checked: bool = False
        for message in response:
            response_jailbreak += message
            if jailbroken_checked:
                yield message
            else:
                if response_jailbroken_success(response_jailbreak):
                    jailbroken_checked = True
                if response_jailbroken_failed(response_jailbreak):
                    yield response_jailbreak
                    jailbroken_checked = True
    else:
        yield from response


def response_jailbroken_success(response: str) -> bool:
    """
    Проверяет, успешно ли выполнен jailbreak.

    Args:
        response (str): Ответ от API.

    Returns:
        bool: True, если jailbreak успешен, иначе False.
    """
    act_match = re.search(r'ACT:', response, flags=re.DOTALL)
    return bool(act_match)


def response_jailbroken_failed(response: str) -> bool:
    """
    Проверяет, не выполнен ли jailbreak.

    Args:
        response (str): Ответ от API.

    Returns:
        bool: True, если jailbreak не выполнен, иначе False.
    """
    return False if len(response) < 4 else not (response.startswith("GPT:") or response.startswith("ACT:"))


def set_response_language(prompt: dict) -> str:
    """
    Определяет язык ответа на основе языка запроса.

    Args:
        prompt (dict): Запрос пользователя.

    Returns:
        str: Строка с указанием языка ответа.
    """
    translator = Translator()
    detected_language: str = translator.detect(prompt['content']).lang
    return f"You will respond in the language: {detected_language}. "


def isJailbreak(jailbreak: str) -> Optional[List[Dict[str, str]]]:
    """
    Проверяет, является ли jailbreak допустимым.

    Args:
        jailbreak (str): Тип jailbreak.

    Returns:
        Optional[List[Dict[str, str]]]: Инструкции для jailbreak, если он допустим, иначе None.
    """
    if jailbreak != "Default":
        return special_instructions[jailbreak] if jailbreak in special_instructions else None
    else:
        return None