```rst
Amazon Graber Module
====================

.. automodule:: hypotez.src.suppliers.amazon.graber
    :members:
    :undoc-members:
    :show-inheritance:

Functions
---------

.. autofunction:: hypotez.src.suppliers.amazon.graber.close_popup
   :noindex:

   .. note::
       Creates a decorator to close pop-ups before executing the main function logic.

.. autofunction:: hypotez.src.suppliers.amazon.graber.Graber.__init__
    :noindex:

.. autofunction:: hypotez.src.suppliers.amazon.graber.Graber.grab_page
    :noindex:

    .. note::
        Asynchronous function to grab product fields.

        :param driver: The driver instance to use for grabbing.
        :type driver: Driver
        :returns: The grabbed product fields.
        :rtype: ProductFields

        **Important:**  This function contains a significant amount of commented-out code.
        The commented sections represent functionality that is not currently being used.
        Uncomment the desired parts to enable the relevant data fetching tasks.


.. autoclass:: hypotez.src.suppliers.amazon.graber.Graber
    :members:
    :undoc-members:
    :show-inheritance:
```
