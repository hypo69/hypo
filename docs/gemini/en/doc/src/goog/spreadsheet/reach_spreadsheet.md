# ReachSpreadsheet Module

## Overview

This module provides a class, `ReachSpreadsheet`, for interacting with Google Sheets using the Google Sheets API v4.  It handles tasks like creating spreadsheets, sharing them, setting dimensions, and adding sheets.  The module is designed for use within a larger application (likely a Telegram bot in this case) and is not intended as a general-purpose Google Sheets library. It relies on a service account for authentication.

## Classes

### `SpreadsheetError`

**Description**: Base class for exceptions related to spreadsheet operations.

### `SpreadsheetNotSetError`

**Description**: Raised when a spreadsheet has not been set.

### `SheetNotSetError`

**Description**: Raised when a sheet has not been set.

### `ReachSpreadsheet`

**Description**: A class for interacting with Google Sheets.

**Methods**

#### `__init__(self, debugMode=False)`

**Description**: Initializes the `ReachSpreadsheet` object.  Loads credentials from a JSON keyfile and creates necessary API services.

**Parameters**

- `debugMode` (bool, optional): If True, prints debug information. Defaults to False.

**Raises**

- `Exception`:  Handles potential errors during credential loading.  Includes detailed error logging.

#### `create(self, title, sheetTitle, rows=1000, cols=26, locale='en-US', timeZone='Etc/GMT')`

**Description**: Creates a new Google Sheet.

**Parameters**

- `title` (str): The title of the spreadsheet.
- `sheetTitle` (str): The title of the sheet within the spreadsheet.
- `rows` (int, optional): Number of rows in the sheet. Defaults to 1000.
- `cols` (int, optional): Number of columns in the sheet. Defaults to 26.
- `locale` (str, optional): The locale of the spreadsheet. Defaults to 'en-US'.
- `timeZone` (str, optional): The time zone of the spreadsheet. Defaults to 'Etc/GMT'.

**Returns**

- `None`: This method doesn't explicitly return a value; it creates the spreadsheet.

#### `share(self, shareRequestBody)`

**Description**: Shares the spreadsheet with specified permissions.

**Parameters**

- `shareRequestBody` (dict): A dictionary containing the permissions for sharing the sheet.

**Raises**

- `SpreadsheetNotSetError`: If no spreadsheet has been set.

#### `shareWithEmailForReading(self, email)`

**Description**: Shares the spreadsheet for reading with a given email address.

**Parameters**

- `email` (str): Email address of the recipient.

#### `shareWithEmailForWriting(self, email)`

**Description**: Shares the spreadsheet for writing with a given email address.

#### `shareWithAnybodyForReading(self)`

**Description**: Shares the spreadsheet for reading with anyone.

#### `shareWithAnybodyForWriting(self)`

**Description**: Shares the spreadsheet for writing with anyone.

#### `getSheetURL(self)`

**Description**: Returns the URL of the sheet.

**Raises**

- `SpreadsheetNotSetError`: If no spreadsheet has been set.
- `SheetNotSetError`: If no sheet has been set.

#### `setSpreadsheetById(self, spreadsheetId)`

**Description**: Sets the current spreadsheet and sheet based on the provided spreadsheet ID.

**Parameters**

- `spreadsheetId` (str): The ID of the spreadsheet.

#### `runPrepared(self, valueInputOption='USER_ENTERED')`

**Description**: Executes prepared updates (requests and value ranges) to the spreadsheet.

**Parameters**

- `valueInputOption` (str, optional): Specifies how input data should be interpreted. Defaults to 'USER_ENTERED'.

**Returns**

- `tuple`: A tuple containing the responses from batchUpdate and values.batchUpdate operations.


#### `prepare_addSheet(self, sheetTitle, rows=1000, cols=26)`

**Description**: Prepares a request to add a new sheet.

#### `addSheet(self, sheetTitle, rows=1000, cols=26)`

**Description**: Adds a new sheet and sets it as current.

**Parameters**

- `sheetTitle` (str): Title of the new sheet.
- `rows` (int): Number of rows. Defaults to 1000.
- `cols` (int): Number of columns. Defaults to 26.

**Returns**

- `int`: The ID of the newly created sheet.

#### `toGridRange(self, cellsRange)`

**Description**: Converts a string cell range to a dictionary representation of a GridRange.

**Parameters**

- `cellsRange` (str): The cell range (e.g., "A1:B2").

**Returns**

- `dict`: A dictionary representing the GridRange.

#### `prepare_setDimensionPixelSize(self, dimension, startIndex, endIndex, pixelSize)`

**Description**: Prepares a request to set the pixel size of dimensions (rows or columns).

#### `prepare_setColumnsWidth(self, startCol, endCol, width)`

**Description**: Prepares a request to set column width(s).

#### `prepare_setColumnWidth(self, col, width)`

**Description**: Prepares a request to set the width of a specific column.

#### `prepare_setRowsHeight(self, startRow, endRow, height)`

**Description**: Prepares a request to set row height(s).

#### `prepare_setRowHeight(self, row, height)`

**Description**: Prepares a request to set the height of a specific row.

#### `prepare_setValues(self, cellsRange, values, majorDimension='ROWS')`

**Description**: Prepares a request to set values in a specific range.

#### `prepare_mergeCells(self, cellsRange, mergeType='MERGE_ALL')`

**Description**: Prepares a request to merge cells.

#### `prepare_setCellStringFormatterormat(self, cellsRange, formatJSON, fields='userEnteredFormat')`

**Description**: Prepares a request to format cells.

#### `prepare_setCellStringFormatterormats(self, cellsRange, formatsJSON, fields='userEnteredFormat')`

**Description**: Prepares a request to format cells (list of formats).



## Functions

### `htmlColorToJSON(htmlColor)`

**Description**: Converts an HTML color string to a JSON-compatible dictionary.

**Parameters**

- `htmlColor` (str): An HTML color string (e.g., "#FF0000").


**Returns**

- `dict`: A dictionary representing the RGB color values.


### `create_pricelist(docTitle, sheetTitle, values)`

**Description**: Creates a spreadsheet with a price list.

**Parameters**

- `docTitle` (str): Title of the spreadsheet.
- `sheetTitle` (str): Title of the sheet within the spreadsheet.
- `values` (list): A list of lists containing the data to be added to the sheet.


## Example Usage (from test functions)

```
# Example of creating a spreadsheet.
ss = Spreadsheet(debugMode=True)
ss.create("Preved medved", "Тестовый лист")
ss.shareWithEmailForWriting("volkov.ioann@gmail.com")
```

```
# Example of setting a spreadsheet by ID.
ss.setSpreadsheetById('19SPK--efwYq9pZ7TvBYtFItxE0gY3zpfR5NykOJ6o7I')
```


```
# Example of adding a sheet.
ss.addSheet("Я лолка №1", 500, 11)
```

This documentation provides a high-level overview of the ReachSpreadsheet module.  More detailed documentation for specific methods, including exception handling, could be included if necessary.