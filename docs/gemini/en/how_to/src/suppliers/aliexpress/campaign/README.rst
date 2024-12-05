rst
How to use the aliexpress campaign module
=========================================================================================

Description
-------------------------
The `campaign` module in the `src.suppliers.aliexpress.campaign` package facilitates the creation and publishing of Facebook advertising campaigns. It handles various aspects of the campaign lifecycle, including initialization, directory management, data collection, promotional material generation, review, and publication.  The module supports both general campaign creation and editing of existing campaigns, handling updates to product, category, and campaign details.

Execution steps
-------------------------
1. **Initialization:** Define the campaign's core details like name, language, and currency.
2. **Directory Creation:** Establish the necessary directories and files for the campaign assets.
3. **Configuration Saving:** Save the campaign's configuration details (e.g., in a database or configuration file).
4. **Data Collection (Products):** Gather product data for promotion (e.g., product IDs, descriptions, images).  This can be accomplished by fetching data from internal sources ("ali" or "html").
5. **Data Storage (Products):** Save the collected product data to a persistent storage.
6. **Promotional Material Creation:** Generate or select promotional assets (e.g., banners, graphics).
7. **Campaign Review:** Review and validate the campaign's components before publication.
8. **Publication Decision:** Check if the campaign is ready for publishing. If not, loop back to the review step.
9. **Facebook Publication:** Publish the campaign to Facebook using appropriate APIs.
10. **(Edit Case):**  If editing an existing campaign:
    - **Data Retrieval:** Retrieve the existing campaign details, category data, and associated products.
    - **Data Validation (e.g., affiliate link):** Verify for relevant parameters like affiliate links.
    - **Data Modification:** Update existing data to reflect changes requested in user input.
    - **Category Update:** Update the categories associated with the campaign based on the changes.
    - **Product Updates:** Update product details as required.
    - **Campaign Parameter Updates:** Modify campaign properties like descriptions.
    - **Persistence:** Save the updated data to persistent storage.

11. **End:** Completion of the campaign creation/update process.

Usage example
-------------------------
.. code-block:: python

    # Example initialization (replace with actual data)
    campaign_name = "Summer Sale"
    language = "English"
    currency = "USD"

    # Import the necessary module
    from src.suppliers.aliexpress.campaign import campaign  # Assuming module is named `campaign`

    # Initialize the campaign object.
    campaign_obj = campaign.AliCampaignEditor(campaign_name, language, currency)

    # Example editing an existing campaign
    campaign_obj.update_product(product_id="12345", new_details={"description": "Updated Description"})

    # Example retrieving a specific category.
    category_name = "Electronics"
    category = campaign_obj.get_category(category_name)
    if category:
        print(f"Found category: {category.name}")

    # Example of listing all categories.
    categories = campaign_obj.list_categories()
    if categories:
      for cat in categories:
        print(f"Category: {cat}")

    # Example of getting all products in a category.
    category_products = campaign_obj.get_category_products(category_name)
    if category_products:
        for product in category_products:
            print(f"Product: {product.id}, Details: {product.details}")

    # ... (other calls to campaign methods) ...
    campaign_obj.update_campaign(new_campaign_description="new campaign description")
    # ... (rest of your campaign setup) ...
    campaign_obj.publish()