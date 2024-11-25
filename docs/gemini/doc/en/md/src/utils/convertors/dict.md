# Module: hypotez/src/utils/convertors/dict.py

## Overview

This module provides functions for converting between dictionaries and SimpleNamespace objects, as well as exporting data to various formats like XML, CSV, JSON, XLS, HTML, and PDF.  It includes recursive conversion capabilities and handles various data types, including lists and nested dictionaries.


## Table of Contents

* [Functions](#functions)
    * [`dict2ns`](#dict2ns)
    * [`dict2xml`](#dict2xml)
    * [`dict2csv`](#dict2csv)
    * [`dict2json`](#dict2json)
    * [`dict2xls`](#dict2xls)
    * [`dict2html`](#dict2html)
    * [`dict2pdf`](#dict2pdf)


## Functions

### `dict2ns`

**Description**: Recursively converts dictionaries to `SimpleNamespace` objects.  It handles nested dictionaries and lists within the input data, preserving the structure.

**Parameters**:

- `data` (Dict[str, Any] | List[Any]): The input dictionary or list of dictionaries/items to convert.

**Returns**:

- `Any`: The converted data.  Returns a `SimpleNamespace` object for dictionaries and a list of converted `SimpleNamespace` objects for lists of dictionaries.

### `dict2xml`

**Description**: Generates an XML string representation of the input dictionary.

**Parameters**:

- `data` (Dict[str, Any]): The dictionary to convert to XML.
- `encoding` (str, optional): The character encoding for the XML output. Defaults to 'UTF-8'.

**Returns**:

- `str`: The XML string representation of the input dictionary.

**Raises**:

- `Exception`: If more than one root node is provided in the input dictionary.

### `dict2csv`

**Description**: Saves the input dictionary or `SimpleNamespace` to a CSV file.

**Parameters**:

- `data` (dict | SimpleNamespace): The data to save to a CSV file.
- `file_path` (str | Path): Path to the output CSV file.

**Returns**:

- `bool`: `True` if the file was saved successfully, `False` otherwise.


### `dict2xls`

**Description**: Saves the input dictionary or `SimpleNamespace` to an XLS (Excel) file.

**Parameters**:

- `data` (dict | SimpleNamespace): The data to save to an XLS file.
- `file_path` (str | Path): Path to the output XLS file.

**Returns**:

- `bool`: `True` if the file was saved successfully, `False` otherwise. (Assumes `save_xls_file` function is defined elsewhere.)


### `dict2html`

**Description**: Generates an HTML table string from the input dictionary or `SimpleNamespace`.  Handles nested dictionaries and lists to create a structured HTML table representation.

**Parameters**:

- `data` (dict | SimpleNamespace): The dictionary or `SimpleNamespace` to convert to HTML.
- `encoding` (str, optional): Data encoding. Defaults to 'UTF-8'.

**Returns**:

- `str`: The HTML string containing the table representation of the input data.


### `dict2pdf`

**Description**: Saves the input dictionary data to a PDF file.  Creates a simple PDF file containing the key-value pairs from the dictionary.

**Parameters**:

- `data` (dict | SimpleNamespace): The dictionary data to convert to PDF.
- `file_path` (str | Path): Path to the output PDF file.

**Returns**:

- `None`


**Note**:  The example PDF generation will create a new page if the content exceeds the space on the current page.  The function assumes the existence of `reportlab.pdfgen` and `reportlab.lib.pagesizes` for PDF generation.  You'll need to install these libraries.  Further, the `save_csv_file` and `save_xls_file` functions are assumed to exist elsewhere in the project, likely in a separate file (`src.utils.xls`) and responsible for the underlying CSV/XLS saving mechanism.