Module src.suppliers
=====================

.. module:: src.suppliers
    :platform: Windows, Unix
    :synopsis: Supplier module. `Supplier` class

For each specific supplier, there are its own specific methods (functions) for extracting information.
These functions supplement the basic `Supplier` class and are connected through the `supplier.related_functions` interface.

Methods of each specific supplier are located in directories with the name `<supplier_prefix>`,
for example: `amazon`, `aliexpress`, `morlevi`, ...
- `<supplier_prefix>` is specified when a new supplier is created in the system and is usually based on the abbreviation of the supplier's name or website.

.. image:: supplier-warehouse-client.png
   :alt: Supplier-Warehouse-Client Relationship Diagram
   :align: center

## Relationship Between Supplier, Driver, and Product Entities

.. image:: supplier-warehouse-client.png
   :alt: Supplier-Warehouse-Client Relationship Diagram
   :align: center

Classes
-------

.. automodule:: hypotez.src.suppliers.supplier
    :members:
    :undoc-members:
    :show-inheritance:

.. automodule:: hypotez.src.suppliers.graber
    :members:
    :undoc-members:
    :show-inheritance:

.. autofunction:: hypotez.src.suppliers.close_pop_up
   :noindex:


Variables
---------

.. autodata:: hypotez.src.suppliers.MODE
   :noindex:

.. toctree::
   :maxdepth: 2

   supplier