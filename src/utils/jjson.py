## \file ../src/utils/jjson.py
## \file ../src/utils/jjson.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
"""
Module for handling JSON and CSV files, including loading, dumping, and merging data.

This module provides functions to:
- **Dump JSON data**: Convert JSON or SimpleNamespace objects into JSON format and write to a file, or return the JSON data as a dictionary.
- **Load JSON and CSV data**: Read JSON or CSV data from a file, directory, or string, and convert it into dictionaries or lists of dictionaries.
- **Convert to SimpleNamespace**: Convert loaded JSON data into SimpleNamespace objects for easier manipulation.
- **Merge JSON files**: Combine multiple JSON files from a directory into a single JSON file.
- **Parse Markdown**: Convert Markdown strings to JSON format for structured data representation.

The functions in this module handle various aspects of working with JSON and CSV data, ensuring that data is loaded, saved, and merged efficiently and effectively.
"""

from datetime import datetime
from math import log
from pathlib import Path
from typing import List, Dict, Optional
from types import SimpleNamespace
import json
import os
import re
import pandas as pd


from src.logger import logger
from .convertors.dict import dict2ns

def fix_json_string(jjson: str | list) -> str:
    """Correct common formatting issues in JSON strings.

    Args:
        jjson (str): The raw JSON string that may contain issues.

    Returns:
        str: Corrected JSON string.
    """
    jjson_list: list = jjson if isinstance(jjson,list) else [jjson]
    for j in jjson_list:
        if isinstance(j, str):
            try:
                j = j.replace('\\n', '\n')  # Convert escaped newlines to actual newlines
                j = j.replace('\\"', '"')   # Remove unnecessary escaping of quotes
                j = j.replace('\\\\', '\\') # Remove double backslashes
                j = re.sub(r'\\(?=")', '', j)  # Remove escaping before double quotes if any
                #return j
            except Exception as ex:
                logger.error(f"Error in string normilizer", ex, True)
                ...
                continue 
    if len(jjson_list) == 1:
        return jjson_list[0]
    return jjson_list

def j_dumps(
    data: Dict | SimpleNamespace | List[Dict] | List[SimpleNamespace],
    file_path: Optional[Path] = None,
    ensure_ascii: bool = False,
    mode: str = "w",
    exc_info: bool = True,
) -> Optional[Dict]:
    """Dump JSON data to a file or return the JSON data.

    Args:
        data (Dict | SimpleNamespace | List[Dict] | List[SimpleNamespace]): JSON objects or SimpleNamespace objects to be dumped.
        file_path (Optional[Path], optional): Path to the output file. If None, returns the JSON data as a dictionary. Defaults to None.
        ensure_ascii (bool, optional): If True, escape non-ASCII characters in the JSON output. Defaults to False.
        mode (str, optional): File open mode ('w' for overwrite, 'a' for append, 'a+' for prepend). Defaults to 'w'.
        exc_info (bool, optional): If True, log exceptions with traceback. Defaults to True.

    Returns:
        Optional[Dict]: The JSON data as a dictionary if successful, or None if an error occurred.

    Raises:
        ValueError: If the file mode is not supported.

    Examples:
        >>> j_dumps({"key": "value"}, "output.json")
        {"key": "value"}

        >>> j_dumps([{"key1": "value1"}, {"key2": "value2"}], "output.json")
        {"key1": "value1", "key2": "value2"}

        >>> j_dumps({"key": "value"}, None)
        {"key": "value"}

        >>> j_dumps({"key": "value"}, "output.json", mode="a")
        {"key": "value"}
    """
    path = file_path
    try:
        path = Path(path) if isinstance(path, (str, tuple, list)) else path

        def convert_to_dict(data):
            """Recursively convert SimpleNamespace objects to dictionaries."""
            if isinstance(data, SimpleNamespace):
                data = vars(data)
            if isinstance(data, list):
                return [convert_to_dict(item) for item in data]
            if isinstance(data, dict):
                return {key: convert_to_dict(value) for key, value in data.items()}
            return data

        data = convert_to_dict(data)

        if mode in {"a", "a+", "+a"}:
            try:
                existing_data = j_loads(path)
                if existing_data:
                    data = existing_data.update(data) if mode == "a+" else data.update(existing_data)
            except Exception as ex:
                logger.warning(f"Error reading {path=}", ex, False)
                return

        if path:
            if not path.parent.exists():
                path.parent.mkdir(parents=True, exist_ok=True)
            try:
                with path.open("w", encoding="utf-8") as f:
                    json.dump(data, f, ensure_ascii=ensure_ascii)
            except Exception as ex:
                logger.error(f"Error creating {path}", ex, exc_info=exc_info)
                return

        return data

    except Exception as ex:
        logger.error(f"Failed to dump JSON file {path}.\n{data}", ex, exc_info=exc_info)
        return

def j_loads(
    jjson: Path | Dict | str,
    ordered: bool = False,
    exc_info: bool = True
) -> Dict | List[Dict] | bool | None:
    """Load JSON or CSV data from a file, directory, or string.

    Args:
        jjson (Path | Dict | str): Path to a file, directory, or JSON data as a string, or JSON object.
        ordered (bool, optional): If True, returns OrderedDict instead of a regular dict to preserve element order. Defaults to False.
        exc_info (bool, optional): If True, logs exceptions with traceback. Defaults to True.

    Returns:
        Dict | List[Dict] | bool | None: Returns a dictionary or list of dictionaries if successfully loaded. Returns False if an error occurred. Returns None if jjson is not found or cannot be read.

    Raises:
        FileNotFoundError: If the specified file is not found.
        json.JSONDecodeError: If JSON data could not be parsed.

    Examples:
        >>> j_loads('data.json')
        {'key': 'value'}

        >>> j_loads(Path('/path/to/directory'))
        [{'key1': 'value1'}, {'key2': 'value2'}]

        >>> j_loads('{"key": "value"}')
        {'key': 'value'}

        >>> j_loads(Path('/path/to/file.csv'))
        [{'column1': 'value1', 'column2': 'value2'}]
    """
    def merge_dicts(dict_list: List[Dict]) -> Dict:
        """Merge a list of dictionaries into a single dictionary if they have the same structure."""
        merged = dict_list[0]
        for d in dict_list[1:]:
            for key in merged.keys():
                if key in d:
                    if isinstance(merged[key], dict) and isinstance(d[key], dict):
                        merged[key] = merge_dicts([merged[key], d[key]])
                    elif isinstance(merged[key], list) and isinstance(d[key], list):
                        merged[key].extend(d[key])
                    else:
                        merged[key] = d[key]
        return merged

    def _load_csv_from_file(file_path: Path) -> List[Dict]:
        """Load data from a CSV file and return as a list of dictionaries."""
        try:
            return pd.read_csv(file_path).to_dict(orient='records')
        except Exception as ex:
            logger.error(f"Error reading CSV file: {file_path}", ex, exc_info=exc_info)
            return []

    try:
        if isinstance(jjson, Path):
            json_path = Path(jjson)
            if json_path.is_dir():
                # Load JSON files from the directory
                json_files = list(json_path.glob("*.json"))
                if not json_files:
                    logger.warning(f"No JSON files found in directory: {json_path}", exc_info=exc_info)
                    return []
                dict_list = [j_loads(json_file) for json_file in json_files]
                if all(isinstance(d, dict) for d in dict_list):
                    return merge_dicts(dict_list)
                return dict_list

            if json_path.suffix.lower() == ".csv":
                # Load data from a CSV file
                return _load_csv_from_file(json_path)

            return json.loads(json_path.open("r", encoding="utf-8").read())

        elif isinstance(jjson, str):
            try:
                return json.loads(fix_json_string(jjson))
            except json.JSONDecodeError as ex:
                logger.error(f"Invalid JSON format: {jjson}", ex, exc_info=exc_info)
                return 
        elif isinstance(jjson, dict):
            return jjson
    except FileNotFoundError as ex:
        logger.error(f"File not found: {jjson}", ex, exc_info=exc_info)
    except Exception as ex:
        logger.error(f"Error loading JSON data from {jjson}", ex, exc_info=exc_info)

    return 

def j_loads_ns(
    jjson: Path | SimpleNamespace | Dict | str,
    ordered: bool = False,
    exc_info: bool = True,
) -> Optional[SimpleNamespace | List[SimpleNamespace]]:
    """Load JSON or CSV data from a file, directory, or string and convert to SimpleNamespace.

    Args:
        jjson (Path | SimpleNamespace | Dict | str): Path to a file, directory, or JSON data as a string, or JSON object.
        ordered (bool, optional): If True, returns OrderedDict instead of a regular dict to preserve element order. Defaults to False.
        exc_info (bool, optional): If True, logs exceptions with traceback. Defaults to True.

    Returns:
        Optional[SimpleNamespace | List[SimpleNamespace]]: Returns SimpleNamespace or a list of SimpleNamespace objects if successful. Returns None if jjson is not found or cannot be read.

    Examples:
        >>> j_loads_ns('data.json')
        SimpleNamespace(key='value')

        >>> j_loads_ns(Path('/path/to/directory'))
        [SimpleNamespace(key1='value1'), SimpleNamespace(key2='value2')]

        >>> j_loads_ns('{"key": "value"}')
        SimpleNamespace(key='value')

        >>> j_loads_ns(Path('/path/to/file.csv'))
        [SimpleNamespace(column1='value1', column2='value2')]
    """
    data = j_loads(jjson, ordered=ordered, exc_info=exc_info)
    if data:
        if isinstance(data, list):
            return [dict2ns(item) for item in data]
        return dict2ns(data)
    return None

def merge_dicts(dict_list: List[dict]) -> dict:
    """Merge a list of dictionaries into a single dictionary if they have the same structure."""
    merged = dict_list[0]
    for d in dict_list[1:]:
        for key in merged.keys():
            if key in d:
                if isinstance(merged[key], dict) and isinstance(d[key], dict):
                    merged[key] = merge_dicts([merged[key], d[key]])
                elif isinstance(merged[key], list) and isinstance(d[key], list):
                    merged[key].extend(d[key])
                else:
                    merged[key] = d[key]
    return merged

def convert_to_namespace(data: dict) -> SimpleNamespace:
    """Convert a dictionary to SimpleNamespace."""
    return dict2ns(data)

def load_json_file(path: Path) -> dict:
    """Load JSON data from a file."""
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)

def load_csv_file(path: Path) -> List[dict]:
    """Load CSV data from a file and convert it to a list of dictionaries."""
    df = pd.read_csv(path)
    return df.to_dict(orient="records")

    def load_data_from_path(path: Path) -> dict | List[dict]:
        """Load data from JSON or CSV files in a directory."""
        data = []
        for file in os.listdir(path):
            file_path = path / file
            if file_path.suffix == ".json":
                data.append(load_json_file(file_path))
            elif file_path.suffix == ".csv":
                data.extend(load_csv_file(file_path))
        if len(data) > 1:
            return merge_dicts(data)
        return data[0] if data else {}

    if isinstance(jjson, Path):
        if jjson.is_file():
            if jjson.suffix == ".json":
                return load_json_file(jjson)
            elif jjson.suffix == ".csv":
                return load_csv_file(jjson)
        elif jjson.is_dir():
            return load_data_from_path(jjson)
    elif isinstance(jjson, str):
        return json.loads(jjson)
    elif isinstance(jjson, dict):
        return convert_to_namespace(jjson) if ordered else jjson

    logger.error(f"Unsupported type or path: {jjson}", exc_info=exc_info)
    return None

def replace_key_in_json(data, old_key, new_key):
    """
    Рекурсивно заменяет ключ в словаре или списке.
    @param data: Словарь или список, в котором происходит замена ключей.
    @param old_key: Ключ, который нужно заменить.
    @param new_key: Новый ключ.
    """
    if isinstance(data, dict):
        for key in list(data.keys()):
            if key == old_key:
                data[new_key] = data.pop(old_key)
            if isinstance(data[key], (dict, list)):
                replace_key_in_json(data[key], old_key, new_key)
    elif isinstance(data, list):
        for item in data:
            replace_key_in_json(item, old_key, new_key)

def process_json_file(json_file: Path):
    """
    Обрабатывает JSON файл, заменяя ключ `name` на `category_name`.
    @param json_file: Путь к JSON файлу.
    """
    try:
        data = j_loads(json_file.read_text())
        replace_key_in_json(data, 'name', 'category_name')
        json_file.write_text(j_dumps(data))
    except Exception as ex:
        logger.error(f"Error processing file: {json_file}", ex)

def recursive_process_json_files(directory: Path):
    """
    Рекурсивно обходит папки и обрабатывает JSON файлы.
    @param directory: Путь к директории, которую нужно обработать.
    """
    for path in directory.rglob('*.json'):
        if path.is_file():
            process_json_file(path)

            
def clean_string(jjson: str) -> str:
    """Очищает строку JSON для обеспечения правильного форматирования.

    Args:
        jjson (str): Строка JSON, которую необходимо очистить.

    Returns:
        str: Очищенная строка JSON.

    Raises:
        ValueError: Если предоставлена пустая строка JSON.

    Examples:
        >>> clean_string(' { "key": "value" } ')
        '{"key": "value"}'

        >>> clean_string('   {"key": "value"}\n')
        '{"key": "value"}'

        >>> clean_string('')
        Traceback (most recent call last):
            ...
        ValueError: Empty JSON string provided.
    """
    cleaned_str = jjson.strip()  # Удаление начальных и конечных пробелов
    if not cleaned_str:
        raise ValueError("Empty JSON string provided.")
    return cleaned_str
