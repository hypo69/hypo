## \file src/ai/gemini/gemini.py
## \file src/ai/gemini/gemini.py
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3

"""
.. module::  src.ai.gemini.gemini
   :platform: Windows, Unix
   :synopsis: Google generative AI integration
   https://github.com/google-gemini/generative-ai-python/blob/main/docs/api/google/generativeai.md
"""
import codecs
import re
import asyncio
import time
import json
import requests
from io import IOBase
from pathlib import Path
from typing import Optional, Dict, List, Any
from types import SimpleNamespace
from dataclasses import dataclass, field
import base64

import google.generativeai as genai


from grpc import RpcError
from google.api_core.exceptions import (
    GatewayTimeout,
    RetryError,
    ServiceUnavailable,
    ResourceExhausted,
    InvalidArgument,
)
from google.auth.exceptions import (
    DefaultCredentialsError, 
    RefreshError,
)

import header
from header import __root__
from src import gs

from src.utils.file import read_text_file, save_text_file
from src.utils.date_time import TimeoutCheck
from src.utils.jjson import j_loads, j_loads_ns, j_dumps
from src.utils.image import get_image_bytes
from src.utils.string.ai_string_normalizer import normalize_answer
from src.utils.printer import pprint as print
from src.logger import logger

timeout_check = TimeoutCheck()

class Config:
    ...

@dataclass
class GoogleGenerativeAI:
    """
    Класс для взаимодействия с моделями Google Generative AI.
    """

    api_key: str
    model_name: str = field(default="gemini-2.0-flash-exp")
    dialogue_txt_path: Path = field(init=False)

    """generation_config.response_mime_type: allowed mimetypes are 
    `text/plain`, 
    `application/json`, 
    `application/xml`, 
    `application/yaml` and 
    `text/x.enum`."""
    generation_config: Dict = field(default_factory=lambda: {"response_mime_type": "text/plain"})
    system_instruction: Optional[str] = None
    history_dir: Path = field(init=False)
    history_txt_file: Path = field(init=False)
    history_json_file: Path = field(init=False)
    config:SimpleNamespace = field(default_factory=lambda: j_loads_ns(__root__ / 'src' / 'ai' / 'gemini' / 'gemini.json'), init=False)
    chat_history: List[Dict] = field(default_factory=list, init=False)
    model: Any = field(init=False)
    _chat: Any = field(init=False)

    MODELS: List[str] = field(default_factory=lambda: [
        "gemini-1.5-flash-8b",
        "gemini-2-13b",
        "gemini-3-20b",
        "gemini-2.0-flash-exp",
    ])

    def __post_init__(self):
        """Инициализация модели GoogleGenerativeAI с дополнительными настройками."""

        self.config = j_loads_ns(__root__ / 'src' / 'ai' / 'gemini' / 'gemini.json')

        _dialogue_log_path:Path = Path(__root__, gs.path.external_storage, "gemini_data", "log")
        _history_dir:Path = Path(__root__, gs.path.external_storage, "gemini_data", "history")

        self.dialogue_txt_path = _dialogue_log_path / f"gemini_{gs.now}.txt"
        self.history_txt_file = _history_dir / f"gemini_{gs.now}.txt"
        self.history_json_file = _history_dir / f"gemini_{gs.now}.json"

        # Инициализация модели
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(
            model_name=self.model_name, 
            generation_config=self.generation_config,
            system_instruction=self.system_instruction
        )
        self._chat = self._start_chat()

    def normalize_answer(self, text:str) -> str:
        """Очистка вывода от 
        ```md, ```python, ```json, ```html, ит.п.
        """
        return normalize_answer(text)

    def _start_chat(self):
        """Запуск чата с начальной настройкой."""
        if self.system_instruction:
            return self.model.start_chat(history=[{"role": "user", "parts": [self.system_instruction]}])
        else:
            return self.model.start_chat(history=[])

    def clear_history(self):
        """
        Очищает историю чата в памяти и удаляет файл истории, если он существует.
        """
        try:
            self.chat_history = []  # Очистка истории в памяти
            if self.history_json_file.exists():
                self.history_json_file.unlink()  # Удаление файла истории
                logger.info(f"Файл истории {self.history_json_file} удалён.")
        except Exception as ex:
            logger.error("Ошибка при очистке истории чата.", ex, False)

    async def _save_chat_history(self, chat_data_folder: Optional[str | Path]):
        """Сохраняет всю историю чата в JSON файл"""
        if chat_data_folder:
            self.history_json_file = Path(chat_data_folder, 'history.json')
        if self.chat_history:
            j_dumps(data=self.chat_history, file_path=self.history_json_file, mode="w")

    async def _load_chat_history(self, chat_data_folder: Optional[str | Path]):
        """Загружает историю чата из JSON файла"""
        try:
            if chat_data_folder:
                self.history_json_file = Path(chat_data_folder, 'history.json')

            if self.history_json_file.exists():
                self.chat_history = j_loads(self.history_json_file)
                self._chat = self._start_chat()
                for entry in self.chat_history:
                    self._chat.history.append(entry)
                logger.info(f"История чата загружена из файла. \n{self.history_json_file=}", None, False)
        except Exception as ex:
            logger.error(f"Ошибка загрузки истории чата из файла {self.history_json_file=}", ex, False)

    async def chat(self, q: str, chat_data_folder: Optional[str | Path], flag: str = "save_chat") -> Optional[str]:
        """
        Обрабатывает чат-запрос с различными режимами управления историей чата.

        Args:
            q (str): Вопрос пользователя.
            chat_data_folder (Optional[str | Path]): Папка для хранения истории чата.
            flag (str): Режим управления историей. Возможные значения: 
                        "save_chat", "read_and_clear", "clear", "start_new".

        Returns:
            Optional[str]: Ответ модели.
        """
        response = None
        try:
            if flag == "save_chat":
                await self._load_chat_history(chat_data_folder)

            if flag == "read_and_clear":
                print(f"Прочитал историю чата и начал новый", text_color='gray')
                await self._load_chat_history(chat_data_folder)
                self.chat_history = []  # Очистить историю

            if flag == "read_and_start_new":
                print(f"Прочитал историю чата, сохранил и начал новый", text_color='gray')
                await self._load_chat_history(chat_data_folder)
                self.chat_history = []  # Очистить историю
                flag = "start_new"
                

            elif flag == "clear":
                print(f"Вытер прошлую историю")
                self.chat_history = []  # Очистить историю
                

            elif flag == "start_new":
                
                timestamp = time.strftime("%Y%m%d_%H%M%S")
                print(f"Сохранил прошлую историю в {timestamp}", text_color='gray')
                archive_file = self.history_dir / f"history_{timestamp}.json"
                if self.chat_history:
                    j_dumps(data=self.chat_history, file_path=archive_file, mode="w")
                self.chat_history = []  # Начать новую историю
                


            # Отправить запрос модели
            response = await self._chat.send_message_async(q)
            if response and response.text:
             
                self.chat_history.append({"role": "user", "parts": [q]})
                self.chat_history.append({"role": "model", "parts": [response.text]})
                await self._save_chat_history(chat_data_folder)
                return response.text
            else:
                logger.error("Empty response in chat", None, False)
                return

        except Exception as ex:
            logger.error(f"Ошибка чата:\n {response=}", ex, False)
            return

        finally:
            if flag == "save_chat":
                await self._save_chat_history(chat_data_folder)

    def ask(self, q: str, attempts: int = 15, save_history:bool = False, clean_response:bool = True) -> Optional[str]:
        """
        Метод отправляет текстовый запрос модели и возвращает ответ.
        """
        for attempt in range(attempts):
            try:
                response = self.model.generate_content(q)
               
                if not response.text:
                    logger.debug(
                        f"No response from the model. Attempt: {attempt}\nSleeping for {2 ** attempt}",
                        None,
                        False
                    )
                    time.sleep(2**attempt)
                    continue  # Повторить попытку

                if save_history:
                    self._save_dialogue([
                        {"role": "user", "content": q},
                        {"role": "model", "content": response.text},
                    ])

                return self.normalize_answer(response.text) if clean_response else response.text 

            except requests.exceptions.RequestException as ex:
                max_attempts = 5
                if attempt > max_attempts:
                    break
                logger.debug(
                    f"Network error. Attempt: {attempt}\nSleeping for {timeout/60} min on {gs.now}",
                    ex,
                    False,
                )
                time.sleep(1200)
                continue  # Повторить попытку
            except (GatewayTimeout, ServiceUnavailable) as ex:
                logger.error("Service unavailable:", ex, False)
                # Экспоненциальный бэк-офф для повторных попыток
                max_attempts = 3
                if attempt > max_attempts:
                    break
                time.sleep(2**attempt + 10)
                continue
            except ResourceExhausted as ex:
                timeout = 14400
                logger.debug(
                    f"Quota exceeded. Attempt: {attempt}\nSleeping for {timeout/60} min on {gs.now}",
                    ex,
                    False,
                )
                time.sleep(timeout)
                continue
            except (DefaultCredentialsError, RefreshError) as ex:
                logger.error("Authentication error:", ex, False)
                return  # Прекратить попытки, если ошибка аутентификации
            except (ValueError, TypeError) as ex:
                max_attempts = 3
                if attempt > max_attempts:
                    break
                timeout = 5
                logger.error(
                    f"Invalid input: Attempt: {attempt}\nSleeping for {timeout/60} min on {gs.now}",
                    ex,
                    None,
                )
                time.sleep(timeout)
                continue
            except (InvalidArgument, RpcError) as ex:
                logger.error("API error:", ex, False)
                return
            except Exception as ex:
                logger.error("Unexpected error:", ex, False)
                return

        return

    async def ask_async(self, q: str, attempts: int = 15, save_history: bool = False, clean_response:bool = True) -> Optional[str]:
        """
        Метод асинхронно отправляет текстовый запрос модели и возвращает ответ.
        """
        for attempt in range(attempts):
            try:
                # response = self.model.generate_content(q)  # Synchronous call
                response = await asyncio.to_thread(self.model.generate_content, q)  # Make it async

                if not response.text:
                    logger.debug(
                        f"No response from the model. Attempt: {attempt}\nSleeping for {2 ** attempt}",
                        None,
                        False
                    )
                    await asyncio.sleep(2 ** attempt)  # Use asyncio.sleep
                    continue  # Повторить попытку


                if save_history:
                    self._save_dialogue([
                        {"role": "user", "content": q},
                        {"role": "model", "content": response.text},
                    ])

                return response.text if clean_response else self.normalize_answer(response.text)

            except requests.exceptions.RequestException as ex:
                max_attempts = 5
                if attempt > max_attempts:
                    break
                timeout:int = 1200
                logger.debug(
                    f"Network error. Attempt: {attempt}\nSleeping for {timeout/60} min on {gs.now}",
                    ex,
                    False,
                )
                await asyncio.sleep(timeout)  # Use asyncio.sleep
                continue  # Повторить попытку
            except (GatewayTimeout, ServiceUnavailable) as ex:
                logger.error("Service unavailable:", ex, False)
                # Экспоненциальный бэк-офф для повторных попыток
                max_attempts = 3
                if attempt > max_attempts:
                    break
                await asyncio.sleep(2 ** attempt + 10)  # Use asyncio.sleep
                continue
            except ResourceExhausted as ex:
                timeout:int = 14440
                logger.debug(
                    f"Quota exceeded. Attempt: {attempt}\nSleeping for {timeout/60} min on {gs.now}",
                    ex,
                    False,
                )
                await asyncio.sleep(timeout)  # Use asyncio.sleep
                continue
            except (DefaultCredentialsError, RefreshError) as ex:
                logger.error("Authentication error:", ex, False)
                return  # Прекратить попытки, если ошибка аутентификации
            except (ValueError, TypeError) as ex:
                max_attempts = 3
                if attempt > max_attempts:
                    break
                timeout = 5
                logger.error(
                    f"Invalid input: Attempt: {attempt}\nSleeping for {timeout/60} min on {gs.now}",
                    ex,
                    None,
                )
                await asyncio.sleep(timeout)  # Use asyncio.sleep
                continue
            except (InvalidArgument, RpcError) as ex:
                logger.error("API error:", ex, False)
                return
            except Exception as ex:
                logger.error("Unexpected error:", ex, False)
                return

        return

    def describe_image(
        self, image: Path | bytes, mime_type: Optional[str] = 'image/jpeg', prompt: Optional[str] = ''
    ) -> Optional[str]:
        """
        Отправляет изображение в Gemini Pro Vision и возвращает его текстовое описание.

        Args:
            image: Путь к файлу изображения или байты изображения

        Returns:
            str: Текстовое описание изображения.
            None: Если произошла ошибка.
        """
        try:
            # Подготовка контента для запроса
            if isinstance(image, Path):
                image = get_image_bytes(image)

            content = \
                [
                    {
                        "role": "user",
                        "parts": {
                            "inlineData": [
                                {
                                    "mimeType": mime_type,
                                    "data": image,
                                }
                            ]
                        }
                    }
                ]


            # Отправка запроса и получение ответа
            try:
                start_time = time.time()
                response = self.model.generate_content(
                    str(
                        {
                            'text': prompt,
                            'data': image
                        }
                    ))

            except DefaultCredentialsError as ex:
                logger.error(f"Ошибка аутентификации: ", print(ex))
                return 

            except (InvalidArgument, RpcError) as ex:
                logger.error("API error:", ex, False)
                return
            except RetryError as ex:
                logger.error(f"Модель перегружена. Подожди час - другой: ", ex)
                return 
            except Exception as ex:
                logger.error(f"Ошибка при отправке запроса модели: ", ex)
                return 
            finally:
                print(f'\nΔ = {time.time() - start_time }\n',text_color='yellow',bg_color='red')


            _t:str | None = response.text 
            if _t:
                return _t
            else:
                print(f"{{Модель вернула:{response}}}",text_color='cyan')
                return None

        except Exception as ex:
            logger.error(f"Произошла ошибка: ", ex)
            ...
            return None

    async def upload_file(
        self, file: str | Path | IOBase, file_name: Optional[str] = None
    ) -> bool:
        """
        https://github.com/google-gemini/generative-ai-python/blob/main/docs/api/google/generativeai/upload_file.md
        response (file_types.File)
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
            logger.debug(f"Файл {file_name} записан", None, False)
            return response
        except Exception as ex:
            logger.error(f"Ошибка записи файла {file_name=}", ex, False)
            try:
                response = await genai.delete_file_async(file_name)
                logger.debug(f"Файл {file_name} удален", None, False)
                await self.upload_file(file, file_name)
            except Exception as ex:
                logger.error(f"Общая ошибка модели: ", ex, False)
                ...
                return


async def main():
    # Замените на свой ключ API

    system_instruction = "Ты - полезный ассистент. Отвечай на все вопросы кратко"
    ai = GoogleGenerativeAI(api_key=gs.credentials.gemini.api_key, system_instruction=system_instruction)

    # Пример вызова describe_image с промптом
    image_path = Path(r"test.jpg")  # Замените на путь к вашему изображению

    if not image_path.is_file():
        print(
            f"Файл {image_path} не существует. Поместите в корневую папку с программой файл с названием test.jpg"
        )
    else:
        prompt = """Проанализируй это изображение. Выдай ответ в формате JSON,
        где ключом будет имя объекта, а значением его описание.
         Если есть люди, опиши их действия."""

        description = await ai.describe_image(image_path, prompt=prompt)
        if description:
            print("Описание изображения (с JSON форматом):")
            print(description)
            try:
                parsed_description = j_loads(description)

            except Exception as ex:
                print("Не удалось распарсить JSON. Получен текст:")
                print(description)

        else:
            print("Не удалось получить описание изображения.")

        # Пример без JSON вывода
        prompt = "Проанализируй это изображение. Перечисли все объекты, которые ты можешь распознать."
        description = await ai.describe_image(image_path, prompt=prompt)
        if description:
            print("Описание изображения (без JSON формата):")
            print(description)

    file_path = Path('test.txt')
    with open(file_path, "w") as f:
        f.write("Hello, Gemini!")

    file_upload = await ai.upload_file(file_path, 'test_file.txt')
    print(file_upload)

    # Пример чата
    while True:
        user_message = input("You: ")
        if user_message.lower() == 'exit':
            break
        ai_message = await ai.chat(user_message)
        if ai_message:
            print(f"Gemini: {ai_message}")
        else:
            print("Gemini: Ошибка получения ответа")


if __name__ == "__main__":
    asyncio.run(main())