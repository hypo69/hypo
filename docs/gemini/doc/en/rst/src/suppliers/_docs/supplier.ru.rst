Supplier Class
============

This module defines the `Supplier` class, which serves as a base class for interacting with data suppliers (e.g., Amazon, AliExpress, Walmart) in your application.  It provides a common interface for data retrieval and manipulation.


.. automodule:: hypotez.src.suppliers._docs.supplier
    :members:
    :undoc-members:
    :show-inheritance:


Class Details
-------------

~ Supplier
~~~~

The `Supplier` class is a foundational component for handling data retrieval from various data sources.


.. autoclass:: hypotez.src.suppliers._docs.supplier.Supplier
    :members:
    :undoc-members:
    :show-inheritance:

    :special-members: __init__


Methods
-------

^ __init__
^^^

Initializes the `Supplier` object.

.. automethod:: hypotez.src.suppliers._docs.supplier.Supplier.__init__


^ _payload
^^^

Loads supplier settings, configuration files, and initializes the webdriver.

.. automethod:: hypotez.src.suppliers._docs.supplier.Supplier._payload


^ login
^^^

Performs the login process to the supplier's website (if required).

.. automethod:: hypotez.src.suppliers._docs.supplier.Supplier.login


^ run_scenario_files
^^^

Executes scenarios defined in files.

.. automethod:: hypotez.src.suppliers._docs.supplier.Supplier.run_scenario_files


^ run_scenarios
^^^

Executes specified scenarios.

.. automethod:: hypotez.src.suppliers._docs.supplier.Supplier.run_scenarios


Attributes
----------

~ supplier_id
~~~~

Unique identifier for the supplier.

~ supplier_prefix
~~~~

Prefix for the supplier (e.g., `aliexpress`, `amazon`).

~ supplier_settings
~~~~

Supplier settings loaded from a configuration file.

~ locale
~~~~

Localization code (e.g., `en` for English, `ru` for Russian).

~ price_rule
~~~~

Rule for calculating prices (e.g., adding VAT or discounts).

~ related_modules
~~~~

Module containing supplier-specific functions.

~ scenario_files
~~~~

List of scenario files to be executed.

~ current_scenario
~~~~

Current scenario being executed.

~ login_data
~~~~

Login data for the supplier's website (if needed).

~ locators
~~~~

Locators for web elements on the supplier's website pages.

~ driver
~~~~

Webdriver for interacting with the supplier's website.

~ parsing_method
~~~~

Data parsing method (e.g., `webdriver`, `api`, `xls`, `csv`).


Usage Example
------------

This example demonstrates how to use the `Supplier` class:

.. code-block:: python

    # Create a Supplier object for 'aliexpress'
    supplier = Supplier(supplier_prefix='aliexpress', locale='en', webdriver='chrome')

    # Perform login
    supplier.login()

    # Run scenarios from files
    supplier.run_scenario_files(['example_scenario.json'])

    # Or run specific scenarios
    supplier.run_scenarios([{'action': 'scrape', 'target': 'product_list'}])


Class Design Overview
--------------------

The `Supplier` class provides a common structure for different data suppliers.  Specific supplier implementations can inherit from this class and override methods to handle their unique requirements, like website-specific login procedures, product data extraction, or different API calls.