## \file ./src/product/product_fields/utils/product_fields_normalizer.py
# -*- coding: utf-8 -*-
#! /venv/Scripts/python.exe
#! /usr/bin/python
#! /usr/share/projects/hypotez/venv/scripts python
"""! HERE SHOULD BE A DESCRIPTION OF THE MODULE OPERATION ! """

from typing import Dict, Union
from src.utils.string import StringNormalizer as sn
from src.utils.string import StringFormatter as sf

def normalize_product_name(value: str) -> str:
    """Normalize product name.

    Args:
        value (str): Product name.

    Returns:
        str: Normalized product name.
    """
    return sn.normalize_string(value)

def normalize_bool(value: Union[str, bool]) -> int:
    """Convert boolean values to 1/0.

    Args:
        value (Union[str, bool]): Value to be normalized.

    Returns:
        int: 1 for True, 0 for False.
    """
    return 1 if sn.normalize_boolean(value) else 0


