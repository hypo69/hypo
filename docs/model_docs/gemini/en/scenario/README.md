```rst
src.scenario Module Documentation
===============================

This module automates interactions with suppliers using scenarios described in JSON files. It extracts product data from supplier websites and synchronizes it with a database (e.g., PrestaShop).

.. automodule:: src.scenario
   :members:
   :undoc-members:
   :show-inheritance:

Functions
---------

.. autofunction:: src.scenario.run_scenario_files
.. autofunction:: src.scenario.run_scenario_file
.. autofunction:: src.scenario.run_scenario
.. autofunction:: src.scenario.dump_journal
.. autofunction:: src.scenario.main

Scenario Structure
------------------

Scenarios are defined in JSON files.  Each scenario describes how to interact with a specific product category on a supplier's website.

.. code-block:: json
   :caption: Example Scenario

   {
       "scenarios": {
           "example_scenario": {
               "url": "https://example.com/category",
               "name": "example_scenario",
               "presta_categories": {
                   "default_category": 123,
                   "additional_categories": [456]
               }
           }
       }
   }

Scenario Fields
^^^^^^^^^^^^^^^

- ``"scenario_name"``: The name of the scenario.

- ``"url"``: The URL of the product category page.

- ``"name"``: The category name (matches scenario name).

- ``"presta_categories"``: Contains category information for PrestaShop.
    - ``"default_category"``: The default category ID in PrestaShop.
    - ``"additional_categories"``: A list of additional category IDs in PrestaShop.

Module Usage
------------

The module is designed to be used with a `Supplier` object.

.. code-block:: python
   :caption: Example Usage - Running Scenario Files

   s = Supplier('aliexpress')
   s.run(['file1.json', 'file2.json'])

.. code-block:: python
   :caption: Example Usage - Running a Single Scenario

   s = Supplier('aliexpress')
   scenario = {'key': 'value'}
   s.run(scenario)


Workflow and Execution
-----------------------

This section outlines the workflow of the module, including how it interacts with JSON files and PrestaShop.

.. code-block:: plaintext
    Scenario Files --> Load Scenarios --> Data Extraction --> Data Saving --> Logging & Reporting
```