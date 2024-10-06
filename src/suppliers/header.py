## \file ./utils/examples/header.py
## \file ../src/suppliers/header.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
""" Module to set the project root path """

import sys
import os
from pathlib import Path

def find_project_root(marker_files_or_dirs: tuple = ('pyproject.toml', 'requirements.txt', '.git'), marker_in_dirname: str = None):
    """ Finds the root directory of the project starting from the current file's directory,
    searching upwards and stopping at the first directory containing any of the marker files 
    or directories, or a directory name containing the marker string.
    
    Args:
        marker_files_or_dirs (tuple): Filenames or directory names to identify the project root.
        marker_in_dirname (str, optional): String to look for in the directory name.

    Returns:
        Path: Path to the root directory if found, otherwise the directory where the script is located.
    """
    # Get the directory of the current file (where this function is called)
    current_path = Path(__file__).resolve().parent

    # Traverse upwards through the directory tree, starting from the file's directory
    for parent in [current_path] + list(current_path.parents):
        # Check if any of the marker files (e.g., 'pyproject.toml', 'requirements.txt', '.git') exist in the current directory
        if any((parent / marker).exists() for marker in marker_files_or_dirs):
            return parent
        
        # Check if the current directory name contains the marker string
        if marker_in_dirname and marker_in_dirname in parent.name:
            return parent

    # If no marker files or directories are found, return the current directory of the file as a fallback
    return current_path

# Define marker files and directory name substring
marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')
marker_in_dirname: str = 'utils'

# Call the function to find the project root
__root__: Path = find_project_root(marker_files, marker_in_dirname)

# Add the project root to `sys.path` to allow importing modules from the project root
sys.path.append(str(__root__))
