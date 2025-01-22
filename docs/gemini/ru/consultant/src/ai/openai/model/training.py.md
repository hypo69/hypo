### Анализ кода модуля `training`

**Качество кода**:
- **Соответствие стандартам**: 7/10
- **Плюсы**:
    - Код хорошо структурирован, используется ООП подход.
    - Присутствует базовая обработка ошибок.
    - Используется `j_loads` и `j_dumps` для работы с JSON.
    - Есть логирование действий и ошибок.
    - Код имеет docstring для классов и методов.
- **Минусы**:
    - Не везде используется `from src.logger.logger import logger`.
    - Некоторые блоки `try-except` перехватывают все исключения без конкретизации.
    -  Много комментариев вида "делаем", "получаем".
    - Есть `...` маркеры.
    - Не все `docstring` соответствуют стандарту RST.
    - Смешивание одинарных и двойных кавычек в коде.
    - Не везде используется логирование для критических ошибок.

**Рекомендации по улучшению**:
- Необходимо привести все строки кода к использованию одинарных кавычек, двойные оставить только для `print`, `input`, `logger`.
- Заменить все `...` на конкретный код или `pass`, если это необходимо.
- Конкретизировать перехватываемые исключения в блоках `try-except`.
- Улучшить логирование ошибок, добавляя контекст и подробности.
- Пересмотреть комментарии, сделать их более информативными и точными.
- Улучшить форматирование `docstring` в соответствии с форматом RST.
- Использовать `from src.logger.logger import logger` для логирования ошибок.
- Использовать f-строки для более удобного форматирования строк.
- Разделить функцию `train` на более мелкие функции для улучшения читаемости.
- Добавить проверку типов данных, где это необходимо.

**Оптимизированный код**:
```python
from __future__ import annotations

# /src/ai/openai/model/training.py
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль для работы с OpenAI API и обучения моделей
==================================================

Модуль содержит класс :class:`OpenAIModel`, который используется для взаимодействия с OpenAI API
и управления обучением моделей.

Пример использования
----------------------
.. code-block:: python

    model = OpenAIModel(system_instruction='You are a helpful assistant.', assistant_id='asst_...')
    response = model.ask('Hello, how are you?')
    print(response)
"""

import time
from pathlib import Path
from types import SimpleNamespace
from typing import List, Dict, Optional

import pandas as pd
import requests
from openai import OpenAI
from PIL import Image
from io import BytesIO

from src import gs
from src.utils.jjson import j_loads, j_loads_ns, j_dumps
from src.utils.csv import save_csv_file
from src.utils.printer import pprint
from src.utils.convertors.base64 import base64encode
from src.utils.convertors.md import md2dict
from src.logger.logger import logger # Используем импорт из src.logger.logger


class OpenAIModel:
    """
    Класс для взаимодействия с OpenAI API и управления моделями.

    :ivar model: Имя используемой модели.
    :vartype model: str
    :ivar client: Клиент OpenAI API.
    :vartype client: OpenAI
    :ivar current_job_id: ID текущего задания.
    :vartype current_job_id: str
    :ivar assistant_id: ID ассистента.
    :vartype assistant_id: str
    :ivar assistant: Объект ассистента.
    :vartype assistant: openai.types.beta.assistant.Assistant
    :ivar thread: Объект потока.
    :vartype thread: openai.types.beta.thread.Thread
    :ivar system_instruction: Системная инструкция для модели.
    :vartype system_instruction: str
    :ivar dialogue_log_path: Путь к файлу для сохранения диалогов.
    :vartype dialogue_log_path: str | Path
    :ivar dialogue: Список диалогов.
    :vartype dialogue: List[Dict[str, str]]
    :ivar assistants: Список доступных ассистентов.
    :vartype assistants: List[SimpleNamespace]
    :ivar models_list: Список доступных моделей.
    :vartype models_list: List[str]
    """

    model: str = 'gpt-4o-mini'
    # model: str = "gpt-4o-2024-08-06"
    client: OpenAI
    current_job_id: str
    assistant_id: str
    assistant = None
    thread = None
    system_instruction: str
    dialogue_log_path: str | Path = gs.path.google_drive / 'AI' / f'{model}_{gs.now}.json'
    dialogue: List[Dict[str, str]] = []
    assistants: List[SimpleNamespace]
    models_list: List[str]

    def __init__(self, system_instruction: str = None, model_name: str = 'gpt-4o-mini', assistant_id: str = None):
        """
        Инициализирует объект Model с ключом API, ID ассистента и загружает доступные модели и ассистентов.

        :param system_instruction: Системная инструкция для модели.
        :type system_instruction: str, optional
        :param model_name: Название модели.
        :type model_name: str, optional
        :param assistant_id: ID ассистента.
        :type assistant_id: str, optional
        """
        self.client = OpenAI(api_key=gs.credentials.openai.api_key) # Используем api_key
        self.current_job_id = None
        self.assistant_id = assistant_id or gs.credentials.openai.assistant_id.code_assistant
        self.system_instruction = system_instruction

        # Загрузка ассистента и потока при инициализации
        try:
            self.assistant = self.client.beta.assistants.retrieve(self.assistant_id)
            self.thread = self.client.beta.threads.create()
        except Exception as ex:
            logger.error(f'An error occurred while initializing the assistant or thread: {ex}', exc_info=True)

    @property
    def list_models(self) -> List[str]:
        """
        Динамически получает и возвращает доступные модели из OpenAI API.

        :return: Список ID моделей, доступных через OpenAI API.
        :rtype: List[str]
        """
        try:
            models = self.client.models.list()
            model_list = [model['id'] for model in models['data']]
            logger.info(f'Loaded models: {model_list}')
            return model_list
        except Exception as ex:
            logger.error(f'An error occurred while loading models: {ex}', exc_info=True)
            return []

    @property
    def list_assistants(self) -> List[str]:
        """
        Динамически загружает доступных ассистентов из JSON файла.

        :return: Список имен ассистентов.
        :rtype: List[str]
        """
        try:
            self.assistants = j_loads_ns(gs.path.src / 'ai' / 'openai' / 'model' / 'assistants' / 'assistants.json')
            assistant_list = [assistant.name for assistant in self.assistants]
            logger.info(f'Loaded assistants: {assistant_list}')
            return assistant_list
        except Exception as ex:
            logger.error(f'An error occurred while loading assistants: {ex}', exc_info=True)
            return []

    def set_assistant(self, assistant_id: str):
        """
        Устанавливает ассистента, используя предоставленный ID.

        :param assistant_id: ID ассистента, которого нужно установить.
        :type assistant_id: str
        """
        try:
            self.assistant_id = assistant_id
            self.assistant = self.client.beta.assistants.retrieve(assistant_id)
            logger.info(f'Assistant set successfully: {assistant_id}')
        except Exception as ex:
             logger.error(f'An error occurred while setting the assistant: {ex}', exc_info=True)

    def _save_dialogue(self):
        """Сохраняет весь диалог в JSON файл."""
        j_dumps(self.dialogue, self.dialogue_log_path)

    def determine_sentiment(self, message: str) -> str:
        """
        Определяет тональность сообщения (положительная, отрицательная или нейтральная).

        :param message: Сообщение для анализа.
        :type message: str
        :return: Тональность ('positive', 'negative', или 'neutral').
        :rtype: str
        """
        positive_words = ['good', 'great', 'excellent', 'happy', 'love', 'wonderful', 'amazing', 'positive']
        negative_words = ['bad', 'terrible', 'hate', 'sad', 'angry', 'horrible', 'negative', 'awful']
        neutral_words = ['okay', 'fine', 'neutral', 'average', 'moderate', 'acceptable', 'sufficient']

        message_lower = message.lower()

        if any(word in message_lower for word in positive_words):
            return 'positive'
        elif any(word in message_lower for word in negative_words):
            return 'negative'
        elif any(word in message_lower for word in neutral_words):
            return 'neutral'
        else:
            return 'neutral'

    def ask(self, message: str, system_instruction: str = None, attempts: int = 3) -> str:
        """
        Отправляет сообщение модели и возвращает ответ вместе с анализом тональности.

        :param message: Сообщение для отправки модели.
        :type message: str
        :param system_instruction: Системная инструкция, опционально.
        :type system_instruction: str, optional
        :param attempts: Количество попыток повтора.
        :type attempts: int, optional
        :return: Ответ от модели.
        :rtype: str
        """
        try:
            messages = []
            if self.system_instruction or system_instruction:
                system_instruction_escaped = (system_instruction or self.system_instruction).replace('"', r'\"')
                messages.append({'role': 'system', 'content': system_instruction_escaped})

            message_escaped = message.replace('"', r'\"')
            messages.append({
                            'role': 'user',
                             'content': message_escaped
                             })

            # Отправка запроса к модели
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0,
                max_tokens=8000,
            )
            reply = response.choices[0].message.content.strip()

            # Анализ тональности
            sentiment = self.determine_sentiment(reply)

            # Добавление сообщений и тональности в диалог
            self.dialogue.append({'role': 'system', 'content': system_instruction or self.system_instruction})
            self.dialogue.append({'role': 'user', 'content': message_escaped})
            self.dialogue.append({'role': 'assistant', 'content': reply, 'sentiment': sentiment})

            # Сохранение диалога
            self._save_dialogue()

            return reply
        except Exception as ex:
            logger.debug(f'An error occurred while sending the message: \\n-----\\n {pprint(messages)} \\n-----\\n {ex}', exc_info=True)
            time.sleep(3)
            if attempts > 0:
                return self.ask(message, system_instruction, attempts - 1)
            return

    def describe_image(self, image_path: str | Path, prompt: Optional[str] = None, system_instruction: Optional[str] = None) -> str | None:
        """
        Отправляет изображение в OpenAI API и получает его описание.

        :param image_path: Путь к изображению.
        :type image_path: str | Path
        :param prompt: Запрос для описания изображения.
        :type prompt: str, optional
        :param system_instruction: Системная инструкция.
        :type system_instruction: str, optional
        :return: Описание изображения.
        :rtype: str | None
        """
        messages: list = []
        base64_image = base64encode(image_path)

        if system_instruction:
            messages.append({'role': 'system', 'content': system_instruction})

        messages.append(
            {
                'role': 'user',
                'content': [
                    {'type': 'text', 'text': prompt if prompt else 'What\'s in this image?'},
                    {'type': 'image_url', 'image_url': {'url': f'data:image/jpeg;base64,{base64_image}'}},
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

            try:
                raw_reply = response.choices[0].message.content.strip()
                return j_loads_ns(raw_reply)
            except Exception as ex:
                logger.error(f'Trouble in response {response}: {ex}', exc_info=True)
                return

        except Exception as ex:
            logger.error(f'Ошибка openai: {ex}', exc_info=True)
            return

    def describe_image_by_requests(self, image_path: str | Path, prompt: str = None) -> str:
        """
        Отправляет изображение в OpenAI API с помощью requests и получает описание.

        :param image_path: Путь к изображению.
        :type image_path: str | Path
        :param prompt: Запрос для описания изображения.
        :type prompt: str, optional
        :return: Описание изображения.
        :rtype: str
        """
        base64_image = base64encode(image_path)

        headers = {
          'Content-Type': 'application/json',
          'Authorization': f'Bearer {gs.credentials.openai.project_api}'
        }

        payload = {
          'model': 'gpt-4o',
          'messages': [
            {
              'role': 'user',
              'content': [
                {
                  'type': 'text',
                  'text': prompt if prompt else 'What’s in this image?'
                },
                {
                  'type': 'image_url',
                  'image_url': {
                    'url': f'data:image/jpeg;base64,{base64_image}'
                  }
                }
              ]
            }
          ],
          'max_tokens': 300
        }
        try:
            response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=payload)
            response.raise_for_status() # Проверка статуса ответа
            response_json = response.json()
        except requests.exceptions.RequestException as ex: # Ловим ошибку запроса
            logger.error(f'Error in image description {image_path=}: {ex}', exc_info=True)
        except Exception as ex:
            logger.error(f'Error while parsing json: {ex}', exc_info=True)

    def dynamic_train(self):
        """Динамически загружает предыдущий диалог и дообучает модель на его основе."""
        try:
            messages = j_loads(gs.path.google_drive / 'AI' / 'conversation' / 'dailogue.json')

            if messages:
                response = self.client.chat.completions.create(
                    model=self.model,
                    # assistant=self.assistant_id, # Ассистент не нужен в этом запросе
                    messages=messages,
                    temperature=0,
                )
                logger.info('Fine-tuning during the conversation was successful.')
            else:
                logger.info('No previous dialogue found for fine-tuning.')
        except Exception as ex:
            logger.error(f'Error during dynamic fine-tuning: {ex}', exc_info=True)

    def train(self, data: str = None, data_dir: Path | str = None, data_file: Path | str = None, positive: bool = True) -> str | None:
        """
        Обучает модель на указанных данных или директории.

        :param data: Путь к CSV файлу или строка в формате CSV с данными.
        :type data: str, optional
        :param data_dir: Директория с CSV файлами для обучения.
        :type data_dir: Path | str, optional
        :param data_file: Путь к одному CSV файлу с данными для обучения.
        :type data_file: Path | str, optional
        :param positive: Определяет, являются ли данные положительными или отрицательными.
        :type positive: bool, optional
        :return: ID задания обучения или None в случае ошибки.
        :rtype: str | None
        """
        if not data_dir:
            data_dir = gs.path.google_drive / 'AI' / 'training'

        try:
            if data:
                documents = j_loads(data)
            elif data_file:
                documents = j_loads(data_file)
            elif data_dir:
                 documents = j_loads(data_dir)
            else:
                logger.error('No training data provided.')
                return None
            
            if not isinstance(documents, list):
               logger.error('Documents must be a list')
               return None
            
            labels = ['positive' if positive else 'negative'] * len(documents)

            response = self.client.training.create(
                model=self.model,
                documents=documents,
                labels=labels,
                show_progress=True
            )
            self.current_job_id = response.id
            return response.id

        except Exception as ex:
            logger.error(f'An error occurred during training: {ex}', exc_info=True)
            return

    def save_job_id(self, job_id: str, description: str, filename: str = 'job_ids.json'):
        """
        Сохраняет ID задания с описанием в файл.

        :param job_id: ID задания для сохранения.
        :type job_id: str
        :param description: Описание задания.
        :type description: str
        :param filename: Имя файла для сохранения ID заданий.
        :type filename: str, optional
        """
        job_data = {'id': job_id, 'description': description, 'created': time.time()}
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
    
    Объяснение:
        Инициализация модели:

        OpenAIModel инициализируется с системной инструкцией и ID ассистента. Параметры можно изменять при необходимости.
        Получение списка моделей и ассистентов:

        Вызываются методы list_models и list_assistants для вывода доступных моделей и ассистентов.
        Запрос к модели:

        Метод ask() используется для отправки сообщения модели и получения ответа.
        Динамическое обучение:

        Метод dynamic_train() выполняет динамическую донастройку на основе предыдущего диалога.
        Обучение модели:

        Метод train() обучает модель, используя данные из указанного файла (в данном случае 'training_data.csv').
        Сохранение ID задания обучения:

        После обучения ID задания сохраняется с описанием в JSON файл.
    """

    # Инициализация модели с системной инструкцией и ID ассистента (опционально)
    model = OpenAIModel(system_instruction='You are a helpful assistant.', assistant_id='asst_dr5AgQnhhhnef5OSMzQ9zdk9')

    # Пример вывода списка доступных моделей
    print('Available Models:')
    models = model.list_models
    pprint(models)

    # Пример вывода списка доступных ассистентов
    print('\nAvailable Assistants:')
    assistants = model.list_assistants
    pprint(assistants)

    # Пример запроса к модели
    user_input = 'Hello, how are you?'
    print('\nUser Input:', user_input)
    response = model.ask(user_input)
    print('Model Response:', response)

    # Пример динамического обучения на основе предыдущего диалога
    print('\nPerforming dynamic training...')
    model.dynamic_train()

    # Пример обучения модели с использованием предоставленных данных
    print('\nTraining the model...')
    training_result = model.train(data_file=gs.path.google_drive / 'AI' / 'training_data.csv')
    print(f'Training job ID: {training_result}')

    # Пример сохранения ID задания
    if training_result:
        model.save_job_id(training_result, 'Training model with new data', filename='job_ids.json')
        print(f'Saved training job ID: {training_result}')

    # Пример описания изображения
    image_path = gs.path.google_drive / 'images' / 'example_image.jpg'
    print('\nDescribing Image:')
    description = model.describe_image(image_path)
    print(f'Image description: {description}')


if __name__ == '__main__':
    main()