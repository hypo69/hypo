```MD
# Code Assistant: Описание и функциональность

## <input code>

```
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
1. файл `code_assistant.json`:\nдобавить новую роль в список ролей     "roles": [\n      "code_checker",\n...] активная роль\nили в `"exclude-roles"` неактивная роль\n2. Добавить роль в файл переводов `translations/translations.json`\n3. Создать системный промпт в `ai/prompts/develpoper`\n4. Создать командную инструкцию в \'instructions/`


```

## <algorithm>

Пошаговая блок-схема алгоритма:

1. **Чтение входных данных:** Программа принимает параметры командной строки (`--settings`, `--role`, `--lang`, `--models`, `--start_dirs`).  Например, `--role doc_writer`, `--lang en`, `--models gemini`, `--start_dirs /path/to/code`.
2. **Парсинг настроек:** Если задан файл настроек (`settings.json`), загрузить его и добавить к входным данным.
3. **Выбор роли и модели:**  Выбор роли (`doc_writer`, `code_checker`) и моделей (`gemini`, `openai`).
4. **Чтение файлов:** Проход по указанным директориям (`start_dirs`) и чтение файлов с расширениями `.py` и `README.MD`.  *Пример*: чтение файла `/path/to/code/main.py`.
5. **Чтение промптов:** Загрузка промптов из директории `src/ai/prompts/developer/` на основе выбранной роли и языка. *Пример*: `doc_writer_en.md`.
6. **Формирование запросов:** Создание запросов для моделей (Gemini или OpenAI) на основе промптов и содержимого файлов. *Пример*: Запрос к Gemini: "Документируйте код из файла main.py".
7. **Обработка ответов от моделей:** Получение ответа от модели. *Пример*: Ответ от Gemini: "Вот документация...".
8. **Сохранение ответов:** Сохранение полученных ответов в директории, соответствующей роли и модели. *Пример*: Сохранение документации в `docs/raw_rst_from_gemini/en/`.
9. **Обработка исключений:** Проверка на исключения при работе с файлами, директориями или API.
10. **Логирование:** Запись логов в файл для отслеживания процесса.

## <mermaid>

```mermaid
graph TD
    A[Входные параметры] --> B{Чтение настроек};
    B --> C[Выбор роли и модели];
    C --> D[Чтение файлов];
    D --> E[Чтение промптов];
    E --> F[Формирование запросов];
    F --> G[Обработка запросов моделями (Gemini/OpenAI)];
    G --> H[Сохранение ответов];
    H --> I[Обработка исключений];
    I --> J[Логирование];
    J --> K[Выход];

    subgraph Модели
        G --> G1(Gemini);
        G --> G2(OpenAI);
    end
```

## <explanation>

**Импорты:**

Код не предоставляет импортов. Прилагаемый пример - описание инструмента `code_assistant` , а не реализация.  Для работы приложения, необходимы импорты библиотек для работы с API Gemini и OpenAI, чтением файлов, обработкой JSON, и т.д., которые отсутствуют в данном коде.  Связь с `src`  определяется путем импорта модулей из этой папки (модели, промпты, инструменты для работы с файлами).

**Классы:**

Описание кода не содержит классов.  В реальном коде для обработки и хранения данных могут использоваться классы.

**Функции:**

Описание кода не содержит функций. В реальном коде, вероятно, будут функции для чтения файлов, отправки запросов в модели, обработки ответов и сохранения результатов.


**Переменные:**

Описание кода не содержит переменных, но в реальном коде будут переменные для хранения параметров командной строки, путей к файлам, содержимого файлов и т.д.

**Возможные ошибки и улучшения:**

- Не указаны детали реализации, которые могут повлиять на производительность и надежность. Необходимы функции для чтения файлов, обработки промптов, отправки запросов, сохранения результатов, обработки ответов.
- Отсутствует информация о структуре `src` проекта, которая необходима для понимания импортов и взаимосвязей между модулями.
- Нет информации о конкретных API для моделей Gemini и OpenAI.
- Не указана система управления зависимостями (например, `requirements.txt`).

**Взаимосвязи с другими частями проекта:**

Описание предполагает взаимодействие с `src/ai/prompts/developer/` для загрузки промптов. Для работы с моделями `Gemini` и `OpenAI` необходимы соответствующие API ключи и инструменты для вызова API. Возможная структура проекта включает файлы настроек (`code_assistant.json`, `settings.json`), директории для хранения промптов, результатов и логов, что свидетельствует о необходимости дальнейшей разработки.