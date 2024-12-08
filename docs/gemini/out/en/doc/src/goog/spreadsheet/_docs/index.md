# Google Spreadsheet API v4 Documentation

## Overview

This module provides a Python wrapper for interacting with Google Sheets API v4. It simplifies the process of creating, updating, and managing spreadsheets, including formatting and data input.  This module addresses the limitations of `gspread` by directly utilizing the more powerful features of Google Sheets API v4.

## Classes

### `Spreadsheet`

**Description**: This class acts as a wrapper around the Google Sheets API v4, simplifying interactions with spreadsheets. It provides methods to prepare and execute multiple operations in a single batch, improving efficiency and control over changes.

**Methods**:

- `prepare_setColumnWidth(col: int, width: int)`:
    **Description**: Prepares a request to set the width of a specific column in the spreadsheet.
    **Parameters**:
        - `col` (int): The index of the column to update (zero-based).
        - `width` (int): The desired width of the column in pixels.
    **Returns**: None

- `prepare_setColumnsWidth(startCol: int, endCol: int, width: int)`:
    **Description**: Prepares a request to set the width of multiple columns.
    **Parameters**:
        - `startCol` (int): Starting column index (inclusive).
        - `endCol` (int): Ending column index (exclusive).
        - `width` (int): The desired width of the columns in pixels.
    **Returns**: None

- `prepare_mergeCells(cellsRange: str)`:
    **Description**: Prepares a request to merge cells in the spreadsheet.
    **Parameters**:
        - `cellsRange` (str): The range of cells to merge, in A1 notation (e.g., "A1:E1").
    **Returns**: None


- `prepare_setCellsFormat(cellsRange: str, format: dict)`:
    **Description**: Prepares a request to set the format of multiple cells.
    **Parameters**:
        - `cellsRange` (str): The range of cells to format, in A1 notation.
        - `format` (dict): A dictionary specifying the format properties (e.g., horizontal alignment, bold text). Example: `{"horizontalAlignment": "CENTER", "textFormat": {"bold": True}}`
    **Returns**: None

- `prepare_setCellsFormats(cellsRange: str, formats: list)`:
    **Description**: Prepares a request to set the format of multiple cells with a list of formats.
    **Parameters**:
        - `cellsRange` (str): The range of cells to format, in A1 notation.
        - `formats` (list): A list of dictionaries, each specifying the format properties for a row of cells.
    **Returns**: None

- `prepare_setValues(cellsRange: str, values: list, majorDimension: str = "ROWS")`:
    **Description**: Prepares a request to set values for a range of cells.
    **Parameters**:
        - `cellsRange` (str): The range of cells to update, in A1 notation (e.g., "B2:C3").
        - `values` (list): A list of lists representing the values to set.  Outer list represents rows, inner lists represent cells.
        - `majorDimension` (str, optional): Specifies whether values should be interpreted as rows or columns (default is "ROWS").
    **Returns**: None


- `runPrepared(valueInputOption: str = "USER_ENTERED")`:
    **Description**: Executes all prepared requests in a batch.
    **Parameters**:
        - `valueInputOption` (str, optional): Specifies how input values should be interpreted ("USER_ENTERED" or "RAW", default "USER_ENTERED").
    **Returns**: A tuple of two lists: the responses from `spreadsheets.batchUpdate` and `spreadsheets.values.batchUpdate`.  Returns `None` if no requests are prepared.

- `__init__(service: object, spreadsheetId: str, sheetId: int = 0, sheetTitle: str = "")`:
    **Description**: Initializes a Spreadsheet object.
    **Parameters**:
        - `service`: The Sheets API service object.
        - `spreadsheetId` (str): The ID of the spreadsheet.
        - `sheetId` (int, optional): The ID of the sheet (default is 0, which usually corresponds to the first sheet).
        - `sheetTitle` (str, optional): The title of the sheet (used for preparing setValues requests).
    **Returns**: None


## Functions

There are no functions defined in the provided code snippet.


## Module Usage

```python
# Example usage (requires appropriate imports and credentials setup)
# ... (import statements for necessary libraries)

# Load credentials from JSON file
credentials = ServiceAccountCredentials.from_json_keyfile_name('your_credentials.json', ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)

# Initialize a Spreadsheet object
spreadsheet_id = 'your_spreadsheet_id'  # Replace with your spreadsheet ID
ss = Spreadsheet(service, spreadsheet_id, sheetTitle = 'Sheet1') #Add sheet title

# Prepare and execute requests
ss.prepare_setColumnWidth(0, 317)
ss.prepare_setColumnWidth(1, 200)
ss.prepare_setColumnsWidth(2, 4, 165)
ss.prepare_setColumnWidth(4, 100)
ss.prepare_mergeCells("A1:E1") # Example merge

data = [
    ["This is B2", "This is C2"],
    ["This is B3", "This is C3"]
]
ss.prepare_setValues("B2:C3", data)


ss.runPrepared()
```


**Note:** Replace placeholders like `'your_credentials.json'` and `'your_spreadsheet_id'` with your actual values.  Ensure that your service account has the necessary permissions.


This expanded documentation provides a more comprehensive and structured overview of the `Spreadsheet` class, including detailed method explanations and a usage example. Remember to install the required libraries (`httplib2`, `apiclient`, and `oauth2client`).