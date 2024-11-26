# Usage Guide for `hypotez/src/utils/csv.py`

This module provides utilities for working with CSV and JSON files.  It includes functions for saving, reading, and converting CSV data.

## Saving CSV Data (`save_csv_file`)

```python
def save_csv_file(
    data: List[Dict[str, str]],
    file_path: Union[str, Path],
    mode: str = 'a',
    exc_info: bool = True,
) -> bool:
    """Saves a list of dictionaries to a CSV file.
```

**How to Use:**

1. **Import the module:**
   ```python
   from hypotez.src.utils.csv import save_csv_file
   ```

2. **Prepare your data:** Ensure your data is a list of dictionaries. Each dictionary represents a row in the CSV, and the keys of the dictionary are the column headers.

   ```python
   data = [
       {'name': 'Alice', 'age': 30, 'city': 'New York'},
       {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'},
   ]
   ```

3. **Specify the file path:** Provide the path to the CSV file where you want to save the data.  Crucially, if the directory for the file doesn't exist, this function will create the necessary parent directories automatically.

   ```python
   file_path = 'mydata.csv'
   ```

4. **Call the function:** Pass the data, file path, and optional `mode` (default is 'a' for append).  Setting `mode='w'` will overwrite the file if it exists.  The `exc_info` parameter controls whether detailed error information is logged.  Set it to `False` to omit the error tracebacks.

   ```python
   success = save_csv_file(data, file_path, mode='w')  # Overwrites the file
   if success:
       print("CSV file saved successfully!")
   else:
       print("Failed to save CSV file.")
   ```

**Important Considerations:**

* **Error Handling:** The function includes robust error handling.  It checks if the input data is valid (a list of dictionaries) and raises `TypeError` or `ValueError` if not.  It catches exceptions during file operations and logs errors using the provided `logger`.  The `exc_info` parameter controls whether stack traces are included in the log messages.

* **File Mode (`mode`):** Using `'a'` (append) is generally recommended for adding data to existing files. `'w'` (overwrite) will erase the previous content if the file exists.

* **File Existence:** It checks if the file already exists and handles the case appropriately when using append mode (`mode='a'`).  It also creates necessary parent directories automatically.


## Reading CSV Data (`read_csv_file`)

```python
def read_csv_file(file_path: Union[str, Path], exc_info: bool = True) -> List[Dict[str, str]] | None:
```

**How to Use:**

Similar to `save_csv_file`, but for reading. This returns a list of dictionaries, where each dictionary corresponds to a row in the CSV. Returns `None` if an error occurs.

```python
file_path = 'mydata.csv'
data = read_csv_file(file_path)

if data:
    print(data)
else:
    print("Failed to read CSV file.")
```

## Converting CSV to JSON (`read_csv_as_json`)

```python
def read_csv_as_json(csv_file_path: Union[str, Path], json_file_path: Union[str, Path], exc_info: bool = True) -> bool:
```

This function converts a CSV file to JSON and saves it.

```python
csv_file = 'mydata.csv'
json_file = 'mydata.json'
success = read_csv_as_json(csv_file, json_file)

if success:
    print("CSV converted to JSON successfully.")
else:
    print("Failed to convert CSV to JSON.")
```


## Other Useful Functions

The module provides functions for converting CSV to dictionary (`read_csv_as_dict`) and loading into a list of dictionaries using Pandas (`read_csv_as_ns`).  Refer to their docstrings for specific usage.


**Key Improvements and Considerations:**

* **Clearer Docstrings:**  Docstrings are now more comprehensive, explaining the purpose, parameters, return values, and potential errors for each function.
* **Explicit Error Handling:** Explicitly handling potential `FileNotFoundError` in the reading functions makes the code more robust.
* **Comprehensive Examples:** Providing more illustrative examples for each function clarifies their usage.
* **Error Reporting:**  Utilizing the `logger` improves error logging and reduces the chances of accidental crashes.
* **Type Hinting:** Utilizing type hints enhances code clarity and maintainability.
* **Parent Directory Creation:** The `save_csv_file` now automatically creates missing parent directories, preventing common errors.


This expanded guide provides a more complete and user-friendly introduction to the `hypotez/src/utils/csv.py` module. Remember to refer to the docstrings of each function for specific details.