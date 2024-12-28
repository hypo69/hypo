# md2dict.py Code Explanation

## <input code>

```python
## \file hypotez/src/utils/convertors/md2dict.py
# -*- coding: utf-8 -*-\
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.utils.convertors.md2dict 
	:platform: Windows, Unix
	:synopsis: Модуль для конвертации строки Markdown в структурированный словарь, включая извлечение JSON содержимого, если оно присутствует.
"""

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

## <algorithm>

**Step 1:** Input Markdown string (`md_string`)

**Step 2:** Try to extract JSON from `md_string` (using `extract_json_from_string`).

**Step 3:** If JSON is found, return a dictionary with the key "json" and the extracted JSON value.

**Step 4:** If JSON is not found:
    * Convert the Markdown string to HTML using `markdown`.
    * Initialize an empty dictionary `sections` to store the extracted sections.
    * Initialize `current_section` to `None`.
    * Iterate over lines in the HTML string:
        * If the line starts with `<h` (heading):
            * Extract the heading level and title.
            * If heading level is 1, create a new section in `sections`.
            * Otherwise, append the title to the current section.
        * If the line is not empty and `current_section` is not `None`, append the cleaned text (removing HTML tags) to the current section.
    * Return the `sections` dictionary.


**Example:**

Input Markdown:
```markdown
# Title 1
Some text
## Subtitle 1
More text
{ "key": "value" }
```

Output (dictionary):
```json
{
  "Title 1": [
    "Some text",
    "Subtitle 1",
    "More text"
  ]
}
```


## <mermaid>

```mermaid
graph TD
    A[Input Markdown] --> B{Extract JSON?};
    B -- Yes --> C[Return {"json": JSON}];
    B -- No --> D[Convert to HTML];
    D --> E[Iterate lines];
    E --> F{Line starts with <h?};
    F -- Yes --> G[Extract Heading];
    G --> H{Heading level = 1?};
    H -- Yes --> I[Create new section];
    H -- No --> J[Append to current section];
    F -- No --> K{Line is not empty and current_section exists?};
    K -- Yes --> L[Clean text and append];
    K -- No --> E;
    I --> E;
    J --> E;
    L --> E;
    E --> M[Return sections];
    C --> N[Output];
    M --> N;
```

**Explanation of Dependencies:**

* `re`: The regular expression module is used for pattern matching (e.g., extracting JSON and heading levels).
* `typing`: Used for type hinting.
* `markdown2`:  A Markdown-to-HTML converter. This is a separate library that needs to be installed (`pip install markdown2`).  The dependency signifies a crucial function: converting Markdown to a structured form (HTML) is a significant part of the algorithm.
* `src.logger`:  Custom logger from the `src` package.  This suggests a logging mechanism is in place for error handling, allowing the calling function to know about potential issues.


## <explanation>

**Imports:**

* `re`: Used for regular expressions to find JSON patterns and extract headings. Crucial for parsing specific formats.
* `typing`: Used for type hinting, improving code readability and maintainability.
* `markdown2`: The `markdown` function is used to convert Markdown text into HTML.  This import is critical; without it, Markdown cannot be interpreted. The function's use is to prepare the Markdown for section-based parsing.
* `src.logger`: This is a custom logging module likely defined in the `src` package, likely used to handle errors during the conversion process and potentially other situations.

**Classes:**

There are no classes in this code.

**Functions:**

* `md2dict(md_string)`: Takes a Markdown string as input and returns a dictionary representing the structured content. It first attempts to extract JSON from the input. If successful, it returns a dictionary containing the JSON. Otherwise, it converts the Markdown to HTML, extracts sections based on headings, and returns a dictionary with section titles as keys and a list of extracted text elements as values.
* `extract_json_from_string(text)`: Extracts JSON from a string. It uses regular expressions to find the JSON portion and the `eval` function to parse it. This method is error-prone and is not recommended in real-world scenarios; using a dedicated JSON parser is safer.


**Variables:**

* `MODE`: A string variable likely used for configuration (e.g., 'dev' or 'prod').
* `json_content`: Stores extracted JSON, if found.
* `html`: Stores the HTML representation of the Markdown input.
* `sections`: A dictionary to store extracted Markdown sections.
* `current_section`: Tracks the currently processed section title.
* `heading_level_match`: Stores the result of regular expression matching against headings.
* `heading_level`: Stores the level of the heading (e.g., 1 for `<h1>`).
* `section_title`: Stores the text of the heading.
* `clean_text`: Stores the text with HTML tags removed.

**Potential Errors and Improvements:**

* **`eval()` in `extract_json_from_string`:** Using `eval()` to parse JSON is highly discouraged, as it opens up significant security vulnerabilities. It's essential to use a dedicated JSON parsing library like `json.loads` instead.  This directly impacts the safety of the application.
* **Error Handling:** While `try...except` blocks are present, more specific exception handling (e.g., `json.JSONDecodeError`) would improve the robustness of the `extract_json_from_string` function.
* **Robustness:** The code assumes that the input Markdown will contain valid JSON and headings. Adding more validation and handling for malformed inputs would significantly enhance the function's reliability.

**Chain of Relationships:**

The `md2dict` function likely is called by other parts of the application (`src` package) to convert Markdown text into structured data. This data would then be used for further processing or display. The `logger` component suggests the function is part of a larger system that records and handles errors effectively.