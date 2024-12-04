# Модуль hypotez/src/ai/gemini/generative_ai.py

## Обзор

Данный модуль предоставляет класс `GoogleGenerativeAI` для взаимодействия с API Google Generative AI. Он позволяет отправлять запросы, получать ответы, а также сохранять историю диалогов в текстовых и JSON файлах. Модуль обрабатывает различные исключения, связанные с сетью, аутентификацией, ресурсами и API.

## Оглавление

- [GoogleGenerativeAI](#googlegenerativeai)
    - [__init__](#init)
    - [ask](#ask)
    - [describe_image](#describe_image)
    - [upload_file](#upload_file)
    - [chat](#chat)
    - [config](#config)
    - [_start_chat](#_start_chat)
    - [_save_dialogue](#_save_dialogue)

## Классы

### `GoogleGenerativeAI`

**Описание**: Класс для взаимодействия с моделями Google Generative AI.  Позволяет отправлять запросы, получать ответы и сохранять историю диалогов.

**Атрибуты**:

- `MODELS (List[str])`: Список доступных моделей AI.
- `api_key (str)`: Ключ API для доступа к генеративной модели.
- `model_name (str)`: Название модели для использования. По умолчанию "gemini-1.5-flash-8b".
- `generation_config (Dict)`: Конфигурация для генерации. По умолчанию `{"response_mime_type": "text/plain"}`.
- `mode (str)`: Режим работы модели (например, 'debug' или 'production').
- `dialogue_log_path (Optional[Path])`: Путь для логирования диалогов.
- `dialogue_txt_path (Optional[Path])`: Путь для сохранения текстовых файлов диалогов.
- `history_dir (Path)`: Директория для хранения истории.
- `history_txt_file (Optional[Path])`: Путь к файлу для хранения истории в формате текста.
- `history_json_file (Optional[Path])`: Путь к файлу для хранения истории в формате JSON.
- `model (Optional[genai.GenerativeModel])`: Объект модели Google Generative AI.
- `system_instruction (Optional[str])`: Инструкция для системы.

**Методы**:

- [`__init__`](#init): Инициализация модели GoogleGenerativeAI.
- [`ask`](#ask): Отправляет текстовый запрос модели и возвращает ответ.
- [`describe_image`](#describe_image): Генерирует описание изображения.
- [`upload_file`](#upload_file): Загружает файл в систему.
- [`chat`](#chat): Проводит чат с моделью.
- [`config`](#config): Получает конфигурацию из файла настроек.
- [`_start_chat`](#_start_chat): Инициализирует чат с моделью.
- [`_save_dialogue`](#_save_dialogue): Сохраняет диалог в текстовые и JSON файлы.

### `__init__`

**Описание**: Инициализация модели GoogleGenerativeAI с дополнительными настройками.

**Параметры**:
- `api_key (str)`: Ключ API для доступа к генеративной модели.
- `model_name (Optional[str], optional)`: Название модели для использования. По умолчанию "gemini-1.5-flash-8b".
- `generation_config (Optional[Dict], optional)`: Конфигурация для генерации. По умолчанию `{"response_mime_type": "text/plain"}`.
- `system_instruction (Optional[str], optional)`: Инструкция для системы.


### `ask`

**Описание**: Отправляет текстовый запрос модели и возвращает ответ.

**Параметры**:
- `q (str)`: Вопрос, который будет отправлен модели.
- `attempts (int, optional)`: Количество попыток для получения ответа. По умолчанию 15.

**Возвращает**:
- `Optional[str]`: Ответ от модели или `None`, если ответ не был получен.

**Вызывает исключения**:
- `requests.exceptions.RequestException`: Ошибки сети.
- `GatewayTimeout`, `ServiceUnavailable`: Ошибки доступности сервиса.
- `ResourceExhausted`: Превышение квоты.
- `DefaultCredentialsError`, `RefreshError`: Ошибки аутентификации.
- `ValueError`, `TypeError`: Ошибки некорректного ввода.
- `InvalidArgument`, `RpcError`: Ошибки API.
- `Exception`: Другие непредвиденные ошибки.


### `describe_image`

**Описание**: Генерирует описание изображения.

**Параметры**:
- `image_path (Path)`: Путь к изображению, которое нужно описать.

**Возвращает**:
- `Optional[str]`: Описание изображения или `None`, если произошла ошибка.

**Вызывает исключения**:
- `Exception`: Различные ошибки.


### `upload_file`

**Описание**: Загружает файл в систему.

**Параметры**:
- `file (str | Path | IOBase)`: Файл для загрузки.
- `file_name (Optional[str], optional)`: Имя файла.

**Возвращает**:
- `bool`: Успешность операции.

**Вызывает исключения**:
- `Exception`: Различные ошибки.


### `chat`

**Описание**: Проводит чат с моделью.

**Параметры**:
- `q (str)`: Вопрос для модели.

**Возвращает**:
- `str`: Ответ модели.

**Вызывает исключения**:
- `Exception`: Различные ошибки.


### `config`

**Описание**: Получает конфигурацию из файла настроек.

**Возвращает**:
- `dict`: Конфигурация из файла.


### `_start_chat`

**Описание**: Инициализирует чат с моделью.

**Возвращает**:
- `object`: Объект чата.


### `_save_dialogue`

**Описание**: Сохраняет диалог в текстовые и JSON файлы.

**Параметры**:
- `dialogue (list)`: Список сообщений диалога.