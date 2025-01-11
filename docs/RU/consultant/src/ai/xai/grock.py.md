# Анализ кода модуля `grock.py`

**Качество кода**
8
-  Плюсы
    - Код хорошо структурирован и разбит на отдельные функции, что облегчает понимание и поддержку.
    - Присутствует базовая документация для классов и методов.
    - Используется `requests.request` для отправки запросов, что предоставляет гибкость.
    - Обработка ошибок HTTP с помощью `response.raise_for_status()`.
-  Минусы
    - Отсутствует обработка ошибок на уровне приложения (например, при ошибках парсинга JSON).
    - Не используются константы для URL.
    - Не используется `from src.logger import logger`.
    -  Не соблюдено правило использования одинарных кавычек.
    -  Нет  документации в формате RST
    -  Нет обработки исключений при stream_chat_completion

**Рекомендации по улучшению**

1.  **Импорты**: Добавить импорт `logger` из `src.logger`.
2.  **Формат кода**: Использовать одинарные кавычки для строк в коде Python, двойные кавычки использовать только для вывода.
3.  **Константы**: Вынести базовый URL API в константу.
4.  **Логирование**: Добавить логирование ошибок с использованием `logger.error`.
5.  **Обработка ошибок**: Обернуть `json.loads` в `try-except` для обработки ошибок парсинга JSON и логировать их.
6.  **Документация**: Привести документацию в RST формат, включая описания аргументов и возвращаемых значений.
7.  **Обработка исключений** : Добавить обработку исключений в `stream_chat_completion`.

**Оптимизированный код**

```python
"""
Модуль для работы с API x.ai
=========================================================================================

Этот модуль содержит класс :class:`XAI`, который используется для взаимодействия с API x.ai,
включая запросы на завершение чата как в обычном режиме, так и с потоковой передачей.

Пример использования
--------------------

Пример использования класса `XAI`:

.. code-block:: python

    xai = XAI(api_key='your_api_key')
    messages = [
       {'role': 'system', 'content': 'You are a helpful assistant.'},
        {'role': 'user', 'content': 'Hello!'}
    ]
    response = xai.chat_completion(messages)
    print(response)
"""
import requests
# Импортируем logger
from src.logger import logger
import json
from typing import List, Dict, Any, Generator


class XAI:
    """
    Класс для взаимодействия с API x.ai.
    """

    BASE_URL = 'https://api.x.ai/v1'

    def __init__(self, api_key: str):
        """
        Инициализация класса XAI.

        Args:
            api_key (str): Ключ API для аутентификации.
        """
        self.api_key = api_key
        # Базовый URL API
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

    def _send_request(self, method: str, endpoint: str, data: dict = None) -> dict:
        """
        Отправка запроса к API x.ai.

        Args:
            method (str): Метод HTTP (GET, POST, PUT, DELETE).
            endpoint (str): Конечная точка API.
            data (dict, optional): Данные для отправки в теле запроса (для POST и PUT).

        Returns:
            dict: Ответ от API в формате JSON.

        Raises:
             requests.exceptions.HTTPError: Если статус ответа не 2xx.
        """
        url = f'{self.BASE_URL}/{endpoint}'
        response = requests.request(method, url, headers=self.headers, json=data)
        response.raise_for_status()  # Выбрасывает исключение, если статус ответа не 2xx
        return response.json()

    def chat_completion(self, messages: List[Dict[str, str]], model: str = 'grok-beta', stream: bool = False, temperature: int = 0) -> dict:
        """
        Запрос на завершение чата.

        Args:
            messages (List[Dict[str, str]]): Список сообщений для чата.
            model (str, optional): Модель для использования. Defaults to 'grok-beta'.
            stream (bool, optional): Флаг для включения потоковой передачи. Defaults to False.
            temperature (int, optional): Температура для генерации ответа. Defaults to 0.

        Returns:
            dict: Ответ от API в формате JSON.
        """
        endpoint = 'chat/completions'
        data = {
            'messages': messages,
            'model': model,
            'stream': stream,
            'temperature': temperature
        }
        response = self._send_request('POST', endpoint, data)
        return response

    def stream_chat_completion(self, messages: List[Dict[str, str]], model: str = 'grok-beta', temperature: int = 0) -> Generator[dict, None, None]:
        """
        Запрос на завершение чата с потоковой передачей.

        Args:
            messages (List[Dict[str, str]]): Список сообщений для чата.
            model (str, optional): Модель для использования. Defaults to 'grok-beta'.
            temperature (int, optional): Температура для генерации ответа. Defaults to 0.

        Returns:
             Generator[dict, None, None]: Поток ответов от API в формате JSON.
        """
        endpoint = 'chat/completions'
        data = {
            'messages': messages,
            'model': model,
            'stream': True,
            'temperature': temperature
        }
        url = f'{self.BASE_URL}/{endpoint}'
        try:
            response = requests.post(url, headers=self.headers, json=data, stream=True)
            response.raise_for_status()
            for line in response.iter_lines(decode_unicode=True):
                if line.strip():
                    try:
                        # Код исполняет преобразование JSON строки в словарь
                        yield json.loads(line)
                    except json.JSONDecodeError as e:
                         #  Логирование ошибки при парсинге JSON
                        logger.error(f'Ошибка парсинга JSON: {e}')
                        continue
        except requests.exceptions.RequestException as e:
             #  Логирование ошибки запроса
            logger.error(f'Ошибка при выполнении запроса: {e}')
            return

# Пример использования класса XAI
if __name__ == '__main__':
    api_key = 'your_api_key_here'  # Замените на ваш реальный API-ключ
    xai = XAI(api_key)

    messages = [
        {
            'role': 'system',
            'content': 'You are Grok, a chatbot inspired by the Hitchhikers Guide to the Galaxy.'
        },
        {
            'role': 'user',
            'content': 'What is the answer to life and universe?'
        }
    ]

    # Непотоковый запрос
    completion_response = xai.chat_completion(messages)
    print('Non-streaming response:', completion_response)

    # Потоковый запрос
    stream_response = xai.stream_chat_completion(messages)
    print('Streaming response:')
    for line in stream_response:
        print(line)
```