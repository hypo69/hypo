## <input code>
```python
## \file hypotez/src/utils/convertors/md2dict.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.utils.convertors 
	:platform: Windows, Unix
	:synopsis: Модуль для конвертации строки Markdown в структурированный словарь, включая извлечение JSON содержимого, если оно присутствует.
"""
MODE = 'dev'
import re
from typing import Dict
from markdown2 import markdown
from src.logger import logger

def md2dict(md_string: str) -> Dict[str, dict | list]:
    """
    Конвертирует строку Markdown в структурированный словарь с извлечением JSON содержимого, если оно присутствует.

    Args:
        md_string (str): Строка Markdown для конвертации.

    Returns:
        Dict[str, dict | list]: Структурированное представление Markdown содержимого.
        Возвращает словарь с ключом "json", если найден JSON контент, или словарь с секциями Markdown.
    """
    try:
        json_content = extract_json_from_string(md_string)
        if json_content:
            return {"json": json_content}

        html = markdown(md_string)
        sections: Dict[str, list] = {}
        current_section: str | None = None

        for line in html.splitlines():
            if line.startswith('<h'):
                heading_level_match = re.search(r'h(\d)', line)
                if heading_level_match:
                    heading_level = int(heading_level_match.group(1))
                    section_title = re.sub(r'<.*?>', '', line).strip()

                    if heading_level == 1:
                        current_section = section_title
                        sections[current_section] = []
                    elif current_section:
                        sections[current_section].append(section_title)

            elif line.strip() and current_section:
                clean_text = re.sub(r'<.*?>', '', line).strip()
                sections[current_section].append(clean_text)

        return sections

    except Exception as ex:
        logger.error("Ошибка при парсинге Markdown в структурированный словарь.", exc_info=True)
        return {}


def extract_json_from_string(text: str) -> dict | None:
    """
    Извлекает JSON контент из строки, если он присутствует.

    Args:
        text (str): Строка для извлечения JSON контента.

    Returns:
        dict | None: Извлеченный JSON контент или `None`, если JSON не найден.
    """
    try:
        json_pattern = r'\{.*\}'
        json_match = re.search(json_pattern, text, re.DOTALL)
        if json_match:
            return eval(json_match.group())  # Используем eval для упрощения примера
        return None
    except Exception as ex:
        logger.error("Ошибка извлечения JSON из строки.", exc_info=True)
        return None
```

```
## <algorithm>

**Step 1: Input Markdown String**
*   **Input:** A string containing Markdown text.
*   **Example:** `# Heading 1\nSome text.\n\n{ { "key": "value" } } \n## Heading 2\nMore text.`

**Step 2: JSON Extraction**
*   **Input:** The Markdown string.
*   **Process:** The `extract_json_from_string` function searches for a JSON block (surrounded by curly braces) within the Markdown string using regular expressions.
*   **Output:** If JSON is found, the extracted JSON data as a Python dictionary, otherwise `None`.
*   **Example:**  Returns `{'key': 'value'}` from the input example.

**Step 3: Conditional Output Based on JSON Result**
*   **Input:** The result of JSON extraction (either a dictionary or None)
*   **Process:** If JSON is found, returns a dictionary with the key 'json' and the value as the extracted JSON data.  Otherwise, proceed to Markdown parsing.
*   **Output:** If JSON present, returns `{"json": {'key': 'value'}}`.

**Step 4: Markdown Conversion to HTML**
*   **Input:** The Markdown string (if no JSON was found).
*   **Process:** The `markdown` function (from the `markdown2` library) converts the Markdown string into HTML.
*   **Output:** HTML representation of the input Markdown string.
*   **Example:**  Converts the Markdown input to HTML.

**Step 5: HTML Parsing and Section Extraction**
*   **Input:** HTML string from step 4.
*   **Process:**  Iterates through the HTML lines. If a line starts with `<h` (heading), extracts the heading level and text.  If the heading level is 1, a new section is started.  Text content is appended to the appropriate section in the `sections` dictionary. 
*   **Output:** A dictionary `sections` where keys are section titles (if they were found) and values are lists of text content.

**Step 6: Error Handling**
*   **Input:** Result of previous steps, or exceptions thrown during processing.
*   **Process:**  Uses a `try-except` block to handle potential errors during JSON extraction, Markdown conversion, or HTML parsing.  Logs errors with `logger` (assuming a logging mechanism is in place).
*   **Output:**  Returns an empty dictionary if any error occurs during processing.

**Step 7: Final Output**
*   **Input:** The result of Markdown parsing (a dictionary of sections) or the JSON result.
*   **Output:** The function returns the resulting dictionary (`sections` or `{"json": ...}`).


```

```
## <explanation>

**Imports:**

*   `re`: Used for regular expressions, primarily for finding JSON blocks and extracting heading levels from HTML.
*   `typing.Dict`:  Defines the type hinting for the return value of `md2dict`, specifying it as a dictionary.
*   `markdown2`:  This library handles converting Markdown to HTML, which is crucial for the section extraction process.
*   `src.logger`:  This is assumed to be a custom logger module (likely part of the project's `src` package) for handling errors and potentially logging useful information during processing.

**Classes:**

*   No classes are defined in this code.

**Functions:**

*   `md2dict(md_string: str) -> Dict[str, dict | list]`:
    *   **Arguments:** `md_string` (str): The Markdown string to be converted.
    *   **Return Value:** `Dict[str, dict | list]`: A dictionary containing either extracted JSON data ('json' key) or a dictionary representing the sections of the Markdown text.
    *   **Functionality:**  This function tries to extract JSON first, if present, it returns a dictionary with that extracted JSON. Otherwise it converts the input Markdown into HTML and extracts sections based on heading levels. Returns an empty dictionary in case of an error.
    *   **Example:**
        ```python
        markdown_text = "# Heading 1\nSome text.\n\n{ \"key\": \"value\" }\n## Heading 2\nMore text."
        result = md2dict(markdown_text)
        print(result)  # Output: {'json': {'key': 'value'}}
        ```

*   `extract_json_from_string(text: str) -> dict | None`:
    *   **Arguments:** `text` (str): The input string to search for JSON within.
    *   **Return Value:** `dict | None`: Returns a Python dictionary if JSON is found, otherwise `None`.
    *   **Functionality:**  This function uses a regular expression to find a JSON block within the input string. If found, it uses `eval()` to parse the JSON string into a Python dictionary.  The use of `eval()` is a potential security risk (see below).
    *   **Example:**
        ```python
        text = "# Heading 1\nSome text.\n\n{ \"key\": \"value\" }"
        json_data = extract_json_from_string(text)
        print(json_data)  # Output: {'key': 'value'}
        ```

**Variables:**

*   `MODE`:  A string ('dev') indicating the current mode (likely for debugging or different configurations).
*   `json_content`:  Stores the extracted JSON data if found.
*   `html`:  Stores the HTML representation of the input Markdown.
*   `sections`: A dictionary that will contain the extracted section data.
*   `current_section`:  Keeps track of the currently processed section.
*   `json_pattern`: A regular expression pattern for finding JSON blocks in a string.

**Potential Errors and Improvements:**

*   **Security Risk with `eval()`**: The use of `eval()` to parse the JSON string is a significant security vulnerability.  Never use `eval()` to parse untrusted data, especially JSON, from external sources.  A safer way to parse JSON would be using the `json` module:  `import json; return json.loads(json_match.group())`
*   **Robustness**: The code doesn't handle cases where the Markdown input is invalid or doesn't conform to expected structure.  Adding more robust error handling could help with handling different Markdown input scenarios.
*   **Input Validation**: Input sanitation and validation (e.g., checking for malformed JSON) would prevent unexpected behavior or errors.
*   **Error Logging**: The use of `logger.error` to log exceptions is a good practice, but it would be even better to add more specific error messages (e.g., logging the type of error that occurred).

**Relationship with Other Parts of the Project:**

*   The `src.logger` module is a dependency and likely part of a larger logging infrastructure within the project.  This function utilizes the `logger` module to log errors and potentially other important information.