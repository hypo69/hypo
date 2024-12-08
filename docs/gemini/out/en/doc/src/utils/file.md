# hypotez/src/utils/file.py

## Overview

This module provides functions for various file operations, including saving data to files, reading file contents, retrieving filenames, recursively searching files, and removing Byte Order Marks (BOMs).  It leverages the `pathlib` module for robust file path handling and includes logging for error reporting.


## Functions

### `save_text_file`

**Description**: Saves data to a text file.  Supports saving strings, lists of strings, and dictionaries.  Handles different data types appropriately. Creates parent directories if they don't exist.

**Parameters**:
- `data` (str | list[str] | dict): Data to write. Can be a string, list of strings, or a dictionary.
- `file_path` (str | Path): Path where the file will be saved.
- `mode` (str, optional): Write mode (`w` for write, `a` for append). Defaults to "w".
- `exc_info` (bool, optional): If True, logs traceback on error. Defaults to True.

**Returns**:
- `bool`: True if the file was successfully saved, False otherwise.

**Raises**:
- `Exception`: If any error occurs during file writing.


### `read_text_file`

**Description**: Reads the contents of a file or directory. If the input is a directory, it recursively searches for files within it and reads the contents, optionally filtering by extension.

**Parameters**:
- `file_path` (str | Path): Path to the file or directory.
- `as_list` (bool, optional): If True, returns content as a list of lines. Defaults to False.
- `extensions` (list[str], optional): List of file extensions to include if reading a directory. Defaults to None.
- `exc_info` (bool, optional): If True, logs traceback on error. Defaults to True.

**Returns**:
- `str | list[str] | None`: File content as a string or list of lines, or None if an error occurs.

**Raises**:
- `Exception`: If any error occurs during file reading.


### `get_filenames`

**Description**: Retrieves filenames within a specified directory, optionally filtering by extension.

**Parameters**:
- `directory` (str | Path): Directory to search.
- `extensions` (str | list[str], optional): Extensions to filter. Defaults to "*".

**Returns**:
- `list[str]`: List of filenames found in the directory.

**Raises**:
- `Exception`: If any error occurs during filename retrieval.


### `recursively_yield_file_path`

**Description**: Recursively yields file paths matching given patterns within a specified directory.

**Parameters**:
- `root_dir` (str | Path): Root directory to search.
- `patterns` (str | list[str], optional): Patterns to match. Defaults to "*".

**Yields**:
- `Path`: File paths matching the patterns.

**Raises**:
- `Exception`: If any error occurs during recursive search.


### `recursively_get_file_path`

**Description**: Recursively gets file paths matching given patterns within a specified directory.

**Parameters**:
- `root_dir` (str | Path): Root directory to search.
- `patterns` (str | list[str], optional): Patterns to match. Defaults to "*".

**Returns**:
- `list[Path]`: List of file paths matching the patterns.

**Raises**:
- `Exception`: If any error occurs during recursive search.



### `recursively_read_text_files`

**Description**: Recursively reads text files matching specified patterns from a root directory.


**Parameters**:
- `root_dir` (str | Path): Root directory to search.
- `patterns` (str | list[str]): Filename patterns.
- `as_list` (bool, optional): If True, returns file content as a list of lines. Defaults to False.
- `exc_info` (bool, optional): If True, includes traceback information in warnings. Defaults to True.

**Returns**:
- `list[str]`: List of file contents (or lines if `as_list=True`) matching the patterns.


**Raises**:
- `Exception`: If any error occurs during file reading.

### `get_directory_names`

**Description**: Retrieves all directory names from a given directory.

**Parameters**:
- `directory` (str | Path): Directory to search.
- `exc_info` (bool, optional): If True, logs traceback information on error. Defaults to True.

**Returns**:
- `list[str]`: List of directory names found.

**Raises**:
- `Exception`: If an error occurs during directory retrieval.


### `read_files_content`

**Description**: Reads contents of files matching patterns recursively.

**Parameters**:
- `root_dir` (str | Path): Root directory to search.
- `patterns` (str | list[str]): File patterns.
- `as_list` (bool, optional): Returns content as list of lines. Defaults to False.
- `exc_info` (bool, optional): If True, logs traceback on error. Defaults to True.


**Returns**:
- `list[str]`: List of file contents.


**Raises**:
- `Exception`: If any error occurs during file reading.

### `remove_bom`

**Description**: Removes BOM (Byte Order Mark) from a text file.

**Parameters**:
- `file_path` (str | Path): Path to the file.


**Raises**:
- `Exception`: If an error occurs during BOM removal.

### `traverse_and_clean`

**Description**: Traverses a directory and removes BOMs from Python files.

**Parameters**:
- `directory` (str | Path): Root directory to process.



**Raises**:
- `Exception`: If an error occurs during the traversal or BOM removal.

### `main`

**Description**: Entry point for BOM removal in Python files.

**Raises**:
- No explicit exception raising.