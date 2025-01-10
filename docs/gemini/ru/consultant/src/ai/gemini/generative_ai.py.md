# Анализ кода модуля `generative_ai.py`

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован и разбит на функции, что облегчает его понимание и поддержку.
    - Используется асинхронное программирование с `asyncio` для неблокирующих операций.
    - Присутствует обработка исключений для различных сценариев ошибок, таких как сетевые ошибки, ошибки аутентификации и таймауты.
    - Используется логирование через `logger` для отслеживания ошибок и отладки.
    -  Используются кастомные функции `j_loads`, `j_dumps`, `j_loads_ns` из `src.utils.jjson` для работы с `json`.
    -  Для работы с изображениями используется кастомная функция `get_image_bytes` из `src.utils.image`.
    - Имеется базовая документация в виде docstring.
- Минусы
    - Не везде используется `logger.error` для обработки ошибок, местами используется `print`.
    - Некоторые docstring требуют более подробного описания аргументов и возвращаемых значений.
    - В некоторых блоках `try-except` не всегда корректно обрабатываются ошибки, например, не возвращается `None` в случае ошибки в `describe_image`.
    - Не все функции документированы в формате RST.
    - Присутствует избыточное использование `try-except`.
    - Присутствует `...` в обработчиках исключений, что затрудняет понимание и отладку.
    - В `describe_image` при передаче изображения в виде байтов не корректно формируется запрос.
    - `save_dialogue` сохраняет каждую запись в отдельной строке, что не соответствует формату `json`.
    - Присутствует дублирование кода загрузки и сохранения истории чата в методы `_save_chat_history` и `_load_chat_history`, код можно объединить в общую функцию.
    - В блоке  `main`  необходимо перенести константы в начало модуля.

**Рекомендации по улучшению**

1.  **Документация:**
    - Добавить подробные docstring в формате RST для всех функций, методов и классов.
    - Уточнить описание аргументов и возвращаемых значений в docstring.
2.  **Логирование:**
    - Заменить все `print` на `logger.error`, `logger.debug` или `logger.info`.
    - Добавить больше контекста в логи, включая значения переменных и текущее время, где это необходимо.
3.  **Обработка ошибок:**
    - Избегать избыточного использования `try-except`, обрабатывая ошибки с помощью `logger.error` и возвращая `None` в случае ошибки.
    - Убрать `...` и добавить обработку ошибок.
4.  **Рефакторинг:**
    - Устранить дублирование кода сохранения и загрузки истории чата.
    - Улучшить обработку ответа в `describe_image` и формировании запроса.
    - Перенести константы (например, `api_key`, `system_instruction`) в начало модуля.
5.  **Форматирование:**
    - Привести все кавычки к одинарным (кроме `print` и `logger.error`).
6.  **Сохранение истории чата:**
    - Переделать сохранение истории чата, чтобы данные записывались в корректном формате `json`.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/bin/python/python3.12
"""
Модуль для взаимодействия с моделями Google Generative AI.
=========================================================================================

Этот модуль содержит класс :class:`GoogleGenerativeAI`, который используется для взаимодействия с различными моделями ИИ Google,
такими как Gemini, для выполнения задач по обработке текста и изображений.

Пример использования
--------------------

Пример использования класса `GoogleGenerativeAI`:

.. code-block:: python

    api_key = 'YOUR_API_KEY'
    ai = GoogleGenerativeAI(api_key=api_key, system_instruction='Ты - полезный ассистент')
    response = await ai.ask('Привет!')
    print(response)
"""
import asyncio
import time
from io import IOBase
from pathlib import Path
from typing import Optional, Dict, List, Any
import base64

import google.generativeai as genai
import requests
from google.api_core.exceptions import (
    GatewayTimeout,
    ServiceUnavailable,
    ResourceExhausted,
    InvalidArgument,
)
from google.auth.exceptions import DefaultCredentialsError, RefreshError
from grpc import RpcError

from src.logger.logger import logger
from src import gs
from src.utils.file import read_text_file, save_text_file
from src.utils.date_time import TimeoutCheck
from src.utils.convertors.unicode import decode_unicode_escape
from src.utils.jjson import j_loads, j_loads_ns, j_dumps
from src.utils.image import get_image_bytes

timeout_check = TimeoutCheck()

API_KEY = "YOUR_API_KEY"  # TODO: Заменить на свой ключ API
SYSTEM_INSTRUCTION = "Ты - полезный ассистент. Отвечай на все вопросы кратко"


class GoogleGenerativeAI:
    """
    Класс для взаимодействия с моделями Google Generative AI.

    Args:
        api_key (str): API ключ Google Generative AI.
        model_name (Optional[str]): Название модели. По умолчанию "gemini-2.0-flash-exp".
        generation_config (Optional[Dict]): Конфигурация генерации.
        system_instruction (Optional[str]): Системная инструкция для модели.

    Attributes:
        MODELS (List[str]): Список доступных моделей.
    """

    MODELS = [
        'gemini-1.5-flash-8b',
        'gemini-2-13b',
        'gemini-3-20b',
        'gemini-2.0-flash-exp',
    ]

    def __init__(
        self,
        api_key: str,
        model_name: Optional[str] = None,
        generation_config: Optional[Dict] = None,
        system_instruction: Optional[str] = None,
        **kwargs,
    ):
        """
        Инициализация модели GoogleGenerativeAI с дополнительными настройками.

        Args:
            api_key (str): API ключ Google Generative AI.
            model_name (Optional[str]): Название модели. По умолчанию "gemini-2.0-flash-exp".
            generation_config (Optional[Dict]): Конфигурация генерации.
            system_instruction (Optional[str]): Системная инструкция для модели.
        """
        self.api_key = api_key
        self.model_name = model_name or 'gemini-2.0-flash-exp'
        self.generation_config = generation_config or {'response_mime_type': 'text/plain'}
        self.system_instruction = system_instruction

        self.dialogue_log_path: Path = Path(gs.path.external_storage, 'AI', 'log')
        self.dialogue_txt_path: Path = self.dialogue_log_path / f'gemini_{gs.now}.txt'
        self.history_dir: Path = Path(gs.path.external_storage, 'AI', 'history')
        self.history_txt_file: Path = self.history_dir / f'gemini_{gs.now}.txt'
        self.history_json_file: Path = self.history_dir / f'gemini_{gs.now}.json'

        # Инициализация модели
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(
            model_name=self.model_name, generation_config=self.generation_config
        )
        self._chat = self._start_chat()
        self.chat_history = []

    @property
    def config(self):
        """Получаю конфигурацию из файла настроек."""
        return j_loads_ns(gs.path.src / 'ai' / 'gemini' / 'generative_ai.json')

    def _start_chat(self):
        """Инициализирует чат с системной инструкцией или без нее."""
        if self.system_instruction:
            return self.model.start_chat(history=[{'role': 'user', 'parts': [self.system_instruction]}])
        else:
            return self.model.start_chat(history=[])

    def _save_dialogue(self, dialogue: list):
        """
        Сохраняет диалог в JSON файл.

        Args:
            dialogue (list): Список сообщений для сохранения.
        """
        try:
            j_dumps(data=dialogue, file_path=self.history_json_file, mode='a')
        except Exception as ex:
            logger.error(f'Ошибка сохранения диалога: {ex}', None, False)

    async def _save_chat_history(self):
        """Сохраняет всю историю чата в JSON файл."""
        if self.chat_history:
            try:
                j_dumps(data=self.chat_history, file_path=self.history_json_file, mode='w')
            except Exception as ex:
                logger.error(f'Ошибка сохранения истории чата: {ex}', None, False)

    async def _load_chat_history(self):
        """Загружает историю чата из JSON файла."""
        try:
            if self.history_json_file.exists():
                self.chat_history = j_loads(self.history_json_file)
                self._chat = self._start_chat()
                for entry in self.chat_history:
                    self._chat.history.append(entry)
                logger.debug('История чата загружена из файла.', None, False)
        except Exception as e:
            logger.error(f'Ошибка загрузки истории чата: {e}', None, False)

    async def ask(self, q: str, attempts: int = 15) -> Optional[str]:
        """
        Отправляет текстовый запрос модели и возвращает ответ.

        Args:
            q (str): Текст запроса.
            attempts (int): Максимальное количество попыток отправки запроса.

        Returns:
            Optional[str]: Текст ответа или None в случае ошибки.
        """
        for attempt in range(attempts):
            try:
                response = await self.model.generate_content_async(q)

                if not response.text:
                    logger.debug(
                        f'No response from the model. Attempt: {attempt}\\nSleeping for {2 ** attempt}',
                        None,
                        False,
                    )
                    time.sleep(2**attempt)
                    continue  # Повторить попытку

                messages = [
                    {'role': 'user', 'content': q},
                    {'role': 'assistant', 'content': response.text},
                ]

                return response.text

            except requests.exceptions.RequestException as ex:
                timeout = 1200
                max_attempts = 5
                if attempt > max_attempts:
                    break
                logger.debug(
                    f'Network error. Attempt: {attempt}\\nSleeping for {timeout/60} min on {gs.now}',
                    ex,
                    False,
                )
                time.sleep(timeout)
                continue  # Повторить попытку
            except (GatewayTimeout, ServiceUnavailable) as ex:
                logger.error(f'Service unavailable: {ex}', None, False)
                # Экспоненциальный бэк-офф для повторных попыток
                max_attempts = 3
                if attempt > max_attempts:
                    break
                time.sleep(2**attempt)
                continue
            except ResourceExhausted as ex:
                timeout = 10800
                logger.debug(
                    f'Quota exceeded. Attempt: {attempt}\\nSleeping for {timeout/60} min on {gs.now}',
                    ex,
                    False,
                )
                time.sleep(timeout)
                continue
            except (DefaultCredentialsError, RefreshError) as ex:
                logger.error(f'Authentication error: {ex}', None, False)
                return  # Прекратить попытки, если ошибка аутентификации
            except (ValueError, TypeError) as ex:
                max_attempts = 3
                if attempt > max_attempts:
                    break
                timeout = 5
                logger.error(
                    f'Invalid input: Attempt: {attempt}\\nSleeping for {timeout/60} min on {gs.now}',
                    ex,
                    None,
                )
                time.sleep(timeout)
                continue
            except (InvalidArgument, RpcError) as ex:
                logger.error(f'API error: {ex}', None, False)
                return
            except Exception as ex:
                logger.error(f'Unexpected error: {ex}', None, False)
                return
        return None

    async def chat(self, q: str) -> Optional[str]:
        """
        Отправляет сообщение в чат и возвращает ответ.

        Args:
            q (str): Текст сообщения.

        Returns:
            Optional[str]: Текст ответа или None в случае ошибки.
        """
        response = None
        try:
            await self._load_chat_history()
            response = await self._chat.send_message_async(q)
            if response and response.text:
                self.chat_history.append({'role': 'user', 'parts': [q]})
                self.chat_history.append({'role': 'assistant', 'parts': [response.text]})
                self._save_dialogue(self.chat_history)
                return response.text
            else:
                logger.error('Empty response in chat', None, False)
                return None
        except Exception as ex:
            logger.error(f'Ошибка чата {response=}: {ex}', None, False)
            return None
        finally:
            await self._save_chat_history()

    async def describe_image(
        self, image: Path | bytes, mime_type: Optional[str] = 'image/jpeg', prompt: Optional[str] = ''
    ) -> Optional[str]:
        """
        Отправляет изображение в Gemini Pro Vision и возвращает его текстовое описание.

        Args:
            image (Path | bytes): Путь к файлу изображения или байты изображения.
            mime_type (Optional[str]): MIME тип изображения. По умолчанию 'image/jpeg'.
            prompt (Optional[str]): Текст запроса.

        Returns:
            Optional[str]: Текстовое описание изображения или None в случае ошибки.
        """
        try:
            if isinstance(image, Path):
                 image = get_image_bytes(image)
            if isinstance(image, bytes):
                content = [
                    {
                        'role': 'user',
                        'parts': [
                                {
                                    'mimeType': mime_type,
                                    'data': base64.b64encode(image).decode('utf-8'),
                                    }
                            ]
                    }
                ]
            else:
                logger.error(f'Неверный тип данных изображения {type(image)=}', None, False)
                return None
            response = await self.model.generate_content_async(content)

            if response.text:
                 return response.text
            else:
                logger.error('Модель вернула пустой ответ.', None, False)
                return None
        except Exception as ex:
            logger.error(f'Произошла ошибка: {ex}', None, False)
            return None

    async def upload_file(
        self, file: str | Path | IOBase, file_name: Optional[str] = None
    ) -> bool:
        """
        Загружает файл в Google Generative AI.

        Args:
            file (str | Path | IOBase): Путь к файлу, сам файл или объект IOBase.
            file_name (Optional[str]): Имя файла.

        Returns:
            bool: True, если файл успешно загружен, False в противном случае.
        """
        response = None
        try:
            response = await genai.upload_file_async(
                path=file,
                mime_type=None,
                name=file_name,
                display_name=file_name,
                resumable=True,
            )
            logger.debug(f'Файл {file_name} записан', None, False)
            return response
        except Exception as ex:
            logger.error(f'Ошибка записи файла {file_name=}: {ex}', None, False)
            try:
                response = await genai.delete_file_async(file_name)
                logger.debug(f'Файл {file_name} удален', None, False)
                await self.upload_file(file, file_name)
            except Exception as ex:
                logger.error(f'Общая ошибка модели: {ex}', None, False)
                return False
        return False


async def main():
    """
    Основная функция для демонстрации работы с классом GoogleGenerativeAI.
    """
    ai = GoogleGenerativeAI(api_key=API_KEY, system_instruction=SYSTEM_INSTRUCTION)

    image_path = Path('test.jpg')

    if not image_path.is_file():
        print(
            f'Файл {image_path} не существует. Поместите в корневую папку с программой файл с названием test.jpg'
        )
    else:
        prompt = """Проанализируй это изображение. Выдай ответ в формате JSON,
        где ключом будет имя объекта, а значением его описание.
        Если есть люди, опиши их действия."""
        description = await ai.describe_image(image_path, prompt=prompt)
        if description:
            print('Описание изображения (с JSON форматом):')
            print(description)
            try:
                parsed_description = j_loads(description)
            except Exception as ex:
                print('Не удалось распарсить JSON. Получен текст:')
                print(description)
        else:
            print('Не удалось получить описание изображения.')

        prompt = 'Проанализируй это изображение. Перечисли все объекты, которые ты можешь распознать.'
        description = await ai.describe_image(image_path, prompt=prompt)
        if description:
            print('Описание изображения (без JSON формата):')
            print(description)

    file_path = Path('test.txt')
    with open(file_path, 'w') as f:
        f.write('Hello, Gemini!')

    file_upload = await ai.upload_file(file_path, 'test_file.txt')
    print(file_upload)

    while True:
        user_message = input('You: ')
        if user_message.lower() == 'exit':
            break
        ai_message = await ai.chat(user_message)
        if ai_message:
            print(f'Gemini: {ai_message}')
        else:
            print('Gemini: Ошибка получения ответа')


if __name__ == '__main__':
    asyncio.run(main())
```