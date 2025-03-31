# Модуль `training.py`

## Обзор

Модуль `training.py` предоставляет класс `OpenAIModel` для взаимодействия с API OpenAI, управления моделями и их обучения. Он включает функциональность для отправки сообщений, анализа тональности, динамической донастройки и обучения моделей на основе предоставленных данных. Модуль также поддерживает описание изображений с использованием API OpenAI.

## Подробней

Этот модуль предназначен для упрощения взаимодействия с OpenAI API в рамках проекта `hypotez`. Он предоставляет удобные методы для выполнения различных задач, таких как:

- Инициализация и настройка моделей OpenAI.
- Получение списка доступных моделей и ассистентов.
- Отправка сообщений и получение ответов от моделей.
- Анализ тональности ответов.
- Динамическая донастройка моделей на основе истории диалогов.
- Обучение моделей с использованием предоставленных данных.
- Описание изображений с использованием мультимодальных моделей.

Класс `OpenAIModel` инкапсулирует всю необходимую логику для работы с OpenAI API, что позволяет легко интегрировать функциональность OpenAI в другие части проекта `hypotez`.

## Классы

### `OpenAIModel`

**Описание**: Класс для взаимодействия с OpenAI API и управления моделями.

**Методы**:

- `__init__`: Инициализирует объект `OpenAIModel` с ключом API, идентификатором ассистента и загружает доступные модели и ассистентов.
- `list_models`: Динамически получает и возвращает доступные модели из OpenAI API.
- `list_assistants`: Динамически загружает доступных ассистентов из JSON-файла.
- `set_assistant`: Устанавливает ассистента, используя предоставленный идентификатор ассистента.
- `_save_dialogue`: Сохраняет весь диалог в JSON-файл.
- `determine_sentiment`: Определяет тональность сообщения (положительную, отрицательную или нейтральную).
- `ask`: Отправляет сообщение модели и возвращает ответ вместе с анализом тональности.
- `describe_image`: Описывает изображение, используя API OpenAI.
- `describe_image_by_requests`: Отправляет изображение в OpenAI API и получает описание.
- `dynamic_train`: Динамически загружает предыдущий диалог и донастраивает модель на его основе.
- `train`: Обучает модель на указанных данных или в каталоге.
- `save_job_id`: Сохраняет идентификатор задания с описанием в файл.

**Параметры**:

- `api_key` (str): Ключ API OpenAI.
- `system_instruction` (str, optional): Системная инструкция для модели. По умолчанию `None`.
- `model_name` (str, optional): Имя модели. По умолчанию `'gpt-4o-mini'`.
- `assistant_id` (str, optional): Идентификатор ассистента. По умолчанию `None`.

**Примеры**

```python
from src.ai.openai.model.training import OpenAIModel

# Инициализация модели
model = OpenAIModel(api_key='YOUR_API_KEY', system_instruction='You are a helpful assistant.')

# Получение списка доступных моделей
models = model.list_models

# Получение списка доступных ассистентов
assistants = model.list_assistants

# Отправка сообщения модели
response = model.ask('Hello, how are you?')

# Обучение модели
training_result = model.train(data_file='training_data.csv')
```

## Функции

### `main`

```python
def main():
    """Main function to initialize the OpenAIModel and demonstrate usage.
    Explanation:
        Initialization of the Model:

        The OpenAIModel is initialized with a system instruction and an assistant ID. You can modify the parameters if necessary.
        Listing Models and Assistants:

        The list_models and list_assistants methods are called to print the available models and assistants.
        Asking the Model a Question:

        The ask() method is used to send a message to the model and retrieve its response.
        Dynamic Training:

        The dynamic_train() method performs dynamic fine-tuning based on past dialogue.
        Training the Model:

        The train() method trains the model using data from a specified file (in this case, 'training_data.csv').
        Saving the Training Job ID:

        After training, the job ID is saved with a description to a JSON file."""
    ...
```

**Описание**: Главная функция для инициализации `OpenAIModel` и демонстрации использования.

**Параметры**:

- Нет параметров.

**Возвращает**:

- Нет возвращаемого значения.

**Вызывает исключения**:

- Не вызывает исключений напрямую, но может генерировать исключения при взаимодействии с OpenAI API.

**Примеры**:

```python
from src.ai.openai.model.training import main

# Вызов главной функции
main()