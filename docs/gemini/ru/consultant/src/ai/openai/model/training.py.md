# Анализ кода модуля `training.py`

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован, использует классы и методы для организации функциональности.
    - Присутствуют docstring для большинства функций и методов.
    - Используется `logger` для логирования ошибок и информационных сообщений.
    - Применяются `j_loads`, `j_loads_ns` и `j_dumps` для работы с JSON.
- Минусы
    - Некоторые docstring требуют доработки и приведения к формату reStructuredText (RST).
    - Есть дублирование кода, например, в методах `describe_image` и `describe_image_by_requests`.
    - В некоторых местах обработка ошибок неполная или отсутствует.
    - Использование `time.sleep` в `ask` методе не лучшее решение для retry логики.
    - В методе `train` не реализована загрузка данных из каталога.

**Рекомендации по улучшению**

1. **Документация**:
   - Привести все docstring к формату RST, включая параметры, возвращаемые значения и описание.
   - Описать назначение модуля в начале файла.

2. **Обработка ошибок**:
   - Использовать `logger.error` для обработки ошибок и предоставлять более информативные сообщения.
   - Убрать избыточные `try-except` блоки, где это возможно.

3. **Рефакторинг**:
   - Вынести общий код для отправки запросов к OpenAI API в отдельную функцию или метод.
   - Добавить обработку случая отсутствия `response.choices` в методе `ask` и `describe_image`.
   - В методе `train` добавить обработку случаев, когда `data` является каталогом, и загружать все CSV файлы из него.
   - Переработать `determine_sentiment` метод с использованием более продвинутых методов анализа тональности.
   - Проработать логику retry в методе `ask`, использовать экспоненциальный откат.
   - Изменить метод `describe_image` на более универсальный, убрав дублирование кода.

4. **Импорты**:
    - Проверить и добавить отсутствующие импорты, например, `Any`.
5. **Общие рекомендации**:
   - Использовать `Path` для работы с путями.
   - Переписать комментарии в стиле RST.
   - Использовать f-строки для форматирования строк, где это уместно.
   - Избегать магических чисел, использовать константы.
   - Убедиться, что все функции и методы имеют правильные типы для параметров и возвращаемых значений.
   - Добавить `TODO` для потенциальных улучшений.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для взаимодействия с OpenAI API и управления обучением моделей.
=====================================================================

Этот модуль содержит класс :class:`OpenAIModel`, который используется для
общения с OpenAI API, управления моделями и их обучения.

Основные возможности включают:
    - Загрузка и управление доступными моделями и ассистентами.
    - Отправка сообщений в модель и получение ответов с анализом тональности.
    - Описание изображений с помощью модели.
    - Динамическая и ручная настройка моделей на основе предоставленных данных.
    - Сохранение ID заданий для обучения.

Пример использования
--------------------

Пример использования класса `OpenAIModel`:

.. code-block:: python

    model = OpenAIModel(system_instruction="You are a helpful assistant.", assistant_id="asst_dr5AgQnhhhnef5OSMzQ9zdk9")
    response = model.ask("Hello, how are you?")
    print(response)
"""
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
from src.utils.convertors.md2dict import md2dict
from src.logger.logger import logger




class OpenAIModel:
    """
    Класс для взаимодействия с OpenAI API и управления моделью.

    :ivar model: Имя используемой модели.
    :vartype model: str
    :ivar client: Клиент OpenAI API.
    :vartype client: OpenAI
    :ivar current_job_id: ID текущего задания.
    :vartype current_job_id: str
    :ivar assistant_id: ID ассистента.
    :vartype assistant_id: str
    :ivar assistant: Объект ассистента.
    :vartype assistant: Optional[Any]
    :ivar thread: Объект потока.
    :vartype thread: Optional[Any]
    :ivar system_instruction: Системная инструкция.
    :vartype system_instruction: str
    :ivar dialogue_log_path: Путь к файлу журнала диалога.
    :vartype dialogue_log_path: Path
    :ivar dialogue: Список сообщений диалога.
    :vartype dialogue: List[Dict[str, str]]
    :ivar assistants: Список доступных ассистентов.
    :vartype assistants: List[SimpleNamespace]
    :ivar models_list: Список доступных моделей.
    :vartype models_list: List[str]
    """
    model: str = "gpt-4o-mini"
    client: OpenAI
    current_job_id: str
    assistant_id: str
    assistant = None
    thread = None
    system_instruction: str
    dialogue_log_path: Path = gs.path.google_drive / 'AI' / f"{model}_{gs.now}.json"
    dialogue: List[Dict[str, str]] = []
    assistants: List[SimpleNamespace]
    models_list: List[str]

    def __init__(self, system_instruction: str = None, model_name: str = 'gpt-4o-mini', assistant_id: str = None):
        """
        Инициализирует объект Model с ключом API, ID ассистента и загружает доступные модели и ассистентов.

        :param system_instruction: Системная инструкция для модели.
        :type system_instruction: Optional[str]
        :param model_name: Имя модели.
        :type model_name: str
        :param assistant_id: ID ассистента.
        :type assistant_id: Optional[str]
        """
        # Инициализация клиента OpenAI API с использованием API ключа
        self.client = OpenAI(api_key=gs.credentials.openai.api_key)
        self.current_job_id = None
        # Установка ID ассистента, если он предоставлен, или использование значения по умолчанию
        self.assistant_id = assistant_id or gs.credentials.openai.assistant_id.code_assistant
        self.system_instruction = system_instruction
        # Загрузка ассистента и создание потока при инициализации
        try:
            self.assistant = self.client.beta.assistants.retrieve(self.assistant_id)
            self.thread = self.client.beta.threads.create()
        except Exception as ex:
             logger.error(f"Ошибка при загрузке ассистента или создании потока: {ex}", ex)
             ...

    @property
    def list_models(self) -> List[str]:
        """
        Динамически загружает и возвращает доступные модели из OpenAI API.

        :return: Список ID моделей, доступных через OpenAI API.
        :rtype: List[str]
        """
        try:
            # Запрос списка моделей от OpenAI API
            models = self.client.models.list()
            # Извлечение ID моделей из ответа
            model_list = [model['id'] for model in models['data']]
            logger.info(f"Загружены модели: {model_list}")
            return model_list
        except Exception as ex:
            logger.error("Произошла ошибка при загрузке моделей:", ex)
            return []

    @property
    def list_assistants(self) -> List[str]:
        """
        Динамически загружает доступных ассистентов из JSON файла.

        :return: Список имен ассистентов.
        :rtype: List[str]
        """
        try:
             # Загрузка ассистентов из файла JSON
            self.assistants = j_loads_ns(gs.path.src / 'ai' / 'openai' / 'model' / 'assistants' / 'assistants.json')
             # Извлечение имен ассистентов
            assistant_list = [assistant.name for assistant in self.assistants]
            logger.info(f"Загружены ассистенты: {assistant_list}")
            return assistant_list
        except Exception as ex:
            logger.error("Произошла ошибка при загрузке ассистентов:", ex)
            return []

    def set_assistant(self, assistant_id: str):
        """
        Устанавливает ассистента с использованием предоставленного ID ассистента.

        :param assistant_id: ID ассистента, которого необходимо установить.
        :type assistant_id: str
        """
        try:
            # Обновление ID ассистента
            self.assistant_id = assistant_id
            # Получение ассистента по ID
            self.assistant = self.client.beta.assistants.retrieve(assistant_id)
            logger.info(f"Ассистент успешно установлен: {assistant_id}")
        except Exception as ex:
            logger.error("Произошла ошибка при установке ассистента:", ex)

    def _save_dialogue(self):
        """Сохраняет весь диалог в JSON файл."""
        # Сериализация диалога и сохранение в файл
        j_dumps(self.dialogue, self.dialogue_log_path)

    def determine_sentiment(self, message: str) -> str:
        """
        Определяет тональность сообщения (положительная, отрицательная или нейтральная).

        :param message: Сообщение для анализа.
        :type message: str
        :return: Тональность сообщения ('positive', 'negative' или 'neutral').
        :rtype: str
        """
        # TODO: Использовать более продвинутые методы анализа тональности.
        positive_words = ["good", "great", "excellent", "happy", "love", "wonderful", "amazing", "positive"]
        negative_words = ["bad", "terrible", "hate", "sad", "angry", "horrible", "negative", "awful"]
        neutral_words = ["okay", "fine", "neutral", "average", "moderate", "acceptable", "sufficient"]

        message_lower = message.lower()
        # Проверка наличия слов, указывающих на тональность
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
        Отправляет сообщение в модель и возвращает ответ с анализом тональности.

        :param message: Сообщение для отправки модели.
        :type message: str
        :param system_instruction: Системная инструкция.
        :type system_instruction: Optional[str]
        :param attempts: Количество попыток отправки сообщения.
        :type attempts: int
        :return: Ответ от модели.
        :rtype: str
        """
        try:
            messages = []
            # Добавление системной инструкции в сообщение
            if self.system_instruction or system_instruction:
                system_instruction_escaped = (system_instruction or self.system_instruction).replace('"', r'\"')
                messages.append({"role": "system", "content": system_instruction_escaped})

            # Подготовка сообщения пользователя
            message_escaped = message.replace('"', r'\"')
            messages.append({"role": "user", "content": message_escaped})

            # Отправка запроса к модели
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0,
                max_tokens=8000,
            )
            # Извлечение ответа из полученных данных
            if not response.choices:
                logger.error(f"Не получен ответ от модели {response=}")
                return ""
            reply = response.choices[0].message.content.strip()
            # Определение тональности ответа
            sentiment = self.determine_sentiment(reply)

            # Сохранение сообщений и тональности в диалог
            self.dialogue.append({"role": "system", "content": system_instruction or self.system_instruction})
            self.dialogue.append({"role": "user", "content": message_escaped})
            self.dialogue.append({"role": "assistant", "content": reply, "sentiment": sentiment})
            # Сохранение диалога
            self._save_dialogue()

            return reply
        except Exception as ex:
            logger.error(f"Произошла ошибка при отправке сообщения: \n-----\n {pprint(messages)} \n-----\n{ex}", ex, True)
            # TODO: Использовать экспоненциальный откат
            time.sleep(3)
            if attempts > 0:
                return self.ask(message, attempts - 1)
            return ""

    def describe_image(self, image_path: str | Path, prompt: Optional[str] = None, system_instruction: Optional[str] = None) -> Optional[Any]:
        """
        Отправляет изображение в OpenAI API и получает его описание.

        :param image_path: Путь к изображению.
        :type image_path: str | Path
        :param prompt: Запрос для описания изображения.
        :type prompt: Optional[str]
        :param system_instruction: Системная инструкция.
        :type system_instruction: Optional[str]
        :return: Описание изображения.
        :rtype: str
        """
        # Подготовка списка сообщений для запроса
        messages: list = []
        # Кодирование изображения в base64
        base64_image = base64encode(image_path)

        # Добавление системной инструкции, если она передана
        if system_instruction:
            messages.append({"role": "system", "content": system_instruction})

        # Добавление сообщения пользователя с изображением
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
            # Отправка запроса в OpenAI API
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0,
                max_tokens=800,
            )
            # TODO: Вынести обработку ответа в отдельную функцию
            try:
                if not response.choices:
                    logger.error(f"Не получен ответ от модели {response=}")
                    return
                # Извлечение ответа из полученных данных
                raw_reply = response.choices[0].message.content.strip()
                # Загрузка ответа из json
                return j_loads_ns(raw_reply)
            except Exception as ex:
                logger.error(f"Ошибка в ответе {response}", ex, True)
                return
        except Exception as ex:
            logger.error(f"Ошибка openai", ex, True)
            return

    def describe_image_by_requests(self, image_path: str | Path, prompt: str = None) -> None:
        """
        Отправляет изображение в OpenAI API и получает описание, используя requests.

        :param image_path: Путь к изображению.
        :type image_path: str | Path
        :param prompt: Запрос для описания изображения.
        :type prompt: str
        """
        # Получение base64 строки
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
                        {
                            "type": "image_url",
                            "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}
                        }
                    ]
                }
            ],
            "max_tokens": 300
        }
        try:
            # Отправка запроса с использованием requests
            response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
            response_json = response.json()
            ...
        except Exception as ex:
            logger.error(f"Ошибка описания изображения {image_path=}\n{ex}", ex)

    def dynamic_train(self):
        """Динамически загружает предыдущий диалог и донастраивает модель на его основе."""
        try:
            # Загрузка предыдущего диалога
            messages = j_loads(gs.path.google_drive / 'AI' / 'conversation' / 'dailogue.json')
            # Проверка наличия сообщений для обучения
            if messages:
                response = self.client.chat.completions.create(
                    model=self.model,
                    assistant=self.assistant_id,
                    messages=messages,
                    temperature=0,
                )
                logger.info("Донастройка во время разговора прошла успешно.")
            else:
                logger.info("Предыдущий диалог не найден для донастройки.")
        except Exception as ex:
            logger.error(f"Ошибка во время динамической донастройки: {ex}", ex)

    def train(self, data: str = None, data_dir: Path | str = None, data_file: Path | str = None, positive: bool = True) -> Optional[str]:
        """
        Обучает модель на указанных данных или директории.

        :param data: Строка с данными в формате CSV или путь к CSV файлу.
        :type data: Optional[str]
        :param data_dir: Каталог, содержащий CSV файлы для обучения.
        :type data_dir: Optional[Path | str]
        :param data_file: Путь к отдельному CSV файлу с данными для обучения.
        :type data_file: Optional[Path | str]
        :param positive: Являются ли данные положительными или отрицательными.
        :type positive: bool
        :return: ID задания обучения или None в случае ошибки.
        :rtype: Optional[str]
        """
        if not data_dir:
            data_dir = gs.path.google_drive / 'AI' / 'training'

        try:
            # Проверка, что передано: строка, файл или директория
            if data:
                documents = j_loads(data)
            elif data_file:
                documents = j_loads(data_file)
            elif data_dir:
                 # TODO: добавить загрузку всех файлов CSV из директории.
                documents = j_loads(data_dir)
            else:
                 logger.error("Не указаны данные для обучения")
                 return

            # Создание задания на обучение
            response = self.client.Training.create(
                model=self.model,
                documents=documents,
                labels=["positive" if positive else "negative"] * len(documents),
                show_progress=True
            )
            self.current_job_id = response.id
            return response.id
        except Exception as ex:
            logger.error("Произошла ошибка во время обучения:", ex)
            return

    def save_job_id(self, job_id: str, description: str, filename: str = "job_ids.json"):
        """
        Сохраняет ID задания с описанием в файл.

        :param job_id: ID задания.
        :type job_id: str
        :param description: Описание задания.
        :type description: str
        :param filename: Имя файла для сохранения ID заданий.
        :type filename: str
        """
        job_data = {"id": job_id, "description": description, "created": time.time()}
        job_file = gs.path.google_drive / filename

        # Проверка существования файла
        if not job_file.exists():
            # Сохранение данных в новый файл
            j_dumps([job_data], job_file)
        else:
            # Загрузка существующих данных и добавление новых
            existing_jobs = j_loads(job_file)
            existing_jobs.append(job_data)
            j_dumps(existing_jobs, job_file)

def main():
    """
    Главная функция для инициализации OpenAIModel и демонстрации использования.

        - Инициализация модели с системной инструкцией и ID ассистента.
        - Вывод доступных моделей и ассистентов.
        - Отправка сообщения модели и вывод ответа.
        - Запуск динамической донастройки модели.
        - Обучение модели на основе предоставленных данных.
        - Сохранение ID задания обучения.
        - Описание изображения с помощью модели.
    """
    # Инициализация модели с системными инструкциями и ID ассистента
    model = OpenAIModel(system_instruction="You are a helpful assistant.", assistant_id="asst_dr5AgQnhhhnef5OSMzQ9zdk9")

    # Вывод доступных моделей
    print("Available Models:")
    models = model.list_models
    pprint(models)

    # Вывод доступных ассистентов
    print("\nAvailable Assistants:")
    assistants = model.list_assistants
    pprint(assistants)

    # Пример отправки сообщения модели
    user_input = "Hello, how are you?"
    print("\nUser Input:", user_input)
    response = model.ask(user_input)
    print("Model Response:", response)

    # Пример динамической донастройки
    print("\nPerforming dynamic training...")
    model.dynamic_train()

    # Пример обучения модели
    print("\nTraining the model...")
    training_result = model.train(data_file=gs.path.google_drive / 'AI' / 'training_data.csv')
    print(f"Training job ID: {training_result}")

    # Пример сохранения ID задания
    if training_result:
        model.save_job_id(training_result, "Training model with new data", filename="job_ids.json")
        print(f"Saved training job ID: {training_result}")

    # Пример описания изображения
    image_path = gs.path.google_drive / 'images' / 'example_image.jpg'
    print("\nDescribing Image:")
    description = model.describe_image(image_path)
    print(f"Image description: {description}")


if __name__ == "__main__":
    main()
```