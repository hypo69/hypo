AliExpress Campaign Module
==========================

This module provides functionalities for managing and editing promotional campaigns,
interacting with Google Sheets for data retrieval and manipulation, and preparing
campaign data for use.  It handles various aspects from campaign initialization and
data retrieval to preparing campaign products for promotions.


.. automodule:: hypotez.src.suppliers.aliexpress.campaign.ali_promo_campaign
   :members:
   :undoc-members:
   :show-inheritance:

Campaign Management Functions
----------------------------

.. autofunction:: hypotez.src.suppliers.aliexpress.campaign.process_campaign_category
.. autofunction:: hypotez.src.suppliers.aliexpress.campaign.process_campaign
.. autofunction:: hypotez.src.suppliers.aliexpress.campaign.process_all_campaigns


Module Overview
---------------

The `campaign` module is structured to facilitate a workflow for campaign management,
including initialization, data interaction with Google Sheets, and preparation of
campaign data.  The module leverages external dependencies and utility functions
for data processing, file handling, and Google Sheet interaction.


.. rubric:: Detailed Workflow
.. list-table::
   :header-rows: 1

   * - Step
     - Description
   * - Initialization
     - Imports necessary modules, initializes settings, and performs initial configuration.
   * - Campaign Editing
     - Uses functions like `process_campaign` or `process_campaign_category` to modify campaign data.
   * - Promotional Campaign Management
     - Manages specific promotional strategies and configurations for campaigns.
   * - Google Sheets Interaction
     - Reads, processes, and writes campaign data to/from Google Sheets.
   * - Data Preparation
     - Preprocesses and validates campaign data for execution.
   * - Testing and Validation
     - Runs tests to validate the functionality and integrity of campaign data.



Example Usages
-------------

The following examples demonstrate how to use the provided functions for processing
campaign categories, individual campaigns, and all campaigns within the system.

.. code-block:: python

   process_campaign_category("SummerSale", "Electronics", "EN", "USD", force=True)

.. code-block:: python

   process_campaign("WinterSale", categories=["Clothing", "Toys"], language="EN", currency="USD", force=False)

.. code-block:: python

   process_all_campaigns(language="EN", currency="USD", force=True)


Further Details
---------------

Refer to the module's source code for detailed implementation details, including
method parameters and return types.  The `_docs` directory contains supporting
markdown files with comprehensive documentation.


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`