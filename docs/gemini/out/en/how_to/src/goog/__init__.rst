rst
How to use the goog module
========================================================================================

Description
-------------------------
This module initializes the `MODE` variable and imports the `SpreadSheet` class from the `spreadsheet` submodule.  It serves as an entry point for using functionality related to spreadsheet operations within the `hypotez` project.  The `MODE` variable likely controls configuration for the project, potentially distinguishing between development and production modes.


Execution steps
-------------------------
1. The module sets the global variable `MODE` to the string value `'dev'`. This assignment likely configures the application for development mode.

2. The module imports the `SpreadSheet` class from the `spreadsheet` submodule.  This allows for the usage of spreadsheet-related functions defined within that module.


Usage example
-------------------------
.. code-block:: python

    from hypotez.src.goog import SpreadSheet

    # Example usage of the SpreadSheet class (assuming the spreadsheet module is correctly defined).
    # Replace with your actual spreadsheet data.
    spreadsheet_data = {
        "Sheet1": [
            ["Header1", "Header2"],
            ["Value1", "Value2"],
            ["Value3", "Value4"]
        ]
    }

    my_spreadsheet = SpreadSheet(spreadsheet_data)

    # Example method call within SpreadSheet (replace with actual method).
    # Example: get_data_from_sheet
    sheet_data = my_spreadsheet.get_data_from_sheet("Sheet1")

    # Print the data (replace with desired output handling)
    print(sheet_data)