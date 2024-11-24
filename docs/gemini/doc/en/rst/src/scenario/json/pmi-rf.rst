PMI RF Scenario
==============

This file defines the parameters for a scenario using the KSP supplier for price monitoring using web scraping.


Parameters
----------

.. data:: supplier

   :type: str
   :value: ksp

   Description: The supplier for the price monitoring.

.. data:: supplier_prefix

   :type: str
   :value: ksp

   Description: Prefix for the supplier.


.. data:: start_url

   :type: str
   :value: https://www.ksp.co.il/

   Description: The starting URL for the web scraping process.

.. data:: price_rule

   :type: str
   :value: +100

   Description: The price rule for the product.

.. data:: num_items_4_flush

   :type: int
   :value: 300

   Description: The number of items to fetch for each price update.

.. data:: if_login

   :type: bool
   :value: False

   Description: Indicates whether login is required for the web scraping process.


.. data:: parcing method [webdriver|api]

   :type: str
   :value: web

   Description: The method used for data extraction (web scraping).


.. data:: about method web scrapping [webdriver|api]

   :type: str
   :value: Если я работаю через API мне не нужен webdriver

   Description: Details on the chosen method for web scraping.

.. data:: collect_products_from_categorypage

   :type: bool
   :value: False

   Description: Whether to collect products from a category page.

.. data:: scenarios

   :type: dict
   :value: {}

   Description: Empty dictionary for scenarios.