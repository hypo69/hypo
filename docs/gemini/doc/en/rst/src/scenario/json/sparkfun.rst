SparkFun Scenario Configuration
=============================

This file configures a scenario for collecting product data from SparkFun's website.

.. automodule:: hypotez.src.scenario.json.sparkfun
    :members:
    :undoc-members:
    :show-inheritance:

Configuration Parameters
------------------------

~ Supplier
^^^

* `supplier`: Specifies the supplier name. (sparkfun)
* `supplier_prefix`: Prefix used for the supplier. (sparkfun)

~ Data Collection
^^^

* `start_url`: Starting URL for the product collection. (https://www.sparkfun.com/categories)
* `price_rule`: Rule for handling prices. (+0)
* `if_login`: Indicates if login is required. (False)
* `collect_products_from_categorypage`: Indicates if products are collected from category pages. (False)
* `parcing method [webdriver|api]`: Specifies if using webdriver or API for data extraction. (web)
* `about method web scrapping [webdriver|api]`: A description of web scraping method used. (If using API, no webdriver needed)
* `root_category`: The starting category ID (3)


~ Scenarios
^^^

* `scenarios`: An empty dictionary, potentially used for additional scenarios.


Example Usage
------------

.. code-block:: python

    import json

    # Load the configuration from the JSON file.
    with open('hypotez/src/scenario/json/sparkfun.json') as f:
        config = json.load(f)
        
    # Access configuration values.
    supplier = config['supplier']
    start_url = config['start_url']

    # ... (More example code for using the configuration data)