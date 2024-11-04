Here's a detailed documentation for the functions in your code, following the format used in `printer.md`. This documentation describes the functionality, arguments, return values, exceptions, and examples for each function.

```markdown
# `jjson` Module

## `j_dumps()`

The `j_dumps` function serializes JSON or `SimpleNamespace` objects into JSON format and writes them to a file or returns the JSON data as a dictionary.

### How the function works:

1. **Data Conversion**: Converts `SimpleNamespace` objects into dictionaries recursively.
2. **File Handling**: Handles different file modes (`w`, `a`, `a+`) for writing JSON data.
3. **Error Handling**: Logs errors if file operations or JSON dumping fails.

### Args:
- **data (Dict | SimpleNamespace | List[Dict] | List[SimpleNamespace])**: JSON objects or `SimpleNamespace` objects to be dumped.
- **file_path (Optional[Path], optional)**: Path to the output file. If `None`, returns the JSON data as a dictionary. Defaults to `None`.
- **ensure_ascii (bool, optional)**: If `True`, escape non-ASCII characters in the JSON output. Defaults to `False`.
- **mode (str, optional)**: File open mode (`'w'` for overwrite, `'a'` for append, `'a+'` for prepend). Defaults to `'w'`.
- **exc_info (bool, optional)**: If `True`, log exceptions with traceback. Defaults to `True`.

### Returns:
- **Optional[Dict]**: The JSON data as a dictionary if successful, or `None` if an error occurred.

### Raises:
- **ValueError**: If the file mode is not supported.

### Examples:
```python
>>> j_dumps({"key": "value"}, "output.json")
{"key": "value"}

>>> j_dumps([{"key1": "value1"}, {"key2": "value2"}], "output.json")
{"key1": "value1", "key2": "value2"}

>>> j_dumps({"key": "value"}, None)
{"key": "value"}

>>> j_dumps({"key": "value"}, "output.json", mode="a")
{"key": "value"}
```

## `j_loads()`

The `j_loads` function loads JSON or CSV data from a file, directory, or string and converts it into dictionaries or lists of dictionaries.

### How the function works:

1. **Data Loading**: Reads JSON or CSV data from the specified path and returns it as a dictionary or list of dictionaries.
2. **Directory Handling**: Handles directories by reading all JSON and CSV files within and combining their data.
3. **Error Handling**: Logs errors if files cannot be read or JSON data cannot be parsed.

### Args:
- **jjson (Path | Dict | str)**: Path to a file, directory, or JSON data as a string, or JSON object.
- **ordered (bool, optional)**: If `True`, returns `OrderedDict` instead of a regular dict to preserve element order. Defaults to `False`.
- **exc_info (bool, optional)**: If `True`, logs exceptions with traceback. Defaults to `True`.

### Returns:
- **Dict | List[Dict] | bool | None**: Returns a dictionary or list of dictionaries if successfully loaded. Returns `False` if an error occurred. Returns `None` if `jjson` is not found or cannot be read.

### Raises:
- **FileNotFoundError**: If the specified file is not found.
- **json.JSONDecodeError**: If JSON data could not be parsed.

### Examples:
```python
>>> j_loads('data.json')
{'key': 'value'}

>>> j_loads(Path('/path/to/directory'))
[{'key1': 'value1'}, {'key2': 'value2'}]

>>> j_loads('{"key": "value"}')
{'key': 'value'}

>>> j_loads(Path('/path/to/file.csv'))
[{'column1': 'value1', 'column2': 'value2'}]
```

## `j_loads_ns()`

The `j_loads_ns` function loads JSON or CSV data from a file, directory, or string and converts it into `SimpleNamespace` objects.

### How the function works:

1. **Data Loading**: Utilizes `j_loads` to load data.
2. **Conversion**: Converts dictionaries to `SimpleNamespace` objects.

### Args:
- **jjson (Path | SimpleNamespace | Dict | str)**: Path to a file, directory, or JSON data as a string, or JSON object.
- **ordered (bool, optional)**: If `True`, returns `OrderedDict` instead of a regular dict to preserve element order. Defaults to `False`.
- **exc_info (bool, optional)**: If `True`, logs exceptions with traceback. Defaults to `True`.

### Returns:
- **Optional[SimpleNamespace | List[SimpleNamespace]]**: Returns `SimpleNamespace` or a list of `SimpleNamespace` objects if successful. Returns `None` if `jjson` is not found or cannot be read.

### Examples:
```python
>>> j_loads_ns('data.json')
SimpleNamespace(key='value')

>>> j_loads_ns(Path('/path/to/directory'))
[SimpleNamespace(key1='value1'), SimpleNamespace(key2='value2')]

>>> j_loads_ns('{"key": "value"}')
SimpleNamespace(key='value')

>>> j_loads_ns(Path('/path/to/file.csv'))
[SimpleNamespace(column1='value1', column2='value2')]
```

## `merge_dicts()`

The `merge_dicts` function merges a list of dictionaries into a single dictionary if they have the same structure.

### How the function works:

1. **Recursive Merging**: Merges dictionaries recursively, handling nested dictionaries and lists.

### Args:
- **dict_list (List[dict])**: List of dictionaries to be merged.

### Returns:
- **dict**: A single merged dictionary.

## `convert_to_namespace()`

The `convert_to_namespace` function converts a dictionary to a `SimpleNamespace` object.

### How the function works:

1. **Conversion**: Uses `dict2namespace` to convert a dictionary to a `SimpleNamespace`.

### Args:
- **data (dict)**: Dictionary to be converted.

### Returns:
- **SimpleNamespace**: Converted `SimpleNamespace` object.

## `load_json_file()`

The `load_json_file` function loads JSON data from a file.

### How the function works:

1. **File Reading**: Reads JSON data from the specified file.

### Args:
- **path (Path)**: Path to the JSON file.

### Returns:
- **dict**: JSON data as a dictionary.

## `load_csv_file()`

The `load_csv_file` function loads CSV data from a file and converts it to a list of dictionaries.

### How the function works:

1. **CSV Reading**: Uses `pandas` to read CSV data and convert it to a list of dictionaries.

### Args:
- **path (Path)**: Path to the CSV file.

### Returns:
- **List[dict]**: CSV data as a list of dictionaries.

## `load_data_from_path()`

The `load_data_from_path` function loads data from JSON or CSV files in a directory.

### How the function works:

1. **Directory Handling**: Reads all JSON and CSV files in the directory and merges their data.

### Args:
- **path (Path)**: Path to the directory.

### Returns:
- **dict | List[dict]**: Merged data from JSON and CSV files.

## `replace_key_in_json()`

The `replace_key_in_json` function recursively replaces a key in a dictionary or list.

### How the function works:

1. **Recursive Replacement**: Recursively searches and replaces the specified key in nested dictionaries and lists.

### Args:
- **data**: Dictionary or list where key replacement will occur.
- **old_key**: Key to be replaced.
- **new_key**: New key.

## `process_json_file()`

The `process_json_file` function processes a JSON file by replacing the key `name` with `category_name`.

### How the function works:

1. **File Processing**: Reads the JSON file, replaces the key, and writes the modified data back to the file.

### Args:
- **json_file (Path)**: Path to the JSON file.

## `recursive_process_json_files()`

The `recursive_process_json_files` function recursively processes all JSON files in a directory.

### How the function works:

1. **Recursive Processing**: Searches for JSON files in the directory and processes each one.

### Args:
- **directory (Path)**: Path to the directory to be processed.

## `clean_string()`

The `clean_string` function cleans a JSON string to ensure correct formatting.

### How the function works:

1. **String Cleaning**: Strips leading and trailing whitespace from the JSON string.

### Args:
- **jjson (str)**: JSON string to be cleaned.

### Returns:
- **str**: Cleaned JSON string.

### Raises:
- **ValueError**: If provided JSON string is empty.

### Examples:
```python
>>> clean_string(' { "key": "value" } ')
'{"key": "value"}'

>>> clean_string('   {"key": "value"}\n')
'{"key": "value"}'

>>> clean_string('')
Traceback (most recent call last):
    ...
ValueError: Empty JSON string provided.
```
```

This documentation should give clear and comprehensive information about each function and how to use them. If you need further adjustments or additional

 details, just let me know!