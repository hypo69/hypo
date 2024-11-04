## \file src/utils/file.py
## \file src/utils/file.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
"""
Module for file operations.


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
        with file_path.open(mode, encoding="utf-8") as file:  # Ensure UTF-8 encoding
            if isinstance(data, list):
                for line in data:
                    file.write(f"{line}\n")
                    #logger.debug(f"{file_path=}", None, False)
            else:
                file.write(data)
        return True
    except Exception as ex:
        logger.error(f"Failed to save file {file_path}.", ex, exc_info=exc_info)
        return False


def read_text_file(
    file_path: str | Path, as_list: bool = False, extensions: list[str] = None, exc_info: bool = True
) -> list[str] | str | None:
    """
    Reads the content of a text file or, if a directory is provided, reads all files within it (with optional extensions).

    Args:
        file_path (str | Path): Path to the text file or directory.
        as_list (bool, optional): If True, returns the content as a list of lines. If False, returns the content as a single string. Defaults to False.
        extensions (list[str], optional): List of file extensions to include (e.g., ['.txt', '.md']). If None, reads all files. Defaults to None.
        exc_info (bool, optional): If True, logs traceback information in case of an error. Defaults to True.

    Returns:
        list[str] | str | None: If `as_list` is True, returns a list of lines. Otherwise, returns concatenated content as a string.
    """
    path = Path(file_path)

    if path.is_file():
        try:
            with path.open("r", encoding="utf-8") as f:
                return [line.strip() for line in f][0]
        except Exception as ex:
            if exc_info:
                logger.error(f"Failed to read file {file_path}.", exc_info=exc_info)
            return
    elif path.is_dir():
        try:
            content = []
            for file in path.iterdir():
                if file.is_file() and (not extensions or file.suffix in extensions):
                    with file.open("r", encoding="utf-8") as f:
                        if as_list:
                            content.extend(line.strip() for line in f)
                        else:
                            content.append(f.read())
            
            return content if as_list else "\n".join(content)
        except Exception as ex:
            if exc_info:
                logger.error(f"Failed to read files in directory {file_path}.", exc_info=exc_info)
            return
    else:
        logger.warning(f"File or directory '{file_path}' does not exist.")
        return



def get_filenames(
    directory: str | Path, extensions: str | List[str] = "*", exc_info: bool = True
) -> list[str]:
    """
    Retrieves all filenames from the specified directory, optionally filtered by file extensions.

    Args:
        directory (str | Path): Path to the directory from which filenames should be retrieved.
        extensions (str | List[str], optional): File extension(s) to filter the filenames. It can be a single extension (e.g., '*.txt') or a list of extensions (e.g., ['*.txt', '*.py']). If '*' is specified, all files are returned. Defaults to '*'..
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
        return [entry.name for entry in Path(directory).iterdir() if entry.is_dir()]
    except Exception as ex:
        if exc_info:
            logger.warning(
                f"Failed to get directory names from '{directory}'.",
                ex,
                exc_info=exc_info,
            )
        return 


def recursive_get_filenames(root_dir: str | Path, pattern: str) -> List[str]:
    """
    Recursively searches directories and gathers file paths matching the given pattern.

    Args:
        root_dir (str | Path): The root directory to start the search.
        pattern (str): The pattern to match files against (e.g., '*.txt').

    Returns:
        List[str]: A list of file paths matching the specified pattern.

    Example:
        >>> matched_files: list[str] = recursive_get_filenames(root_dir=".", pattern="*.py")
        >>> print(matched_files)
        ['script1.py', 'script2.py']

    More documentation: https://github.com/hypo69/tiny-utils/wiki/Files-and-Directories#recursive_get_filenames
    """
    matches = []
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in fnmatch.filter(filenames, pattern):
            matches.append(os.path.join(dirpath, filename))
    return matches

def recursively_get_filepath(
    root_dir: str | Path, 
    patterns: str | List[str] = '*', 
    exc_info: bool = True
) -> List[str] | None:
    """
    Recursively retrieves all file paths in the directory matching the specified pattern or patterns.

    Args:
        root_dir (str | Path): The root directory to start the recursive search.
        patterns (str | List[str], optional): A pattern or list of patterns to filter files. 
            Defaults to '*', which matches all files.
        exc_info (bool, optional): If True, logs traceback information in case of an error.

    Returns:
        List[str]: A list of file paths matching the specified pattern(s).

    Example:
        >>> files = recursively_get_filepath('.', ['*.txt', '*.md'])
        >>> print(files)
        ['./file1.txt', './file2.md']
    """
    try:
        if isinstance(patterns, str):
            patterns = [patterns]  # Convert single string pattern to list

        file_paths = []
        for pattern in patterns:
            file_paths.extend(Path(root_dir).rglob(pattern))

        return [str(file) for file in file_paths]
    except Exception as ex:
        if exc_info:
            logger.error(
                f"Failed to recursively get file paths from '{root_dir}'.", 
                ex, 
                exc_info=exc_info
            )
        return 


def recursive_read_text_files(
    root_dir: str | Path, 
    patterns: str | list[str], 
    as_list: bool = False, 
    exc_info: bool = True
) -> list[str]:
    """
    Recursively reads text files from the specified root directory that match the given patterns.

    Args:
        root_dir (str | Path): Path to the root directory for the search.
        patterns (str | list[str]): Filename pattern(s) to filter the files.
                                    Can be a single pattern (e.g., '*.txt') or a list of patterns.
        as_list (bool, optional): If True, returns the file content as a list of lines.
                                  Defaults to False.
        exc_info (bool, optional): If True, includes exception information in warnings. Defaults to True.

    Returns:
        list[str]: List of file contents (or lines if `as_list=True`) that match the specified patterns.

    Example:
        >>> contents = recursive_read_text_files("/path/to/root", ["*.txt", "*.md"], as_list=True)
        >>> for line in contents:
        ...     print(line)
        This will print each line from all matched text files in the specified directory.
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

                try:
                    with file_path.open("r", encoding="utf-8") as file:
                        if as_list:
                            # Read lines if `as_list=True`
                            matches.extend(file.readlines())
                        else:
                            # Read entire content otherwise
                            matches.append(file.read())
                except Exception as ex:
                    logger.warning(f"Failed to read file '{file_path}'.", exc_info=exc_info)

    return matches
