# Code Assistant: Обучение модели коду проекта

## Описание

`Code Assistant` — инструмент для взаимодействия с моделями **Gemini** и **OpenAI** для обработки исходного кода. Он выполняет задачи, такие как создание документации, проверка кода, и генерация тестов на основе кода из указанных файлов.

## Основные возможности

- **Чтение исходных файлов**: Чтение кода из файлов с расширениями `.py` и `README.MD` из указанных директорий.
- **Обработка с помощью моделей**: Отправка кода в модели для выполнения задач, таких как создание документации или проверка ошибок.
- **Генерация результатов**: Ответы моделей сохраняются в указанные директории для каждой роли.

## Структура проекта

- **Модели**: Используются модели **Gemini** и **OpenAI** для обработки запросов.
- **Промпты**: Программа читает промпты из файлов в директории `src/ai/prompts/developer/` (например, `doc_writer_en.md`).
- **Файлы**: Обрабатываются файлы с расширениями `.py` и `README.MD` в указанных стартовых директориях.

## Пример использования

### Запуск с настройками из JSON:

```bash
python assistant.py --settings settings.json
```

### Запуск с явным указанием параметров:

```bash
python assistant.py --role doc_writer --lang ru --models gemini openai --start_dirs /path/to/dir1 /path/to/dir2
```

### Пример для роли `code_checker`:

```bash
python assistant.py --role code_checker --lang en --models gemini --start_dirs /path/to/dir
```

### Пример для модели `openai`:

```bash
python assistant.py --role doc_writer --lang en --models openai
```

## Параметры командной строки

- `--settings`: Путь к JSON файлу с настройками. Загружает параметры из файла.
- `--role`: Роль модели для выполнения задачи (например, `doc_writer`, `code_checker`).
- `--lang`: Язык выполнения задачи (например, `ru` или `en`).
- `--models`: Список моделей для инициализации (например, `gemini`, `openai`).
- `--start_dirs`: Список директорий для обработки (например, `/path/to/dir1`).

## Логика работы

1. **Чтение файлов**: Поиск файлов с расширениями `.py` и `README.MD` в указанных стартовых директориях.
   * **Вход:** Список директорий `start_dirs`, `exclude_dirs`, `exclude_file_patterns`.
   * **Выход:** Список файлов для обработки.  **Пример:** `/path/to/dir1/file1.py`, `/path/to/dir2/file2.md`.
2. **Загрузка промптов**: Загрузка файлов промптов для каждой роли и языка из директории `src/ai/prompts/developer/`.
   * **Вход:** `role`, `lang`.
   * **Выход:** Загруженный промпт.  **Пример:** текст документации для `doc_writer_en.md`.
3. **Обработка запросов**: Формирование запросов на основе загруженных файлов и отправка их в модели.
   * **Вход:** Файлы, промпт, `model`.
   * **Выход:** Ответ от модели. **Пример:** сгенерированный текст документации.
4. **Сохранение ответов**: Ответы от моделей сохраняются в директории, соответствующей роли и модели (например, `docs/raw_rst_from_<model>/<lang>/`).
   * **Вход:** Ответ от модели, `role`, `model`, `lang`.
   * **Выход:** Сохраненный файл.  **Пример:** `docs/raw_rst_from_gemini/en/file1.rst`.


## Исключения

Настройка исключений для файлов и директорий с помощью параметров:
- `exclude_file_patterns`: Список регулярных выражений для исключения файлов.
- `exclude_dirs`: Список директорий для исключения.
- `exclude_files`: Список файлов для исключения.


## Логирование

Логи сохраняются с помощью библиотеки `logger` и содержат информацию о процессе обработки файлов и полученных ответах.

## Зависимости

- **Gemini API**: Требуется API-ключ для работы с моделью Gemini.
- **OpenAI API**: Требуется API-ключ для работы с моделью OpenAI.
```

<algorithm>

[Start] --> [Read Files] --> [Load Prompts] --> [Process Requests] --> [Save Responses] --> [End]

**Read Files:**
Input: `start_dirs`, `exclude_dirs`, `exclude_file_patterns`
Output: List of files to process
Example: `/path/to/dir1/file1.py`, `/path/to/dir1/file2.md`


**Load Prompts:**
Input: `role`, `lang`
Output: Loaded prompt
Example: content of `src/ai/prompts/developer/doc_writer_en.md`


**Process Requests:**
Input: Files, loaded prompt, `model`
Output: Response from model
Example: Using the loaded prompt to generate documentation for `/path/to/dir1/file1.py`, and sending it to a Gemini model.


**Save Responses:**
Input: Response, `role`, `model`, `lang`
Output: Saved file
Example: Save the generated documentation into `docs/raw_rst_from_gemini/en/file1.rst`.


</algorithm>

<explanation>

**Imports:**  There are no imports shown in the code snippet, which is a description of the program, not the code itself.  The description implies that the script likely uses libraries for handling file operations, regular expressions (for filtering), interacting with Gemini and OpenAI APIs, and logging.

**Classes:** No classes are defined in the provided text. The description indicates that the program is likely structured around functions rather than classes.

**Functions:**  While no specific function definitions are given, the description implies the existence of functions for file reading, prompt loading, API calls, and response saving.  Crucially, the description notes the use of command-line arguments (e.g., `--role`, `--lang`). This suggests a modular design where different parts of the code can be triggered based on the given arguments.

**Variables:**  The variables implied by the text are mainly command-line arguments (`role`, `lang`, `models`, `start_dirs`, etc.) and potentially internal variables for file lists, prompt contents, and API responses.


**Potential Errors and Improvements:**

* **Error Handling:** The description mentions "исключения" (exceptions), but doesn't detail specific error handling. Implementing robust error handling for file access (e.g., file not found), API calls (e.g., API errors, rate limits), and prompt loading is crucial.
* **File Exclusion:** The use of `exclude_file_patterns` suggests the need for a regular expression engine to correctly filter unwanted files. Implementing this needs careful consideration to prevent unexpected behavior and avoid accidental exclusion of essential files.
* **API Keys:**  Storing API keys directly in the code is highly discouraged.  A better approach would be to manage API keys securely, either via environment variables or a configuration file (not directly in the script).
* **Logging:** The mention of a `logger` library is positive.  Adding more detailed logging (with timestamps, levels of severity) will help immensely in debugging and monitoring program execution.

**Relationships with other project parts:**

The description implies that the `Code Assistant` sits within a larger project (`hypotez/src`). The `src/ai/prompts/developer/` directory suggests a separate module for prompts, indicating a clear separation of concerns.  The `assistant.py` script interacts with files and APIs, potentially calling upon other parts of the project's infrastructure.

**Key points:** The structure is mostly described; to fully analyze the code and address specifics, the actual Python script is necessary.