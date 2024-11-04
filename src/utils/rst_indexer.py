## \file src/utils/rst_indexer.py
# -*- coding: utf-8 -*-
#! /path/to/python/interpreter
"""
This module recursively traverses subdirectories from the current directory,
reads all *.py files, and creates an index.rst file in the `docs` directory that lists all these files.
It also logs the process for tracking and debugging purposes.
"""
import header
import os
from pathlib import Path
from src.logger import logger

def create_index_rst(start_dir: str) -> None:
    """
    Recursively traverses all subdirectories from the start directory, reads all *.py files,
    and creates an index.rst file in the `docs` directory that lists all these files. Logs the process throughout.

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
        with index_file_path.open('w') as index_file:
            logger.debug(f"Opening file for writing: {index_file_path}")
            index_file.write('Python Modules Index\n')
            index_file.write('====================\n\n')

            found_files = False
            for root, _, files in os.walk(start_path):
                py_files = [f for f in files if f.endswith('.py') and '(' not in f and ')' not in f]

                if py_files:
                    found_files = True
                    logger.info(f"Processing directory: {root}")
                    index_file.write(f'In directory: {root}\n')
                    index_file.write('------------------\n')
                    for py_file in py_files:
                        module_path = Path(root).relative_to(start_path) / py_file
                        index_file.write(f'- `/{module_path}`\n')
                    index_file.write('\n')
                    logger.info(f"Added {len(py_files)} Python files from {root} to index.rst")

            if not found_files:
                logger.info("No Python files found in the specified directory.")

        logger.debug(f"Successfully wrote to file: {index_file_path}")

    except Exception as e:
        logger.error(f"An error occurred while creating index.rst: {e}")
        raise

# Example usage
if __name__ == "__main__":
    create_index_rst(Path(header.__root__, 'src', 'utils'))
