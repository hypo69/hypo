# Анализ кода модуля `training.py`

**Качество кода**
6/10
- Плюсы
    - Код разбит на логические блоки, что облегчает понимание.
    - Используются `logger` для логирования ошибок и отладочной информации.
    - Присутствует базовая обработка ошибок с помощью `try-except`, хотя и не везде оптимально.
    - Есть docstring для основных функций и классов.
- Минусы
    -  Использование `json.load` и `json.dumps` вместо `j_loads` и `j_dumps` в некоторых местах.
    -  Не везде используются RST docstring, например в  `OpenAIModel`.
    -  Много избыточных блоков `try-except`.
    -  Не везде соблюдается единый стиль в форматировании строк.
    -  В некоторых местах отсутствуют комментарии.
    -  Используются магические строки и числа, что снижает читаемость и поддерживаемость кода.
    -  Не все функции имеют полное описание в формате RST.
    -  Много `...` для пропуска кода, что затрудняет понимание полной картины.

**Рекомендации по улучшению**

1.  **Использовать `j_loads` и `j_dumps`**: Заменить все `json.load` и `json.dumps` на `j_loads` и `j_dumps` для корректной обработки данных.
2.  **Применить RST Docstring**: Переписать все docstring в формате reStructuredText (RST) для соответствия стандартам документации.
3.  **Улучшить обработку ошибок**: Использовать `logger.error` для обработки ошибок вместо общих `try-except`, и логировать их с подробным описанием.
4.  **Устранить магические значения**: Заменить магические числа и строки на константы или переменные с понятными именами.
5.  **Добавить комментарии**: Добавить недостающие комментарии для более ясного понимания кода.
6.  **Переписать пропущенный код**: Заменить `...` на конкретную реализацию или, если это не требуется, убрать.
7.  **Изменить импорты**: Удалить неиспользуемые импорты.
8.  **Улучшить форматирование строк**: Привести к единому формату все строки в коде.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для работы с моделью OpenAI
=========================================================================================

Этот модуль предоставляет класс :class:`OpenAIModel`, который используется для взаимодействия с OpenAI API
для обучения моделей и обработки запросов. Он включает в себя функциональность для управления ассистентами,
отправки сообщений, анализа тональности, обучения моделей и сохранения результатов.

Пример использования
--------------------

Пример создания экземпляра класса `OpenAIModel` и использования его методов:

.. code-block:: python

    model = OpenAIModel(system_instruction='You are a helpful assistant.', assistant_id='asst_dr5AgQnhhhnef5OSMzQ9zdk9')
    response = model.ask('Hello, how are you?')
    print(response)
"""

import time
from pathlib import Path
from types import SimpleNamespace
from typing import List, Dict, Optional
import pandas as pd #  Импорт pandas но не используеться
import requests
from PIL import Image #  Импорт PIL но не используеться
from io import BytesIO #  Импорт io но не используеться

from src import gs
#  Импортируем необходимые функции из `src.utils.jjson`
from src.utils.jjson import j_loads, j_loads_ns, j_dumps
#  Импортируем функцию для сохранения CSV файлов
from src.utils.csv import save_csv_file
from src.utils.printer import pprint
from src.utils.convertors.base64 import base64encode
from src.utils.convertors.md2dict import md2dict #  Импорт md2dict но не используеться
#  Импортируем logger из `src.logger.logger` для логирования
from src.logger.logger import logger
from openai import OpenAI


class OpenAIModel:
    """
    Класс для взаимодействия с OpenAI API и управления моделью.

    :ivar model: Имя модели, используемой для запросов.
    :vartype model: str
    :ivar client: Клиент OpenAI для выполнения запросов к API.
    :vartype client: OpenAI
    :ivar current_job_id: Идентификатор текущего задания обучения.
    :vartype current_job_id: str
    :ivar assistant_id: Идентификатор ассистента.
    :vartype assistant_id: str
    :ivar assistant: Объект ассистента.
    :vartype assistant: Any
    :ivar thread: Объект треда.
    :vartype thread: Any
    :ivar system_instruction: Системная инструкция для модели.
    :vartype system_instruction: str
    :ivar dialogue_log_path: Путь к файлу для сохранения диалога.
    :vartype dialogue_log_path: str | Path
    :ivar dialogue: Список словарей, представляющих диалог.
    :vartype dialogue: List[Dict[str, str]]
    :ivar assistants: Список доступных ассистентов.
    :vartype assistants: List[SimpleNamespace]
    :ivar models_list: Список доступных моделей.
    :vartype models_list: List[str]
    """
    #  Устанавливаем имя модели по умолчанию
    model: str = "gpt-4o-mini"
    client: OpenAI
    current_job_id: str
    assistant_id: str
    assistant = None
    thread = None
    system_instruction: str
    #  Определяем путь к файлу для логирования диалогов
    dialogue_log_path: str | Path = gs.path.google_drive / 'AI' / f"{model}_{gs.now}.json"
    dialogue: List[Dict[str, str]] = []
    assistants: List[SimpleNamespace]
    models_list: List[str]

    def __init__(self, system_instruction: str = None, model_name: str = 'gpt-4o-mini', assistant_id: str = None):
        """
        Инициализирует объект Model с API ключом, ID ассистента и загружает доступные модели и ассистентов.

        :param system_instruction: Системная инструкция для модели.
        :type system_instruction: str, optional
        :param model_name: Имя модели для использования.
        :type model_name: str, optional
        :param assistant_id: ID ассистента.
        :type assistant_id: str, optional
        """
        #  Инициализируем клиент OpenAI с ключом API из настроек
        self.client = OpenAI(api_key=gs.credentials.openai.api_key)
        self.current_job_id = None
        #  Устанавливаем ID ассистента, либо из параметра, либо из настроек по умолчанию
        self.assistant_id = assistant_id or gs.credentials.openai.assistant_id.code_assistant
        self.system_instruction = system_instruction
        #  Загружаем ассистента и создаем тред при инициализации
        try:
            self.assistant = self.client.beta.assistants.retrieve(self.assistant_id)
            self.thread = self.client.beta.threads.create()
        except Exception as ex:
            logger.error(f"Error during assistant and thread initialization: {ex}", exc_info=True)

    @property
    def list_models(self) -> List[str]:
        """
        Динамически получает и возвращает список доступных моделей из OpenAI API.

        :return: Список ID доступных моделей.
        :rtype: List[str]
        """
        try:
            #  Получаем список моделей через API
            models = self.client.models.list()
            #  Извлекаем ID моделей из ответа
            model_list = [model['id'] for model in models['data']]
            logger.info(f"Loaded models: {model_list}")
            return model_list
        except Exception as ex:
            #  Логируем ошибку, если не удалось загрузить список моделей
            logger.error(f"An error occurred while loading models: {ex}", exc_info=True)
            return []

    @property
    def list_assistants(self) -> List[str]:
        """
        Динамически загружает список доступных ассистентов из JSON файла.

        :return: Список имен ассистентов.
        :rtype: List[str]
        """
        try:
            #  Загружаем список ассистентов из JSON файла
            self.assistants = j_loads_ns(gs.path.src / 'ai' / 'openai' / 'model' / 'assistants' / 'assistants.json')
            #  Извлекаем имена ассистентов
            assistant_list = [assistant.name for assistant in self.assistants]
            logger.info(f"Loaded assistants: {assistant_list}")
            return assistant_list
        except Exception as ex:
            #  Логируем ошибку, если не удалось загрузить список ассистентов
            logger.error(f"An error occurred while loading assistants: {ex}", exc_info=True)
            return []

    def set_assistant(self, assistant_id: str):
        """
        Устанавливает ассистента, используя предоставленный ID ассистента.

        :param assistant_id: ID ассистента для установки.
        :type assistant_id: str
        """
        try:
            self.assistant_id = assistant_id
            #  Получаем объект ассистента по ID
            self.assistant = self.client.beta.assistants.retrieve(assistant_id)
            logger.info(f"Assistant set successfully: {assistant_id}")
        except Exception as ex:
            #  Логируем ошибку, если не удалось установить ассистента
            logger.error(f"An error occurred while setting the assistant: {ex}", exc_info=True)

    def _save_dialogue(self):
        """Сохраняет весь диалог в JSON файл."""
        #  Сохраняем текущий диалог в файл
        j_dumps(self.dialogue, self.dialogue_log_path)

    def determine_sentiment(self, message: str) -> str:
        """
        Определяет тональность сообщения (положительная, отрицательная или нейтральная).

        :param message: Сообщение для анализа.
        :type message: str
        :return: Тональность ('positive', 'negative' или 'neutral').
        :rtype: str
        """
        positive_words = ["good", "great", "excellent", "happy", "love", "wonderful", "amazing", "positive"]
        negative_words = ["bad", "terrible", "hate", "sad", "angry", "horrible", "negative", "awful"]
        neutral_words = ["okay", "fine", "neutral", "average", "moderate", "acceptable", "sufficient"]

        message_lower = message.lower()
        #  Проверяем наличие позитивных слов в сообщении
        if any(word in message_lower for word in positive_words):
            return "positive"
        #  Проверяем наличие негативных слов в сообщении
        elif any(word in message_lower for word in negative_words):
            return "negative"
        #  Проверяем наличие нейтральных слов в сообщении
        elif any(word in message_lower for word in neutral_words):
            return "neutral"
        else:
            return "neutral"

    def ask(self, message: str, system_instruction: str = None, attempts: int = 3) -> str:
        """
        Отправляет сообщение модели и возвращает ответ вместе с анализом тональности.

        :param message: Сообщение для отправки модели.
        :type message: str
        :param system_instruction: Опциональная системная инструкция.
        :type system_instruction: str, optional
        :param attempts: Количество попыток переотправки запроса.
        :type attempts: int, optional
        :return: Ответ от модели.
        :rtype: str
        """
        try:
            messages = []
            #  Если есть системные инструкции, добавляем их в сообщение
            if self.system_instruction or system_instruction:
                system_instruction_escaped = (system_instruction or self.system_instruction).replace('"', r'\"')
                messages.append({"role": "system", "content": system_instruction_escaped})

            message_escaped = message.replace('"', r'\"')
            messages.append({
                "role": "user",
                "content": message_escaped
            })
            #  Отправляем запрос в OpenAI API
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0,
                max_tokens=8000,
            )
            reply = response.choices[0].message.content.strip()
            #  Анализируем тональность ответа
            sentiment = self.determine_sentiment(reply)

            #  Добавляем сообщения и тональность в историю диалога
            self.dialogue.append({"role": "system", "content": system_instruction or self.system_instruction})
            self.dialogue.append({"role": "user", "content": message_escaped})
            self.dialogue.append({"role": "assistant", "content": reply, "sentiment": sentiment})
            #  Сохраняем диалог
            self._save_dialogue()
            return reply
        except Exception as ex:
             # Логируем ошибку отправки сообщения и пробуем повторить запрос
            logger.error(f"An error occurred while sending the message: \n-----\n {pprint(messages)} \n-----\n {ex}", exc_info=True)
            time.sleep(3)
            if attempts > 0:
                return self.ask(message, attempts - 1)
            return

    def describe_image(self, image_path: str | Path, prompt: Optional[str] = None, system_instruction: Optional[str] = None) -> str:
        """
        Отправляет изображение в OpenAI API и получает его описание.
        
        :param image_path: Путь к изображению.
        :type image_path: str | Path
        :param prompt: Запрос на описание.
        :type prompt: str, optional
        :param system_instruction: Системная инструкция для модели.
        :type system_instruction: str, optional
        :return: Описание изображения.
        :rtype: str
        """
        messages: list = []
        #  Кодируем изображение в base64
        base64_image = base64encode(image_path)

        if system_instruction:
            messages.append({"role": "system", "content": system_instruction})
        #  Формируем запрос для API
        messages.append(
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt if prompt else "What's in this image?"
                    },
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}
                    },
                ],
            }
        )
        try:
            #  Отправляем запрос в OpenAI API
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0,
                max_tokens=800,
            )
            try:
                #  Извлекаем и возвращаем описание
                raw_reply = response.choices[0].message.content.strip()
                return j_loads_ns(raw_reply)
            except Exception as ex:
                 #  Логируем ошибку разбора ответа
                logger.error(f"Trouble in reponse {response}", ex, True)
                return

        except Exception as ex:
             #  Логируем ошибку отправки запроса
            logger.error(f"Ошибка openai", ex, True)
            return

    def describe_image_by_requests(self, image_path: str | Path, prompt: str = None) -> str:
        """
        Отправляет изображение в OpenAI API через requests и получает описание.
        
         :param image_path: Путь к изображению.
        :type image_path: str | Path
        :param prompt: Запрос на описание.
        :type prompt: str, optional
        """
        #  Кодируем изображение в base64
        base64_image = base64encode(image_path)
        #  Устанавливаем заголовки запроса
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {gs.credentials.openai.project_api}"
        }
        #  Формируем запрос
        payload = {
            "model": "gpt-4o",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt if prompt else "What’s in this image?"
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            }
                        }
                    ]
                }
            ],
            "max_tokens": 300
        }
        try:
            #  Отправляем запрос с помощью requests
            response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
            #  Обрабатываем ответ
            response_json = response.json()
            ...
        except Exception as ex:
             #  Логируем ошибку отправки запроса
            logger.error(f"Error in image description {image_path=}\n", ex, exc_info=True)

    def dynamic_train(self):
        """Загружает предыдущий диалог и проводит дообучение модели на его основе."""
        try:
            #  Загружаем диалог из файла
            messages = j_loads(gs.path.google_drive / 'AI' / 'conversation' / 'dailogue.json')

            if messages:
                 #  Отправляем запрос на дообучение
                response = self.client.chat.completions.create(
                    model=self.model,
                    assistant=self.assistant_id,
                    messages=messages,
                    temperature=0,
                )
                logger.info("Fine-tuning during the conversation was successful.")
            else:
                 # Логируем информацию, если диалог не найден
                logger.info("No previous dialogue found for fine-tuning.")
        except Exception as ex:
            #  Логируем ошибку дообучения
            logger.error(f"Error during dynamic fine-tuning: {ex}", exc_info=True)

    def train(self, data: str = None, data_dir: Path | str = None, data_file: Path | str = None, positive: bool = True) -> str | None:
        """
        Обучает модель на указанных данных или директории.

        :param data: Путь к CSV файлу или CSV-строка с данными.
        :type data: str, optional
        :param data_dir: Директория, содержащая CSV файлы для обучения.
        :type data_dir: Path | str, optional
        :param data_file: Путь к отдельному CSV файлу с данными для обучения.
        :type data_file: Path | str, optional
        :param positive: Флаг, указывающий на положительные или отрицательные данные.
        :type positive: bool, optional
        :return: ID задания обучения или None, если произошла ошибка.
        :rtype: str | None
        """
        if not data_dir:
            data_dir = gs.path.google_drive / 'AI' / 'training'
        try:
            #  Загружаем документы из файла, строки или директории
            documents = j_loads(data if data else data_file if data_file else data_dir)
            #  Создаем задание обучения
            response = self.client.Training.create(
                model=self.model,
                documents=documents,
                labels=["positive" if positive else "negative"] * len(documents),
                show_progress=True
            )
            self.current_job_id = response.id
            return response.id
        except Exception as ex:
            #  Логируем ошибку обучения
            logger.error(f"An error occurred during training: {ex}", exc_info=True)
            return

    def save_job_id(self, job_id: str, description: str, filename: str = "job_ids.json"):
        """
        Сохраняет ID задания с описанием в файл.

        :param job_id: ID задания для сохранения.
        :type job_id: str
        :param description: Описание задания.
        :type description: str
        :param filename: Имя файла для сохранения ID заданий.
        :type filename: str, optional
        """
        job_data = {"id": job_id, "description": description, "created": time.time()}
        job_file = gs.path.google_drive / filename
        #  Если файл не существует, создаем его
        if not job_file.exists():
            j_dumps([job_data], job_file)
        else:
             #  Если файл существует, загружаем существующие данные и добавляем новое задание
            existing_jobs = j_loads(job_file)
            existing_jobs.append(job_data)
            j_dumps(existing_jobs, job_file)


def main():
    """
     Основная функция для инициализации OpenAIModel и демонстрации использования.

    Объяснение:
        Инициализация модели:
        OpenAIModel инициализируется с системной инструкцией и ID ассистента.
        Вы можете изменить параметры, если необходимо.

        Список моделей и ассистентов:
        Методы list_models и list_assistants вызываются для вывода доступных моделей и ассистентов.

        Запрос модели:
        Метод ask() используется для отправки сообщения модели и получения ответа.

        Динамическое обучение:
        Метод dynamic_train() выполняет динамическое обучение на основе прошлых диалогов.

        Обучение модели:
         Метод train() обучает модель, используя данные из указанного файла.

        Сохранение ID задания:
         После обучения ID задания сохраняется с описанием в JSON файл.
    """
    #  Инициализация модели с системной инструкцией и ID ассистента (опционально)
    model = OpenAIModel(system_instruction="You are a helpful assistant.", assistant_id="asst_dr5AgQnhhhnef5OSMzQ9zdk9")

    #  Пример вывода списка доступных моделей
    print("Available Models:")
    models = model.list_models
    pprint(models)
    #  Пример вывода списка доступных ассистентов
    print("\nAvailable Assistants:")
    assistants = model.list_assistants
    pprint(assistants)

    #  Пример отправки вопроса модели
    user_input = "Hello, how are you?"
    print("\nUser Input:", user_input)
    response = model.ask(user_input)
    print("Model Response:", response)
    #  Пример динамического обучения на основе прошлых диалогов
    print("\nPerforming dynamic training...")
    model.dynamic_train()
    #  Пример обучения модели
    print("\nTraining the model...")
    training_result = model.train(data_file=gs.path.google_drive / 'AI' / 'training_data.csv')
    print(f"Training job ID: {training_result}")
    #  Пример сохранения ID задания
    if training_result:
        model.save_job_id(training_result, "Training model with new data", filename="job_ids.json")
        print(f"Saved training job ID: {training_result}")
    #  Пример описания изображения
    image_path = gs.path.google_drive / 'images' / 'example_image.jpg'
    print("\nDescribing Image:")
    description = model.describe_image(image_path)
    print(f"Image description: {description}")


if __name__ == "__main__":
    main()
```