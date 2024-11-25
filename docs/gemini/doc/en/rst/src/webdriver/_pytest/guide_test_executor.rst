Guide for Testing `ExecuteLocator` Class
=====================================

This document provides a detailed guide for testers on how to test the `ExecuteLocator` class in the project.  It covers the essential steps, from setting up the environment to writing and running tests.

----

.. toctree::
   :maxdepth: 2

   test_executor

----

Testing the `ExecuteLocator` Class
---------------------------------

### Introduction

The `ExecuteLocator` class is designed to interact with web elements via Selenium WebDriver.  It includes methods to perform various actions on web page elements, such as retrieving attributes and sending messages.  This guide details how to set up the testing environment, write tests for the `ExecuteLocator` class, and execute those tests.


### 1. Environment Setup

#### 1.1 Installing Dependencies

Ensure all necessary libraries for the project and testing are installed. Execute the following command:

.. code-block:: bash

   pip install -r requirements.txt

The `requirements.txt` file should contain the following dependencies:

.. code-block:: text

   pytest==7.4.0
   selenium==4.16.1


#### 1.2 Setting up WebDriver

Ensure you have the appropriate WebDriver for the browser you intend to use for testing (e.g., ChromeDriver for Chrome).  See the official WebDriver documentation for instructions.


### 2. Writing Tests

#### 2.1 Test Structure

Create a test file named `test_executor.py` within the `tests` directory. This file will contain the tests for the `ExecuteLocator` class. Here's a sample test file structure:

.. code-block:: python
   :linenos:

   import pytest
   from unittest.mock import MagicMock, patch
   from selenium.webdriver.remote.webelement import WebElement
   from selenium.webdriver.common.by import By

   from src.webdriver.executor import ExecuteLocator
   from src.logger.exceptions import ExecuteLocatorException

   @pytest.fixture
   def driver_mock():
       return MagicMock()

   @pytest.fixture
   def execute_locator(driver_mock):
       return ExecuteLocator(driver_mock)

   # Example tests for ExecuteLocator methods
   def test_get_webelement_by_locator_single_element(execute_locator, driver_mock):
       pass  # Test implementation

   def test_get_webelement_by_locator_multiple_elements(execute_locator, driver_mock):
       pass  # Test implementation

   def test_get_webelement_by_locator_no_element(execute_locator, driver_mock):
       pass  # Test implementation

   def test_get_attribute_by_locator(execute_locator, driver_mock):
       pass  # Test implementation

   def test_send_message(execute_locator, driver_mock):
       pass  # Test implementation

   def test_send_message_typing_speed(execute_locator, driver_mock):
       pass  # Test implementation


#### 2.2 Implementing Tests

Implement the tests for `get_webelement_by_locator`, `get_attribute_by_locator`, and `send_message`, as demonstrated in the example.  Detailed test cases are included in the original input.


### 3. Running Tests

To execute the tests, run the following command from the project root:

.. code-block:: bash

   pytest tests/test_executor.py


### 4. Evaluating Test Results

After running the tests, `pytest` will display the results in the terminal. Ensure all tests pass successfully. If any test fails, `pytest` will indicate the error or failure; analyze the output and correct any issues in the tests or code.


### 5. Updating Tests

As the `ExecuteLocator` code changes, update the tests accordingly.  Maintain test validity to ensure they cover all new or modified functions.


### 6. Documentation

If you add or modify tests, update the relevant documentation to aid other developers and testers in understanding how `ExecuteLocator` functionality is being tested.

.. automodule:: src.webdriver.executor
    :members:
    :undoc-members:
    :show-inheritance:

----

Test Documentation
------------------

.. automodule:: tests.test_executor
    :members:
    :undoc-members:
    :show-inheritance:


### Example Test Documentation (Conceptual)

.. code-block:: rst

   Test Cases for `ExecuteLocator`
   ===============================

   .. toctree::
       :maxdepth: 1

       test_get_webelement_by_locator
       test_get_attribute_by_locator
       test_send_message


.. autofunction:: test_executor.test_get_webelement_by_locator_single_element
.. autofunction:: test_executor.test_get_webelement_by_locator_multiple_elements


Additional Resources
--------------------

- `pytest` documentation: [link to pytest docs](https://docs.pytest.org/en/latest/)
- Selenium WebDriver documentation: [link to Selenium docs](https://www.selenium.dev/documentation/webdriver/)
- Python Unit Testing Guide: [link to Python unittest docs](https://docs.python.org/3/library/unittest.html)

Follow this guide for effective testing of the `ExecuteLocator` class to ensure its functionality.  If you have further questions or need assistance, please consult your development or testing team lead.