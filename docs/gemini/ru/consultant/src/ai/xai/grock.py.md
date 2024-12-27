# Анализ кода модуля `grock.py`

**Качество кода**

8
-  Плюсы
    - Код предоставляет базовую функциональность для взаимодействия с API x.ai, включая запросы на завершение чата (потоковые и непотоковые).
    - Используется `requests` для выполнения HTTP-запросов, что является стандартной практикой.
    - Код хорошо структурирован и разбит на логические функции.
    - Присутствует пример использования в блоке `if __name__ == "__main__":`.
    - Присутствуют docstring для классов и методов.
-  Минусы
    - Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Отсутствует обработка ошибок с использованием `logger.error`.
    - Не все комментарии оформлены в формате reStructuredText (RST).
    - Присутствует жестко заданный `base_url`.
    - Не используются константы для значений по умолчанию, таких как модель "grok-beta".
    - В примере использования необходимо заменить api_key вручную.

**Рекомендации по улучшению**

1.  Использовать `j_loads` для обработки JSON ответов.
2.  Добавить логирование ошибок с использованием `logger.error` вместо `response.raise_for_status()`.
3.  Переписать docstring в формате reStructuredText (RST) и добавить более подробное описание.
4.  Использовать константы для `base_url` и `model="grok-beta"`.
5.  Удалить пример использования в `if __name__ == "__main__"`, так как это не является частью модуля.
6.  Улучшить обработку ошибок в методах `_send_request` и `stream_chat_completion`.
7.  Добавить проверку на наличие `api_key` при инициализации класса.
8.  Улучшить читаемость кода, добавив константы для ключей словарей.
9.  Добавить импорт необходимых модулей.

**Оптимизиробанный код**

```python
"""
Модуль для взаимодействия с API x.ai
====================================

Этот модуль предоставляет класс :class:`XAI`, который используется для взаимодействия с API x.ai
для выполнения задач, таких как завершение чата (потоковое и непотоковое).

Пример использования
--------------------

Пример использования класса `XAI`:

.. code-block:: python

    xai = XAI(api_key="your_api_key")
    messages = [
        {"role": "user", "content": "Hello, how are you?"}
    ]
    response = xai.chat_completion(messages)
    print(response)
"""
import requests
import json
from typing import List, Dict, Any, Iterator
from src.logger.logger import logger
from src.utils.jjson import j_loads

BASE_URL = "https://api.x.ai/v1"
DEFAULT_MODEL = "grok-beta"
ROLE = "role"
CONTENT = "content"
MESSAGES = "messages"
MODEL = "model"
STREAM = "stream"
TEMPERATURE = "temperature"

class XAI:
    """
    Класс для взаимодействия с API x.ai.

    :param api_key: Ключ API для аутентификации.
    :raises ValueError: Если `api_key` не предоставлен.
    """
    def __init__(self, api_key: str):
        if not api_key:
            raise ValueError("API key is required")
        self.api_key = api_key
        self.base_url = BASE_URL  # Базовый URL API
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def _send_request(self, method: str, endpoint: str, data: Dict = None) -> Dict:
        """
        Отправляет запрос к API x.ai.

        :param method: Метод HTTP (GET, POST, PUT, DELETE).
        :param endpoint: Конечная точка API.
        :param data: Данные для отправки в теле запроса (для POST и PUT).
        :return: Ответ от API.
        :raises Exception: Если возникает ошибка при отправке запроса или при обработке ответа.
        """
        url = f"{self.base_url}/{endpoint}"
        try:
            # отправка запроса к API
            response = requests.request(method, url, headers=self.headers, json=data)
            response.raise_for_status()
            # обработка JSON ответа
            return j_loads(response.text)
        except requests.exceptions.RequestException as ex:
            # логирование ошибки при отправке запроса
            logger.error(f"Error during request to {url}: {ex}")
            raise
        except json.JSONDecodeError as ex:
            # логирование ошибки при декодировании JSON
            logger.error(f"Error decoding JSON response from {url}: {ex}")
            raise
        except Exception as ex:
            # логирование других ошибок
            logger.error(f"An unexpected error occurred: {ex}")
            raise

    def chat_completion(self, messages: List[Dict], model: str = DEFAULT_MODEL, stream: bool = False, temperature: float = 0) -> Dict:
        """
        Запрос на завершение чата.

        :param messages: Список сообщений для чата.
        :param model: Модель для использования.
        :param stream: Флаг для включения потоковой передачи.
        :param temperature: Температура для генерации ответа.
        :return: Ответ от API.
        """
        endpoint = "chat/completions"
        data = {
            MESSAGES: messages,
            MODEL: model,
            STREAM: stream,
            TEMPERATURE: temperature
        }
        # отправка запроса на завершение чата
        return self._send_request("POST", endpoint, data)

    def stream_chat_completion(self, messages: List[Dict], model: str = DEFAULT_MODEL, temperature: float = 0) -> Iterator[str]:
        """
        Запрос на завершение чата с потоковой передачей.

        :param messages: Список сообщений для чата.
        :param model: Модель для использования.
        :param temperature: Температура для генерации ответа.
        :return: Поток ответов от API.
        :raises Exception: Если возникает ошибка при отправке потокового запроса.
        """
        endpoint = "chat/completions"
        data = {
            MESSAGES: messages,
            MODEL: model,
            STREAM: True,
            TEMPERATURE: temperature
        }
        url = f"{self.base_url}/{endpoint}"
        try:
            # отправка потокового запроса
            response = requests.post(url, headers=self.headers, json=data, stream=True)
            response.raise_for_status()
            # возвращает итератор для обработки потока данных
            return response.iter_lines(decode_unicode=True)
        except requests.exceptions.RequestException as ex:
            # логирование ошибок при отправке потокового запроса
            logger.error(f"Error during stream request to {url}: {ex}")
            raise
```