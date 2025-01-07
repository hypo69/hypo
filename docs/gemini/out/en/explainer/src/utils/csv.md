# CSV Utilities for Hypotez Project

## <input code>

```python
# \file hypotez/src/utils/csv.py
# -*- coding: utf-8 -*-

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
from src.logger import logger


def save_csv_file(
    data: List[Dict[str, str]],
    file_path: Union[str, Path],
    mode: str = 'a',
    exc_info: bool = True,
) -> bool:
    """Saves a list of dictionaries to a CSV file."""
    # ... (function definition as in the code)
    pass

def read_csv_file(file_path: Union[str, Path], exc_info: bool = True) -> List[Dict[str, str]] | None:
    """Reads CSV content as a list of dictionaries."""
    # ... (function definition as in the code)
    pass

def read_csv_as_json(csv_file_path: Union[str, Path], json_file_path: Union[str, Path], exc_info: bool = True) -> bool:
    """Convert a CSV file to JSON format and save it."""
    # ... (function definition as in the code)
    pass

def read_csv_as_dict(csv_file: Union[str, Path]) -> dict | None:
    """Convert CSV content to a dictionary."""
    # ... (function definition as in the code)
    pass

def read_csv_as_ns(file_path: Union[str, Path]) -> List[dict]:
    """Load CSV data into a list of dictionaries using Pandas."""
    # ... (function definition as in the code)
    pass
```

## <algorithm>

The code provides functions for working with CSV files, including saving, reading, and converting to JSON. The workflow is as follows:

1. **`save_csv_file`**:
   - Takes a list of dictionaries (`data`), file path (`file_path`), and optional mode ('a' to append, 'w' to overwrite) as input.
   - Validates the input data (must be a non-empty list of dictionaries).
   - Creates the parent directory if it doesn't exist.
   - Opens the CSV file in the specified mode, handling UTF-8 encoding.
   - Creates a DictWriter object using the keys of the first dictionary as fieldnames.
   - Writes a header if it's a new file or if the mode is 'w'.
   - Writes the data rows using `writerows`.
   - Handles potential exceptions and logs errors.

2. **`read_csv_file`**:
   - Takes a file path (`file_path`) as input.
   - Opens the CSV file in read mode with UTF-8 encoding.
   - Creates a DictReader object.
   - Returns a list of dictionaries read from the CSV.
   - Handles potential `FileNotFoundError` and other exceptions, logging errors and returning `None` on failure.

3. **`read_csv_as_json`**:
   - Takes CSV and JSON file paths as input.
   - Calls `read_csv_file` to read CSV data.
   - If `read_csv_file` fails (returns `None`), it returns `False`.
   - Opens the JSON file in write mode with UTF-8 encoding.
   - Writes the data to the JSON file using `json.dump` with indentation for readability.
   - Handles potential exceptions and returns `False` on failure.

4. **`read_csv_as_dict`**:
   - Takes a CSV file path as input.
   - Opens the CSV file in read mode with UTF-8 encoding.
   - Creates a DictReader object.
   - Returns a dictionary with 'data' key containing the list of dictionaries read from the CSV.  
   - Handles exceptions and returns `None` if any error occurs.

5. **`read_csv_as_ns`**:
   - Takes a CSV file path as input.
   - Uses Pandas to read the CSV into a DataFrame.
   - Converts the DataFrame to a list of dictionaries using `to_dict(orient='records')`.
   - Returns the list of dictionaries, handles `FileNotFoundError` and other exceptions, returning an empty list on failure.


## <mermaid>

```mermaid
graph LR
    A[save_csv_file] --> B(Validate input);
    B --> C{Create parent dir};
    C --> D[Open CSV file];
    D --> E{Create DictWriter};
    E --> F{Write header (if needed)};
    F --> G[Write rows];
    G --> H[Return True];
    B -- Invalid input --> I[Raise TypeError/ValueError];
    D -- Exception --> J[Log error, Return False];
    
    K[read_csv_file] --> L[Open CSV file];
    L --> M{Create DictReader};
    M --> N[Read rows];
    N --> O[Return list];
    L -- File Not Found --> P[Log error, Return None];
    L -- Exception --> Q[Log error, Return None];

    R[read_csv_as_json] --> S[read_csv_file];
    S --> T{Check if data is valid};
    T -- data is valid --> U[Open JSON file];
    U --> V[Write JSON data];
    V --> W[Return True];
    T -- data is invalid --> X[Return False];
    S -- Error --> Y[Log error, Return False];

    Z[read_csv_as_dict] --> AA[Open CSV file];
    AA --> AB{Create DictReader};
    AB --> AC[Read rows];
    AC --> AD[Return dict];
    AA -- Exception --> AE[Log error, Return None];

    AF[read_csv_as_ns] --> AG[Read CSV with Pandas];
    AG --> AH[Convert to dict];
    AH --> AI[Return list];
    AG -- FileNotFoundError --> AJ[Log error, Return []];
    AG -- Exception --> AK[Log error, Return []];

    subgraph Dependencies
        style AG fill:#ccf;
        pandas[pandas] --> AG;
    end
```

**Dependencies:**

- `csv`: For working with CSV files.
- `json`: For working with JSON files.
- `pathlib`: For working with file paths in a more object-oriented way.
- `types`: Provides the `SimpleNamespace` class, though not currently used.
- `typing`: Provides type hints for improved code readability and maintainability.
- `pandas`: Enables efficient data manipulation and analysis using DataFrames. Crucial for `read_csv_as_ns`.
- `src.logger`: A custom logger likely defined elsewhere in the `src` package.  Crucial for logging errors and information. This points to a hierarchical structure where `utils` is a module within the `src` package.


## <explanation>

**Imports:**

- `csv`: Used for reading and writing CSV files.
- `json`: Used for converting data to and from JSON format.
- `pathlib`: Used for working with file paths in a more object-oriented way, making file operations more robust.
- `types`: Includes the `SimpleNamespace` class (although not used in this file).
- `typing`: Provides type hints, crucial for better code understanding, maintainability, and type safety.
- `pandas`: Used for reading and processing CSV files in a DataFrame format.  Importantly, this is used by `read_csv_as_ns`, showing a dependency between this `csv` module and pandas.
- `src.logger`: Imports a custom logger likely defined in a different file within the `src` package, enabling structured logging of errors and information. This is the link to the `logger` package.


**Classes:**

- No classes are defined in this file.


**Functions:**

- `save_csv_file`: Saves a list of dictionaries to a CSV file.
  - Takes `data` (list of dictionaries), `file_path` (string or `Path` object), `mode` ('a' or 'w'), and `exc_info` (boolean) as arguments.
  - Returns `True` on success and `False` on failure. Raises `TypeError` or `ValueError` for invalid input.
- `read_csv_file`: Reads a CSV file and returns a list of dictionaries.
  - Takes `file_path` (string or `Path` object) and `exc_info` (boolean) as arguments.
  - Returns a list of dictionaries on success and `None` on failure (e.g., file not found).
- `read_csv_as_json`: Converts a CSV file to JSON format and saves it.
  - Takes `csv_file_path` (string or `Path`), `json_file_path` (string or `Path`), and `exc_info` (boolean) as arguments.
  - Returns `True` on successful conversion, `False` otherwise.
- `read_csv_as_dict`: Converts a CSV file to a Python dictionary.
  - Takes the `csv_file` path as input and returns a dictionary containing the CSV data.
- `read_csv_as_ns`: Reads a CSV file into a list of dictionaries using Pandas.
  - Takes the `file_path` and returns a list of dictionaries if successful, or empty list if there is an error.


**Variables:**

- No significant variables exist, except for the function arguments (`data`, `file_path`, etc.) that represent the data and file paths used in file operations.


**Potential Errors/Improvements:**

- **Error Handling:** The error handling is comprehensive, logging errors and providing useful messages. However, adding more specific error messages for various exceptions could improve debugging.
- **Input Validation:** The input validation in `save_csv_file` is good, but adding checks for the structure of the dictionaries (e.g., ensuring all dictionaries have the same keys) would enhance robustness.
- **File Existence Check:** Checking if the file already exists before appending would make more sense.
- **Pandas Dependency:** The code utilizes Pandas (`read_csv_as_ns`). Ensure this library is installed for all environments.
- **File Encoding:** While UTF-8 is a good default, specifying the encoding explicitly (or inferring it based on the file) is important.  Especially if there are potential non-UTF-8 CSV files.


**Relationship with Other Parts:**

The `src.logger` import indicates a relationship to a broader logging system in the project.  The `utils` package likely provides general utility functions for various parts of the Hypotez project. This structure is quite common in Python projects.