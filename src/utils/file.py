## \file hypotez/src/utils/file.py
# -*- coding: utf-8 -*-
""" Module for file operations. """

import os
import json
import fnmatch
from pathlib import Path
from typing import List, Optional, Union, Generator
from src.logger import logger


def save_text_file(
    data: str | list[str] | dict,
    file_path: Union[str, Path],
    mode: str = "w",
    exc_info: bool = True,
) -> bool:
    """
    Save data to a text file.

    Args:
        data (str | list[str] | dict): Data to write (can be string, list of strings, or dictionary).
        file_path (str | Path): Path where the file will be saved.
        mode (str, optional): Write mode (`w` for write, `a` for append). Defaults to 'w'.
        exc_info (bool, optional): If True, logs traceback on error. Defaults to True.

    Returns:
        bool: True if the file was successfully saved, False otherwise.
    """
    try:
        file_path = Path(file_path)
        file_path.parent.mkdir(parents=True, exist_ok=True)

        with file_path.open(mode, encoding="utf-8") as file:
            if isinstance(data, list):
                file.writelines(f"{line}\n" for line in data)
            elif isinstance(data, dict):
                json.dump(data, file, ensure_ascii=False, indent=4)
            else:
                file.write(data)
        return True
    except Exception as ex:
        logger.error(f"Failed to save file {file_path}.", ex, exc_info=exc_info)
        return False


def read_text_file(
    file_path: Union[str, Path],
    as_list: bool = False,
    extensions: Optional[list[str]] = None,
    exc_info: bool = True,
) -> Union[str, list[str], None]:
    """
    Read the contents of a file.

    Args:
        file_path (str | Path): Path to the file or directory.
        as_list (bool, optional): If True, returns content as list of lines. Defaults to False.
        extensions (list[str], optional): List of file extensions to include if reading a directory. Defaults to None.
        exc_info (bool, optional): If True, logs traceback on error. Defaults to True.

    Returns:
        str | list[str] | None: File content as a string or list of lines, or None if an error occurs.
    """
    try:
        path = Path(file_path)
        if path.is_file():
            with path.open("r", encoding="utf-8") as f:
                return f.readlines() if as_list else f.read()
        elif path.is_dir():
            files = [
                p for p in path.rglob("*") if p.is_file() and (not extensions or p.suffix in extensions)
            ]
            contents = [read_text_file(p, as_list) for p in files]
            return [item for sublist in contents if sublist for item in sublist] if as_list else "\n".join(filter(None, contents))
        else:
            logger.warning(f"Path '{file_path}' is invalid.")
            return None
    except Exception as ex:
        logger.error(f"Failed to read file {file_path}.", ex, exc_info=exc_info)
        return None


def get_filenames(
    directory: Union[str, Path], extensions: Union[str, list[str]] = "*", exc_info: bool = True
) -> list[str]:
    """
    Get filenames in a directory optionally filtered by extension.

    Args:
        directory (str | Path): Directory to search.
        extensions (str | list[str], optional): Extensions to filter. Defaults to '*'.

    Returns:
        list[str]: Filenames found in the directory.
    """
    try:
        path = Path(directory)
        if isinstance(extensions, str):
            extensions = [extensions] if extensions != "*" else []
        extensions = [ext if ext.startswith(".") else f".{ext}" for ext in extensions]

        return [
            file.name
            for file in path.iterdir()
            if file.is_file() and (not extensions or file.suffix in extensions)
        ]
    except Exception as ex:
        logger.warning(f"Failed to list filenames in '{directory}'.", ex, exc_info=exc_info)
        return []


def recursively_get_files(
    root_dir: Union[str, Path], patterns: Union[str, list[str]] = "*", exc_info: bool = True
) -> Generator[Path, None, None]:
    """
    Recursively yield file paths matching given patterns.

    Args:
        root_dir (str | Path): Root directory to search.
        patterns (str | list[str]): Patterns to filter files.

    Yields:
        Path: File paths matching the patterns.
    """
    try:
        patterns = [patterns] if isinstance(patterns, str) else patterns
        for pattern in patterns:
            yield from Path(root_dir).rglob(pattern)
    except Exception as ex:
        logger.error(f"Failed to search files in '{root_dir}'.", ex, exc_info=exc_info)


def read_files_content(
    root_dir: Union[str, Path],
    patterns: Union[str, list[str]],
    as_list: bool = False,
    exc_info: bool = True,
) -> list[str]:
    """
    Read contents of files matching patterns.

    Args:
        root_dir (str | Path): Root directory to search.
        patterns (str | list[str]): File patterns to match.
        as_list (bool, optional): Return content as list of lines. Defaults to False.

    Returns:
        list[str]: List of file contents.
    """
    content = []
    for file_path in recursively_get_files(root_dir, patterns, exc_info):
        file_content = read_text_file(file_path, as_list, exc_info=exc_info)
        if file_content:
            content.extend(file_content if as_list else [file_content])
    return content


def remove_bom(file_path: Union[str, Path]) -> None:
    """
    Remove BOM from a text file.

    Args:
        file_path (str | Path): File to process.
    """
    path = Path(file_path)
    try:
        with path.open("r+", encoding="utf-8") as file:
            content = file.read().replace("\ufeff", "")
            file.seek(0)
            file.write(content)
            file.truncate()
    except Exception as ex:
        logger.error(f"Failed to remove BOM from '{file_path}'.", ex)


def traverse_and_clean(directory: Union[str, Path]) -> None:
    """
    Traverse directory and remove BOM from Python files.

    Args:
        directory (str | Path): Root directory to process.
    """
    for file in recursively_get_files(directory, "*.py"):
        remove_bom(file)


def main() -> None:
    """Entry point for BOM removal in Python files."""
    root_dir = Path("..", "src")
    logger.info(f"Starting BOM removal in {root_dir}")
    traverse_and_clean(root_dir)


if __name__ == "__main__":
    main()
