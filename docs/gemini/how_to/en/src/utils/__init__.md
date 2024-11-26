# Usage Guide for hypotez/src/utils/__init__.py

This module, `hypotez/src/utils/__init__.py`, provides a collection of utility functions for various tasks, including data conversion, file handling, and formatted output.  It's designed to simplify common programming operations.

## Key Features

This module groups related utilities into submodules:

* **`convertors`**:  Handles conversions between various data formats (base64, CSV, JSON, HTML, XML, etc.).
* **`csv`**:  Functions for reading and writing CSV files (as dictionaries or named structures).
* **`date_time`**:  Handles time-related operations, including timeouts.
* **`file`**:  Provides functions for file system interactions (reading, writing, listing files and directories, recursive operations).
* **`image`**:  Functions for handling image files and URLs.
* **`jjson`**:  Functions for working with JSON data (including loading/dumping, replacing keys).
* **`pdf`**:  Functions for PDF file manipulation (currently only `PDFUtils`).
* **`printer`**:  Provides formatted printing (e.g., `pprint`).
* **`string`**:  Handles string formatting, normalization, and validation.
* **`video`**:  Functions for saving videos from URLs.
* **`url`**:  Functions for working with URLs (extracting parameters, checking URL validity).
* **`path`**: Functions for working with file paths (including getting relative paths)


## How to Use

The module is designed to be imported and used directly.  Since it's an `__init__.py` file, you can import the functions from the submodules directly without needing to explicitly import each one:

```python
from hypotez.src.utils import base64_to_tmpfile, read_csv_as_dict, save_text_file, pprint, is_url
```

### Example: Converting a JSON string to a CSV file

```python
import json
import io

# Sample JSON data
json_data = '{"name": "John Doe", "age": 30}'

# Load JSON data from a string.
try:
   data = json.loads(json_data)
except json.JSONDecodeError as e:
   print(f"Invalid JSON data: {e}")
   exit()

# Convert the dictionary to a CSV string.
csv_string = utils.dict2csv(data)

# Write the CSV string to a temporary file or create a file to save to.
# ...
```

### Example: Reading CSV file as a dictionary

```python
import os

# Specify the path to your CSV file.  Adjust this!
csv_file_path = "your_file.csv"

if os.path.exists(csv_file_path):
   try:
      data = utils.read_csv_as_dict(csv_file_path)
      # Now you can work with the 'data' dictionary.
      print(data)

   except Exception as e:
      print(f"Error reading CSV: {e}")
else:
    print(f"File not found: {csv_file_path}")

```


**Crucially, replace `"your_file.csv"` with the actual path to your CSV file.**


### Example: Checking if a string is a valid URL

```python
from hypotez.src.utils import is_url

string1 = "https://www.example.com"
string2 = "not a url"

print(f"'{string1}' is a URL: {is_url(string1)}")  # Output: True
print(f"'{string2}' is a URL: {is_url(string2)}")  # Output: False
```


**Important Notes:**

* Be sure to install any required libraries (e.g., `pandas` for some operations, `openpyxl`, etc.) for the specific functions you're using.
* Always handle potential errors (e.g., file not found, invalid input data) using `try...except` blocks to make your code more robust.
* Refer to the documentation for each function for detailed parameters, return values, and usage examples within specific submodules (e.g., `convertors`, `file`).


This guide provides a starting point; explore the individual submodules for a complete understanding of the available functionalities.