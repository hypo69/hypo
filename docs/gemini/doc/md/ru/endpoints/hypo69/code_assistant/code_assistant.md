```markdown
# Модуль code_assistant

## Обзор

Данный модуль предоставляет класс `CodeAssistant` для обработки файлов кода с использованием моделей ИИ (например, Google Gemini и OpenAI).  Он предназначен для выполнения различных задач, связанных с анализом и генерацией кода, включая проверку кода, создание документации и другие.

## Классы

### `CodeAssistant`

**Описание**: Класс `CodeAssistant` отвечает за взаимодействие с моделями ИИ для обработки кода. Он инициализирует модели, обрабатывает файлы, создает запросы и сохраняет результаты.

**Атрибуты**:
- `role` (str): Роль ассистента (например, `code_checker`, `doc_writer_rst`).
- `lang` (str): Язык (например, `ru`, `en`).
- `start_dirs` (Path | str | list[Path] | list[str]): Директории, с которых начинается обработка.
- `base_path` (Path): Базовый путь к директории ассистента.
- `config` (SimpleNamespace): Конфигурация ассистента из файла `code_assistant.json`.
- `gemini_model` (GoogleGenerativeAI): Модель Google Gemini.
- `openai_model` (OpenAIModel): Модель OpenAI.
- `start_file_number` (int): Номер файла для начала обработки.

**Методы**:

- `__init__(self, **kwargs)`: Инициализирует ассистента с заданными параметрами.
- `_initialize_models(self, **kwargs)`: Инициализирует модели ИИ (Gemini и OpenAI) на основе `self.model`.
- `parse_args(self)`: Парсит аргументы командной строки.
- `system_instruction(self)`: Чтение инструкции для системы из файла `developer/<role>_<lang>.md`. Возвращает строку инструкции или `False` при ошибке.
- `code_instruction(self)`: Чтение инструкции для кода из файла `instructions/instruction_<role>_<lang>.md`. Возвращает строку инструкции или `False` при ошибке.
- `translations(self)`: Загрузка переводов для ролей и языков из файла `translations/translations.json`. Возвращает `SimpleNamespace` с переводами.
- `process_files(self, start_file_number: int = 1)`: Обработка файлов, взаимодействие с моделью и сохранение результата.  Обрабатывает каждый файл, отправляет запрос в модель, получает ответ и сохраняет его.
- `_create_request(self, content: str) -> str`: Создание запроса для модели ИИ, включающего роль, язык, инструкцию и входящий код.
- `_yield_files_content(self, start_dirs: List[Path] = [gs.path.src]) -> Iterator[tuple[Path, str]]`: Генерирует итератор кортежей (путь к файлу, содержимое файла) для обработки, учитывая `start_dirs`,  фильтрацию по шаблонам и исключение директорий/файлов.
- `_save_response(self, file_path: Path, response: str, model_name: str)`: Сохранение ответа модели в файл в формате `.md` с учетом  `output_directory`.
- `remove_outer_quotes(self, response: str) -> str`: Удаляет внешние кавычки в начале и конце строки.
- `run(self, start_file_number: int = 1)`: Запуск процесса обработки файлов. Обрабатывает прерывания (Ctrl+C).
- `_signal_handler(self, signal, frame)`: Обработчик прерывания.


## Функции

### `main()`

**Описание**: Основная функция для запуска ассистента. Парсит аргументы командной строки и запускает процесс обработки файлов.

### `CodeAssistant.parse_args()`

**Описание**: Парсит аргументы командной строки, относящиеся к ассистенту.

**Возвращает**: Словарь с аргументами командной строки.

##  Примечания

Модуль использует библиотеки `argparse`, `pathlib`, `typing`, `signal`, `time` и другие, для обработки аргументов, путей к файлам, управления процессами и вывода сообщений.  Важно, что загрузка переводов, настройка моделей ИИ и обработка ошибок происходят внутри кода, что важно учитывать при использовании.


```