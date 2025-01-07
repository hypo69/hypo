# Анализ кода модуля `src.ai.gemini.generative_ai`

**Качество кода**
8
-   Плюсы
    -   Код соответствует PEP 8.
    -   Присутствует базовая обработка ошибок.
    -   Используется `logger` для логирования.
    -   Присутствуют docstring для класса и методов.
    -   Код разбит на отдельные методы.
-   Минусы
    -   Не везде используется `j_loads` или `j_loads_ns`.
    -   Не все комментарии написаны в формате RST.
    -   Много избыточных `try-except`.
    -   Отсутствует подробное описание некоторых методов.

**Рекомендации по улучшению**

1.  **Форматирование документации**:
    *   Используйте reStructuredText (RST) для всех комментариев и docstring.
    *   Всегда используйте одинарные кавычки (`'`) в Python коде.

2.  **Обработка данных**:
    *   Используйте `j_loads` или `j_loads_ns` из `src.utils.jjson` вместо стандартного `json.load` для чтения файлов.

3.  **Импорты**:
    *   Проверьте и добавьте отсутствующие импорты в код.
    *   Приведите в соответствие имена функций, переменных и импортов с ранее обработанными файлами.

4.  **Рефакторинг и улучшения**:
    *   Добавьте комментарии в формате RST ко всем функциям, методам и классам.
    *   Используйте `from src.logger.logger import logger` для логирования ошибок.
    *   Избегайте избыточного использования стандартных блоков `try-except`, предпочитая обработку ошибок с помощью `logger.error`.

5.  **Обработка исключений**:
    *   Используйте `logger.error` для логирования ошибок вместо `print(f"Error: {ex}")`.

6.  **Логирование**:
    *   Добавьте более подробные сообщения в логгер.

7.  **Метод `upload_file`**:
    *   Упростите логику повторной загрузки файла.
    *   Обработайте ошибки более грациозно.
    *   Добавьте docstring.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль для интеграции с Google Generative AI.
=========================================================================================

Этот модуль обеспечивает взаимодействие с моделями Google Generative AI, включая отправку текстовых и
графических запросов, а также управление диалогами и загрузкой файлов.

:platform: Windows, Unix
:synopsis: Google generative AI integration
:github: https://github.com/google-gemini/generative-ai-python/blob/main/docs/api/google/generativeai.md

Пример использования
--------------------

.. code-block:: python

    from src.ai.gemini.generative_ai import GoogleGenerativeAI
    ai = GoogleGenerativeAI(api_key="YOUR_API_KEY", system_instruction="You are a helpful assistant.")
    response = ai.ask("How are you?")
    print(response)
"""


import time
import base64
from io import IOBase
from pathlib import Path
from typing import Optional, Dict, List
from types import SimpleNamespace
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
from src.utils.file import save_text_file
from src.utils.date_time import TimeoutCheck
from src.utils.jjson import j_loads_ns, j_dumps
from src.utils.printer import pprint # исправил импорт
# from src.utils.convertors.unicode import decode_unicode_escape # удалил неиспользуемый импорт

timeout_check = TimeoutCheck()

class GoogleGenerativeAI:
    """
    Класс для взаимодействия с моделями Google Generative AI.

    Этот класс предоставляет интерфейс для настройки и использования моделей Google Generative AI,
    включая отправку запросов, получение ответов, управление диалогами и загрузку файлов.

    :param api_key: API ключ для доступа к Google Generative AI.
    :type api_key: str
    :param model_name: Название используемой модели.
    :type model_name: Optional[str]
    :param generation_config: Конфигурация для генерации текста.
    :type generation_config: Optional[Dict]
    :param system_instruction: Системная инструкция для модели.
    :type system_instruction: Optional[str]
    :raises DefaultCredentialsError: Если не удается получить учетные данные.
    :raises RefreshError: Если не удается обновить учетные данные.

    :ivar MODELS: Список доступных моделей.
    :vartype MODELS: List[str]
    :ivar api_key: Ключ API для доступа к генеративной модели.
    :vartype api_key: str
    :ivar model_name: Название модели для использования.
    :vartype model_name: str
    :ivar generation_config: Конфигурация для генерации.
    :vartype generation_config: Dict
    :ivar dialogue_log_path: Путь для хранения журналов диалогов.
    :vartype dialogue_log_path: Optional[Path]
    :ivar dialogue_txt_path: Путь для хранения текстовых файлов диалогов.
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
        Инициализация экземпляра класса GoogleGenerativeAI.

        :param api_key: Ключ API для доступа к генеративной модели.
        :type api_key: str
        :param model_name: Название модели для использования. По умолчанию "gemini-1.5-flash-8b".
        :type model_name: Optional[str]
        :param generation_config: Конфигурация для генерации. По умолчанию {"response_mime_type": "text/plain"}.
        :type generation_config: Optional[Dict]
        :param system_instruction: Инструкция для системы. По умолчанию None.
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
        # код получает конфигурацию из файла `generative_ai.json`
        return j_loads_ns(gs.path.src / 'ai' / 'gemini' / 'generative_ai.json')

    def _start_chat(self):
        """
        Инициирует чат с моделью.

        :return: Объект чата.
        """
        ...
        return self.model.start_chat(history=[])

    def _save_dialogue(self, dialogue: list):
        """
        Сохраняет диалог в текстовый и JSON файл.

        :param dialogue: Список сообщений, представляющих диалог.
        :type dialogue: list
        """
        # Сохраняет диалог в текстовый файл
        save_text_file(dialogue, self.history_txt_file, mode='+a')
        # Сохраняет каждое сообщение диалога в json файл
        for message in dialogue:
            j_dumps(data=message, file_path=self.history_json_file, mode='+a')


    async def ask(self, q: str, attempts: int = 15) -> Optional[str]:
        """
        Отправляет текстовый запрос модели и возвращает ответ.

        :param q: Запрос к модели.
        :type q: str
        :param attempts: Количество попыток для получения ответа. По умолчанию 15.
        :type attempts: int
        :return: Ответ от модели или None, если ответа нет.
        :rtype: Optional[str]

        :raises requests.exceptions.RequestException: Если произошла ошибка сети.
        :raises GatewayTimeout: Если время ожидания ответа истекло.
        :raises ServiceUnavailable: Если сервис временно недоступен.
        :raises ResourceExhausted: Если превышена квота запросов.
        :raises DefaultCredentialsError: Если произошла ошибка аутентификации.
        :raises RefreshError: Если не удалось обновить учетные данные.
        :raises ValueError: Если входные данные невалидны.
        :raises TypeError: Если тип входных данных невалиден.
        :raises InvalidArgument: Если запрос некорректен.
        :raises RpcError: Если произошла ошибка RPC.
        :raises Exception: Если произошла неожиданная ошибка.


        Пример:
            >>> ai = GoogleGenerativeAI(api_key="your_api_key")
            >>> response = ai.ask("Какая погода сегодня?")
            >>> print(response)
        """
        # TODO:  препарировать `response`
        for attempt in range(attempts):
            try:
                #  отправляет запрос к модели
                response = self.model.generate_content(q)

                if not response:
                    logger.debug(f"No response from the model. Attempt: {attempt}\\nSleeping for {2 ** attempt}")
                    time.sleep(2 ** attempt)
                    continue  # Повторить попытку

                messages = [
                    {"role": "user", "content": q},
                    {"role": "assistant", "content": response.text}
                ]
                # сохраняет диалог
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

        :param q: Сообщение для отправки в чат.
        :type q: str
        :return: Ответ от чат-модели или None в случае ошибки.
        :rtype: Optional[str]
        """
        ...
        response = None
        try:
            # отправляет сообщение в чат и получает ответ
            response = self._chat.send_message(q)
            return response.text
        except Exception as ex:
            # Логирует ошибку чата
            logger.error(f"Ошибка чата {response=}",ex)
            ...
            return


    def describe_image(self, image_path: Path) -> Optional[str]:
        """
        Генерирует описание изображения.

        :param image_path: Путь к изображению.
        :type image_path: Path
        :return: Описание изображения или None в случае ошибки.
        :rtype: Optional[str]
        """
        try:
            # читает изображение и кодирует в base64
            with image_path.open('rb') as f:
                encoded_image = base64.b64encode(f.read()).decode('utf-8')
            # отправляет закодированное изображение модели и получает описание
            response = self.model.generate_content(encoded_image)
            return response.text

        except Exception as ex:
             # логирует ошибку описания изображения
            logger.error(f"Error describing image:" , ex)
            return

    def upload_file(self, file: str | Path | IOBase, file_name:Optional[str] = None) -> bool:
        """
        Загружает файл в Google Generative AI.

        :param file: Путь к файлу, объект файла или имя файла.
        :type file: str | Path | IOBase
        :param file_name: Имя файла для отображения.
        :type file_name: Optional[str]
        :return: True в случае успешной загрузки, False в случае ошибки.
        :rtype: bool
        :raises Exception: Если произошла ошибка загрузки файла.

        :github: https://github.com/google-gemini/generative-ai-python/blob/main/docs/api/google/generativeai/upload_file.md
        """
        response = None
        try:
            #  загружает файл
            response = genai.upload_file(
                    path = file,
                    mime_type = None,
                    name = file_name,
                    display_name = file_name,
                    resumable = True
                )
            logger.debug(f"Файл {file_name} записан", None, False)
            return response
        except Exception as ex:
            logger.error(f"Ошибка записи файла {file_name=}", ex, False)
            try:
                #  удаляет файл
                response = genai.delete_file(file_name)
                logger.debug(f"Файл {file_name} удален", None, False)
                # повторно загружает файл
                self.upload_file(file,file_name)
            except Exception as ex:
                 # Логирует общую ошибку модели
                logger.error(f"Общая ошибка модели: ", ex, False)
                ...
                return


if __name__ == "__main__":
    ...
```