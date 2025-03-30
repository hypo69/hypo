### Анализ кода модуля `generative_ai`

**Качество кода**:
- **Соответствие стандартам**: 7/10
- **Плюсы**:
    - Использование асинхронности для неблокирующих операций.
    - Наличие базовой обработки ошибок и повторных попыток при сбоях.
    - Разделение функциональности на методы, что облегчает чтение кода.
    - Присутствует сохранение истории диалогов и чата.
- **Минусы**:
    - Неполная документация в формате RST.
    - Смешение стилей кавычек (одинарные и двойные).
    - Использование `print` вместо `logger.info` для вывода сообщений.
    - Избыточное использование `try-except` блоков с общими `Exception` без конкретизации.
    - Многократное дублирование кода в обработке ошибок (например, sleep).
    - Не все методы имеют RST-документацию.

**Рекомендации по улучшению**:

1.  **Документация**:
    - Добавить полноценные RST-комментарии для всех классов, методов и функций, включая описание параметров и возвращаемых значений.

2.  **Стиль кода**:
    - Привести в порядок все кавычки, используя одинарные (`'`) для кода и двойные (`"`) для вывода.

3.  **Логирование**:
    - Заменить `print()` на `logger.info()` или `logger.debug()` для вывода сообщений, связанных с состоянием выполнения.
    - Использовать `logger.error()` с конкретизацией ошибок (например, `Network error: {ex}`) и трассировкой стека.

4.  **Обработка ошибок**:
    - Уменьшить дублирование кода обработки ошибок, вынеся общую логику в отдельные функции, если это возможно.
    - Конкретизировать исключения, которые обрабатываются. Вместо `except Exception as ex:` использовать более конкретные исключения.

5.  **Импорты**:
    - Выровнять импорты по алфавиту и длине для лучшей читаемости.
    - Привести все импорты к стандарту, используя `from src.logger.logger import logger`.

6.  **Общее**:
    - Избегать пустых `except` блоков с `...`. Вместо этого использовать `pass` или логировать ошибку.
    - Использовать константы для магических чисел (например, для таймаутов).
    - Пересмотреть логику повторных попыток, возможно использовать декораторы.

**Оптимизированный код**:

```python
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
Модуль для работы с ассистентом программиста Google Gemini
=========================================================

Модуль содержит класс :class:`GoogleGenerativeAI`, который используется для взаимодействия
с моделями Google Generative AI и выполнения задач обработки текста и изображений.

Пример использования
----------------------
.. code-block:: python

    api_key = 'YOUR_API_KEY'
    ai = GoogleGenerativeAI(api_key=api_key, system_instruction='You are a helpful assistant.')
    response = await ai.ask('What is the capital of France?')
    print(response)
"""
import asyncio
import time
import base64
from io import IOBase
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, List
from types import SimpleNamespace

import google.generativeai as genai
import requests

from grpc import RpcError
from google.api_core.exceptions import (
    GatewayTimeout,
    InvalidArgument,
    ResourceExhausted,
    ServiceUnavailable,
)
from google.auth.exceptions import DefaultCredentialsError, RefreshError

from src import gs
from src.logger.logger import logger  # Исправленный импорт
from src.utils.convertors.unicode import decode_unicode_escape
from src.utils.date_time import TimeoutCheck
from src.utils.file import read_text_file, save_text_file
from src.utils.image import get_image_bytes
from src.utils.jjson import j_dumps, j_loads, j_loads_ns
# from src.utils.printer import pprint as print # Удален лишний импорт


TIMEOUT_CHECK = TimeoutCheck()
MAX_ATTEMPTS_DEFAULT = 5
DEFAULT_MODEL_NAME = 'gemini-2.0-flash-exp'
class GoogleGenerativeAI:
    """
    Класс для взаимодействия с моделями Google Generative AI.
    
    :param api_key: API-ключ Google Gemini.
    :type api_key: str
    :param model_name: Название модели, по умолчанию 'gemini-2.0-flash-exp'.
    :type model_name: Optional[str]
    :param generation_config: Дополнительные параметры конфигурации генерации.
    :type generation_config: Optional[Dict]
    :param system_instruction: Инструкции для модели.
    :type system_instruction: Optional[str]
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
        
        :param api_key: API-ключ Google Gemini.
        :type api_key: str
        :param model_name: Название модели, по умолчанию 'gemini-2.0-flash-exp'.
        :type model_name: Optional[str]
        :param generation_config: Дополнительные параметры конфигурации генерации.
        :type generation_config: Optional[Dict]
        :param system_instruction: Инструкции для модели.
        :type system_instruction: Optional[str]
        """
        self.api_key = api_key
        self.model_name = model_name or DEFAULT_MODEL_NAME # Исправлено на константу
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
    def config(self) -> SimpleNamespace:
        """
        Получает конфигурацию из файла настроек.

        :return: Конфигурация в виде SimpleNamespace.
        :rtype: SimpleNamespace
        """
        return j_loads_ns(gs.path.src / 'ai' / 'gemini' / 'generative_ai.json')

    def _start_chat(self):
        """
        Начинает новый чат, устанавливая историю, если она есть.
        
        :return: Экземпляр чата с историей или без.
        :rtype: google.generativeai.generative_model.ChatSession
        """
        if self.system_instruction:
            return self.model.start_chat(history=[{'role': 'user', 'parts': [self.system_instruction]}])
        else:
            return self.model.start_chat(history=[])

    def _save_dialogue(self, dialogue: list) -> None:
        """
        Сохраняет диалог в JSON файл.
        
        :param dialogue: Список сообщений для сохранения.
        :type dialogue: list
        """
        for message in dialogue:
            j_dumps(data=message, file_path=self.history_json_file, mode='+a')

    async def _save_chat_history(self) -> None:
         """
         Сохраняет всю историю чата в JSON файл.
        """
         if self.chat_history:
            j_dumps(data=self.chat_history, file_path=self.history_json_file, mode='w')

    async def _load_chat_history(self) -> None:
        """
         Загружает историю чата из JSON файла.
        """
        try:
            if self.history_json_file.exists():
                self.chat_history = j_loads(self.history_json_file)
                self._chat = self._start_chat()
                for entry in self.chat_history:
                    self._chat.history.append(entry)
                logger.debug('История чата загружена из файла.', None, False)
        except Exception as e:
            logger.error(f'Ошибка загрузки истории чата: {e}', None, False)

    async def ask(self, q: str, attempts: int = MAX_ATTEMPTS_DEFAULT) -> Optional[str]:
        """
        Метод отправляет текстовый запрос модели и возвращает ответ.
        
        :param q: Текстовый запрос.
        :type q: str
        :param attempts: Максимальное количество попыток запроса.
        :type attempts: int, optional
        :return: Ответ модели или None в случае ошибки.
        :rtype: Optional[str]
        """

        for attempt in range(attempts):
            try:
                response = await self.model.generate_content_async(q)

                if not response.text:
                    logger.debug(
                        f'No response from the model. Attempt: {attempt}\\nSleeping for {2 ** attempt}'
                    )
                    time.sleep(2**attempt)
                    continue  # Повторить попытку

                messages = [
                    {'role': 'user', 'content': q},
                    {'role': 'assistant', 'content': response.text},
                ]

                # self._save_dialogue([messages])
                return response.text

            except requests.exceptions.RequestException as ex:
                timeout = 1200
                max_attempts = 5
                if attempt > max_attempts:
                    break
                logger.debug(
                    f'Network error. Attempt: {attempt}\\nSleeping for {timeout/60} min on {gs.now}',
                    ex,
                    None,
                )
                time.sleep(timeout)
                continue  # Повторить попытку

            except (GatewayTimeout, ServiceUnavailable) as ex:
                 logger.error(f'Service unavailable: {ex}', None)
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
                    None,
                )
                time.sleep(timeout)
                continue

            except (DefaultCredentialsError, RefreshError) as ex:
                logger.error(f'Authentication error: {ex}', None)
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
                logger.error(f'API error: {ex}', None)
                return
            except Exception as ex:
                logger.error(f'Unexpected error: {ex}', None)
                return

        return

    async def chat(self, q: str) -> Optional[str]:
        """
        Отправляет сообщение в чат и возвращает ответ.
        
        :param q: Сообщение пользователя.
        :type q: str
        :return: Ответ модели или None в случае ошибки.
        :rtype: Optional[str]
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
                 logger.error('Empty response in chat', None)
                 return None
        except Exception as ex:
             logger.error(f'Ошибка чата {response=}', ex)
             return None
        finally:
           await self._save_chat_history()

    async def describe_image(
        self, image: Path | bytes, mime_type: Optional[str] = 'image/jpeg', prompt: Optional[str] = ''
    ) -> Optional[str]:
        """
        Отправляет изображение в Gemini Pro Vision и возвращает его текстовое описание.

        :param image: Путь к файлу изображения или байты изображения.
        :type image: Path | bytes
        :param mime_type: MIME-тип изображения, по умолчанию 'image/jpeg'.
        :type mime_type: Optional[str]
        :param prompt: Текстовый запрос для модели.
        :type prompt: Optional[str]
        :return: Текстовое описание изображения или None в случае ошибки.
        :rtype: Optional[str]
        """
        try:
            if isinstance(image, Path):
                image = get_image_bytes(image)

            content = [
                {
                    'role': 'user',
                    'parts': {
                        'inlineData': [
                            {
                                'mimeType': mime_type,  # Измени на mime-тип твоего  изображения ('image/jpeg','image/png')
                                'data': image,
                            }
                        ]
                    },
                }
            ]

            response = self.model.generate_content(
                str(
                    {
                        'text': prompt,
                        'data': image
                    }
                ))

            if response.text:
                return response.text
            else:
                logger.info('Модель вернула пустой ответ.')
                return None

        except Exception as ex:
             logger.error(f'Произошла ошибка: {ex}', None)
             return None

    async def upload_file(
        self, file: str | Path | IOBase, file_name: Optional[str] = None
    ) -> bool:
        """
        Загружает файл в Google Gemini API.

        :param file: Путь к файлу, байты файла или файловый объект.
        :type file: str | Path | IOBase
        :param file_name: Имя файла для загрузки.
        :type file_name: Optional[str]
        :return: True в случае успешной загрузки, иначе False.
        :rtype: bool
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
             logger.error(f'Ошибка записи файла {file_name=}: {ex}', ex, False)
            
             try:
                 response = await genai.delete_file_async(file_name)
                 logger.debug(f'Файл {file_name} удален', None, False)
                 await self.upload_file(file, file_name)
             except Exception as ex:
                 logger.error(f'Общая ошибка модели: {ex}', ex, False)
                 return False

async def main():
    # Замените на свой ключ API
    api_key = 'YOUR_API_KEY'
    system_instruction = 'Ты - полезный ассистент. Отвечай на все вопросы кратко'
    ai = GoogleGenerativeAI(api_key=api_key, system_instruction=system_instruction)

    # Пример вызова describe_image с промптом
    image_path = Path(r'test.jpg')  # Замените на путь к вашему изображению

    if not image_path.is_file():
         logger.info(
             f'Файл {image_path} не существует. Поместите в корневую папку с программой файл с названием test.jpg'
        )
    else:
        prompt = """Проанализируй это изображение. Выдай ответ в формате JSON,
        где ключом будет имя объекта, а значением его описание.
        Если есть люди, опиши их действия."""

        description = await ai.describe_image(image_path, prompt=prompt)
        if description:
            logger.info('Описание изображения (с JSON форматом):')
            logger.info(description)
            try:
                parsed_description = j_loads(description)

            except Exception as ex:
                logger.info('Не удалось распарсить JSON. Получен текст:')
                logger.info(description)

        else:
             logger.info('Не удалось получить описание изображения.')

        # Пример без JSON вывода
        prompt = 'Проанализируй это изображение. Перечисли все объекты, которые ты можешь распознать.'
        description = await ai.describe_image(image_path, prompt=prompt)
        if description:
            logger.info('Описание изображения (без JSON формата):')
            logger.info(description)

    file_path = Path('test.txt')
    with open(file_path, 'w') as f:
        f.write('Hello, Gemini!')

    file_upload = await ai.upload_file(file_path, 'test_file.txt')
    logger.info(file_upload)

    # Пример чата
    while True:
        user_message = input('You: ')
        if user_message.lower() == 'exit':
            break
        ai_message = await ai.chat(user_message)
        if ai_message:
            logger.info(f'Gemini: {ai_message}')
        else:
            logger.info('Gemini: Ошибка получения ответа')


if __name__ == '__main__':
    asyncio.run(main())