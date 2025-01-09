## \file /src/utils/convertors/ns.py
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
.. module:: src.utils.convertors.ns 
	:platform: Windows, Unix
	:synopsis: convert SimpleNamespace (ns) into various formats: dict, JSON, CSV, XML, and XLS

Functions:
    - ns2dict: Convert SimpleNamespace object to a dictionary.
    - ns2json: Convert SimpleNamespace object to JSON format.
    - ns2csv: Convert SimpleNamespace object to CSV format.
    - ns2xml: Convert SimpleNamespace object to XML format.
    - ns2xls: Convert SimpleNamespace object to XLS format.
"""

import json
import csv
from types import SimpleNamespace
from pathlib import Path
from typing import List, Dict, Any
from src.utils.convertors import xml2dict
from src.utils.csv import save_csv_file
from src.utils.xls import save_xls_file
from src.logger.logger import logger


from types import SimpleNamespace
from typing import Any, Dict
from types import SimpleNamespace
from typing import Any, Dict

from types import SimpleNamespace
from typing import Any, Dict

def ns2dict(obj: Any) -> Dict[str, Any]:
    """
    Recursively convert an object with key-value pairs to a dictionary.
    Handles empty keys by substituting them with an empty string.

    Args:
        obj (Any): The object to convert. Can be SimpleNamespace, dict, or any object
                   with a similar structure.

    Returns:
        Dict[str, Any]: Converted dictionary with nested structures handled.
    """
    def convert(value: Any) -> Any:
        """
        Recursively process values to handle nested structures and empty keys.

        Args:
            value (Any): Value to process.

        Returns:
            Any: Converted value.
        """
        # If the value has a `__dict__` attribute (e.g., SimpleNamespace or custom objects)
        if hasattr(value, '__dict__'):
            return {key or "": convert(val) for key, val in vars(value).items()}
        # If the value is a dictionary-like object (has .items())
        elif hasattr(value, 'items'):
            return {key or "": convert(val) for key, val in value.items()}
        # If the value is a list or other iterable
        elif isinstance(value, list):
            return [convert(item) for item in value]
        return value

    return convert(obj)




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
