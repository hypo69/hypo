rst
How to use the GWorksheet class
========================================================================================

Description
-------------------------
The `GWorksheet` class provides methods for managing Google Sheets worksheets.  It inherits from the `Worksheet` class and facilitates creation, access, and modification of worksheets within a spreadsheet.  Crucially, it handles checking if a worksheet already exists and optionally wiping existing data before creating a new one. It also integrates with the `GSRender` class for formatting tasks like setting the worksheet's direction and adding headers.


Execution steps
-------------------------
1. **Import necessary modules:**  Import the `Spreadsheet`, `Worksheet`, `GSRender` classes, and any other required modules.  Note that the code currently uses `global_settingspread` and `goog.grender`, which suggests these are custom modules you've created.

2. **Instantiate a GWorksheet object:** Create a `GWorksheet` object, passing the spreadsheet object (`sh`) and optional parameters like `ws_title`, `rows`, `cols`, `direction`, and `wipe_if_exist`.

3. **Use the `get` method to create or retrieve a worksheet:** Call the `get` method on the `GWorksheet` object to create a new worksheet or retrieve an existing one. This method handles both scenarios, checking if the worksheet with the given `ws_title` already exists.
    *   If `ws_title` is 'new', it creates a new worksheet.
    *   If `ws_title` exists, it retrieves the existing worksheet. If `wipe_if_exist` is `True`, the existing worksheet's data is cleared before retrieval.

4. **Perform operations on the worksheet:** Utilize the `header`, `category`, or `direction` methods to add headers, write category titles, or set the worksheet direction, respectively.


5. **Handle potential errors:** The `get` method prints a message if a worksheet with the specified `ws_title` already exists.  Check for and handle any other potential errors.

Usage example
-------------------------
.. code-block:: python

    from global_settingspread import Spreadsheet, Worksheet
    from goog.grender import GSRender
    from hypotez.src.goog.spreadsheet.bberyakov.gworksheets import GWorksheet

    # Replace with your actual spreadsheet and worksheet details
    spreadsheet_obj = Spreadsheet(...)  # Example:  spreadsheet_obj = Spreadsheet('your_spreadsheet_id')
    ws_title = 'My Worksheet'
    rows = 10
    cols = 20


    # Create a GWorksheet object
    worksheet_obj = GWorksheet(spreadsheet_obj, ws_title=ws_title, rows=rows, cols=cols, wipe_if_exist=True)


    # Get the worksheet.
    worksheet_obj.get(spreadsheet_obj, ws_title=ws_title)

    # Add a header
    worksheet_obj.header(ws_title, range='A1:B1')

    # Write some data (This would depend on the Spreadsheet library)
    # Example:
    # worksheet_obj.write('A2', 'Value1')
    # worksheet_obj.write('B2', 'Value2')

    # Set the worksheet direction
    worksheet_obj.direction('rtl')

    # Save the spreadsheet (optional, depends on your library).
    spreadsheet_obj.save()