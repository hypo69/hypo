# ReachSpreadsheet Module

## Overview

This module provides a class, `ReachSpreadsheet`, for interacting with Google Sheets API v4.  It allows creation, sharing, and manipulation of spreadsheets, including setting dimensions, formatting cells, and adding sheets.  It handles authorization using service account credentials and provides methods to retrieve a sheet's URL and prepare batches of updates for efficient API calls.


## Classes

### `SpreadsheetError`

**Description**: Base class for exceptions related to spreadsheet operations.

**Attributes**: None


### `SpreadsheetNotSetError`

**Description**: Exception raised when a spreadsheet ID hasn't been set.

**Attributes**: None


### `SheetNotSetError`

**Description**: Exception raised when a sheet ID hasn't been set.

**Attributes**: None


### `ReachSpreadsheet`

**Description**: A class for interacting with Google Sheets, enabling the creation, manipulation, and sharing of spreadsheets.

**Methods**:

- `__init__(self, debugMode=False)`
    **Description**: Initializes the `ReachSpreadsheet` object. Loads credentials from a temporary JSON file, authenticates, and initializes the `httpAuth` and `service` objects.  Handles potential errors during credential loading.
    **Parameters**:
        - `debugMode` (bool, optional): If True, prints debug information. Defaults to False.
    **Raises**:
        - `Exception`:  Raised if there's an error loading credentials.
- `create(self, title, sheetTitle, rows=1000, cols=26, locale='en-US', timeZone='Etc/GMT')`
    **Description**: Creates a new spreadsheet with the given title and sheet title, specifying the initial dimensions, locale, and time zone.
    **Parameters**:
        - `title` (str): The title of the new spreadsheet.
        - `sheetTitle` (str): The title of the sheet to be created within the spreadsheet.
        - `rows` (int, optional): The number of rows in the sheet. Defaults to 1000.
        - `cols` (int, optional): The number of columns in the sheet. Defaults to 26.
        - `locale` (str, optional): The locale of the spreadsheet. Defaults to 'en-US'.
        - `timeZone` (str, optional): The time zone of the spreadsheet. Defaults to 'Etc/GMT'.
    **Returns**:
        - `dict`:  The created spreadsheet's details (dictionary).
    **Raises**:
        - `Exception`:  If there's an issue creating the spreadsheet.
- `share(self, shareRequestBody)`
    **Description**: Shares the current spreadsheet.
    **Parameters**:
        - `shareRequestBody` (dict): A dictionary containing the sharing parameters.
    **Raises**:
        - `SpreadsheetNotSetError`: Raised if the spreadsheet ID is not set.
        - `Exception`:  If there's a problem with the sharing process.
- `shareWithEmailForReading(self, email)`
    **Description**: Shares the spreadsheet with the provided email address as a reader.
- `shareWithEmailForWriting(self, email)`
    **Description**: Shares the spreadsheet with the provided email address as a writer.
- `shareWithAnybodyForReading(self)`
    **Description**: Shares the spreadsheet with anyone with a reading role.
- `shareWithAnybodyForWriting(self)`
    **Description**: Shares the spreadsheet with anyone with a writing role.
- `getSheetURL(self)`
    **Description**: Retrieves the URL of the current sheet.
    **Parameters**: None
    **Returns**:
        - `str`: The URL of the sheet.
    **Raises**:
        - `SpreadsheetNotSetError`: Raised if the spreadsheet ID is not set.
        - `SheetNotSetError`: Raised if the sheet ID is not set.
- `setSpreadsheetById(self, spreadsheetId)`
    **Description**: Sets the current spreadsheet by its ID.
    **Parameters**:
        - `spreadsheetId` (str): The ID of the spreadsheet.
    **Returns**:
        - `dict`: The details of the selected spreadsheet.
    **Raises**:
        - `Exception`:  If there's an issue retrieving the spreadsheet.
- `runPrepared(self, valueInputOption='USER_ENTERED')`
    **Description**: Executes prepared updates to the spreadsheet.  Updates include batch operations (e.g., batchUpdate)
    **Parameters**:
        - `valueInputOption` (str, optional):  Specifies how values in the input data should be interpreted. Defaults to 'USER_ENTERED'.
    **Returns**:
        - `tuple`: A tuple containing the replies and responses from the batch updates.
    **Raises**:
        - `SpreadsheetNotSetError`: Raised if the spreadsheet ID is not set.
- `prepare_addSheet(self, sheetTitle, rows=1000, cols=26)`
    **Description**:  Prepares an addSheet request.
    **Parameters**:
        - `sheetTitle` (str): The title of the sheet to add.
        - `rows` (int, optional): The number of rows. Defaults to 1000.
        - `cols` (int, optional): The number of columns. Defaults to 26.
    **Returns**:
         None.
- `addSheet(self, sheetTitle, rows=1000, cols=26)`
    **Description**: Adds a new sheet, sets it as the current sheet, and returns its ID.
    **Parameters**:
        - `sheetTitle` (str): The title of the new sheet.
        - `rows` (int, optional): The number of rows. Defaults to 1000.
        - `cols` (int, optional): The number of columns. Defaults to 26.
    **Returns**:
        - int: The ID of the added sheet.
    **Raises**:
        - `SpreadsheetNotSetError`: If no spreadsheet is set.
- `toGridRange(self, cellsRange)`
    **Description**: Converts a cell range string to a dictionary representing a GridRange.
    **Parameters**:
        - `cellsRange` (str): The cell range (e.g., "A1:B2").
    **Returns**:
        - dict: A dictionary representing the GridRange.
    **Raises**:
        - `SheetNotSetError`: If the sheet ID is not set.

- (Remaining methods) ... (Similar method descriptions with parameters, return values, and potential exceptions)


## Functions

### `htmlColorToJSON(htmlColor)`
**Description**: Converts an HTML color string to a JSON-compatible dictionary.

**Parameters**:
- `htmlColor` (str): The HTML color string (e.g., "#FF0000").

**Returns**:
- dict: A dictionary with "red", "green", and "blue" keys representing the normalized color components.


### `testCreateSpreadsheet()`, `testSetSpreadsheet()`, `testAddSheet()`, etc.

**Description**:  These are test functions for the `ReachSpreadsheet` class.  They demonstrate various usage patterns.  You can safely ignore details of implementation.


```