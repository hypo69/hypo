# Модуль `hypotez/src/endpoints/hypo69/code_assistant/assistant.py`

## Обзор

Этот модуль предоставляет класс `CodeAssistant` для работы с ассистентом программиста, который читает файлы кода, передает их в модели ИИ (например, Gemini), обрабатывает полученные ответы и сохраняет результаты в директории `docs/gemini`.  Ассистент поддерживает различные роли и языки, настраиваемые через конфигурацию.

## Классы

### `CodeAssistant`

**Описание**: Класс для работы ассистента программиста с моделями ИИ. Он загружает файлы, формирует запросы, отправляет их в модели ИИ, обрабатывает ответы и сохраняет результаты.

**Атрибуты**:

- `role` (str): Роль ассистента (например, `code_checker`).
- `lang` (str): Язык обработки (например, `ru`).
- `start_dirs` (Path | str | list[Path] | list[str]): Директории для поиска файлов.
- `base_path` (Path): Базовый путь к директории с конфигурацией.
- `config` (SimpleNamespace): Конфигурационные настройки.
- `gemini_model` (GoogleGenerativeAI): Объект для работы с моделью Gemini.
- `openai_model` (OpenAIModel): Объект для работы с моделью OpenAI.
- `start_file_number` (int): С какого номера файла начинать обработку (для возобновления после ошибок).

**Методы**:

#### `__init__(self, **kwargs)`

**Описание**: Инициализирует объект `CodeAssistant` с заданными параметрами.

**Параметры**:
- `kwargs`: Словарь ключевых параметров.

#### `_initialize_models(self, **kwargs)`

**Описание**: Инициализирует модели ИИ (Gemini, OpenAI) в зависимости от указанных параметров.

**Параметры**:
- `kwargs`: Словарь ключевых параметров.


#### `parse_args()` (статический метод)

**Описание**: Разбирает аргументы командной строки.

**Возвращает**: Словарь с аргументами командной строки.

#### `system_instruction(self)`

**Описание**: Чтение инструкции для системы из файла.

**Возвращает**: Строка с инструкцией или `False` при ошибке.

#### `code_instruction(self)`

**Описание**: Чтение инструкции для обработки кода из файла.

**Возвращает**: Строка с инструкцией или `False` при ошибке.

#### `translations(self)`

**Описание**: Загрузка переводов для ролей и языков из файла.

**Возвращает**: Объект `SimpleNamespace` с переводами.

#### `process_files(self, start_file_number: Optional[int] = 1)`

**Описание**: Обрабатывает файлы из указанных директорий, отправляя их в модель ИИ и сохраняя результат.

**Параметры**:
- `start_file_number` (int): С какого номера файла начинать обработку.

#### `_create_request(self, file_path: str, content: str) -> str`

**Описание**: Формирует запрос для модели ИИ на основе содержимого файла и конфигурации.

**Параметры**:
- `file_path` (str): Путь к файлу.
- `content` (str): Содержимое файла.

**Возвращает**: Строку с запросом в формате JSON.

#### `_yield_files_content(self, start_dirs: List[Path] = [gs.path.src])`

**Описание**: Генерирует итератор пар (путь к файлу, содержимое файла) из заданных директорий, учитывая паттерны включения/исключения.

**Параметры**:
- `start_dirs` (List[Path]): Список директорий для обхода.

**Возвращает**: Итератор кортежей.

#### `_save_response(self, file_path: Path, response: str, model_name: str)`

**Описание**: Сохраняет ответ модели ИИ в файл, учитывая роль, язык и имя модели.

**Параметры**:
- `file_path` (Path): Путь к исходному файлу.
- `response` (str): Ответ модели.
- `model_name` (str): Имя модели.


#### `_remove_outer_quotes(self, response: str) -> str`

**Описание**: Удаляет внешние кавычки из строки, если они присутствуют.

**Параметры**:
- `response` (str): Строка, из которой нужно удалить кавычки.

**Возвращает**: Обработанную строку.


#### `run(self, start_file_number: int = 1)`

**Описание**: Запускает процесс обработки файлов.

**Параметры**:
- `start_file_number` (int): С какого номера файла начинать обработку.


### `main()`

**Описание**: Главная функция для запуска ассистента.


## Функции

### `send_file(file_path: Path) -> bool`

**Описание**: Отправляет файл в модель ИИ.

**Параметры**:
- `file_path` (Path): Путь к файлу.


##  Комментарии

- Модуль использует `asyncio.sleep(20)` для задержки в цикле обработки, что может быть использовано для отладки. Подумайте о более элегантном подходе для обработки concurrency.
- В методе `_yield_files_content` есть блоки `pprint` - их целесообразно удалить из production кода.
- Функции `_remove_outer_quotes` содержит обращение к `config`, которое необходимо пересмотреть для повышения надежности.