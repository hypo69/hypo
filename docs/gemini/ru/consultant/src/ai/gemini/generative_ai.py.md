# Анализ кода модуля `generative_ai.py`

**Качество кода**
10
- Плюсы
    - Код хорошо структурирован, используется ООП.
    - Присутствует логирование ошибок.
    - Используются асинхронные вызовы.
    - Документация в формате reStructuredText.
    - Код соответствует PEP8.
- Минусы
    - Избыточное использование try-except блоков.
    - Отсутствует обработка ошибок в некоторых функциях.
    - Не все функции имеют docstring.
    - Используется `j_dumps` для каждого сообщения, что может быть неэффективно для больших диалогов.
    - Не везде используется `logger.error` для обработки исключений.

**Рекомендации по улучшению**
1.  **Улучшить обработку исключений:**
    *   Уменьшить количество блоков `try-except` с помощью `logger.error` и более точного определения исключений.
    *   Добавить обработку исключений в функции `chat` и `upload_file`.

2.  **Рефакторинг:**
    *   Заменить `j_dumps` на более эффективный метод записи диалогов (например, с сохранением всего списка в конце диалога).
    *   Переписать docstring для `_start_chat` и `chat` для соответствия стандарту.
    *   Использовать константы для магических значений, таких как таймауты.

3.  **Дополнить документацию:**
    *   Добавить docstring для всех недостающих функций, методов.

4. **Использовать единый формат логирования:**
    * Привести логирование к единому формату (сообщение, исключение, флаг)

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12
"""
Модуль для интеграции с Google Generative AI.
=========================================================================================

Этот модуль содержит класс :class:`GoogleGenerativeAI`, который используется для
взаимодействия с моделями Google Generative AI, включая отправку запросов,
получение ответов и сохранение диалогов в текстовых и JSON файлах.

.. _Google Generative AI documentation:
    https://github.com/google-gemini/generative-ai-python/blob/main/docs/api/google/generativeai.md

Пример использования
--------------------

Пример использования класса `GoogleGenerativeAI`:

.. code-block:: python

    ai = GoogleGenerativeAI(api_key="your_api_key", system_instruction="Instruction")
    response = ai.ask("Как дела?")
    print(response)
"""
import time
import json
from io import IOBase
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, List
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

    MODELS = [
        "gemini-1.5-flash-8b",
        "gemini-2-13b",
        "gemini-3-20b"
    ]
    _DEFAULT_MODEL = "gemini-1.5-flash-8b"
    _DEFAULT_GENERATION_CONFIG = {"response_mime_type": "text/plain"}
    _NETWORK_ERROR_TIMEOUT = 1200
    _QUOTA_EXCEEDED_TIMEOUT = 10800
    _INVALID_INPUT_TIMEOUT = 5
    _MAX_ATTEMPTS = 5
    _MAX_SERVICE_ATTEMPTS = 3
    _MAX_INPUT_ATTEMPTS = 3
    
    def __init__(self, 
                 api_key: str, 
                 model_name: Optional[str] = None, 
                 generation_config: Optional[Dict] = None, 
                 system_instruction: Optional[str] = None, 
                 **kwargs):
        """
        Инициализация модели GoogleGenerativeAI с дополнительными настройками.

        :param api_key: Ключ API для доступа к генеративной модели.
        :type api_key: str
        :param model_name: Название модели для использования. По умолчанию "gemini-1.5-flash-8b".
        :type model_name: Optional[str], optional
        :param generation_config: Конфигурация для генерации. По умолчанию {"response_mime_type": "text/plain"}.
        :type generation_config: Optional[Dict], optional
        :param system_instruction: Инструкция для системы. По умолчанию None.
        :type system_instruction: Optional[str], optional
        """
        _now = gs.now
        self.api_key = api_key
        self.model_name = model_name or self._DEFAULT_MODEL
        self.generation_config = generation_config or self._DEFAULT_GENERATION_CONFIG
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

        :return: Конфигурация в виде объекта SimpleNamespace.
        :rtype: SimpleNamespace
        """
        return j_loads_ns(gs.path.src / 'ai' / 'gemini' / 'generative_ai.json')

    def _start_chat(self) -> genai.ChatSession:
        """
        Инициализирует чат.

        :return: Объект чат сессии.
        :rtype: genai.ChatSession
        """
        return self.model.start_chat(history=[])

    def _save_dialogue(self, dialogue: List[Dict]):
        """
        Сохраняет диалог в текстовый и JSON файл с управлением размером файлов.

        :param dialogue: Список сообщений, представляющих диалог, который нужно сохранить.
        :type dialogue: List[Dict]
        """
        save_text_file(dialogue, self.history_txt_file, mode='+a')
        with open(self.history_json_file, 'a', encoding='utf-8') as f:
            for message in dialogue:
                json.dump(message, f, ensure_ascii=False)
                f.write('\n')

    async def ask(self, q: str, attempts: int = 15) -> Optional[str]:
        """
        Отправляет текстовый запрос модели и возвращает ответ.

        :param q: Вопрос, который будет отправлен модели.
        :type q: str
        :param attempts: Количество попыток для получения ответа. По умолчанию 15.
        :type attempts: int, optional
        :return: Ответ от модели или None, если ответ не был получен.
        :rtype: Optional[str]

        :Example:
            >>> ai = GoogleGenerativeAI(api_key="your_api_key")
            >>> response = ai.ask("Какая погода сегодня?")
            >>> print(response)
        """
        for attempt in range(attempts):
            try:
                response = self.model.generate_content(q)

                if not response or not response.text:
                    logger.debug(f"Нет ответа от модели. Попытка: {attempt}. Сон {2 ** attempt} секунд.", None, False)
                    time.sleep(2 ** attempt)
                    continue

                messages = [
                    {"role": "user", "content": q},
                    {"role": "assistant", "content": response.text}
                ]
                # self._save_dialogue(messages)
                return response.text

            except requests.exceptions.RequestException as ex:
                if attempt > self._MAX_ATTEMPTS:
                    break
                logger.debug(f"Сетевая ошибка. Попытка: {attempt}. Сон {self._NETWORK_ERROR_TIMEOUT/60} мин {gs.now=}", ex, False)
                time.sleep(self._NETWORK_ERROR_TIMEOUT)
                continue
            except (GatewayTimeout, ServiceUnavailable) as ex:
                if attempt > self._MAX_SERVICE_ATTEMPTS:
                   break
                logger.error("Сервис недоступен", ex, False)
                time.sleep(2 ** attempt)
                continue
            except ResourceExhausted as ex:
                if attempt > self._MAX_ATTEMPTS:
                   break
                logger.debug(f"Превышена квота. Попытка: {attempt}. Сон {self._QUOTA_EXCEEDED_TIMEOUT/60} мин {gs.now=}", ex, False)
                time.sleep(self._QUOTA_EXCEEDED_TIMEOUT)
                continue
            except (DefaultCredentialsError, RefreshError) as ex:
                logger.error("Ошибка аутентификации:",ex,False)
                return
            except (ValueError, TypeError) as ex:
                 if attempt > self._MAX_INPUT_ATTEMPTS:
                    break
                 logger.error(f"Неверный ввод. Попытка: {attempt}. Сон {self._INVALID_INPUT_TIMEOUT/60} мин {gs.now=}",ex, False)
                 time.sleep(self._INVALID_INPUT_TIMEOUT)
                 continue
            except (InvalidArgument, RpcError) as ex:
                logger.error("Ошибка API:",ex,False)
                return
            except Exception as ex:
                logger.error("Непредвиденная ошибка:",ex,False)
                return
        return

    def chat(self, q:str) -> Optional[str]:
        """
        Отправляет сообщение в чат и возвращает ответ.

        :param q: Сообщение для отправки в чат.
        :type q: str
        :return: Ответ от чат-бота.
        :rtype: Optional[str]
        """
        response = None
        try:
            response = self._chat.send_message(q)
            return response.text
        except Exception as ex:
            logger.error(f"Ошибка чата {response=}", ex, False)
            return

    def describe_image(self, image_path: Path) -> Optional[str]:
        """
        Генерирует описание изображения.

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
            with image_path.open('rb') as f:
                encoded_image = base64.b64encode(f.read()).decode('utf-8')

            response = self.model.generate_content(encoded_image)
            return response.text

        except Exception as ex:
            logger.error(f"Ошибка при описании изображения:", ex, False)
            return

    def upload_file(self, file: str | Path | IOBase, file_name:Optional[str] = None) -> bool:
        """
        Загружает файл в Google Generative AI.

        :param file: Путь к файлу, объект файла или строка с путем к файлу.
        :type file: str | Path | IOBase
        :param file_name: Имя файла.
        :type file_name: Optional[str]
        :return: True, если файл успешно загружен, False в противном случае.
        :rtype: bool

        .. _upload_file:
            https://github.com/google-gemini/generative-ai-python/blob/main/docs/api/google/generativeai/upload_file.md
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
            return response
        except Exception as ex:
            logger.error(f"Ошибка записи файла {file_name=}", ex, False)
            try:
                response = genai.delete_file(file_name)
                logger.debug(f"Файл {file_name} удален", None, False)
                self.upload_file(file,file_name)
            except Exception as ex:
                logger.error(f"Общая ошибка модели: ", ex, False)
                return

if __name__ == "__main__":
    ...
```