## \file hypotez/src/webdriver/__init__.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" module: src.webdriver """
MODE = 'debug'
""" module: src.webdriver """
MODE = 'debug'


import sys
from pathlib import Path
def get_project_root(marker_files=('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """!
    Finds the root directory of the project starting from the current file's directory,
    searching upwards and stopping at the first directory containing any of the marker files.

    Args:
        marker_files (tuple): Filenames or directory names to identify the project root.
    
    Returns:
        Path: Path to the root directory if found, otherwise the directory where the script is located.
    """
    __root__:Path
    current_path:Path = Path(__file__).resolve().parent
    __root__ = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__


# Get the root directory of the project
__root__: Path = get_project_root()
"""__root__ (Path): Path to the root directory of the project"""
from src import gs

from packaging.version import Version
from .version import __doc__, __details__, __version__  

from .driver import Driver
from .chrome import Chrome
from .firefox import Firefox
from .edge import Edge
from .bs import BS
from .playwright import Playwrid
from .crawlee_python import CrawleePython

