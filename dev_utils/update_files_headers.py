## \file ./dev_utils/update_files_headers.py
# -*- coding: utf-8 -*-
#! /venv/Scripts/python.exe
import os
from pathlib import Path

def add_or_replace_file_header(file_path: str):
    """Adds or replaces a header and interpreter line in the specified Python file.

    This function ensures that the Python file has a consistent header, coding declaration, 
    and interpreter line by removing any existing lines that match these patterns 
    and replacing them with new ones in the specified order.

    Additionally, it removes any BOM (U+FEFF) characters if they exist.

    Args:
        file_path (str): The path to the Python file to be processed.

    Example:
        >>> add_or_replace_file_header('example.py')
        This will add or update the header, coding declaration, and interpreter line in 'example.py'.
    """
    # Convert backslashes to forward slashes for the file path
    file_path = file_path.replace('\\', '/')
    header_line = f'## \\file {file_path}\n'
    coding_index = '# -*- coding: utf-8 -*-\n'
    interpreter_line = '#! /venv/Scripts/python.exe\n'  # Specify the desired interpreter line

    print(f"Processing file: {file_path}")
    
    try:
        with open(file_path, 'r+', encoding='utf-8', newline='') as file:
            lines = file.readlines()

            # Remove BOM from each line if present
            cleaned_lines = [line.lstrip('\ufeff') for line in lines]

            # Remove existing lines that match the specified patterns
            filtered_lines = [
                line for line in cleaned_lines 
                if not (line.startswith("## \\file") 
                        or line.startswith("# -*- coding")
                        or line.startswith("#! /path/to/interpreter/python")
                        or line.startswith("#! /venv/Scripts/python.exe"))
            ]

            # Flags to check if lines need to be added
            header_needs_update = not any(line == header_line for line in filtered_lines)
            coding_needs_update = not any(line == coding_index for line in filtered_lines)
            interpreter_needs_update = not any(line == interpreter_line for line in filtered_lines)

            print(f"Header needs update: {header_needs_update}")
            print(f"Coding declaration needs update: {coding_needs_update}")
            print(f"Interpreter line needs update: {interpreter_needs_update}")

            # Prepare the lines to be added in order
            new_lines = []
            if header_needs_update:
                print("Adding header line.")
                new_lines.append(header_line)
            if coding_needs_update:
                print("Adding coding declaration line.")
                new_lines.append(coding_index)
            if interpreter_needs_update:
                print("Adding interpreter line.")
                new_lines.append(interpreter_line)

            # Insert new lines at the beginning of filtered lines
            if new_lines:
                print("Writing new lines to the file.")
                file.seek(0)  # Move to the start of the file
                file.writelines(new_lines + filtered_lines)  # Write new lines followed by remaining content
                file.truncate()  # Remove any leftover content after the new end of file
                print(f"Updated {file_path} successfully.")
            else:
                print(f"No updates necessary for {file_path}.")

    except IOError as ex:
        print(f"Error processing file {file_path}: {ex}")

def traverse_directory(directory: str):
    """Recursively traverses the directory and processes Python files.

    This function walks through the given directory and all its subdirectories,
    processing each Python file found by calling `add_or_replace_file_header` 
    to ensure consistent headers.

    Args:
        directory (str): The root directory to start traversing.

    Example:
        >>> traverse_directory('/path/to/directory')
        This will recursively process all Python files in '/path/to/directory'.
    """
    print(f"Traversing directory: {directory}")
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                print(f"Found Python file: {file_path}")
                add_or_replace_file_header(file_path)

def main():
    """Main function to execute the script.

    This function sets the root directory for the script to start processing
    Python files by invoking `traverse_directory`.

    Example:
        >>> main()
        This will start processing Python files in the specified root directory.
    """
    root_dir = Path('.')  # Set your target directory here
    print(f"Starting script to process Python files in: {root_dir}")
    traverse_directory(root_dir)

if __name__ == "__main__":
    main()
