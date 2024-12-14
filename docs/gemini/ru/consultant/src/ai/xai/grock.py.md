# Анализ кода модуля `grock.py`

**Качество кода**

**Оценка: 7/10**
-  **Плюсы**
    - Код хорошо структурирован и разбит на логические блоки.
    - Используется класс `XAI` для инкапсуляции логики работы с API.
    - Присутствуют docstring для классов и методов, что облегчает понимание кода.
    - Обработка ошибок HTTP через `response.raise_for_status()`.
    - Есть пример использования класса в блоке `if __name__ == "__main__":`.
-  **Минусы**
    - Отсутствует обработка исключений в `stream_chat_completion`.
    - Не используется `j_loads` или `j_loads_ns` для работы с `json`, как указано в инструкции.
    - Нет логирования ошибок через `src.logger.logger`.
    - Некоторые комментарии не соответствуют формату RST.
    - Использование `print` для вывода, вместо логирования.
    - Отсутствуют необходимые импорты из `src.utils.jjson` и `src.logger.logger`.

**Рекомендации по улучшению**
1.  Использовать `j_loads` или `j_loads_ns` для разбора JSON в `stream_chat_completion`.
2.  Добавить обработку исключений в `stream_chat_completion` и логировать их с помощью `logger.error`.
3.  Импортировать и использовать `logger` для логирования.
4.  Переписать все комментарии в формате RST, как указано в инструкции.
5.  Удалить использование `print` для вывода, и заменить на логирование через `logger`.
6.  Убедиться в правильности всех импортов.

**Оптимизированный код**

```python
"""
Модуль для взаимодействия с API x.ai
=========================================================================================

Этот модуль содержит класс :class:`XAI`, который используется для взаимодействия с API x.ai для выполнения задач чат-бота.

Пример использования
--------------------

Пример использования класса `XAI`:

.. code-block:: python

    xai = XAI(api_key='your_api_key_here')
    messages = [
        {"role": "system", "content": "You are Grok, a chatbot"},
        {"role": "user", "content": "What is the answer?"}
    ]
    completion_response = xai.chat_completion(messages)
    print(completion_response)
"""
import requests
from typing import List, Dict, Any
from src.utils.jjson import j_loads # импортируем j_loads из src.utils.jjson
from src.logger.logger import logger # импортируем logger из src.logger.logger

class XAI:
    """
    Класс для взаимодействия с API x.ai.

    :param api_key: Ключ API для аутентификации.
    """
    def __init__(self, api_key: str):
        """
        Инициализация класса XAI.
        """
        self.api_key = api_key
        self.base_url = "https://api.x.ai/v1"  # Базовый URL API
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
        """
        url = f"{self.base_url}/{endpoint}"
        #  отправляем запрос к API
        try:
            response = requests.request(method, url, headers=self.headers, json=data)
            response.raise_for_status()  #  Выбрасывает исключение, если статус ответа не 2xx
            return response.json()
        except requests.exceptions.RequestException as ex:
            logger.error(f'Ошибка при отправке запроса к API: {ex}')
            return {} # возвращаем пустой словарь в случае ошибки

    def chat_completion(self, messages: List[Dict[str, str]], model: str = "grok-beta", stream: bool = False, temperature: float = 0) -> dict:
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
        #  отправляем запрос на завершение чата
        return self._send_request("POST", endpoint, data)

    def stream_chat_completion(self, messages: List[Dict[str, str]], model: str = "grok-beta", temperature: float = 0) -> Any:
        """
        Запрос на завершение чата с потоковой передачей.

        :param messages: Список сообщений для чата.
        :param model: Модель для использования.
        :param temperature: Температура для генерации ответа.
        :return: Поток ответов от API.
        """
        endpoint = "chat/completions"
        data = {
            "messages": messages,
            "model": model,
            "stream": True,
            "temperature": temperature
        }
        url = f"{self.base_url}/{endpoint}"
        #  отправляем запрос на завершение чата с потоковой передачей
        try:
            response = requests.post(url, headers=self.headers, json=data, stream=True)
            response.raise_for_status()
            for line in response.iter_lines(decode_unicode=True):
                if line.strip():
                    #  Используем j_loads для разбора JSON
                    yield j_loads(line)
        except requests.exceptions.RequestException as ex:
            logger.error(f'Ошибка при потоковой передаче запроса: {ex}')
            return

# Пример использования класса XAI
if __name__ == "__main__":
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

    #  Непотоковый запрос
    completion_response = xai.chat_completion(messages)
    logger.info(f"Non-streaming response: {completion_response}")

    #  Потоковый запрос
    stream_response = xai.stream_chat_completion(messages)
    logger.info("Streaming response:")
    if stream_response:
      for line in stream_response:
        logger.info(line)
```