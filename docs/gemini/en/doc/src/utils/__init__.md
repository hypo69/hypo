# src.utils

## Overview

This module contains a collection of utility functions for various data manipulation, file handling, and output formatting tasks.  It aims to streamline common programming tasks by providing reusable functions for data conversion, file operations, and more.

## Table of Contents

* [Classes](#classes)
* [Functions](#functions)
    * [`csv2dict`](#csv2dict)
    * [`json2xls`](#json2xls)
    * [`save_text_file`](#save_text_file)
    * ... (All functions)
* [Modules](#modules)
    * [.convertors](#convertors)
    * [.csv](#csv)
    * [.date_time](#date_time)
    * [.file](#file)
    * [.image](#image)
    * [.jjson](#jjson)
    * [.pdf](#pdf)
    * [.printer](#printer)
    * [.string](#string)
    * [.url](#url)
    * [.video](#video)
    * [.path](#path)


## Classes

(No classes are directly defined in the provided code, so this section is empty.)


## Functions

### `csv2dict`

**Description**: Converts a CSV file to a dictionary.

**Parameters**:
- `filepath` (str): The path to the CSV file.

**Returns**:
- `dict`: A dictionary representing the CSV data, or `None` if an error occurs.

**Raises**:
- `FileNotFoundError`: If the specified file does not exist.
- `ValueError`: If the input file is not a valid CSV format or if other conversion errors occur.


### `json2xls`

**Description**: Converts a JSON file to an XLSX file.

**Parameters**:
- `filepath` (str): The path to the JSON file.

**Returns**:
- `str | None`: The path to the generated XLSX file, or `None` if an error occurs.


**Raises**:
- `FileNotFoundError`: If the specified file does not exist.
- `ValueError`: If the input file is not a valid JSON format or if other conversion errors occur.
- `TypeError`: If input is not a string representing the filepath.


### `save_text_file`

**Description**: Saves text to a file.

**Parameters**:
- `filepath` (str): The path to the file where the text will be saved.
- `text` (str): The text content to be saved.

**Returns**:
- `bool`: `True` if the file was saved successfully, `False` otherwise.

**Raises**:
- `TypeError`: If the input `filepath` or `text` is not of the expected type.
- `IOError`: If there is an error during file writing.



### `csv2ns`

**Description**: Converts a CSV file to a Namespace.

**Parameters**:

- `filepath` (str): The path to the CSV file.

**Returns**:

- `object | None`: A Namespace object representing the CSV data or None in case of error.


**Raises**:

- `FileNotFoundError`: If the specified file does not exist.
- `ValueError`: If the input file is not a valid CSV format or if other conversion errors occur.


**(Similar documentation should be generated for all other functions, classes, and modules in the `src.utils` package.)**