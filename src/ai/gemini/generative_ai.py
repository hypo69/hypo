# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module::  src.ai.gemini
   :platform: Windows, Unix
   :synopsis: Google generative AI integration
   https://github.com/google-gemini/generative-ai-python/blob/main/docs/api/google/generativeai.md
"""

import asyncio
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
from src.utils.image import get_image_bytes

timeout_check = TimeoutCheck()


class GoogleGenerativeAI:
    """
    Класс для взаимодействия с моделями Google Generative AI.
    """

    MODELS = [
        "gemini-1.5-flash-8b",
        "gemini-2-13b",
        "gemini-3-20b",
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
        """
        _now = gs.now
        self.api_key = api_key
        self.model_name = model_name or "gemini-1.5-flash-8b"
        self.generation_config = generation_config or {"response_mime_type": "text/plain"}
        self.system_instruction = system_instruction

        self.dialogue_log_path = gs.path.external_storage / "AI" / "log"
        self.dialogue_txt_path = self.dialogue_log_path / f"gemini_{_now}.txt"
        self.history_dir = gs.path.external_storage / "AI" / "history"
        self.history_txt_file = self.history_dir / f"gemini_{_now}.txt"
        self.history_json_file = self.history_dir / f"gemini_{_now}.json"

        # Инициализация модели
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(
            model_name=self.model_name, generation_config=self.generation_config
        )
        self._chat = self._start_chat()
        self.chat_history = []


    @property
    def config(self):
        """Получаю конфигурацию из файла настроек"""
        return j_loads_ns(gs.path.src / "ai" / "gemini" / "generative_ai.json")

    def _start_chat(self):
        """"""
        if self.system_instruction:
             return self.model.start_chat(history=[{"role": "user", "parts": [self.system_instruction]}])
        else:
            return self.model.start_chat(history=[])

    def _save_dialogue(self, dialogue: list):
        """
        Сохранить диалог в текстовый и JSON файл с управлением размером файлов.
        """
        save_text_file(dialogue, self.history_txt_file, mode="+a")
        for message in dialogue:
            j_dumps(data=message, file_path=self.history_json_file, mode="+a")

    async def ask(self, q: str, attempts: int = 15) -> Optional[str]:
        """
        Метод отправляет текстовый запрос модели и возвращает ответ.
        """
        for attempt in range(attempts):
            try:
                response = await self.model.generate_content_async(q)
                #response = response.resolve()

                if not response.text:
                    logger.debug(
                        f"No response from the model. Attempt: {attempt}\nSleeping for {2 ** attempt}"
                    )
                    time.sleep(2**attempt)
                    continue  # Повторить попытку

                messages = [
                    {"role": "user", "content": q},
                    {"role": "assistant", "content": response.text},
                ]

                # self._save_dialogue([messages])
                return response.text

            except requests.exceptions.RequestException as ex:
                timeout = 1200
                max_attempts = 5
                if attempt > max_attempts:
                    break
                logger.debug(
                    f"Network error. Attempt: {attempt}\nSleeping for {timeout/60} min on {gs.now}",
                    ex,
                    None,
                )
                time.sleep(timeout)
                continue  # Повторить попытку
            except (GatewayTimeout, ServiceUnavailable) as ex:
                logger.error("Service unavailable:", ex, None)
                # Экспоненциальный бэк-офф для повторных попыток
                max_attempts = 3
                if attempt > max_attempts:
                    break
                time.sleep(2**attempt)
                continue
            except ResourceExhausted as ex:
                timeout = 10800
                logger.debug(
                    f"Quota exceeded. Attempt: {attempt}\nSleeping for {timeout/60} min on {gs.now}",
                    ex,
                    None,
                )
                time.sleep(timeout)
                continue
            except (DefaultCredentialsError, RefreshError) as ex:
                logger.error("Authentication error:", ex, None)
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
                logger.error("API error:", ex, None)
                return
            except Exception as ex:
                logger.error("Unexpected error:", ex, None)
                return

        return

    async def chat(self, q: str) -> Optional[str]:
        """"""
        response = None
        try:
            response = await self._chat.send_message_async(q)
            response = await response.resolve()
            if response and response.text:
                self.chat_history.append({"role": "user", "parts": [q]})
                self.chat_history.append({"role": "assistant", "parts": [response.text]})
                self._save_dialogue(self.chat_history)
                return response.text
            else:
                logger.error("Empty response in chat", None)
                return
        except Exception as ex:
            logger.error(f"Ошибка чата {response=}", ex)
            return

    async def describe_image(
        self, image_path: Path, prompt: Optional[str] = None
    ) -> Optional[str]:
        """
        Отправляет изображение в Gemini Pro Vision и возвращает его текстовое описание.

        Args:
            image_path: Путь к файлу изображения.

        Returns:
            str: Текстовое описание изображения.
            None: Если произошла ошибка.
        """
        try:
            # Подготовка контента для запроса
            contents = [
                {
                    "mime_type": "image/jpeg",  # Измените на mime-тип вашего изображения
                    "data":  get_image_bytes(image_path),
                },
                prompt if prompt else "Опиши это изображение.",
            ]


            # Отправка запроса и получение ответа
            response = await self.model.generate_content_async(contents)
            #response = response.resolve()

            if response.text:
                return response.text
            else:
                print("Модель вернула пустой ответ.")
                return None

        except Exception as e:
            print(f"Произошла ошибка: {e}")
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
    api_key = "YOUR_API_KEY"
    system_instruction = "Ты - полезный ассистент. Отвечай на все вопросы кратко"
    ai = GoogleGenerativeAI(api_key=api_key, system_instruction=system_instruction)

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
                print("Парсинг json:")
                pprint(parsed_description)

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

    file_upload = await ai.upload_file(file_path,'test_file.txt')
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
