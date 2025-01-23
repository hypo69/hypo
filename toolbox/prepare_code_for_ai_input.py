## \file /dev_utils/prepare_code_for_ai_input.py
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


""" This script collects the contents of specific files in the 'src' directory, 
saves them in a single text file for machine learning model input, excluding 
specific directories and files, and including only .py, .json, .md, .dot, and .mer files.
"""

import header
from pathlib import Path
from src.utils.jjson import j_dumps

def collect_file_contents(directory: Path, target_directory: Path) -> dict:
    """ Recursively collects the content of specific files.

    Traverses the specified `directory`, filters out unwanted directories and files,
    and collects the content of remaining files with specific extensions.

    Args:
        directory (Path): Path to the source directory to scan.
        target_directory (Path): Path to save the final text file for ML input.

    Returns:
        dict: A dictionary where keys are file paths and values are file contents.

    """
    contents = {}

    for item in directory.iterdir():
        if item.is_dir():
            if item.name not in ['profiles', '__pycache__', '_experiments'] and not item.name.startswith('___') and '*' not in item.name:
                contents.update(collect_file_contents(item, target_directory))
        else:
            if (item.suffix in ['.py', '.json', '.md', '.dot', '.mer']) and not item.name.startswith('___') and '*' not in item.name and '(' not in item.name and ')' not in item.name:
                with item.open('r', encoding='utf-8') as file:
                    contents[str(item)] = file.read()
                
    return contents

def save_contents_to_text(contents: dict, output_file: Path):
    """ Saves collected file contents to a single text file.

    Args:
        contents (dict): Dictionary with file paths as keys and file contents as values.
        output_file (Path): Path to the output text file for ML input.

    """
    with output_file.open('w', encoding='utf-8') as f:
        for path, content in contents.items():
            f.write(f"File: {path}\n")
            f.write(content)
            f.write("\n" + "="*80 + "\n\n")  # Separator between files

def main():
    """ Main function to initiate content collection and save to a text file."""

    src_directory = Path(header.__root__, 'src', 'utils')
    project_structure_directory = Path(src_directory, 'prod')
    project_structure_directory.mkdir(parents=True, exist_ok=True)  # Ensure the 'prod' folder exists

    # Collect contents of files
    file_contents = collect_file_contents(src_directory, project_structure_directory)
    
    # Save all contents to a single text file for ML
    output_file_path = Path(project_structure_directory, 'all_file_contents.txt')
    save_contents_to_text(file_contents, output_file_path)

if __name__ == "__main__":
    main()
