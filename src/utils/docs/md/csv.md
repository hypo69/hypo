# CSV Module

## Overview

The `csv.py` module provides functions for handling CSV files, including saving data to a CSV file, reading data from a CSV file, and converting data between JSON and CSV formats. It also includes functionality for reading CSV data and returning it as a dictionary.

## Functions

### `save_csv_file`

```python
def save_csv_file(
    data: List[Dict[str, str]],
    file_path: str | Path,
    mode: str = 'a',
    exc_info: bool = True
) -> bool:
```

#### Description
Saves a list of dictionaries to a CSV file.

#### Args
- `data` (`List[Dict[str, str]]`): The data to be written to the CSV file.
- `file_path` (`str | Path`): The full path to the CSV file.
- `mode` (`str`, optional): The file mode. Defaults to `'a'` (append).
- `exc_info` (`bool`, optional): If `True`, includes traceback information in the log. Defaults to `True`.

#### Returns
- `bool`: `True` if successful, else `False`.

#### Example
```python
data = [{'role': 'user', 'content': 'Hello'}]
success = save_csv_file(data=data, file_path='dialogue_log.csv')
print(success)  # True
```

### `read_csv_file`

```python
def read_csv_file(
    file_path: str | Path,
    exc_info: bool = True
) -> List[Dict[str, str]] | None:
```

#### Description
Reads the content of a CSV file and returns it as a list of dictionaries.

#### Args
- `file_path` (`str | Path`): The path to the CSV file.
- `exc_info` (`bool`, optional): If `True`, includes traceback information in the log. Defaults to `True`.

#### Returns
- `List[Dict[str, str]] | None`: The CSV file content as a list of dictionaries, or `None` if an error occurred.

#### Example
```python
data = read_csv_file(file_path='dialogue_log.csv')
print(data)  # [{'role': 'user', 'content': 'Hello'}, {'role': 'assistant', 'content': 'Hi there!'}]
```

### `json_to_csv`

```python
def json_to_csv(
    json_data: List[Dict[str, str]],
    csv_file_path: str | Path,
    exc_info: bool = True
) -> bool:
```

#### Description
Converts a list of dictionaries from JSON format to a CSV file.

#### Args
- `json_data` (`List[Dict[str, str]]`): The JSON data to be converted to CSV.
- `csv_file_path` (`str | Path`): The path to the CSV file to write.
- `exc_info` (`bool`, optional): If `True`, includes traceback information in the log. Defaults to `True`.

#### Returns
- `bool`: `True` if successful, else `False`.

#### Example
```python
json_data = [{'role': 'user', 'content': 'Hello'}]
success = json_to_csv(json_data, 'dialogue_log.csv')
print(success)  # True
```

### `csv_to_json`

```python
def csv_to_json(
    csv_file_path: str | Path,
    json_file_path: str | Path,
    exc_info: bool = True
) -> List[Dict[str, str]] | None:
```

#### Description
Converts CSV data to JSON format and saves it to a JSON file.

#### Args
- `csv_file_path` (`str | Path`): The path to the CSV file to read.
- `json_file_path` (`str | Path`): The path to the JSON file to write.
- `exc_info` (`bool`, optional): If `True`, includes traceback information in the log. Defaults to `True`.

#### Returns
- `List[Dict[str, str]] | None`: The CSV data as a list of dictionaries, or `None` if an error occurred.

#### Example
```python
data = csv_to_json('dialogue_log.csv', 'dialogue_log.json')
print(data)  # [{'role': 'user', 'content': 'Hello'}, {'role': 'assistant', 'content': 'Hi there!'}]
```

### `read_csv_as_dict`

```python
def read_csv_as_dict(
    csv_file: str | Path
) -> dict | bool:
```

#### Description
Converts CSV data to a dictionary containing the data from the CSV file.

#### Args
- `csv_file` (`str | Path`): The path to the CSV file to read.

#### Returns
- `dict | bool`: Dictionary containing the data from CSV converted to JSON format, or `False` if conversion failed.

#### Example
```python
data = read_csv_as_dict('dialogue_log.csv')
print(data)  # {'data': [{'role': 'user', 'content': 'Hello'}, {'role': 'assistant', 'content': 'Hi there!'}]}
```

## Notes

- The `save_csv_file` function appends to the file by default but can be set to overwrite the file.
- The `read_csv_file` function returns `None` if the file does not exist or an error occurs.
- The `json_to_csv` and `csv_to_json` functions rely on the `save_csv_file` and `read_csv_file` functions respectively.
- The `read_csv_as_dict` function handles both single-column and multi-column CSV files by returning either a list of values or a list of dictionaries.

For further customization or detailed explanations, refer to the function docstrings and examples provided.
