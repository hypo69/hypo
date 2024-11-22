```rst
Scenario Executor Module
=======================

.. module:: hypotez.src.scenario.executor
    :platform: Windows, Unix
    :synopsis: Module for executing scenarios to collect product data and insert it into PrestaShop.

Description
----------

This module contains functions for executing scenarios to collect product data from various sources and store it in PrestaShop.  It defines a pipeline involving a driver, suppliers, and a PrestaShop handler.

Functions
---------

.. autofunction:: hypotez.src.scenario.executor.run_scenario_files
.. autofunction:: hypotez.src.scenario.executor.run_scenario_file
.. autofunction:: hypotez.src.scenario.executor.run_scenario
.. autofunction:: hypotez.src.scenario.executor.run_scenarios
.. autofunction:: hypotez.src.scenario.executor.insert_grabbed_data
.. autofunction:: hypotez.src.scenario.executor.execute_PrestaShop_insert
.. autofunction:: hypotez.src.scenario.executor.execute_PrestaShop_insert_async
.. autofunction:: hypotez.src.scenario.executor.dump_journal


Data Structures
---------------

.. autoclass:: hypotez.src.scenario.executor.ProductFields
    :members:
```