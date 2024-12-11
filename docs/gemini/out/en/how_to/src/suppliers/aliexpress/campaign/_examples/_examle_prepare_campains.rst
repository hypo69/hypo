rst
How to use the campaign preparation examples
============================================================================================

Description
-------------------------
This code provides examples for preparing campaigns on AliExpress. It demonStartes how to process single campaign categories, specific campaigns, and all campaigns. It also showcases the interaction with campaign data directories.


Execution steps
-------------------------
1. **Import necessary modules:** The code imports the necessary modules from the `..prepare_campaigns` module.


2. **Process a single campaign category (Example 1):**
   The `process_campaign_category` function is called with the category name, product category, language, currency, and a force flag. This likely prepares or updates campaign data for a specific category.


3. **Process a specific campaign (Example 2):**
   The `process_campaign` function is called with the campaign name, a list of categories, language, currency, and a force flag. This likely prepares or updates campaign data for a specific campaign, potentially considering multiple categories.


4. **Process all campaigns (Example 3):**
   The `process_all_campaigns` function is called with the language, currency, and a force flag. This likely prepares or updates campaign data for all campaigns.


5. **Define campaigns directory and get campaign names:** The code sets the campaigns directory path using the `gs.path.google_drive` variable. It then retrieves the names of all campaigns in the defined directory.


6. **Define languages and currencies:** A dictionary `languages` is created to map languages to their corresponding currencies.


Usage example
-------------------------
.. code-block:: python

    import os
    import pathlib
    # Replace with your actual path or mock the gs.path.google_drive object
    # for testing purposes
    class Mock:
        def __init__(self):
            self.path = lambda x :"/your/path/to/campaign"
    gs = Mock()
    from ..prepare_campaigns import * #Assuming these functions are defined in prepare_campaigns

    # Example usage
    # Example 1: Process a single campaign category
    process_campaign_category("SummerSale", "Electronics", "EN", "USD", force=True)


    # Example 2: Process a specific campaign
    process_campaign("WinterSale", categories=["Clothing", "Toys"], language="EN", currency="USD", force=False)


    # Example 3: Process all campaigns
    process_all_campaigns(language="EN", currency="USD", force=True)


    # Example usage with retrieved directory data (replace with actual path)
    campaigns_directory = Path(gs.path("aliexpress","campaigns"))
    campaign_names = get_directory_names(campaigns_directory)
    languages = {"EN": "USD", "HE": "ILS", "RU": "ILS"}