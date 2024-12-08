rst
How to use the GSRender class for Google Spreadsheet Rendering
=================================================================

Description
-------------------------
This code defines a `GSRender` class for formatting and rendering Google Sheets.  It provides methods for setting header formatting, merging cells, setting worksheet direction, and appending rows with specific formatting.  Crucially, it handles different data types (strings and lists) for header and category titles, and automatically determines the first empty row if not specified.

Execution steps
-------------------------
1. **Import necessary modules:** The code imports various libraries like `gspread`, `gspread_formatting`, `json`, and custom modules (`src`, `helpers`).  This ensures the necessary functionalities for interacting with Google Sheets and processing data are available.

2. **Define the `GSRender` class:** This class encapsulates the logic for rendering Google Sheet content.  It has methods like `render_header`, `merge_range`, `set_worksheet_direction`, `header`, `write_category_title`, and `get_first_empty_row`.

3. **`render_header` method:**  This method formats a header row in a Google Sheet with specified formatting options (background color, alignment, text boldness). It allows merging cells based on a `merge_type` parameter. It also utilizes `ConditionalFormatRule`  to apply formatting based on conditional rules (e.g., applying specific formatting only if cell values exceed 50).

4. **`merge_range` method:** This method merges cells in a specified range based on the given merge type (all cells, columns, or rows).  

5. **`set_worksheet_direction` method:**  Updates the properties of the worksheet to render content in right-to-left direction.

6. **`header` method:** Appends a header row to the worksheet. It automatically finds the first empty row if not specified. It also calls `render_header` to apply formatting to the header.

7. **`write_category_title` method:** Appends a row containing a category title. It handles both string and list inputs for `ws_category_title` and intelligently finds the next empty row.

8. **`get_first_empty_row` method:**  Efficiently determines the first empty row in a worksheet, either by column or across the entire table, helping to position new data appropriately.


Usage example
-------------------------
.. code-block:: python

    from hypotez.src.goog.spreadsheet.bberyakov.grender import GSRender
    from src import gs

    # Assuming you have a Spreadsheet object 'spreadsheet' and a Worksheet object 'worksheet'
    # obtained through gspread

    renderer = GSRender()
    worksheet = spreadsheet.worksheet("Sheet1")

    # Example usage of header method
    header_text = "My Important Header"  # or ['col1','col2','col3']
    renderer.header(worksheet, header_text, row=2) # Append header in row 2


    # Example usage of write_category_title method
    category_title = "Category A" # or ['col1','col2']
    renderer.write_category_title(worksheet, category_title)



    # Example of updating the worksheet direction if needed (use with caution)
    #renderer.set_worksheet_direction(spreadsheet, worksheet, direction='rtl')