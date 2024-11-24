executor Module
===============

.. automodule:: hypotez.src.scenario.executor
   :members:
   :undoc-members:
   :show-inheritance:


Examples
--------

This module provides examples demonstrating the usage of its functions for scenario execution,
file handling, product processing, and interaction with the PrestaShop API.

Example 1: `run_scenario_files`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Runs a list of scenario files sequentially.

.. autofunction:: hypotez.src.scenario.executor.run_scenario_files
   :noindex:


Example 2: `run_scenario_file`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Runs a single scenario file.

.. autofunction:: hypotez.src.scenario.executor.run_scenario_file
   :noindex:


Example 3: `run_scenario`
^^^^^^^^^^^^^^^^^^^^^^^^^

Executes a single scenario.

.. autofunction:: hypotez.src.scenario.executor.run_scenario
   :noindex:


Example 4: `insert_grabbed_data`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Inserts grabbed product data into PrestaShop.

.. autofunction:: hypotez.src.scenario.executor.insert_grabbed_data
   :noindex:


Example 5: `add_coupon`
^^^^^^^^^^^^^^^^^^^^^^^

Adds a coupon to the PrestaShop database.

.. autofunction:: hypotez.src.scenario.executor.add_coupon
   :noindex:


Example 6: `execute_PrestaShop_insert_async`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Asynchronously executes PrestaShop product insertion.

.. autofunction:: hypotez.src.scenario.executor.execute_PrestaShop_insert_async
   :noindex:


Example 7: `execute_PrestaShop_insert`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Synchronously executes PrestaShop product insertion.

.. autofunction:: hypotez.src.scenario.executor.execute_PrestaShop_insert
   :noindex:


Detailed Explanation of Examples
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Example 1 demonstrates running a list of scenario files, while Example 2 shows how to run a single file. Example 3 illustrates executing a scenario.  Example 4 describes inserting grabbed product data. Example 5 provides an example of adding a coupon, and Examples 6 and 7 showcase asynchronous and synchronous PrestaShop product insertion, respectively.

These examples provide insight into how to use the `executor` module's functions for various tasks within your project.  Note the usage of mock classes (`MockSupplier`, `MockRelatedModules`, `MockDriver`) for demonstration purposes.  Actual implementation should use appropriate classes from the `src` modules.