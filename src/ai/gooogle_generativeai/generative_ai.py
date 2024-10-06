""" Google generative ai """
## \file ../src/ai/gooogle_generativeai/generative_ai.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python

import header  
import time
import base64
from typing import Optional, List, Dict
from pathlib import Path
import os
import pathlib
import textwrap
import google.generativeai as genai

from src.logger import logger
from src import gs
from src.utils import pprint
from src.utils.csv import save_csv_file
from src.utils.jjson import j_dumps  


class GoogleGenerativeAI:
    """GoogleGenerativeAI class for interacting with Google's Generative AI models."""

    model: genai.GenerativeModel
    dialogue_log_path: str | Path = gs.path.data / 'AI' / f"gemini_{gs.now}.json"
    dialogue: List[Dict[str, str]] = []  # Список для хранения диалога
    system_instruction:str

    def __init__(self, system_instruction: Optional[str] = None, generation_config: dict = {"response_mime_type": "application/json"}):
        """Initialize GoogleGenerativeAI with the model and API key.

        Args:
            system_instruction (Optional[str], optional): Optional system instruction for the model.
            generation_config (dict): "response_mime_type": "text/html" | "text/plain" | "application/json" 
            "response_mime_type": 
        """
        genai.configure(api_key=gs.credentials.googleai.api_key)
        self.system_instruction = system_instruction
        # Using `response_mime_type` requires either a Gemini 1.5 Pro or 1.5 Flash model
        models = ["gemini-1.5-flash-8b-exp-0924","gemini-1.5-flash"]
        self.model = genai.GenerativeModel(
            models[0],
            generation_config = generation_config,
            system_instruction = system_instruction if system_instruction else None
        )

    def _save_dialogue(self):
        """Save the entire dialogue to a CSV file."""
        j_dumps(self.dialogue, self.dialogue_log_path)

    def ask(self, prompt: str, system_instruction: Optional[str] = None, attempts: int = 3, total_wait_time: int = 0) -> Optional[str]:
        """Send a prompt to the model and return the response.

        Args:
            prompt (str): The prompt to send to the model.
            system_instruction (Optional[str], optional): Instruction for system role. Defaults to None.
            attempts (int, optional): Number of retry attempts in case of failure. Defaults to 3.
            total_wait_time (int, optional): The total time spent waiting between attempts. Defaults to 0.

        Returns:
            Optional[str]: The model's response or None if an error occurs.
        """
        try:
            # Send prompt to the model
            response = self.model.generate_content(prompt)
            reply = response.text

            # Add user prompt and model reply to the dialogue
            if system_instruction:
                self.dialogue.append({"role": "system", "content": system_instruction})

            self.dialogue.append({"role": "user", "content": prompt})
            self.dialogue.append({"role": "assistant", "content": reply})

            # Save the dialogue to a CSV file
            self._save_dialogue()

            return reply
        except Exception as ex:
            wait_time = 15  # Time to sleep in case of an error
            total_wait_time += wait_time
            logger.error(f"Error occurred. Waiting for {wait_time} seconds. Total wait time so far: {total_wait_time} seconds", ex, False)
            time.sleep(wait_time)

            if attempts > 0:
                return self.ask(prompt, system_instruction, attempts - 1, total_wait_time)
            else:
                logger.debug(f"Max attempts have been exceeded. Total wait time: {total_wait_time} seconds", None, False)
                attempts = 3
                return self.ask(prompt, system_instruction, attempts, total_wait_time)


    def describe_image(self, image_path: str, prompt: str = None) -> Optional[str]:
        """Описывает изображение с помощью модели генерации текста.

        Args:
            image_path (str): Путь к файлу изображения.
            prompt (str, optional): Дополнительный промпт для модели.

        Returns:
            Optional[str]: Описание изображения или None в случае ошибки.
        """
        ##################################################################################
        #
        #
        # Модель не определяет фото!
        # 
        # 
        # # Проверка поддержки модели для работы с изображениями
        # if self.model.generation_config.get("response_mime_type") != "application/json":
        #     logger.error("Текущая модель не поддерживает работу с изображениями.")
        #     return None

        # Кодирование изображения в формат base64
        with open(image_path, 'rb') as f:
            image_data = f.read()
        encoded_image = base64.b64encode(image_data).decode('utf-8')

        request = encoded_image

        try:
            # Отправка запроса к модели
            response = self.model.generate_content(request)
            return response.text
        except Exception as e:
            logger.error(f"Ошибка при описании изображения: {e}")
            return 