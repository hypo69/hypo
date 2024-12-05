# aliexpress.py

## Overview

This module provides the `Aliexpress` class, which integrates functionality from `Supplier`, `AliRequests`, and `AliApi` for working with AliExpress.  It handles various initialization options, including different webdriver choices and locale settings.

## Table of Contents

* [Aliexpress](#aliexpress)

## Classes

### `Aliexpress`

**Description**: The `Aliexpress` class is a base class for interacting with AliExpress. It combines the features of `Supplier`, `AliRequests`, and `AliApi`.

**Methods**:

#### `__init__`

**Description**: Initializes an instance of the `Aliexpress` class.

**Parameters**:

- `webdriver` (bool | str, optional): Webdriver mode. Defaults to `False`. Supported values are:
    - `False`: No webdriver.
    - `'chrome'`: Use the Chrome webdriver.
    - `'mozilla'`: Use the Mozilla webdriver.
    - `'edge'`: Use the Edge webdriver.
    - `'default'`: Use the system's default webdriver.
- `locale` (str | dict, optional): The language and currency settings for the script. Defaults to `{'EN': 'USD'}`.
- `*args`: Additional positional arguments.
- `**kwargs`: Additional keyword arguments.

**Returns**:
- None

**Raises**:
- `Exception`: In case of initialization issues.


```python
def __init__(self,
                 webdriver: bool | str = False,
                 locale: str | dict = {'EN': 'USD'},
                 *args, **kwargs):
    """
    Initialize the Aliexpress class.

    :param webdriver: Webdriver mode. Supported values are:
        - `False` (default): No webdriver.
        - `'chrome'`: Use the Chrome webdriver.
        - `'mozilla'`: Use the Mozilla webdriver.
        - `'edge'`: Use the Edge webdriver.
        - `'default'`: Use the system's default webdriver.
    :type webdriver: bool | str

    :param locale: The language and currency settings for the script.
    :type locale: str | dict

    :param args: Additional positional arguments.
    :param kwargs: Additional keyword arguments.

    **Examples**:

    .. code-block:: python

        # Run without a webdriver
        a = Aliexpress()

        # Webdriver `Chrome`
        a = Aliexpress('chrome')

    """
    super().__init__(supplier_prefix='aliexpress',
                     locale=locale,
                     webdriver=webdriver,
                     *args, **kwargs)