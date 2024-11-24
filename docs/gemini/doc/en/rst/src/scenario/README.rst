Module: src.scenario
===================

.. automodule:: scenario
    :members:
    :undoc-members:
    :show-inheritance:

Scenarios
--------

.. autofunction:: run_scenario_files
.. autofunction:: run_scenario_file
.. autofunction:: run_scenario
.. autofunction:: dump_journal
.. autofunction:: main

Example Scenario
---------------

An example JSON scenario is shown below, describing how to interact with specific product categories on a website. It includes the URL of the page, the category name, and the categories in the PrestaShop database where the products will be saved.

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


Scenario Fields
^^^^^^^^^^^^^^

The following fields are used in the scenario definitions:

* ``"scenario_name"``: The name of the scenario.
* ``"url"``: The target address (link to a category, section, or individual product).
* ``"name"``: The category name, matching the scenario name.
* ``"presta_categories"``:
    * ``"default_category"``: The default category ID in PrestaShop where products will be categorized.
    * ``"additional_categories"``: A list of additional category IDs in PrestaShop for further categorization.

Workflow
-------

The module automates the process of collecting product data from supplier websites and synchronizing it with the PrestaShop database.  The general workflow is described as follows:

1.  Initialization: Instantiate the `Supplier` class with the appropriate supplier identifier.
2.  Running Scenarios: Execute scenarios from files or a list of scenarios using methods like `run_scenario_files`, `run_scenario_file`, and `run_scenarios`.
3.  Execution Flow: Details of how scenarios are processed, including data fetching, processing, and saving.  (See detailed descriptions of the relevant functions below.)

Detailed Function Descriptions
----------------------------

.. autofunction:: run_scenario_files
    :noindex:

.. autofunction:: run_scenario_file
    :noindex:

.. autofunction:: run_scenario
    :noindex:

.. autofunction:: dump_journal
    :noindex:

.. autofunction:: execute_PrestaShop_insert_async
    :noindex:

.. autofunction:: execute_PrestaShop_insert
    :noindex:

.. autofunction:: insert_grabbed_data
    :noindex:


Module Usage Examples
---------------------

The following code snippets show how to use the module functions:

.. code-block:: python

    s = Supplier('aliexpress')
    s.run('file1')

.. code-block:: python

    scenario_files = ['file1', 'file2']
    s.run(scenario_files)

.. code-block:: python

    scenario1 = {'key': 'value'}
    s.run(scenario1)

.. code-block:: python

    list_of_scenarios = [scenario1, scenario2]
    s.run(list_of_scenarios)


Module Dependencies
------------------

The module has dependencies on other modules or components that are not described here.