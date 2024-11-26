## File: hypotez/src/utils/convertors/html.py

# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.utils.convertors
	:platform: Windows, Unix
	:synopsis: HTML conversion utilities
Functions:
    - `html2escape`: Convert HTML to escape sequences.
    - `escape2html`: Convert escape sequences to HTML.
    - `html2dict`: Convert HTML to dictionaries.
    - `html2ns`: Convert HTML to SimpleNamespace objects.
    https://stackoverflow.com/questions/73599970/how-to-solve-wkhtmltopdf-reported-an-error-exit-with-code-1-due-to-network-err
https://chatgpt.com/share/672266a3-0048-800d-a97b-c38f647d496b
"""
MODE = 'dev'
import re
from typing import Dict
from pathlib import Path
from venv import logger
from src.utils.string import StringFormatter
from src.logger import logger
from types import SimpleNamespace
from html.parser import HTMLParser
from xhtml2pdf import pisa
try:
    from weasyprint import HTML
except Exception as ex:
    logger.error(ex)
    ...

def html2escape(input_str: str) -> str:
    """
    Convert HTML to escape sequences.

    Args:
        input_str (str): The HTML code.

    Returns:
        str: HTML converted into escape sequences.

    Example:
        >>> html = "<p>Hello, world!</p>"
        >>> result = html2escape(html)
        >>> print(result)
        &lt;p&gt;Hello, world!&lt;/p&gt;
    """
    return StringFormatter.escape_html_tags(input_str)

def escape2html(input_str: str) -> str:
    """
    Convert escape sequences to HTML.

    Args:
        input_str (str): The string with escape sequences.

    Returns:
        str: The escape sequences converted back into HTML.

    Example:
        >>> escaped = "&lt;p&gt;Hello, world!&lt;/p&gt;"
        >>> result = escape2html(escaped)
        >>> print(result)
        <p>Hello, world!</p>
    """
    return StringFormatter.unescape_html_tags(input_str)

def html2dict(html_str: str) -> Dict[str, str]:
    """
    Convert HTML to a dictionary where tags are keys and content are values.

    Args:
        html_str (str): The HTML string to convert.

    Returns:
        dict: A dictionary with HTML tags as keys and their content as values.

    Example:
        >>> html = "<p>Hello</p><a href='link'>World</a>"
        >>> result = html2dict(html)
        >>> print(result)
        {'p': 'Hello', 'a': 'World'}
    """
    class HTMLToDictParser(HTMLParser):
        def __init__(self):
            super().__init__()
            self.result = {}
            self.current_tag = None

        def handle_starttag(self, tag, attrs):
            self.current_tag = tag

        def handle_endtag(self, tag):
            self.current_tag = None

        def handle_data(self, data):
            if self.current_tag:
                self.result[self.current_tag] = data.strip()

    parser = HTMLToDictParser()
    parser.feed(html_str)
    return parser.result

def html2ns(html_str: str) -> SimpleNamespace:
    """
    Convert HTML to a SimpleNamespace object where tags are attributes and content are values.

    Args:
        html_str (str): The HTML string to convert.

    Returns:
        SimpleNamespace: A SimpleNamespace object with HTML tags as attributes and their content as values.

    Example:
        >>> html = "<p>Hello</p><a href='link'>World</a>"
        >>> result = html2ns(html)
        >>> print(result.p)
        Hello
        >>> print(result.a)
        World
    """
    html_dict = html2dict(html_str)
    return SimpleNamespace(**html_dict)


def html2pdf(html_str: str, pdf_file: str | Path) -> bool | None:
    """Converts HTML content to a PDF file using WeasyPrint."""
    try:
        HTML(string=html_str).write_pdf(pdf_file)
        return True
    except Exception as e:
        print(f"Error during PDF generation: {e}")
        return
```

```
<algorithm>
**Step 1: Input HTML String**
    * Input: html_str (string) containing HTML code
    * Example: "<p>Hello</p><a href='link'>World</a>"

**Step 2:  html2escape (Optional)**
    * Input: html_str
    * Output: Escaped HTML string
    * Example: "&lt;p&gt;Hello&lt;/p&gt;&lt;a href=&quot;link&quot;&gt;World&lt;/a&gt;"
    * This step is optional but potentially useful in some scenarios, handling HTML entities.

**Step 3:  html2dict**
    * Input: html_str
    * Output: Dictionary where tags are keys and text content are values
    * Example: {'p': 'Hello', 'a': 'World'}
    * This function parses the HTML structure using an HTMLParser subclass.

**Step 4: html2ns**
    * Input: html_str
    * Output: SimpleNamespace object with attributes corresponding to HTML tags
    * Example: object with attributes `.p` = 'Hello', `.a` = 'World'
    * This function leverages the dictionary produced by html2dict to create an object where accessing `.p` returns 'Hello', etc.


**Step 5: html2pdf**
    * Input: html_str (HTML code), pdf_file (string representing PDF file path)
    * Output: True if PDF generation successful, None otherwise
    * Example: html_str as above, pdf_file = 'output.pdf'
    * This function attempts to generate a PDF using WeasyPrint from the HTML string.  Error handling is included.


**Data Flow Diagram (Simplified):**

```
+-----------------+     +-----------------+     +-------------------+
|     html_str     | --> |  html2dict()  | --> |   html2ns()     |
+-----------------+     +-----------------+     +-------------------+
                     |                    |                     |
                     |                    |                     |
                     V                    V                    V
+-----------------+     +-----------------+     +---------------------+
|       dict      | --> | SimpleNamespace  | --> | WeasyPrint(pdf_file)|
+-----------------+     +-----------------+     +---------------------+
```

```
</algorithm>
```

```
<explanation>

**Imports:**

- `re`: Regular expression operations (used in potential PDF preprocessing)
- `typing`: Type hints for better code readability and maintainability.
- `pathlib`: For interacting with file paths.
- `venv`:  Potentially related to virtual environment management.
- `logger`: Likely a custom logger from the `src` package, facilitating logging for debugging and monitoring.
- `StringFormatter`: Custom utility for string formatting/manipulation in the `src.utils.string` module, used for HTML escaping.
- `SimpleNamespace`: Creates an object with attributes for easy access to tag content in `html2ns`.
- `HTMLParser`: Parses HTML, useful for structure-oriented processing of the HTML in `html2dict`.
- `xhtml2pdf`:  Handles conversion from HTML to PDF through pisa.
- `weasyprint`: Alternative, potentially more robust, PDF generation library.

**Classes:**

- `HTMLToDictParser(HTMLParser)`:  A subclass of `HTMLParser` to extract tag and content data from HTML.
    - `__init__`: Initializes the parser and an empty dictionary to store results.
    - `handle_starttag`: Stores the current tag being processed.
    - `handle_endtag`: Resets the current tag to `None` upon encountering closing tags.
    - `handle_data`: Extracts the text content within the current tag, removing any extra whitespace.

**Functions:**

- `html2escape`: Escapes HTML tags within a string.
- `escape2html`: Reverses the HTML escaping process.
- `html2dict`: Parses the HTML into a dictionary where keys are tags and values are tag content.
- `html2ns`: Creates a `SimpleNamespace` object from the parsed HTML dictionary.
- `html2pdf`: This is the crucial function for converting HTML to PDF. It uses the `weasyprint` library, which is more modern and generally more robust than `xhtml2pdf`.


**Variables:**

- `MODE`: A string variable set to 'dev', likely for conditional behavior.
- `logger`: An instance of a logger object for recording messages.

**Potential Errors/Improvements:**

- The code includes a `try...except` block for `weasyprint` import, which is good error handling practice.
- The commented-out `html2pdf` implementation using `xhtml2pdf` has potential errors. The error handling within `html2pdf` is more complete and better handles issues, potentially arising from user input issues.
- `StringFormatter`:  Using a custom formatter class is preferable for maintainability but should be thoroughly documented.


**Relationships:**

- The code relies on `src.utils.string` (StringFormatter) for string manipulation (escaping), indicating a dependency on that module.
- It relies on a `src.logger` module for logging.
- This `html` converter is likely a helper for other functionalities in the project.  This might include functions for generating reports, documents, or other output formats.


```
</explanation>