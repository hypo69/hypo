```rst
Module suppliers
===============

.. module:: hypotez.src.suppliers
    :platform: Windows, Unix
    :synopsis: Module for suppliers.


Description
----------

This module defines the `Supplier` class and related functionalities for handling data extraction from various suppliers.  Specific extraction methods for each supplier are located in subdirectories (e.g., `amazon`, `aliexpress`). These methods extend the base `Supplier` class and are integrated via the `supplier.related_functions` interface.  The `supplier_prefix` used in directory names is based on the supplier's name or website.

.. image:: supplier-warehouse-client.png
   :alt: Supplier-Warehouse-Client Diagram
   :align: center


Classes
-------

.. autoclass:: hypotez.src.suppliers.Supplier
    :members:
    :undoc-members:
    :show-inheritance:

.. autoclass:: hypotez.src.suppliers.Graber
    :members:
    :undoc-members:
    :show-inheritance:


Functions
--------

(No functions defined in this file)

```
