# Module aliexpress

## Overview

The `aliexpress` module provides the `Aliexpress` class, which integrates functionality from `Supplier`, `AliRequests`, and `AliApi` classes to work with AliExpress. It's designed for tasks related to parsing and interacting with the AliExpress API.

## Table of Contents

- [Module aliexpress](#module-aliexpress)
- [Class Aliexpress](#class-aliexpress)
    - [Method `__init__`](#method-init)


## Class Aliexpress

### `Aliexpress`

**Description**: The base class for working with AliExpress. It combines the capabilities of the `Supplier`, `AliRequests`, and `AliApi` classes for easy interaction with AliExpress.

**Usage Examples**:

```python
# Running without a webdriver
a = Aliexpress()

# Chrome webdriver
a = Aliexpress('chrome')

# Using Requests mode
a = Aliexpress(requests=True)
```


### Method `__init__`

**Description**: Initializes the `Aliexpress` class.

**Parameters**:

- `webdriver` (bool | str, optional): Webdriver usage mode. Valid values:
    - `False` (default): No webdriver.
    - `'chrome'`: Using Chrome webdriver.
    - `'mozilla'`: Using Mozilla webdriver.
    - `'edge'`: Using Edge webdriver.
    - `'default'`: Using the default system webdriver.
- `locale` (str | dict, optional): Language and currency settings. Defaults to `{'EN': 'USD'}`.
- `*args`: Additional positional arguments.
- `**kwargs`: Additional keyword arguments.

**Examples**:

```python
# Running without a webdriver
a = Aliexpress()

# Chrome webdriver
a = Aliexpress('chrome')
```

**Returns**:
- None

**Raises**:
- `Exception`: Any exception related to webdriver initialization or other errors during interaction with AliExpress.