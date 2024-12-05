# hypotez/src/endpoints/advertisement/facebook/scenarios/switch_account.py

## Overview

This module contains the `switch_account` function for switching between Facebook accounts. It utilizes the `Driver` class to interact with the Facebook webpage and locate the "Switch Account" button.

## Table of Contents

* [Overview](#overview)
* [Functions](#functions)
    * [`switch_account`](#switch_account)

## Functions

### `switch_account`

**Description**: This function attempts to switch to a different Facebook account if a "Switch Account" button is present.

**Parameters**:

* `driver` (Driver): An instance of the `Driver` class, responsible for interacting with the browser and the Facebook page.

**Returns**:

*  None.  The function does not explicitly return any value.


**Raises**:

* No exceptions are explicitly raised.  The `Driver` class methods might raise exceptions if the locator is invalid or if the web page element is not found.  These exceptions would need to be handled in a calling function.

```python
def switch_account(driver: Driver):
    """ Если есть кнопка `Переключить` - нажимаю её  """
    driver.execute_locator(locator.switch_to_account_button)
```