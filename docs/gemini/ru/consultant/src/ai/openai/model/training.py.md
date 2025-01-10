## Анализ кода модуля `training.py`

**Качество кода**
7
-  Плюсы
    - Код разбит на функции, что облегчает его понимание и поддержку.
    - Используются аннотации типов, что улучшает читаемость и помогает в отладке.
    - Применяется `logger` для логирования ошибок и информационных сообщений.
    - Есть документация для классов и методов.
-  Минусы
    - Не везде используется `j_loads_ns` и `j_dumps`, где это необходимо.
    - Отсутствуют docstring для некоторых методов.
    - Есть некоторые избыточные блоки `try-except`, которые можно оптимизировать.
    - Жестко заданы значения по умолчанию, например, `assistant_id` в `__init__`.
    - Не везде есть обработка ошибок и вывод конкретных сообщений.
    - В методе `ask` не используется `system_instruction` из параметров метода при добавлении в диалог.

**Рекомендации по улучшению**

1. **Импорты**: Добавить `from src.logger import logger` явно.
2. **Использование `j_loads` и `j_dumps`**: Заменить `json.load` на `j_loads` и `json.dumps` на `j_dumps`.
3. **Комментарии**: Добавить docstring для `describe_image` и `describe_image_by_requests`.
4. **Обработка ошибок**: Оптимизировать `try-except` блоки, заменяя их на логирование через `logger.error`.
5. **Параметры по умолчанию**: Вынести значения по умолчанию в константы.
6. **Логирование**: Добавить больше информативных сообщений в `logger`.
7. **Использование system_instruction**: При добавлении в диалог использовать параметр `system_instruction` переданный в метод `ask`.
8. **Улучшение `describe_image`**: добавить проверку на наличие данных перед тем как обращаться к `response.choices[0].message.content.strip()`
9. **Улучшение `describe_image_by_requests`**: добавить обработку ошибки, когда `response.json()` не может быть декодирован.

**Оптимизированный код**
```python
"""
Модуль для работы с OpenAI API.
=========================================================================================

Этот модуль содержит класс :class:`OpenAIModel`, который используется для взаимодействия с OpenAI API
и управления моделями.

Пример использования
--------------------

Пример использования класса `OpenAIModel`:

.. code-block:: python

    model = OpenAIModel(system_instruction='You are a helpful assistant.')
    response = model.ask('Hello, how are you?')
    print(response)
"""
from __future__ import annotations

# /src/ai/openai/model/training.py
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

import time
from pathlib import Path
from types import SimpleNamespace
from typing import List, Dict, Optional, Any
import pandas as pd
from openai import OpenAI
import requests
from PIL import Image
from io import BytesIO

from src import gs
from src.utils.jjson import j_loads, j_loads_ns, j_dumps
from src.utils.csv import save_csv_file
from src.utils.printer import pprint
from src.utils.convertors.base64 import base64encode
from src.utils.convertors.md import md2dict
from src.logger.logger import logger

DEFAULT_MODEL = "gpt-4o-mini"
DEFAULT_ASSISTANT_ID = gs.credentials.openai.assistant_id.code_assistant
DEFAULT_DIALOGUE_LOG_PATH = gs.path.google_drive / 'AI' / f"{DEFAULT_MODEL}_{gs.now}.json"


class OpenAIModel:
    """
    OpenAI Model Class для взаимодействия с OpenAI API и управления моделью.
    
    Attributes:
        model (str): Название модели OpenAI.
        client (OpenAI): Клиент OpenAI.
        current_job_id (str): Идентификатор текущей работы.
        assistant_id (str): Идентификатор ассистента.
        assistant (Any): Объект ассистента.
        thread (Any): Объект треда.
        system_instruction (str): Системные инструкции для модели.
        dialogue_log_path (str | Path): Путь к файлу журнала диалога.
        dialogue (List[Dict[str, str]]): Список диалогов.
        assistants (List[SimpleNamespace]): Список доступных ассистентов.
        models_list (List[str]): Список доступных моделей.
    """
    model: str = DEFAULT_MODEL
    client: OpenAI
    current_job_id: str
    assistant_id: str
    assistant = None
    thread = None
    system_instruction: str
    dialogue_log_path: str | Path = DEFAULT_DIALOGUE_LOG_PATH
    dialogue: List[Dict[str, str]] = []
    assistants: List[SimpleNamespace]
    models_list: List[str]

    def __init__(self, system_instruction: str = None, model_name: str = DEFAULT_MODEL, assistant_id: str = None):
        """
        Инициализирует объект Model с ключом API, ID ассистента и загружает доступные модели и ассистентов.

        Args:
            system_instruction (str, optional): Системные инструкции для модели.
            model_name (str, optional): Название модели.
            assistant_id (str, optional): Идентификатор ассистента.
        """
        self.client = OpenAI(api_key=gs.credentials.openai.api_key)
        self.current_job_id = None
        self.assistant_id = assistant_id or DEFAULT_ASSISTANT_ID
        self.system_instruction = system_instruction

        try:
            self.assistant = self.client.beta.assistants.retrieve(self.assistant_id)
            self.thread = self.client.beta.threads.create()
            logger.info(f"Assistant {self.assistant_id} and thread created successfully.")
        except Exception as ex:
            logger.error(f"Error initializing assistant or thread: {ex}")

    @property
    def list_models(self) -> List[str]:
        """
        Динамически получает и возвращает доступные модели из OpenAI API.

        Returns:
            List[str]: Список идентификаторов моделей, доступных через OpenAI API.
        """
        try:
            models = self.client.models.list()
            model_list = [model['id'] for model in models['data']]
            logger.info(f"Loaded models: {model_list}")
            return model_list
        except Exception as ex:
            logger.error(f"An error occurred while loading models: {ex}")
            return []

    @property
    def list_assistants(self) -> List[str]:
        """
        Динамически загружает доступных ассистентов из JSON файла.

        Returns:
            List[str]: Список имен ассистентов.
        """
        try:
            self.assistants = j_loads_ns(gs.path.src / 'ai' / 'openai' / 'model' / 'assistants' / 'assistants.json')
            assistant_list = [assistant.name for assistant in self.assistants]
            logger.info(f"Loaded assistants: {assistant_list}")
            return assistant_list
        except Exception as ex:
            logger.error(f"An error occurred while loading assistants: {ex}")
            return []

    def set_assistant(self, assistant_id: str):
        """
        Устанавливает ассистента, используя предоставленный ID ассистента.

        Args:
            assistant_id (str): ID ассистента для установки.
        """
        try:
            self.assistant_id = assistant_id
            self.assistant = self.client.beta.assistants.retrieve(assistant_id)
            logger.info(f"Assistant set successfully: {assistant_id}")
        except Exception as ex:
            logger.error(f"An error occurred while setting the assistant: {ex}")

    def _save_dialogue(self):
        """Сохраняет весь диалог в JSON файл."""
        j_dumps(self.dialogue, self.dialogue_log_path)

    def determine_sentiment(self, message: str) -> str:
        """
        Определяет тональность сообщения (положительное, отрицательное или нейтральное).

        Args:
            message (str): Сообщение для анализа.

        Returns:
            str: Тональность ('positive', 'negative' или 'neutral').
        """
        positive_words = ["good", "great", "excellent", "happy", "love", "wonderful", "amazing", "positive"]
        negative_words = ["bad", "terrible", "hate", "sad", "angry", "horrible", "negative", "awful"]
        neutral_words = ["okay", "fine", "neutral", "average", "moderate", "acceptable", "sufficient"]

        message_lower = message.lower()

        if any(word in message_lower for word in positive_words):
            return "positive"
        elif any(word in message_lower for word in negative_words):
            return "negative"
        elif any(word in message_lower for word in neutral_words):
            return "neutral"
        else:
            return "neutral"

    def ask(self, message: str, system_instruction: str = None, attempts: int = 3) -> str:
        """
        Отправляет сообщение модели и возвращает ответ вместе с анализом тональности.

        Args:
            message (str): Сообщение для отправки модели.
            system_instruction (str, optional): Системные инструкции.
            attempts (int, optional): Количество попыток.

        Returns:
            str: Ответ от модели.
        """
        try:
            messages = []
            if self.system_instruction or system_instruction:
                system_instruction_escaped = (system_instruction or self.system_instruction).replace('"', r'\"')
                messages.append({"role": "system", "content": system_instruction_escaped})

            message_escaped = message.replace('"', r'\"')
            messages.append({
                "role": "user",
                "content": message_escaped
            })

            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0,
                max_tokens=8000,
            )
            reply = response.choices[0].message.content.strip()

            sentiment = self.determine_sentiment(reply)

            #  Используем параметр system_instruction, переданный в метод, при добавлении в диалог
            self.dialogue.append({"role": "system", "content": system_instruction or self.system_instruction})
            self.dialogue.append({"role": "user", "content": message_escaped})
            self.dialogue.append({"role": "assistant", "content": reply, "sentiment": sentiment})

            self._save_dialogue()

            return reply
        except Exception as ex:
            logger.error(f"An error occurred while sending the message: \n-----\n {pprint(messages)} \n-----\n{ex}", exc_info=True)
            time.sleep(3)
            if attempts > 0:
                return self.ask(message, system_instruction, attempts - 1)
            return

    def describe_image(self, image_path: str | Path, prompt: Optional[str] = None, system_instruction: Optional[str] = None) -> Optional[str]:
        """
        Отправляет изображение в OpenAI API и получает его описание.

        Args:
            image_path (str | Path): Путь к изображению.
            prompt (Optional[str]): Запрос к модели.
            system_instruction (Optional[str]): Системные инструкции.

        Returns:
             Optional[str]: Описание изображения.
        """
        messages: list = []
        base64_image = base64encode(image_path)

        if system_instruction:
            messages.append({"role": "system", "content": system_instruction})

        messages.append(
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt if prompt else "What's in this image?"},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}},
                ],
            }
        )
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0,
                max_tokens=800,
            )
            # Проверяем что есть хоть какие то данные в ответе
            if response.choices and response.choices[0].message and response.choices[0].message.content:
                try:
                    raw_reply = response.choices[0].message.content.strip()
                    return j_loads_ns(raw_reply)
                except Exception as ex:
                    logger.error(f"Trouble parsing response: {response} {ex}", exc_info=True)
                    return None
            else:
               logger.error(f"Empty response from OpenAI: {response}", exc_info=True)
               return None
        except Exception as ex:
            logger.error(f"Error in openai: {ex}", exc_info=True)
            return None

    def describe_image_by_requests(self, image_path: str | Path, prompt: str = None) -> None:
        """
        Отправляет изображение в OpenAI API и получает описание через requests.

        Args:
            image_path (str | Path): Путь к изображению.
            prompt (str, optional): Запрос к модели.
        """
        base64_image = base64encode(image_path)

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {gs.credentials.openai.project_api}"
        }

        payload = {
            "model": "gpt-4o",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt if prompt else "What’s in this image?"},
                        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
                    ]
                }
            ],
            "max_tokens": 300
        }
        try:
            response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
            response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
            response_json = response.json()

        except requests.exceptions.RequestException as ex:
            logger.error(f"Error in image description {image_path=}: {ex}", exc_info=True)
        except Exception as ex:
            logger.error(f"Error decoding JSON response for {image_path=}: {ex}", exc_info=True)

    def dynamic_train(self):
        """Загружает предыдущий диалог и дообучает модель на его основе."""
        try:
            messages = j_loads(gs.path.google_drive / 'AI' / 'conversation' / 'dailogue.json')

            if messages:
                response = self.client.chat.completions.create(
                    model=self.model,
                    assistant=self.assistant_id,
                    messages=messages,
                    temperature=0,
                )
                logger.info("Fine-tuning during the conversation was successful.")
            else:
                logger.info("No previous dialogue found for fine-tuning.")
        except Exception as ex:
            logger.error(f"Error during dynamic fine-tuning: {ex}", exc_info=True)

    def train(self, data: str = None, data_dir: Path | str = None, data_file: Path | str = None, positive: bool = True) -> Optional[str]:
        """
        Обучает модель на основе указанных данных или директории.

        Args:
            data (str, optional): Путь к CSV файлу или CSV-форматированная строка с данными.
            data_dir (Path | str, optional): Директория, содержащая CSV файлы для обучения.
            data_file (Path | str, optional): Путь к отдельному CSV файлу с обучающими данными.
            positive (bool, optional): Являются ли данные положительными или отрицательными.

        Returns:
            Optional[str]: ID тренировочной работы или None, если произошла ошибка.
        """
        if not data_dir:
            data_dir = gs.path.google_drive / 'AI' / 'training'

        try:
            documents = j_loads(data if data else data_file if data_file else data_dir)

            response = self.client.training.create(
                model=self.model,
                documents=documents,
                labels=["positive" if positive else "negative"] * len(documents),
                show_progress=True
            )
            self.current_job_id = response.id
            return response.id

        except Exception as ex:
            logger.error(f"An error occurred during training: {ex}", exc_info=True)
            return None

    def save_job_id(self, job_id: str, description: str, filename: str = "job_ids.json"):
        """
        Сохраняет ID работы с описанием в файл.

        Args:
            job_id (str): ID работы для сохранения.
            description (str): Описание работы.
            filename (str, optional): Имя файла для сохранения ID работ.
        """
        job_data = {"id": job_id, "description": description, "created": time.time()}
        job_file = gs.path.google_drive / filename

        if not job_file.exists():
            j_dumps([job_data], job_file)
        else:
            existing_jobs = j_loads(job_file)
            existing_jobs.append(job_data)
            j_dumps(existing_jobs, job_file)


def main():
    """
    Основная функция для инициализации OpenAIModel и демонстрации использования.

    Описание:
        Инициализация модели:
            OpenAIModel инициализируется с системной инструкцией и ID ассистента.

        Вывод списка моделей и ассистентов:
             Методы `list_models` и `list_assistants` вызываются для вывода доступных моделей и ассистентов.
        Запрос к модели:
             Метод `ask()` используется для отправки сообщения модели и получения ответа.
        Динамическое обучение:
             Метод `dynamic_train()` выполняет динамическое обучение на основе прошлых диалогов.
        Обучение модели:
             Метод `train()` обучает модель, используя данные из указанного файла (`training_data.csv`).
        Сохранение ID тренировочной работы:
             После обучения ID работы сохраняется с описанием в JSON файл.
    """

    model = OpenAIModel(system_instruction="You are a helpful assistant.", assistant_id="asst_dr5AgQnhhhnef5OSMzQ9zdk9")

    print("Available Models:")
    models = model.list_models
    pprint(models)

    print("\nAvailable Assistants:")
    assistants = model.list_assistants
    pprint(assistants)

    user_input = "Hello, how are you?"
    print("\nUser Input:", user_input)
    response = model.ask(user_input)
    print("Model Response:", response)

    print("\nPerforming dynamic training...")
    model.dynamic_train()

    print("\nTraining the model...")
    training_result = model.train(data_file=gs.path.google_drive / 'AI' / 'training_data.csv')
    print(f"Training job ID: {training_result}")

    if training_result:
        model.save_job_id(training_result, "Training model with new data", filename="job_ids.json")
        print(f"Saved training job ID: {training_result}")

    image_path = gs.path.google_drive / 'images' / 'example_image.jpg'
    print("\nDescribing Image:")
    description = model.describe_image(image_path)
    print(f"Image description: {description}")


if __name__ == "__main__":
    main()