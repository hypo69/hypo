# hypotez/src/utils/url.py

## Overview

This module provides functions for working with URLs, including extracting query parameters and validating URL strings.


## Functions

### `extract_url_params`

**Description**: Extracts parameters from a URL string.

**Parameters**:
- `url` (str): The URL string to parse.

**Returns**:
- `dict | None`: A dictionary of query parameters and their values, or `None` if the URL does not contain parameters.

**Raises**:
- `ValueError`: If the input `url` is not a valid URL string.


### `is_url`

**Description**: Checks if the given text is a valid URL using the `validators` library.

**Parameters**:
- `text` (str): The string to validate.

**Returns**:
- `bool`: `True` if the string is a valid URL, otherwise `False`.


## Usage Example

```python
# Example usage (included in the file)
url = input("Введите URL: ")
if is_url(url):
    params = extract_url_params(url)
    if params:
        print("Параметры URL:")
        for key, value in params.items():
            print(f"{key}: {value}")
    else:
        print("URL не содержит параметров.")
else:
    print("Введенная строка не является валидным URL.")
```

## Module Details

This module leverages the `urllib.parse` module for URL parsing and the `validators` library for URL validation.  It converts parameters from lists to strings if they contain a single value.


## Contributing

If you'd like to contribute to this module, please ensure your code adheres to the existing style and functionality.  Feel free to add more robust error handling or additional validation checks if necessary.


## Dependencies

This module requires the `validators` library.  Install it using:

```bash
pip install validators
```