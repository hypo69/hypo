## \file ../src/utils/file.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
"""
Module for file operations.

This module provides functions for performing various file operations, including:
- Saving text to a file.
- Reading text from a file.
- Retrieving filenames from a specified directory.
- Recursively retrieving filenames from directories based on a pattern.
- Retrieving directory names from a specified directory.

Functions:
    save_text_file(data: str | list | dict, file_path: str | Path, mode: str = 'w', exc_info: bool = True) -> bool:
        Saves the provided data to a file at the specified file path.
    
    read_text_file(file_path: str | Path, as_list: bool = False, exc_info: bool = True) -> list | None:
        Reads content from a file and returns it either as a list of lines or a single string.
    
    get_filenames(directory: str | Path, extensions: str | List[str] = '*', exc_info: bool = True) -> list[str]:
        Retrieves filenames from the specified directory, optionally filtered by file extension(s).

    get_directory_names(directory: str | Path, exc_info: bool = True) -> list[str]:
        Retrieves all directory names from the specified directory.
    
    recursive_get_filenames(root_dir: str | Path, pattern: str) -> List[str]:
        Recursively searches directories and gathers file paths matching the given pattern.

Examples:
    >>> success: bool = save_text_file(data="Hello World", file_path="/path/to/file.txt")
    >>> file_content: str = read_text_file(file_path="/path/to/file.txt")
    >>> filenames: list[str] = get_filenames(directory="/path/to/directory")
    >>> dir_names: list[str] = get_directory_names(directory="/path/to/directory")
    >>> matched_files: list[str] = recursive_get_filenames(root_dir="/path/to/root", pattern="*.txt")
"""

import os
import json
import fnmatch
from typing import List, Optional, Union
from pathlib import Path
from src.logger import logger


def save_text_file(
    data: str | list | dict,
    file_path: str | Path,
    mode: str = "w",
    exc_info: bool = True,
) -> bool:
    """
    Saves the provided data to a file at the specified file path.
    
    Args:
        data (str | list | dict): The data to be written to the file. It can be a string, list, or dictionary.
        file_path (str | Path): The full path to the file where the data should be saved.
        mode (str, optional): The file mode for writing, defaults to 'w'. Options include:
            - 'w': Write mode, which overwrites the file.
            - 'a': Append mode, which appends to the file.
        exc_info (bool, optional): If True, logs traceback information in case of an error. Defaults to True.
    
    Returns:
        bool: Returns True if the file is successfully saved, otherwise returns False.

    Example:
        >>> success: bool = save_text_file(data="Hello, World!", file_path="output.txt")
        >>> print(success)
        True

        >>> success: bool = save_text_file(data="This will fail", file_path="/invalid/path/output.txt")
        >>> print(success)
        False
    More documentation: https://github.com/hypo69/tiny-utils/wiki/Files-and-Directories#save_text_file
    """
    try:
        file_path = Path(file_path)
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with file_path.open(mode) as file:
            if isinstance(data, list):
                for line in data:
                    file.write(f"{line}\n")
                    logger.debug(f"{file_path=}", None, False)
            else:
                file.write(data)
        return True
    except Exception as ex:
        logger.error(f"Failed to save file {file_path}.", ex, exc_info=exc_info)
        return False


def read_text_file(
    file_path: str | Path, as_list: bool = False, exc_info: bool = True
) -> list | str | None:
    """
    Reads the content of a text file or, if a directory is provided, reads all .txt and .md files inside.

    Args:
        file_path (str | Path): Path to the text file or directory.
        as_list (bool, optional): If True, returns the content as a list of lines. If False, returns the content as a single string. Defaults to False.
        exc_info (bool, optional): If True, logs traceback information in case of an error. Defaults to True.

    Returns:
        list[str] | str | None: If `as_list` is True and it's a file, returns a list of lines. If it's a directory, returns the concatenated content of all .txt and .md files as a string.

    Example:
        >>> lines: list[str] = read_text_file(file_path="example.txt", as_list=True)
        >>> print(lines)
        ['Line 1', 'Line 2', 'Line 3']

        >>> content: str = read_text_file(file_path="example.txt")
        >>> print(content)
        'Line 1\nLine 2\nLine 3'

        >>> all_content: str = read_text_file(file_path="directory_path")
        >>> print(all_content)
        'Content of file1.txt\nContent of file2.md'
    """
    path = Path(file_path)

    if path.is_file():
        try:
            with path.open("r", encoding="utf-8") as file:
                if as_list:
                    return [line.strip() for line in file]
                else:
                    return file.read()
        except Exception as ex:
            if exc_info:
                logger.error(f"Failed to read file {file_path}.", ex, exc_info=exc_info)
            return None
    elif path.is_dir():
        try:
            content = []
            for file in path.glob("*.txt"):
                with file.open("r", encoding="utf-8") as f:
                    content.append(f.read())
            
            for file in path.glob("*.md"):
                with file.open("r", encoding="utf-8") as f:
                    content.append(f.read())
            
            return "\n".join(content)
        except Exception as ex:
            if exc_info:
                logger.error(f"Failed to read files in directory {file_path}.", ex, exc_info=exc_info)
            return None
    else:
        logger.warning(f"File or directory '{file_path}' does not exist.")
        return None


def get_filenames(
    directory: str | Path, extensions: str | List[str] = "*", exc_info: bool = True
) -> list[str]:
    """
    Retrieves all filenames from the specified directory, optionally filtered by file extensions.

    Args:
        directory (str | Path): Path to the directory from which filenames should be retrieved.
        extensions (str | List[str], optional): File extension(s) to filter the filenames. It can be a single extension (e.g., '*.txt') or a list of extensions (e.g., ['*.txt', '*.py']). If '*' is specified, all files are returned. Defaults to '*'.
        exc_info (bool, optional): If True, logs traceback information in case of an error. Defaults to True.

    Returns:
        list[str]: List of filenames found in the directory, optionally filtered by the provided extensions.

    Example:
        >>> files: list[str] = get_filenames(directory=".", extensions="*.py")
        >>> print(files)
        ['file1.py', 'file2.py']

    More documentation: https://github.com/hypo69/tiny-utils/wiki/Files-and-Directories#get_filenames
    """
    try:
        path = Path(directory)
        if isinstance(extensions, str):
            if extensions == "*":
                extensions = []  # If '*' is specified, no filtering by extension
            else:
                extensions = [extensions]  # Convert a single extension to a list

        # Normalize extensions to include a leading dot if necessary
        extensions = [ext if ext.startswith(".") else f".{ext}" for ext in extensions]

        filenames = []
        for file in path.iterdir():
            if file.is_file() and (not extensions or file.suffix in extensions):
                filenames.append(file.name)
        return filenames
    except Exception as ex:
        if exc_info:
            logger.warning(
                f"Failed to get filenames from directory '{directory}'.",
                ex,
                exc_info=exc_info,
            )
        return []


def get_directory_names(directory: str | Path, exc_info: bool = True) -> list[str]:
    """
    Retrieves all directory names from the specified directory.

    Args:
        directory (str | Path): Path to the directory from which directory names should be retrieved.
        exc_info (bool, optional): If True, logs traceback information in case of an error. Defaults to True.

    Returns:
        list[str]: List of directory names found in the specified directory.

    Example:
        >>> directories: list[str] = get_directory_names(directory=".")
        >>> print(directories)
        ['dir1', 'dir2']
    More documentation: https://github.com/hypo69/tiny-utils/wiki/Files-and-Directories#get_directory_names
    """
    try:
        path = Path(directory)
        directory_names = [dir.name for dir in path.iterdir() if dir.is_dir()]
        return directory_names
    except Exception as ex:
        if exc_info:
            logger.warning(f"Failed to get directory names from '{directory}'.", ex, exc_info=exc_info)
        return []

def recursive_get_filenames(root_dir: str | Path, pattern: str = "*") -> List[str]:
    """
    Recursively retrieves filenames from directories and subdirectories that match the provided pattern.

    Args:
        root_dir (str | Path): The root directory from which to start the recursive search.
        pattern (str, optional): The pattern to match filenames against (e.g., '*.txt'). Defaults to '*'.

    Returns:
        list[str]: List of filenames that match the provided pattern.

    Example:
        >>> files: list[str] = recursive_get_filenames(root_dir="/path/to/root", pattern="*.txt")
        >>> print(files)
        ['/path/to/root/file1.txt', '/path/to/root/subdir/file2.txt']
    """
    matches = []
    root_path = Path(root_dir)

    if not root_path.is_dir():
        logger.debug(f"The root directory '{root_path}' does not exist or is not a directory.")
        return []

    for root, dirs, files in os.walk(root_path):
        for filename in files:
            file_path = Path(root) / filename
            if fnmatch.fnmatch(filename, pattern):
                try:
                    with file_path.open("r", encoding="utf-8") as file:
                        matches.append(file.read())
                except Exception as ex:
                    logger.warning(f"Failed to read file {file_path}.", ex, exc_info=True)
    
    return matches

def recursively_get_filepath(
    root_dir: str | Path, 
    pattern: str = '*', 
    exc_info: bool = True
) -> List[str]:
    """
    Recursively retrieves all file paths in the directory matching the specified pattern.

    Args:
        root_dir (str | Path): The root directory from which to start the recursive search.
        pattern (str, optional): Pattern to filter files (e.g., '*.txt'). Defaults to '*', which matches all files.
        exc_info (bool, optional): If True, logs traceback information in case of an error. Defaults to True.

    Returns:
        list[str]: List of file paths that match the specified pattern.

    Example:
        >>> files: list[str] = recursively_get_filepath(root_dir=".", pattern="*.py")
        >>> print(files)
        ['./src/main.py', './tests/test_main.py']
    """
    try:
        root_dir = Path(root_dir)
        file_paths = []
        
        # Recursively go through directories and find files matching the pattern
        for path in root_dir.rglob(pattern):
            if path.is_file():
                file_paths.append(str(path))
        
        return file_paths
    except Exception as ex:
        if exc_info:
            logger.error(f"Failed to retrieve file paths in '{root_dir}'", ex, exc_info=exc_info)
        return []

def recursive_read_text_files(root_dir: str | Path, patterns: str | list[str]) -> list[str]:
    """
    Recursively reads text files from the specified root directory that match the given patterns.

    Args:
        root_dir (str | Path): Path to the root directory for the search.
        patterns (str | list[str]): Filename pattern(s) to filter the files. 
                                     Can be a single pattern (e.g., '*.txt') or a list of patterns.

    Returns:
        list[str]: List of file contents that match the specified patterns.

    Example:
        >>> contents = recursive_read_text_files("/path/to/root", ["*.txt", "*.md"])
        >>> for content in contents:
        ...     print(content)
        This will print the contents of all matched text files in the specified directory.
    """
    matches = []
    root_path = Path(root_dir)

    # Check if the root directory exists
    if not root_path.is_dir():
        logger.debug(f"The root directory '{root_path}' does not exist or is not a directory.")
        return []

    print(f"Searching in directory: {root_path}")

    # Normalize patterns to a list if it's a single string
    if isinstance(patterns, str):
        patterns = [patterns]

    for root, dirs, files in os.walk(root_path):
        for filename in files:
            # Check if the filename matches any of the specified patterns
            if any(fnmatch.fnmatch(filename, pattern) for pattern in patterns):
                file_path = Path(root) / filename
               
                # Read the file content and append to matches
                try:
                    with file_path.open("r", encoding="utf-8") as file:
                        matches.append(file.read())
                except Exception as ex:
                    logger.warning(f"Failed to read file '{file_path}'.", ex)

    return matches




