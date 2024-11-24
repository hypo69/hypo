ebay Scenario Configuration
==========================

This file defines the configuration for the eBay data scraping scenario.  It specifies the supplier, URL, price rules, and other important parameters.

.. code-block:: json
   :linenos:

   ```json
   {
     "supplier": "ebay",
     "supplier_prefix": "ebay",
     "start_url": "https://www.ebay.com/",
     "price_rule": "1",
     "supplier_id": "2792",
     "num_items_4_flush": 300,
     "if_login": false,
     "parcing method [webdriver|api]": "web",
     "about method web scrapping [webdriver|api]": "Если я работаю через API мне не нужен webdriver",
     "collect_products_from_categorypage": false,
     "scenario_files": [
       "ebay_categories_phones_apple.json",
       "ebay_stores_mmhfcom.json",
       "ebay_stores_pacificindustriesltd.json",
       "ebay_stores_thegasketsman75.json",
       "ebay_stores_himaio12.json"
     ],
     "excluded": [
     ],
     "last_runned_scenario": ""
   }
   ```

Configuration Details
--------------------

~ Supplier:  `ebay`
~ Supplier Prefix: `ebay`
~ Start URL: `https://www.ebay.com/`
~ Price Rule: `1`
~ Supplier ID: `2792`
~ Number of Items to Flush: `300`
~ Login Required: `False`
~ Parsing Method: `web` (using webdriver)
~ Web Scraping Method Details:  If using an API, a webdriver is not needed.
~ Collect Products from Category Page: `False`
~ Scenario Files: A list of JSON files containing configurations for specific scenarios (e.g., categories, stores).
~ Excluded Items: An empty list, indicating no items are excluded.
~ Last Runned Scenario:  Empty string, indicating no previous scenario run.


Scenario Files
-------------

This section lists the scenario files included in the configuration.

.. toctree::
   :maxdepth: 2

   ebay_categories_phones_apple.rst
   ebay_stores_mmhfcom.rst
   ebay_stores_pacificindustriesltd.rst
   ebay_stores_thegasketsman75.rst
   ebay_stores_himaio12.rst