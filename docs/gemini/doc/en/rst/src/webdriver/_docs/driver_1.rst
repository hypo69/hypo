Driver Metaclass
=================

This module defines a metaclass `DriverMeta` for dynamically creating a `Driver` class that inherits from both a base `Driver` class and a specified Selenium WebDriver class (`Chrome`, `Firefox`, or `Edge`).  This metaclass enables flexible and dynamic instantiation of WebDriver objects with custom functionality.

.. automodule:: hypotez.src.webdriver._docs.driver_1
    :members:
    :undoc-members:
    :show-inheritance:

Metaclass Functionality
-----------------------

~ DriverMeta Metaclass
~~~~

This metaclass is responsible for creating a new `Driver` class dynamically, inheriting from both the base `Driver` class and the specified Selenium WebDriver class.

^ `__call__` Method
^^^

.. automethod:: hypotez.src.webdriver._docs.driver_1.DriverMeta.__call__
    :noindex:

    :param cls: The class being instantiated.
    :type cls: class
    :param webdriver_cls: The Selenium WebDriver class to inherit from.
    :type webdriver_cls: class
    :param \*args: Positional arguments to pass to the `Driver` class constructor.
    :param \*\*kwargs: Keyword arguments to pass to the `Driver` class constructor.
    :returns: The dynamically created `Driver` class instance.
    :rtype: class


^ Assertions
^^^

.. automethod:: hypotez.src.webdriver._docs.driver_1.DriverMeta.__call__
    :noindex:

    :raises TypeError: if `webdriver_cls` is not a class.
    :raises TypeError: if `webdriver_cls` is not a subclass of `Chrome`, `Firefox`, or `Edge`.

^ Dynamic Class Creation
^^^

The `__call__` method dynamically creates a new class named `Driver`. This class inherits from both the base `Driver` class and the specified WebDriver class.

^ Driver Class Constructor
^^^

.. automethod:: hypotez.src.webdriver._docs.driver_1.Driver.__init__
    :noindex:

    :param webdriver_cls: The Selenium WebDriver class.
    :type webdriver_cls: type
    :param \*args: Arguments for the `Driver` class.
    :param \*\*kwargs: Keyword arguments for the `Driver` class.
    :raises TypeError: if webdriver_cls is not a valid WebDriver class.


^ driver_payload Method
^^^

.. automethod:: hypotez.src.webdriver._docs.driver_1.Driver.driver_payload
    :noindex:

    :return:  Result of calling driver_payload method in the parent class.


Example Usage
-------------

The following example demonstrates how to use the `Driver` class with different WebDriver classes:

.. code-block:: python

    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
    from selenium.webdriver.firefox.webdriver import WebDriver as Firefox
    from selenium.webdriver.edge.webdriver import WebDriver as Edge

    # Import Driver class
    from hypotez.src.webdriver._docs.driver_1 import Driver
    from hypotez.src.webdriver._docs.driver_1 import DriverMeta

    # Example usage with Chrome
    chrome_driver = Driver(metaclass=DriverMeta, webdriver_cls=Chrome, options=None)

    # Example usage with Firefox
    firefox_driver = Driver(metaclass=DriverMeta, webdriver_cls=Firefox, options=None)

    # Example usage with Edge
    edge_driver = Driver(metaclass=DriverMeta, webdriver_cls=Edge, options=None)