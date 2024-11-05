## \file ./src/__init__.py
# -*- coding: utf-8 -*-
#! /venv/Scripts/python.exe
# /path/to/interpreter/python
"""  **Это корневая директория проекта** """ 


from packaging.version import Version
from .version import __version__, __doc__, __details__
from .credentials import gs
from .check_relise import check_latest_release
