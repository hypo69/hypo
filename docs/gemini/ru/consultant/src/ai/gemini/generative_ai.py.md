# Анализ кода модуля `src.ai.gemini.generative_ai`

**Качество кода**
9
-  Плюсы
    - Код хорошо структурирован и разбит на функции, что делает его читабельным.
    - Используются аннотации типов, что повышает надежность и читаемость кода.
    - Присутствует обработка исключений для различных сценариев ошибок.
    - Код логирует ошибки, что помогает при отладке.
-  Минусы
    - Некоторые docstring не полностью соответствуют стандарту reStructuredText (RST).
    - Не везде используются константы для таймаутов и количества попыток, что затрудняет их изменение.
    - Отсутствуют некоторые необходимые импорты.
    - Избыточное использование `try-except` конструкций.
    - Необходимо улучшить форматирование вывода логов.

**Рекомендации по улучшению**

1.  **Формат документации**:
    -   Привести все docstring к формату RST.
    -   Добавить недостающие описания для параметров и возвращаемых значений.
2.  **Сохранение комментариев**:
    -   Сохранить все существующие комментарии после `#`.
3.  **Обработка данных**:
    -   Использовать `j_loads` или `j_loads_ns` для чтения конфигурационных файлов.
4.  **Анализ структуры**:
    -   Добавить отсутствующие импорты, такие как `Any`
    -   Привести имена переменных и функций в соответствие с общей структурой проекта.
5.  **Рефакторинг и улучшения**:
    -   Заменить избыточные блоки `try-except` на более компактную обработку ошибок с использованием `logger.error`.
    -   Добавить константы для таймаутов и количества попыток.
    -   Улучшить форматирование логов.
    -   Улучшить обработку ошибок в функции `upload_file`.
    -   Добавить docstring для функции `_start_chat`.
6. **Логирование**:
    -  Использовать `logger.debug` для вывода отладочной информации, `logger.info` для информационных сообщений, `logger.warning` для предупреждений и `logger.error` для ошибок.
    -  Добавить более информативные сообщения в логи, включая контекст и значения переменных.

**Оптимизированный код**

```python
"""
Модуль для интеграции с Google Generative AI.
=========================================================================================

Этот модуль содержит класс :class:`GoogleGenerativeAI`, который используется для взаимодействия с моделями Google Generative AI,
включая отправку запросов, получение ответов, сохранение диалогов и работу с изображениями.

Пример использования
--------------------

Пример использования класса `GoogleGenerativeAI`:

.. code-block:: python

    ai = GoogleGenerativeAI(api_key="your_api_key", system_instruction="Instruction")
    response = ai.ask("Как дела?")
    print(response)
"""
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12
import time
import base64
from io import IOBase
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, List, Any
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
from src.utils.printer import pprint
from src.utils.file import read_text_file, save_text_file
from src.utils.date_time import TimeoutCheck
from src.utils.convertors.unicode import decode_unicode_escape
from src.utils.jjson import j_loads, j_loads_ns, j_dumps

timeout_check = TimeoutCheck()

class GoogleGenerativeAI:
    """
    Класс для взаимодействия с моделями Google Generative AI.

    Этот класс используется для настройки и работы с моделью Google Generative AI, включая отправку запросов,
    получение ответов и сохранение диалогов в текстовых и JSON файлах.

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

    :Example:
        >>> ai = GoogleGenerativeAI(api_key="your_api_key", system_instruction="Instruction")
        >>> response = ai.ask("Как дела?")
        >>> print(response)
    """

    MODELS: List[str] = [
        "gemini-1.5-flash-8b",
        "gemini-2-13b",
        "gemini-3-20b"
    ]
    _MAX_ATTEMPTS: int = 5
    _TIMEOUT_BASE: int = 2
    _QUOTA_TIMEOUT: int = 10800
    _NETWORK_TIMEOUT: int = 1200
    _INPUT_TIMEOUT: int = 5
    

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
        # код исполняет загрузку конфигурации из файла
        return j_loads_ns(gs.path.src / 'ai' / 'gemini' / 'generative_ai.json')

    def _start_chat(self) -> genai.ChatSession:
        """
        Инициализирует и возвращает объект чата.

        :return: Объект чата.
        :rtype: genai.ChatSession
        """
        # код инициализирует чат
        return self.model.start_chat(history=[])

    def _save_dialogue(self, dialogue: List[Dict]):
        """
        Сохраняет диалог в текстовый и JSON файл с управлением размером файлов.

        Этот метод сохраняет каждый диалог в текстовом и JSON формате для последующего анализа.

        :param dialogue: Список сообщений, представляющих диалог, который нужно сохранить.
        :type dialogue: List[Dict]
        """
        # код сохраняет диалог в текстовый файл
        save_text_file(dialogue, self.history_txt_file, mode='+a')
        # код сохраняет диалог в json файл
        for message in dialogue:
            j_dumps(data=message, file_path=self.history_json_file, mode='+a')


    async def ask(self, q: str, attempts: int = 15) -> Optional[str]:
        """
        Отправляет текстовый запрос модели и возвращает ответ.

        :param q: Вопрос, который будет отправлен модели.
        :type q: str
        :param attempts: Количество попыток для получения ответа. По умолчанию 15.
        :type attempts: int
        :return: Ответ от модели или None, если ответ не был получен.
        :rtype: Optional[str]

        :Example:
            >>> ai = GoogleGenerativeAI(api_key="your_api_key")
            >>> response = ai.ask("Какая погода сегодня?")
            >>> print(response)
        
        :TODO:
            препарировать `response`
        """
        for attempt in range(attempts):
            try:
                # код исполняет запрос к модели
                response = self.model.generate_content(q)
                if not response:
                    logger.debug(f"No response from the model. Attempt: {attempt}, sleeping for {self._TIMEOUT_BASE ** attempt} seconds")
                    time.sleep(self._TIMEOUT_BASE ** attempt)
                    continue  # Повторить попытку

                messages = [
                    {"role": "user", "content": q},
                    {"role": "assistant", "content": response.text}
                ]
                # код сохраняет диалог
                self._save_dialogue([messages])
                return response.text

            except requests.exceptions.RequestException as ex:
                # Код обрабатывает сетевые ошибки
                if attempt > self._MAX_ATTEMPTS:
                    break
                logger.debug(f"Network error. Attempt: {attempt}, sleeping for {self._NETWORK_TIMEOUT/60} min on {gs.now}", exc_info=ex)
                time.sleep(self._NETWORK_TIMEOUT)
                continue  # Повторить попытку
            except (GatewayTimeout, ServiceUnavailable) as ex:
                # Код обрабатывает ошибки недоступности сервиса
                logger.error(f"Service unavailable: {ex}", exc_info=ex)
                if attempt > self._MAX_ATTEMPTS:
                     break
                time.sleep(self._TIMEOUT_BASE ** attempt)
                continue
            except ResourceExhausted as ex:
                # Код обрабатывает ошибки исчерпания ресурсов
                logger.debug(f"Quota exceeded. Attempt: {attempt}, sleeping for {self._QUOTA_TIMEOUT/60} min on {gs.now}", exc_info=ex)
                time.sleep(self._QUOTA_TIMEOUT)
                continue
            except (DefaultCredentialsError, RefreshError) as ex:
                # Код обрабатывает ошибки аутентификации
                logger.error(f"Authentication error: {ex}", exc_info=ex)
                return  # Прекратить попытки, если ошибка аутентификации
            except (ValueError, TypeError) as ex:
                 # Код обрабатывает ошибки неверного ввода
                if attempt > self._MAX_ATTEMPTS:
                    break
                logger.error(f"Invalid input: Attempt: {attempt}, sleeping for {self._INPUT_TIMEOUT} seconds", exc_info=ex)
                time.sleep(self._INPUT_TIMEOUT)
                continue
            except (InvalidArgument, RpcError) as ex:
                 # Код обрабатывает ошибки API
                logger.error(f"API error: {ex}", exc_info=ex)
                return
            except Exception as ex:
                # Код обрабатывает прочие ошибки
                logger.error(f"Unexpected error: {ex}", exc_info=ex)
                return
        return None

    def chat(self, q:str) -> Optional[str]:
        """
        Отправляет запрос в чат и возвращает ответ.

        :param q: Сообщение для отправки в чат.
        :type q: str
        :return: Ответ из чата или None в случае ошибки.
        :rtype: Optional[str]
        """
        # код инициализирует переменную
        response = None
        try:
             # код отправляет сообщение в чат и возвращает ответ
            response = self._chat.send_message(q)
            return response.text
        except Exception as ex:
             # код обрабатывает ошибку чата
            logger.error(f"Chat error: response={response}", exc_info=ex)
            return None

    def describe_image(self, image_path: Path) -> Optional[str]:
        """
        Генерирует описание изображения.

        Этот метод отправляет изображение в модель для анализа и получает текстовое описание изображения.

        :param image_path: Путь к изображению, которое нужно описать.
        :type image_path: Path
        :return: Описание изображения или None, если произошла ошибка.
        :rtype: Optional[str]

        :Example:
            >>> ai = GoogleGenerativeAI(api_key="your_api_key")
            >>> description = ai.describe_image(Path("path/to/image.jpg"))
            >>> print(description)
        """
        try:
             # код открывает изображение и кодирует его в base64
            with image_path.open('rb') as f:
                encoded_image = base64.b64encode(f.read()).decode('utf-8')
            # код отправляет изображение на обработку и возвращает описание
            response = self.model.generate_content(encoded_image)
            return response.text

        except Exception as ex:
            # код обрабатывает ошибку описания изображения
            logger.error(f"Error describing image:", exc_info=ex)
            return None

    def upload_file(self, file: str | Path | IOBase, file_name: Optional[str] = None) -> bool:
        """
        Загружает файл в Google Generative AI.

        :param file: Путь к файлу или сам файл для загрузки.
        :type file: str | Path | IOBase
        :param file_name: Имя файла.
        :type file_name: Optional[str]
        :return: True если файл был успешно загружен
        :rtype: bool
        :raises Exception: В случае ошибки загрузки файла
        
        :seealso:
        https://github.com/google-gemini/generative-ai-python/blob/main/docs/api/google/generativeai/upload_file.md
        """
        # код инициализирует переменную
        response = None
        try:
            # код отправляет файл на загрузку
            response =  genai.upload_file(
                    path = file,
                    mime_type = None,
                    name = file_name,
                    display_name = file_name,
                    resumable = True
                )
            logger.debug(f"File {file_name} uploaded successfully",  False)
            return response
        except Exception as ex:
             # код обрабатывает ошибку загрузки файла
            logger.error(f"Error uploading file: {file_name=}", exc_info=ex)
            try:
                # код пытается удалить файл, если произошла ошибка
                response = genai.delete_file(file_name)
                logger.debug(f"File {file_name} deleted", None, False)
                # код повторно вызывает функцию загрузки файла
                self.upload_file(file, file_name)
            except Exception as ex:
                # Код обрабатывает общую ошибку модели
                logger.error(f"Model error: ", exc_info=ex)
                return False


if __name__ == "__main__":
    ...
```