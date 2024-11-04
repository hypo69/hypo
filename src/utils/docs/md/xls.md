
# `xls` Module
## Overview

The `xls.py` module provides functions for converting data between Excel and JSON formats. It includes functionality for converting individual sheets or entire workbooks from Excel to JSON, as well as converting JSON data back into Excel files.

## `xls_to_json()`

The `xls_to_json` function converts an Excel file to JSON format. 

### How the function works:

1. **Read Excel File**: Utilizes `pandas` to read the Excel file into a DataFrame.
2. **Convert to JSON**: Converts the DataFrame to JSON format.
3. **Save JSON**: Optionally saves the JSON data to a file.
4. **Error Handling**: Logs errors if file operations or conversions fail.

### Args:
- **xls_file (str | Path)**: Path to the input Excel file.
- **json_file (str | Path, optional)**: Path to the output JSON file. If not provided, JSON data is not saved to a file.
- **sheet_name (str, optional)**: The sheet name to be converted. If not provided, converts all sheets.
- **exc_info (bool, optional)**: If `True`, includes traceback information in the log. Defaults to `True`.

### Returns:
- **SimpleNamespace | List[SimpleNamespace] | bool**: Returns `SimpleNamespace` or a list of `SimpleNamespace` if successful, `None` if the list is empty, or `False` if an error occurred.

### Raises:
- **FileNotFoundError**: If the Excel file does not exist.
- **Exception**: Logs error if file reading, conversion, or saving fails.

### Examples:

```python
>>> result = xls_to_json('input.xlsx', 'output.json')
>>> print(result)
[{'column1': 'value1', 'column2': 'value2'}, ...]

>>> result = xls_to_json('input.xlsx', sheet_name='Sheet1')
>>> print(result)
[{'column1': 'value1', 'column2': 'value2'}, ...]

>>> result = xls_to_json('input.xlsx')
>>> print(result)
[{'column1': 'value1', 'column2': 'value2'}, ...]
```

## `xls_to_json_all_sheets()`

The `xls_to_json_all_sheets` function converts all sheets in an Excel file to JSON format and saves them to a file.

### How the function works:

1. **Read All Sheets**: Utilizes `pandas` to read all sheets from the Excel file.
2. **Convert to JSON**: Converts each sheet to JSON format.
3. **Save JSON**: Saves the JSON data to a file.
4. **Error Handling**: Logs errors if file operations or conversions fail.

### Args:
- **xls_file (str | Path)**: Path to the input Excel file.
- **json_file (str | Path)**: Path to the output JSON file.
- **exc_info (bool, optional)**: If `True`, includes traceback information in the log. Defaults to `True`.

### Returns:
- **bool**: `True` if successful, else `False`.

### Raises:
- **FileNotFoundError**: If the Excel file does not exist.
- **Exception**: Logs error if file reading, conversion, or saving fails.

### Examples:

```python
>>> success = xls_to_json_all_sheets('input.xlsx', 'output_all_sheets.json')
>>> print(success)
True
```

## `json_to_xls()`

The `json_to_xls` function converts JSON data to an Excel file.

### How the function works:

1. **Data Conversion**: Converts JSON data to a DataFrame using `pandas`.
2. **Save Excel**: Saves the DataFrame to an Excel file.
3. **Error Handling**: Logs errors if JSON conversion or file saving fails.

### Args:
- **json_data (List[Dict[str, str]])**: The JSON data to be converted to Excel.
- **xls_file_path (str | Path)**: Path to the output Excel file.
- **exc_info (bool, optional)**: If `True`, includes traceback information in the log. Defaults to `True`.

### Returns:
- **bool**: `True` if successful, else `False`.

### Examples:

```python
>>> json_data = [{'column1': 'value1', 'column2': 'value2'}]
>>> success = json_to_xls(json_data, 'output.xlsx')
>>> print(success)
True
```
