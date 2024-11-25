# Module: hypotez/src/utils/convertors

## Overview

This module provides a collection of functions and classes for converting data between various formats, such as CSV, JSON, XML, HTML, and more.  It facilitates the conversion of data for various purposes, from data analysis to presentation.


## Table of Contents

* [CSV Conversion](#csv-conversion)
* [Dictionary Conversion](#dictionary-conversion)
* [HTML Conversion](#html-conversion)
* [HTML to Text Conversion](#html-to-text-conversion)
* [JSON Conversion](#json-conversion)
* [Namespace Conversion](#namespace-conversion)
* [Markdown to Dictionary Conversion](#markdown-to-dictionary-conversion)
* [XLS Conversion](#xls-conversion)
* [XML Conversion](#xml-conversion)
* [Base64 Conversion](#base64-conversion)
* [PNG Image Conversion](#png-image-conversion)
* [Text-to-Speech Conversion](#text-to-speech-conversion)
* [DOT Graph Conversion](#dot-graph-conversion)


## CSV Conversion

### `csv2dict`

**Description**: Converts a CSV file to a dictionary.

**Parameters**:
- `file_path` (str): Path to the CSV file.


**Returns**:
- `dict | None`: Returns a dictionary representation of the CSV data or None if an error occurs.


### `csv2ns`

**Description**: Converts a CSV file to a namespace representation.


**Parameters**:
- `file_path` (str): Path to the CSV file.


**Returns**:
- `dict | None`: Returns a dictionary representing the namespace or None if an error occurs.


## Dictionary Conversion

### `dict2ns`

**Description**: Converts a dictionary to a namespace representation.

**Parameters**:
- `data` (dict): The dictionary to convert.


**Returns**:
- `dict | None`: Returns a namespace representation of the input dictionary or None if an error occurs.


### `dict2xls`

**Description**: Converts a dictionary to an XLS (Excel) file.


**Parameters**:
- `data` (dict): The dictionary to convert.
- `file_path` (str): Path to save the generated XLS file.



**Returns**:
- `bool`: True if the conversion was successful; False otherwise.


### `dict2xml`

**Description**: Converts a dictionary to an XML string.

**Parameters**:
- `data` (dict): The dictionary to convert.



**Returns**:
- `str | None`: Returns the XML string or None if an error occurs.



### `dict2csv`

**Description**: Converts a dictionary to a CSV file.



**Parameters**:
- `data` (dict): The dictionary to convert.
- `file_path` (str): Path to the CSV file to save.


**Returns**:
- `bool`: True if the conversion was successful; False otherwise.


### `dict2html`

**Description**: Converts a dictionary to HTML.


**Parameters**:
- `data` (dict): The dictionary to convert.


**Returns**:
- `str | None`: Returns the HTML string or None if an error occurs.



## HTML Conversion

### `html2escape`

**Description**: Escapes HTML special characters.

**Parameters**:
- `text` (str): The text to escape.


**Returns**:
- `str`: The escaped text.


### `html2ns`

**Description**: Converts HTML to a namespace representation.


**Parameters**:
- `html_string` (str): HTML string.


**Returns**:
- `dict | None`: Returns a namespace representation or None if an error occurs.



### `html2dict`

**Description**: Converts HTML to a dictionary.

**Parameters**:
- `html_string` (str): HTML string.



**Returns**:
- `dict | None`: Returns a dictionary representation of the HTML content, or None if an error occurs.


### `escape2html`

**Description**: Converts escaped HTML back to original form.

**Parameters**:
- `text` (str): The escaped text to convert.



**Returns**:
- `str`: The unescaped text.


## HTML to Text Conversion

(Docstrings for each function in this section are omitted for brevity, but the format would follow the same pattern.)

### `html2text`
### `html2text_file`
### `google_fixed_width_font`
### `google_has_height`
### `google_list_style`
### `google_nest_count`
### `google_text_emphasis`
### `dumb_css_parser`
### `dumb_property_dict`


## JSON Conversion

### `json2csv`
### `json2ns`
### `json2xls`
### `json2xml`


## Namespace Conversion

### `ns2csv`
### `ns2dict`
### `ns2json`
### `ns2xls`
### `ns2xml`


## Markdown to Dictionary Conversion

### `md2dict`

## XLS Conversion

### `xls2dict`

## XML Conversion

### `xml2dict`

## Base64 Conversion

### `base64_to_tmpfile`
### `base64encode`


## PNG Image Conversion

### `TextToImageGenerator`
### `webp2png`


## Text-to-Speech Conversion

### `speech_recognizer`
### `text2speech`


## DOT Graph Conversion

### `dot2png`