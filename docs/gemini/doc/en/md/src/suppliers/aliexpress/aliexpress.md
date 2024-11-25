# Aliexpress Module Documentation

## Overview

This module provides the `Aliexpress` class, which integrates functionality from `Supplier`, `AliRequests`, and `AliApi` for working with AliExpress.  It facilitates interaction with the platform using various modes, including webdriver-based and request-based interactions.

## Table of Contents

* [Aliexpress Class](#aliexpress-class)


## Aliexpress Class

### `Aliexpress`

**Description**: Base class for AliExpress. This class combines features of the `Supplier`, `AliRequests`, and `AliApi` classes to facilitate interaction with AliExpress. It offers different interaction modes including those that rely on a webdriver or that directly use `requests`.

**Usage Examples**:

```python
# Run without a webdriver
a = Aliexpress()

# Webdriver `Chrome`
a = Aliexpress('chrome')

# Requests mode
a = Aliexpress(requests=True)
```

**Methods**:

### `__init__`

**Description**: Initializes the Aliexpress class.


**Parameters**:

- `webdriver` (bool | str, optional): Webdriver mode. Supported values are:
    - `False` (default): No webdriver.
    - `'chrome'`: Use the Chrome webdriver.
    - `'mozilla'`: Use the Mozilla webdriver.
    - `'edge'`: Use the Edge webdriver.
    - `'default'`: Use the system's default webdriver.

- `locale` (str | dict, optional): The language and currency settings for the script.  Defaults to `{'EN': 'USD'}`.

- `*args`: Additional positional arguments.

- `**kwargs`: Additional keyword arguments.


**Examples**:

```python
# Run without a webdriver
a = Aliexpress()

# Webdriver `Chrome`
a = Aliexpress('chrome')
```

**Raises**:

- `Exception`:  For any issues during initialization.



**Inherited Methods**:

The `Aliexpress` class inherits methods from `Supplier`, `AliRequests`, and `AliApi`.  These are not explicitly documented here, but their documentation is available in those respective modules.