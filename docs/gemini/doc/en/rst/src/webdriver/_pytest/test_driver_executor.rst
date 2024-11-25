hypotez/src/webdriver/_pytest/test_driver_executor.py
=====================================================

.. module:: hypotez.src.webdriver._pytest.test_driver_executor
    :platform: Windows, Unix
    :synopsis: This module contains tests for the driver executor.


.. automodule:: hypotez.src.webdriver._pytest.test_driver_executor
    :members:
    :undoc-members:
    :show-inheritance:


Functions
--------

.. autofunction:: test_navigate_to_page
.. autofunction:: test_get_webelement_by_locator_single_element
.. autofunction:: test_get_webelement_by_locator_no_element
.. autofunction:: test_send_message
.. autofunction:: test_get_attribute_by_locator
.. autofunction:: test_execute_locator_event
.. autofunction:: test_get_locator_keys
.. autofunction:: test_navigate_and_interact
.. autofunction:: test_invalid_locator


Fixtures
--------

.. autofunction:: driver
.. autofunction:: execute_locator


.. rubric:: Notes

The tests utilize the `selenium` library to interact with a WebDriver instance.  They include tests for basic navigation, element retrieval, attribute fetching, message sending, and event execution, demonstrating correct usage of `ExecuteLocator` and handling potential exceptions.  The `driver` fixture provides a setup and teardown mechanism to ensure a clean WebDriver environment for each test. The `execute_locator` fixture initializes the `ExecuteLocator` instance using the driver. The tests cover valid and invalid locator scenarios and include assertions to verify expected behavior.