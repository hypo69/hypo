## \file src/utils/csv.py
# -*- coding: utf-8 -*-
"""!
Module for CSV and JSON file operations.

This module provides utilities for:
- Saving and reading CSV files.
- Converting JSON data to CSV and vice versa.
- Transforming CSV content into dictionaries for easy manipulation.

Functions:
    - save_csv_file: Save a list of dictionaries to a CSV file.
    - read_csv_file: Read CSV content as a list of dictionaries.
    - json_to_csv: Convert JSON data to CSV.
    - csv_to_json: Convert CSV to JSON and save to a file.
    - read_csv_as_dict: Convert CSV content to a dictionary format.

Example usage:
    >>> data = [{'role': 'user', 'content': 'Hello'}]
    >>> save_csv_file(data, 'dialogue_log.csv')
    True

    >>> read_data = read_csv_file('dialogue_log.csv')
    >>> print(read_data)
    [{'role': 'user', 'content': 'Hello'}]
"""

import csv
import json
from pathlib import Path
from types import SimpleNamespace
from typing import List, Dict, Union
import pandas as pd
from src.utils.jjson import j_loads, j_loads_ns, j_dumps
from src.logger import logger

def save_csv_file(
    data: List[Dict[str, str] | SimpleNamespace],
    file_path: Union[str, Path],
    mode: str = 'a',
    exc_info: bool = True
) -> bool:
    """! Save a list of dictionaries to a CSV file.

    Args:
        data (List[Dict[str, str]]): Data to be saved in CSV format.
        file_path (str | Path): Path to the CSV file.
        mode (str, optional): File mode ('a' to append, 'w' to overwrite). Default is 'a'.
        exc_info (bool, optional): Include traceback information in logs. Default is True.

    Returns:
        bool: True if successful, otherwise False.

    Example:
        >>> data = [{'name': 'Alice', 'age': '30'}]
        >>> save_csv_file(data, 'people.csv', mode='w')
        True
    """
    try:
        file_path = Path(file_path)
        file_path.parent.mkdir(parents=True, exist_ok=True)

        with file_path.open(mode, newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            if mode == 'w' or not file_path.exists():
                writer.writeheader()
            writer.writerows(data)
        return True
    except Exception as ex:
        logger.error(f"Failed to save CSV to {file_path}", exc_info=exc_info)
        return False

def read_csv_file(file_path: Union[str, Path], exc_info: bool = True) -> List[Dict[str, str]] | None:
    """! Read CSV content as a list of dictionaries.

    Args:
        file_path (str | Path): Path to the CSV file.
        exc_info (bool, optional): Include traceback information in logs. Default is True.

    Returns:
        List[Dict[str, str]] | None: List of dictionaries with CSV data or None if failed.

    Example:
        >>> data = read_csv_file('people.csv')
        >>> print(data)
        [{'name': 'Alice', 'age': '30'}]
    """
    try:
        with Path(file_path).open('r', encoding='utf-8') as f:
            return list(csv.DictReader(f))
    except Exception as ex:
        logger.error(f"Failed to read CSV from {file_path}", exc_info=exc_info)
        return


def read_csv_as_json(csv_file_path: Union[str, Path], json_file_path: Union[str, Path], exc_info: bool = True) -> bool:
    """! Convert a CSV file to JSON format and save it.

    Args:
        csv_file_path (str | Path): Path to the CSV file.
        json_file_path (str | Path): Path to save the JSON file.
        exc_info (bool, optional): Include traceback information in logs. Default is True.

    Returns:
        bool: True if conversion is successful, else False.

    Example:
        >>> csv_to_json('people.csv', 'people.json')
        True
    """
    try:
        data = read_csv_file(csv_file_path, exc_info=exc_info)
        if data is None:
            return False
        with Path(json_file_path).open('w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        return True
    except Exception as ex:
        logger.error(f"Failed to convert CSV to JSON at {json_file_path}", exc_info=exc_info)
        return False

def read_csv_as_dict(csv_file: Union[str, Path]) -> dict | None:
    """! Convert CSV content to a dictionary.

    Args:
        csv_file (str | Path): Path to the CSV file.

    Returns:
        dict | None: Dictionary representation of CSV content, or None if failed.

    Example:
        >>> data = read_csv_as_dict('people.csv')
        >>> print(data)
        {'data': [{'name': 'Alice', 'age': '30'}]}
    """
    try:
        with Path(csv_file).open('r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return {"data": [row for row in reader]}
    except Exception as ex:
        logger.error("Failed to read CSV as dictionary", exc_info=True)
        return

def read_csv_as_ns(file_path: Union[str, Path]) -> List[dict]:
    """! Load CSV data into a list of dictionaries using Pandas.

    Args:
        file_path (str | Path): Path to the CSV file.

    Returns:
        List[dict]: List of dictionaries representing the CSV content.

    Example:
        >>> data = read_csv_as_ns('people.csv')
        >>> print(data)
        [{'name': 'Alice', 'age': '30'}]
    """
    try:
        df = pd.read_csv(file_path)
        data: SimpleNamespace = SimpleNamespace(**df.to_dict(orient='records'))
        return data
    except Exception as ex:
        logger.error(f"Failed to load CSV as namespaces from {file_path}", exc_info=True)
        return []
