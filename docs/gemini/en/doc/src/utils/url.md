# Module: hypotez/src/utils/string/url.py

## Overview

This module provides functions for working with URLs, including extracting query parameters and validating URL strings.  It leverages the `urllib.parse` and `validators` libraries.

## Table of Contents

- [extract_url_params](#extract-url-params)
- [is_url](#is-url)


## Functions

### `extract_url_params`

**Description**: Extracts query parameters from a URL string.

**Parameters**:

- `url` (str): The URL string to parse.

**Returns**:

- `dict | None`: A dictionary containing the query parameters and their values, or `None` if the URL does not contain any parameters.


**Example Usage**:

```python
url = "https://example.com/page?param1=value1&param2=value2&param3="
params = extract_url_params(url)
print(params)  # Output: {'param1': 'value1', 'param2': 'value2', 'param3': ''}
```

### `is_url`

**Description**: Checks if a given string is a valid URL using the `validators` library.

**Parameters**:

- `text` (str): The string to validate.

**Returns**:

- `bool`: `True` if the string is a valid URL, `False` otherwise.

**Example Usage**:

```python
url = "https://www.example.com"
is_valid = is_url(url)
print(is_valid)  # Output: True
```


```python
invalid_url = "invalid-url"
is_valid = is_url(invalid_url)
print(is_valid)  # Output: False
```


## Usage Example

```python
# Example usage of the module.
url = input("Enter a URL: ")
if is_url(url):
  params = extract_url_params(url)
  if params:
    print("URL Parameters:")
    for key, value in params.items():
      print(f"{key}: {value}")
  else:
    print("URL has no parameters.")
else:
  print("Invalid URL.")
```
```
```
```python

```
```python

```
```python