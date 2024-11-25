hypotez/src/webdriver/_pytest/test_executor.py
==============================================

.. module:: hypotez.src.webdriver._pytest.test_executor
   :platform: Windows, Unix
   :synopsis: This module contains tests for the `ExecuteLocator` class.

Module Contents
---------------

The module defines fixtures and tests for the `ExecuteLocator` class, focusing on various scenarios related to interacting with web elements.  It includes tests for finding elements, retrieving attributes, and sending messages (simulating typing).

Fixtures
--------

.. autofunction:: driver_mock
.. autofunction:: execute_locator


Tests
-----

.. autofunction:: test_get_webelement_by_locator_single_element
.. autofunction:: test_get_webelement_by_locator_multiple_elements
.. autofunction:: test_get_webelement_by_locator_no_element
.. autofunction:: test_get_attribute_by_locator
.. autofunction:: test_send_message
.. autofunction:: test_send_message_typing_speed


Detailed Descriptions
--------------------

**`driver_mock` Fixture**

.. autofunction:: driver_mock
   :noindex:
   :show-inheritance:

**`execute_locator` Fixture**

.. autofunction:: execute_locator
   :noindex:
   :show-inheritance:

**`test_get_webelement_by_locator_single_element`**

.. autofunction:: test_get_webelement_by_locator_single_element
   :noindex:
   :show-inheritance:

   Tests successful retrieval of a single web element using a locator.

**`test_get_webelement_by_locator_multiple_elements`**

.. autofunction:: test_get_webelement_by_locator_multiple_elements
   :noindex:
   :show-inheritance:

   Tests retrieval of multiple web elements using a locator.

**`test_get_webelement_by_locator_no_element`**

.. autofunction:: test_get_webelement_by_locator_no_element
   :noindex:
   :show-inheritance:

   Tests the case where no element is found using a locator, returning `False`.

**`test_get_attribute_by_locator`**

.. autofunction:: test_get_attribute_by_locator
   :noindex:
   :show-inheritance:

   Tests the retrieval of an attribute from a web element using a locator.

**`test_send_message`**

.. autofunction:: test_send_message
   :noindex:
   :show-inheritance:

   Tests the sending of a message to a web element (e.g., typing).  It handles the case where `continue_on_error` is set to `True`.

**`test_send_message_typing_speed`**

.. autofunction:: test_send_message_typing_speed
   :noindex:
   :show-inheritance:

   Tests the sending of a message with a specified typing speed (delay between characters).