hypotez/src/scenario/_examples/_example_executor.py
==================================================

.. module:: hypotez.src.scenario._examples._example_executor
    :platform: Windows, Unix
    :synopsis: This module contains examples for the executor module from src.scenario.executor.  It demonstrates how to run scenarios, handle scenario files, and interact with the PrestaShop API.

.. moduleauthor:: <Your Name>


Examples
--------

This file provides examples for using the `executor` module, demonstrating scenario execution, file handling, and PrestaShop API interactions.  It includes examples for running lists of scenario files, individual files, single scenarios, product page scenarios, and adding coupons via the PrestaShop API, along with asynchronous execution of PrestaShop inserts.


Example Usage
~~~~~~~~~~~~~

.. autofunction:: example_run_scenario_files
.. autofunction:: example_run_scenario_file
.. autofunction:: example_run_scenario
.. autofunction:: example_insert_grabbed_data
.. autofunction:: example_add_coupon
.. autofunction:: example_execute_PrestaShop_insert_async
.. autofunction:: example_execute_PrestaShop_insert


Classes
-------

.. autoclass:: MockSupplier
    :members:
    :undoc-members:
    :show-inheritance:

.. autoclass:: MockRelatedModules
    :members:
    :undoc-members:
    :show-inheritance:

.. autoclass:: MockDriver
    :members:
    :undoc-members:
    :show-inheritance:

.. autoclass:: ProductFields
    :members:
    :undoc-members:
    :show-inheritance:


.. automodule:: src.scenario.executor
    :members:
    :undoc-members:
    :show-inheritance:
    
.. automodule:: src.utils
    :members:
    :undoc-members:
    :show-inheritance:

.. automodule:: src.product
    :members:
    :undoc-members:
    :show-inheritance:
    
.. automodule:: src.endpoints.PrestaShop
    :members:
    :undoc-members:
    :show-inheritance:



.. note::

   This documentation assumes that the classes `Supplier`, `RelatedModules`, and `Driver` (and potentially others) are defined elsewhere in the project.  The provided `Mock` classes are placeholders.  The actual implementation of `run_scenario_files`, `run_scenario_file`, etc., should be documented in the appropriate `src.scenario.executor` module.