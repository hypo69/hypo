# Модуль `hypotez/src/ai/gemini/generative_ai.py`

## Обзор

Этот модуль предоставляет класс `GoogleGenerativeAI` для взаимодействия с API Google Generative AI.  Класс позволяет отправлять запросы, получать ответы, сохранять диалоги и загружать файлы.  Включает обработку различных ошибок и экспоненциальный бэк-офф для повышения надежности.

## Оглавление

- [Модуль `hypotez/src/ai/gemini/generative_ai.py`](#модуль-hypotezsrc-ai-gemini-generative-ai-py)
- [Обзор](#обзор)
- [Класс `GoogleGenerativeAI`](#класс-googlegenerativeai)
    - [`__init__`](#-init-)
    - [`ask`](#ask)
    - [`chat`](#chat)
    - [`describe_image`](#describe-image)
    - [`upload_file`](#upload-file)
    - [`_save_dialogue`](#_save-dialogue)
    - [`_start_chat`](#_start-chat)
    - [`config`](#config)


## Класс `GoogleGenerativeAI`

### Описание

Класс для взаимодействия с моделями Google Generative AI.  Обеспечивает настройку, отправку запросов, получение ответов и сохранение диалогов.

### Методы

#### `__init__`

**Описание**: Инициализирует модель Google Generative AI с дополнительными настройками.

**Параметры**:
- `api_key` (str): Ключ API для доступа к генеративной модели.
- `model_name` (Optional[str], optional): Название модели для использования. По умолчанию "gemini-1.5-flash-8b".
- `generation_config` (Optional[Dict], optional): Конфигурация для генерации. По умолчанию `{"response_mime_type": "text/plain"}`.
- `system_instruction` (Optional[str], optional): Инструкция для системы. По умолчанию `None`.

#### `ask`

**Описание**: Отправляет текстовый запрос модели и возвращает ответ.

**Параметры**:
- `q` (str): Вопрос, который будет отправлен модели.
- `attempts` (int, optional): Количество попыток для получения ответа. По умолчанию 15.

**Возвращает**:
- `Optional[str]`: Ответ от модели или `None`, если ответ не был получен.

**Возможные исключения**:
- `requests.exceptions.RequestException`: Ошибка сети.
- `GatewayTimeout`, `ServiceUnavailable`: Сервис недоступен.
- `ResourceExhausted`: Превышен лимит запросов.
- `DefaultCredentialsError`, `RefreshError`: Ошибка аутентификации.
- `ValueError`, `TypeError`: Неверный входной формат.
- `InvalidArgument`, `RpcError`: Ошибка API.
- `Exception`: Другие непредвиденные ошибки.

#### `chat`

**Описание**: Отправляет запрос в чат-боту и возвращает ответ.

**Параметры**:
- `q` (str): Вопрос.

**Возвращает**:
- `str`: Ответ.

**Возможные исключения**:
- `Exception`: Ошибки во время взаимодействия с чатом.


#### `describe_image`

**Описание**: Генерирует описание изображения.

**Параметры**:
- `image_path` (Path): Путь к изображению, которое нужно описать.

**Возвращает**:
- `Optional[str]`: Описание изображения или `None`, если произошла ошибка.

**Возможные исключения**:
- `Exception`: Ошибки при работе с изображением.


#### `upload_file`

**Описание**: Загружает файл в Google Cloud Storage.

**Параметры**:
- `file` (str | Path | IOBase): Путь или объект файла для загрузки.
- `file_name` (Optional[str], optional): Имя файла для загрузки. По умолчанию `None`.

**Возвращает**:
- `bool`: `True`, если загрузка прошла успешно; `False` в противном случае.

**Возможные исключения**:
- `Exception`: Ошибки при загрузке файла.


#### `_save_dialogue`

**Описание**: Сохраняет диалог в текстовый и JSON файлы.

**Параметры**:
- `dialogue` (list): Список сообщений, представляющих диалог.

#### `_start_chat`

**Описание**: Начинает сеанс чата с моделью.


#### `config`

**Описание**: Возвращает конфигурацию из файла настроек.