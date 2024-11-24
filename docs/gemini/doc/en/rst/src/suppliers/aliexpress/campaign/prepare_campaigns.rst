Module prepare_campaigns
========================

.. module:: hypotez.src.suppliers.aliexpress.campaign.prepare_campaigns
    :platform: Windows, Unix
    :synopsis: Module prepares AliExpress campaigns by processing categories, handling campaign data, and generating promotional materials.

### Examples:

To run the script for a specific campaign:

    python src/suppliers/aliexpress/campaigns/prepare_campaigns.py summer_sale -c electronics -l EN -cu USD

To process all campaigns:

    python src/suppliers/aliexpress/campaigns/prepare_campaigns.py --all -l EN -cu USD


Functions
---------

.. autofunction:: process_campaign_category
.. autofunction:: process_campaign
.. autofunction:: process_all_campaigns
.. autofunction:: main_process
.. autofunction:: main