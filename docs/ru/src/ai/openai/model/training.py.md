# Модуль для работы с OpenAI Model для обучения моделей
=========================================================

Модуль содержит класс :class:`OpenAIModel`, который используется для взаимодействия с OpenAI API и управления моделью.

Пример использования
----------------------

```python
>>> model = OpenAIModel(api_key="YOUR_API_KEY", system_instruction="You are a helpful assistant.")
>>> response = model.ask("Hello, how are you?")
```

## Оглавление

- [Обзор](#обзор)
- [Подробнее](#подробнее)
- [Классы](#классы)
    - [`OpenAIModel`](#openaimodel)
- [Функции](#функции)
    - [`main`](#main)

## Обзор

Модуль `training.py` предоставляет класс `OpenAIModel` для взаимодействия с OpenAI API. Он включает в себя функции для обучения моделей, получения списка доступных моделей и ассистентов, а также для отправки сообщений модели и получения ответов. Модуль также содержит функцию `main` для демонстрации использования класса `OpenAIModel`.

## Подробнее

Этот модуль является частью проекта `hypotez` и предназначен для упрощения взаимодействия с OpenAI API. Он предоставляет удобный интерфейс для обучения моделей, получения списка доступных моделей и ассистентов, а также для отправки сообщений модели и получения ответов. Он также содержит функцию `main` для демонстрации использования класса `OpenAIModel`.
Модуль использует модуль `logger` из `src.logger.logger` для логгирования.

## Классы

### `OpenAIModel`

**Описание**: Класс для взаимодействия с OpenAI API и управления моделью.

**Принцип работы**:
Класс `OpenAIModel` инициализируется с API-ключом, системной инструкцией и идентификатором ассистента. Он предоставляет методы для получения списка доступных моделей и ассистентов, установки ассистента, сохранения диалога, определения тональности сообщения, отправки сообщения модели и получения ответа, динамического обучения модели на основе предыдущего диалога, обучения модели на указанных данных или каталоге, сохранения идентификатора задания и описания.

**Атрибуты**:

- `model` (str): Название используемой модели. По умолчанию "gpt-4o-mini".
- `client` (OpenAI): Клиент OpenAI API.
- `current_job_id` (str): Идентификатор текущего задания.
- `assistant_id` (str): Идентификатор ассистента.
- `assistant` (Any): Объект ассистента.
- `thread` (Any): Объект треда.
- `system_instruction` (str): Системная инструкция для модели.
- `dialogue_log_path` (str | Path): Путь к файлу журнала диалога.
- `dialogue` (List[Dict[str, str]]): Список диалогов.
- `assistants` (List[SimpleNamespace]): Список ассистентов.
- `models_list` (List[str]): Список моделей.

**Методы**:

- [`__init__`](#__init__): Инициализирует объект `OpenAIModel` с API-ключом, системной инструкцией и идентификатором ассистента.
- [`list_models`](#list_models): Возвращает список доступных моделей из OpenAI API.
- [`list_assistants`](#list_assistants): Возвращает список доступных ассистентов из JSON файла.
- [`set_assistant`](#set_assistant): Устанавливает ассистента, используя предоставленный идентификатор ассистента.
- [`_save_dialogue`](#_save_dialogue): Сохраняет весь диалог в JSON файл.
- [`determine_sentiment`](#determine_sentiment): Определяет тональность сообщения (положительную, отрицательную или нейтральную).
- [`ask`](#ask): Отправляет сообщение модели и возвращает ответ вместе с анализом тональности.
- [`describe_image`](#describe_image): Описывает изображение, отправляя его в OpenAI API.
- [`describe_image_by_requests`](#describe_image_by_requests): Отправляет изображение в OpenAI API и получает описание, используя requests.
- [`dynamic_train`](#dynamic_train): Динамически загружает предыдущий диалог и дообучает модель на его основе.
- [`train`](#train): Обучает модель на указанных данных или каталоге.
- [`save_job_id`](#save_job_id): Сохраняет идентификатор задания с описанием в файл.

### `__init__`

```python
def __init__(self, api_key:str, system_instruction: str = None, model_name:str = 'gpt-4o-mini', assistant_id: str = None):
```

**Назначение**: Инициализирует объект `OpenAIModel` с API-ключом, системной инструкцией и идентификатором ассистента.

**Параметры**:
- `api_key` (str): Ключ API для OpenAI.
- `system_instruction` (str, optional): Системная инструкция для модели. По умолчанию `None`.
- `model_name` (str, optional): Имя модели для использования. По умолчанию `'gpt-4o-mini'`.
- `assistant_id` (str, optional): Идентификатор ассистента. По умолчанию `None`.

**Как работает функция**:

1. Инициализирует клиент OpenAI API с использованием предоставленного API-ключа или API-ключа из `gs.credentials.openai.api_key`.
2. Устанавливает `current_job_id` в `None`.
3. Устанавливает `assistant_id` с использованием предоставленного идентификатора ассистента или значения по умолчанию из `gs.credentials.openai.assistant_id.code_assistant`.
4. Устанавливает `system_instruction` с использованием предоставленной системной инструкции.
5. Загружает ассистента и создает тред с использованием OpenAI API.

```
Инициализация OpenAI API клиента --> Установка параметров (current_job_id, assistant_id, system_instruction) --> Загрузка ассистента и создание треда
```

### `list_models`

```python
@property
def list_models(self) -> List[str]:
```

**Назначение**: Динамически получает и возвращает доступные модели из OpenAI API.

**Возвращает**:
- `List[str]`: Список идентификаторов моделей, доступных через OpenAI API.

**Вызывает исключения**:
- `Exception`: Возникает, если происходит ошибка во время загрузки моделей.

**Как работает функция**:

1. Пытается получить список моделей из OpenAI API с использованием `self.client.models.list()`.
2. Извлекает идентификаторы моделей из ответа API и сохраняет их в списке `model_list`.
3. Логирует список загруженных моделей с использованием `logger.info()`.
4. В случае возникновения ошибки логирует ошибку с использованием `logger.error()` и возвращает пустой список.

```
Получение списка моделей из OpenAI API --> Извлечение идентификаторов моделей --> Логирование списка моделей
```

**Примеры**:

```python
model = OpenAIModel(api_key="YOUR_API_KEY")
models = model.list_models
print(models)
```

### `list_assistants`

```python
@property
def list_assistants(self) -> List[str]:
```

**Назначение**: Динамически загружает доступных ассистентов из JSON-файла.

**Возвращает**:
- `List[str]`: Список имен ассистентов.

**Вызывает исключения**:
- `Exception`: Возникает, если происходит ошибка во время загрузки ассистентов.

**Как работает функция**:

1. Пытается загрузить список ассистентов из JSON-файла с использованием `j_loads_ns()`.
2. Извлекает имена ассистентов из загруженного списка и сохраняет их в списке `assistant_list`.
3. Логирует список загруженных ассистентов с использованием `logger.info()`.
4. В случае возникновения ошибки логирует ошибку с использованием `logger.error()` и возвращает пустой список.

```
Загрузка списка ассистентов из JSON-файла --> Извлечение имен ассистентов --> Логирование списка ассистентов
```

**Примеры**:

```python
model = OpenAIModel(api_key="YOUR_API_KEY")
assistants = model.list_assistants
print(assistants)
```

### `set_assistant`

```python
def set_assistant(self, assistant_id: str):
```

**Назначение**: Устанавливает ассистента, используя предоставленный идентификатор ассистента.

**Параметры**:
- `assistant_id` (str): Идентификатор ассистента для установки.

**Вызывает исключения**:
- `Exception`: Возникает, если происходит ошибка во время установки ассистента.

**Как работает функция**:

1. Устанавливает `self.assistant_id` с использованием предоставленного идентификатора ассистента.
2. Получает ассистента из OpenAI API с использованием `self.client.beta.assistants.retrieve(assistant_id)`.
3. Логирует успешную установку ассистента с использованием `logger.info()`.
4. В случае возникновения ошибки логирует ошибку с использованием `logger.error()`.

```
Установка assistant_id --> Получение ассистента из OpenAI API --> Логирование успешной установки ассистента
```

**Примеры**:

```python
model = OpenAIModel(api_key="YOUR_API_KEY")
model.set_assistant("asst_...")
```

### `_save_dialogue`

```python
def _save_dialogue(self):
```

**Назначение**: Сохраняет весь диалог в JSON-файл.

**Как работает функция**:

1. Сохраняет весь диалог (`self.dialogue`) в JSON-файл, указанный в `self.dialogue_log_path`, используя `j_dumps()`.

```
Сохранение диалога в JSON-файл
```

### `determine_sentiment`

```python
def determine_sentiment(self, message: str) -> str:
```

**Назначение**: Определяет тональность сообщения (положительную, отрицательную или нейтральную).

**Параметры**:
- `message` (str): Сообщение для анализа.

**Возвращает**:
- `str`: Тональность сообщения ('positive', 'negative' или 'neutral').

**Как работает функция**:

1. Преобразует сообщение в нижний регистр.
2. Проверяет наличие положительных слов в сообщении. Если есть, возвращает "positive".
3. Проверяет наличие отрицательных слов в сообщении. Если есть, возвращает "negative".
4. Проверяет наличие нейтральных слов в сообщении. Если есть, возвращает "neutral".
5. Если ни одно из вышеперечисленных условий не выполнено, возвращает "neutral".

```
Преобразование сообщения в нижний регистр --> Проверка наличия положительных слов --> Проверка наличия отрицательных слов --> Проверка наличия нейтральных слов --> Возврат тональности
```

**Примеры**:

```python
model = OpenAIModel(api_key="YOUR_API_KEY")
sentiment = model.determine_sentiment("This is a great product!")
print(sentiment)  # Вывод: positive
```

### `ask`

```python
def ask(self, message: str, system_instruction: str = None, attempts: int = 3) -> str:
```

**Назначение**: Отправляет сообщение модели и возвращает ответ вместе с анализом тональности.

**Параметры**:
- `message` (str): Сообщение для отправки модели.
- `system_instruction` (str, optional): Системная инструкция для модели. По умолчанию `None`.
- `attempts` (int, optional): Количество попыток повтора отправки сообщения. По умолчанию 3.

**Возвращает**:
- `str`: Ответ от модели.

**Вызывает исключения**:
- `Exception`: Возникает, если происходит ошибка во время отправки сообщения.

**Как работает функция**:

1. Создает список сообщений `messages`.
2. Если предоставлена системная инструкция или уже есть `self.system_instruction`, добавляет системное сообщение в список `messages`.
3. Добавляет сообщение пользователя в список `messages`.
4. Отправляет запрос к модели с использованием `self.client.chat.completions.create()`.
5. Извлекает ответ из ответа модели.
6. Определяет тональность ответа с использованием `self.determine_sentiment()`.
7. Добавляет системное сообщение, сообщение пользователя и ответ модели в диалог `self.dialogue`.
8. Сохраняет диалог с использованием `self._save_dialogue()`.
9. В случае возникновения ошибки логирует ошибку с использованием `logger.debug()` и повторяет попытку отправки сообщения, если количество попыток `attempts` больше 0.

```
Создание списка сообщений --> Добавление системного сообщения (если есть) --> Добавление сообщения пользователя --> Отправка запроса к модели --> Извлечение ответа --> Определение тональности ответа --> Добавление сообщений в диалог --> Сохранение диалога
```

**Примеры**:

```python
model = OpenAIModel(api_key="YOUR_API_KEY", system_instruction="You are a helpful assistant.")
response = model.ask("Hello, how are you?")
print(response)
```

### `describe_image`

```python
def describe_image(self, image_path: str | Path, prompt:Optional[str] = None, system_instruction:Optional[str] = None ) -> str:
```

**Назначение**: <Описание назначения функции: Запрос описания изображения у модели OpenAI.>

**Параметры**:
- `image_path` (str | Path): Путь к файлу изображения.
- `prompt` (Optional[str], optional): Текст запроса для описания изображения. По умолчанию `None`.
- `system_instruction` (Optional[str], optional): Системная инструкция для модели. По умолчанию `None`.

**Возвращает**:
- `str`: <Описание возвращаемого значения, которое модель предоставляет для данного изображения.>

**Как работает функция**:

1.  <Шаг 1: Инициализация списка сообщений для запроса.>
2.  <Шаг 2: Кодирование изображения в формат base64 для передачи в API.>
3.  <Шаг 3: Добавление системной инструкции в список сообщений, если она предоставлена.>
4.  <Шаг 4: Формирование сообщения пользователя с текстом запроса и закодированным изображением.>
5.  <Шаг 5: Отправка запроса в OpenAI API для получения описания изображения.>
6.  <Шаг 6: Обработка ответа от API и извлечение текстового описания изображения.>
7.  <Шаг 7: Логирование ошибок в случае неуспешного запроса или обработки ответа.>

```
Инициализация списка сообщений -> Кодирование изображения в base64 -> Добавление системной инструкции (если есть) -> Формирование сообщения пользователя с изображением -> Отправка запроса в OpenAI API -> Обработка ответа и извлечение описания -> Логирование ошибок
```

### `describe_image_by_requests`

```python
def describe_image_by_requests(self, image_path: str | Path, prompt:str = None) -> str:
```

**Назначение**: Отправляет изображение в OpenAI API и получает описание, используя requests.

**Параметры**:
- `image_path` (str | Path): Путь к файлу изображения.
- `prompt` (str, optional): Текст запроса для описания изображения. По умолчанию `None`.

**Как работает функция**:

1. Кодирует изображение в base64 формат.
2. Устанавливает заголовки для запроса, включая Content-Type и Authorization.
3. Формирует JSON payload с моделью, сообщением пользователя (содержащим текст запроса и закодированное изображение) и максимальным количеством токенов.
4. Отправляет POST запрос к OpenAI API с использованием библиотеки requests.
5. Обрабатывает ответ от API.
6. Логирует ошибки в случае неуспешного запроса.

```
Кодирование изображения в base64 --> Установка заголовков запроса --> Формирование JSON payload --> Отправка POST запроса к OpenAI API --> Обработка ответа --> Логирование ошибок
```

### `dynamic_train`

```python
def dynamic_train(self):
```

**Назначение**: Динамически загружает предыдущий диалог и дообучает модель на его основе.

**Как работает функция**:

1. Пытается загрузить предыдущий диалог из JSON-файла с использованием `j_loads()`.
2. Если диалог найден, отправляет запрос к OpenAI API для дообучения модели на основе диалога.
3. Логирует успешное дообучение модели или отсутствие предыдущего диалога.
4. В случае возникновения ошибки логирует ошибку.

```
Загрузка предыдущего диалога --> Отправка запроса к OpenAI API для дообучения модели --> Логирование результата
```

### `train`

```python
def train(self, data: str = None, data_dir: Path | str = None, data_file: Path | str = None, positive: bool = True) -> str | None:
```

**Назначение**: Обучает модель на указанных данных или каталоге.

**Параметры**:
- `data` (str, optional): Путь к CSV-файлу или CSV-форматированная строка с данными.
- `data_dir` (Path | str, optional): Каталог, содержащий CSV-файлы для обучения.
- `data_file` (Path | str, optional): Путь к отдельному CSV-файлу с данными для обучения.
- `positive` (bool, optional): Указывает, являются ли данные положительными или отрицательными. По умолчанию `True`.

**Возвращает**:
- `str | None`: Идентификатор задания обучения или `None`, если произошла ошибка.

**Вызывает исключения**:
- `Exception`: Возникает, если происходит ошибка во время обучения.

**Как работает функция**:

1. Устанавливает `data_dir` в `gs.path.google_drive / 'AI' / 'training'`, если `data_dir` не предоставлен.
2. Пытается загрузить документы из `data`, `data_file` или `data_dir` с использованием `j_loads()`.
3. Отправляет запрос к OpenAI API для обучения модели на основе загруженных документов.
4. Сохраняет идентификатор задания обучения в `self.current_job_id`.
5. Возвращает идентификатор задания обучения.
6. В случае возникновения ошибки логирует ошибку и возвращает `None`.

```
Установка data_dir (если не предоставлен) --> Загрузка документов --> Отправка запроса к OpenAI API для обучения модели --> Сохранение идентификатора задания обучения --> Возврат идентификатора задания обучения
```

**Примеры**:

```python
model = OpenAIModel(api_key="YOUR_API_KEY")
training_result = model.train(data_file=gs.path.google_drive / 'AI' / 'training_data.csv')
print(training_result)
```

### `save_job_id`

```python
def save_job_id(self, job_id: str, description: str, filename: str = "job_ids.json"):
```

**Назначение**: Сохраняет идентификатор задания с описанием в файл.

**Параметры**:
- `job_id` (str): Идентификатор задания для сохранения.
- `description` (str): Описание задания.
- `filename` (str, optional): Имя файла для сохранения идентификаторов заданий. По умолчанию "job_ids.json".

**Как работает функция**:

1. Создает словарь `job_data` с идентификатором задания, описанием и временем создания.
2. Устанавливает `job_file` в `gs.path.google_drive / filename`.
3. Если файл не существует, создает файл и сохраняет список с `job_data` в файл.
4. Если файл существует, загружает существующие задания из файла, добавляет `job_data` в список и сохраняет обновленный список в файл.

```
Создание словаря job_data --> Установка job_file --> Проверка существования файла --> Сохранение данных в файл
```

## Функции

### `main`

```python
def main():
```

**Назначение**: Основная функция для инициализации `OpenAIModel` и демонстрации использования.

**Как работает функция**:

1.  <Инициализация модели с системными инструкциями и ID ассистента.>
2.  <Получение списка доступных моделей и ассистентов.>
3.  <Запрос к модели и получение ответа.>
4.  <Динамическое обучение модели на основе прошлых диалогов.>
5.  <Обучение модели с использованием предоставленных данных.>
6.  <Сохранение ID задания обучения.>
7.  <Описание изображения.>

```
Инициализация модели -> Получение списков -> Запрос к модели -> Динамическое обучение -> Обучение модели -> Сохранение ID -> Описание изображения
```

**Примеры**:

```python
if __name__ == "__main__":
    main()