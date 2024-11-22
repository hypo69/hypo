```rst
Wallmart Graber Module
=======================

This module contains the logic for grabbing product data from Walmart.

.. automodule:: hypotez.src.suppliers.wallmart.graber
    :members:
    :undoc-members:
    :show-inheritance:


Functions
---------

.. autofunction:: hypotez.src.suppliers.wallmart.graber.close_popup
   :noindex:

   This decorator closes pop-ups before executing the wrapped function.

.. autofunction:: hypotez.src.suppliers.wallmart.graber.Graber.grab_page
   :noindex:

   Grabs product fields from the Walmart page.

   :param driver: The webdriver instance to use.
   :type driver: src.webdriver.Driver
   :raises ExecuteLocatorException: if there is an error during locator execution.
   :returns: ProductFields: A dataclass containing the grabbed product data.
   :rtype: ProductFields


Classes
-------

.. autoclass:: hypotez.src.suppliers.wallmart.graber.Graber
   :members:
   :undoc-members:
   :show-inheritance:

   This class handles grabbing product data from Walmart.  It inherits from `src.suppliers.Graber`.


Module Details
-------------

MODE:
^^^^^^^
The variable `MODE` is set to 'development' in this module.

Variables:
^^^^^^^^^
The variables `d` and `l` are defined to store instances of Driver and Locator, respectively.

Data Structures
--------------
The module uses dataclasses and pydantic models to define data structures like `ProductFields`, providing typed data.


```
