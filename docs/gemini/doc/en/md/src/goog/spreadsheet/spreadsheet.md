# hypotez/src/goog/spreadsheet/spreadsheet.py

## Overview

This module provides a minimal library for working with Google Sheets. It includes a `SpreadSheet` class for interacting with Google Sheets, managing spreadsheets, and uploading data from CSV files.


## Classes

### `SpreadSheet`

**Description**: This class handles interactions with Google Sheets, including creating new spreadsheets, uploading data from CSV files, and managing worksheets.

**Attributes**:

- `spreadsheet_id` (str | None): ID of the Google Sheets spreadsheet.  `None` if creating a new spreadsheet.
- `spreadsheet_name` (str | None): Name of the new spreadsheet if `spreadsheet_id` is `None`.
- `spreadsheet` (Spreadsheet): The Google Sheets spreadsheet object.
- `data_file` (Path): Path to the CSV file containing data.
- `sheet_name` (str): Name of the sheet in Google Sheets.
- `credentials` (ServiceAccountCredentials): Credentials for accessing Google Sheets.
- `client` (gspread.Client): Authorized client for Google Sheets API.
- `worksheet` (Worksheet): The worksheet object within the spreadsheet.
- `create_sheet` (bool): A flag (not used in the provided code, but could be useful for future expansion).


**Methods**:

#### `__init__(self, spreadsheet_id: str, *args, **kwards)`

**Description**: Initializes the `SpreadSheet` object with spreadsheet ID, optionally sheet name, and spreadsheet name.

**Parameters**:

- `spreadsheet_id` (str): ID of the Google Sheets spreadsheet. Specify `None` to create a new spreadsheet.
- `*args`: Variable positional arguments.
- `**kwards`: Keyword arguments.

**Raises**:
- `gspread.exceptions.SpreadsheetNotFound`: If a spreadsheet with the given ID does not exist.


#### `_create_credentials(self)`

**Description**: Creates credentials for accessing the Google Sheets API.

**Returns**:
- `ServiceAccountCredentials`: The created credentials object.

**Raises**:
- `Exception`: If there's an error during credential creation. Includes detailed error logging with `exc_info=True`.


#### `_authorize_client(self)`

**Description**: Authorizes a client for the Google Sheets API.

**Returns**:
- `gspread.Client`: The authorized client object.

**Raises**:
- `Exception`: If there's an error during client authorization. Includes detailed error logging with `exc_info=True`.


#### `get_worksheet(self, worksheet_name: str | Worksheet) -> Worksheet | None`

**Description**: Retrieves a worksheet by name. If the worksheet doesn't exist, it attempts to create it.

**Parameters**:

- `worksheet_name` (str | Worksheet): Name of the sheet.

**Returns**:
- `Worksheet`: The worksheet object if found or created. Returns `None` if an error occurs.

#### `create_worksheet(self, title:str, dim:dict = {\'rows\':100,\'cols\':10}) -> Worksheet | None`

**Description**: Creates a new worksheet within the spreadsheet with the specified title and dimensions.

**Parameters**:
- `title` (str): Title of the new worksheet.
- `dim` (dict): Dictionary specifying the dimensions (rows, columns) for the new worksheet. Defaults to `{\'rows\': 100, \'cols\': 10}`.


**Returns**:
- `Worksheet`: The newly created worksheet. Returns `None` if an error occurs.


#### `copy_worksheet(self, from_worksheet: str, to_worksheet: str)`

**Description**: Copies a worksheet to a new worksheet with a specified name. (Not fully documented in the provided code)


#### `upload_data_to_sheet(self)`

**Description**: Uploads data from a CSV file to a specified sheet in Google Sheets.


**Raises**:
- `ValueError`: If the data file path is not set or the file does not exist.
- `Exception`: If there's any error during data upload. Includes detailed error logging with `exc_info=True`.


## Functions

###  (None in the provided code)


## Module Usage Example

```python
# Example usage of the class
if __name__ == "__main__":
    from pathlib import Path
    data_file = Path('/mnt/data/google_extracted/your_data_file.csv')  # Replace with actual data file
    sheet_name = 'Sheet1'  # Replace with actual sheet name in Google Sheets

    # Create a new Spreadsheet if spreadsheet_id is not specified
    google_sheet_handler = SpreadSheet(
        spreadsheet_id=None,
        sheet_name=sheet_name,
        spreadsheet_name='My New Spreadsheet'
    )
    google_sheet_handler.upload_data_to_sheet()

```