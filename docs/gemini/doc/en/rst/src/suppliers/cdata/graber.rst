hypotez/src/suppliers/cdata/graber.py
=======================================

.. module:: hypotez.src.suppliers.cdata.graber
   :platform: Windows, Unix
   :synopsis: This module contains the `Graber` class for grabbing product fields from the Morlevi supplier.


Module Contents
---------------

.. automodule:: hypotez.src.suppliers.cdata.graber
   :members:
   :undoc-members:
   :show-inheritance:


Classes
-------

.. autoclass:: Graber
   :members:
   :undoc-members:
   :show-inheritance:

   .. automethod:: __init__
      :noindex:
      :show-inheritance:

      .. rubric:: Args:

         driver (Driver): The driver instance to use for grabbing.


   .. automethod:: grab_page
      :noindex:
      :show-inheritance:

      .. rubric:: Args:

         driver (Driver): The driver instance to use for grabbing.

      .. rubric:: Returns:

         ProductFields: The grabbed product fields.