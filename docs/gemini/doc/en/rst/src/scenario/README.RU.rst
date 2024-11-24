scenario Module Documentation
============================

.. module:: scenario
   :synopsis: This module automates interaction with vendors using scenarios described in JSON files. It adapts data extraction and processing from vendor websites to synchronize product information with your database system.

.. automodule:: scenario
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autofunction:: run_scenario_files
   :param s: The source object
   :type s: object
   :param scenario_files_list: A list of scenario file paths.
   :type scenario_files_list: list
   :raises FileNotFoundError: If a scenario file does not exist.


.. autofunction:: run_scenario_file
   :param s: The source object
   :type s: object
   :param scenario_file: Path to the scenario file.
   :type scenario_file: str
   :raises FileNotFoundError: If the scenario file does not exist.


.. autofunction:: run_scenario
   :param s: The source object
   :type s: object
   :param scenario: The scenario data (e.g., from JSON file).
   :type scenario: dict
   :raises ValueError: If scenario data is invalid or missing required fields.


.. autofunction:: dump_journal
   :param s: The source object
   :type s: object
   :param journal: The journal data to be saved.
   :type journal: dict
   :raises ValueError: If the journal data is invalid or missing required fields.


.. autofunction:: main
   :param s: The source object
   :type s: object


Scenario Example
---------------

A sample JSON scenario describes how to interact with specific product categories on a vendor website. It includes:

- **URL of the product page**: For accessing and extracting product data.
- **Category name**: For category identification.
- **`presta_categories`**: PrestaShop category IDs where products will be saved.

.. code-block:: json
   :linenos:
   :lineno-start: 1

   {
       "scenarios": {
           "מינרל+לחויותלפניםמינרליםותמציותצמחים": {
               "url": "https://hbdeadsea.co.il/product-category/facial/moisture-face/",
               "name": "מינרל+לחויותלפניםמינרליםותמציותצמחים",
               "presta_categories": {
                   "default_category": 11245,
                   "additional_categories": [11288]
               }
           }
       }
   }