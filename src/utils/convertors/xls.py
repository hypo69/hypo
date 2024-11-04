## \file src/utils/convertors/xls.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
"""

"""
from pathlib import Path

from src.utils.xls import read_xls_as_dict, save_xls_file


def xls2dict(xls_file: str | Path) -> dict | None:
    """!"""
    return read_xls_as_dict(xls_file = xls_file)

