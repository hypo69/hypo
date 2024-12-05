rst
How to use the aliexpress campaign modules
========================================================================================

Description
-------------------------
This Python module (`hypotez/src/suppliers/aliexpress/campaign/__init__.py`) provides functions for managing Aliexpress advertising campaigns.  It imports classes and functions from submodules like `ali_campaign_editor`, `prepare_campaigns`, and `html_generators` to facilitate various campaign-related operations.  Specifically, it provides functionality to process campaigns, create campaign categories, process all campaigns, and generate HTML reports.

Execution steps
-------------------------
1. **Import necessary modules:** The `__init__.py` file imports classes and functions from submodules within the `campaign` package. This makes those components available for use in other parts of the project.

2. **Access campaign management functions:**  Functions like `process_campaign`, `process_campaign_category`, and `process_all_campaigns` are imported and can be called to perform tasks related to campaign management and processing.

3. **Utilize HTML generation functions:**  `CategoryHTMLGenerator` and `ProductHTMLGenerator` classes are available to generate HTML reports or documents based on campaign data.  These could be used to create detailed reports or visualizations.

4. **Employ the campaign editor:**  `AliCampaignEditor` (and potentially other editor classes) provides an interface to manage campaign data directly. This is probably for more complex editing or configuration tasks.

Usage example
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.campaign import process_campaign, process_all_campaigns
    # ... (Other necessary imports)

    # Example of processing a single campaign
    campaign_data = {
        "campaign_id": 12345,
        "campaign_name": "Summer Sale Campaign",
        # ... other campaign details ...
    }
    
    process_campaign(campaign_data)

    # Example of processing all campaigns
    process_all_campaigns()


    # Example usage (assuming necessary data is prepared):
    #from hypotez.src.suppliers.aliexpress.campaign import CategoryHTMLGenerator

    # ... (Get category data) ...
    category_data = {
        "category_name": "Electronics",
        "products": [
            {"product_id": 67890, "product_name": "Laptop"},
            {"product_id": 101112, "product_name": "Tablet"}
        ]
    }
    
    html_generator = CategoryHTMLGenerator(category_data)
    html_output = html_generator.generate_html()
    
    # ... (Save or process the generated HTML) ...