```rst
test_executor.py
=================

This file contains tests for the `ExecuteLocator` class, focusing on interacting with web elements.

.. automodule:: hypotez.src.webdriver._pytest.test_executor
    :members:
    :undoc-members:
    :show-inheritance:

Fixtures
--------

.. autofunction:: hypotez.src.webdriver._pytest.test_executor.driver_mock
.. autofunction:: hypotez.src.webdriver._pytest.test_executor.execute_locator

Test Cases
----------

^ test_get_webelement_by_locator_single_element
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tests retrieving a single web element using a locator.

.. autofunction:: hypotez.src.webdriver._pytest.test_executor.test_get_webelement_by_locator_single_element

^ test_get_webelement_by_locator_multiple_elements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tests retrieving multiple web elements using a locator.

.. autofunction:: hypotez.src.webdriver._pytest.test_executor.test_get_webelement_by_locator_multiple_elements


^ test_get_webelement_by_locator_no_element
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tests the case where no element is found using a locator.

.. autofunction:: hypotez.src.webdriver._pytest.test_executor.test_get_webelement_by_locator_no_element

^ test_get_attribute_by_locator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tests retrieving an attribute of a web element using a locator.

.. autofunction:: hypotez.src.webdriver._pytest.test_executor.test_get_attribute_by_locator

^ test_send_message
~~~~~~~~~~~~~~~~~~~~

Tests sending a message to a web element using a locator.

.. autofunction:: hypotez.src.webdriver._pytest.test_executor.test_send_message


^ test_send_message_typing_speed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tests sending a message to a web element with a specified typing speed.

.. autofunction:: hypotez.src.webdriver._pytest.test_executor.test_send_message_typing_speed
```
