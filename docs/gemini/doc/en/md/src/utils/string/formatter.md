# hypotez/src/utils/string/formatter.py

## Overview

This module provides functions for formatting strings, handling HTML, and removing various characters. It includes utilities for cleaning, escaping, and transforming strings for use in different contexts.

## Table of Contents

* [StringFormatter](#stringformatter)
* [remove_line_breaks](#remove_line_breaks)
* [remove_htmls](#remove_htmls)
* [escape_html_tags](#escape_html_tags)
* [escape_to_html](#escape_to_html)
* [remove_non_latin_characters](#remove_non_latin_characters)
* [remove_special_characters](#remove_special_characters)
* [clear_numbers](#clear_numbers)
* [convert_to_list](#convert_to_list)
* [extract_value_from_parentheses_with_lead_dollar](#extract_value_from_parentheses_with_lead_dollar)
* [clean_url_from_protocols](#clean_url_from_protocols)


## Classes

### `StringFormatter`

**Description**: This class encapsulates various string formatting utilities.

**Methods**:

- [`remove_line_breaks`](#remove_line_breaks)
- [`remove_htmls`](#remove_htmls)
- [`escape_html_tags`](#escape_html_tags)
- [`escape_to_html`](#escape_to_html)
- [`remove_non_latin_characters`](#remove_non_latin_characters)
- [`remove_special_characters`](#remove_special_characters)
- [`clear_numbers`](#clear_numbers)



## Functions

### `remove_line_breaks`

**Description**: Removes newline characters (`\n` and `\r`) from the input string.

**Parameters**:

- `input_str` (str): The input string.

**Returns**:

- str: The string with line breaks removed.


### `remove_htmls`

**Description**: Removes HTML tags from the input string.

**Parameters**:

- `input_html` (str): The input HTML string.

**Returns**:

- str: The string with HTML tags removed.


### `escape_html_tags`

**Description**: Escapes `<` and `>` characters to `&lt;` and `&gt;` respectively in the input string.

**Parameters**:

- `input_html` (str): The input HTML string.

**Returns**:

- str: The escaped HTML string.


### `escape_to_html`

**Description**: Replaces characters with their HTML escape sequences.

**Parameters**:

- `text` (str): The input text.

**Returns**:

- str: The text with characters replaced by HTML escape sequences.


### `remove_non_latin_characters`

**Description**: Removes non-Latin characters from the input string.

**Parameters**:

- `input_str` (str): The input string.

**Returns**:

- str: The string with non-Latin characters removed.


### `remove_special_characters`

**Description**: Removes special characters from the input string or list of strings.

**Parameters**:

- `input_str` (str | list): The input string or list of strings.

**Returns**:

- str | list: The processed string or list with special characters removed.  Returns a list if input is a list.


### `clear_numbers`

**Description**: Extracts only decimal numbers and points from the input string.

**Parameters**:

- `input_str` (str): The input string.

**Returns**:

- str: The string containing only decimal numbers and points.

**Example**:

```python
input_str = 'aaa123.456 cde'
output_str = StringFormatter.clear_numbers(input_str)
print(output_str)  # Output: 123.456
```


### `convert_to_list`

(Missing Docstring - Add Docstring)

### `extract_value_from_parentheses_with_lead_dollar`

(Missing Docstring - Add Docstring)

### `clean_url_from_protocols`

(Missing Docstring - Add Docstring)