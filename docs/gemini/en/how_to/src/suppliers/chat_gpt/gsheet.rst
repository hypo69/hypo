rst
How to use the GptGs class for managing Google Sheets
============================================================================================

Description
-------------------------
This Python code defines a `GptGs` class, inheriting from `SpreadSheet`, designed to manage Google Sheets within AliExpress campaigns.  It allows for writing and reading data related to categories, products, and campaigns within those spreadsheets.  Crucially, it handles SimpleNamespace objects for data organization, simplifying data access and manipulation.  Methods include clearing data, updating various sheets (like 'campaign', 'category', 'categories'), copying templates to create new product sheets, and deleting worksheets.

Execution steps
-------------------------
1. **Import necessary libraries:** The code begins by importing necessary libraries like `time`, `SimpleNamespace`, `List`, `gspread` objects, custom classes from `src`, and `logger` for logging.

2. **Define the `GptGs` class:** This class inherits from `SpreadSheet`, establishing a connection to a specified Google Sheet using a spreadsheet ID.

3. **`__init__` method:** Initializes the Google Sheet connection with the given spreadsheet ID.  It also takes parameters for `campaign_name`, `category_name`, `language`, and `currency`, though these are not used in the provided example.

4. **`clear` method:** Clears the Google Sheet by deleting product worksheets and clearing data on specific sheets ('category', 'categories', 'campaign').  It includes error handling for potential exceptions during clearing.

5. **`update_chat_worksheet` method:** Updates a specified Google Sheet worksheet with campaign data provided in a SimpleNamespace object. Extracts data fields from the object and writes them to the worksheet.

6. **`get_campaign_worksheet` method:** Reads campaign data from the 'campaign' worksheet and returns it in a SimpleNamespace object.

7. **`set_category_worksheet` method:** Writes category data from a SimpleNamespace object to the 'category' worksheet in a vertical format.

8. **`get_category_worksheet` method:** Reads category data from the 'category' worksheet and returns it as a SimpleNamespace object.

9. **`set_categories_worksheet` method:** Writes data from a SimpleNamespace object to the 'categories' worksheet.  Handles potential errors and gracefully skips non-SimpleNamespace attributes. It iterates over the SimpleNamespace and inserts data into the sheet.

10. **`get_categories_worksheet` method:** Reads data from columns A-E, starting from the second row, from the 'categories' worksheet.

11. **`set_product_worksheet` method:** Creates a new product worksheet by copying the 'product_template' worksheet and writes product data to the new sheet. Takes a SimpleNamespace object for product data.

12. **`get_product_worksheet` method:** Reads product data from the 'products' worksheet and returns it in a SimpleNamespace object.

13. **`set_products_worksheet` method:** Writes product data from a list of SimpleNamespace objects to the respective category worksheets. It iterates through the product list, writes the data, and updates the worksheet.

14. **`delete_products_worksheets` method:** Deletes all worksheets in the spreadsheet except for 'categories' and 'product_template'.

15. **`save_categories_from_worksheet` method:** Saves edited categories from the 'categories' worksheet into a SimpleNamespace object, updating the campaign data accordingly.

16. **`save_campaign_from_worksheet` method:** Saves edited campaign data, including categories, from the Google Sheet into the campaign object, then updates the campaign.


Usage example
-------------------------
```python
from hypotez.src.suppliers.chat_gpt.gsheet import GptGs
from types import SimpleNamespace

# Example usage
sheet_manager = GptGs()

# Example data (replace with your actual data)
campaign_data = SimpleNamespace(
    name="Campaign_Name",
    title="Campaign Title",
    description="Campaign Description",
    tags=["tag1", "tag2"],
    products_count=10
)

sheet_manager.update_chat_worksheet(campaign_data, "conversation_name") #Update worksheet
sheet_manager.save_campaign_from_worksheet() #Save edited campaign data from the sheet

# ... (add other operations using the class)
```
```
```
**Important Notes**:

* Replace `'1nu4mNNFMzSePlggaaL_QM2vdKVP_NNBl2OG7R9MNrs0'` with the actual ID of your Google Sheet in the `__init__` method of `GptGs`.
*  The `campaign_data` example needs to be replaced with your actual campaign data structured as a SimpleNamespace object.
* Error handling is included to catch and log exceptions, improving robustness.
* The code heavily relies on the existence of a `SpreadSheet` class (and other helper classes from `src`) that is not provided in this snippet. You'll need to have that class available in your project for this code to function correctly.