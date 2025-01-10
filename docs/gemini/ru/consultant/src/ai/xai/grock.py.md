# Анализ кода модуля `grock.py`

**Качество кода**
7
- Плюсы
    - Код достаточно хорошо структурирован и имеет базовую функциональность для работы с API x.ai.
    - Присутствует документация к классам и методам.
    - Использование `response.raise_for_status()` для обработки ошибок HTTP.
- Минусы
    - Отсутствуют необходимые импорты для логирования.
    - Используется стандартный `json.loads` вместо `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Не используется единый подход к обработке ошибок через `logger.error` в методах.
    - В документации не используется формат RST для Sphinx.
    - Не хватает обработки ошибок в потоковом методе.

**Рекомендации по улучшению**

1.  Добавить необходимые импорты: `from src.logger.logger import logger`, `from src.utils.jjson import j_loads`
2.  Использовать `j_loads` из `src.utils.jjson` вместо стандартного `json.loads`.
3.  Переработать обработку ошибок, используя `logger.error` вместо общих `except Exception`.
4.  Дополнить docstring в формате RST для Sphinx.
5.  Улучшить документацию, добавив примеры использования.
6.  Добавить обработку ошибок в методе `stream_chat_completion`.
7.  Привести к единому виду кавычки в коде. Использовать одинарные кавычки (`'`) в Python коде, двойные (`"`) - только в операциях вывода.

**Оптимизированный код**

```python
"""
Модуль для взаимодействия с API X.ai.
=========================================================================================

Этот модуль содержит класс :class:`XAI`, который используется для взаимодействия с API x.ai
для выполнения задач по обработки чата.

Пример использования
--------------------

Пример использования класса `XAI`:

.. code-block:: python

    api_key = 'your_api_key_here'
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

    completion_response = xai.chat_completion(messages)
    print('Non-streaming response:', completion_response)

    stream_response = xai.stream_chat_completion(messages)
    print('Streaming response:')
    for line in stream_response:
        if line.strip():
            print(j_loads(line))
"""
import requests
#  Импорт j_loads из src.utils.jjson
from src.utils.jjson import j_loads
#  Импорт logger из src.logger.logger
from src.logger.logger import logger


class XAI:
    """
    Класс для взаимодействия с API x.ai.
    """
    def __init__(self, api_key: str):
        """
        Инициализирует класс XAI.

        :param api_key: Ключ API для аутентификации.
        :type api_key: str
        """
        self.api_key = api_key
        #  Базовый URL API
        self.base_url = 'https://api.x.ai/v1'
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

    def _send_request(self, method: str, endpoint: str, data: dict = None) -> dict:
        """
        Отправляет запрос к API x.ai.

        :param method: Метод HTTP (GET, POST, PUT, DELETE).
        :type method: str
        :param endpoint: Конечная точка API.
        :type endpoint: str
        :param data: Данные для отправки в теле запроса (для POST и PUT).
        :type data: dict
        :raises requests.exceptions.HTTPError: Если статус ответа не 2xx.
        :return: Ответ от API.
        :rtype: dict
        """
        url = f'{self.base_url}/{endpoint}'
        try:
            #  Код отправляет запрос к API
            response = requests.request(method, url, headers=self.headers, json=data)
            response.raise_for_status() #  Код выбрасывает исключение, если статус ответа не 2xx
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f'Ошибка при отправке запроса к API: {e}')
            return {}


    def chat_completion(self, messages: list, model: str = 'grok-beta', stream: bool = False, temperature: int = 0) -> dict:
        """
        Отправляет запрос на завершение чата.

        :param messages: Список сообщений для чата.
        :type messages: list
        :param model: Модель для использования.
        :type model: str
        :param stream: Флаг для включения потоковой передачи.
        :type stream: bool
        :param temperature: Температура для генерации ответа.
        :type temperature: int
        :return: Ответ от API.
        :rtype: dict
        """
        endpoint = 'chat/completions'
        data = {
            'messages': messages,
            'model': model,
            'stream': stream,
            'temperature': temperature
        }
        # Код отправляет запрос и возвращает ответ
        response = self._send_request('POST', endpoint, data)
        return response

    def stream_chat_completion(self, messages: list, model: str = 'grok-beta', temperature: int = 0) -> iter:
        """
        Отправляет запрос на завершение чата с потоковой передачей.

        :param messages: Список сообщений для чата.
        :type messages: list
        :param model: Модель для использования.
        :type model: str
        :param temperature: Температура для генерации ответа.
        :type temperature: int
         :raises requests.exceptions.HTTPError: Если статус ответа не 2xx.
        :return: Поток ответов от API.
        :rtype: iter
        """
        endpoint = 'chat/completions'
        data = {
            'messages': messages,
            'model': model,
            'stream': True,
            'temperature': temperature
        }
        url = f'{self.base_url}/{endpoint}'
        try:
            #  Код отправляет POST запрос к API
            response = requests.post(url, headers=self.headers, json=data, stream=True)
            response.raise_for_status() #  Код выбрасывает исключение, если статус ответа не 2xx
            # Код возвращает итератор по строкам ответа
            return response.iter_lines(decode_unicode=True)
        except requests.exceptions.RequestException as e:
            logger.error(f'Ошибка при отправке потокового запроса к API: {e}')
            return iter([])

# Пример использования класса XAI
if __name__ == '__main__':
    #  Замените на ваш реальный API-ключ
    api_key = 'your_api_key_here'
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

    #  Непотоковый запрос
    completion_response = xai.chat_completion(messages)
    print('Non-streaming response:', completion_response)

    #  Потоковый запрос
    stream_response = xai.stream_chat_completion(messages)
    print('Streaming response:')
    for line in stream_response:
        if line.strip():
            print(j_loads(line))
```