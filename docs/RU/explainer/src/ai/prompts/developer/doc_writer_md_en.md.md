## ИНСТРУКЦИЯ:

Анализируй предоставленный код подробно и объясни его функциональность. Ответ должен включать три раздела:

1.  **<алгоритм>**: Опиши рабочий процесс в виде пошаговой блок-схемы, включая примеры для каждого логического блока, и проиллюстрируй поток данных между функциями, классами или методами.
2.  **<mermaid>**: Напиши код для диаграммы в формате `mermaid`, проанализируй и объясни все зависимости,
    которые импортируются при создании диаграммы.
    **ВАЖНО!** Убедитесь, что все имена переменных, используемые в диаграмме `mermaid`,
    имеют осмысленные и описательные имена. Имена переменных вроде `A`, `B`, `C`, и т.д., не допускаются!

    **Дополнительно**: Если в коде есть импорт `import header`, добавьте блок `mermaid` flowchart, объясняющий `header.py`:
    ```mermaid
    flowchart TD
        Start --> Header[<code>header.py</code><br> Determine Project Root]

        Header --> import[Import Global Settings: <br><code>from src import gs</code>]
    ```

3.  **<объяснение>**: Предоставьте подробные объяснения:
    *   **Импорты**: Их назначение и взаимосвязь с другими пакетами `src.`.
    *   **Классы**: Их роль, атрибуты, методы и взаимодействие с другими компонентами проекта.
    *   **Функции**: Их аргументы, возвращаемые значения, назначение и примеры.
    *   **Переменные**: Их типы и использование.
    *   Выделите потенциальные ошибки или области для улучшения.

Дополнительно, постройте цепочку взаимосвязей с другими частями проекта (если применимо).

Это обеспечивает всесторонний и структурированный анализ кода.
## Формат ответа: `.md` (markdown)
**КОНЕЦ ИНСТРУКЦИИ**
```markdown
## <алгоритм>

1.  **Инициализация и Описание Модуля:**
    *   Модуль описывается как продвинутый инструмент для документирования кода в проекте `hypotez`.
    *   Основная цель модуля – обработка и документирование кода в формате Markdown, следуя определенным правилам.
    *   Примеры: Примеры использования модуля пока не предоставляются, но описывается формат и ожидания для документации.
2.  **Документация Модуля:**
    *   Указывается, что каждый модуль должен иметь описание в начале, поясняющее его цель.
    *   Приводятся примеры использования модуля, если это возможно. Код примеров должен быть заключен в блоки кода с идентификатором языка `python`.
    *   Указываются платформы и краткое описание модуля.
    *   Для описания атрибутов и методов модуля используются заголовки.
        *   Пример:
            ```markdown
            # Module: Programming Assistant

            This module contains the `CodeAssistant` class, which is used to interact with various AI models, such as Google Gemini and OpenAI, for code processing tasks.

            ## Example Usage

            Example of using the `CodeAssistant` class:

            ```python
            assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
            assistant.process_files()
            ```
            ```
3.  **Документация Классов:**
    *   Каждый класс должен быть описан с указанием его назначения.
    *   Включается описание класса, его атрибуты и методы.
    *   В разделе класса перечисляются все методы, их назначение и примеры использования.
    *   Для каждого метода дается описание параметров и возвращаемых значений, а также примеры.
        *   Пример:
            ```markdown
            # Class: CodeAssistant

            The `CodeAssistant` class is used to interact with various AI models such as Google Gemini and provides methods for analyzing and generating documentation for code.

            ## Attributes
            - `role`: The role of the assistant (e.g., 'code_checker').
            - `lang`: The language the assistant will use (e.g., 'ru').
            - `model`: List of AI models used (e.g., `['gemini']`).

            ## Methods
            ### `process_files`

            Method for processing code files.

            ## Example Usage

            ```python
            assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
            assistant.process_files()
            ```
            ```
4.  **Документация Функций и Методов:**
    *   Каждая функция или метод должны быть документированы с указанием параметров и возвращаемых значений.
    *   Для каждой функции приводится описание ее назначения и примеры использования в блоках кода с идентификатором языка `python`.
        *   Пример:
            ```markdown
            # Method: process_files

            This method is used to analyze and process code files.

            ## Parameters
            - `files`: A list of files to process.
            - `options`: Additional parameters for configuring the processing.

            ## Return Value
            - Returns the processing result as a list of analyzed data.

            ## Example Usage

            ```python
            assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
            result = assistant.process_files(files=['file1.py', 'file2.py'], options={})
            ```
            ```
5.  **Комментарии в Коде:**
    *   Все комментарии в коде должны быть написаны в формате Markdown и пояснять, что делает конкретная часть кода.
    *   Комментарии должны быть в блоках, а не в строках.
    *   Комментарии используются для описания логики и объяснения решений или временных решений в коде.
        *   Пример:
            ```markdown
            # Here, the exception is being handled to continue execution if the file is not found
            try:
                process_file(file)
            except FileNotFoundError as ex:
                handle_exception(ex)
            ```
6. **Документация Исключений**
    *   Исключения документируются для классов, методов и функций.
    *   Указывается, какие исключения могут быть сгенерированы и при каких обстоятельствах.
        *   Пример:
            ```markdown
            # Exception: File Not Found

            This exception is raised when a file is not found during processing.

            ## Parameters
            - `file`: The path of the file that was not found.

            ## Example Usage

            ```python
            try:
                open(file)
            except FileNotFoundError as ex:
                raise FileNotFoundError("File not found") from ex
            ```
            ```

7.  **Создание Mermaid Flowchart Диаграмм:**
    *   Описывается как использовать `mermaid` для создания блок-схем.
    *   Указываются различные типы графиков, такие как `flowchart`, `LR`, `BT`, `RL`.
    *   Имена узлов должны быть осмысленными и описательными.
    *   Используются HTML теги для стилизации текста в узлах.
    *   Приводятся примеры использования HTML тегов и escape-кодов.
    *   Связи между узлами определяются с помощью стрелок `-->` или `---`.
    *   Пример диаграммы:
        ```mermaid
        flowchart TD
            Start[<html>Start of the process<br><b>Create instance</b></html>]
                --> InitSupplier[<html>Initialize Supplier<br><code>_payload&#40;params&#41;</code></html>]
            InitSupplier --> Validate[<html>Validate parameters<br><i>is_valid&#40;params&#41;</i></html>]
            Validate -->|Validation passed| Success[<html><b>Success</b><br>Creation completed</html>]
            Validate -->|Error| Error[<html>Error<br><span style="color:red;">Invalid parameters</span></html>]
        ```

## <mermaid>

```mermaid
flowchart TD
    Start[<html>Start processing<br><b>Document Generation</b></html>]
    
    Start --> ModuleDoc[<html>Document Module<br><code>process_module()</code></html>]
    ModuleDoc --> ClassDoc[<html>Document Class<br><code>process_class()</code></html>]
    ClassDoc --> MethodDoc[<html>Document Method<br><code>process_method()</code></html>]
    MethodDoc --> FunctionDoc[<html>Document Function<br><code>process_function()</code></html>]
    FunctionDoc --> CommentDoc[<html>Document Code Comments<br><code>process_comment()</code></html>]
    CommentDoc --> ExceptionDoc[<html>Document Exceptions<br><code>process_exception()</code></html>]
    ExceptionDoc --> MermaidGen[<html>Generate Mermaid Diagram<br><code>generate_mermaid()</code></html>]
    MermaidGen --> End[<html><b>End of processing</b><br>Documentation completed</html>]

    %% Define connections for better structure
    linkStyle default stroke:#333,stroke-width:2px;
```

**Анализ зависимостей:**

Диаграмма `mermaid` описывает процесс генерации документации, следуя структуре, заданной инструкциями:
*   `Start`: Начало процесса документации.
*   `ModuleDoc`: Этап документирования модуля.  Ожидается, что будет функция `process_module()` для обработки информации о модуле.
*   `ClassDoc`: Этап документирования класса, который предполагает наличие функции `process_class()`.
*   `MethodDoc`: Этап документирования методов класса, который будет использовать `process_method()`.
*   `FunctionDoc`: Этап документирования отдельных функций,  использует `process_function()`.
*   `CommentDoc`: Этап документирования комментариев в коде,  выполняет  `process_comment()`.
*   `ExceptionDoc`: Этап документирования исключений, для этого вызывается функция `process_exception()`.
*   `MermaidGen`: Этап генерации диаграммы `mermaid`,  выполняет `generate_mermaid()`.
*   `End`: Завершение процесса документации.

**Зависимости:**

*   Процесс документирования идет последовательно от модулей до исключений и, наконец, генерации диаграммы.
*   Каждый этап зависит от результата предыдущего этапа.
*   В диаграмме не используется импорт `header`, поэтому дополнительный блок `mermaid` не добавляется.

## <объяснение>

**Импорты:**

В предоставленном коде нет явных импортов, но подразумевается, что модуль будет использовать функции и классы из других частей проекта `hypotez`. Эти функции и классы будут отвечать за обработку данных, генерацию Markdown и, возможно, взаимодействие с AI-моделями.

**Классы:**

В коде примера упоминается класс `CodeAssistant`, но его определение отсутствует. Тем не менее, из описания можно понять его роль:
*   **`CodeAssistant`:** Класс предназначен для взаимодействия с различными AI-моделями (например, Google Gemini, OpenAI) для обработки и документирования кода.
    *   **Атрибуты:**
        *   `role`: Роль ассистента (например, `code_checker`).
        *   `lang`: Язык, который использует ассистент (например, `ru`).
        *   `model`: Список используемых AI-моделей (например, `['gemini']`).
    *   **Методы:**
        *   `process_files`: Метод для обработки файлов с кодом.

**Функции:**

В тексте инструкций подразумеваются следующие функции (явное определение отсутствует):
*   `process_module()`: Функция для документирования модулей.
*   `process_class()`: Функция для документирования классов.
*   `process_method()`: Функция для документирования методов.
*   `process_function()`: Функция для документирования отдельных функций.
*   `process_comment()`: Функция для обработки и документирования комментариев в коде.
*   `process_exception()`: Функция для документирования исключений.
*  `generate_mermaid()`: Функция для генерации диаграмм `mermaid`.

**Переменные:**

Переменные явно не указаны, но из примеров можно выделить:
*   `files`: Список файлов для обработки (например, `['file1.py', 'file2.py']`).
*   `options`: Дополнительные параметры для настройки обработки (например, `{}`).
*   `result`: Переменная для хранения результата обработки.

**Потенциальные ошибки и области для улучшения:**

*   **Отсутствие определений:** Класс `CodeAssistant` и функции не определены, что усложняет понимание полной картины.
*   **Жесткая структура:**  Документация предполагает строгую последовательность (модули -> классы -> методы -> функции -> комментарии -> исключения -> mermaid). Можно сделать процесс более гибким, например, обрабатывать только необходимые этапы.
*   **Нет описания взаимодействия с AI:** Как именно `CodeAssistant` взаимодействует с AI-моделями не описано.

**Взаимосвязи с другими частями проекта:**

*   Предполагается, что модуль будет взаимодействовать с AI-моделями через API или другие механизмы.
*   Модуль будет использовать другие части `hypotez` для доступа к файлам, их анализа, генерации Markdown и возможно для взаимодействия с диаграммами `mermaid`.
*   Ожидается интеграция с системой управления проектами.