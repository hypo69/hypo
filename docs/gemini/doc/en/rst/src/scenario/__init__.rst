hypotez/src/scenario/__init__.py
============================

.. module:: scenario
   :platform: Windows, Unix
   :synopsis: Module with scenario execution functions: `run_scenario_files`, `run_scenarios`  
Scenario executor for suppliers.

The logic executed is as follows:

.. image:: scenario_flowchart.png
   :alt: Scenario Execution Flowchart
   :width: 50%


.. code-block:: text
   
   +-----------+
   |  Scenario |
   +-----------+
         |
         | Defines
         |
         v
   +-----------+
   | Executor  |
   +-----------+
         |
         | Uses
         |
         v
   +-----------+        +-----------+
   |  Supplier | <----> |  Driver   |
   +-----------+        +-----------+
         |                     |
         | Provides Data        | Provides Interface
         |                     |
         v                     v
   +-----------+        +-----------+
   |  PrestaShop       | Other Suppliers |
   +-----------+        +-----------+

Example usage:


.. code-block:: python
   s = Supplier('aliexpress')
   run_scenario_files(s, 'file1')

   scenario_files = ['file1', ...]
   run_scenario_files(s, scenario_files)

   scenario1 = {'key': 'value'}
   run_scenarios(s, scenario1)

   list_of_scenarios = [scenario1, ...]
   run_scenarios(s, list_of_scenarios)

Example of a scenario file:

.. code-block:: json

   {
     "scenarios": {
       "feet-hand-treatment": {
         "url": "https://hbdeadsea.co.il/product-category/bodyspa/feet-hand-treatment/",
         "name": "Foot and Hand Care",
         "condition": "new",
         "presta_categories": {
           "default_category": 11259,
           "additional_categories": []
         }
       },
       "creams-butters-serums-for-body": {
         "url": "https://hbdeadsea.co.il/product-category/bodyspa/creams-butters-serums-for-body/",
         "name": "Creams, Butters, and Serums for Body",
         "condition": "new",
         "presta_categories": {
           "default_category": 11260,
           "additional_categories": []
         }
       }
     }
   }

For detailed information on the scenario dictionary, read here: ...


.. code-block:: python

   When the program is started via main(), the following sequence of execution occurs:

   s = Supplier('aliexpress')

   s.run()

   s.run('file1')

   scenario_files = ['file1', ...]
   s.run(scenario_files)

   scenario1 = {'key': 'value'}
   s.run(scenario1)

   list_of_scenarios = [scenario1, ...]
   s.run(list_of_scenarios)

Functions
---------

.. autofunction:: run_scenario_files
.. autofunction:: run_scenarios
.. autofunction:: run_scenario
.. autofunction:: run_scenario_file
.. autofunction:: execute_PrestaShop_insert
.. autofunction:: execute_PrestaShop_insert_async