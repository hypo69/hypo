# Модуль `training.py`

## Обзор

Модуль `training.py` предоставляет класс `OpenAIModel` для взаимодействия с API OpenAI, управления моделями и их обучения. Он включает в себя функции для отправки сообщений, анализа тональности, обучения моделей, а также управления ассистентами и диалогами.

## Оглавление

1. [Классы](#классы)
   - [`OpenAIModel`](#openai-model)
2. [Функции](#функции)
   - [`main`](#main)

## Классы

### `OpenAIModel`

**Описание**: Класс для взаимодействия с API OpenAI, управления моделями и их обучения.

**Методы**:

- `__init__`: Инициализирует объект `OpenAIModel` с ключом API, ID ассистента и загружает доступные модели и ассистентов.
- `list_models`: Возвращает список доступных моделей из API OpenAI.
- `list_assistants`: Возвращает список доступных ассистентов из JSON-файла.
- `set_assistant`: Устанавливает ассистента, используя предоставленный ID.
- `_save_dialogue`: Сохраняет весь диалог в JSON-файл.
- `determine_sentiment`: Определяет тональность сообщения (положительная, отрицательная или нейтральная).
- `ask`: Отправляет сообщение модели и возвращает ответ с анализом тональности.
- `describe_image`: Отправляет изображение модели для получения описания.
- `describe_image_by_requests`: Отправляет изображение модели для получения описания используя `requests`.
- `dynamic_train`: Динамически загружает предыдущий диалог и настраивает модель на его основе.
- `train`: Обучает модель на указанных данных.
- `save_job_id`: Сохраняет ID задания с описанием в файл.

#### `__init__`
```python
def __init__(self, system_instruction: str = None, model_name:str = 'gpt-4o-mini', assistant_id: str = None)
```

**Описание**: Инициализирует объект `OpenAIModel` с ключом API, ID ассистента и загружает доступные модели и ассистентов.

**Параметры**:
- `system_instruction` (str, optional): Системная инструкция для модели. По умолчанию `None`.
- `model_name` (str, optional): Имя модели. По умолчанию `gpt-4o-mini`.
- `assistant_id` (str, optional): ID ассистента. По умолчанию `None`.

#### `list_models`
```python
@property
def list_models(self) -> List[str]:
```
**Описание**: Динамически получает и возвращает доступные модели из API OpenAI.

**Возвращает**:
- `List[str]`: Список ID доступных моделей.

**Вызывает исключения**:
- `Exception`: В случае ошибки при загрузке моделей.

#### `list_assistants`
```python
@property
def list_assistants(self) -> List[str]:
```

**Описание**: Загружает доступных ассистентов из JSON-файла.

**Возвращает**:
- `List[str]`: Список имен ассистентов.

**Вызывает исключения**:
- `Exception`: В случае ошибки при загрузке ассистентов.

#### `set_assistant`
```python
def set_assistant(self, assistant_id: str)
```

**Описание**: Устанавливает ассистента, используя предоставленный ID.

**Параметры**:
- `assistant_id` (str): ID ассистента для установки.

**Вызывает исключения**:
- `Exception`: В случае ошибки при установке ассистента.

#### `_save_dialogue`
```python
def _save_dialogue(self)
```
**Описание**: Сохраняет весь диалог в JSON-файл.

#### `determine_sentiment`
```python
def determine_sentiment(self, message: str) -> str
```

**Описание**: Определяет тональность сообщения (положительная, отрицательная или нейтральная).

**Параметры**:
- `message` (str): Сообщение для анализа.

**Возвращает**:
- `str`: Тональность ('positive', 'negative' или 'neutral').

#### `ask`
```python
def ask(self, message: str, system_instruction: str = None, attempts: int = 3) -> str
```

**Описание**: Отправляет сообщение модели и возвращает ответ с анализом тональности.

**Параметры**:
- `message` (str): Сообщение для отправки модели.
- `system_instruction` (str, optional): Системная инструкция. По умолчанию `None`.
- `attempts` (int, optional): Количество попыток отправки. По умолчанию `3`.

**Возвращает**:
- `str`: Ответ от модели.

**Вызывает исключения**:
- `Exception`: В случае ошибки при отправке сообщения.

#### `describe_image`
```python
def describe_image(self, image_path: str | Path, prompt:Optional[str] = None, system_instruction:Optional[str] = None ) -> str
```

**Описание**: Отправляет изображение модели для получения описания.

**Параметры**:
- `image_path` (str | Path): Путь к изображению.
- `prompt` (Optional[str], optional):  Запрос для модели. По умолчанию `None`.
- `system_instruction` (Optional[str], optional):  Системная инструкция для модели. По умолчанию `None`.
**Возвращает**:
- `str`: Описание изображения.

**Вызывает исключения**:
- `Exception`: В случае ошибки при обработке изображения.

#### `describe_image_by_requests`
```python
def describe_image_by_requests(self, image_path: str | Path, prompt:str = None) -> str
```

**Описание**: Отправляет изображение модели для получения описания используя `requests`.

**Параметры**:
- `image_path` (str | Path): Путь к изображению.
- `prompt` (str, optional): Запрос для модели. По умолчанию `None`.

**Вызывает исключения**:
- `Exception`: В случае ошибки при запросе описания изображения.

#### `dynamic_train`
```python
def dynamic_train(self)
```

**Описание**: Динамически загружает предыдущий диалог и настраивает модель на его основе.

**Вызывает исключения**:
- `Exception`: В случае ошибки во время динамической настройки.

#### `train`
```python
def train(self, data: str = None, data_dir: Path | str = None, data_file: Path | str = None, positive: bool = True) -> str | None
```

**Описание**: Обучает модель на указанных данных.

**Параметры**:
- `data` (str, optional): Путь к CSV-файлу или CSV-форматированная строка с данными. По умолчанию `None`.
- `data_dir` (Path | str, optional): Директория с CSV-файлами для обучения. По умолчанию `None`.
- `data_file` (Path | str, optional): Путь к CSV-файлу с данными. По умолчанию `None`.
- `positive` (bool, optional): Указывает, являются ли данные положительными. По умолчанию `True`.

**Возвращает**:
- `str | None`: ID задания обучения или `None` при ошибке.

**Вызывает исключения**:
- `Exception`: В случае ошибки во время обучения.

#### `save_job_id`
```python
def save_job_id(self, job_id: str, description: str, filename: str = "job_ids.json")
```
**Описание**: Сохраняет ID задания с описанием в файл.

**Параметры**:
- `job_id` (str): ID задания для сохранения.
- `description` (str): Описание задания.
- `filename` (str, optional): Имя файла для сохранения. По умолчанию "job_ids.json".

## Функции

### `main`
```python
def main()
```
**Описание**: Основная функция для инициализации `OpenAIModel` и демонстрации его использования.

**Объяснение**:
- Инициализация модели `OpenAIModel` с системной инструкцией и ID ассистента.
- Вывод списка доступных моделей и ассистентов.
- Запрос модели с использованием метода `ask()`.
- Динамическая настройка модели с помощью `dynamic_train()`.
- Обучение модели с помощью `train()`.
- Сохранение ID задания обучения с помощью `save_job_id()`.
- Пример описания изображения.