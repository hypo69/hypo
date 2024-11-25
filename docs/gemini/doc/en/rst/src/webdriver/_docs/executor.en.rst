WebDriver Executor
==================

.. automodule:: hypotez.src.webdriver.executor
    :members:
    :undoc-members:
    :show-inheritance:


Locator Handling
---------------

~ Execute Locator
^^^^^^^^^^^^^^^^

The `execute_locator` method is the central function for interacting with web elements based on provided locator dictionaries. It handles various actions and data retrieval operations.

^ Locator Structure
^^^^^^^^^^^^^^^^^

The `locator` parameter is expected to be a dictionary containing the necessary information to locate and interact with web elements.  This data structure enables the `ExecuteLocator` to dynamically execute a variety of actions.

^ Error Handling
^^^^^^^^^^^^^^^^

The `execute_locator` method includes extensive error handling using `try...except` blocks, ensuring robustness against potential Selenium exceptions.

~ Locator Examples
^^^^^^^^^^^^^^^^^^

The module provides examples demonstrating the usage of locator dictionaries for diverse web element interactions.


~ Element Retrieval
^^^^^^^^^^^^^^^^^^^^

^ `get_webelement_by_locator`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The `get_webelement_by_locator` method is used to locate web elements based on the provided `locator`.  It waits for the element to become available before returning.


^ `get_attribute_by_locator`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The `get_attribute_by_locator` method retrieves specified attributes from the identified web elements.

^ `_get_element_attribute`
^^^^^^^^^^^^^^^^^^^^^^^^^^^

This helper method retrieves a specific attribute from a given web element.


~ Message Sending
^^^^^^^^^^^^^^^^^^

^ `send_message`
^^^^^^^^^^^^^^^^^

The `send_message` method facilitates sending messages to web elements with support for typing speed configuration and error handling.


~ Locator Evaluation
^^^^^^^^^^^^^^^^^^^^

^ `evaluate_locator`
^^^^^^^^^^^^^^^^^^^^^

This method evaluates locator attributes, including handling of placeholders and complex expressions.

^ `_evaluate`
^^^^^^^^^^^^^^

This helper method evaluates a single locator attribute.

~ Additional Functionality
^^^^^^^^^^^^^^^^^^^^^^^^^

^ Locator Keys
^^^^^^^^^^^^^^

The `get_locator_keys` method provides a list of available locator keys.

^ Error Handling
^^^^^^^^^^^^^^^^

The module utilizes extensive `try...except` blocks to catch various exceptions (e.g., `NoSuchElementException`, `TimeoutException`) and log errors appropriately.


Usage
-----

~ Initialization
^^^^^^^^^^^^^^^^

Create an instance of `ExecuteLocator` with a WebDriver instance.

~ Execute Locator
^^^^^^^^^^^^^^^^^

Call the `execute_locator` method with a locator dictionary to perform actions or retrieve data from web elements.


Dependencies
-----------

The module relies on the Selenium WebDriver library for interacting with web browsers.  Importantly, it incorporates internal modules for settings, logging, and specific exception handling, enabling the `ExecuteLocator` to function in conjunction with a comprehensive automation framework.


Example Usage
------------

The provided example demonstrates how to initialize the `ExecuteLocator`, use the `execute_locator` method, and handle the resulting data.

```python
# Example usage (replace with your actual code)
from selenium import webdriver
from hypotez.src.webdriver import ExecuteLocator
from hypotez.src.logger import logger
...  # Import other necessary modules
```
```
```
```
```
```
```
```

```
```

```
```
```
```
```
```
```
```

```
```
```
```
```

```
```
```
```
```
```

```
```

```
```