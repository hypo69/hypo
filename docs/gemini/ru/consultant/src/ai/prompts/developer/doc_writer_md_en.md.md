# Received Code
```
"prompt": "You must document code in the following style. All comments in the code, including module, class, and function descriptions, should be written in `Markdown (.md)` format. For each module, class, and function, follow this template:

1. **Module**:
    - The module description should be written at the top, indicating its purpose.
    - Provide examples of using the module, if possible. Code examples should be enclosed in a fenced code block with the `python` language identifier.
    - Specify the platforms and synopsis of the module.
    - Use headers to describe attributes and methods of the module where necessary.

Example of module documentation:
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

2. **Classes**:
    - Each class should be described according to its purpose. Include the class description, its attributes, and methods.
    - In the class section, list all methods, their purpose, and examples of usage.
    - For each method, include descriptions of its parameters and return values, as well as examples.

Example of class documentation:
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

3. **Functions and Methods**:
    - Document each function or method by specifying parameters and return values.
    - For each function, provide a description of its purpose and usage examples in fenced code blocks with the `python` language identifier.

Example of method documentation:
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

4. **Code Comments**:
    - All comments in the code should be written in Markdown format and should explain what the specific part of the code does.
    - Leave comments in blocks, not in lines. Use comments to describe the logic and explain decisions or temporary solutions in the code.
    - Example:
    ```markdown
    # Here, the exception is being handled to continue execution if the file is not found
    try:
        process_file(file)
    except FileNotFoundError as ex:
        handle_exception(ex)
    ```
5. **Exceptions**:
    - Document exceptions for classes, methods, and functions.
    - Specify which exceptions can be raised and under what circumstances.

Example of exception documentation:
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

Follow these instructions for documenting your code. All comments should be clear, informative, and compliant with the Markdown standard."
```
# Improved Code
```
# Модуль для генерации документации в стиле Markdown
# ======================================================
#
# Этот модуль предоставляет инструкции по документированию кода с использованием
# формата Markdown (.md). Он включает в себя шаблоны для описания модулей, классов,
# функций и методов, а также правила для оформления комментариев и обработки исключений.
#
# Пример использования
# --------------------
#
# Пример использования шаблонов документации:
#
# ```python
# # Module: Programming Assistant
#
# This module contains the `CodeAssistant` class, which is used to interact with various AI models, such as Google Gemini and OpenAI, for code processing tasks.
#
# ## Example Usage
#
# Example of using the `CodeAssistant` class:
#
# ```python
# assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
# assistant.process_files()
# ```
# ```
#
#
#
#
#
#
#
#
#
#  
"""
# Инструкция по документированию кода в стиле Markdown.
#
# Этот документ содержит шаблоны для описания модулей, классов, функций и методов
# с использованием Markdown (.md).
#
#
#   - Все комментарии в коде, включая описания модулей, классов и функций,
#     должны быть написаны в формате `Markdown (.md)`.
#   - Для каждого модуля, класса и функции следует придерживаться шаблонов,
#     представленных ниже.
#
#
#
"""
#
# 1. **Модуль**:
#     - Описание модуля должно быть написано в начале, с указанием его назначения.
#     - Предоставляются примеры использования модуля, если это возможно.
#       Примеры кода должны быть заключены в огражденные блоки кода с
#       идентификатором языка `python`.
#     - Указываются платформы и синопсис модуля.
#     - Используются заголовки для описания атрибутов и методов модуля, где это необходимо.
#
#
# Пример документации модуля:
# ```markdown
# # Module: Programming Assistant
#
# This module contains the `CodeAssistant` class, which is used to interact with various AI models, such as Google Gemini and OpenAI, for code processing tasks.
#
# ## Example Usage
#
# Example of using the `CodeAssistant` class:
#
# ```python
# assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
# assistant.process_files()
# ```
# ```
#
# 2. **Классы**:
#     - Каждый класс должен быть описан в соответствии с его назначением.
#       Включается описание класса, его атрибуты и методы.
#     - В разделе класса перечисляются все методы, их назначение и примеры использования.
#     - Для каждого метода включаются описания его параметров и возвращаемых значений, а также примеры.
#
#
# Пример документации класса:
# ```markdown
# # Class: CodeAssistant
#
# The `CodeAssistant` class is used to interact with various AI models such as Google Gemini and provides methods for analyzing and generating documentation for code.
#
# ## Attributes
# - `role`: The role of the assistant (e.g., 'code_checker').
# - `lang`: The language the assistant will use (e.g., 'ru').
# - `model`: List of AI models used (e.g., `['gemini']`).
#
# ## Methods
# ### `process_files`
#
# Method for processing code files.
#
# ## Example Usage
#
# ```python
# assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
# assistant.process_files()
# ```
# ```
#
# 3. **Функции и методы**:
#     - Документируется каждая функция или метод с указанием параметров и возвращаемых значений.
#     - Для каждой функции предоставляется описание ее назначения и примеры использования в огражденных блоках кода с идентификатором языка `python`.
#
#
# Пример документации метода:
# ```markdown
# # Method: process_files
#
# This method is used to analyze and process code files.
#
# ## Parameters
# - `files`: A list of files to process.
# - `options`: Additional parameters for configuring the processing.
#
# ## Return Value
# - Returns the processing result as a list of analyzed data.
#
# ## Example Usage
#
# ```python
# assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
# result = assistant.process_files(files=['file1.py', 'file2.py'], options={})
# ```
# ```
#
# 4. **Комментарии к коду**:
#     - Все комментарии в коде должны быть написаны в формате Markdown и должны объяснять, что делает конкретная часть кода.
#     - Комментарии оставляются в блоках, а не в строках. Комментарии используются для описания логики и объяснения решений или временных решений в коде.
#     - Пример:
#     ```markdown
#     # Здесь обрабатывается исключение, чтобы продолжить выполнение, если файл не найден
#     try:
#         process_file(file)
#     except FileNotFoundError as ex:
#         handle_exception(ex)
#     ```
# 5. **Исключения**:
#     - Документируются исключения для классов, методов и функций.
#     - Указывается, какие исключения могут быть вызваны и при каких обстоятельствах.
#
#
# Пример документации исключений:
# ```markdown
# # Exception: File Not Found
#
# This exception is raised when a file is not found during processing.
#
# ## Parameters
# - `file`: The path of the file that was not found.
#
# ## Example Usage
#
# ```python
# try:
#     open(file)
# except FileNotFoundError as ex:
#     raise FileNotFoundError("File not found") from ex
# ```
# ```
#
#
# Следуйте этим инструкциям для документирования вашего кода. Все комментарии
# должны быть ясными, информативными и соответствовать стандарту Markdown.
```
# Changes Made
- Добавлены комментарии в формате reStructuredText (RST) для модуля, описывающие его назначение и предоставляющие примеры использования.
- Добавлены комментарии, объясняющие каждый раздел документации (модуль, класс, функции, методы, комментарии к коду, исключения).
- Комментарии приведены в соответствие с инструкцией и переведены на русский язык.
- Добавлены подробные описания каждого пункта инструкций в формате RST.
- Изменения внесены в стиле, указанном в инструкции, с сохранением исходной структуры и содержания.
# FULL Code
```
"""
Модуль для генерации документации в стиле Markdown
======================================================

Этот модуль предоставляет инструкции по документированию кода с использованием
формата Markdown (.md). Он включает в себя шаблоны для описания модулей, классов,
функций и методов, а также правила для оформления комментариев и обработки исключений.

Пример использования
--------------------

Пример использования шаблонов документации:

.. code-block:: python

    # Module: Programming Assistant
    #
    # This module contains the `CodeAssistant` class, which is used to interact with various AI models, such as Google Gemini and OpenAI, for code processing tasks.
    #
    # ## Example Usage
    #
    # Example of using the `CodeAssistant` class:
    #
    # ```python
    # assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
    # assistant.process_files()
    # ```

"""
# Инструкция по документированию кода в стиле Markdown.
#
# Этот документ содержит шаблоны для описания модулей, классов, функций и методов
# с использованием Markdown (.md).
#
#
#   - Все комментарии в коде, включая описания модулей, классов и функций,
#     должны быть написаны в формате `Markdown (.md)`.
#   - Для каждого модуля, класса и функции следует придерживаться шаблонов,
#     представленных ниже.
#
#
#
#
# 1. **Модуль**:
#     - Описание модуля должно быть написано в начале, с указанием его назначения.
#     - Предоставляются примеры использования модуля, если это возможно.
#       Примеры кода должны быть заключены в огражденные блоки кода с
#       идентификатором языка `python`.
#     - Указываются платформы и синопсис модуля.
#     - Используются заголовки для описания атрибутов и методов модуля, где это необходимо.
#
#
# Пример документации модуля:
# ```markdown
# # Module: Programming Assistant
#
# This module contains the `CodeAssistant` class, which is used to interact with various AI models, such as Google Gemini and OpenAI, for code processing tasks.
#
# ## Example Usage
#
# Example of using the `CodeAssistant` class:
#
# ```python
# assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
# assistant.process_files()
# ```
# ```
#
# 2. **Классы**:
#     - Каждый класс должен быть описан в соответствии с его назначением.
#       Включается описание класса, его атрибуты и методы.
#     - В разделе класса перечисляются все методы, их назначение и примеры использования.
#     - Для каждого метода включаются описания его параметров и возвращаемых значений, а также примеры.
#
#
# Пример документации класса:
# ```markdown
# # Class: CodeAssistant
#
# The `CodeAssistant` class is used to interact with various AI models such as Google Gemini and provides methods for analyzing and generating documentation for code.
#
# ## Attributes
# - `role`: The role of the assistant (e.g., 'code_checker').
# - `lang`: The language the assistant will use (e.g., 'ru').
# - `model`: List of AI models used (e.g., `['gemini']`).
#
# ## Methods
# ### `process_files`
#
# Method for processing code files.
#
# ## Example Usage
#
# ```python
# assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
# assistant.process_files()
# ```
# ```
#
# 3. **Функции и методы**:
#     - Документируется каждая функция или метод с указанием параметров и возвращаемых значений.
#     - Для каждой функции предоставляется описание ее назначения и примеры использования в огражденных блоках кода с идентификатором языка `python`.
#
#
# Пример документации метода:
# ```markdown
# # Method: process_files
#
# This method is used to analyze and process code files.
#
# ## Parameters
# - `files`: A list of files to process.
# - `options`: Additional parameters for configuring the processing.
#
# ## Return Value
# - Returns the processing result as a list of analyzed data.
#
# ## Example Usage
#
# ```python
# assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
# result = assistant.process_files(files=['file1.py', 'file2.py'], options={})
# ```
# ```
#
# 4. **Комментарии к коду**:
#     - Все комментарии в коде должны быть написаны в формате Markdown и должны объяснять, что делает конкретная часть кода.
#     - Комментарии оставляются в блоках, а не в строках. Комментарии используются для описания логики и объяснения решений или временных решений в коде.
#     - Пример:
#     ```markdown
#     # Здесь обрабатывается исключение, чтобы продолжить выполнение, если файл не найден
#     try:
#         process_file(file)
#     except FileNotFoundError as ex:
#         handle_exception(ex)
#     ```
# 5. **Исключения**:
#     - Документируются исключения для классов, методов и функций.
#     - Указывается, какие исключения могут быть вызваны и при каких обстоятельствах.
#
#
# Пример документации исключений:
# ```markdown
# # Exception: File Not Found
#
# This exception is raised when a file is not found during processing.
#
# ## Parameters
# - `file`: The path of the file that was not found.
#
# ## Example Usage
#
# ```python
# try:
#     open(file)
# except FileNotFoundError as ex:
#     raise FileNotFoundError("File not found") from ex
# ```
# ```
#
#
# Следуйте этим инструкциям для документирования вашего кода. Все комментарии
# должны быть ясными, информативными и соответствовать стандарту Markdown.