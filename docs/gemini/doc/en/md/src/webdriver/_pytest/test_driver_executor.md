# Module: hypotez/src/webdriver/_pytest/test_driver_executor.py

## Overview

This module contains pytest tests for the `ExecuteLocator` class, which interacts with a WebDriver instance.  It verifies various functionalities, including navigation, element interaction, and error handling.  Tests include navigating to a page, finding elements by locator, sending messages, getting attributes, triggering events, and handling invalid locators.


## Fixtures

### `driver`

**Description**: A pytest fixture that sets up a WebDriver instance (using Chrome) with headless mode enabled. It navigates to a starting URL ("http://example.com") and yields the driver object. After the test, the driver is quit.

**Parameters**:

* None

**Returns**:
* `webdriver`: The instantiated WebDriver object.

**Usage Example**:
```python
@pytest.fixture(scope="module")
def driver():
    # ... (driver setup code) ...
    yield driver
    driver.quit()
```

### `execute_locator`

**Description**: A pytest fixture that initializes an `ExecuteLocator` object using the provided `driver` fixture.

**Parameters**:

* `driver`: The WebDriver object.

**Returns**:
* `ExecuteLocator`: The initialized `ExecuteLocator` object.


## Functions

### `test_navigate_to_page`

**Description**: Tests that the WebDriver can successfully navigate to the specified starting page.

**Parameters**:

* `execute_locator`: An instance of `ExecuteLocator`.
* `driver`: The WebDriver instance.

**Returns**:
* None.

**Raises**:
* None


### `test_get_webelement_by_locator_single_element`

**Description**: Verifies that the `get_webelement_by_locator` method correctly returns a single web element using a valid XPATH locator.

**Parameters**:

* `execute_locator`: An instance of `ExecuteLocator`.
* `driver`: The WebDriver instance.

**Returns**:
* None.

**Raises**:
* None


### `test_get_webelement_by_locator_no_element`

**Description**: Tests the handling of a locator that does not match any element on the page. Asserts that `get_webelement_by_locator` returns `False` in this case.

**Parameters**:

* `execute_locator`: An instance of `ExecuteLocator`.
* `driver`: The WebDriver instance.

**Returns**:
* None.

**Raises**:
* None


### `test_send_message`

**Description**: Tests the `send_message` method for sending text to an input field.


**Parameters**:

* `execute_locator`: An instance of `ExecuteLocator`.
* `driver`: The WebDriver instance.

**Returns**:
* None

**Raises**:
* None


### `test_get_attribute_by_locator`

**Description**: Tests the `get_attribute_by_locator` method to retrieve a specific attribute from an element.


**Parameters**:

* `execute_locator`: An instance of `ExecuteLocator`.
* `driver`: The WebDriver instance.

**Returns**:
* None.

**Raises**:
* None


### `test_execute_locator_event`

**Description**: Tests the `execute_locator` method for triggering an event (like clicking) on an element.


**Parameters**:

* `execute_locator`: An instance of `ExecuteLocator`.
* `driver`: The WebDriver instance.

**Returns**:
* None.

**Raises**:
* None


### `test_get_locator_keys`

**Description**: Verifies that `ExecuteLocator.get_locator_keys()` returns a set of expected locator keys.


**Parameters**:

* `execute_locator`: An instance of `ExecuteLocator`.
* `driver`: The WebDriver instance.

**Returns**:
* None.

**Raises**:
* None


### `test_navigate_and_interact`

**Description**: Tests a navigation sequence involving interaction with elements on a different page.


**Parameters**:

* `execute_locator`: An instance of `ExecuteLocator`.
* `driver`: The WebDriver instance.

**Returns**:
* None.

**Raises**:
* None


### `test_invalid_locator`

**Description**: Tests the handling of an invalid locator, ensuring the expected `ExecuteLocatorException` is raised.


**Parameters**:

* `execute_locator`: An instance of `ExecuteLocator`.
* `driver`: The WebDriver instance.

**Returns**:
* None.

**Raises**:
* `ExecuteLocatorException`: If an invalid locator is used.