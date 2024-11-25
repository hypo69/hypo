# src.utils

## Overview

This module, `src.utils`, provides a collection of small, reusable utility functions for various tasks, including data conversion, file handling, and formatted output.  It streamlines common programming tasks by offering tools for working with CSV, JSON, HTML, image, and other data formats, as well as file system navigation and manipulation.

## Table of Contents

* [Classes](#classes)
* [Functions](#functions)
    * [convertors](#convertors)
    * [csv](#csv)
    * [date_time](#date_time)
    * [file](#file)
    * [image](#image)
    * [jjson](#jjson)
    * [pdf](#pdf)
    * [printer](#printer)
    * [string](#string)
    * [video](#video)
    * [url](#url)
    * [path](#path)


## Classes

### `TimeoutCheck`

**Description**: A class for checking timeouts. (Implementation details would be needed for more specific documentation).


### `PDFUtils`

**Description**: A class for PDF manipulation. (Implementation details would be needed for more specific documentation).


### `TextToImageGenerator`

**Description**: A class for generating images from text. (Implementation details would be needed for more specific documentation).

### `StringFormatter`

**Description**: A class for formatting strings. (Implementation details would be needed for more specific documentation).

### `StringNormalizer`

**Description**: A class for normalizing strings. (Implementation details would be needed for more specific documentation).

### `ProductFieldsValidator`

**Description**: A class for validating product fields. (Implementation details would be needed for more specific documentation).



## Functions

### `convertors`

This section contains functions for converting between various data formats.

#### `base64_to_tmpfile`

**Description**: Converts base64 encoded data to a temporary file.

**Parameters**:

* `base64_data` (str): The base64 encoded data.

**Returns**:

* `str`: The path to the temporary file.


#### `base64encode`

**Description**: Encodes data to base64 format.

**Parameters**:

* `data` (str): The data to encode.

**Returns**:

* `str`: The base64 encoded data.


#### `csv2dict`, `csv2ns`, `dict2csv`, `dict2html`, `dict2ns`, `dict2xls`, `dict2xml`, `json2csv`, `json2ns`, `json2xls`, `json2xml`, `md2dict`, `ns2csv`, `ns2dict`, `ns2json`, `ns2xls`, `ns2xml`, `html2dict`, `html2escape`, `html2ns`, `html2text`, `html2text_file`, `escape2html`, `dot2png`, `webp2png`, `xls2dict`

_(Details for each function would need to be populated from the implementation)_

#### `speech_recognizer`


#### `text2speech`

#### `get_directory_names`


#### `get_filenames`


#### `read_text_file`, `save_text_file`, `recursively_get_file_path`, `recursively_read_text_files`, `recursively_yield_file_path`, `remove_bom`

_(Details for each function would need to be populated from the implementation)_

#### `save_png_from_url`, `save_png`


#### `j_dumps`, `j_loads`, `j_loads_ns`, `replace_key_in_json`


#### `read_csv_as_dict`, `read_csv_as_ns`, `read_csv_file`, `save_csv_file`


#### `pprint`


#### `extract_url_params`, `is_url`, `get_relative_path`


#### `TimeoutCheck`


#### `ProductFieldsValidator`, `StringFormatter`, `StringNormalizer`



#### `save_video_from_url`


### `csv`


### `date_time`


### `file`


### `image`


### `jjson`


### `pdf`


### `printer`


### `string`


### `video`


### `url`


### `path`