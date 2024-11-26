## File: hypotez/src/utils/convertors/ns.py
# -*- coding: utf-8 -*-\
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.utils.convertors 
	:platform: Windows, Unix
	:synopsis: convert SimpleNamespace (ns) into various formats: dict, JSON, CSV, XML, and XLS

Functions:
    - ns2dict: Convert SimpleNamespace object to a dictionary.
    - ns2json: Convert SimpleNamespace object to JSON format.
    - ns2csv: Convert SimpleNamespace object to CSV format.
    - ns2xml: Convert SimpleNamespace object to XML format.
    - ns2xls: Convert SimpleNamespace object to XLS format.
"""
MODE = 'dev'
import json
import csv
from types import SimpleNamespace
from pathlib import Path
from typing import List, Dict
from src.utils.convertors import xml2dict
from src.utils.csv import save_csv_file
from src.utils.jjson import j_dumps
from src.utils.xls import save_xls_file
from src.logger import logger

def ns2dict(ns_obj: SimpleNamespace) -> dict:
    """
    Convert SimpleNamespace object to a dictionary.

    Args:
        ns_obj (SimpleNamespace): The SimpleNamespace object to convert.

    Returns:
        dict: Converted dictionary.
    """
    return vars(ns_obj)

def ns2json(ns_obj: SimpleNamespace, json_file_path: str | Path = None) -> str | bool:
    """
    Convert SimpleNamespace object to JSON format.

    Args:
        ns_obj (SimpleNamespace): The SimpleNamespace object to convert.
        json_file_path (str | Path, optional): Path to save the JSON file. If not provided, returns the JSON string.

    Returns:
        str | bool: JSON string if no file path is provided, otherwise True if the file is written successfully.
    """
    try:
        data = ns2dict(ns_obj)
        json_data = json.dumps(data, indent=4)
        
        if json_file_path:
            with open(json_file_path, 'w', encoding='utf-8') as json_file:
                json_file.write(json_data)
            return True
        return json_data
    except Exception as ex:
        logger.error(f"ns2json failed", ex, True)

def ns2csv(ns_obj: SimpleNamespace, csv_file_path: str | Path) -> bool:
    """
    Convert SimpleNamespace object to CSV format.

    Args:
        ns_obj (SimpleNamespace): The SimpleNamespace object to convert.
        csv_file_path (str | Path): Path to save the CSV file.

    Returns:
        bool: True if successful, False otherwise.
    """
    try:
        data = [ns2dict(ns_obj)]
        save_csv_file(data, csv_file_path)
        return True
    except Exception as ex:
        logger.error(f"ns2csv failed", ex, True)


def ns2xml(ns_obj: SimpleNamespace, root_tag: str = "root") -> str:
    """
    Convert SimpleNamespace object to XML format.

    Args:
        ns_obj (SimpleNamespace): The SimpleNamespace object to convert.
        root_tag (str): The root element tag for the XML.

    Returns:
        str: The resulting XML string.
    """
    try:
        data = ns2dict(ns_obj)
        return xml2dict(data)
    except Exception as ex:
        logger.error(f"ns2xml failed", ex, True)


def ns2xls(data: SimpleNamespace, xls_file_path: str | Path) -> bool:
    """
    Convert SimpleNamespace object to XLS format.

    Args:
        ns_obj (SimpleNamespace): The SimpleNamespace object to convert.
        xls_file_path (str | Path): Path to save the XLS file.

    Returns:
        bool: True if successful, False otherwise.
    """
    return save_xls_file(data,xls_file_path)
```

```
<algorithm>
1. **Input:** A SimpleNamespace object (`ns_obj`).
   - *Example*: `ns_obj = SimpleNamespace(name="Alice", age=30)`

2. **Convert to Dictionary (`ns2dict`):**
   - Takes the `ns_obj` as input.
   - Uses `vars(ns_obj)` to convert the SimpleNamespace into a dictionary.
   - *Example Output*: `{'name': 'Alice', 'age': 30}`

3. **Convert to JSON (`ns2json`):**
   - Takes the `ns_obj` and optional `json_file_path` as input.
   - Calls `ns2dict` to get the dictionary representation.
   - Uses `json.dumps` to convert the dictionary to a JSON string, with indentation for readability.
   - *Example output string*: `"{\"name\": \"Alice\", \"age\": 30}\n"`
   - If `json_file_path` is provided, writes the JSON string to the file.
   - *Example*: `ns2json(ns_obj, "output.json")` will save the JSON to a file.

4. **Convert to CSV (`ns2csv`):**
   - Takes the `ns_obj` and `csv_file_path` as input.
   - Calls `ns2dict` to get the dictionary.
   - Creates a list containing the dictionary.
   - Calls `save_csv_file` to write the list (which is a single dictionary in this case) to the CSV file.


5. **Convert to XML (`ns2xml`):**
   - Takes `ns_obj` and optional `root_tag` as input.
   - Calls `ns2dict` to get the dictionary.
   - Calls `xml2dict` (from a separate module) to convert the dictionary to an XML string.
   - *Example output string*: `"<root><name>Alice</name><age>30</age></root>"`

6. **Convert to XLS (`ns2xls`):**
   - Takes the `ns_obj` and `xls_file_path` as input.
   - Calls `save_xls_file` (from a separate module) to save the data to an XLS file.

```

```
<explanation>

**Imports:**

- `json`: Used for encoding and decoding JSON data.
- `csv`: Used for handling CSV files.
- `types.SimpleNamespace`: Provides the `SimpleNamespace` class for creating namespace objects.
- `pathlib.Path`: Used for working with file paths in a more object-oriented way.
- `typing.List`, `typing.Dict`: Used for type hinting (clarifying data types).
- `src.utils.convertors.xml2dict`: Likely handles converting Python dictionaries to XML strings (details depend on implementation within `xml2dict`).
- `src.utils.csv.save_csv_file`: Handles saving data to CSV files.
- `src.utils.jjson.j_dumps`: (Likely) a custom function related to JSON, possibly for handling specific JSON output requirements (needs more context to confirm).
- `src.utils.xls.save_xls_file`: Handles saving data to XLS files.
- `src.logger`: Handles logging, probably using a custom logger for structured output.  Important for error handling.

**Classes:**

- `SimpleNamespace`: A built-in class (not explicitly defined here) used to create objects with attributes like a dictionary (more concise way to create such objects).  This approach is commonly used for configuration objects.

**Functions:**

- `ns2dict(ns_obj)`: Converts a `SimpleNamespace` object into a dictionary, returning it.  It's a simple helper function, but crucial for all other conversion functions.

- `ns2json(ns_obj, json_file_path=None)`: Converts a `SimpleNamespace` to JSON. Returns the JSON string if `json_file_path` is not provided.  If a file path is provided, it saves the JSON to a file and returns `True` to indicate success.  Includes a `try...except` block for robust error handling.

- `ns2csv(ns_obj, csv_file_path)`: Converts a `SimpleNamespace` to CSV format and saves it to the given file path. It returns `True` if the save is successful, and `False` otherwise.  It has a `try...except` block for robust error handling.

- `ns2xml(ns_obj, root_tag="root")`: Converts a `SimpleNamespace` to XML format and returns it as a string.

- `ns2xls(data, xls_file_path)`: Converts a `SimpleNamespace` (or equivalent data) to XLS format and saves it. Returns `True` on success, `False` otherwise.


**Variables:**

- `MODE`: A global variable, likely for setting the execution mode (e.g., development vs. production).


**Potential Errors/Improvements:**

- **Error Handling:** All conversion functions use `try...except` blocks, which is good practice for robust code. The `logger` framework is used to record errors.
- **Data Validation:**  No explicit data validation for input `ns_obj`.  The functions rely on the expected format of the input.  More validation (e.g., checking if required attributes are present in `ns_obj`) could be added for robustness.
- **Type Hinting:** The `typing` imports are used properly. 
- **`ns2xls`:**  The `data` argument in this function is expected to be a `SimpleNamespace`  but the function's signature suggests it expects a different object type.  This is potentially a sign of a naming conflict or a missing type specification. 
- **`src` Modules:**  The code relies on the existence of `src.utils.csv`, `src.utils.jjson`, `src.utils.xls`, `src.logger`, and `src.utils.convertors` modules.  These modules should be present for the code to function correctly.


**Relationships:**

This module (`ns.py`) relies on other modules within the `src` package, particularly for CSV, JSON, XML, and XLS file handling.  The `src.utils.convertors.xml2dict` function is key for the XML conversion. The error handling also ties in the `src.logger` module for logging of exceptions.