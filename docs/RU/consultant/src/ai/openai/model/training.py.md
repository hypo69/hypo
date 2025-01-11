# Анализ кода модуля `training.py`

**Качество кода: 7/10**

*   **Плюсы:**
    *   Код структурирован в класс `OpenAIModel`, что облегчает управление и повторное использование.
    *   Используется `logger` для логирования ошибок и важной информации.
    *   Реализована обработка исключений в различных методах.
    *   Присутствуют методы для взаимодействия с OpenAI API, включая отправку сообщений, описание изображений, обучение модели.
    *   Используются `j_loads` и `j_dumps` для работы с JSON файлами.
*   **Минусы:**
    *   Отсутствует документация в формате RST для класса и методов, что затрудняет понимание кода.
    *   В некоторых местах используется `try-except` без конкретной обработки ошибок, что может скрывать проблемы.
    *   Некоторые константы (например, `model: str = "gpt-4o-mini"`) жестко заданы, что затрудняет их изменение.
    *   Не везде используются f-строки для форматирования строк.
    *   Некоторые методы, такие как `dynamic_train`, не имеют подробных комментариев.
    *   Смешаны стили кавычек в коде.
    *   В `describe_image` лишняя проверка на `response` и не обрабатывается, что является ошибкой.

**Рекомендации по улучшению:**

1.  Добавить документацию в формате RST для класса `OpenAIModel` и всех его методов.
2.  Использовать `logger.error` с подробным описанием ошибки вместо общих `try-except`.
3.  Реализовать константы для моделей и других настроек для более легкой конфигурации.
4.  Привести в соответствие кавычки в коде.
5.  Использовать f-строки для форматирования строк, где это возможно.
6.  Улучшить обработку ошибок в методе `describe_image`.
7.  Добавить комментарии ко всем методам.

**Оптимизированный код:**

```python
"""
Модуль для взаимодействия с OpenAI API и обучения моделей.
=========================================================================================

Этот модуль содержит класс :class:`OpenAIModel`, который используется для взаимодействия с OpenAI API,
включая отправку сообщений, описание изображений и обучение моделей.

Пример использования
--------------------

Пример использования класса `OpenAIModel`:

.. code-block:: python

    model = OpenAIModel(system_instruction='You are a helpful assistant.', model_name='gpt-4o-mini', assistant_id='asst_dr5AgQnhhhnef5OSMzQ9zdk9')
    response = model.ask('Hello, how are you?')
"""
from __future__ import annotations

# /src/ai/openai/model/training.py
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

import time
from pathlib import Path
from types import SimpleNamespace
from typing import List, Dict, Optional
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

class OpenAIModel:
    """
    Класс для взаимодействия с OpenAI API и управления моделями.

    Attributes:
        model (str): Имя используемой модели.
        client (OpenAI): Клиент OpenAI API.
        current_job_id (str): Идентификатор текущей задачи.
        assistant_id (str): Идентификатор ассистента.
        assistant (Any): Объект ассистента.
        thread (Any): Объект треда.
        system_instruction (str): Системная инструкция для модели.
        dialogue_log_path (str | Path): Путь к файлу для сохранения диалога.
        dialogue (List[Dict[str, str]]): Список словарей с диалогом.
        assistants (List[SimpleNamespace]): Список доступных ассистентов.
        models_list (List[str]): Список доступных моделей.
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
        Инициализирует объект Model с ключом API, идентификатором ассистента и загружает доступные модели и ассистентов.

        Args:
            system_instruction (str, optional): Системная инструкция для модели.
            model_name (str, optional): Имя модели для использования.
            assistant_id (str, optional): Идентификатор ассистента. По умолчанию 'asst_dr5AgQnhhhnef5OSMzQ9zdk9'.
        """
        # self.client = OpenAI(api_key = gs.credentials.openai.project_api)
        # инициализация клиента OpenAI API с использованием ключа API из конфигурации
        self.client = OpenAI(api_key=gs.credentials.openai.api_key)
        self.current_job_id = None
        # определение идентификатора ассистента, либо из переданного параметра, либо из конфигурации
        self.assistant_id = assistant_id or gs.credentials.openai.assistant_id.code_assistant
        self.system_instruction = system_instruction

        # Загрузка ассистента и треда при инициализации
        # загрузка объекта ассистента
        try:
            self.assistant = self.client.beta.assistants.retrieve(self.assistant_id)
            # создание нового треда
            self.thread = self.client.beta.threads.create()
        except Exception as ex:
             logger.error('Ошибка инициализации ассистента или треда', ex)

    @property
    def list_models(self) -> List[str]:
        """
        Динамически получает и возвращает доступные модели из OpenAI API.

        Returns:
            List[str]: Список идентификаторов моделей, доступных через OpenAI API.
        """
        try:
            # отправка запроса на получение списка моделей
            models = self.client.models.list()
            # извлечение id моделей из ответа
            model_list = [model['id'] for model in models['data']]
            logger.info(f'Загружены модели: {model_list}')
            return model_list
        except Exception as ex:
            logger.error('Произошла ошибка при загрузке моделей:', ex)
            return []

    @property
    def list_assistants(self) -> List[str]:
        """
        Динамически загружает доступных ассистентов из JSON файла.

        Returns:
            List[str]: Список имен ассистентов.
        """
        try:
             # загрузка ассистентов из файла
            self.assistants = j_loads_ns(gs.path.src / 'ai' / 'openai' / 'model' / 'assistants' / 'assistants.json')
            # извлечение имен ассистентов
            assistant_list = [assistant.name for assistant in self.assistants]
            logger.info(f'Загружены ассистенты: {assistant_list}')
            return assistant_list
        except Exception as ex:
            logger.error('Произошла ошибка при загрузке ассистентов:', ex)
            return []

    def set_assistant(self, assistant_id: str):
        """
        Устанавливает ассистента, используя предоставленный идентификатор.

        Args:
            assistant_id (str): Идентификатор ассистента для установки.
        """
        try:
            self.assistant_id = assistant_id
             # загрузка объекта ассистента
            self.assistant = self.client.beta.assistants.retrieve(assistant_id)
            logger.info(f'Ассистент успешно установлен: {assistant_id}')
        except Exception as ex:
            logger.error('Произошла ошибка при установке ассистента:', ex)

    def _save_dialogue(self):
        """Сохраняет весь диалог в JSON файл."""
        j_dumps(self.dialogue, self.dialogue_log_path)

    def determine_sentiment(self, message: str) -> str:
        """
        Определяет тональность сообщения (положительная, отрицательная или нейтральная).

        Args:
            message (str): Сообщение для анализа.

        Returns:
            str: Тональность ('positive', 'negative' или 'neutral').
        """
        # список позитивных слов
        positive_words = ['good', 'great', 'excellent', 'happy', 'love', 'wonderful', 'amazing', 'positive']
        # список негативных слов
        negative_words = ['bad', 'terrible', 'hate', 'sad', 'angry', 'horrible', 'negative', 'awful']
        # список нейтральных слов
        neutral_words = ['okay', 'fine', 'neutral', 'average', 'moderate', 'acceptable', 'sufficient']

        # приведение сообщения к нижнему регистру для упрощения поиска
        message_lower = message.lower()
        # проверка на наличие позитивных слов в сообщении
        if any(word in message_lower for word in positive_words):
            return 'positive'
        # проверка на наличие негативных слов в сообщении
        elif any(word in message_lower for word in negative_words):
            return 'negative'
        # проверка на наличие нейтральных слов в сообщении
        elif any(word in message_lower for word in neutral_words):
            return 'neutral'
        else:
            return 'neutral'

    def ask(self, message: str, system_instruction: str = None, attempts: int = 3) -> str:
        """
        Отправляет сообщение модели и возвращает ответ с анализом тональности.

        Args:
            message (str): Сообщение для отправки модели.
            system_instruction (str, optional): Системная инструкция для модели.
            attempts (int, optional): Количество попыток повтора при ошибке. По умолчанию 3.

        Returns:
            str: Ответ от модели.
        """
        try:
            messages = []
            # проверка наличия системной инструкции
            if self.system_instruction or system_instruction:
                # экранирование кавычек в системной инструкции
                system_instruction_escaped = (system_instruction or self.system_instruction).replace('"', r'\"')
                # добавление системной инструкции в список сообщений
                messages.append({'role': 'system', 'content': system_instruction_escaped})

            # экранирование кавычек в пользовательском сообщении
            message_escaped = message.replace('"', r'\"')
            # добавление пользовательского сообщения в список сообщений
            messages.append({'role': 'user', 'content': message_escaped})

            # отправка запроса к модели
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0,
                max_tokens=8000,
            )
            # извлечение ответа из ответа модели
            reply = response.choices[0].message.content.strip()

            # анализ тональности ответа
            sentiment = self.determine_sentiment(reply)

            # добавление сообщений и тональности в диалог
            self.dialogue.append({'role': 'system', 'content': system_instruction or self.system_instruction})
            self.dialogue.append({'role': 'user', 'content': message_escaped})
            self.dialogue.append({'role': 'assistant', 'content': reply, 'sentiment': sentiment})

            # сохранение диалога
            self._save_dialogue()

            return reply
        except Exception as ex:
            logger.debug(f'Произошла ошибка при отправке сообщения: \n-----\n {pprint(messages)} \n-----\n', ex, True)
            time.sleep(3)
            if attempts > 0:
                return self.ask(message, attempts - 1)
            return

    def describe_image(self, image_path: str | Path, prompt: Optional[str] = None, system_instruction: Optional[str] = None) -> str | None:
        """
        Отправляет изображение в OpenAI API и получает его описание.

        Args:
            image_path (str | Path): Путь к изображению.
            prompt (str, optional): Запрос для описания изображения.
            system_instruction (str, optional): Системная инструкция для модели.

        Returns:
            str | None: Описание изображения или None в случае ошибки.
        """
        messages: list = []
        # получение изображения в формате base64
        base64_image = base64encode(image_path)

        if system_instruction:
             # добавление системной инструкции в список сообщений
            messages.append({'role': 'system', 'content': system_instruction})

         # добавление пользовательского сообщения и изображения в список сообщений
        messages.append(
            {
                'role': 'user',
                'content': [
                    {'type': 'text', 'text': prompt if prompt else "What's in this image?"},
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
            # попытка извлечь описание из ответа модели
            try:
                raw_reply = response.choices[0].message.content.strip()
                return j_loads_ns(raw_reply)
            except Exception as ex:
                logger.error(f'Ошибка в ответе {response}', ex, True)
                return
        except Exception as ex:
            logger.error(f'Ошибка openai', ex, True)
            return

    def describe_image_by_requests(self, image_path: str | Path, prompt: str = None) -> str | None:
        """
        Отправляет изображение в OpenAI API, используя requests, и получает его описание.

        Args:
            image_path (str | Path): Путь к изображению.
            prompt (str, optional): Запрос для описания изображения.

        Returns:
           str | None: Описание изображения или None в случае ошибки.
        """
        # получение изображения в формате base64
        base64_image = base64encode(image_path)

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {gs.credentials.openai.project_api}',
        }

        payload = {
            'model': 'gpt-4o',
            'messages': [
                {
                    'role': 'user',
                    'content': [
                        {'type': 'text', 'text': prompt if prompt else "What’s in this image?"},
                        {
                            'type': 'image_url',
                            'image_url': {'url': f'data:image/jpeg;base64,{base64_image}'},
                        },
                    ],
                }
            ],
            'max_tokens': 300,
        }
        try:
            # отправка POST запроса в OpenAI API
            response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=payload)
            response_json = response.json()
            return response_json
        except Exception as ex:
            logger.error(f'Ошибка при описании изображения {image_path=}\n', ex)
            return

    def dynamic_train(self):
        """Динамически загружает предыдущий диалог и дообучает модель на его основе."""
        try:
            # загрузка предыдущего диалога
            messages = j_loads(gs.path.google_drive / 'AI' / 'conversation' / 'dailogue.json')
            # проверка наличия диалога
            if messages:
                # отправка запроса на обучение модели
                response = self.client.chat.completions.create(
                    model=self.model,
                    assistant=self.assistant_id,
                    messages=messages,
                    temperature=0,
                )
                logger.info('Дообучение во время разговора прошло успешно.')
            else:
                logger.info('Предыдущий диалог для дообучения не найден.')
        except Exception as ex:
            logger.error(f'Ошибка при динамическом дообучении: {ex}')

    def train(self, data: str = None, data_dir: Path | str = None, data_file: Path | str = None, positive: bool = True) -> str | None:
        """
        Обучает модель на основе предоставленных данных или директории.

        Args:
            data (str, optional): Строка с данными в формате CSV или путь к CSV файлу.
            data_dir (Path | str, optional): Директория с CSV файлами для обучения.
            data_file (Path | str, optional): Путь к CSV файлу с данными для обучения.
            positive (bool, optional): Указывает, являются ли данные позитивными или негативными. По умолчанию True.

        Returns:
            str | None: Идентификатор задания на обучение или None в случае ошибки.
        """
        if not data_dir:
            # определение директории для обучения
            data_dir = gs.path.google_drive / 'AI' / 'training'

        try:
            # загрузка данных для обучения
            documents = j_loads(data if data else data_file if data_file else data_dir)
            # отправка запроса на обучение модели
            response = self.client.Training.create(
                model=self.model,
                documents=documents,
                labels=['positive' if positive else 'negative'] * len(documents),
                show_progress=True,
            )
            # сохранение идентификатора задания
            self.current_job_id = response.id
            return response.id
        except Exception as ex:
            logger.error('Произошла ошибка во время обучения:', ex)
            return

    def save_job_id(self, job_id: str, description: str, filename: str = 'job_ids.json'):
        """
        Сохраняет идентификатор задания с описанием в файл.

        Args:
            job_id (str): Идентификатор задания для сохранения.
            description (str): Описание задания.
            filename (str, optional): Имя файла для сохранения идентификаторов заданий. По умолчанию 'job_ids.json'.
        """
        # создание словаря с данными о задании
        job_data = {'id': job_id, 'description': description, 'created': time.time()}
        # определение пути к файлу
        job_file = gs.path.google_drive / filename
        # проверка существования файла
        if not job_file.exists():
            # если файл не существует, создать и сохранить данные
            j_dumps([job_data], job_file)
        else:
            # если файл существует, загрузить имеющиеся данные
            existing_jobs = j_loads(job_file)
            # добавить новые данные
            existing_jobs.append(job_data)
            # сохранить обновленные данные
            j_dumps(existing_jobs, job_file)

def main():
    """
    Основная функция для инициализации OpenAIModel и демонстрации использования.

    Описание:
        Инициализация модели:
            `OpenAIModel` инициализируется с системной инструкцией и идентификатором ассистента.

        Список моделей и ассистентов:
            Методы `list_models` и `list_assistants` вызываются для вывода доступных моделей и ассистентов.

        Отправка вопроса модели:
             Метод `ask()` используется для отправки сообщения модели и получения ее ответа.

        Динамическое обучение:
            Метод `dynamic_train()` выполняет динамическое дообучение на основе предыдущего диалога.

        Обучение модели:
            Метод `train()` обучает модель, используя данные из указанного файла ('training_data.csv').

        Сохранение идентификатора задания обучения:
            После обучения идентификатор задания сохраняется с описанием в JSON файл.

        Пример описания изображения:
            Метод `describe_image()` используется для описания изображения.
    """
    # инициализация модели с системными инструкциями и идентификатором ассистента (опционально)
    model = OpenAIModel(system_instruction='You are a helpful assistant.', assistant_id='asst_dr5AgQnhhhnef5OSMzQ9zdk9')

    # пример вывода списка доступных моделей
    print('Available Models:')
    models = model.list_models
    pprint(models)

    # пример вывода списка доступных ассистентов
    print('\nAvailable Assistants:')
    assistants = model.list_assistants
    pprint(assistants)

    # пример отправки вопроса модели
    user_input = 'Hello, how are you?'
    print('\nUser Input:', user_input)
    response = model.ask(user_input)
    print('Model Response:', response)

    # пример динамического обучения с использованием предыдущего диалога
    print('\nPerforming dynamic training...')
    model.dynamic_train()

    # пример обучения модели с использованием предоставленных данных
    print('\nTraining the model...')
    training_result = model.train(data_file=gs.path.google_drive / 'AI' / 'training_data.csv')
    print(f'Training job ID: {training_result}')

    # пример сохранения идентификатора задания
    if training_result:
        model.save_job_id(training_result, 'Training model with new data', filename='job_ids.json')
        print(f'Saved training job ID: {training_result}')

    # пример описания изображения
    image_path = gs.path.google_drive / 'images' / 'example_image.jpg'
    print('\nDescribing Image:')
    description = model.describe_image(image_path)
    print(f'Image description: {description}')


if __name__ == '__main__':
    main()