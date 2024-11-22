## \file hypotez/src/ai/gemini/generative_ai.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module:: src.ai.gemini
   :platform: Windows, Unix
   :synopsis: Google generative AI integration
"""

MODE = 'development'
import time
import json
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict
from types import SimpleNamespace
import base64
import google.generativeai as genai
from src.logger import logger
from src import gs
from src.utils import pprint
from src.utils.file import read_text_file, save_text_file
from src.utils.date_time import TimeoutCheck
from src.utils.jjson import j_loads, j_loads_ns, j_dumps

timeout_check = TimeoutCheck()

class GoogleGenerativeAI:
    """
    Класс для взаимодействия с моделями Google Generative AI.

    Этот класс используется для настройки и работы с моделью Google Generative AI, включая отправку запросов,
    получение ответов и сохранение диалогов в текстовых и JSON файлах.

    Атрибуты:
        MODELS (List[str]): Список доступных моделей AI.
        api_key (str): Ключ API для доступа к генеративной модели.
        model_name (str): Название модели для использования.
        generation_config (Dict): Конфигурация для генерации.
        mode (str): Режим работы модели (например, 'debug' или 'production').
        dialogue_log_path (Optional[Path]): Путь для логирования диалогов.
        dialogue_txt_path (Optional[Path]): Путь для сохранения текстовых файлов диалогов.
        history_dir (Path): Директория для хранения истории.
        history_txt_file (Optional[Path]): Путь к файлу для хранения истории в формате текста.
        history_json_file (Optional[Path]): Путь к файлу для хранения истории в формате JSON.
        model (Optional[genai.GenerativeModel]): Объект модели Google Generative AI.
        system_instruction (Optional[str]): Инструкция для системы, которая задает параметры поведения модели.

    Пример использования:
        >>> ai = GoogleGenerativeAI(api_key="your_api_key", system_instruction="Instruction")
        >>> response = ai.ask("Как дела?")
        >>> print(response)
    """

    MODELS = [
        "gemini-1.5-flash-8b",
        "gemini-2-13b",
        "gemini-3-20b"
    ]

    def __init__(self, 
                 api_key: str, 
                 model_name: Optional[str] = None, 
                 generation_config: Optional[Dict] = None, 
                 system_instruction: Optional[str] = None, 
                 **kwargs):
        """
        Инициализация модели GoogleGenerativeAI с дополнительными настройками.

        Этот метод настраивает модель AI, а также определяет пути для логирования и истории.

        Аргументы:
            api_key (str): Ключ API для доступа к генеративной модели.
            model_name (Optional[str], optional): Название модели для использования. По умолчанию "gemini-1.5-flash-8b".
            generation_config (Optional[Dict], optional): Конфигурация для генерации. По умолчанию {"response_mime_type": "text/plain"}.
            system_instruction (Optional[str], optional): Инструкция для системы. По умолчанию None.
        """
        
        self.api_key = api_key
        self.model_name = model_name or "gemini-1.5-flash-8b"
        self.generation_config = generation_config or {"response_mime_type": "text/plain"}
        self.system_instruction = system_instruction

        self.dialogue_log_path = gs.path.google_drive / 'AI' / 'log'
        self.dialogue_txt_path = self.dialogue_log_path / f"gemini_{gs.now}.txt"
        self.history_dir = gs.path.google_drive / 'AI' / 'history'
        self.history_txt_file = self.history_dir / f"gemini_{gs.now}.txt"
        self.history_json_file = self.history_dir / f"gemini_{gs.now}.json"

        # Инициализация модели
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(
            model_name=self.model_name,
            generation_config=self.generation_config
        )

    def __post_init__(self):
        """
        Метод для инициализации модели и других параметров после создания экземпляра.

        Этот метод гарантирует, что модель будет инициализирована, если ключ API указан, но модель еще не была
        настроена в конструкторе.
        """
        if self.api_key and not self.model:
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel(
                model_name=self.model_name,
                generation_config=self.generation_config,
                system_instruction=self.system_instruction,       
            )

    def _save_dialogue(self, dialogue: list):
        """
        Сохранить диалог в текстовый и JSON файл с управлением размером файлов.

        Этот метод сохраняет каждый диалог в текстовом и JSON формате для последующего анализа.

        Аргументы:
            dialogue (list): Список сообщений, представляющих диалог, который нужно сохранить.
        """
        save_text_file(dialogue, self.history_txt_file, mode='+a')
        for message in dialogue:
            j_dumps(data=message, file_path=self.history_json_file, mode='+a')

    def ask(self, q: str, attempts: int = 3) -> Optional[str]:
        """
        Отправить запрос к модели и получить ответ.

        Этот метод отправляет текстовый запрос модели и возвращает ответ.

        Аргументы:
            q (str): Вопрос, который будет отправлен модели.
            attempts (int, optional): Количество попыток для получения ответа. По умолчанию 3.

        Возвращает:
            Optional[str]: Ответ от модели или None, если ответ не был получен.

        Пример:
            >>> ai = GoogleGenerativeAI(api_key="your_api_key")
            >>> response = ai.ask("Какая погода сегодня?")
            >>> print(response)
        """
        
        try:
            
            response = self.model.generate_content(q)

            if not response:
                logger.debug("No response from the model.")
                return None

            messages = [
                {"role": "user", "content": q},
                {"role": "assistant", "content": response.text}
                ]

            self._save_dialogue([messages])
            return response.text

        except Exception as ex:
            logger.error("Error during request", ex, False)
            return None

    def describe_image(self, image_path: Path) -> Optional[str]:
        """
        Генерирует описание изображения.

        Этот метод отправляет изображение в модель для анализа и получает текстовое описание изображения.

        Аргументы:
            image_path (Path): Путь к изображению, которое нужно описать.

        Возвращает:
            Optional[str]: Описание изображения или None, если произошла ошибка.

        Пример:
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
            logger.error(f"Error describing image: {ex}")
            return None


def chat():
    """
    Запускает интерактивную сессию чата.

    Этот метод запускает цикл общения с пользователем, где можно задавать вопросы модели и получать ответы.

    Пример:
        >>> chat()  # Запуск чата
    """
    logger.debug("Hello, I am the AI assistant. Ask your questions.")
    print("Type 'exit' to end the chat.\n")

    system_instruction = input("Enter system instruction (or press Enter to skip): ")
    
    # Передаем значение api_key и system_instruction при инициализации
    ai = GoogleGenerativeAI(api_key="your_api_key", system_instruction=system_instruction or None)

    while True:
        user_input = input("> Question: ")
        if user_input.lower() == 'exit':
            print("Chat ended.")
            break

        response = ai.ask(q=user_input)
        print(f">> Response:\n{response}\n")

if __name__ == "__main__":
    chat()
