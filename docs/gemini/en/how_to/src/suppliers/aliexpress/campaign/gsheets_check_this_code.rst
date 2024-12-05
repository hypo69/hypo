rst
How to use this code block
=========================================================================================

Description
-------------------------
This Python code defines a class `AliCampaignGoogleSheet` for interacting with Google Sheets to manage AliExpress campaign data.  It inherits from `SpreadSheet` and provides methods to handle campaign, category, and product data, including data insertion, deletion, and formatting. It allows for updating and clearing various worksheets within the Google Sheet spreadsheet.  The class manages the creation of worksheets, adding headers, and populating them with data, all while maintaining error handling.

Execution steps
-------------------------
1. **Import necessary modules:** The code starts by importing various libraries like `time`, `SimpleNamespace`, `Driver`, `SpreadSheet`, `AliCampaignEditor`, `j_dumps`, `pprint`, `logger`,  and `gspread_formatting` which are crucial for interacting with Google Sheets, handling data structures, and logging.

2. **Define the `AliCampaignGoogleSheet` class:** This class handles all the Google Sheets interaction logic for the AliExpress campaigns.

3. **Initialization (`__init__` method):**
    - It initializes a `SpreadSheet` object with the spreadsheet ID.
    - It creates an instance of `AliCampaignEditor` to manage campaign data.
    - It clears the spreadsheet (deletes any existing product worksheets).
    - It sets up worksheets for campaign, categories, and potentially products.
    - It opens the Google Sheet URL using a webdriver.

4. **Data Clearing (`clear` method):**
   - Attempts to delete all worksheets except 'categories' and 'product_template'.

5. **Deleting worksheets (`delete_products_worksheets`):**
    - Iterates through all existing worksheets.
    - If a worksheet is not in the excluded list (e.g. 'categories', 'products'), it deletes it.

6. **Setting campaign data (`set_campaign_worksheet`):**
   - Retrieves the 'campaign' worksheet.
   - Prepares data for vertical insertion (header and value pairs).
   - Uses `batch_update` for efficient data insertion.

7. **Setting category data (`set_categories_worksheet`):**
   - Clears the 'categories' worksheet.
   - Retrieves category data from a `SimpleNamespace` object.
   - Adds headers to the 'categories' worksheet.
   - Adds category data in rows (name, title, description, tags, products_count).
   - Formats the 'categories' worksheet.


8. **Setting product data (`set_products_worksheet`):**
   - Copies the 'product' worksheet, naming it after the category.
   - Retrieves product data from a `SimpleNamespace` object.
   - Inserts product data in rows (carefully handling nested structures and potentially empty lists).
   - Formats the newly created product worksheet.


9. **Formatting (`_format_categories_worksheet`, `_format_category_products_worksheet`):**
    - Sets column widths for better readability.
    - Sets row heights for headers.
    - Applies formatting to headers (bold, font size, color).


10. **Retrieving data (`get_categories`):**
    - Fetches all data from the 'categories' worksheet.

11. **Error Handling:** The code includes `try...except` blocks to catch and log exceptions that might occur during file operations, effectively handling potential errors and improving robustness.


Usage example
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.campaign.gsheets_check_this_code import AliCampaignGoogleSheet
    from types import SimpleNamespace

    # Example campaign data (replace with your actual data)
    campaign_data = SimpleNamespace(name="My Campaign", title="Ali Campaign Title", language="English", currency="USD", description="Campaign Description", category=SimpleNamespace(Electronics=SimpleNamespace(name="Electronics", title="Electronics", description="electronics", tags=["electronics", "gadgets"], products_count=10, products=[SimpleNamespace(product_id=123, product_title="phone", promotion_link="promo", app_sale_price=100)])))
    
    # Create an instance of the class
    gsheets_instance = AliCampaignGoogleSheet(campaign_name="My Campaign", language="English", currency="USD")
    
    # Set campaign data in the Google Sheet
    gsheets_instance.set_campaign_worksheet(campaign_data)
    
    # Set category data (replace with your category data)
    gsheets_instance.set_categories_worksheet(campaign_data.category)
    
    # Set product data (replace with your product data)
    gsheets_instance.set_products_worksheet('Electronics')