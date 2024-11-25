Execute Locator Module
=======================

.. automodule:: hypotez.src.webdriver.executor
    :members:
    :undoc-members:
    :show-inheritance:

Functions
---------

.. autofunction:: hypotez.src.webdriver.executor.ExecuteLocator.__init__
.. autofunction:: hypotez.src.webdriver.executor.ExecuteLocator.execute_locator
.. autofunction:: hypotez.src.webdriver.executor.ExecuteLocator.get_webelement_by_locator
.. autofunction:: hypotez.src.webdriver.executor.ExecuteLocator.get_attribute_by_locator
.. autofunction:: hypotez.src.webdriver.executor.ExecuteLocator._get_element_attribute
.. autofunction:: hypotez.src.webdriver.executor.ExecuteLocator.send_message
.. autofunction:: hypotez.src.webdriver.executor.ExecuteLocator.evaluate_locator
.. autofunction:: hypotez.src.webdriver.executor.ExecuteLocator._evaluate
.. autofunction:: hypotez.src.webdriver.executor.ExecuteLocator.get_locator_keys


Class Documentation
-------------------

.. autoclass:: hypotez.src.webdriver.executor.ExecuteLocator
    :members:
    :special-members: __init__
    :show-inheritance:


Example Usage
-------------

This section provides examples of how to use the `ExecuteLocator` class.  (These examples are placeholders, as specific usage depends on the context of the test cases.)


Locator Examples
---------------

The module provides example locator structures. These examples are crucial for demonstrating how the script finds and interacts with elements. For example:


.. code-block:: json

    {
      "product_links": {
        "attribute": "href",
        "by": "xpath",
        "selector": "//div[contains(@id,\'node-galery\')]//li[contains(@class,\'item\')]//a",
        "selector 2": "//span[@data-component-type=\'s-product-image\']//a",
        "if_list":"first","use_mouse": false,
        "mandatory": true,
        "event": null
      },
      ...
    }


.. note::
  These examples demonstrate the structure of the locator dictionaries used by the `execute_locator` method.  Their interpretation depends on the logic inside the `execute_locator` implementation.