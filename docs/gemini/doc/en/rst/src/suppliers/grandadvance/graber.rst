grandadvance Graber Module
==========================

.. module:: hypotez.src.suppliers.grandadvance.graber
    :platform: Windows, Unix
    :synopsis: Module for grabbing Morlevi product fields.

Module Description
------------------

This module contains the `Graber` class for grabbing product fields from Grandadvance.  It uses asynchronous operations and interacts with a web driver to fetch data. The module leverages data structures like `ProductFields` and utilizes the `gs`, `Context`, and other modules.


Classes
-------

.. autoclass:: Graber
    :members:
    :undoc-members:
    :show-inheritance:

Functions
---------

.. autofunction:: close_pop_up
    :noindex:


Methods
-------

.. automethod:: Graber.grab_page
.. automethod:: Graber.local_saved_image