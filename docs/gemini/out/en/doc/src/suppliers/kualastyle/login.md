# src/suppliers/kualastyle/login.py

## Overview

This module contains functions for logging in to the Kualastyle supplier platform. It utilizes Selenium WebDriver for interacting with the web browser.


## Functions

### `login`

**Description**: This function handles the login process for a given supplier.

**Parameters**:

- `s` (Supplier): The supplier object containing necessary information.


**Returns**:

- `bool`: `True` if login is successful, `False` otherwise.


**Raises**:

- `Exception`: Any exception during the login process.


### `close_pop_up`

**Description**: This function closes any pop-ups that may appear during the login process.

**Parameters**:

- `s` (Supplier): The supplier object containing necessary information.


**Returns**:

- `bool`: `True` if the pop-up is closed successfully, `False` otherwise.


**Raises**:

- `Exception`: Any exception during the pop-up closing process.