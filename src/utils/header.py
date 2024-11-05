## \file ./src/utils/header.py
# -*- coding: utf-8 -*-
#! /venv/Scripts/python.exe
# /path/to/interpreter/python
"""! Module to set the project root path """
import json
import sys
import os
from pathlib import Path

def find_project_root(marker_files=('pyproject.toml', 'requirements.txt', '.git')):
    """! Finds the root directory of the project starting from the current file's directory,
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

# Get the project name from the root folder
project_name = __root__.name  # This will get the name of the directory in __root__

# Alternatively, if you want to keep the logic of reading from settings.json
try:
    with open('../settings.json', 'r') as settings_file:
        settings = json.load(settings_file)
        project_name = settings.get("project_name", project_name)  # Fallback to folder name if not found
        
except (FileNotFoundError, json.JSONDecodeError) as ex:
    print(ex)
    ...
except Exception as ex:
    print(ex)
    ...


# Paths to bin directories
gtk_bin_path = __root__ / "bin" / "gtk" / "gtk-nsis-pack" / "bin"
ffmpeg_bin_path = __root__ / "bin" / "ffmpeg" / "bin"
graphviz_bin_path = __root__ / "bin" / "graphviz" / "bin"

# Update the PATH variable if the paths are missing
paths_to_add = [gtk_bin_path, ffmpeg_bin_path, graphviz_bin_path]
current_paths = set(Path(p) for p in sys.path)

for bin_path in paths_to_add:
    if bin_path not in current_paths:
        sys.path.insert(0, str(bin_path))

os.environ['WEASYPRINT_DLL_DIRECTORIES'] = str(gtk_bin_path)


"""Suppress GTK log output to the console"""
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
