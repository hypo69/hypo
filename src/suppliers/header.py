## \file hypotez/src/suppliers/header.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
#! venv/bin/python # <- venv linux/macos
#! py # <- system win
#! /usr/bin/python # <- system linux/macos
## ~~~~~~~~~~~~~
""" module: src.suppliers """
import sys
from pathlib import Path
from packaging.version import Version

# Define the project root directory
def get_project_root(marker_files=('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """!
    Finds the project's root directory starting from the current file's directory and moving upwards
    in the hierarchy until one of the marker files is found.

    Args:
        marker_files (tuple): Filenames or directory names that identify the project's root.

    Returns:
        Path: The path to the root directory if found, otherwise the directory where the script is located.
    """
    __root__: Path 
    current_path = Path(__file__).resolve().parent
    __root__ = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    if str(__root__) not in sys.path:
        sys.path.insert(0, str(__root__))
        
    return __root__

__root__: Path = get_project_root()
