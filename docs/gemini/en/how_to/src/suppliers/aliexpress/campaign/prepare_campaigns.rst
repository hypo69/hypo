rst
How to use this code block
=========================================================================================

Description
-------------------------
This Python script `prepare_campaigns.py` prepares AliExpress advertising campaigns. It handles processing categories, managing campaign data, and generating promotional materials.  The script uses command-line arguments to specify the campaign, categories, language, and currency.  It can process a single campaign, a set of categories within a campaign, or all campaigns in a directory.  It leverages the `AliCampaignEditor` class for campaign-specific operations and `logger` for logging.


Execution steps
-------------------------
1. **Argument Parsing:** The script begins by parsing command-line arguments using `argparse`.  It extracts the campaign name, optional categories, language, and currency.  The `--all` flag indicates processing all campaigns.

2. **Processing Logic:**
   - **Single Campaign Processing (`main_process`):** If `--all` is not set, `main_process` is called.  It determines locales to process based on provided language and currency. If categories are specified, it iterates through them, calling `process_campaign_category` for each. Otherwise, it calls `process_campaign`.

   - **Category Processing (`process_campaign_category`):**  This function utilizes the `AliCampaignEditor` to process a specific category within a campaign for a given language and currency. It returns a list of product titles.

   - **Campaign Processing (`process_campaign`):**  This function also employs `AliCampaignEditor` to handle campaign setup and processing, considering a list of locales.

   - **All Campaigns Processing (`process_all_campaigns`):** If `--all` is set, `process_all_campaigns` is called. It iterates through the campaigns in the `campaigns_directory` and calls `process_campaign` for each.


3. **Campaign Editor Actions:** The `AliCampaignEditor` handles the specific AliExpress campaign operations based on the provided input. These likely include fetching data, manipulating campaign files, and potentially generating promotional materials.

4. **Logging:** The script uses a logger to provide informational and error messages about the campaign processing progress.

5. **Return Values:** The `process_campaign` and `process_all_campaigns` functions return `True` to indicate that the campaign processing completed successfully, assuming no error.


Usage example
-------------------------
.. code-block:: bash

    # Process the "summer_sale" campaign for "electronics" category in English (EN) and US Dollars (USD)
    python prepare_campaigns.py summer_sale -c electronics -l EN -cu USD


.. code-block:: bash

    # Process all campaigns in the "campaigns" directory for English (EN) and US Dollars (USD)
    python prepare_campaigns.py --all -l EN -cu USD

.. code-block:: bash

    # Process the "summer_sale" campaign in all locales (all possible language/currency combinations)
    python prepare_campaigns.py summer_sale