# src.suppliers.aliexpress.utils.locales

## Overview

This module provides functions for loading and processing locales data from a JSON file.  It specifically deals with loading locale information (e.g., language codes and corresponding currency codes) and using this data within the broader application context.


## Functions

### `load_locales_data`

**Description**: Loads locales data from a JSON file, returning a list of dictionaries containing locale and currency pairs.


**Parameters**:

- `path` (Path): The path to the JSON file containing the locale data.


**Returns**:

- `list[dict[str, str]]`: A list of dictionaries. Each dictionary maps a locale (e.g., 'EN', 'RU') to a currency (e.g., 'USD', 'EUR'). Returns `None` if the file does not exist or is not properly formatted.


**Examples**:

```python
>>> from src.suppliers.aliexpress.utils.locales import load_locales_data
>>> locales = load_locales_data(Path('/path/to/locales.json'))
>>> print(locales)
[{'EN': 'USD'}, {'HE': 'ILS'}, {'RU': 'ILS'}, {'EN': 'EUR'}, {'EN': 'GBR'}, {'RU': 'EUR'}]
```



### `get_locales`

**Description**: This function fetches locale data from a specified JSON file.


**Parameters**:

- `locales_path` (Path | str): The path to the JSON file containing locale data.


**Returns**:

- `list[dict[str, str]] | None`: A list of dictionaries mapping locales to currencies, or `None` if the file is not found or the format is invalid.


**Examples**:

```python
>>> from src.suppliers.aliexpress.utils.locales import get_locales
>>> locales = get_locales(Path('/path/to/locales.json'))
>>> print(locales)
[{'EN': 'USD'}, {'HE': 'ILS'}, {'RU': 'ILS'}, {'EN': 'EUR'}, {'EN': 'GBR'}, {'RU': 'EUR'}]
```



## Variables

### `locales`

**Description**: Contains the loaded locales data.  This variable is assigned the result of calling `get_locales` with a specific path to a locales.json file.


**Type**:

`list[dict[str, str]] | None`


**Value**:

The value is populated from the `locales.json` file.  This is usually the result of loading locale information for specific campaigns.

```