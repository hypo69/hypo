## \file /dev_utils/file_counter.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module: dev_utils 
	:platform: Windows, Unix
	:synopsis:

"""
MODE = 'development'

"""
	:platform: Windows, Unix
	:synopsis:

"""
 

"""
 
	:platform: Windows, Unix
	:synopsis:

"""

"""
  :platform: Windows, Unix

"""
"""
  :platform: Windows, Unix
  :platform: Windows, Unix
  :synopsis:
"""MODE = 'development'
  
"""  """


import os
import sys
from pathlib import Path

def count_lines_in_files(directory):
    """
    Recursively counts the number of lines in text files in the specified directory and its subdirectories,
    as well as the number of classes and functions.

    @param directory: Path to the directory
    @return: Total number of lines in text files, number of classes, and number of functions
    """
    total_lines = 0
    total_classes = 0
    total_functions = 0
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            # Check if the file is a text file and not from the __pycache__ directory, and not a Jupyter Notebook file
            if not is_binary(filepath) and not filename.endswith('.ipynb') and filename != '__init__.py':
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
                    lines_in_file, classes_in_file, functions_in_file = count_lines_classes_functions(file)
                    total_lines += lines_in_file
                    total_classes += classes_in_file
                    total_functions += functions_in_file
        elif os.path.isdir(filepath):
            if not filename.startswith('__pycache__') or not filename.startswith('.') :  # Exclude __pycache__ directories
                # If it's a directory, recursively call the function to count lines, classes, and functions in it
                nested_lines, nested_classes, nested_functions = count_lines_in_files(filepath)
                total_lines += nested_lines
                total_classes += nested_classes
                total_functions += nested_functions
    return total_lines, total_classes, total_functions

def is_binary(filepath):
    """
    Checks if the file is binary.

    @param filepath: Path to the file
    @return: True if the file is binary, otherwise False
    """
    try:
        with open(filepath, 'rb') as file:
            # Read the first 512 bytes of the file to check for null bytes
            chunk = file.read(512)
            return b'\0' in chunk
    except Exception as ex:
        # If there's an error reading the file, consider it binary
        print(f"Error reading file '{filepath}': {ex}")
        return True


def count_lines_classes_functions(file):
    """
    Counts the number of lines, classes, and functions in the file.

    @param file: File object
    @return: Number of lines, number of classes, and number of functions
    """
    lines = 0
    classes_count = 0
    functions_count = 0
    for line in file:
        line = line.strip()  # Remove leading and trailing whitespace
        if line:  # Check if the line is not empty
            lines += 1
            if line.startswith('class'):
                classes_count += 1
            elif line.startswith('def'):
                functions_count += 1
    return lines, classes_count, functions_count


if __name__ == "__main__":
    dir_root = Path(os.getcwd()[:os.getcwd().rfind('hypotez')+7])  # Root directory of the project
    dir_src = Path(dir_root, 'src')
    
    print(f"Counting lines, classes, and functions in files in directory: {dir_src}")
    total_lines, total_classes, total_functions = count_lines_in_files(dir_src)
    print(f"Total lines in text files in '{dir_src}': {total_lines}")
    print(f"Total classes: {total_classes}")
    print(f"Total functions: {total_functions}")
