## \file src/utils/xls.py
## \file src/utils/xls.py
# -*- coding: utf-8 -*-
#! /path/to/python/interpreter
"""
Converter for Excel (`xls`) to JSON and JSON to Excel (`xls`).
This module provides functions to convert Excel files to JSON format, handle multiple sheets, and save JSON data back to Excel files.

Functions:
    read_xls_as_dict(xls_file: str, json_file: str = None, sheet_name: Union[str, int] = None) -> Union[Dict, List[Dict], bool]:
        Convert an Excel file to JSON format. Optionally, convert a specific sheet and save the result to a JSON file.

    save_xls_file(data: Dict[str, List[Dict]], file_path: str) -> bool:
        Save data to an Excel file. The data should be a dictionary where keys are sheet names and values are lists of dictionaries representing rows.

Examples:
    >>> data = read_xls_as_dict('input.xlsx', 'output.json')
    >>> print(data)
    {'Sheet1': [{'column1': 'value1', 'column2': 'value2'}]}

    >>> success = save_xls_file({'Sheet1': [{'column1': 'value1', 'column2': 'value2'}]}, 'output.xlsx')
    >>> print(success)
    True
"""

import pandas as pd
import json
from typing import List, Dict, Union
from pathlib import Path

def read_xls_as_dict(
    xls_file: str,
    json_file: str = None,
    sheet_name: Union[str, int] = None
) -> Union[Dict, List[Dict], bool]:
    """Convert an Excel file to JSON format. Optionally, convert a specific sheet and save the result to a JSON file.

    Args:
        xls_file (str): Path to the input Excel file.
        json_file (str, optional): Path to the output JSON file. If not provided, JSON data is not saved to a file.
        sheet_name (Union[str, int], optional): The sheet name or index to convert. If not specified, all sheets are processed.

    Returns:
        Union[Dict, List[Dict], bool]: JSON data as a dictionary or list of dictionaries, or False if an error occurred.

    Example:
        >>> data = read_xls_as_dict('input.xlsx', 'output.json')
        >>> print(data)
        {'Sheet1': [{'column1': 'value1', 'column2': 'value2'}]}
    """
    try:
        # Load the Excel file
        xls = pd.ExcelFile(xls_file)
        
        if sheet_name is None:
            # Convert all sheets to JSON
            all_sheets_data = {}
            for sheet in xls.sheet_names:
                df = pd.read_excel(xls, sheet_name=sheet)
                all_sheets_data[sheet] = df.to_dict(orient='records')
            data_dict = all_sheets_data
        else:
            # Convert specified sheet to JSON
            df = pd.read_excel(xls, sheet_name=sheet_name)
            data_dict = df.to_dict(orient='records')

        if json_file:
            # Save JSON to file if path is provided
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(data_dict, f, ensure_ascii=False, indent=4)
        
        return data_dict
    
    except Exception as ex:
        print(f"Error occurred: {ex}")
        return False

def save_xls_file(
    data: Dict[str, List[Dict]],
    file_path: str
) -> bool:
    """Save data to an Excel file. The data should be a dictionary where keys are sheet names and values are lists of dictionaries representing rows.

    Args:
        data (Dict[str, List[Dict]]): Data to be saved, where keys are sheet names and values are lists of dictionaries representing rows.
        file_path (str): Path to the output Excel file.

    Returns:
        bool: True if successful, else False.

    Example:
        >>> data = {'Sheet1': [{'column1': 'value1', 'column2': 'value2'}]}
        >>> success = save_xls_file(data, 'output.xlsx')
        >>> print(success)
        True
    """
    try:
        with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
            for sheet_name, rows in data.items():
                df = pd.DataFrame(rows)
                df.to_excel(writer, sheet_name=sheet_name, index=False)
        return True
    except Exception as ex:
        print(f"Error occurred: {ex}")
        return False
