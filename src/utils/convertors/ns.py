## \file src/utils/convertors/ns.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
"""
Module to convert SimpleNamespace (ns) into various formats: dict, JSON, CSV, XML, and XLS.

Functions:
    - ns2dict: Convert SimpleNamespace object to a dictionary.
    - ns2json: Convert SimpleNamespace object to JSON format.
    - ns2csv: Convert SimpleNamespace object to CSV format.
    - ns2xml: Convert SimpleNamespace object to XML format.
    - ns2xls: Convert SimpleNamespace object to XLS format.
"""

import header
import json
import csv
from types import SimpleNamespace
from pathlib import Path
from typing import List, Dict
from src.utils.convertors import xml2dict
from src.utils.csv import save_csv_file
from src.utils.jjson import j_dumps
from src.utils.xls import save_xls_file
from src.logger import logger


def ns2dict(ns_obj: SimpleNamespace) -> dict:
    """
    Convert SimpleNamespace object to a dictionary.

    Args:
        ns_obj (SimpleNamespace): The SimpleNamespace object to convert.

    Returns:
        dict: Converted dictionary.
    """
    return vars(ns_obj)


def ns2json(ns_obj: SimpleNamespace, json_file_path: str | Path = None) -> str | bool:
    """
    Convert SimpleNamespace object to JSON format.

    Args:
        ns_obj (SimpleNamespace): The SimpleNamespace object to convert.
        json_file_path (str | Path, optional): Path to save the JSON file. If not provided, returns the JSON string.

    Returns:
        str | bool: JSON string if no file path is provided, otherwise True if the file is written successfully.
    """
    try:
        data = ns2dict(ns_obj)
        json_data = json.dumps(data, indent=4)
        
        if json_file_path:
            with open(json_file_path, 'w', encoding='utf-8') as json_file:
                json_file.write(json_data)
            return True
        return json_data
    except Exception as ex:
        logger.error(f"ns2json failed", ex, True)


def ns2csv(ns_obj: SimpleNamespace, csv_file_path: str | Path) -> bool:
    """
    Convert SimpleNamespace object to CSV format.

    Args:
        ns_obj (SimpleNamespace): The SimpleNamespace object to convert.
        csv_file_path (str | Path): Path to save the CSV file.

    Returns:
        bool: True if successful, False otherwise.
    """
    try:
        data = [ns2dict(ns_obj)]
        save_csv_file(data, csv_file_path)
        return True
    except Exception as ex:
        logger.error(f"ns2csv failed", ex, True)




def ns2xml(ns_obj: SimpleNamespace, root_tag: str = "root") -> str:
    """
    Convert SimpleNamespace object to XML format.

    Args:
        ns_obj (SimpleNamespace): The SimpleNamespace object to convert.
        root_tag (str): The root element tag for the XML.

    Returns:
        str: The resulting XML string.
    """
    try:
        data = ns2dict(ns_obj)
        return xml2dict(data)
    except Exception as ex:
        logger.error(f"ns2xml failed", ex, True)


def ns2xls(data: SimpleNamespace, xls_file_path: str | Path) -> bool:
    """
    Convert SimpleNamespace object to XLS format.

    Args:
        ns_obj (SimpleNamespace): The SimpleNamespace object to convert.
        xls_file_path (str | Path): Path to save the XLS file.

    Returns:
        bool: True if successful, False otherwise.
    """
    return save_xls_file(data,xls_file_path)
