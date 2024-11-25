# hypotez/src/utils/convertors/xml2dict.py

## Overview

This module provides utilities for converting XML data into dictionaries.  It includes functions for parsing XML strings and converting XML element trees into dictionary representations.

## Table of Contents

- [Functions](#functions)
    - [_parse_node](#_parse_node)
    - [_make_dict](#_make_dict)
    - [xml2dict](#xml2dict)
    - [ET2dict](#ET2dict)

## Functions

### `_parse_node`

**Description**: Parses an XML node into a dictionary.

**Parameters**:

- `node` (ET.Element): The XML element to parse.

**Returns**:

- `dict | str`: A dictionary representation of the XML node, or a string if the node has no attributes or children.

**Raises**:
- None


### `_make_dict`

**Description**: Generates a dictionary with the tag name and value.

**Parameters**:

- `tag` (str): The tag name of the XML element.
- `value` (any): The value associated with the tag.

**Returns**:

- `dict`: A dictionary with the tag name as the key and the value as the dictionary value.


**Raises**:
- None


### `xml2dict`

**Description**: Parse XML string into a dictionary.

**Parameters**:

- `xml` (str): The XML string to parse.

**Returns**:

- `dict`: The dictionary representation of the XML.

**Raises**:
- None


### `ET2dict`

**Description**: Convert an XML element tree into a dictionary.

**Parameters**:

- `element_tree` (ET.Element): The XML element tree.

**Returns**:

- `dict`: The dictionary representation of the XML element tree.

**Raises**:
- None