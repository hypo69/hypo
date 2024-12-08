# Модуль `hypotez/src/endpoints/hypo69/code_assistant/assistant.py`

## Обзор

Этот модуль предоставляет класс `CodeAssistant` для работы с ассистентом программиста, который читает файлы кода, передает их в модель ИИ (например, Gemini), обрабатывает результат и сохраняет его в директории `docs/gemini`.  Класс позволяет задавать роль исполнителя (например, "code_checker"), язык (например, "ru") и список моделей ИИ для использования.

## Классы

### `CodeAssistant`

**Описание**: Класс `CodeAssistant` отвечает за обработку файлов кода, взаимодействие с моделями ИИ и сохранение результатов.

**Атрибуты**:

- `role` (str): Роль исполнителя (например, "code_checker").
- `lang` (str): Язык выполнения.
- `start_dirs` (Path | str | list[Path] | list[str]): Список директорий для обработки файлов.
- `base_path` (Path): Базовый путь для хранения конфигурации и результатов.
- `config` (SimpleNamespace): Объект конфигурации.
- `gemini_model` (GoogleGenerativeAI): Объект модели Gemini.
- `openai_model` (OpenAIModel): Объект модели OpenAI.
- `start_file_number` (int): Номер файла, с которого начать обработку.

**Методы**:

- `__init__(self, **kwargs)`: Инициализирует ассистента с заданными параметрами.
    - **kwargs**: Параметры инициализации.
- `_initialize_models(self, **kwargs)`: Инициализирует модели ИИ на основе заданных параметров.
- `parse_args()`: Разбирает аргументы командной строки.
- `system_instruction`: Возвращает инструкцию из файла.
- `code_instruction`: Возвращает инструкцию для кода из файла.
- `translations`: Возвращает переводы ролей и языков.
- `process_files(self, start_file_number: Optional[int] = 1)`: Обрабатывает файлы, отправляя их в модель ИИ.
    - **start_file_number**: Номер файла, с которого начать обработку.
- `send_file(file_path: Path) -> bool`: Отправка файла в модель ИИ.
    - **file_path** (Path): Путь к файлу.
    - **file_name** (Optional[str]): Имя файла.
    - **Возвращает**: True, если отправка успешна, False иначе.
- `_create_request(self, file_path: str, content: str) -> str`: Создание запроса к модели ИИ.
    - **file_path** (str): Путь к файлу.
    - **content** (str): Содержимое файла.
- `_yield_files_content(self, start_dirs: List[Path] = [gs.path.src]) -> Iterator[tuple[Path, str]]`: Генерирует пути файлов и их содержимое по указанным директориям.
- `_save_response(self, file_path: Path, response: str, model_name: str) -> None`: Сохраняет ответ модели в файл.
    - **file_path** (Path): Путь к исходному файлу.
    - **response** (str): Ответ модели.
    - **model_name** (str): Имя модели.
- `_remove_outer_quotes(self, response: str) -> str`: Удаляет внешние кавычки из ответа модели.
    - **response** (str): Ответ модели.
- `run(self, start_file_number: int = 1)`: Запуск процесса обработки файлов.
- `_signal_handler(self, signal, frame)`: Обработчик прерывания (Ctrl+C).

## Функции

### `main()`

**Описание**: Основная функция для запуска ассистента.

##  Дополнительные замечания

- Модуль использует `asyncio.sleep(20)` в методе `process_files`, это для отладки. В рабочем варианте этот запрос должен быть удалён.
- `start_dirs` по умолчанию (`[".."]`) требует корректировки, если ваш код не расположен в каталоге `hypotez/src` относительно этого файла.

- Документация содержит примеры использования, но не все детали.

- Модуль использует внешние библиотеки (например, `header`, `gs`, `jjson`, `gemini`, `openai`, `printer`, `path`, `logger`, `make_summary`). Документация для этих библиотек должна быть доступна отдельно.