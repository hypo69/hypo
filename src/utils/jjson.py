## \file src/utils/jjson.py
## \file src/utils/jjson.py
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
    """Dump JSON data to a file or return the JSON data as a dictionary.

    Args:
        data (Dict | SimpleNamespace | List[Dict] | List[SimpleNamespace]): JSON-compatible data or SimpleNamespace objects to dump.
        file_path (Optional[Path], optional): Path to the output file. If None, returns JSON as a dictionary. Defaults to None.
        ensure_ascii (bool, optional): If True, escapes non-ASCII characters in output. Defaults to True.
        mode (str, optional): File open mode ('w' for overwrite, 'a' for append, 'a+' for merge). Defaults to 'w'.
        exc_info (bool, optional): If True, logs exceptions with traceback. Defaults to True.

    Returns:
        Optional[Dict]: JSON data as a dictionary if successful, or nothing if an error occurs.

    Raises:
        ValueError: If the file mode is unsupported.

    Examples:
        >>> j_dumps({"key": "value"}, "output.json")
        {"key": "value"}
    """
    
    path = Path(file_path) if isinstance(file_path, (str, Path)) else None
    
    def convert_to_dict(data):
        """Convert SimpleNamespace instances to dictionaries recursively."""
        if isinstance(data, SimpleNamespace):
            return vars(data)
        if isinstance(data, list):
            return [convert_to_dict(item) for item in data]
        if isinstance(data, dict):
            return {key: convert_to_dict(value) for key, value in data.items()}
        return data
    
    data = convert_to_dict(data)

    if mode not in {"w", "a", "a+"}:
        raise ValueError(f"Unsupported file mode '{mode}'. Use 'w', 'a', or 'a+'.")

    if path and mode in {"a", "a+"}:
        try:
            existing_data = j_loads(path)
            if existing_data:
                if mode == "a+":
                    data.update(existing_data)
                else:
                    existing_data.update(data)
                    data = existing_data
        except Exception as ex:
            logger.error(f"Error reading {path=}: {ex}", exc_info=exc_info)
            return

    if path:
        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open(mode, encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=ensure_ascii)
        except Exception as ex:
            logger.error(f"Failed to write to {path}: {ex}", exc_info=exc_info)
            return
    else:
        return data
    
    return data

def j_loads(
    jjson: dict | SimpleNamespace | str | Path | list[dict] | list[SimpleNamespace],
    ordered: bool = True,
    exc_info: bool = True
) -> Any:
    """Load JSON or CSV data from a file, directory, or string.

    Args:
        jjson (Path | dict | str): Path to a file, directory, JSON data as a string, or JSON object.
        ordered (bool, optional): If True, returns OrderedDict to preserve element order. Defaults to False.
        exc_info (bool, optional): If True, logs exceptions with traceback. Defaults to True.

    Returns:
        Any: A dictionary or list of dictionaries if successful, or nothing if an error occurs.
    
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
    
    def clean_string(json_string: str) -> str:
        """Remove triple backticks and 'json' from the beginning and end of the string."""
        if json_string.startswith(("```", "```json")) and json_string.endswith("```"):
            return json_string.strip("`").replace("json", "", 1).strip()
        return json_string

    def merge_dicts(dict_list: list[dict]) -> dict:
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

    def _load_csv_from_file(file_path: Path) -> list[dict]:
        """Load data from a CSV file and return as a list of dictionaries."""
        try:
            return pd.read_csv(file_path).to_dict(orient='records')
        except Exception as ex:
            logger.error(f"Error reading CSV file: {file_path}", exc_info=exc_info)
            return []

    try:
        if isinstance(jjson, Path):
            json_path = Path(jjson)
            if json_path.is_dir():
                json_files = list(json_path.glob("*.json"))
                if not json_files: 
                    logger.warning(f"No JSON files found in directory: {json_path}", exc_info=True)
                    return

                dict_list = [j_loads(file)[1] for file in json_files if j_loads(file)[0]]
                if all(isinstance(d, dict) for d in dict_list):
                    return merge_dicts(dict_list)
                return dict_list

            if json_path.suffix.lower() == ".csv":
                csv_data = _load_csv_from_file(json_path)
                return csv_data

            try:
                data = json.loads(json_path.read_text(encoding="utf-8"))
                return data
            except Exception as ex:
                logger.debug(f"Error reading file {json_path=}", ex, exc_info=exc_info)
                ...
                return

        elif isinstance(jjson, str):
            data = clean_string(jjson)
            try:
                data = json.loads(data)
                return data
            except Exception as ex:
                data = repair_json(data)  # Assuming repair_json is defined elsewhere
                try: 
                    data = json.loads(data)
                    return data
                except Exception as ex:
                    logger.debug(f"Invalid JSON format {data}", exc_info=exc_info)
                    return

        elif isinstance(jjson, dict):
            return jjson

    except FileNotFoundError as ex:
        logger.error(f"File not found: {jjson}", exc_info=exc_info)
        return
    except Exception as ex:
        logger.error(f"Error loading JSON data from {jjson}", exc_info=exc_info)
        return

    return

def j_loads_ns(
    jjson: Path | SimpleNamespace | Dict | str,
    ordered: bool = True,
    exc_info: bool = True,
) -> Optional[SimpleNamespace | List[SimpleNamespace]] | None:
    """Load JSON or CSV data from a file, directory, or string and convert to SimpleNamespace.

    Args:
        jjson (Path | SimpleNamespace | Dict | str): Path to a file, directory, or JSON data as a string, or JSON object.
        ordered (bool, optional): If  returns OrderedDict instead of a regular dict to preserve element order. Defaults to False.
        exc_info (bool, optional): If  logs exceptions with traceback. Defaults to True.

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
            return  [dict2ns(item) for item in data]
        return  dict2ns(data)
    return  data 

def replace_key_in_json(data, old_key, new_key) -> dict:
    """
    Recursively replaces a key in a dictionary or list.
    
    Args:
        data (dict | list): The dictionary or list where key replacement occurs.
        old_key (str): The key to be replaced.
        new_key (str): The new key.
    
    Returns:
        dict: The updated dictionary with replaced keys.

    Example Usage:

        replace_key_in_json(data, 'name', 'category_name')

        # Example 1: Simple dictionary
        data = {"old_key": "value"}
        updated_data = replace_key_in_json(data, "old_key", "new_key")
        # updated_data becomes {"new_key": "value"}

        # Example 2: Nested dictionary
        data = {"outer": {"old_key": "value"}}
        updated_data = replace_key_in_json(data, "old_key", "new_key")
        # updated_data becomes {"outer": {"new_key": "value"}}

        # Example 3: List of dictionaries
        data = [{"old_key": "value1"}, {"old_key": "value2"}]
        updated_data = replace_key_in_json(data, "old_key", "new_key")
        # updated_data becomes [{"new_key": "value1"}, {"new_key": "value2"}]

        # Example 4: Mixed nested structure with lists and dictionaries
        data = {"outer": [{"inner": {"old_key": "value"}}]}
        updated_data = replace_key_in_json(data, "old_key", "new_key")
        # updated_data becomes {"outer": [{"inner": {"new_key": "value"}}]}

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
    
    return data

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
        
def extract_json_from_string(md_string: str) -> str:
    """Extract JSON content from Markdown string between ```json and ``` markers.

    Args:
        md_string (str): The Markdown string that contains JSON enclosed in ```json ```.

    Returns:
        str: The extracted JSON string or an empty string if not found.
    """
    try:
        match = re.search(r'```json\s*(.*?)\s*```', md_string, re.DOTALL)
        if match:
            json_string = match.group(1).strip()
            return json_string
        else:
            logger.warning("No JSON content found between ```json and ``` markers.")
            return ""
    except Exception as ex:
        logger.error("Error extracting JSON from Markdown.", exc_info=True)
        return ""
