## \file ../src/utils/__init__.py
## \file ../src/utils/__init__.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
"""
# tiny_utils Module

The `tiny_utils` module is a collection of small, useful utilities designed to simplify common programming tasks. It includes tools for data conversion, file handling, and formatted output. This module helps streamline coding by providing straightforward and reusable functions.

## Overview

### Modules Included

#### `convertors` module
Functions for data conversion and handling.
- **`xml2dict`**: Convert XML data to dictionaries.
- **`base64_to_tmpfile`**: Convert base64 encoded data to a temporary file.
- **`csv2dict`**: Convert CSV data to dictionaries.
- **`csv2ns`**: Convert CSV data to SimpleNamespace objects.
- **`dict2csv`**: Convert dictionaries to CSV format.
- **`dict2html`**: Convert dictionaries to HTML format.
- **`dict2json`**: Convert dictionaries to JSON format.
- **`dict2ns`**: Convert dictionaries to SimpleNamespace objects.
- **`dict2xls`**: Convert dictionaries to XLS format.
- **`dict2xml`**: Convert dictionaries to XML format.
- **`html2dict`**: Convert HTML data to dictionaries.
- **`html2ns`**: Convert HTML data to SimpleNamespace objects.
- **`html2escape`**: Convert HTML characters to their escaped equivalents.
- **`escape2html`**: Convert escaped HTML characters back to normal.
- **`json2csv`**: Convert JSON data to CSV format.
- **`json2ns`**: Convert JSON data to SimpleNamespace objects.
- **`json2xls`**: Convert JSON data to XLS format.
- **`json2xml`**: Convert JSON data to XML format.
- **`ns2csv`**: Convert SimpleNamespace objects to CSV format.
- **`ns2dict`**: Convert SimpleNamespace objects to dictionaries.
- **`ns2json`**: Convert SimpleNamespace objects to JSON format.
- **`ns2xls`**: Convert SimpleNamespace objects to XLS format.
- **`ns2xml`**: Convert SimpleNamespace objects to XML format.
- **`text2png`**: Generate PNG images from text.

#### `printer` module
Functions for pretty-printing data structures.
- **`pprint`**: Pretty-print complex data structures for easier readability.

#### `jjson` module
Functions for working with JSON data.
- **`j_loads`**: Load JSON data from a string.
- **`j_loads_ns`**: Load JSON data from a string into SimpleNamespace objects.
- **`j_dumps`**: Dump data to a JSON string.

#### `file` module
Utilities for file operations.
- **`get_directory_names`**: Retrieve names of directories within a given path.
- **`get_filenames`**: Retrieve names of files within a given path.
- **`read_text_file`**: Read the contents of a text file.
- **`save_text_file`**: Save content to a text file.
- **`recursive_get_filenames`**: Recursively retrieve filenames within a directory.
- **`save_png`**: Save PNG images.
- **`save_png_from_url`**: Save a PNG image from a URL.
- **`save_video_from_url`**: Save a video file from a URL.

This `__init__.py` file provides an overview of the `tiny_utils` module and imports various utilities for file operations, data conversions, pretty printing, and more. The `tiny_utils` module is modular and well-organized, offering multiple functionalities under submodules, such as `convertors`, `file`, `printer`, `jjson`, `image`, and `video`.

Here is an explanation of the key elements:


1. **`convertors`**:
   - Provides data conversion tools, such as converting between XML, JSON, CSV, and other formats.
   - Includes methods for working with `SimpleNamespace` objects, which can offer more intuitive handling of data than plain dictionaries.
   
2. **`file`**:
   - Handles file operations, including saving and reading text files, retrieving filenames and directory names, and more.
   
3. **`printer`**:
   - Provides the `pprint` function for pretty-printing complex data structures.
   
4. **`jjson`**:
   - Offers utilities for working with JSON data, such as loading, dumping, and converting to `SimpleNamespace`.
   
5. **`image`**:
   - Functions to save PNG images, either from raw text or URLs.
   
6. **`video`**:
   - Handles saving video files from URLs.

### Usage
- The module offers a simplified approach to commonly repeated tasks in data conversion, file handling, and more. By importing specific functions, you can perform operations like saving a text file, converting XML to JSON, or pretty-printing data with minimal code.

This setup enhances modularity and readability, making the module highly reusable across different projects.
"""

from packaging.version import Version
from .version import __version__, __doc__, __details__

from .convertors import (xml2dict, 
                        base64_to_tmpfile,
                        base64encode,
                        csv2dict, 
                        csv2ns, 
                        dict2csv, 
                        dict2html, 
                        dict2ns, 
                        dict2xls, 
                        dict2xml, 
                        html2dict, 
                        html2ns, 
                        html2escape, 
                        html2text,
                        html2text_file,
                        escape2html, 
                        extract_json_from_md,
                        json2csv, 
                        json2ns, 
                        json2xls, 
                        json2xml, 
                        md2dict,
                        ns2csv, 
                        ns2dict, 
                        ns2json, 
                        ns2xls, 
                        ns2xml, 
                        text2png,
                        xls2dict,
                        webp2png,
                        ) 


from .printer import  pprint

from .jjson import (j_loads, 
                    j_loads_ns, 
                    j_dumps,
                    fix_json_string,
                    )

from .file import (get_directory_names, 
                    get_filenames, 
                    read_text_file, 
                    save_text_file, 
                    recursive_get_filenames,
                    )

from .image import (save_png, 
                    save_png_from_url
                    )

from .video import save_video_from_url

from .csv import (read_csv_file, 
                  read_csv_as_dict, 
                  read_csv_as_ns, 
                  save_csv_file,
                    )

