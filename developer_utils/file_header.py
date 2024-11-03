## \file src/suppliers/aliexpress/gui/category.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
"""! HERE SHOULD BE A DESCRIPTION OF THE MODULE OPERATION ! """

import header 

import os
from pathlib import Path

def add_or_replace_file_header(file_path: str):
    """! Adds or replaces a header above the coding declaration in the Python file.
    
    @param file_path The path to the Python file.
    """
    # Convert backslashes to forward slashes for the file path
    file_path = file_path.replace('\\', '/')
    header_line = f"## \\file {file_path}\n"
    
    try:
        with open(file_path, 'r+', encoding='utf-8', newline='') as file:
            lines = file.readlines()
            
            # Check if the coding declaration exists
            coding_index = next((i for i, line in enumerate(lines) if line.strip() == '# -*- coding: utf-8 -*-'), None)
            
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
            
            file.seek(0, 0)  # Move the cursor to the beginning of the file
            file.writelines(lines)
            file.truncate()  # Truncate the file to the new length
    
    except IOError as ex:
        print(f"Error processing file {file_path}: {ex}")

def traverse_directory(directory: str):
    """! Recursively traverses the directory and processes Python files.
    
    @param directory The root directory to start traversing.
    """
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                add_or_replace_file_header(file_path)

def main():
    root_dir = Path('..', 'src')
    traverse_directory(root_dir)

if __name__ == "__main__":
    main()
