## \file ../src/utils/csv.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
"""!
Module for CSV file operations.

This module provides functions for saving and reading CSV files, including:
- Saving data to a CSV file.
- Reading data from a CSV file.
- Converting data from JSON to CSV and vice versa.
- Converting CSV data to a dictionary format.

Functions:
    save_csv_file(data: List[Dict[str, str]], file_path: str | Path, mode: str = 'a', exc_info: bool = True) -> bool:
        Saves a list of dictionaries to a CSV file.

    read_csv_file(file_path: str | Path, exc_info: bool = True) -> List[Dict[str, str]] | None:
        Reads the content of a CSV file and returns it as a list of dictionaries.

    json_to_csv(json_data: List[Dict[str, str]], csv_file_path: str | Path, exc_info: bool = True) -> bool:
        Converts a list of dictionaries from JSON format to a CSV file.

    csv_to_json(csv_file_path: str | Path, json_file_path: str | Path, exc_info: bool = True) -> List[Dict[str, str]] | None:
        Converts a CSV file to JSON format and saves it to a JSON file.

    read_csv_as_dict(csv_file: str | Path) -> dict | bool:
        Converts CSV data to a dictionary containing the data from the CSV file.

Examples:
    >>> data = [{'role': 'user', 'content': 'Hello'}, {'role': 'assistant', 'content': 'Hi there!'}]
    >>> success = save_csv_file(data=data, file_path='dialogue_log.csv')
    >>> print(success)
    True

    >>> data = read_csv_file(file_path='dialogue_log.csv')
    >>> print(data)
    [{'role': 'user', 'content': 'Hello'}, {'role': 'assistant', 'content': 'Hi there!'}]

    >>> json_data = [{'role': 'user', 'content': 'Hello'}, {'role': 'assistant', 'content': 'Hi there!'}]
    >>> success = json_to_csv(json_data, 'dialogue_log.csv')
    >>> print(success)
    True

    >>> json_data = csv_to_json('dialogue_log.csv', 'dialogue_log.json')
    >>> print(json_data)
    [{'role': 'user', 'content': 'Hello'}, {'role': 'assistant', 'content': 'Hi there!'}]

    >>> data = read_csv_as_dict('dialogue_log.csv')
    >>> print(data)
    {'data': [{'role': 'user', 'content': 'Hello'}, {'role': 'assistant', 'content': 'Hi there!'}]}
"""

import csv
import json
from pathlib import Path
from typing import List, Dict, Union
from src.logger import logger

def save_csv_file(
    data: List[Dict[str, str]],
    file_path: str | Path,
    mode: str = 'a',
    exc_info: bool = True
) -> bool:
    """! Save a list of dictionaries to a CSV file.

    Args:
        data (List[Dict[str, str]]): The data to be written to the CSV file.
        file_path (str | Path): The full path to the CSV file.
        mode (str, optional): The file mode. Defaults to 'a' (append).
        exc_info (bool, optional): If True, includes traceback information in the log. Defaults to True.

    Returns:
        bool: True if successful, else False.

    Example:
        >>> data = [{'role': 'user', 'content': 'Hello'}]
        >>> success = save_csv_file(data=data, file_path='dialogue_log.csv')
        >>> print(success)
        True

        >>> data = [{'role': 'user', 'content': 'Hello'}, {'role': 'assistant', 'content': 'Hi there!'}]
        >>> success = save_csv_file(data=data, file_path='dialogue_log.csv', mode='w')
        >>> print(success)
        True
    """
    try:
        file_path = Path(file_path)
        file_exists = file_path.exists()
        file_path.parent.mkdir(parents=True, exist_ok=True)

        if data:
            headers = list(data[0].keys())
        else:
            headers = []

        with file_path.open(mode, newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            if not file_exists and headers:
                writer.writeheader()
            writer.writerows(data)
        return True
    except Exception as ex:
        logger.error(f"Failed to save CSV file {file_path}.", ex, exc_info=exc_info)
        return False

def read_csv_file(
    file_path: str | Path,
    exc_info: bool = True
) -> List[Dict[str, str]] | None:
    """! Read the content of a CSV file and return it as a list of dictionaries.

    Args:
        file_path (str | Path): The path to the CSV file to read.
        exc_info (bool, optional): If True, includes traceback information in the log. Defaults to True.

    Returns:
        List[Dict[str, str]] | None: The content of the CSV file as a list of dictionaries, or None if reading failed.

    Example:
        >>> data = read_csv_file(file_path='dialogue_log.csv')
        >>> print(data)
        [{'role': 'user', 'content': 'Hello'}, {'role': 'assistant', 'content': 'Hi there!'}]
    """
    try:
        file_path = Path(file_path)
        with file_path.open('r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except Exception as ex:
        logger.error(f"Failed to read CSV file {file_path}.", ex, exc_info=exc_info)
        return None

def read_csv_as_dict(
    csv_file: str | Path
) -> dict | bool:
    """! Convert CSV data to a dictionary containing the data from the CSV file.

    Args:
        csv_file (str | Path): The path to the CSV file to read.

    Returns:
        dict | bool: Dictionary containing the data from CSV, or False if conversion failed.

    Example:
        >>> data = read_csv_as_dict('dialogue_log.csv')
        >>> print(data)
        {'data': [{'role': 'user', 'content': 'Hello'}, {'role': 'assistant', 'content': 'Hi there!'}]}
    """
    try:
        with open(csv_file, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            rows = [row for row in reader]

        if len(rows[0]) == 1:
            # If there is only one column, return a list of values
            return {"data": [row[0] for row in rows]}
        else:
            # Otherwise, assume multiple columns and return a list of dictionaries
            headers = rows[0]
            data = [dict(zip(headers, row)) for row in rows[1:]]
            return {"data": data}
    except Exception as ex:
        logger.error("Failed to convert CSV to dictionary", ex)
        return False

def read_csv_as_ns():
    """! Placeholder function for future extension.

    Currently, this function does nothing and serves as a stub for future implementation.
    """
    pass
