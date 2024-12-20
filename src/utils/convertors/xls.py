## \file hypotez/src/utils/convertors/xls.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module:: src.utils.convertors 
	:platform: Windows, Unix
	:synopsis:

"""
MODE = 'dev'


from pathlib import Path

from src.utils.xls import read_xls_as_dict, save_xls_file


def xls2dict(xls_file: str | Path) -> dict | None:
    """"""
    return read_xls_as_dict(xls_file = xls_file)

