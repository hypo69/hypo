# hypotez/src/utils/convertors/ns.py

## Overview

This module provides functions for converting `SimpleNamespace` objects to various formats, including dictionaries, JSON, CSV, XML, and XLS. It utilizes external libraries for file handling and formatting.


## Table of Contents

* [ns2dict](#ns2dict)
* [ns2json](#ns2json)
* [ns2csv](#ns2csv)
* [ns2xml](#ns2xml)
* [ns2xls](#ns2xls)


## Functions

### `ns2dict`

**Description**: Converts a `SimpleNamespace` object to a dictionary.

**Parameters**:

* `ns_obj` (SimpleNamespace): The `SimpleNamespace` object to convert.

**Returns**:

* `dict`: The converted dictionary representation of the `SimpleNamespace` object.


### `ns2json`

**Description**: Converts a `SimpleNamespace` object to JSON format.  Can optionally save the JSON to a file.

**Parameters**:

* `ns_obj` (SimpleNamespace): The `SimpleNamespace` object to convert.
* `json_file_path` (str | Path, optional): Path to save the JSON file.  If not provided, the function returns the JSON string. Defaults to `None`.


**Returns**:

* `str | bool`: If `json_file_path` is not provided, returns a JSON string. If `json_file_path` is provided, returns `True` if the file was written successfully, otherwise raises an exception and logs an error.


**Raises**:

* `Exception`: If an error occurs during the JSON conversion or file writing process. Error message and exception details are logged.



### `ns2csv`

**Description**: Converts a `SimpleNamespace` object to CSV format and saves it to a file.

**Parameters**:

* `ns_obj` (SimpleNamespace): The `SimpleNamespace` object to convert.
* `csv_file_path` (str | Path): Path to save the CSV file.

**Returns**:

* `bool`: `True` if the CSV file was written successfully, `False` otherwise.


**Raises**:

* `Exception`: If an error occurs during the CSV conversion or file writing process. Error message and exception details are logged.


### `ns2xml`

**Description**: Converts a `SimpleNamespace` object to XML format.

**Parameters**:

* `ns_obj` (SimpleNamespace): The `SimpleNamespace` object to convert.
* `root_tag` (str, optional): The root element tag for the XML. Defaults to `"root"`.

**Returns**:

* `str`: The resulting XML string.


**Raises**:

* `Exception`: If an error occurs during the XML conversion process. Error message and exception details are logged.


### `ns2xls`

**Description**: Converts a `SimpleNamespace` object to XLS format and saves it to a file.

**Parameters**:

* `ns_obj` (SimpleNamespace): The `SimpleNamespace` object to convert.
* `xls_file_path` (str | Path): Path to save the XLS file.

**Returns**:

* `bool`: `True` if the XLS file was written successfully, `False` otherwise.


**Raises**:

* `Exception`: If an error occurs during the XLS conversion or file writing process. Error message and exception details are logged.