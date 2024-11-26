# file hypotez/src/utils/csv.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module:: src.utils.csv
	:platform: Windows, Unix
	:synopsis: Utilities for working with CSV and JSON files.
"""

import csv
import json
from pathlib import Path
from types import SimpleNamespace
from typing import List, Dict, Union
import pandas as pd
from src.utils.jjson import j_loads, j_loads_ns, j_dumps
from src.logger import logger
```

```
<algorithm>

**save_csv_file(data, file_path, mode='a', exc_info=True)**

1. **Input Validation:** Checks if 'data' is a list of dictionaries and if it's not empty. Raises TypeError or ValueError if not.
2. **File Handling:** Creates the parent directory of the file if it doesn't exist. Opens the file in the specified mode ('a' for append, 'w' for overwrite).
3. **CSV Writing:** Creates a DictWriter object using the first dictionary in the 'data' list's keys as fieldnames. If the mode is 'w' or the file doesn't exist, it writes the header.  Writes the rows of data using writerows.
4. **Error Handling:** Uses a `try...except` block to catch and log any exceptions that occur during file operations.

Example:
```python
data = [{"col1": "val1", "col2": "val2"}, {"col1": "val3", "col2": "val4"}]
save_csv_file(data, "my_file.csv", mode='w')
```

**read_csv_file(file_path, exc_info=True)**

1. **File Handling:** Opens the file in read mode ('r').
2. **CSV Reading:** Creates a DictReader object to read the CSV data.
3. **Data Extraction:** Reads all rows from the CSV using `list(reader)` and returns the list of dictionaries.
4. **Error Handling:** Uses `try...except` to handle FileNotFoundError and other exceptions during file reading.

Example:
```python
result = read_csv_file("my_file.csv")
```

**read_csv_as_json(csv_file_path, json_file_path, exc_info=True)**

1. **CSV Reading:** Calls `read_csv_file()` to read the CSV data.
2. **Input Validation:** Checks if the `read_csv_file()` returned a valid data set.
3. **JSON Writing:** Creates a JSON file at the specified `json_file_path` containing the data read from CSV. Uses `json.dump()` to write.
4. **Error Handling:** Handles exceptions during both reading and writing.

Example:
```python
read_csv_as_json("my_csv.csv", "my_json.json")
```

**read_csv_as_dict(csv_file)**

1. **CSV Reading:** Opens the CSV file. Creates a DictReader object and collects all rows into a list.
2. **Data Formatting:** Constructs a dictionary with the key "data" containing the list of dictionaries read from the CSV. Returns the dictionary.
3. **Error Handling:** Includes error handling for file operations.

Example:
```python
result = read_csv_as_dict("my_csv.file")
```

**read_csv_as_ns(file_path)**

1. **CSV Loading (Pandas):** Loads the CSV file into a Pandas DataFrame using `pd.read_csv()`.
2. **Data Conversion:** Converts the DataFrame to a list of dictionaries using `df.to_dict(orient='records')`.
3. **Error Handling:** Includes error handling for file not found and general exceptions during loading. Returns an empty list if there's a problem.
```

```
<explanation>

**Imports:**

- `csv`: For working with CSV files.
- `json`: For working with JSON files.
- `pathlib`: For working with file paths in a more object-oriented way.
- `types`: For the `SimpleNamespace` type.
- `typing`: For type hinting (e.g., `List`, `Dict`, `Union`).
- `pandas`: For efficient data manipulation and analysis.
- `src.utils.jjson`: Likely custom functions for handling JSON (loads, dumps, etc.).
- `src.logger`: Likely a custom logging module.


**Classes:**

- None. This code only contains functions.


**Functions:**

- `save_csv_file(data, file_path, mode='a', exc_info=True)`: Saves a list of dictionaries to a CSV file. Takes a list of dictionaries, the file path, optional mode ('a' to append, 'w' to overwrite), and an `exc_info` flag for logging.
- `read_csv_file(file_path, exc_info=True)`: Reads a CSV file into a list of dictionaries. Takes a file path and an optional `exc_info` flag.
- `read_csv_as_json(csv_file_path, json_file_path, exc_info=True)`: Converts a CSV file to JSON format and saves it. Takes the CSV and JSON file paths and an optional `exc_info` flag.
- `read_csv_as_dict(csv_file)`: Converts CSV content to a dictionary. Takes the file path.
- `read_csv_as_ns(file_path)`: Loads CSV data into a list of dictionaries using Pandas. Takes the file path.

**Variables:**

- `data`: A list of dictionaries. Used in `save_csv_file`.
- `file_path`: A string or `Path` object representing the CSV file path.
- `mode`: A string ('a' or 'w') specifying the file mode.
- `exc_info`: A boolean indicating whether traceback information should be included in log messages.
- `reader`/`writer`: Objects for reading/writing CSV data, initialized with the appropriate CSV library object.

**Potential Errors and Improvements:**

- **Robust Error Handling:** While the code includes `try...except` blocks, adding more specific exception handling (e.g., `IOError`, `UnicodeDecodeError`) could improve resilience.
- **File Existence Checks:** Consider checking if the file already exists *before* attempting to write in append mode ('a').  If the file doesn't exist, the program might try to append data to a non-existent file.
- **Input Validation:**  Adding checks for file existence before reading would prevent unexpected errors.
- **Type Hinting:** The type hints are generally good, but consider specifying the types of the keys in the dictionaries in `save_csv_file` and `read_csv_file`.

**Relationships with other parts of the project:**

- The `src.utils.jjson` module is clearly used for interacting with JSON data, suggesting a relationship with handling JSON formats.
- The `src.logger` module is used for logging errors, which indicates a logging framework is part of the project, and likely critical for monitoring and debugging.


**Chain of Relationships:**

The functions in `hypotez/src/utils/csv.py` are utilities for file handling and conversion related to CSV and potentially JSON data.  They likely integrate into other parts of the `hypotez` project that need to work with this data. This could include data processing pipelines, reports, or data import/export modules.