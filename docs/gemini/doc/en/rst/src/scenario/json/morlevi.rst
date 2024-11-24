morlevi Scenario Documentation
============================

This file documents the scenarios defined in the `morlevi.json` configuration file.  It outlines the various categories and products to be scraped.


.. toctree::
   :maxdepth: 2

   morlevi_categories_cases_antec
   morlevi_categories_storage_samsung
   morlevi_categories_storage_kingston
   morlevi_categories_video
   morlevi_categories_monitors_samsung
   morlevi_categories_monitors_lenovo
   morlevi_categories_mb_gigabyte
   morlevi_categories_cases_coolermaster
   morlevi_categories_cases_corsair
   morlevi_categories_cases_generic
   morlevi_categories_headsets
   morlevi_categories_laptops_asus
   morlevi_categories_laptops_gigabyte
   morlevi_categories_laptops_dell
   morlevi_categories_laptops_hp
   morlevi_categories_laptops_lenovo
   morlevi_categories_memory
   morlevi_categories_cpu
   morlevi_categories_cases_antec


morlevi Configuration
---------------------

This section details the configuration parameters within the `morlevi.json` file.

* `supplier`: morlevi
* `supplier_id`: 2784
* `supplier_prefix`: mlv
* `start_url`: https://www.morlevi.co.il/
* `login_url`: https://www.morlevi.co.il/
* `price_rule`: *1.43
* `if_list`: first
* `use_mouse`: False
* `mandatory`: True
* `collect_products_from_categorypage`: False
* `num_items_4_flush`: 500
* `if_login`: True
* `parcing method [webdriver|api]`: web
* `about method web scrapping [webdriver|api]`: Если я работаю через API мне не нужен webdriver
* `scenario_files`: A list of referenced scenario files.
* `last_runned_scenario`: morlevi_categories_mb_gigabyte.json
* `excluded`: A list of excluded scenarios (organized in nested lists for grouping).

Detailed descriptions of individual scenario files (e.g., `morlevi_categories_cases_antec.json`) are documented in their respective files.

```