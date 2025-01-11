# Анализ кода модуля xAI API Client

**Качество кода**
8
 -  Плюсы
    - Документ содержит подробное описание модуля, его функциональности и примеров использования.
    - Приведены инструкции по установке и базовому использованию клиента.
    - Есть разделение на не-стриминговый и стриминговый запросы, что облегчает понимание различий между ними.
 -  Минусы
    - Отсутствует описание структуры кода.
    - Нет документации к функциям и классам в формате RST.
    - Не используются логирование.
    -  В коде не соблюдены требования по использованию одинарных кавычек, json.loads

**Рекомендации по улучшению**
1. Добавить описание структуры кода, классов и методов.
2. Привести документацию к формату RST, что облегчит интеграцию с инструментами документации.
3. Добавить логирование для отслеживания ошибок и дебага.
4. Использовать `j_loads` для обработки `json`.
5. Исправить использование кавычек в коде Python в соответствии с требованиями.
6. Добавить проверку наличия API key.
7. Добавить обработку ошибок при запросах к API.
8. Обогатить документацию примерами использования и возможными вариантами.

**Оптимизированный код**
```python
"""
xAI API Client
=========================================================================================

Этот модуль содержит класс `XAI`, который используется для взаимодействия с xAI API.
Клиент предназначен для упрощения процесса отправки запросов к xAI API, включая как стандартные, так и потоковые запросы.

Пример использования
--------------------

Пример использования класса `XAI`:

.. code-block:: python

    from xai import XAI

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
from src.utils.jjson import j_loads  # импортируем j_loads
from src.logger.logger import logger # импортируем logger


class XAI:
    """
    Класс для взаимодействия с xAI API.

    Args:
        api_key (str): API ключ для xAI.

    Attributes:
        api_key (str): API ключ для xAI.
        base_url (str): Базовый URL для xAI API.

    """
    def __init__(self, api_key: str):
        """
        Инициализация класса XAI.

        Args:
             api_key (str): API ключ для xAI.
        """
        self.api_key = api_key
        self.base_url = 'https://api.x.ai'  # Базовый URL для xAI API.

    def chat_completion(self, messages: list) -> dict:
        """
        Отправляет запрос на завершение чата в xAI API.

        Args:
            messages (list): Список сообщений для чата.

        Returns:
            dict: Ответ от xAI API в виде словаря.

        Raises:
            Exception: В случае ошибки при отправке запроса или обработки ответа.

        Example:
        >>> api_key = 'your_api_key_here'
        >>> xai = XAI(api_key)
        >>> messages = [
        ...     {
        ...         'role': 'system',
        ...         'content': 'You are Grok, a chatbot inspired by the Hitchhikers Guide to the Galaxy.'
        ...     },
        ...     {
        ...         'role': 'user',
        ...         'content': 'What is the answer to life and universe?'
        ...     }
        ... ]
        >>> response = xai.chat_completion(messages)
        >>> print(response)
        {'choices': [{'message': {'role': 'assistant', 'content': '42.'}}]}
        """
        if not self.api_key:
            logger.error('API key is not provided.') #Проверка наличия API key
            return {}

        url = f'{self.base_url}/v1/chat/completions'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'
        }
        data = {
            'model': 'grok-1',
            'messages': messages
        }

        try:
             # Отправляет запрос к API
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()  # Проверяет статус код ответа
            return response.json() # Возвращает json
        except requests.exceptions.RequestException as e:
            logger.error(f'Error during request to {url}: {e}') #Логируем ошибку
            return {}
        except Exception as e:
             #Логируем любую другую ошибку
            logger.error(f'Error during processing response: {e}')
            return {}

    def stream_chat_completion(self, messages: list) -> str:
        """
        Отправляет запрос на потоковое завершение чата в xAI API.

        Args:
            messages (list): Список сообщений для чата.

        Yields:
            str: Строки из потокового ответа от xAI API.

        Raises:
            Exception: В случае ошибки при отправке запроса или обработки ответа.

        Example:
        >>> api_key = 'your_api_key_here'
        >>> xai = XAI(api_key)
        >>> messages = [
        ...     {
        ...         'role': 'system',
        ...         'content': 'You are Grok, a chatbot inspired by the Hitchhikers Guide to the Galaxy.'
        ...     },
        ...     {
        ...         'role': 'user',
        ...         'content': 'What is the answer to life and universe?'
        ...     }
        ... ]
        >>> for line in xai.stream_chat_completion(messages):
        ...     if line.strip():
        ...         print(j_loads(line))
        {'choices': [{'delta': {'content': '42.'}}]}

        """
        if not self.api_key:
            logger.error('API key is not provided.')# Проверка наличия API key
            return

        url = f'{self.base_url}/v1/chat/completions'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'
        }
        data = {
            'model': 'grok-1',
            'messages': messages,
            'stream': True
        }
        try:
            # Код исполняет отправку запроса к API
            response = requests.post(url, headers=headers, json=data, stream=True)
            response.raise_for_status()
            for line in response.iter_lines():
                if line:
                    yield line.decode('utf-8')
        except requests.exceptions.RequestException as e:
           # Логируем ошибку запроса
            logger.error(f'Error during streaming request to {url}: {e}')
            return
        except Exception as e:
           # Логируем любую другую ошибку
            logger.error(f'Error during streaming response processing: {e}')
            return
```
```python
# xAI API Client
#
# ## Overview
#
# This repository contains a Python client for interacting with the xAI API. The client is designed to simplify the process of making requests to the xAI API, including both standard and streaming requests.
#
# ## Features
#
# - **Authentication**: Securely authenticate your requests using your xAI API key.
# - **Chat Completion**: Generate responses from the xAI models using the `chat_completion` method.
# - **Streaming Responses**: Stream responses from the xAI models using the `stream_chat_completion` method.
#
# ## Installation
#
# To use this client, you need to have Python installed on your system. You can install the required dependencies using pip:
#
# ```bash
# pip install requests
# ```
#
# ## Usage
#
# ### Initialization
#
# First, initialize the `XAI` class with your API key:
#
# ```python
# from xai import XAI
#
# api_key = "your_api_key_here"  # Replace with your actual API key
# xai = XAI(api_key)
# ```
#
# ### Chat Completion
#
# To generate a response from the xAI model, use the `chat_completion` method:
#
# ```python
# messages = [
#     {
#         "role": "system",
#         "content": "You are Grok, a chatbot inspired by the Hitchhikers Guide to the Galaxy."
#     },
#     {
#         "role": "user",
#         "content": "What is the answer to life and universe?"
#     }
# ]
#
# completion_response = xai.chat_completion(messages)
# print("Non-streaming response:", completion_response)
# ```
#
# ### Streaming Chat Completion
#
# To stream responses from the xAI model, use the `stream_chat_completion` method:
#
# ```python
# stream_response = xai.stream_chat_completion(messages)
# print("Streaming response:")
# for line in stream_response:
#     if line.strip():
#         print(json.loads(line))
# ```
#
# ## Example
#
# Here is a complete example of how to use the `XAI` client:
#
# ```python
# import json
# from xai import XAI
#
# api_key = "your_api_key_here"  # Replace with your actual API key
# xai = XAI(api_key)
#
# messages = [
#     {
#         "role": "system",
#         "content": "You are Grok, a chatbot inspired by the Hitchhikers Guide to the Galaxy."
#     },
#     {
#         "role": "user",
#         "content": "What is the answer to life and universe?"
#     }
# ]
#
# # Non-streaming request
# completion_response = xai.chat_completion(messages)
# print("Non-streaming response:", completion_response)
#
# # Streaming request
# stream_response = xai.stream_chat_completion(messages)
# print("Streaming response:")
# for line in stream_response:
#     if line.strip():
#         print(json.loads(line))
# ```
#
# ## Contributing
#
# Contributions are welcome! Please feel free to submit a pull request or open an issue if you encounter any problems or have suggestions for improvements.
#
# ## License
#
# This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
#
# ## Acknowledgments
#
# - Thanks to xAI for providing the API that powers this client.
# - Inspired by the need for a simple and efficient way to interact with xAI\'s powerful models.
#
# ---
#
# For more information, please refer to the [xAI API documentation](https://api.x.ai/docs).
#
# https://console.x.ai/team/4cd3d20f-f1d9-4389-9ffb-87c855e5ffac
# https://docs.x.ai/docs
"""
# xAI API Client
# =========================================================================================
#
# Этот модуль содержит класс `XAI`, который используется для взаимодействия с xAI API.
# Клиент предназначен для упрощения процесса отправки запросов к xAI API, включая как стандартные, так и потоковые запросы.
#
# Пример использования
# --------------------
#
# Пример использования класса `XAI`:
#
# .. code-block:: python
#
#     from xai import XAI
#
#     api_key = 'your_api_key_here'
#     xai = XAI(api_key)
#
#     messages = [
#         {
#             'role': 'system',
#             'content': 'You are Grok, a chatbot inspired by the Hitchhikers Guide to the Galaxy.'
#         },
#         {
#             'role': 'user',
#             'content': 'What is the answer to life and universe?'
#         }
#     ]
#
#     completion_response = xai.chat_completion(messages)
#     print('Non-streaming response:', completion_response)
#
#     stream_response = xai.stream_chat_completion(messages)
#     print('Streaming response:')
#     for line in stream_response:
#         if line.strip():
#             print(j_loads(line))
# """
import requests
# from src.utils.jjson import j_loads  # импортируем j_loads
# from src.logger.logger import logger # импортируем logger
from src.utils.jjson import j_loads
from src.logger.logger import logger

class XAI:
    """
    Класс для взаимодействия с xAI API.

    Args:
        api_key (str): API ключ для xAI.

    Attributes:
        api_key (str): API ключ для xAI.
        base_url (str): Базовый URL для xAI API.

    """
    def __init__(self, api_key: str):
        """
        Инициализация класса XAI.

        Args:
             api_key (str): API ключ для xAI.
        """
        self.api_key = api_key
        self.base_url = 'https://api.x.ai'  # Базовый URL для xAI API.

    def chat_completion(self, messages: list) -> dict:
        """
        Отправляет запрос на завершение чата в xAI API.

        Args:
            messages (list): Список сообщений для чата.

        Returns:
            dict: Ответ от xAI API в виде словаря.

        Raises:
            Exception: В случае ошибки при отправке запроса или обработки ответа.

        Example:
        >>> api_key = 'your_api_key_here'
        >>> xai = XAI(api_key)
        >>> messages = [
        ...     {
        ...         'role': 'system',
        ...         'content': 'You are Grok, a chatbot inspired by the Hitchhikers Guide to the Galaxy.'
        ...     },
        ...     {
        ...         'role': 'user',
        ...         'content': 'What is the answer to life and universe?'
        ...     }
        ... ]
        >>> response = xai.chat_completion(messages)
        >>> print(response)
        {'choices': [{'message': {'role': 'assistant', 'content': '42.'}}]}
        """
        if not self.api_key:
            logger.error('API key is not provided.') #Проверка наличия API key
            return {}

        url = f'{self.base_url}/v1/chat/completions'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'
        }
        data = {
            'model': 'grok-1',
            'messages': messages
        }

        try:
             # Отправляет запрос к API
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()  # Проверяет статус код ответа
            return response.json() # Возвращает json
        except requests.exceptions.RequestException as e:
            logger.error(f'Error during request to {url}: {e}') #Логируем ошибку
            return {}
        except Exception as e:
             #Логируем любую другую ошибку
            logger.error(f'Error during processing response: {e}')
            return {}

    def stream_chat_completion(self, messages: list) -> str:
        """
        Отправляет запрос на потоковое завершение чата в xAI API.

        Args:
            messages (list): Список сообщений для чата.

        Yields:
            str: Строки из потокового ответа от xAI API.

        Raises:
            Exception: В случае ошибки при отправке запроса или обработки ответа.

        Example:
        >>> api_key = 'your_api_key_here'
        >>> xai = XAI(api_key)
        >>> messages = [
        ...     {
        ...         'role': 'system',
        ...         'content': 'You are Grok, a chatbot inspired by the Hitchhikers Guide to the Galaxy.'
        ...     },
        ...     {
        ...         'role': 'user',
        ...         'content': 'What is the answer to life and universe?'
        ...     }
        ... ]
        >>> for line in xai.stream_chat_completion(messages):
        ...     if line.strip():
        ...         print(j_loads(line))
        {'choices': [{'delta': {'content': '42.'}}]}

        """
        if not self.api_key:
            logger.error('API key is not provided.')# Проверка наличия API key
            return

        url = f'{self.base_url}/v1/chat/completions'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'
        }
        data = {
            'model': 'grok-1',
            'messages': messages,
            'stream': True
        }
        try:
            # Код исполняет отправку запроса к API
            response = requests.post(url, headers=headers, json=data, stream=True)
            response.raise_for_status()
            for line in response.iter_lines():
                if line:
                    yield line.decode('utf-8')
        except requests.exceptions.RequestException as e:
           # Логируем ошибку запроса
            logger.error(f'Error during streaming request to {url}: {e}')
            return
        except Exception as e:
           # Логируем любую другую ошибку
            logger.error(f'Error during streaming response processing: {e}')
            return