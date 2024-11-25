# hypotez/src/endpoints/advertisement/facebook/scenarios/login.py

## Overview

This module contains the logic for logging into Facebook using a provided webdriver. It utilizes locators from a JSON file to interact with the Facebook login page.

## Functions

### `login`

**Description**: This function handles the Facebook login process. It takes a `Driver` object, inputs the credentials, and clicks the login button.  It returns `True` if the login is successful, `False` otherwise.


**Parameters**:

- `d` (Driver): The webdriver instance to interact with the Facebook login page.


**Returns**:

- `bool`: `True` if the login was successful, `False` otherwise.


**Raises**:

- `Exception`: If any error occurs during login (e.g., entering credentials, clicking the button).



## Variables

### `MODE`

**Description**: A string variable representing the mode, currently set to 'dev'.


### `locators`

**Description**: A dictionary loaded from `login.json` containing web element locators for Facebook login.  Loading from a file is error-handled, logging an error and returning `None` if the file is not valid or doesn't load.


## Modules Used

- `pathlib`
- `typing`
- `src.gs`
- `src.webdriver`
- `src.utils`
- `src.logger`