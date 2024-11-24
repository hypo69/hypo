Supplier Module
==============

.. automodule:: hypotez.src.suppliers.supplier
    :members:
    :undoc-members:
    :show-inheritance:


Functions
--------

.. autofunction:: hypotez.src.suppliers.supplier.Supplier.__init__
.. autofunction:: hypotez.src.suppliers.supplier.Supplier._payload
.. autofunction:: hypotez.src.suppliers.supplier.Supplier.login
.. autofunction:: hypotez.src.suppliers.supplier.Supplier.run_scenario_files
.. autofunction:: hypotez.src.suppliers.supplier.Supplier.run_scenarios


Supplier Class
-------------

.. autoclass:: hypotez.src.suppliers.supplier.Supplier
    :members:
    :undoc-members:
    :show-inheritance:

How It Works
-----------

1. **Initialization**

   - The `__init__` method sets up the supplier prefix, locale, and WebDriver.
     Example:

     .. code-block:: python
        supplier = Supplier(supplier_prefix='aliexpress', locale='en', webdriver='chrome')

2. **Configuration Loading**

   - `_payload` loads the configuration and initializes locators and WebDriver.
     Example:

     .. code-block:: python
        supplier._payload(webdriver='firefox')

3. **Authentication**

   - `login` handles user login to the supplier's website.
     Example:

     .. code-block:: python
        supplier.login()

4. **Scenario Execution**

   - **Run scenario files:**

     .. code-block:: python
        supplier.run_scenario_files(['example_scenario.json'])

   - **Run specific scenarios:**

     .. code-block:: python
        supplier.run_scenarios([{'action': 'scrape', 'target': 'product_list'}])


Class Diagram
------------

.. image:: class_diagram.png
   :alt: Supplier Class Diagram
   :align: center