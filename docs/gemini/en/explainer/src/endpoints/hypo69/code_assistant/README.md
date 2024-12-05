# Code Assistant: Code Model Training

## <input code>

```[Русский](https://github.com/hypo69/hypo/blob/master/endpoints/hypo69/code_assistant/README.RU.MD)
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
2. **Загрузка промптов**: Загрузка файлов промптов для каждой роли и языка из директории `src/ai/prompts/developer/`.
3. **Обработка запросов**: Формирование запросов на основе загруженных файлов и отправка их в модели.
4. **Сохранение ответов**: Ответы от моделей сохраняются в директории, соответствующей роли и модели (например, `docs/raw_rst_from_<model>/<lang>/`).

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

порядок действий для создания новой роли для модели ии (`gemini`,`openai`,...):
1. файл `code_assistant.json`
добавить новую роль в список ролей     "roles": [
      "code_checker",
...] активная роль
или в `"exclude-roles"` неактивная роль
2. Добавить роль в файл переводов `translations/translations.json`
3. Создать системный промпт в `ai/prompts/develpoper`
4. Создать командную инструкцию в \'instructions/`
```

## <algorithm>

The workflow can be described as follows:

1. **Input:** Command-line arguments (e.g., `--role`, `--lang`, `--models`, `--start_dirs`).
2. **Configuration Loading:** Loads settings from a JSON file (`settings.json`) or uses command-line arguments.
3. **File Reading:** Iterates through the specified directories (`--start_dirs`) and reads files with `.py` and `README.MD` extensions.  Filters files based on `exclude_file_patterns`, `exclude_dirs`, and `exclude_files`.
4. **Prompt Loading:** Retrieves the appropriate prompt files from `src/ai/prompts/developer/` based on the `--role` and `--lang`.
5. **Request Formation:** Constructs API requests by combining the loaded code snippets with the loaded prompts.
6. **API Call:** Sends the requests to the specified AI models (Gemini or OpenAI).
7. **Response Handling:** Processes responses from the models and saves them in designated output directories.  Error handling (e.g., API errors) is crucial.
8. **Logging:** Records the process details, including files processed, API responses, and potential errors.


## <mermaid>

```mermaid
graph TD
    A[Input Args] --> B{Config Loading};
    B --> C[File Reading];
    C --> D[Prompt Loading];
    D --> E[Request Formation];
    E --> F[API Call (Gemini/OpenAI)];
    F --> G[Response Handling];
    G --> H[Saving Results];
    G --Error--> I[Error Handling];
    I --> J[Logging];
    H --> J;
```

**Dependencies Analysis:**

The diagram shows the main steps. The specific libraries used for file reading, configuration loading, API calls, and logging are not directly shown but are implicit dependencies.  These libraries (e.g., `json`, `os`, `shutil`) would likely be part of the Python standard library.  The code heavily relies on the Gemini and OpenAI APIs, which would require specific import statements and handling of API keys.  `logger` library is also used for logging.


## <explanation>

**Imports:**

The code likely imports modules for file system interactions (e.g., `os`, `pathlib`), JSON parsing (`json`), command-line argument handling (`argparse`), and potentially logging (`logging`).  These imports are critical for file operations, configuration loading, and error handling. The most important imports are those related to interacting with the Gemini and OpenAI APIs. Without those, the code would not be able to communicate with the respective models.  The `src` package structure implies that the project has modular components and potentially dependencies on other Python packages.

**Classes:**

The provided code snippet does not contain class definitions.  It seems likely there are classes within the project (e.g., a class for handling the AI interactions). This would be needed for organizing and abstracting the logic of communicating with models.

**Functions:**

Functions for file reading, prompt loading, API calls, response handling, and logging are likely present but not shown in the snippet.   The code's core logic is probably structured around a function (`main` or similar) to orchestrate the workflow described in the algorithm.


**Variables:**

Variables will hold command-line arguments, loaded configuration data, file paths, API keys, and model responses. These variables' types will depend on their function. (e.g., `start_dirs` is a list, `API_KEY` is a string).

**Potential Errors and Improvements:**

* **Error Handling:**  Comprehensive error handling is essential.  The code needs robust checks for invalid arguments, file access problems, API errors, and incorrect responses from the models.
* **Robustness:**  Add checks for missing or incorrect API keys.
* **Asynchronous Operations:**  Consider using asynchronous programming for API calls if multiple requests are sent concurrently. This can significantly increase performance.
* **Input Validation:** Validate command-line arguments and configuration to prevent unexpected behavior.
* **Testing:**  Include tests for different scenarios, including valid and invalid input.


**Relationships with Other Parts of the Project:**

The code assistant interacts with various components:

* `src/ai/prompts/developer/`: Contains the prompt templates for different roles and languages.
*  Other packages in the `src` directory could contain classes for handling specific tasks, file formats, or interacting with external services.
* `assistant.py`: The entry point orchestrating the entire process.