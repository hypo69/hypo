## File: hypotez/src/utils/jjson.py
# -*- coding: utf-8 -*-\n#! venv/Scripts/python.exe\n#! venv/bin/python/python3.12\n\n"""
.. module: src.utils 
	:platform: Windows, Unix
	:synopsis: Module for handling JSON and CSV files, including loading, dumping, and merging data.
 This module provides functions to:
- **Dump JSON data**: Convert JSON or SimpleNamespace objects into JSON format and write to a file, or return the JSON data as a dictionary.
- **Load JSON and CSV data**: Read JSON or CSV data from a file, directory, or string, and convert it into dictionaries or lists of dictionaries.
- **Convert to SimpleNamespace**: Convert loaded JSON data into SimpleNamespace objects for easier manipulation.
- **Merge JSON files**: Combine multiple JSON files from a directory into a single JSON file.
- **Parse Markdown**: Convert Markdown strings to JSON format for structured data representation.

The functions in this module handle various aspects of working with JSON and CSV data, ensuring that data is loaded, saved, and merged efficiently and effectively.
"""
MODE = 'dev'
from datetime import datetime
from math import log
from pathlib import Path
from typing import List, Dict, Optional, Any
from types import SimpleNamespace
import json
import os
import re
import pandas as pd
from json_repair import repair_json
from typing import Any
from pathlib import Path
import json
import pandas as pd
from types import SimpleNamespace
from collections import OrderedDict

from src.logger import logger
from src.utils.printer import pprint
from .convertors.dict import dict2ns

def j_dumps(
    data: Dict | SimpleNamespace | List[Dict] | List[SimpleNamespace],
    file_path: Optional[Path] = None,
    ensure_ascii: bool = True,
    mode: str = "w",
    exc_info: bool = True,
) -> Optional[Dict]:
    """Dump JSON data to a file or return the JSON data as a dictionary."""
    # ... (function body)
```

```
<algorithm>
**j_dumps Function:**

1. **Input:** JSON data (Dict, SimpleNamespace, list of Dict/SimpleNamespace), optional file path, ensure_ascii flag, write mode, exception info flag.

2. **Data Conversion (convert_to_dict):** Converts SimpleNamespace objects to dictionaries recursively to handle nested structures.  
   * **Example:** `SimpleNamespace(name="Alice", age=30)` becomes `{"name": "Alice", "age": 30}`.

3. **File Mode Handling:** Checks if the file mode is valid (`"w"`, `"a+"`, or `"+a"`). If not, defaults to `"w"`.
   * **Example:** If `mode="x"`, it's changed to `mode="w"`

4. **Existing Data Handling (if applicable):**  If file exists and mode is `"a+"` or `"+a"`, loads existing data from the file.  Handles `JSONDecodeError` and other potential read exceptions.
   * **Example:** If the file already contains `{"count": 10}`, and mode is `"a+"`, the `existing_data` becomes this.

5. **Data Processing:**
   * If `mode="a+"`, updates the existing data with the new data.
   * If `mode="+a"`, updates the new data with existing data.

6. **Write to File (if file path is provided):** Creates parent directories if they don't exist. Writes the processed data to the file with proper indentation. Handles potential writing exceptions.
   * **Example:** Writes the data as a properly formatted JSON to a file.


7. **Return Value:** Returns the data as a dictionary if no file path was provided, otherwise returns nothing.



**j_loads Function:**

1. **Input:** JSON data (file path, directory path, string, dictionary, list of dictionaries).


2. **String Cleaning (clean_string):** Removes triple backticks and "json" from the beginning and end of strings, if present.

3. **File Handling (if jjson is a Path):**
   * If it's a directory, recursively loads all `.json` files within and merges their data into a single dictionary. Handles the case where no `.json` files are present.
   * If it's a `.csv` file, loads it with pandas.
   * If it's a `.json` file, loads its content. Handles potential file not found errors and other load exceptions.


4. **String Handling (if jjson is a string):**
   * Cleans the input string.
   * Loads the JSON data from the string.
   * Attempts to fix invalid JSON using `repair_json`.

5. **Dictionary Handling (if jjson is a dictionary):** Returns the dictionary directly.

6. **Error Handling:** Catches and logs `FileNotFoundError`, `json.JSONDecodeError`, and other exceptions.

7. **Return Value:** Returns the loaded JSON data as a dictionary or list of dictionaries, or `None` if an error occurs.


**j_loads_ns Function:**

1. **Input:** JSON data (similar to j_loads).


2. **Data Loading:** Calls `j_loads` to load the data.


3. **Conversion to SimpleNamespace:** Converts the loaded data into `SimpleNamespace` or a list of `SimpleNamespace` objects using `dict2ns`.


4. **Error Handling:** Catches exceptions during loading and conversion.

5. **Return Value:** Returns the loaded data as `SimpleNamespace` or a list of `SimpleNamespace` objects if successful. Returns `None` otherwise.


**replace_key_in_json Function:**

1. **Input:** Dictionary or list of dictionaries, old key, new key.

2. **Recursive Key Replacement:** Recursively traverses the structure replacing all instances of the old key with the new key.


3. **Return Value:** Updated dictionary or list.


**process_json_file Function:**

1. **Input:** Path to a JSON file.

2. **Loading and Replacing:** Loads the JSON data, replaces `name` with `category_name` using `replace_key_in_json`, and saves the updated data back to the file.


3. **Error Handling:** Handles potential loading and saving errors.


**recursive_process_json_files Function:**

1. **Input:** Directory path.

2. **Recursive Processing:** Recursively traverses the directory and its subdirectories, processing each JSON file found using `process_json_file`.


**extract_json_from_string Function:**

1. **Input:** Markdown string.


2. **Regular Expression Matching:** Uses a regular expression to find JSON content enclosed within ```json ``` tags.


3. **Error Handling:** Handles potential errors during regex matching.

4. **Return Value:** Extracted JSON string, or an empty string if no JSON is found.
```

```
<explanation>

**Imports:**

- `datetime`, `log`, `Path`: Standard library modules for date and time handling, mathematical functions, and file path manipulation, respectively. These are essential for various general-purpose tasks.
- `List`, `Dict`, `Optional`, `Any`, `SimpleNamespace`: Typing modules, crucial for type hinting to improve code readability and maintainability.
- `json`, `os`, `re`, `pandas`: Essential for JSON processing, operating system interactions, regular expressions, and data manipulation (specifically for CSV handling).
- `json_repair`: Likely a third-party library specifically for fixing malformed JSON data.
- `src.logger`, `src.utils.printer`, `.convertors.dict`: Imports from other modules within the `hypotez` project.  `logger` provides logging capabilities, `pprint` likely offers pretty printing of data structures, and `dict2ns` converts dictionaries to `SimpleNamespace` objects.


**Classes:**

There are no classes defined directly within this file. The `SimpleNamespace` class is used extensively. It is imported from the `types` module and provides a way to create objects with attributes similar to dictionaries. This class is common when data is expected to be structured but doesn't necessarily need the full complexity of a Python class.



**Functions:**

- `j_dumps`: Dumps JSON data to a file or returns it as a dictionary.  It takes JSON-compatible data, an optional file path,  and various flags to control formatting and error handling.  Handles existing data during append operations.  Critically, it converts `SimpleNamespace` objects to dictionaries during the dump process.
- `j_loads`: Loads JSON or CSV data from a file, directory, or string. It is highly versatile, supporting both `.json` and `.csv` files, as well as JSON in strings.  It cleverly handles JSON data in markdown strings, and directories full of JSON files. This is a powerful utility function.
- `j_loads_ns`: Loads JSON data and converts it into `SimpleNamespace` objects (or a list of `SimpleNamespace` objects if the data is a list). This function simplifies data access after loading.
- `replace_key_in_json`: Recursively replaces a key in a nested dictionary or list of dictionaries. It's a utility function for data manipulation.
- `process_json_file`, `recursive_process_json_files`: Functions for processing and replacing keys within JSON files in specified directories. Useful for large-scale data transformations.
- `extract_json_from_string`: Extracts JSON content from a Markdown string. Useful for parsing structured data embedded within Markdown documentation or reports.


**Variables:**

- `MODE`: A string variable likely used for configuring the module's behavior (development/production).
- Other variables are function parameters and local variables used for intermediate storage during data loading, formatting and file handling.  `existing_data` is important for updating existing JSON files.


**Potential Errors and Improvements:**

- **Robustness:** The error handling in `j_loads` and `j_dumps` is good but could be more comprehensive (e.g., handling all possible exceptions during file operations or JSON parsing).   The `except ...: ...` blocks are a bit too broad and should be more specific, at least with descriptive logging messages.
- **Explicit Typing:** The typing annotations are mostly present but could be more explicit for functions returning lists of dictionaries, especially when nested structures are involved.
- **File Handling:** The use of `encoding="utf-8"` in file operations is generally good practice to avoid issues with character encoding.
- **Consistency:** Consider whether using `Path` objects throughout is necessary or if a mix of strings and Path objects is fine. The use of `Path` in some cases but not others in a function like `j_loads` can make it less clear how it handles the inputs and needs more commenting.
- **Clarity in `j_loads`**: The `dict_list` handling and conditional merging in `j_loads` could be clearer.


**Relationships with Other Parts of the Project:**

The `logger` and `pprint` functions indicate that this module interacts with other components of the `hypotez` project.  The `dict2ns` converter likely comes from a `src.utils.convertors.dict` module.  The `repair_json` function is assumed to be external, but part of the `hypotez` project's package.  This highlights that this module likely plays a vital role in managing data formats for various parts of the project.