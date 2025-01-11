### Анализ кода модуля `src.ai.gemini`

**Качество кода**:
- **Соответствие стандартам**: 7
- **Плюсы**:
    - Хорошее описание функциональности модуля и основных методов.
    - Понятная структура документации, включая примеры использования.
    - Подробное описание обработки ошибок.
    - Указаны необходимые зависимости.
- **Минусы**:
    - Отсутствуют RST-комментарии в коде.
    - Не используются `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Присутствуют неоднозначные формулировки в комментариях.
    - Не все импорты соответствуют рекомендациям.
    - Не хватает более подробных примеров для каждой функции, включая обработку ошибок.

**Рекомендации по улучшению**:
    - Необходимо добавить RST-документацию для всех функций, методов и классов.
    - Заменить все использования `json.load` на `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Переформулировать комментарии, убрав неясные выражения, такие как "получаем", "делаем", и заменить их на более точные, например, "проверяем", "отправляем", "выполняем".
    - Использовать `from src.logger.logger import logger` для импорта логгера.
    - Добавить больше примеров использования каждой функции, включая примеры с обработкой ошибок.
    - Привести импорты в соответствие с ранее обработанными файлами.
    - Привести код к стандартам PEP8.

**Оптимизированный код**:

```python
"""
Модуль для интеграции с Google Generative AI
==========================================

Этот модуль предоставляет класс :class:`GoogleGenerativeAI` для взаимодействия с моделями Google Generative AI.
Он включает в себя методы для отправки запросов, обработки ответов, управления диалогами и интеграции с различными функциональностями ИИ.

Пример использования
--------------------
.. code-block:: python

    from src.ai.gemini.generative_ai import GoogleGenerativeAI

    ai = GoogleGenerativeAI(api_key='your_api_key', system_instruction='Instruction')
    response = ai.ask('Как дела?')
    print(response)
"""
from pathlib import Path
from typing import IO, Optional, Dict, List
import time
import json
import base64
from io import IOBase

import google.generativeai as genai  # type: ignore
from requests import Response  # type: ignore
from google.api_core.exceptions import GoogleAPIError  # type: ignore
from google.auth.exceptions import GoogleAuthError  # type: ignore

from src.logger import logger  # type: ignore # Import logger from src.logger
from src.utils.printer import print_error, print_info  # type: ignore
from src.utils.file import save_text_file, check_file_exist  # type: ignore
from src.utils.date_time import get_current_time  # type: ignore
from src.utils.convertors.unicode import normalize_text  # type: ignore
from src.utils.jjson import j_loads  # type: ignore
from src.settings import gs  # type: ignore


class GoogleGenerativeAI:
    """
    Класс для взаимодействия с моделями Google Generative AI.

    :param api_key: API-ключ Google Generative AI.
    :type api_key: str
    :param model_name: Имя модели Google Generative AI. По умолчанию 'gemini-pro'.
    :type model_name: Optional[str], optional
    :param generation_config: Конфигурация генерации.
    :type generation_config: Optional[Dict], optional
    :param system_instruction: Системная инструкция для модели.
    :type system_instruction: Optional[str], optional
    :raises Exception: Если не удалось инициализировать модель Google Generative AI.
    """

    def __init__(
        self,
        api_key: str,
        model_name: Optional[str] = None,
        generation_config: Optional[Dict] = None,
        system_instruction: Optional[str] = None,
        **kwargs,
    ):
        self.api_key = api_key
        self.model_name = model_name if model_name else "gemini-pro" # Set default model name
        self.generation_config = generation_config if generation_config else {} # Set default config
        self.system_instruction = system_instruction # System instruction for model

        self.dialogues_path = gs.path.src / "ai" / "gemini" / "dialogues" # Path to save dialogues
        self.history_path = self.dialogues_path / "history.json" # Path to save history
        self.dialogue_text_path = self.dialogues_path / "history.txt" # Path to save history in text format

        try: # Try to initialize the model
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel(self.model_name) # Initialize model
            if self.system_instruction:
                self.chat = self.model.start_chat(
                    history=[
                        {
                            "role": "user",
                            "parts": [self.system_instruction],
                        },
                    ]
                )
            else:
                self.chat = self.model.start_chat()
            
            print_info("Google Generative AI model initialized")
        except Exception as e:
            logger.error(f"Error initializing Google Generative AI model: {e}")
            raise Exception(f"Error initializing Google Generative AI model: {e}") # Raise an exception


    def config(self) -> Dict:
        """
        Получает конфигурацию из файла настроек.

        :return: Словарь с конфигурацией.
        :rtype: Dict
        :raises Exception: Если не удалось загрузить или прочитать файл конфигурации.
        """
        try:
            config_path = gs.path.src / "ai" / "gemini" / "generative_ai.json" # Path to config file
            with open(config_path, "r", encoding="utf-8") as f:
                return j_loads(f.read()) # Load config from json file
        except Exception as e:
            logger.error(f"Error loading Gemini config: {e}")
            raise Exception(f"Error loading Gemini config: {e}") # Raise an exception

    def _start_chat(self):
        """
        Запускает сессию чата с моделью ИИ.

        :raises Exception: Если не удалось запустить сессию чата.
        """
        try:
            self.chat = self.model.start_chat() # Start a new chat session
            print_info("New chat session started")
        except Exception as e:
            logger.error(f"Error starting chat session: {e}") # Log error
            raise Exception(f"Error starting chat session: {e}") # Raise an exception

    async def _save_dialogue(self, dialogue: list):
        """
        Асинхронно сохраняет диалог в текстовый и JSON файлы.

        :param dialogue: Список сообщений диалога.
        :type dialogue: list
        :raises Exception: Если не удалось сохранить диалог.
        """
        try:
            if not self.dialogues_path.exists():
                self.dialogues_path.mkdir(parents=True) # Create directory if not exists

            if not check_file_exist(self.history_path):
                await save_text_file(self.history_path, "[]") # Create json file if not exists
            if not check_file_exist(self.dialogue_text_path):
                await save_text_file(self.dialogue_text_path, "") # Create text file if not exists

            text_data = "" # Initialize text data
            json_data = j_loads(await self.history_path.read_text(encoding="utf-8")) # Load json data from file
            
            for item in dialogue:
                if item.get("parts"): # If message has parts
                    text_data += f"{item.get('role')}: {item.get('parts')[0]}\n" # Add message to text data
                    json_data.append(item) # Add message to json data
                else:
                    text_data += f"{item.get('role')}: {item.get('content')}\n" # Add message to text data
                    json_data.append(item) # Add message to json data

            await save_text_file(self.dialogue_text_path, text_data, mode="a") # Save text data to file
            await save_text_file(self.history_path, json.dumps(json_data, indent=4), mode='w') # Save json data to file
            print_info("Dialogue saved successfully") # Log success

        except Exception as e:
            logger.error(f"Error saving dialogue: {e}")
            raise Exception(f"Error saving dialogue: {e}") # Raise an exception

    def ask(self, q: str, attempts: int = 15) -> Optional[str]:
        """
        Отправляет текстовый запрос модели ИИ и получает ответ.

        :param q: Текстовый запрос.
        :type q: str
        :param attempts: Количество попыток в случае ошибки. По умолчанию 15.
        :type attempts: int, optional
        :return: Текст ответа от модели ИИ или None в случае ошибки.
        :rtype: Optional[str]
        :raises Exception: Если все попытки исчерпаны и не удалось получить ответ.
        """
        attempt = 0
        delay = 1
        while attempt < attempts:
            try:
                response = self.model.generate_content(q)
                if response.text:
                    dialogue = [{"role": "user", "parts": [q]}, {"role": "model", "parts": [response.text]}] # Create dialogue
                    self._save_dialogue(dialogue) # Save dialogue
                    return response.text # Return response
                else:
                    logger.error("Empty response from model") # Log error
                    attempt += 1
                    time.sleep(delay)
                    delay *= 2
            except GoogleAPIError as e:
                logger.error(f"Google API Error during ask attempt {attempt + 1}: {e}") # Log error
                attempt += 1
                time.sleep(delay)
                delay *= 2
            except Exception as e:
                 logger.error(f"Unexpected error during ask attempt {attempt + 1}: {e}") # Log error
                 attempt += 1
                 time.sleep(delay)
                 delay *= 2

        logger.error(f"Failed to get a response after {attempts} attempts.") # Log error
        return None

    def chat(self, q: str) -> Optional[str]:
        """
        Отправляет сообщение чата модели ИИ и получает ответ.

        :param q: Текстовый запрос для чата.
        :type q: str
        :return: Текст ответа от модели ИИ или None в случае ошибки.
        :rtype: Optional[str]
        :raises Exception: Если не удалось получить ответ от модели.
        """
        try:
            response = self.chat.send_message(q) # Send message to chat
            if response.text:
                dialogue = [{"role": "user", "parts": [q]}, {"role": "model", "parts": [response.text]}] # Create dialogue
                self._save_dialogue(dialogue) # Save dialogue
                return response.text # Return response
            else:
                logger.error("Empty response from chat model") # Log error
                return None
        except Exception as e:
            logger.error(f"Error during chat: {e}") # Log error
            return None

    def describe_image(self, image_path: Path) -> Optional[str]:
        """
        Генерирует текстовое описание изображения.

        :param image_path: Путь к файлу изображения.
        :type image_path: Path
        :return: Текстовое описание изображения или None в случае ошибки.
        :rtype: Optional[str]
        :raises Exception: Если не удалось описать изображение.
        """
        try:
            with open(image_path, "rb") as f:
                image_data = f.read() # Read image data
            base64_image = base64.b64encode(image_data).decode("utf-8") # Encode image to base64
            
            response = self.model.generate_content(
                [
                    {
                        "mime_type": "image/jpeg",
                        "data": base64_image,
                    },
                    "Опиши изображение",
                ]
            ) # Send request to model
            if response.text:
                dialogue = [{"role": "user", "parts": [f"Image: {image_path}" ]}, {"role": "model", "parts": [response.text]}] # Create dialogue
                self._save_dialogue(dialogue) # Save dialogue
                return response.text # Return response
            else:
                logger.error("Empty response from image model") # Log error
                return None

        except Exception as e:
            logger.error(f"Error describing image: {e}") # Log error
            return None

    def upload_file(self, file: str | Path | IOBase, file_name: Optional[str] = None) -> bool:
        """
        Загружает файл в модель ИИ.

        :param file: Путь к файлу или открытый файловый объект.
        :type file: str | Path | IOBase
        :param file_name: Имя файла.
        :type file_name: Optional[str], optional
        :return: True, если файл успешно загружен, иначе False.
        :rtype: bool
        :raises Exception: Если не удалось загрузить файл.
        """
        try:
            if isinstance(file, (str, Path)):
                with open(file, "rb") as f:
                    file_data = f.read() # Read file data
                    file_name = file_name if file_name else Path(file).name
            elif isinstance(file, IOBase):
                file_data = file.read() # Read file data
                file_name = file_name if file_name else "uploaded_file"
            else:
                logger.error("Invalid file format")
                return False
                
            base64_file = base64.b64encode(file_data).decode("utf-8") # Encode file data to base64
            response = self.model.generate_content(
                [
                    {
                        "mime_type": "text/plain",
                        "data": base64_file,
                    },
                    f"Проанализируй файл {file_name}",
                ]
            ) # Send request to model

            if response.text:
                dialogue = [{"role": "user", "parts": [f"File: {file_name}" ]}, {"role": "model", "parts": [response.text]}] # Create dialogue
                self._save_dialogue(dialogue) # Save dialogue
                print_info("File uploaded and processed") # Log success
                return True
            else:
                logger.error("Empty response from file model") # Log error
                return False
        except Exception as e:
            logger.error(f"Error uploading file: {e}") # Log error
            return False