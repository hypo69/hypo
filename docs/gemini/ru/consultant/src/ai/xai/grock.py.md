# Анализ кода модуля `grock.py`

**Качество кода**
-  Соответствие требованиям по оформлению кода: 7/10
    -  Плюсы:
        - Код относительно хорошо структурирован и понятен.
        - Используются docstring для описания классов и методов.
        - Присутствует базовая обработка ошибок с помощью `response.raise_for_status()`.
    - Минусы:
        - Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson`.
        - Отсутствует использование `from src.logger.logger import logger` для логирования ошибок.
        - Некоторые комментарии не соответствуют reStructuredText.
        - Нет обработки ошибок в `stream_chat_completion`, кроме `response.raise_for_status()`.
        - Отсутствует обработка ошибок при чтении потоковых данных.
        - Нет проверки типа `api_key` при инициализации класса.
        - Нет обработки ошибок в блоке `if __name__ == "__main__":`
        - Не используется константа для `https://api.x.ai/v1`.
        - `if line.strip():` избыточно, можно перенести логику обработки в генератор.

**Рекомендации по улучшению**

1.  **Импорты**: Добавить недостающие импорты, такие как `Any` из `typing`, `j_loads` из `src.utils.jjson`, и `logger` из `src.logger.logger`.
2.  **Формат документации**: Переписать все docstring и комментарии в формате reStructuredText (RST).
3.  **Обработка данных**: Использовать `j_loads` для обработки JSON из потокового ответа.
4.  **Логирование**: Добавить логирование ошибок с помощью `logger.error`.
5.  **Рефакторинг**:
    -   В `_send_request` добавить обработку ошибок `requests.exceptions.RequestException`.
    -   В `stream_chat_completion` добавить обработку ошибок при итерации по потоку.
    -   Использовать константу для базового URL.
    -   Упростить обработку потока в `stream_chat_completion`.
    -   Добавить проверку типа `api_key` при инициализации класса.
    -   Добавить обработку ошибок в блоке `if __name__ == "__main__":`

**Оптимизированный код**

```python
"""
Модуль для взаимодействия с API x.ai.
=========================================================================================

Этот модуль содержит класс :class:`XAI`, который используется для
взаимодействия с API x.ai для выполнения задач, связанных с генерацией текста.

Пример использования
--------------------

Пример использования класса `XAI`:

.. code-block:: python

    api_key = "your_api_key_here"  # Замените на ваш реальный API-ключ
    xai = XAI(api_key)

    messages = [
        {
            "role": "system",
            "content": "You are Grok, a chatbot inspired by the Hitchhikers Guide to the Galaxy."
        },
        {
            "role": "user",
            "content": "What is the answer to life and universe?"
        }
    ]

    # Непотоковый запрос
    completion_response = xai.chat_completion(messages)
    print("Non-streaming response:", completion_response)

    # Потоковый запрос
    stream_response = xai.stream_chat_completion(messages)
    print("Streaming response:")
    for line in stream_response:
        print(line)
"""
import requests
from typing import Any, List, Dict, Generator
#  импортируем j_loads для обработки json
from src.utils.jjson import j_loads
#  импортируем logger для логирования
from src.logger.logger import logger
#  Константа для базового URL
BASE_URL = "https://api.x.ai/v1"

class XAI:
    """
    Класс для взаимодействия с API x.ai.
    """
    def __init__(self, api_key: str):
        """
        Инициализация класса XAI.

        :param api_key: Ключ API для аутентификации.
        :raises TypeError: Если `api_key` не является строкой.
        """
        if not isinstance(api_key, str):
            # Проверка типа api_key
            raise TypeError('api_key must be a string')
        self.api_key = api_key
        #  Устанавливаем базовый URL
        self.base_url = BASE_URL
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def _send_request(self, method: str, endpoint: str, data: dict = None) -> dict:
        """
        Отправка запроса к API x.ai.

        :param method: Метод HTTP (GET, POST, PUT, DELETE).
        :param endpoint: Конечная точка API.
        :param data: Данные для отправки в теле запроса (для POST и PUT).
        :return: Ответ от API в формате JSON.
        :raises requests.exceptions.RequestException: Если возникает ошибка при отправке запроса.
        """
        url = f"{self.base_url}/{endpoint}"
        try:
            # отправляем запрос к API
            response = requests.request(method, url, headers=self.headers, json=data)
            # выбрасывает исключение, если статус ответа не 2xx
            response.raise_for_status()
            # возвращаем json
            return response.json()
        except requests.exceptions.RequestException as ex:
            # Логируем ошибку при отправке запроса
            logger.error(f'Ошибка при отправке запроса к {url}', exc_info=ex)
            raise

    def chat_completion(self, messages: List[Dict[str, str]], model: str = "grok-beta", stream: bool = False, temperature: int = 0) -> dict:
        """
        Запрос на завершение чата.

        :param messages: Список сообщений для чата.
        :param model: Модель для использования.
        :param stream: Флаг для включения потоковой передачи.
        :param temperature: Температура для генерации ответа.
        :return: Ответ от API в формате JSON.
        """
        endpoint = "chat/completions"
        data = {
            "messages": messages,
            "model": model,
            "stream": stream,
            "temperature": temperature
        }
        # отправляем запрос
        return self._send_request("POST", endpoint, data)

    def stream_chat_completion(self, messages: List[Dict[str, str]], model: str = "grok-beta", temperature: int = 0) -> Generator[dict, None, None]:
        """
        Запрос на завершение чата с потоковой передачей.

        :param messages: Список сообщений для чата.
        :param model: Модель для использования.
        :param temperature: Температура для генерации ответа.
        :return: Генератор, выдающий ответы от API в формате JSON.
        :raises requests.exceptions.RequestException: Если возникает ошибка при отправке запроса.
        """
        endpoint = "chat/completions"
        data = {
            "messages": messages,
            "model": model,
            "stream": True,
            "temperature": temperature
        }
        url = f"{self.base_url}/{endpoint}"
        try:
             # отправляем запрос с потоком
            response = requests.post(url, headers=self.headers, json=data, stream=True)
            # выбрасываем исключение если статус код не 200
            response.raise_for_status()
            # преобразовываем поток
            for line in response.iter_lines(decode_unicode=True):
                if line:
                    # обрабатываем json
                    yield j_loads(line)
        except requests.exceptions.RequestException as ex:
            # логируем ошибку
            logger.error(f'Ошибка при запросе потока к {url}', exc_info=ex)
            raise
        except json.JSONDecodeError as ex:
            # логируем ошибку
            logger.error(f'Ошибка при декодировании JSON', exc_info=ex)
            raise

# Пример использования класса XAI
if __name__ == "__main__":
    try:
        #  замените на ваш реальный API-ключ
        api_key = "your_api_key_here"
        xai = XAI(api_key)

        messages = [
            {
                "role": "system",
                "content": "You are Grok, a chatbot inspired by the Hitchhikers Guide to the Galaxy."
            },
            {
                "role": "user",
                "content": "What is the answer to life and universe?"
            }
        ]

        # Непотоковый запрос
        completion_response = xai.chat_completion(messages)
        print("Non-streaming response:", completion_response)

        # Потоковый запрос
        stream_response = xai.stream_chat_completion(messages)
        print("Streaming response:")
        for line in stream_response:
            print(line)
    except Exception as ex:
         # логируем ошибку
        logger.error(f'Произошла ошибка', exc_info=ex)
```