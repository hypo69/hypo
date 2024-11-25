# hypotez/src/endpoints/advertisement/facebook/scenarios/switch_account.py

## Overview

This module contains the `switch_account` function for switching between Facebook accounts. It utilizes the `Driver` class to interact with the Facebook website.  It also loads locators from a JSON file.

## Table of Contents

* [Overview](#overview)
* [Functions](#functions)
    * [switch_account](#switch_account)


## Functions

### `switch_account`

**Description**: This function attempts to switch to another Facebook account if a "Switch Account" button is present.

**Parameters**:
- `driver` (Driver): An instance of the `Driver` class, responsible for interacting with the web driver.


**Returns**:
-  None.


**Raises**:
- No exceptions are explicitly raised.  Implicit exceptions from `driver.execute_locator` will be propagated.


```python
def switch_account(driver: Driver):
    """ Если есть кнопка `Переключить` - нажимаю её  """
    driver.execute_locator(locator.switch_to_account_button)