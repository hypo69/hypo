# hypotez/src/suppliers/cdata/login.py

## Overview

This module defines the `login` function for the C-data supplier, handling the web driver login process. It utilizes locators for interacting with the login page elements.

## Functions

### `login`

**Description**: This function implements the login procedure for the C-data website using a web driver. It takes no parameters, finds login fields, enters credentials, and clicks the login button. It returns `True` upon successful login and logs an informational message.


**Parameters**:
- `self`:  Instance of the class containing the web driver and locator data.


**Returns**:
- `True`: Indicates successful login.


**Raises**:
- `Exception`:  Any exceptions encountered during the process (e.g., element not found, incorrect locator).