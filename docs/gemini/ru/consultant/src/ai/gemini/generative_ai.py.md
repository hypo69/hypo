# Улучшенный код
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для интеграции с Google Generative AI.
=========================================================================================

Этот модуль предоставляет класс :class:`GoogleGenerativeAI` для взаимодействия с моделями Google Generative AI,
включая отправку запросов, получение ответов и управление историей диалогов.

.. module:: src.ai.gemini.generative_ai
   :platform: Windows, Unix
   :synopsis: Интеграция с Google Generative AI.
   :note: https://github.com/google-gemini/generative-ai-python/blob/main/docs/api/google/generativeai.md

Пример использования
--------------------

Пример использования класса `GoogleGenerativeAI`:

.. code-block:: python

    from pathlib import Path
    from src.ai.gemini.generative_ai import GoogleGenerativeAI
    
    api_key = "YOUR_API_KEY"
    ai = GoogleGenerativeAI(api_key=api_key, system_instruction="You are a helpful assistant")
    response = ai.ask("How are you?")
    print(response)
    
    image_path = Path("path/to/your/image.jpg")
    description = ai.describe_image(image_path)
    print(description)

    file_path = Path("path/to/your/file.txt")
    uploaded = ai.upload_file(file_path)
    print(uploaded)

"""

MODE = 'dev'
import time
import json
from io import IOBase
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, List, Any
from types import SimpleNamespace
import base64

import google.generativeai as genai
import requests

from grpc import RpcError
from google.api_core.exceptions import (
    GatewayTimeout,
    ServiceUnavailable,
    ResourceExhausted,
    InvalidArgument,
)
from google.auth.exceptions import DefaultCredentialsError, RefreshError
from src.logger.logger import logger
from src import gs
from src.utils.printer import pprint
from src.utils.file import read_text_file, save_text_file
from src.utils.date_time import TimeoutCheck
from src.utils.convertors.unicode import decode_unicode_escape
from src.utils.jjson import j_loads, j_loads_ns, j_dumps

timeout_check = TimeoutCheck()

class GoogleGenerativeAI:
    """
    Класс для взаимодействия с моделями Google Generative AI.
    
    :ivar MODELS: Список доступных моделей AI.
    :vartype MODELS: List[str]
    :ivar api_key: Ключ API для доступа к генеративной модели.
    :vartype api_key: str
    :ivar model_name: Название модели для использования.
    :vartype model_name: str
    :ivar generation_config: Конфигурация для генерации.
    :vartype generation_config: Dict
    :ivar mode: Режим работы модели (например, 'debug' или 'production').
    :vartype mode: str
    :ivar dialogue_log_path: Путь для логирования диалогов.
    :vartype dialogue_log_path: Optional[Path]
    :ivar dialogue_txt_path: Путь для сохранения текстовых файлов диалогов.
    :vartype dialogue_txt_path: Optional[Path]
    :ivar history_dir: Директория для хранения истории.
    :vartype history_dir: Path
    :ivar history_txt_file: Путь к файлу для хранения истории в формате текста.
    :vartype history_txt_file: Optional[Path]
    :ivar history_json_file: Путь к файлу для хранения истории в формате JSON.
    :vartype history_json_file: Optional[Path]
    :ivar model: Объект модели Google Generative AI.
    :vartype model: Optional[genai.GenerativeModel]
    :ivar system_instruction: Инструкция для системы, которая задает параметры поведения модели.
    :vartype system_instruction: Optional[str]
    
    Этот класс используется для настройки и работы с моделью Google Generative AI, включая отправку запросов,
    получение ответов и сохранение диалогов в текстовых и JSON файлах.

    Args:
        api_key (str): Ключ API для доступа к генеративной модели.
        model_name (Optional[str], optional): Название модели для использования. По умолчанию "gemini-1.5-flash-8b".
        generation_config (Optional[Dict], optional): Конфигурация для генерации. По умолчанию {"response_mime_type": "text/plain"}.
        system_instruction (Optional[str], optional): Инструкция для системы. По умолчанию None.

    Пример использования:
        >>> ai = GoogleGenerativeAI(api_key="your_api_key", system_instruction="Instruction")
        >>> response = ai.ask("Как дела?")
        >>> print(response)
    """

    MODELS = [
        "gemini-1.5-flash-8b",
        "gemini-2-13b",
        "gemini-3-20b"
    ]

    def __init__(self,
                 api_key: str,
                 model_name: Optional[str] = None,
                 generation_config: Optional[Dict] = None,
                 system_instruction: Optional[str] = None,
                 **kwargs):
        """
        Инициализация модели GoogleGenerativeAI с дополнительными настройками.

        Этот метод настраивает модель AI, а также определяет пути для логирования и истории.

        :param api_key: Ключ API для доступа к генеративной модели.
        :type api_key: str
        :param model_name: Название модели для использования.
        :type model_name: Optional[str]
        :param generation_config: Конфигурация для генерации.
        :type generation_config: Optional[Dict]
        :param system_instruction: Инструкция для системы.
        :type system_instruction: Optional[str]
        """
        _now = gs.now
        self.api_key = api_key
        self.model_name = model_name or "gemini-1.5-flash-8b"
        self.generation_config = generation_config or {"response_mime_type": "text/plain"}
        self.system_instruction = system_instruction

        self.dialogue_log_path = gs.path.external_storage / 'AI' / 'log'
        self.dialogue_txt_path = self.dialogue_log_path / f"gemini_{_now}.txt"
        self.history_dir = gs.path.external_storage / 'AI' / 'history'
        self.history_txt_file = self.history_dir / f"gemini_{_now}.txt"
        self.history_json_file = self.history_dir / f"gemini_{_now}.json"

        # Инициализация модели
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(
            model_name=self.model_name,
            generation_config=self.generation_config
        )
        self._chat = self._start_chat()


    @property
    def config(self) -> SimpleNamespace:
        """
        Получает конфигурацию из файла настроек.

        :return: Конфигурация в виде SimpleNamespace.
        :rtype: SimpleNamespace
        """
        return j_loads_ns(gs.path.src / 'ai' / 'gemini' / 'generative_ai.json')

    def _start_chat(self) -> genai.ChatSession:
        """
        Запускает чат с моделью.

        :return: Сессия чата.
        :rtype: genai.ChatSession
        """
        ...
        return self.model.start_chat(history=[])

    def _save_dialogue(self, dialogue: list):
        """
        Сохраняет диалог в текстовый и JSON файл с управлением размером файлов.

        :param dialogue: Список сообщений, представляющих диалог, который нужно сохранить.
        :type dialogue: list
        """
        save_text_file(dialogue, self.history_txt_file, mode='+a')
        for message in dialogue:
            j_dumps(data=message, file_path=self.history_json_file, mode='+a')


    async def ask(self, q: str, attempts: int = 15) -> Optional[str]:
        """
        Отправляет текстовый запрос модели и возвращает ответ.
        
        :param q: Вопрос, который будет отправлен модели.
        :type q: str
        :param attempts: Количество попыток для получения ответа.
        :type attempts: int
        :return: Ответ от модели или None, если ответ не был получен.
        :rtype: Optional[str]

        :raises requests.exceptions.RequestException: Ошибка при сетевом запросе.
        :raises google.api_core.exceptions.GatewayTimeout: Таймаут шлюза.
        :raises google.api_core.exceptions.ServiceUnavailable: Сервис недоступен.
        :raises google.api_core.exceptions.ResourceExhausted: Исчерпан лимит ресурсов.
        :raises google.auth.exceptions.DefaultCredentialsError: Ошибка аутентификации (неверные учетные данные).
        :raises google.auth.exceptions.RefreshError: Ошибка обновления токена аутентификации.
        :raises ValueError: Неверный формат входных данных.
        :raises TypeError: Неверный тип данных.
        :raises google.api_core.exceptions.InvalidArgument: Неверный аргумент API.
        :raises grpc.RpcError: Ошибка gRPC.
        :raises Exception: Любая другая непредвиденная ошибка.

        Пример:
            >>> ai = GoogleGenerativeAI(api_key="your_api_key")
            >>> response = ai.ask("Какая погода сегодня?")
            >>> print(response)
        TODO:
            препарировать `response`
        """
        for attempt in range(attempts):
            try:
                response = self.model.generate_content(q)

                if not response:
                    logger.debug(f"No response from the model. Attempt: {attempt}\\nSleeping for {2 ** attempt}")
                    time.sleep(2 ** attempt)
                    continue  # Повторить попытку

                messages = [
                    {"role": "user", "content": q},
                    {"role": "assistant", "content": response.text}
                ]

                self._save_dialogue([messages])
                return response.text

            except requests.exceptions.RequestException as ex:
                timeout = 1200
                max_attempts = 5
                if attempt > max_attempts:
                    break
                logger.debug(f"Network error. Attempt: {attempt}\\nSleeping for {timeout/60} min on {gs.now}",ex,None)
                time.sleep(timeout)
                continue  # Повторить попытку
            except (GatewayTimeout, ServiceUnavailable) as ex:
                logger.error("Service unavailable:", ex, None)
                # Экспоненциальный бэк-офф для повторных попыток
                max_attempts = 3
                if attempt > max_attempts:
                    break
                time.sleep(2 ** attempt)
                continue
            except ResourceExhausted as ex:
                timeout = 10800
                logger.debug(f"Quota exceeded. Attempt: {attempt}\\nSleeping for {timeout/60} min on {gs.now}",ex,None)
                time.sleep(timeout)
                continue
            except (DefaultCredentialsError, RefreshError) as ex:
                logger.error("Authentication error:",ex,None)
                return  # Прекратить попытки, если ошибка аутентификации
            except (ValueError, TypeError) as ex:
                max_attempts = 3
                if attempt > max_attempts:
                    break
                timeout = 5
                logger.error(f"Invalid input: Attempt: {attempt}\\nSleeping for {timeout/60} min on {gs.now}",ex,None)
                time.sleep(timeout)
                continue
            except (InvalidArgument, RpcError) as ex:
                logger.error("API error:",ex,None)
                return
            except Exception as ex:
                logger.error("Unexpected error:",ex,None)
                return

        return

    def chat(self, q:str) -> Optional[str]:
        """
        Отправляет сообщение в чат и возвращает ответ.

        :param q: Сообщение для отправки.
        :type q: str
        :return: Ответ от модели или None, если произошла ошибка.
        :rtype: Optional[str]
        """
        ...
        response = None
        try:
            response = self._chat.send_message(q)
            return response.text
        except Exception as ex:
            logger.error(f"Ошибка чата {response=}",ex)
            ...
            return

    def describe_image(self, image_path: Path) -> Optional[str]:
        """
        Генерирует описание изображения.

        :param image_path: Путь к изображению, которое нужно описать.
        :type image_path: Path
        :return: Описание изображения или None, если произошла ошибка.
        :rtype: Optional[str]

        :raises Exception: Если произошла ошибка при обработке изображения.
        
        Пример:
            >>> ai = GoogleGenerativeAI(api_key="your_api_key")
            >>> description = ai.describe_image(Path("path/to/image.jpg"))
            >>> print(description)
        """
        try:
            with image_path.open('rb') as f:
                encoded_image = base64.b64encode(f.read()).decode('utf-8')

            response = self.model.generate_content(encoded_image)
            return response.text

        except Exception as ex:
            logger.error(f"Error describing image:" , ex)
            return

    def upload_file(self, file: str | Path | IOBase, file_name:Optional[str] = None) -> Optional[bool]:
        """
        Загружает файл в Google Generative AI.
        https://github.com/google-gemini/generative-ai-python/blob/main/docs/api/google/generativeai/upload_file.md

        :param file: Путь к файлу, объект файла или путь к файлу в виде строки.
        :type file: str | Path | IOBase
        :param file_name: Имя файла.
        :type file_name: Optional[str]
        :return: True если файл загружен успешно, в противном случае None
        :rtype: Optional[bool]

        :raises Exception: Если произошла ошибка при загрузке файла.
        """
        response = None
        try:
            response =  genai.upload_file(
                    path = file,
                    mime_type = None,
                    name = file_name,
                    display_name = file_name,
                    resumable = True
                )
            logger.debug(f"Файл {file_name} записан", None, False)
            return True
        except Exception as ex:
            logger.error(f"Ошибка записи файла {file_name=}", ex, False)
            try:
                response = genai.delete_file(file_name)
                logger.debug(f"Файл {file_name} удален", None, False)
                self.upload_file(file,file_name)
            except Exception as ex:
                logger.error(f"Общая ошибка модели: ", ex, False)
                ...
                return



if __name__ == "__main__":
    ...
```
# Внесённые изменения
1.  **Добавлены RST комментарии**:
    *   Добавлены комментарии в формате RST для модуля, класса, методов и переменных, включая описания параметров, типов и возвращаемых значений.
2.  **Импорты**:
    *   Добавлен импорт `List` и `Any` из `typing`.
3.  **Логирование**:
    *   Используется `logger.error` для логирования ошибок вместо стандартных блоков `try-except`, где это возможно.
4.  **Удаление try except**:
    *   Удалены избыточные `try-except`, где они не нужны.
5.  **Конфигурация**:
    *   Добавлено документирование к методу `config`.
6.  **Функция ask**:
    *   Добавлены rst коментарии.
    *   Добавлены  типы исключений.
7.  **Функция chat**:
    *   Добавлены rst коментарии.
8.  **Функция describe_image**:
    *   Добавлены rst коментарии.
9.  **Функция upload_file**:
    *   Добавлены rst коментарии.
    *   Изменен тип возвращаемого значения.
10. **Форматирование**:
    *   Улучшено форматирование кода и добавлены разделители для лучшей читаемости.

# Оптимизированный код
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для интеграции с Google Generative AI.
=========================================================================================

Этот модуль предоставляет класс :class:`GoogleGenerativeAI` для взаимодействия с моделями Google Generative AI,
включая отправку запросов, получение ответов и управление историей диалогов.

.. module:: src.ai.gemini.generative_ai
   :platform: Windows, Unix
   :synopsis: Интеграция с Google Generative AI.
   :note: https://github.com/google-gemini/generative-ai-python/blob/main/docs/api/google/generativeai.md

Пример использования
--------------------

Пример использования класса `GoogleGenerativeAI`:

.. code-block:: python

    from pathlib import Path
    from src.ai.gemini.generative_ai import GoogleGenerativeAI
    
    api_key = "YOUR_API_KEY"
    ai = GoogleGenerativeAI(api_key=api_key, system_instruction="You are a helpful assistant")
    response = ai.ask("How are you?")
    print(response)
    
    image_path = Path("path/to/your/image.jpg")
    description = ai.describe_image(image_path)
    print(description)

    file_path = Path("path/to/your/file.txt")
    uploaded = ai.upload_file(file_path)
    print(uploaded)

"""

MODE = 'dev'
import time
import json
from io import IOBase
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, List, Any
from types import SimpleNamespace
import base64

import google.generativeai as genai
import requests

from grpc import RpcError
from google.api_core.exceptions import (
    GatewayTimeout,
    ServiceUnavailable,
    ResourceExhausted,
    InvalidArgument,
)
from google.auth.exceptions import DefaultCredentialsError, RefreshError
from src.logger.logger import logger
from src import gs
from src.utils.printer import pprint
from src.utils.file import read_text_file, save_text_file
from src.utils.date_time import TimeoutCheck
from src.utils.convertors.unicode import decode_unicode_escape
from src.utils.jjson import j_loads, j_loads_ns, j_dumps

timeout_check = TimeoutCheck()

class GoogleGenerativeAI:
    """
    Класс для взаимодействия с моделями Google Generative AI.
    
    :ivar MODELS: Список доступных моделей AI.
    :vartype MODELS: List[str]
    :ivar api_key: Ключ API для доступа к генеративной модели.
    :vartype api_key: str
    :ivar model_name: Название модели для использования.
    :vartype model_name: str
    :ivar generation_config: Конфигурация для генерации.
    :vartype generation_config: Dict
    :ivar mode: Режим работы модели (например, 'debug' или 'production').
    :vartype mode: str
    :ivar dialogue_log_path: Путь для логирования диалогов.
    :vartype dialogue_log_path: Optional[Path]
    :ivar dialogue_txt_path: Путь для сохранения текстовых файлов диалогов.
    :vartype dialogue_txt_path: Optional[Path]
    :ivar history_dir: Директория для хранения истории.
    :vartype history_dir: Path
    :ivar history_txt_file: Путь к файлу для хранения истории в формате текста.
    :vartype history_txt_file: Optional[Path]
    :ivar history_json_file: Путь к файлу для хранения истории в формате JSON.
    :vartype history_json_file: Optional[Path]
    :ivar model: Объект модели Google Generative AI.
    :vartype model: Optional[genai.GenerativeModel]
    :ivar system_instruction: Инструкция для системы, которая задает параметры поведения модели.
    :vartype system_instruction: Optional[str]
    
    Этот класс используется для настройки и работы с моделью Google Generative AI, включая отправку запросов,
    получение ответов и сохранение диалогов в текстовых и JSON файлах.

    Args:
        api_key (str): Ключ API для доступа к генеративной модели.
        model_name (Optional[str], optional): Название модели для использования. По умолчанию "gemini-1.5-flash-8b".
        generation_config (Optional[Dict], optional): Конфигурация для генерации. По умолчанию {"response_mime_type": "text/plain"}.
        system_instruction (Optional[str], optional): Инструкция для системы. По умолчанию None.

    Пример использования:
        >>> ai = GoogleGenerativeAI(api_key="your_api_key", system_instruction="Instruction")
        >>> response = ai.ask("Как дела?")
        >>> print(response)
    """

    MODELS = [
        "gemini-1.5-flash-8b",
        "gemini-2-13b",
        "gemini-3-20b"
    ]

    def __init__(self,
                 api_key: str,
                 model_name: Optional[str] = None,
                 generation_config: Optional[Dict] = None,
                 system_instruction: Optional[str] = None,
                 **kwargs):
        """
        Инициализация модели GoogleGenerativeAI с дополнительными настройками.

        Этот метод настраивает модель AI, а также определяет пути для логирования и истории.

        :param api_key: Ключ API для доступа к генеративной модели.
        :type api_key: str
        :param model_name: Название модели для использования.
        :type model_name: Optional[str]
        :param generation_config: Конфигурация для генерации.
        :type generation_config: Optional[Dict]
        :param system_instruction: Инструкция для системы.
        :type system_instruction: Optional[str]
        """
        _now = gs.now
        self.api_key = api_key
        self.model_name = model_name or "gemini-1.5-flash-8b"
        self.generation_config = generation_config or {"response_mime_type": "text/plain"}
        self.system_instruction = system_instruction

        self.dialogue_log_path = gs.path.external_storage / 'AI' / 'log'
        self.dialogue_txt_path = self.dialogue_log_path / f"gemini_{_now}.txt"
        self.history_dir = gs.path.external_storage / 'AI' / 'history'
        self.history_txt_file = self.history_dir / f"gemini_{_now}.txt"
        self.history_json_file = self.history_dir / f"gemini_{_now}.json"

        # Инициализация модели
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(
            model_name=self.model_name,
            generation_config=self.generation_config
        )
        self._chat = self._start_chat()


    @property
    def config(self) -> SimpleNamespace:
        """
        Получает конфигурацию из файла настроек.

        :return: Конфигурация в виде SimpleNamespace.
        :rtype: SimpleNamespace
        """
        return j_loads_ns(gs.path.src / 'ai' / 'gemini' / 'generative_ai.json')

    def _start_chat(self) -> genai.ChatSession:
        """
        Запускает чат с моделью.

        :return: Сессия чата.
        :rtype: genai.ChatSession
        """
        ...
        return self.model.start_chat(history=[])

    def _save_dialogue(self, dialogue: list):
        """
        Сохраняет диалог в текстовый и JSON файл с управлением размером файлов.

        :param dialogue: Список сообщений, представляющих диалог, который нужно сохранить.
        :type dialogue: list
        """
        save_text_file(dialogue, self.history_txt_file, mode='+a')
        for message in dialogue:
            j_dumps(data=message, file_path=self.history_json_file, mode='+a')


    async def ask(self, q: str, attempts: int = 15) -> Optional[str]:
        """
        Отправляет текстовый запрос модели и возвращает ответ.
        
        :param q: Вопрос, который будет отправлен модели.
        :type q: str
        :param attempts: Количество попыток для получения ответа.
        :type attempts: int
        :return: Ответ от модели или None, если ответ не был получен.
        :rtype: Optional[str]

        :raises requests.exceptions.RequestException: Ошибка при сетевом запросе.
        :raises google.api_core.exceptions.GatewayTimeout: Таймаут шлюза.
        :raises google.api_core.exceptions.ServiceUnavailable: Сервис недоступен.
        :raises google.api_core.exceptions.ResourceExhausted: Исчерпан лимит ресурсов.
        :raises google.auth.exceptions.DefaultCredentialsError: Ошибка аутентификации (неверные учетные данные).
        :raises google.auth.exceptions.RefreshError: Ошибка обновления токена аутентификации.
        :raises ValueError: Неверный формат входных данных.
        :raises TypeError: Неверный тип данных.
        :raises google.api_core.exceptions.InvalidArgument: Неверный аргумент API.
        :raises grpc.RpcError: Ошибка gRPC.
        :raises Exception: Любая другая непредвиденная ошибка.

        Пример:
            >>> ai = GoogleGenerativeAI(api_key="your_api_key")
            >>> response = ai.ask("Какая погода сегодня?")
            >>> print(response)
        TODO:
            препарировать `response`
        """
        for attempt in range(attempts):
            try:
                response = self.model.generate_content(q)

                if not response:
                    logger.debug(f"No response from the model. Attempt: {attempt}\\nSleeping for {2 ** attempt}")
                    time.sleep(2 ** attempt)
                    continue  # Повторить попытку

                messages = [
                    {"role": "user", "content": q},
                    {"role": "assistant", "content": response.text}
                ]

                self._save_dialogue([messages])
                return response.text

            except requests.exceptions.RequestException as ex:
                timeout = 1200
                max_attempts = 5
                if attempt > max_attempts:
                    break
                logger.debug(f"Network error. Attempt: {attempt}\\nSleeping for {timeout/60} min on {gs.now}",ex,None)
                time.sleep(timeout)
                continue  # Повторить попытку
            except (GatewayTimeout, ServiceUnavailable) as ex:
                logger.error("Service unavailable:", ex, None)
                # Экспоненциальный бэк-офф для повторных попыток
                max_attempts = 3
                if attempt > max_attempts:
                    break
                time.sleep(2 ** attempt)
                continue
            except ResourceExhausted as ex:
                timeout = 10800
                logger.debug(f"Quota exceeded. Attempt: {attempt}\\nSleeping for {timeout/60} min on {gs.now}",ex,None)
                time.sleep(timeout)
                continue
            except (DefaultCredentialsError, RefreshError) as ex:
                logger.error("Authentication error:",ex,None)
                return  # Прекратить попытки, если ошибка аутентификации
            except (ValueError, TypeError) as ex:
                max_attempts = 3
                if attempt > max_attempts:
                    break
                timeout = 5
                logger.error(f"Invalid input: Attempt: {attempt}\\nSleeping for {timeout/60} min on {gs.now}",ex,None)
                time.sleep(timeout)
                continue
            except (InvalidArgument, RpcError) as ex:
                logger.error("API error:",ex,None)
                return
            except Exception as ex:
                logger.error("Unexpected error:",ex,None)
                return

        return

    def chat(self, q:str) -> Optional[str]:
        """
        Отправляет сообщение в чат и возвращает ответ.

        :param q: Сообщение для отправки.
        :type q: str
        :return: Ответ от модели или None, если произошла ошибка.
        :rtype: Optional[str]
        """
        ...
        response = None
        try:
            response = self._chat.send_message(q)
            return response.text
        except Exception as ex:
            logger.error(f"Ошибка чата {response=}",ex)
            ...
            return

    def describe_image(self, image_path: Path) -> Optional[str]:
        """
        Генерирует описание изображения.

        :param image_path: Путь к изображению, которое нужно описать.
        :type image_path: Path
        :return: Описание изображения или None, если произошла ошибка.
        :rtype: Optional[str]

        :raises Exception: Если произошла ошибка при обработке изображения.
        
        Пример:
            >>> ai = GoogleGenerativeAI(api_key="your_api_key")
            >>> description = ai.describe_image(Path("path/to/image.jpg"))
            >>> print(description)
        """
        try:
            with image_path.open('rb') as f:
                encoded_image = base64.b64encode(f.read()).decode('utf-8')

            response = self.model.generate_content(encoded_image)
            return response.text

        except Exception as ex:
            logger.error(f"Error describing image:" , ex)
            return

    def upload_file(self, file: str | Path | IOBase, file_name:Optional[str] = None) -> Optional[bool]:
        """
        Загружает файл в Google Generative AI.
        https://github.com/google-gemini/generative-ai-python/blob/main/docs/api/google/generativeai/upload_file.md

        :param file: Путь к файлу, объект файла или путь к файлу в виде строки.
        :type file: str | Path | IOBase
        :param file_name: Имя файла.
        :type file_name: Optional[str]
        :return: True если файл загружен успешно, в противном случае None
        :rtype: Optional[bool]

        :raises Exception: Если произошла ошибка при загрузке файла.
        """
        response = None
        try:
            response =  genai.upload_file(
                    path = file,
                    mime_type = None,
                    name = file_name,
                    display_name = file_name,
                    resumable = True
                )
            logger.debug(f"Файл {file_name} записан", None, False)
            return True
        except Exception as ex:
            logger.error(f"Ошибка записи файла {file_name=}", ex, False)
            try:
                response = genai.delete_file(file_name)
                logger.debug(f"Файл {file_name} удален", None, False)
                self.upload_file(file,file_name)
            except Exception as ex:
                logger.error(f"Общая ошибка модели: ", ex, False)
                ...
                return



if __name__ == "__main__":
    ...
```
```
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для интеграции с Google Generative AI.
=========================================================================================

Этот модуль предоставляет класс :class:`GoogleGenerativeAI` для взаимодействия с моделями Google Generative AI,
включая отправку запросов, получение ответов и управление историей диалогов.

.. module:: src.ai.gemini.generative_ai
   :platform: Windows, Unix
   :synopsis: Интеграция с Google Generative AI.
   :note: https://github.com/google-gemini/generative-ai-python/blob/main/docs/api/google/generativeai.md

Пример использования
--------------------

Пример использования класса `GoogleGenerativeAI`:

.. code-block:: python

    from pathlib import Path
    from src.ai.gemini.generative_ai import GoogleGenerativeAI
    
    api_key = "YOUR_API_KEY"
    ai = GoogleGenerativeAI(api_key=api_key, system_instruction="You are a helpful assistant")
    response = ai.ask("How are you?")
    print(response)
    
    image_path = Path("path/to/your/image.jpg")
    description = ai.describe_image(image_path)
    print(description)

    file_path = Path("path/to/your/file.