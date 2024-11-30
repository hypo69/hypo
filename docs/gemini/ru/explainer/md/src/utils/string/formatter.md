# <input code>

```python
## \file hypotez/src/utils/string/formatter.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.utils.string 
	:platform: Windows, Unix
	:synopsis: String formatting functions.

Functions:
    - remove_line_breaks(input_str: str) -> str
    - remove_htmls(input_html: str) -> str
    - escape_html_tags(input_html: str) -> str
    - escape_to_html(text: str) -> str
    - remove_non_latin_characters(input_str: str) -> str
    - remove_special_characters(input_str: str | list) -> str
    - clear_numbers(input_str: str) -> str

Data transformation:
    - convert_to_list(input: str | list[str, dict, list[dict]], delimiter: str = ',') -> list
    - extract_value_from_parentheses_with_lead_dollar(input_str: str) -> str | list | bool
    - clean_url_from_protocols(url: str) -> str
"""
MODE = 'dev'
import re
import html
from typing import List, Dict
from urllib.parse import urlparse, parse_qs
from src.logger import logger
from .html_escapes import html_escapes

class StringFormatter:
    """
    StringFormatter (String Formatting):

    Provides utility functions for formatting strings, such as removing line breaks, HTML tags, non-Latin characters, and special characters.
    """

    # ... (rest of the code)
```

# <algorithm>

The code defines a `StringFormatter` class containing static methods for various string manipulation tasks.  The algorithm for each method is straightforward and primarily relies on regular expressions (`re`) and string methods like `replace`, `strip`, and `join`.  Let's outline a basic flow for `remove_line_breaks`:

1. **Input:** Receives a string (`input_str`).
2. **Replacement:** Replaces newline characters (`\n` and `\r`) with a space (` `).
3. **Stripping:** Removes leading and trailing whitespace using `.strip()`.
4. **Return:** Returns the modified string.

A similar approach applies to other methods using regular expressions for pattern matching and replacement.

**Example (remove_line_breaks):**

```
Input: "Line 1\nLine 2\r\nLine 3"
Step 1: "Line 1 Line 2 Line 3"
Step 2: "Line 1 Line 2 Line 3" (no change due to strip)
Output: "Line 1 Line 2 Line 3"
```

# <mermaid>

```mermaid
graph TD
    subgraph StringFormatter
        A[input_str] --> B{remove_line_breaks};
        B --> C[input_str.replace("\n", " ")]
        C --> D[input_str.replace("\r", " ")]
        D --> E[input_str.strip()]
        E --> F[return value]
    end
    
    subgraph StringFormatter
    A1[input_html] --> B1{remove_htmls};
    B1 --> C1[re.sub(r'<.*?>', '', input_html)]
    C1 --> D1[input_html.strip()]
    D1 --> E1[return value]
    end
    
    subgraph StringFormatter
       A2[input_str] --> B2{remove_non_latin_characters};
       B2 --> C2[re.sub(r"[^a-zA-Z\s]", "", input_str)]
       C2 --> D2[input_str.strip()]
       D2 --> E2[return value]
    end

    subgraph StringFormatter
       A3[input_str] --> B3{remove_special_characters};
       B3 -- is input a list? --> C3[yes];
       C3 --> D3[ list comprehension with re.sub ]
       B3 -- is input not a list? --> C4[no];
       C4 --> D4[re.sub(r"[^a-zA-Z0-9\s]", "", input_str)]
       D4 --> E3[return value]
    end
    
    F --> G(String)
    E1 --> G(String)
    E2 --> G(String)
    E3 --> G(String)
```

# <explanation>

**Imports:**

- `re`: The regular expression module for pattern matching and replacement.
- `html`: Provides functions for escaping and unescaping HTML entities.
- `typing`: Provides type hints.
- `List`, `Dict`: Type hints from `typing` for lists and dictionaries.
- `urllib.parse`: Module for URL manipulation (parsing).
- `src.logger`: A custom logger likely defined elsewhere in the `src` directory; this is a dependency.
- `.html_escapes`: Import from the `html_escapes` module within the same directory (`utils/string`).  The `html_escapes` module is crucial for character-to-HTML entity conversion.


**Classes:**

- `StringFormatter`: This class encapsulates string formatting utilities.  It's a container for static methods, meaning no instances of the class need to be created.  This is a common design pattern for utility classes.


**Functions:**

- Methods like `remove_line_breaks`, `remove_htmls`, `escape_html_tags`, etc. are all static methods within the `StringFormatter` class.  They take a string as input and return a modified string.  They leverage regular expressions for complex string manipulations.
- `remove_special_characters`: Handles both strings and lists as input.  This is a more robust implementation than if it was designed to just deal with strings. 
- `clear_numbers`:  Removes all characters from a string except digits and periods, leaving only the numerical part of the string.  It's a simple but useful operation.

**Variables:**

- `MODE`: A variable likely set for different development modes (e.g., 'dev', 'prod').


**Possible Errors/Improvements:**

- **Error Handling:**  Adding `try...except` blocks for potential errors (e.g., invalid input types) would make the code more robust.
- **Docstrings:**  While some functions have good docstrings, others could be more comprehensive, including examples.
- **Code Clarity:** Some functions could benefit from more descriptive variable names. For example, instead of `input_html`, a name like `html_string` might be more clear.
- **Input Validation:**  Checking the validity of the input types (`isinstance`) for `remove_special_characters` is a good start but considering handling empty or `None` values for enhanced robustness.


**Relationships with other parts of the project:**

The `src.logger` import suggests a logging system within the project, which would capture error messages or other important events during string formatting operations.  The `html_escapes` dependency hints that a separate module exists to provide a mapping from characters to HTML escapes, which might be used in the larger project for tasks requiring conversion to HTML output.