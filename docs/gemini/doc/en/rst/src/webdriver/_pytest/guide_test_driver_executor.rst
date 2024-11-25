Test Driver Executor Guide
==========================

.. automodule:: hypotez.src.webdriver._pytest.test_driver_executor
   :members:
   :undoc-members:
   :show-inheritance:

Introduction
-----------

This guide provides instructions for testers on how to run and execute tests from the `test_driver_executor.py` file, along with descriptions of the tests and their purposes.

Test Structure
-------------

The `test_driver_executor.py` file contains tests for two classes: `Driver` and `ExecuteLocator`. These tests verify the correctness of class methods, interactions between them, and use cases in various situations.

~ Testable Methods and Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- `test_navigate_to_page`: Verifies that WebDriver correctly loads the specified page.
- `test_get_webelement_by_locator_single_element`: Verifies that the `get_webelement_by_locator` method correctly returns an element by its locator.
- `test_get_webelement_by_locator_no_element`: Verifies that the `get_webelement_by_locator` method returns `False` if an element is not found.
- `test_send_message`: Verifies that the `send_message` method correctly sends a message to an element.
- `test_get_attribute_by_locator`: Verifies that the `get_attribute_by_locator` method correctly returns an element's attribute.
- `test_execute_locator_event`: Verifies that the `execute_locator` method correctly executes an event on the locator.
- `test_get_locator_keys`: Verifies that the `get_locator_keys` method returns the correct locator keys.
- `test_navigate_and_interact`: Verifies the sequence of navigation and interaction with elements on another page.
- `test_invalid_locator`: Verifies handling of invalid locators and the corresponding exception.

Running the Tests
----------------

^ Installation of Dependencies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before running the tests, ensure that all necessary dependencies are installed.  Execute the following command:

.. code-block:: bash

   pip install -r requirements.txt


The `requirements.txt` file should list required libraries such as `pytest` and `selenium`.

^ Setting up WebDriver
~~~~~~~~~~~~~~~~~~~~~~

The tests use Chrome WebDriver. Ensure that you have [ChromeDriver](https://sites.google.com/chromium.org/driver/) installed and specify the path to `chromedriver` in the code:

.. code-block:: python

   from selenium import webdriver
   from selenium.webdriver.chrome.service import Service
   service = Service(executable_path="/path/to/chromedriver")  # Replace with the actual path
   options = webdriver.ChromeOptions()
   driver = webdriver.Chrome(service=service, options=options)

^ Running the Tests
~~~~~~~~~~~~~~~~~~~

Use the following command to run the tests:

.. code-block:: bash

   pytest src/webdriver/_pytest/test_driver_executor.py


This command will execute all tests defined in the `test_driver_executor.py` file.

Test Descriptions
----------------

^ 1. `test_navigate_to_page`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Purpose**: Verify that WebDriver correctly loads the specified page.
- **Expected Result**: The current page URL should be `"http://example.com"`.


^ 2. `test_get_webelement_by_locator_single_element`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Purpose**: Verify that the `get_webelement_by_locator` method returns an element by its locator.
- **Expected Result**: The element should be an instance of `WebElement` and contain the text `"Example Domain"`.


^ 3. `test_get_webelement_by_locator_no_element`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Purpose**: Verify that the `get_webelement_by_locator` method returns `False` if an element is not found.
- **Expected Result**: The returned value should be `False`.


^ (Remaining test descriptions follow a similar format, describing purpose and expected result for each test.)

Reporting Test Results
----------------------

After running the tests, `pytest` will generate a report with the results. You can view it in the console or use command-line flags to create detailed reports:

- **Detailed Text Report**:

.. code-block:: bash

   pytest src/webdriver/_pytest/test_driver_executor.py -v


- **HTML Report**:

    Install `pytest-html` and generate a report:

.. code-block:: bash

   pip install pytest-html
   pytest src/webdriver/_pytest/test_driver_executor.py --html=report.html

    The report will be saved in `report.html`.

Checklist
---------

Before running the tests, ensure that:

- [ ] All dependencies from `requirements.txt` are installed.
- [ ] The correct path to `chromedriver` is specified in `test_driver_executor.py`.
- [ ] The `headless` mode is configured in the `Options` (if necessary).
- [ ] Tests are run using the `pytest` command.

Conclusion
----------

Following this guide, you can run and verify tests for the `Driver` and `ExecuteLocator` classes. If you have questions or encounter problems, refer to the developers or check the documentation for more information.