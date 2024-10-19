## \file ../src/ai/gemini/generative_ai.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
""" Google generative ai """
from types import SimpleNamespace
import header  
import time
import base64
import argparse
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
from src.utils.file import read_text_file, save_text_file, recursive_read_text_files
from src.utils.date_time import TimeoutCheck

timeout_check = TimeoutCheck()

class GoogleGenerativeAI:
    """GoogleGenerativeAI class for interacting with Google's Generative AI models."""

    model: genai.GenerativeModel
    dialogue_log_path: str | Path = gs.path.data / 'AI' / f"gemini_{gs.now}.json"
    dialogue_txt_path: str | Path = gs.path.data / 'AI' / f"gemini_{gs.now}.txt"
    system_instruction:str

    def __init__(self, api_key:str, system_instruction: Optional[str] = None,  generation_config: dict = {"response_mime_type": "application/json"}):
        """Initialize GoogleGenerativeAI with the model and API key.

        Args:
            system_instruction (Optional[str], optional): Optional system instruction for the model.
            generation_config (dict): "response_mime_type": "text/html" | "text/plain" | "application/json" 
            "response_mime_type": 
        """
        genai.configure(api_key = api_key)
        #genai.configure(api_key=gs.credentials.googleai.api_key)
        self.system_instruction = system_instruction
        # Using `response_mime_type` requires either a Gemini 1.5 Pro or 1.5 Flash model
        models = [
                    "gemini-1.5-flash-8b-exp-0924",
                    "gemini-1.5-flash",
                    "gemini-1.5-flash-8b",
                  ]
        self.model = genai.GenerativeModel(
            models[2],
            generation_config = generation_config,
            system_instruction = system_instruction if system_instruction else None
        )
        
    def _save_dialogue(self, dialogue):
        """Save the entire dialogue to a CSV file."""
        #j_dumps(dialogue, self.dialogue_log_path)
        save_text_file(dialogue, self.dialogue_txt_path, mode = '+a')

    def ask(self, q: str, system_instruction: Optional[str] = None, attempts: int = 3, total_wait_time: int = 0, no_log:bool = False, with_pretrain:bool = False) -> Optional[str]:
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
            if with_pretrain:
                train_data_list:list = recursive_read_text_files(gs.path.data / 'AI', ['*.txt'], exc_info=False)
                if train_data_list:
                    i:int = 0
                    for train_data in train_data_list:
                        i += 1
                        print(f"pretrain {i} from {len(train_data_list)}")
                        print(f"Q:> {train_data}")
                        response = self.model.generate_content(train_data)  # Генерация ответа модели
                        print(f"A:> {response.text}")

                        # # Ожидаем ввод с тайм-аутом 5 секунд
                        # print("U: Waiting for input... (timeout in 5 seconds) >")
                        # u = timeout_check.input_with_timeout(timeout=5)
    
                        # if u:
                        #     response = self.model.generate_content(u)
                        #     print(f"A:> {response.text}")
                        # else:
                        #     print("Timeout occurred, no input provided.")

                        # print("Continuing execution after timeout.")
                        time.sleep(8)

            ...
            content:dict = {
               "messages":[{"role": "user", "content": q},
                           {"role": "system", "content": system_instruction} if system_instruction else None] ,
                "model": "gemini-1.5-flash-8b",
                "temperature": 0.7
            }

            messages = [{"role": "user", "content": q},
                           {"role": "system", "content": system_instruction} if system_instruction else None]

            try:
                response = self.model.generate_content(str(messages))
            except Exception as ex:
                logger.debug("Ошибка ответа от модели\n", ex, True)
                ...
                return
            if not response:
                logger.debug("Не получил ответ от модели", None, True)
                ...
                return
            if not no_log:
                self._save_dialogue([{"role": "system", "content": system_instruction} if system_instruction else None,
                                    {"role": "user", "content": q},
                                    {"role": "assistant", "content": response }]
                                    )

            return response.text

        except Exception as ex:
            wait_time = 15  # Time to sleep in case of an error
            total_wait_time += wait_time
            logger.error(f"Error occurred", ex, False)
            #time.sleep(wait_time)

            if attempts > 0:
                return self.ask(q, system_instruction, attempts - 1, total_wait_time)
            else:
                logger.debug(f"Max attempts have been exceeded. Total wait time: {total_wait_time} seconds", None, False)
                attempts = 3
                return self.ask(q, system_instruction, attempts, total_wait_time)


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



def chat():
    logger.debug("Привет, я ИИ ассистент компьюрного мастера Сергея Казаринова. Задавайте вопросы", None, False)
    print("Чтобы завершить чат, напишите 'exit'.\n")
    
    # Инициализация модели с системной инструкцией, если нужно
    system_instruction = input("Введите системную инструкцию (или нажмите Enter, чтобы пропустить): @TODO: - сделать возможность чтения из .txt")
    ...
    ai = GoogleGenerativeAI(system_instruction=system_instruction if system_instruction else None)

    while True:
        # Получаем вопрос от пользователя
        user_input = input("> вопрос\n> ")
        
        if user_input.lower() == 'exit':
            print("Чат завершен.")
            break
        
        # Отправляем запрос модели и получаем ответ
        response = ai.ask(prompt=user_input)
        
        # Выводим ответ
        print(f">> ответ\n>> {response}\n")

if __name__ == "__main__":
    chat()
