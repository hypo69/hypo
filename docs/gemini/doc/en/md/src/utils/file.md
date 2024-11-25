# hypotez/src/utils/file.py

## Overview

This module provides functions for various file operations, including saving data to files, reading file contents, getting filenames, recursively yielding/getting file paths, and recursively reading text files from directories.  It also includes functions for removing Byte Order Marks (BOM) from files and traversing directories for specific operations (like BOM removal).

## Table of Contents

* [save_text_file](#save-text-file)
* [read_text_file](#read-text-file)
* [get_filenames](#get-filenames)
* [recursively_yield_file_path](#recursively-yield-file-path)
* [recursively_get_file_path](#recursively-get-file-path)
* [recursively_read_text_files](#recursively-read-text-files)
* [get_directory_names](#get-directory-names)
* [read_files_content](#read-files-content)
* [remove_bom](#remove-bom)
* [traverse_and_clean](#traverse-and-clean)
* [main](#main)


## Functions

### `save_text_file`

**Description**: Saves data to a text file.  Supports saving strings, lists of strings, and dictionaries. Uses JSON for dictionaries, ensuring proper encoding and indentation.

**Parameters**:
- `data` (str | list[str] | dict): Data to write (can be string, list of strings, or dictionary).
- `file_path` (Union[str, Path]): Path where the file will be saved.
- `mode` (str, optional): Write mode (`w` for write, `a` for append). Defaults to 'w'.
- `exc_info` (bool, optional): If True, logs traceback on error. Defaults to True.

**Returns**:
- bool: True if the file was successfully saved, False otherwise.

**Raises**:
- Exception: Any exception during file operation.


### `read_text_file`

**Description**: Reads the contents of a file or directory of files. If reading a directory, allows specifying extensions for filtering which files to include.

**Parameters**:
- `file_path` (Union[str, Path]): Path to the file or directory.
- `as_list` (bool, optional): If True, returns content as list of lines. Defaults to False.
- `extensions` (Optional[list[str]], optional): List of file extensions to include if reading a directory. Defaults to None (reads all files).
- `exc_info` (bool, optional): If True, logs traceback on error. Defaults to True.

**Returns**:
- Union[str, list[str], None]: File content as a string or list of lines, or None if an error occurs or the file doesn't exist.

**Raises**:
- Exception: Any exception during file operation.


### `get_filenames`

**Description**: Retrieves filenames from a directory, optionally filtering by extension(s).

**Parameters**:
- `directory` (Union[str, Path]): Directory to search.
- `extensions` (Union[str, list[str]], optional): Extensions to filter. Defaults to "*".
- `exc_info` (bool, optional): If True, logs traceback on error. Defaults to True.

**Returns**:
- list[str]: List of filenames found.

**Raises**:
- Exception: Any exception during directory traversal.


### `recursively_yield_file_path`

**Description**: Recursively yields file paths matching given patterns within a directory.

**Parameters**:
- `root_dir` (Union[str, Path]): Root directory to search.
- `patterns` (Union[str, list[str]], optional): Patterns to filter files. Defaults to "*".
- `exc_info` (bool, optional): If True, logs traceback on error. Defaults to True.

**Yields**:
- Path: File paths matching the patterns.

**Raises**:
- Exception: Any exception during recursive search.


### `recursively_get_file_path`

**Description**: Recursively gets file paths matching given patterns within a directory.

**Parameters**:
- `root_dir` (Union[str, Path]): Root directory to search.
- `patterns` (Union[str, list[str]], optional): Patterns to filter files. Defaults to "*".
- `exc_info` (bool, optional): If True, logs traceback on error. Defaults to True.

**Returns**:
- list[Path]: List of file paths matching the patterns.

**Raises**:
- Exception: Any exception during recursive search.


### `recursively_read_text_files`

**Description**: Recursively reads text files from a directory, filtering by patterns.

**Parameters**:
- `root_dir` (str | Path): Root directory for the search.
- `patterns` (str | list[str]): Filename patterns to filter files (e.g., "*.txt", "*.md").
- `as_list` (bool, optional): If True, returns file content as a list of lines. Defaults to False.
- `exc_info` (bool, optional): If True, includes exception information in warnings. Defaults to True.

**Returns**:
- list[str]: List of file contents (or lines if `as_list=True`).

**Raises**:
- Exception: Any exception during file reading or processing.


### `get_directory_names`

**Description**: Retrieves all directory names within a given directory.

**Parameters**:
- `directory` (str | Path): Path to the directory.
- `exc_info` (bool, optional): If True, logs traceback information in case of an error. Defaults to True.

**Returns**:
- list[str]: List of directory names found.

**Raises**:
- Exception: Any exception during directory traversal.


### `read_files_content`

**Description**: Reads contents of files matching patterns recursively.

**Parameters**:
- `root_dir` (Union[str, Path]): Root directory to search.
- `patterns` (Union[str, list[str]]): File patterns to match.
- `as_list` (bool, optional): Return content as list of lines. Defaults to False.


**Returns**:
- list[str]: List of file contents.


**Raises**:
- Exception: Exception during file operation.


### `remove_bom`

**Description**: Removes BOM (Byte Order Mark) from a text file.

**Parameters**:
- `file_path` (Union[str, Path]): File to process.

**Raises**:
- Exception: Exception during file operation.


### `traverse_and_clean`

**Description**: Traverses a directory and removes BOM from Python files.

**Parameters**:
- `directory` (Union[str, Path]): Root directory to process.


### `main`

**Description**: Entry point for BOM removal in Python files.