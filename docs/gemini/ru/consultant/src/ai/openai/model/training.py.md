# Анализ кода модуля `training.py`

**Качество кода**
8
-  Плюсы
    - Код хорошо структурирован, с разделением на классы и методы, что обеспечивает его модульность.
    - Используется logging для отслеживания ошибок и событий.
    - Присутствует обработка исключений.
    - Документация в формате docstring присутствует для основных классов и методов.
    - Используются константы для модели `gpt-4o-mini`.
    - Код использует `j_loads`, `j_loads_ns`, `j_dumps` для работы с `json`.
-  Минусы
    - Отсутствует reStructuredText (RST) для docstring.
    - Некоторые docstring нуждаются в улучшении (отсутствуют описания аргументов и возвращаемых значений).
    - Используются стандартные блоки `try-except` вместо `logger.error` в некоторых местах.
    - Не всегда применяется форматирование строк с использованием f-строк.
    - Не хватает описания модуля в начале файла.
    - Не все ошибки логируются с трассировкой стека.
    - Не везде используются константы, например, для `model="gpt-4o"`.
    - Потенциально избыточное использование `pprint` в `logger.debug`.

**Рекомендации по улучшению**

1.  **Документация**:
    -   Переписать все docstring в формате reStructuredText (RST), включая описание параметров и возвращаемых значений.
    -   Добавить описание модуля в начале файла.
2.  **Логирование**:
    -   Использовать `logger.error(message, exc_info=True)` для логирования ошибок с трассировкой стека.
    -   Избегать дублирования логирования ошибок с помощью `try-except`.
    -   Удалить `pprint` из логирования ошибок и использовать f-строки для форматирования.
3.  **Обработка данных**:
    -   Убедиться, что везде используются `j_loads` и `j_loads_ns` для загрузки JSON данных.
4.  **Структура кода**:
    -   Разделить длинные функции на более мелкие, чтобы улучшить читаемость.
    -   Использовать константы для `model = "gpt-4o"` и других общих строк.
    -   Использовать более информативные имена переменных.
5.  **Общее**:
    -   Удалить неиспользуемые импорты.
    -   Форматировать код в соответствии с PEP8.

**Оптимизированный код**

```python
"""
Модуль для работы с моделями OpenAI
=========================================================================================

Этот модуль содержит класс :class:`OpenAIModel`, который используется для взаимодействия с API OpenAI
и управления моделями, ассистентами и их обучением.

Пример использования
--------------------

Пример использования класса `OpenAIModel`:

.. code-block:: python

    model = OpenAIModel(system_instruction='You are a helpful assistant.', assistant_id='asst_dr5AgQnhhhnef5OSMzQ9zdk9')
    models = model.list_models
    response = model.ask('Hello, how are you?')
"""
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
from src.utils.convertors.md2dict import md2dict
from src.logger.logger import logger

MODE = 'dev'
MODEL_NAME = "gpt-4o-mini"
GPT_4o = "gpt-4o"

class OpenAIModel:
    """
    Класс для взаимодействия с API OpenAI и управления моделями.

    :param system_instruction: Инструкция для системы (по умолчанию None).
    :type system_instruction: str, optional
    :param model_name: Имя модели для использования (по умолчанию 'gpt-4o-mini').
    :type model_name: str, optional
    :param assistant_id: ID ассистента (по умолчанию None).
    :type assistant_id: str, optional
    """

    model: str = MODEL_NAME
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

    def __init__(self, system_instruction: str = None, model_name:str = MODEL_NAME, assistant_id: str = None):
        """
        Инициализация объекта Model с API ключом, ID ассистента и загрузка доступных моделей и ассистентов.

        :param system_instruction: Инструкция для системы (по умолчанию None).
        :type system_instruction: str, optional
        :param model_name: Имя модели для использования (по умолчанию 'gpt-4o-mini').
        :type model_name: str, optional
        :param assistant_id: ID ассистента (по умолчанию None).
        :type assistant_id: str, optional
        """
        self.client = OpenAI(api_key=gs.credentials.openai.api_key)
        self.current_job_id = None
        self.assistant_id = assistant_id or gs.credentials.openai.assistant_id.code_assistant
        self.system_instruction = system_instruction

        # Загрузка ассистента и треда во время инициализации
        try:
            self.assistant = self.client.beta.assistants.retrieve(self.assistant_id)
            self.thread = self.client.beta.threads.create()
        except Exception as ex:
            logger.error(f"Ошибка инициализации ассистента или треда: {ex}", exc_info=True)

    @property
    def list_models(self) -> List[str]:
        """
        Динамически получает и возвращает доступные модели из API OpenAI.

        :return: Список ID моделей, доступных через API OpenAI.
        :rtype: List[str]
        """
        try:
            models = self.client.models.list()
            model_list = [model['id'] for model in models['data']]
            logger.info(f"Загружены модели: {model_list}")
            return model_list
        except Exception as ex:
            logger.error(f"Произошла ошибка при загрузке моделей: {ex}", exc_info=True)
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
            logger.info(f"Загружены ассистенты: {assistant_list}")
            return assistant_list
        except Exception as ex:
            logger.error(f"Произошла ошибка при загрузке ассистентов: {ex}", exc_info=True)
            return []

    def set_assistant(self, assistant_id: str):
        """
        Устанавливает ассистента, используя предоставленный ID.

        :param assistant_id: ID ассистента для установки.
        :type assistant_id: str
        """
        try:
            self.assistant_id = assistant_id
            self.assistant = self.client.beta.assistants.retrieve(assistant_id)
            logger.info(f"Ассистент успешно установлен: {assistant_id}")
        except Exception as ex:
            logger.error(f"Произошла ошибка при установке ассистента: {ex}", exc_info=True)

    def _save_dialogue(self):
        """Сохраняет весь диалог в JSON файл."""
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

        if any(word in message_lower for word in positive_words):
            return "positive"
        elif any(word in message_lower for word in negative_words):
            return "negative"
        elif any(word in message_lower for word in neutral_words):
            return "neutral"
        else:
            return "neutral"

    def ask(self, message: str, system_instruction: str = None, attempts: int = 3) -> Optional[str]:
        """
        Отправляет сообщение модели и возвращает ответ вместе с анализом тональности.

        :param message: Сообщение для отправки модели.
        :type message: str
        :param system_instruction: Опциональная инструкция для системы (по умолчанию None).
        :type system_instruction: str, optional
        :param attempts: Количество попыток (по умолчанию 3).
        :type attempts: int, optional
        :return: Ответ от модели или None в случае ошибки.
        :rtype: str, optional
        """
        try:
            messages = []
            if self.system_instruction or system_instruction:
                system_instruction_escaped = (system_instruction or self.system_instruction).replace('"', r'\"')
                messages.append({"role": "system", "content": system_instruction_escaped})

            message_escaped = message.replace('"', r'\"')
            messages.append({"role": "user", "content": message_escaped})

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
            self.dialogue.append({"role": "system", "content": system_instruction or self.system_instruction})
            self.dialogue.append({"role": "user", "content": message_escaped})
            self.dialogue.append({"role": "assistant", "content": reply, "sentiment": sentiment})

            # Сохранение диалога
            self._save_dialogue()

            return reply
        except Exception as ex:
            logger.error(f"Произошла ошибка при отправке сообщения: \n-----\n {messages} \n-----\n", exc_info=True)
            time.sleep(3)
            if attempts > 0:
                return self.ask(message, system_instruction, attempts - 1)
            return None

    def describe_image(self, image_path: str | Path, prompt:Optional[str] = None, system_instruction:Optional[str] = None ) -> Optional[str]:
        """
        Отправляет изображение в OpenAI API и получает описание.

        :param image_path: Путь к изображению.
        :type image_path: str | Path
        :param prompt: Подсказка для описания изображения (по умолчанию None).
        :type prompt: str, optional
        :param system_instruction: Инструкция для системы (по умолчанию None).
        :type system_instruction: str, optional
        :return: Описание изображения или None в случае ошибки.
        :rtype: str, optional
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
            
            try:
                raw_reply = response.choices[0].message.content.strip()
                return j_loads_ns(raw_reply)
            except Exception as ex:
                logger.error(f"Проблема в ответе {response}", exc_info=True)
                return None

        except Exception as ex:
            logger.error(f"Ошибка openai: {ex}", exc_info=True)
            return None


    def describe_image_by_requests(self, image_path: str | Path, prompt:str = None) -> None:
        """
        Отправляет изображение в OpenAI API и получает описание с использованием requests.

        :param image_path: Путь к изображению.
        :type image_path: str | Path
        :param prompt: Подсказка для описания изображения (по умолчанию None).
        :type prompt: str, optional
        """
        # Получение base64 строки
        base64_image = base64encode(image_path)

        headers = {
          "Content-Type": "application/json",
          "Authorization": f"Bearer {gs.credentials.openai.project_api}"
        }

        payload = {
          "model": GPT_4o,
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
            response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
            response_json = response.json()
        except Exception as ex:
            logger.error(f"Ошибка в описании изображения {image_path=}\n{ex}", exc_info=True)

    def dynamic_train(self):
        """Динамически загружает предыдущий диалог и дообучает модель на его основе."""
        try:
            messages = j_loads(gs.path.google_drive / 'AI' / 'conversation' / 'dailogue.json')

            if messages:
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=messages,
                    temperature=0,
                )
                logger.info("Дообучение во время разговора прошло успешно.")
            else:
                logger.info("Предыдущий диалог не найден для дообучения.")
        except Exception as ex:
            logger.error(f"Ошибка во время динамического дообучения: {ex}", exc_info=True)

    def train(self, data: str = None, data_dir: Path | str = None, data_file: Path | str = None, positive: bool = True) -> Optional[str]:
        """
        Обучает модель на указанных данных или директории.

        :param data: Путь к CSV файлу или CSV-форматированная строка с данными (по умолчанию None).
        :type data: str, optional
        :param data_dir: Директория, содержащая CSV файлы для обучения (по умолчанию None).
        :type data_dir: Path | str, optional
        :param data_file: Путь к отдельному CSV файлу с обучающими данными (по умолчанию None).
        :type data_file: Path | str, optional
        :param positive: Указывает, являются ли данные позитивными или негативными (по умолчанию True).
        :type positive: bool, optional
        :return: ID задания обучения или None в случае ошибки.
        :rtype: str, optional
        """
        if not data_dir:
            data_dir = gs.path.google_drive / 'AI' / 'training'

        try:
            documents = j_loads(data if data else data_file if data_file else data_dir)

            response = self.client.beta.training.create(
                model=self.model,
                documents=documents,
                labels=["positive" if positive else "negative"] * len(documents),
                show_progress=True
            )
            self.current_job_id = response.id
            return response.id

        except Exception as ex:
            logger.error(f"Произошла ошибка во время обучения: {ex}", exc_info=True)
            return None

    def save_job_id(self, job_id: str, description: str, filename: str = "job_ids.json"):
        """
        Сохраняет ID задания с описанием в файл.

        :param job_id: ID задания для сохранения.
        :type job_id: str
        :param description: Описание задания.
        :type description: str
        :param filename: Имя файла для сохранения ID заданий (по умолчанию "job_ids.json").
        :type filename: str, optional
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

        OpenAIModel инициализируется с инструкцией системы и ID ассистента. Можно изменить параметры по мере необходимости.
        Список моделей и ассистентов:

        Методы list_models и list_assistants вызываются для вывода доступных моделей и ассистентов.
        Запрос модели:

        Метод ask() используется для отправки сообщения модели и получения ответа.
        Динамическое обучение:

        Метод dynamic_train() выполняет динамическое дообучение на основе прошлого диалога.
        Обучение модели:

        Метод train() обучает модель, используя данные из указанного файла ('training_data.csv').
        Сохранение ID задания обучения:

        После обучения ID задания сохраняется с описанием в JSON файл.
    """
    # Инициализация модели с инструкцией системы и ID ассистента (опционально)
    model = OpenAIModel(system_instruction="You are a helpful assistant.", assistant_id="asst_dr5AgQnhhhnef5OSMzQ9zdk9")

    # Пример вывода доступных моделей
    print("Available Models:")
    models = model.list_models
    pprint(models)

    # Пример вывода доступных ассистентов
    print("\nAvailable Assistants:")
    assistants = model.list_assistants
    pprint(assistants)

    # Пример запроса модели
    user_input = "Hello, how are you?"
    print("\nUser Input:", user_input)
    response = model.ask(user_input)
    print("Model Response:", response)

    # Пример динамического обучения с использованием прошлых диалогов
    print("\nPerforming dynamic training...")
    model.dynamic_train()

    # Пример обучения модели с использованием предоставленных данных
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