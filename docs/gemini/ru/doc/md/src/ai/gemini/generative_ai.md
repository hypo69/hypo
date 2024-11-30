# Модуль `hypotez/src/ai/gemini/generative_ai.py`

## Обзор

Данный модуль предоставляет класс `GoogleGenerativeAI` для взаимодействия с API Google Generative AI, включая отправку запросов, получение ответов, сохранение диалогов и работу с изображениями. Модуль интегрирует обработку ошибок, экспоненциальный бэк-офф и логирование для устойчивой работы с API.

## Оглавление

* [GoogleGenerativeAI](#googlegenerativeai)
    * [__init__](#init)
    * [__post_init__](#postinit)
    * [config](#config)
    * [start_chat](#startchat)
    * [_save_dialogue](#savedialogue)
    * [ask](#ask)
    * [chat](#chat)
    * [describe_image](#describeimage)


## Классы

### `GoogleGenerativeAI`

**Описание**: Класс для взаимодействия с моделями Google Generative AI. Он позволяет отправлять текстовые запросы, обрабатывать изображения, сохранять диалоги и управлять историей.

**Атрибуты**:

- `MODELS (List[str])`: Список доступных моделей AI.
- `api_key (str)`: Ключ API для доступа к генеративной модели.
- `model_name (str)`: Название модели для использования. По умолчанию `gemini-1.5-flash-8b`.
- `generation_config (Dict)`: Конфигурация для генерации. По умолчанию `{"response_mime_type": "text/plain"}`.
- `mode (str)`: Режим работы модели (например, 'debug' или 'production').
- `dialogue_log_path (Optional[Path])`: Путь для логирования диалогов.
- `dialogue_txt_path (Optional[Path])`: Путь для сохранения текстовых файлов диалогов.
- `history_dir (Path)`: Директория для хранения истории.
- `history_txt_file (Optional[Path])`: Путь к файлу для хранения истории в формате текста.
- `history_json_file (Optional[Path])`: Путь к файлу для хранения истории в формате JSON.
- `model (Optional[genai.GenerativeModel])`: Объект модели Google Generative AI.
- `system_instruction (Optional[str])`: Инструкция для системы, задающая параметры поведения модели.


**Методы**:

#### `__init__`

**Описание**: Инициализация модели GoogleGenerativeAI с дополнительными настройками.

**Аргументы**:

- `api_key (str)`: Ключ API для доступа к генеративной модели.
- `model_name (Optional[str], optional)`: Название модели для использования. По умолчанию `"gemini-1.5-flash-8b"`.
- `generation_config (Optional[Dict], optional)`: Конфигурация для генерации. По умолчанию `{"response_mime_type": "text/plain"}`.
- `system_instruction (Optional[str], optional)`: Инструкция для системы. По умолчанию `None`.

#### `__post_init__`

**Описание**: Метод для инициализации модели и других параметров после создания экземпляра.

#### `config`

**Описание**: Получение конфигурации из файла настроек.

**Возвращает**: Словарь с конфигурацией.

#### `start_chat`

**Описание**: Начало чата с моделью.

#### `_save_dialogue`

**Описание**: Сохраняет диалог в текстовый и JSON файлы.

**Аргументы**:

- `dialogue (list)`: Список сообщений диалога.

#### `ask`

**Описание**: Отправляет текстовый запрос модели и возвращает ответ.

**Аргументы**:

- `q (str)`: Вопрос для модели.
- `attempts (int, optional)`: Количество попыток. По умолчанию 15.

**Возвращает**: Ответ от модели или `None`, если ответ не был получен.

**Обрабатывает исключения**:
- `requests.exceptions.RequestException`
- `GatewayTimeout`, `ServiceUnavailable`
- `ResourceExhausted`
- `DefaultCredentialsError`, `RefreshError`
- `ValueError`, `TypeError`
- `InvalidArgument`, `RpcError`
- `Exception`

#### `chat`

**Описание**: Ведет диалог с моделью.

#### `describe_image`

**Описание**: Генерирует описание изображения.

**Аргументы**:

- `image_path (Path)`: Путь к изображению.

**Возвращает**: Описание изображения или `None` при ошибке.


## Функции


```
```

**Примечания**: Документация для функций `start_chat` и `chat` неполная.  Необходимо добавить описание, параметры, возвращаемые значения и обработку исключений в соответствии с заданным форматом.  Фрагмент `if __name__ == "__main__":` также требует документирования.