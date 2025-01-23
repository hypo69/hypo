## \file /dev_utils/rst_indexer.py
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


"""
This module recursively traverses subdirectories from the current directory,
reads all *.py files, and creates an index.rst file in the `docs` directory 
formatted according to Sphinx conventions.
"""
import header
import os
from pathlib import Path
from src.logger import logger

def create_index_rst(start_dir: str) -> None:
    """
    Recursively traverses all subdirectories from the start directory, reads all *.py files,
    and creates an index.rst file in the `docs` directory that lists all these files
    using the Sphinx `toctree` structure. Logs the process throughout.

    Args:
        start_dir (str): The root directory to start the traversal from.

    Returns:
        None

    Example:
        >>> create_index_rst(os.getcwd())
    """
    start_path = Path(start_dir)
    docs_dir = start_path / 'docs'
    index_file_path = docs_dir / 'index.rst'

    # Ensure the docs directory exists
    if not docs_dir.exists():
        docs_dir.mkdir(parents=True)
        logger.info(f"Created 'docs' directory at: {docs_dir}")

    logger.info(f"Starting to create index.rst in directory: {docs_dir}")

    try:
        with index_file_path.open('w', encoding='utf-8') as index_file:
            logger.debug(f"Opening file for writing: {index_file_path}")

            # Writing the header for index.rst in Sphinx format
            index_file.write("Welcome to the Project's Documentation\n")
            index_file.write("======================================\n\n")
            index_file.write(".. toctree::\n")
            index_file.write("   :maxdepth: 2\n")
            index_file.write("   :caption: Contents:\n\n")

            found_files = False
            for root, _, files in os.walk(start_path):
                py_files = [f for f in files if f.endswith('.py') and '(' not in f and ')' not in f]

                if py_files:
                    found_files = True
                    # Calculating relative path for Sphinx documentation
                    rel_root = Path(root).relative_to(start_path)

                    for py_file in py_files:
                        module_path = rel_root / py_file
                        # Removing `.py` extension for module path
                        module_name = str(module_path).replace('.py', '').replace(os.sep, '.')
                        # Adding module to index.rst with Sphinx format
                        index_file.write(f"   {module_name}\n")

                    logger.info(f"Added {len(py_files)} Python files from {root} to index.rst")

            if not found_files:
                logger.info("No Python files found in the specified directory.")
                index_file.write("\nNo modules found.\n")

        logger.debug(f"Successfully wrote to file: {index_file_path}")

    except Exception as ex:
        logger.error(f"An error occurred while creating index.rst: {ex}")
        raise ex

# Example usage
if __name__ == "__main__":
    create_index_rst(Path(header.__root__, 'src', 'utils'))
