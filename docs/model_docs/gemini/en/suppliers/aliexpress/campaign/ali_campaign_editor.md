```rst
Ali Campaign Editor
====================

.. module:: hypotez.src.suppliers.aliexpress.campaign.ali_campaign_editor
   :platform: Windows, Unix
   :synopsis: This module provides the editor for advertising campaigns.

Module Description
------------------

This module implements the `AliCampaignEditor` class, inheriting from `AliPromoCampaign`,  for managing and editing advertising campaigns on AliExpress.  It provides functions for deleting, updating products, updating campaign details, updating categories, and retrieving category information.  The class handles interactions with campaign data stored in JSON files, CSV, and potentially Google Sheets.


Classes
-------

.. autoclass:: hypotez.src.suppliers.aliexpress.campaign.ali_campaign_editor.AliCampaignEditor
   :members:
   :undoc-members:
   :show-inheritance:

Functions
--------

.. autofunction:: hypotez.src.suppliers.aliexpress.campaign.ali_campaign_editor.AliCampaignEditor.__init__
.. autofunction:: hypotez.src.suppliers.aliexpress.campaign.ali_campaign_editor.AliCampaignEditor.delete_product
.. autofunction:: hypotez.src.suppliers.aliexpress.campaign.ali_campaign_editor.AliCampaignEditor.update_product
.. autofunction:: hypotez.src.suppliers.aliexpress.campaign.ali_campaign_editor.AliCampaignEditor.update_campaign
.. autofunction:: hypotez.src.suppliers.aliexpress.campaign.ali_campaign_editor.AliCampaignEditor.update_category
.. autofunction:: hypotez.src.suppliers.aliexpress.campaign.ali_campaign_editor.AliCampaignEditor.get_category
.. autofunction:: hypotez.src.suppliers.aliexpress.campaign.ali_campaign_editor.AliCampaignEditor.list_categories
.. autofunction:: hypotez.src.suppliers.aliexpress.campaign.ali_campaign_editor.AliCampaignEditor.get_category_products


Further Details
---------------

^ AliCampaignEditor Class
~~~~~~~~~~~~~~~

The `AliCampaignEditor` class acts as a central hub for campaign operations. Its methods allow for manipulating products, categories, and campaign meta-data. The class maintains references to pertinent data sources (files and potentially external services).

^ init method
~~~~~~~~~~~~~~~

The `__init__` method initializes the campaign editor, loading campaign data either from parameters or from a specified JSON file.


^ Other methods
~~~~~~~~~~~~~~~

The remaining methods (`delete_product`, `update_product`, `update_campaign`, `update_category`, `get_category`, `list_categories`, and `get_category_products`) are specialized for handling specific campaign tasks. They handle file reading and writing operations to the respective campaign folders and potentially interact with a Google Sheet API. Error handling is included via `try...except` blocks and logs for critical exceptions.
```
