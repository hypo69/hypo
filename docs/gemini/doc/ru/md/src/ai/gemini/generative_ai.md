# Модуль `hypotez/src/ai/gemini/generative_ai.py`

## Обзор

Данный модуль предоставляет класс `GoogleGenerativeAI` для взаимодействия с генеративными моделями Google AI (Gemini).  Он позволяет отправлять запросы, получать ответы и сохранять диалоги в текстовые и JSON файлы. Модуль включает обработку исключений для устойчивости работы и логирование для отладки.

## Оглавление

* [GoogleGenerativeAI](#googlegenerativeai)
    * [__init__](#init)
    * [__post_init__](#postinit)
    * [config](#config)
    * [_save_dialogue](#save_dialogue)
    * [ask](#ask)
    * [describe_image](#describe_image)
* [chat](#chat)


## Классы

### `GoogleGenerativeAI`

**Описание**: Класс для работы с генеративными моделями Google AI (Gemini).  Позволяет отправлять запросы, получать ответы, сохранять историю диалогов.

**Атрибуты**:

* `MODELS` (List[str]): Список поддерживаемых моделей Gemini.
* `api_key` (str): Ключ API для доступа к модели.
* `model_name` (str): Название модели (по умолчанию "gemini-1.5-flash-8b").
* `generation_config` (Dict): Конфигурация для генерации (по умолчанию `{"response_mime_type": "text/plain"}`).
* `system_instruction` (Optional[str]): Инструкция для системы, задающая поведение модели.
* `dialogue_log_path` (Optional[Path]): Путь для логирования диалогов.
* `dialogue_txt_path` (Optional[Path]): Путь для сохранения текстовых файлов диалогов.
* `history_dir` (Path): Директория для хранения истории.
* `history_txt_file` (Optional[Path]): Путь к файлу для сохранения истории в текстовом формате.
* `history_json_file` (Optional[Path]): Путь к файлу для сохранения истории в JSON формате.
* `model` (Optional[genai.GenerativeModel]): Объект модели Google Generative AI.

**Методы**:

#### `__init__`

**Описание**: Инициализирует экземпляр класса `GoogleGenerativeAI`.

**Параметры**:

* `api_key` (str): Ключ API для доступа к модели.
* `model_name` (Optional[str], optional): Название модели. По умолчанию "gemini-1.5-flash-8b".
* `generation_config` (Optional[Dict], optional): Конфигурация для генерации. По умолчанию `{"response_mime_type": "text/plain"}`.
* `system_instruction` (Optional[str], optional): Инструкция для системы. По умолчанию `None`.

#### `__post_init__`

**Описание**: Вызывается после инициализации.  Инициализирует модель, если `api_key` указан, но модель не была инициализирована в конструкторе.

#### `config`

**Описание**:  Получает конфигурацию из файла настроек.

**Возвращает**: 
    Dict: Конфигурация.


#### `_save_dialogue`

**Описание**: Сохраняет диалог в текстовый и JSON файлы. Управляет размером файлов.

**Параметры**:

* `dialogue` (list): Список сообщений в формате диалога.

#### `ask`

**Описание**: Отправляет запрос модели и возвращает ответ.

**Параметры**:

* `q` (str): Запрос.
* `attempts` (int, optional): Количество попыток. По умолчанию 15.

**Возвращает**:
* `Optional[str]`:  Ответ модели или `None` при ошибках.


#### `describe_image`

**Описание**: Генерирует описание изображения на основе его пути.

**Параметры**:

* `image_path` (Path): Путь к изображению.

**Возвращает**:
* `Optional[str]`: Текстовое описание изображения или `None` при ошибках.


## Функции

### `chat`

**Описание**: Запускает интерактивный чат с моделью.

**Пример**:

```python
chat()
```


**Примечания**: Приведенный пример требует установки библиотек `google.generativeai`, `requests`, и др.