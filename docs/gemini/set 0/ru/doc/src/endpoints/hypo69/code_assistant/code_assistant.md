# Модуль src.endpoints.hypo69.code_assistant

## Обзор

Этот модуль предоставляет класс `CodeAssistant` для обработки файлов кода с использованием моделей ИИ, таких как Gemini.  Класс позволяет задавать роль ассистента (например, "code_checker"), язык (например, "ru") и список моделей для работы.  Результаты обработки сохраняются в директории `docs/gemini`.  Модуль предоставляет механизмы для чтения инструкций, обработки аргументов командной строки, инициализации моделей ИИ и взаимодействия с файлами.

## Классы

### `CodeAssistant`

**Описание**: Класс для работы ассистента программиста с моделями ИИ.  Предназначен для чтения файлов кода, отправки запросов моделям ИИ, обработки ответов и сохранения результатов в указанной директории.

**Атрибуты**:

- `role` (str): Роль ассистента (например, "code_checker", "doc_writer_rst").
- `lang` (str): Язык (например, "ru", "en").
- `start_dirs` (Path | str | list[Path] | list[str]): Директории для обработки файлов. По умолчанию `[".."]`.
- `base_path` (Path): Базовый путь к директории с ассистентом.
- `config` (SimpleNamespace): Конфигурация ассистента (загружается из `code_assistant.json`).
- `gemini_model` (GoogleGenerativeAI): Модель ИИ Gemini.
- `openai_model` (OpenAIModel): Модель ИИ OpenAI (если указана в `model`).
- `start_file_number` (int): С какого номера файла начать обработку.

**Методы**:

- `__init__(self, **kwargs)`: Инициализация ассистента с заданными параметрами.
- `_initialize_models(self, **kwargs)`: Инициализация моделей ИИ.
- `parse_args()`: Разбор аргументов командной строки.
- `system_instruction`: Чтение инструкции из файла (с учетом роли и языка).
- `code_instruction`: Чтение инструкции для обработки кода (с учетом роли и языка).
- `translations`: Загрузка переводов для ролей и языков.
- `process_files(self, start_file_number: Optional[int] = 1)`: Обработка файлов.
- `_create_request(self, file_path: str, content: str) -> str`: Создание запроса для модели ИИ.
- `_yield_files_content(self, start_dirs: List[Path] = [gs.path.src])`: Генерирует пути файлов и их содержимое из указанных директорий.
- `_save_response(self, file_path: Path, response: str, model_name: str) -> None`: Сохранение ответа модели в файл.
- `_remove_outer_quotes(self, response: str) -> str`: Удаляет внешние кавычки в начале и в конце строки.
- `run(self, start_file_number: int = 1)`: Запуск обработки файлов.
- `_signal_handler(self, signal, frame)`: Обработка прерывания выполнения.


## Функции

### `main()`

**Описание**: Основная функция для запуска. Разбирает аргументы командной строки, создает экземпляр `CodeAssistant` и запускает метод `process_files`.


## Поддержка исключений

В методах класса `CodeAssistant`, где присутствует обработка исключений, используются `try...except` блоки.  Вместо `e` используется `ex` для обозначения исключения.


## Взаимодействие с другими модулями

Модуль использует классы и функции из других модулей:

- `asyncio`, `argparse`, `sys`, `pathlib`, `typing`, `types`, `signal`, `time`, `re`, `fnmatch` - стандартные библиотеки Python
- `header`, `gs`, `j_loads`, `j_loads_ns`, `GoogleGenerativeAI`, `OpenAIModel`, `pprint`, `get_relative_path`, `logger`, `make_summary` - пользовательские модули.