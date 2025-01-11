# Анализ кода модуля src.ai.gemini.generative_ai

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован, с использованием классов и асинхронных функций.
    - Присутствует обработка исключений для различных ситуаций, таких как сетевые ошибки, ошибки аутентификации и ошибки API.
    - Используется логгирование для отслеживания ошибок и отладки.
    - Применение `j_loads`, `j_dumps`, `j_loads_ns` для работы с JSON файлами.
    - Добавлены docstring для функций и классов.
    - Код разбит на логические блоки, что облегчает его чтение и понимание.
- Минусы
    -  В некоторых местах не используются f-строки для форматирования строк.
    -  В некоторых исключениях нет обработки `...` для отладки.
    -  `time.sleep()` может блокировать основной поток в асинхронном коде. Желательно использовать `asyncio.sleep()` вместо `time.sleep()`.
    -  В `describe_image` есть `print`, а должен быть `logger.debug`.
    -  Не всегда используется `None` для логгирования.
    -  В `upload_file` нет обработки `None` для `file_name`.

**Рекомендации по улучшению**

1.  **Использование f-строк**: Заменить конкатенацию строк на f-строки для лучшей читаемости и производительности.
2.  **Асинхронный `sleep`**: Заменить `time.sleep` на `asyncio.sleep` в асинхронных функциях для неблокирующей задержки.
3.  **Логирование**: Использовать `logger.debug` вместо `print` и везде указывать `None` как `exc_info`.
4.  **Улучшить обработку ошибок**: Добавить `...` в блоки `except Exception` для отладки.
5.  **Документация**:  Дополнить `docstring` в соответствии со стандартом `Sphinx`.
6.  **Обработка `None`**:  Добавить обработку `None` для `file_name` в `upload_file`.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для интеграции с Google Generative AI.
=========================================================================================

Этот модуль содержит класс :class:`GoogleGenerativeAI`, который используется для взаимодействия с моделями Google Generative AI,
такими как Gemini, для выполнения задач по генерации текста и обработки изображений.

Пример использования
--------------------

Пример использования класса `GoogleGenerativeAI`:

.. code-block:: python

    api_key = "YOUR_API_KEY"
    system_instruction = "Ты - полезный ассистент. Отвечай на все вопросы кратко"
    ai = GoogleGenerativeAI(api_key=api_key, system_instruction=system_instruction)

    # Пример вызова describe_image с промптом
    image_path = Path(r"test.jpg")  # Замените на путь к вашему изображению
    description = await ai.describe_image(image_path, prompt=prompt)
"""

import asyncio
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

import header
from src.logger.logger import logger #импортируем логгер
from src import gs

from src.utils.file import read_text_file, save_text_file
from src.utils.date_time import TimeoutCheck
from src.utils.convertors.unicode import decode_unicode_escape
from src.utils.jjson import j_loads, j_loads_ns, j_dumps
from src.utils.image import get_image_bytes

timeout_check = TimeoutCheck()


class GoogleGenerativeAI:
    """
    Класс для взаимодействия с моделями Google Generative AI.

    :param api_key: API ключ для доступа к Google Generative AI.
    :type api_key: str
    :param model_name: Название модели для использования.
    :type model_name: str, optional
    :param generation_config: Конфигурация для генерации.
    :type generation_config: dict, optional
    :param system_instruction: Системные инструкции для модели.
    :type system_instruction: str, optional
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

        :param api_key: API ключ для доступа к Google Generative AI.
        :type api_key: str
        :param model_name: Название модели для использования. По умолчанию 'gemini-2.0-flash-exp'.
        :type model_name: str, optional
        :param generation_config: Конфигурация для генерации. По умолчанию {"response_mime_type": "text/plain"}.
        :type generation_config: dict, optional
        :param system_instruction: Системные инструкции для модели.
        :type system_instruction: str, optional
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
    def config(self) -> SimpleNamespace:
        """
        Получает конфигурацию из файла настроек.

        :return: Конфигурация в виде SimpleNamespace.
        :rtype: SimpleNamespace
        """
        return j_loads_ns(gs.path.src / 'ai' / 'gemini' / 'generative_ai.json')

    def _start_chat(self):
        """
        Запускает новый чат с моделью, при наличии системных инструкций добавляет их в начало истории.

        :return: Объект чата.
        :rtype: google.generativeai.generative_models.ChatSession
        """
        if self.system_instruction:
            return self.model.start_chat(history=[{'role': 'user', 'parts': [self.system_instruction]}])
        else:
            return self.model.start_chat(history=[])

    def _save_dialogue(self, dialogue: list):
        """
        Сохраняет диалог в JSON файл.

        :param dialogue: Список сообщений для сохранения.
        :type dialogue: list
        """
        for message in dialogue:
            j_dumps(data=message, file_path=self.history_json_file, mode='+a')

    async def _save_chat_history(self):
        """Сохраняет всю историю чата в JSON файл"""
        if self.chat_history:
            j_dumps(data=self.chat_history, file_path=self.history_json_file, mode='w')

    async def _load_chat_history(self):
        """Загружает историю чата из JSON файла"""
        try:
            if self.history_json_file.exists():
                self.chat_history = j_loads(self.history_json_file)
                self._chat = self._start_chat()
                for entry in self.chat_history:
                    self._chat.history.append(entry)
                logger.debug('История чата загружена из файла.', None, False)
        except Exception as e:
            logger.error(f'Ошибка загрузки истории чата: {e}', exc_info=True)

    async def ask(self, q: str, attempts: int = 15) -> Optional[str]:
        """
        Метод отправляет текстовый запрос модели и возвращает ответ.

        :param q: Текстовый запрос.
        :type q: str
        :param attempts: Количество попыток отправки запроса.
        :type attempts: int, optional
        :return: Ответ модели.
        :rtype: str, optional
        """
        for attempt in range(attempts):
            try:
                response = await self.model.generate_content_async(q)
                #response = response.resolve()

                if not response.text:
                    logger.debug(
                        f'No response from the model. Attempt: {attempt}\nSleeping for {2 ** attempt}',
                        exc_info=None
                    )
                    await asyncio.sleep(2**attempt)
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
                    f'Network error. Attempt: {attempt}\nSleeping for {timeout/60} min on {gs.now}',
                    ex,
                    None,
                )
                await asyncio.sleep(timeout)
                continue  # Повторить попытку
            except (GatewayTimeout, ServiceUnavailable) as ex:
                logger.error('Service unavailable:', ex, None)
                # Экспоненциальный бэк-офф для повторных попыток
                max_attempts = 3
                if attempt > max_attempts:
                    break
                await asyncio.sleep(2**attempt)
                continue
            except ResourceExhausted as ex:
                timeout = 10800
                logger.debug(
                    f'Quota exceeded. Attempt: {attempt}\nSleeping for {timeout/60} min on {gs.now}',
                    ex,
                    None,
                )
                await asyncio.sleep(timeout)
                continue
            except (DefaultCredentialsError, RefreshError) as ex:
                logger.error('Authentication error:', ex, None)
                return  # Прекратить попытки, если ошибка аутентификации
            except (ValueError, TypeError) as ex:
                max_attempts = 3
                if attempt > max_attempts:
                    break
                timeout = 5
                logger.error(
                    f'Invalid input: Attempt: {attempt}\nSleeping for {timeout/60} min on {gs.now}',
                    ex,
                    None,
                )
                await asyncio.sleep(timeout)
                continue
            except (InvalidArgument, RpcError) as ex:
                logger.error('API error:', ex, None)
                return
            except Exception as ex:
                logger.error('Unexpected error:', ex, None)
                return

        return

    async def chat(self, q: str) -> Optional[str]:
        """
         Отправляет текстовый запрос в чат модели и возвращает ответ.

        :param q: Текстовый запрос.
        :type q: str
        :return: Ответ модели.
        :rtype: str, optional
        """
        response = None
        try:
            await self._load_chat_history()
            response = await self._chat.send_message_async(q)
            #response = await response.resolve()
            if response and response.text:
                self.chat_history.append({'role': 'user', 'parts': [q]})
                self.chat_history.append({'role': 'assistant', 'parts': [response.text]})
                self._save_dialogue(self.chat_history)
                return response.text
            else:
                logger.error('Empty response in chat', None)
                return
        except Exception as ex:
            logger.error(f'Ошибка чата {response=}', ex)
            return
        finally:
            await self._save_chat_history()

    async def describe_image(
        self, image: Path | bytes, mime_type: Optional[str] = 'image/jpeg', prompt: Optional[str] = ''
    ) -> Optional[str]:
        """
        Отправляет изображение в Gemini Pro Vision и возвращает его текстовое описание.

        :param image: Путь к файлу изображения или байты изображения.
        :type image: Path | bytes
        :param mime_type: MIME тип изображения. По умолчанию 'image/jpeg'.
        :type mime_type: str, optional
        :param prompt: Дополнительный текстовый запрос для описания изображения.
        :type prompt: str, optional
        :return: Текстовое описание изображения.
        :rtype: str, optional
        """
        try:
            # Подготовка контента для запроса
            if isinstance(image, Path):
                image = get_image_bytes(image)

            content = [
                {
                    'role': 'user',
                    'parts': {
                        'inlineData': [
                            {
                                'mimeType': mime_type, # Измени на mime-тип твоего  изображения ('image/jpeg','image/png')
                                'data': image,
                            }
                        ]
                    }
                }
            ]

            # Отправка запроса и получение ответа
            #response = self.model.generate_content(content)
            #response = self.model.generate_content(image)
            response = self.model.generate_content(
                str(
                    {
                        'text':prompt,
                        'data':image
                    }
                    ))
            #response = response.resolve()

            if response.text:
                return response.text
            else:
                logger.debug('Модель вернула пустой ответ.', None)
                return None

        except Exception as ex:
            logger.error(f'Произошла ошибка: {ex}', exc_info=True)
            ...
            return None

    async def upload_file(
        self, file: str | Path | IOBase, file_name: Optional[str] = None
    ) -> bool:
        """
        Загружает файл в Google Generative AI.

        :param file: Путь к файлу, файловый объект или байтовая строка.
        :type file: str | Path | IOBase
        :param file_name: Название файла.
        :type file_name: str, optional
        :return: Возвращает True если загрузка прошла успешно, False в случае ошибки.
        :rtype: bool
        """

        response = None
        try:
            if not file_name:
                logger.error('Не указано имя файла для загрузки.', exc_info=True)
                return False

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
            logger.error(f'Ошибка записи файла {file_name=}', ex, False)
            try:
                response = await genai.delete_file_async(file_name)
                logger.debug(f'Файл {file_name} удален', None, False)
                await self.upload_file(file, file_name)
            except Exception as ex:
                logger.error('Общая ошибка модели: ', ex, False)
                ...
                return


async def main():
    # Замените на свой ключ API
    api_key = 'YOUR_API_KEY'
    system_instruction = 'Ты - полезный ассистент. Отвечай на все вопросы кратко'
    ai = GoogleGenerativeAI(api_key=api_key, system_instruction=system_instruction)

    # Пример вызова describe_image с промптом
    image_path = Path(r'test.jpg')  # Замените на путь к вашему изображению

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

        # Пример без JSON вывода
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

    # Пример чата
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