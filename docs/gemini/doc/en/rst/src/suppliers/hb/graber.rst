Module graber
============

.. module:: hypotez.src.suppliers.hb.graber
    :platform: Windows, Unix
    :synopsis: This module contains the Graber class for grabbing Morlevi product fields.


Class Graber
------------

.. autoclass:: hypotez.src.suppliers.hb.graber.Graber
    :members:
    :undoc-members:
    :show-inheritance:

    .. automethod:: __init__
        :noindex:

        :param driver: The driver instance to use.
        :type driver: Driver

        :returns: None
        :rtype: None



    .. automethod:: grab_page
        :noindex:


        :param driver: The driver instance to use for grabbing.
        :type driver: Driver

        :returns: The grabbed product fields.
        :rtype: ProductFields

        :raises ExecuteLocatorException: If an error occurs during locator execution.

        
Functions
---------

# Global settings
# ----------------


# Close pop-up decorator
# ---------------------

# Note: The close_pop_up decorator is not implemented.
# The comments in the original code refer to an incomplete implementation.

# Note: This section is likely to be expanded once the decorator is completed.
#
# .. autofunction:: hypotez.src.suppliers.hb.graber.close_pop_up
#     :noindex:
#
#     :param value: Optional additional value for the decorator.
#     :type value: Any
#
#     :returns: Callable: The decorator for wrapping a function.
#     :rtype: Callable
#