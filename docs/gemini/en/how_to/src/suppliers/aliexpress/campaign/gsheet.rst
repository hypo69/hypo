rst
How to use the AliCampaignGoogleSheet class
=========================================================================================

Description
-------------------------
This Python code defines a class `AliCampaignGoogleSheet` for interacting with Google Sheets, specifically within the context of AliExpress campaign management.  It inherits from the `SpreadSheet` class and provides methods for managing worksheets, recording category and product data, and formatting sheets.  Critically, it handles bulk updates and error handling through logging. The code focuses on maintaining a structured, organized, and efficient approach to data manipulation within a Google Sheet campaign setup.

Execution steps
-------------------------
1. **Initialization:** The `__init__` method of the class initializes the connection to a specific Google Sheet (`spreadsheet_id`).  It takes the campaign name, language, and currency as input, enabling tailored data management.

2. **Clearing Data:** The `clear` method deletes all worksheets except 'categories' and 'product_template', ensuring a clean slate for new data. Error handling is implemented within this method to catch and log any exceptions during sheet deletion.

3. **Setting Campaign Data:** The `set_campaign_worksheet` method writes campaign details (name, title, language, currency, description) into the 'campaign' worksheet in a vertical format. This method utilizes `batch_update` for efficiency, handling errors to maintain program integrity.

4. **Setting Category Data:** The `set_categories_worksheet` method writes data from a `SimpleNamespace` object representing categories into the 'categories' worksheet, ensuring correct attribute handling and proper formatting.

5. **Setting Product Data:** The `set_products_worksheet` method is crucial for populating product data for a specific category. It iterates through products within a category, extracts data, and updates the corresponding worksheet, handling potential errors gracefully. This method efficiently populates the product sheets using a bulk update approach for optimal performance.

6. **Formatting Worksheets:** The `_format_categories_worksheet` and `_format_category_products_worksheet` methods handle formatting the 'categories' and product category worksheets, respectively. This includes setting column widths, row heights, and applying styling to headers for enhanced readability. Error handling is included to manage potential issues during formatting.

7. **Retrieving Data:** The `get_categories` method retrieves all category data from the 'categories' worksheet and returns it as a list of dictionaries, facilitating data retrieval.


Usage example
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.campaign.gsheet import AliCampaignGoogleSheet
    from types import SimpleNamespace

    # Sample campaign data (replace with your actual data)
    campaign_data = SimpleNamespace(
        campaign_name='Example Campaign',
        title='Example Campaign Title',
        language='English',
        currency='USD',
        description='Description of the campaign',
    )


    # Sample category data (replace with your actual data)
    category_data = SimpleNamespace(
        category_1=SimpleNamespace(
            name='Electronics',
            title='Electronic Devices',
            description='A description of the electronics category',
            tags=['electronics', 'gadgets'],
            products_count=10,
            products=[
              SimpleNamespace(product_id=1, product_title="Phone", promotion_link="link"),
              SimpleNamespace(product_id=2, product_title="Tablet", promotion_link="link")
            ],
        ),
    )

    # Initialize the Google Sheets class
    gsheet = AliCampaignGoogleSheet(campaign_name='sample')

    # Set the campaign data
    gsheet.set_campaign_worksheet(campaign_data)

    # Set the category data
    gsheet.set_categories_worksheet(category_data.category_1)

    # Set the product data
    gsheet.set_products_worksheet('category_1')

    # Clear the sheets (optional, for testing)
    # gsheet.clear()

    # Retrieve categories data
    categories = gsheet.get_categories()
    print(categories)