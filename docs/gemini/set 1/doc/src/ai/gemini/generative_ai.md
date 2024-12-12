# Модуль `hypotez/src/ai/gemini/generative_ai.py`

## Обзор

Модуль `generative_ai.py` предоставляет инструменты для работы с API Google Generative AI. Он позволяет отправлять запросы, получать ответы, сохранять диалоги и обрабатывать различные типы запросов, включая текстовые и запросы с изображениями. Модуль также реализует механизмы обработки ошибок и обеспечивает логирование для отладки.

## Классы

### `GoogleGenerativeAI`

**Описание**: Класс `GoogleGenerativeAI` предоставляет интерфейс для работы с моделью Google Generative AI.  Он инициализируется ключом API, названием модели и дополнительными параметрами, и управляет диалогом с моделью, включая сохранение истории.

**Атрибуты**:

- `MODELS` (List[str]): Список поддерживаемых моделей.
- `api_key` (str): Ключ API для доступа к модели.
- `model_name` (str): Название используемой модели. По умолчанию "gemini-1.5-flash-8b".
- `generation_config` (Dict): Конфигурация для генерации. По умолчанию `{"response_mime_type": "text/plain"}`.
- `system_instruction` (Optional[str]): Инструкция для системы, задающая поведение модели.
- `dialogue_log_path` (Path): Путь для логирования диалогов.
- `dialogue_txt_path` (Path): Путь для сохранения текстовых файлов диалогов.
- `history_dir` (Path): Директория для хранения истории диалогов.
- `history_txt_file` (Path): Путь к файлу для хранения истории в формате текста.
- `history_json_file` (Path): Путь к файлу для хранения истории в формате JSON.
- `model` (Optional[genai.GenerativeModel]): Объект модели Google Generative AI.
- `_chat` (объект): Объект для управления чатом с моделью.

**Методы**:

- `__init__(self, api_key: str, model_name: Optional[str] = None, generation_config: Optional[Dict] = None, system_instruction: Optional[str] = None, **kwargs)`: Инициализирует объект `GoogleGenerativeAI`.
- `ask(self, q: str, attempts: int = 15) -> Optional[str]`: Отправляет текстовый запрос модели и получает ответ. Обрабатывает различные исключения, включая сетевые ошибки, ошибки аутентификации и ошибки API.
- `chat(self, q:str) -> str`: Отправляет запрос в чат с моделью.
- `describe_image(self, image_path: Path) -> Optional[str]`: Генерирует описание изображения, отправляя его в модель.
- `upload_file(self, file: str | Path | IOBase, file_name: Optional[str] = None) -> bool`: Загружает файл в Google Cloud Storage.

### `TimeoutCheck`

**Описание**: Класс для контроля времени выполнения операций.


## Функции

### `_save_dialogue(self, dialogue: list)`

**Описание**: Сохраняет диалог в текстовые и JSON файлы.  Управляет размером файлов, добавляя новые данные.

**Параметры**:

- `dialogue` (list): Список сообщений, представляющих диалог.


## Вспомогательные функции (из других модулей)

- `gs.now`: Получение текущей даты и времени.
- `gs.path`: Обработка путей к файлам.
- `pprint`: Вывод отформатированных данных.
- `read_text_file`: Чтение данных из файла.
- `save_text_file`: Запись данных в файл.
- `j_loads`: Парсинг JSON данных.
- `j_loads_ns`: Парсинг JSON данных в формате SimpleNamespace.
- `j_dumps`: Сериализация данных в JSON формат.
- `decode_unicode_escape`: Декодирование Unicode escape последовательностей.
- `genai.configure`: Настройка API Google Generative AI.
- `genai.upload_file`: Загрузка файла в Google Cloud Storage.
- `genai.delete_file`: Удаление файла из Google Cloud Storage.


## Обрабатываемые исключения

- `requests.exceptions.RequestException`
- `GatewayTimeout`
- `ServiceUnavailable`
- `ResourceExhausted`
- `InvalidArgument`
- `DefaultCredentialsError`
- `RefreshError`
- `RpcError`
- `ValueError`
- `TypeError`
- `Exception`


## Заметки

- Документация содержит примеры использования функций и классов.
- Некоторые методы (`_start_chat`) имеют недокументированные части.  
- Необходимы дополнительные проверки в методах, особенно в обработке ошибок и в `upload_file`.
- Необходимо добавить обработку ситуаций, когда `response` может быть `None`.
- Документация должна быть дополнена примерами использования `generation_config`.
- Необходимо добавить подробное описание `_chat` и его методов.