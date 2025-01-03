# -*- coding: utf-8 -*-

"""
.. module::  src.ai.gemini
   :platform: Windows, Unix
   :synopsis: Google generative AI integration
   https://github.com/google-gemini/generative-ai-python/blob/main/docs/api/google/generativeai.md
"""

import asyncio
import time
from pathlib import Path
from typing import Optional, Dict, Union, IO

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
from src.utils.printer import pprint
from src.utils.file import save_text_file
from src.utils.jjson import j_loads, j_dumps
from src.utils.image import get_image_bytes
from src.utils.date_time import TimeoutCheck


class GoogleGenerativeAI:
    """Класс для взаимодействия с моделями Google Generative AI."""

    MODELS = [
        "gemini-1.5-flash-8b",
        "gemini-2-13b",
        "gemini-3-20b",
        "gemini-2.0-flash-exp",
    ]

    def __init__(
        self,
        api_key: str,
        model_name: Optional[str] = None,
        generation_config: Optional[Dict] = None,
        system_instruction: Optional[str] = None,
    ):
        """Инициализация модели GoogleGenerativeAI с дополнительными настройками."""
        self.api_key = api_key
        self.model_name = model_name or "gemini-2.0-flash-exp"
        self.generation_config = generation_config or {"response_mime_type": "text/plain"}
        self.system_instruction = system_instruction

        self.dialogue_log_path = gs.path.external_storage / "AI" / "log"
        self.history_dir = gs.path.external_storage / "AI" / "history"
        
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(
            model_name=self.model_name, generation_config=self.generation_config
        )
        self._chat = None
        self.chat_history = []

    def _initialize_chat(self):
        """Создает новый чат только если он еще не существует."""
        if self._chat is None:
            history = []
            if self.system_instruction:
                history.append({"role": "user", "parts": [self.system_instruction]})
            self._chat = self.model.start_chat(history=history)

    def _save_dialogue(self, dialogue: list):
        """Сохраняет диалог в текстовый и JSON файл."""
        timestamp = gs.now
        txt_path = self.history_dir / f"gemini_{timestamp}.txt"
        json_path = self.history_dir / f"gemini_{timestamp}.json"

        save_text_file(dialogue, txt_path, mode="a")
        j_dumps(data=dialogue, file_path=json_path, mode="a")

    async def ask(self, q: str, attempts: int = 3) -> Optional[str]:
        """
        Отправляет текстовый запрос модели и возвращает ответ.

        Args:
            q (str): Вопрос для модели.
            attempts (int): Количество попыток при ошибках.

        Returns:
            Optional[str]: Ответ модели или None в случае ошибки.
        """
        for attempt in range(1, attempts + 1):
            try:
                response = await self.model.generate_content_async(q)
                
                if response.text:
                    self.chat_history.append({"role": "user", "content": q})
                    self.chat_history.append({"role": "assistant", "content": response.text})
                    return response.text
                else:
                    logger.warning(f"Attempt {attempt}: Empty response from model.")
            except (GatewayTimeout, ServiceUnavailable, ResourceExhausted) as ex:
                logger.warning(f"Attempt {attempt}: Service error: {ex}")
                await asyncio.sleep(2 ** attempt)
            except (DefaultCredentialsError, RefreshError, InvalidArgument, RpcError) as ex:
                logger.error(f"Critical error: {ex}")
                break
            except Exception as ex:
                logger.error(f"Unexpected error: {ex}")
                break
        return None

    async def describe_image(self, image_path: Path, prompt: Optional[str] = None) -> Optional[str]:
        """
        Отправляет изображение в модель и получает описание.

        Args:
            image_path (Path): Путь к изображению.
            prompt (Optional[str]): Дополнительный текстовый запрос.

        Returns:
            Optional[str]: Текстовое описание изображения или None.
        """
        try:
            contents = [
                {"mime_type": "image/jpeg", "data": get_image_bytes(image_path)},
                prompt or "Опишите это изображение."
            ]
            response = await self.model.generate_content_async(contents)
            return response.text if response.text else None
        except Exception as ex:
            logger.error(f"Error describing image: {ex}")
            return None

    async def upload_file(self, file: Union[Path, IO], file_name: Optional[str] = None) -> bool:
        """
        Загружает файл в модель.

        Args:
            file (Union[Path, IO]): Файл для загрузки.
            file_name (Optional[str]): Имя файла.

        Returns:
            bool: Успешно ли загружен файл.
        """
        try:
            response = await genai.upload_file_async(
                path=file, mime_type=None, name=file_name, display_name=file_name, resumable=True
            )
            logger.info(f"File uploaded: {file_name}")
            return True
        except Exception as ex:
            logger.error(f"Error uploading file: {ex}")
            return False


async def main():
    """Главная функция для демонстрации работы."""
    api_key = iinput( "YOUR_API_KEY")
    system_instruction = "Ты - полезный ассистент. Отвечай на вопросы кратко."
    ai = GoogleGenerativeAI(api_key=api_key, system_instruction=system_instruction)

    while True:
        user_message = input("You: ")
        if user_message.lower() == "exit":
            break
        ai_response = await ai.ask(user_message)
        if ai_response:
            print(f"Gemini: {ai_response}")
        else:
            print("Gemini: Ошибка получения ответа.")

if __name__ == "__main__":
    asyncio.run(main())
