## \file ..
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

"""
This module provides functionality to add or replace headers and interpreter lines
in Python files within a specified directory. It ensures that each Python file has
a consistent header and interpreter declaration.
"""

import header

import os
from pathlib import Path

def add_or_replace_file_header(file_path: str):
    """Adds or replaces a header and interpreter line in the specified Python file.

    This function adds a header indicating the file path and ensures that the
    correct interpreter line is present at the top of the specified Python file.
    
    If the file already contains a header, it will be replaced. If the file lacks
    a coding declaration, the header will be added at the beginning. The function
    also checks if the interpreter line exists and matches the expected format,
    and adds it if missing or incorrect.

    Args:
        file_path (str): The path to the Python file to be processed.

    Example:
        >>> add_or_replace_file_header('example.py')
        This will add or update the header and interpreter line in 'example.py'.
    """
    # Convert backslashes to forward slashes for the file path
    file_path = file_path.replace('\\', '/')
    header_line = f"## \\file {file_path}\n"
    interpreter_line = '#! /usr/bin/python\n'  # Specify the desired interpreter line

    try:
        with open(file_path, 'r+', encoding='utf-8', newline='') as file:
            lines = file.readlines()

            # Check if the coding declaration exists
            coding_index = next((i for i, line in enumerate(lines) if line.strip() == '# -*- coding: utf-8 -*-'), None)

            # Check if the interpreter line exists
            interpreter_index = next((i for i, line in enumerate(lines) if line.startswith('#!')), None)

            # If coding declaration exists, update or add the header before it
            if coding_index is not None:
                if lines[coding_index - 1].startswith('## \\file '):
                    lines[coding_index - 1] = header_line  # Replace existing header with the new one
                else:
                    lines.insert(coding_index, header_line)  # Add the header before the coding declaration
            else:
                # If no coding declaration is found, just add the header at the top
                if lines and lines[0].startswith('## \\file '):
                    lines[0] = header_line  # Replace existing header with the new one
                else:
                    lines.insert(0, header_line)  # Add the header to the beginning of the file
            
            # Check and add the interpreter line if it doesn't exist or is incorrect
            if interpreter_index is None or lines[interpreter_index].strip() != interpreter_line.strip():
                lines.insert(0, interpreter_line)  # Add interpreter line at the top if missing or incorrect
            
            file.seek(0, 0)  # Move the cursor to the beginning of the file
            file.writelines(lines)
            file.truncate()  # Truncate the file to the new length

    except IOError as ex:
        print(f"Error processing file {file_path}: {ex}")

def traverse_directory(directory: str):
    """Recursively traverses the directory and processes Python files.

    This function walks through the given directory and all its subdirectories,
    processing each Python file found. It calls `add_or_replace_file_header`
    for every Python file encountered.

    Args:
        directory (str): The root directory to start traversing.

    Example:
        >>> traverse_directory('/path/to/directory')
        This will recursively process all Python files in '/path/to/directory'.
    """
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                add_or_replace_file_header(file_path)

def main():
    """Main function to execute the script.

    This function sets the root directory for the script to start processing
    Python files and invokes the `traverse_directory` function.

    Example:
        >>> main()
        This will start processing Python files in the specified root directory.
    """
    root_dir = Path('..', 'src')
    traverse_directory(root_dir)

if __name__ == "__main__":
    main()
