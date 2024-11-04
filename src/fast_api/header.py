## \file ./utils/examples/header.py
## \file src/fast_api/header.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
""" Module to set the project root path """

import sys
import os
from pathlib import Path

def find_project_root(marker_files=('pyproject.toml', 'requirements.txt', '.git')):
    """ Finds the root directory of the project starting from the current file's directory,
    searching upwards and stopping at the first directory containing any of the marker files.
    
    Args:
        marker_files (tuple): Filenames or directory names to identify the project root.
    
    Returns:
        Path: Path to the root directory if found, otherwise the directory where the script is located.
    """
    # Get the directory of the current file (where this function is called)
    current_path = Path(__file__).resolve().parent

    # Traverse upwards through the directory tree, starting from the file's directory
    for parent in [current_path] + list(current_path.parents):
        # Check if any of the marker files (e.g., 'pyproject.toml', 'requirements.txt', '.git') exist in the current directory
        if any((parent / marker).exists() for marker in marker_files):
            # If found, return this directory as the root of the project
            return parent

    # If no marker files are found, return the current directory of the file as a fallback
    return current_path

# Call the function to find the project root
__root__: Path = find_project_root()

# Add the project root to `sys.path` to allow importing modules from the project root
sys.path.append(str(__root__))
