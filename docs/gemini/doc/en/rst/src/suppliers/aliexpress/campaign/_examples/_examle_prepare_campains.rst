Module _examle_prepare_campains
=============================

.. module:: hypotez.src.suppliers.aliexpress.campaign._examples._examle_prepare_campains
    :platform: Windows, Unix
    :synopsis: This module contains example functions for preparing campaigns on AliExpress.


Description
-----------

This module provides example usage for functions in the `prepare_campaigns` module.  It demonstrates how to process single campaign categories, specific campaigns, and all campaigns.  It also shows how to handle different languages and currencies.


Functions
---------

.. autofunction:: hypotez.src.suppliers.aliexpress.campaign._examples._examle_prepare_campains.process_campaign_category
   :noindex:
.. autofunction:: hypotez.src.suppliers.aliexpress.campaign._examples._examle_prepare_campains.process_campaign
   :noindex:
.. autofunction:: hypotez.src.suppliers.aliexpress.campaign._examples._examle_prepare_campains.process_all_campaigns
   :noindex:


Example Usage
------------

The examples in this module demonstrate the use of the provided functions, processing different campaign types and configurations.

Example 1: Processing a Single Campaign Category

.. code-block:: python

    process_campaign_category("SummerSale", "Electronics", "EN", "USD", force=True)

Example 2: Processing a Specific Campaign

.. code-block:: python

    process_campaign("WinterSale", categories=["Clothing", "Toys"], language="EN", currency="USD", force=False)


Example 3: Processing All Campaigns

.. code-block:: python

    process_all_campaigns(language="EN", currency="USD", force=True)


Variables
---------

.. autovariable:: hypotez.src.suppliers.aliexpress.campaign._examples._examle_prepare_campains.MODE
   :noindex:

.. autovariable:: hypotez.src.suppliers.aliexpress.campaign._examples._examle_prepare_campains.campaigns_directory
   :noindex:
.. autovariable:: hypotez.src.suppliers.aliexpress.campaign._examples._examle_prepare_campains.campaign_names
   :noindex:
.. autovariable:: hypotez.src.suppliers.aliexpress.campaign._examples._examle_prepare_campains.languages
   :noindex:

.. note::  The usage of `gs.path.google_drive` suggests an external dependency.  Ensure the appropriate imports are documented and available to the Sphinx build environment.