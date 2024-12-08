# Модуль `hypotez/src/ai/gemini/generative_ai.py`

## Обзор

Этот модуль предоставляет класс `GoogleGenerativeAI` для взаимодействия с генеративной моделью Google Gemini. Он позволяет отправлять запросы, получать ответы, сохранять диалоги в файлы и управлять историей взаимодействий. Модуль использует библиотеку `google.generativeai` для работы с API Google Gemini.

## Классы

### `GoogleGenerativeAI`

**Описание**: Класс `GoogleGenerativeAI` предназначен для взаимодействия с генеративной моделью Google Gemini.  Он позволяет отправлять запросы, получать ответы, сохранять диалоги и историю в файлы, а также управлять настройками модели.

**Атрибуты**:

- `MODELS` (List[str]): Список доступных моделей AI.
- `api_key` (str): Ключ API для доступа к генеративной модели.
- `model_name` (str): Название модели для использования.
- `generation_config` (Dict): Конфигурация для генерации.
- `mode` (str): Режим работы модели.
- `dialogue_log_path` (Optional[Path]): Путь для логирования диалогов.
- `dialogue_txt_path` (Optional[Path]): Путь для сохранения текстовых файлов диалогов.
- `history_dir` (Path): Директория для хранения истории.
- `history_txt_file` (Optional[Path]): Путь к файлу для хранения истории в формате текста.
- `history_json_file` (Optional[Path]): Путь к файлу для хранения истории в формате JSON.
- `model` (Optional[genai.GenerativeModel]): Объект модели Google Generative AI.
- `system_instruction` (Optional[str]): Инструкция для системы.

**Методы**:

- `__init__(self, api_key: str, model_name: Optional[str] = None, generation_config: Optional[Dict] = None, system_instruction: Optional[str] = None, **kwargs)`: Инициализация модели с дополнительными настройками.
- `ask(self, q: str, attempts: int = 15) -> Optional[str]`: Отправляет текстовый запрос модели и возвращает ответ. Обрабатывает возможные ошибки (сетевые, временные, аутентификации).
- `chat(self, q:str) -> str`: Проводит чат-сессию с моделью.
- `describe_image(self, image_path: Path) -> Optional[str]`: Генерирует описание изображения по предоставленному пути.
- `upload_file(self, file: str | Path | IOBase, file_name:Optional[str] = None) -> bool`: Загружает файл в систему. Поддерживает результирующее сохранение и обработку ошибок.


## Функции

Нет функций в этом модуле.

## Дополнительная информация

- Модуль использует логгирование через `logger`.
- `TimeoutCheck`: класс для управления таймаутами.
-  Использует библиотеку `google.generativeai` для работы с Google Gemini.
-  Обработка ошибок: модуль включает обработку различных исключений, таких как сетевые ошибки, ошибки авторизации и временные ошибки.