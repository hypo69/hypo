## \file <file_path>
# -*- coding: utf-8 -*-
# /path/to/python/interpreter
"""
This module provides functionality to add or replace headers and interpreter lines
in Python files within a specified directory. It ensures that each Python file has
a consistent header and interpreter declaration.
"""

import header
import os
from pathlib import Path

def add_or_replace_file_header(file_path: str):
    """ Adds or replaces a header and interpreter line in the specified Python file.

    This function adds a header indicating the file path and ensures that the
    correct interpreter line is present at the top of the specified Python file.
    
    If the file already contains a header, it will be replaced. If the file lacks
    a coding declaration or an interpreter line, they will be added in the specified order:
    header, coding declaration, interpreter line.

    Args:
        file_path (str): The path to the Python file to be processed.

    Example:
        >>> add_or_replace_file_header('example.py')
        This will add or update the header and interpreter line in 'example.py'.
    """
    # Convert backslashes to forward slashes for the file path
    file_path = file_path.replace('\\', '/')
    header_line = f'## \\file {file_path}\n'
    coding_index = '# -*- coding: utf-8 -*-\n'
    interpreter_line = '# /path/to/interpreter/python\n'  # Specify the desired interpreter line

    try:
        with open(file_path, 'r+', encoding='utf-8', newline='') as file:
            lines = file.readlines()

            # Flags to track the presence of lines
            has_header = any(line.startswith('## \\file ') for line in lines)
            has_coding = any(line.strip() == coding_index.strip() for line in lines)
            has_interpreter = any(line.startswith('# /path/to/interpreter/python') for line in lines)

            # Prepare the lines to be added in order
            new_lines = []
            if not has_header:
                new_lines.append(header_line)
            if not has_coding:
                new_lines.append(coding_index)
            if not has_interpreter:
                new_lines.append(interpreter_line)

            # Insert new lines at the beginning if any are missing
            if new_lines:
                file.seek(0, 0)  # Move the cursor to the beginning of the file
                file.writelines(new_lines + lines)  # Write new lines followed by existing lines
                file.truncate()  # Truncate the file to the new length

    except IOError as ex:
        print(f"Error processing file {file_path}: {ex}")

def traverse_directory(directory: str):
    """ Recursively traverses the directory and processes Python files.

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
    """ Main function to execute the script.

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
