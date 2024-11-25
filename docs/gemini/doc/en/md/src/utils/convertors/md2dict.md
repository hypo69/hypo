# md2dict Module Documentation

## Overview

This module provides a function for converting Markdown strings into structured dictionaries.  It extracts JSON content if present and handles Markdown sections.


## Table of Contents

* [md2dict](#md2dict)
* [extract_json_from_string](#extract-json-from-string)


## Functions

### `md2dict`

**Description**: Converts a Markdown string into a structured dictionary, extracting JSON content if present.

**Parameters**:

* `md_string` (str): The Markdown string to convert.

**Returns**:

* `Dict[str, dict | list]`: A structured representation of the Markdown content. Returns a dictionary with a "json" key if JSON content is found, otherwise a dictionary containing sections parsed from the Markdown.


**Raises**:

* `Exception`: Any exception during Markdown parsing or JSON extraction is logged and returns an empty dictionary.


### `extract_json_from_string`

**Description**: Extracts JSON content from a string, if any.

**Parameters**:

* `text` (str): The string to extract JSON from.

**Returns**:

* `dict | None`: The extracted JSON content as a Python dictionary, or `None` if no JSON is found.

**Raises**:

* `Exception`: Any exception during JSON extraction is logged and returns `None`.