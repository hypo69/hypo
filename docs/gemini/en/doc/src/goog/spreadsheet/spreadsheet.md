# hypotez/src/goog/spreadsheet/spreadsheet.py

## Overview

This module provides a minimal library for working with Google Sheets. It includes a class, `SpreadSheet`, to interact with spreadsheets, create new ones, and upload data from CSV files.  It leverages the `gspread` library and `pandas` for efficient data handling. Error handling and logging are included for robustness.

## Table of Contents

* [Overview](#overview)
* [Classes](#classes)
    * [SpreadSheet](#spreadsheet)
        * [\_\_init\_\_](#__init__)
        * [\_\_create\_credentials](#_create_credentials)
        * [\_\_authorize\_client](#_authorize_client)
        * [get\_worksheet](#get_worksheet)
        * [create\_worksheet](#create_worksheet)
        * [copy\_worksheet](#copy_worksheet)
        * [upload\_data\_to\_sheet](#upload_data_to_sheet)


## Classes

### `SpreadSheet`

**Description**: A class for working with Google Sheets, allowing interaction with existing spreadsheets, creation of new spreadsheets, and uploading data from CSV files.

**Attributes**:
- `spreadsheet_id`: (str | None): The ID of the Google Sheet spreadsheet. `None` if creating a new spreadsheet.
- `spreadsheet_name`: (str | None): The name of the new spreadsheet if `spreadsheet_id` is `None`.
- `spreadsheet`: (Spreadsheet): The `gspread.Spreadsheet` object for interacting with the spreadsheet.
- `data_file`: (Path): The path to the CSV file containing the data.
- `sheet_name`: (str): The name of the sheet in Google Sheets to which data will be uploaded.
- `credentials`: (`oauth2client.service_account.ServiceAccountCredentials`): Credentials for authenticating with the Google Sheets API.
- `client`: (gspread.Client): Authorized client for interacting with the Google Sheets API.
- `worksheet`: (Worksheet): The `gspread.Worksheet` object representing the target sheet.
- `create_sheet`: (bool):  A flag indicating whether a new sheet should be created if it doesn't exist. (Implied, not explicitly a member variable)


**Methods**:

#### `__init__`

**Description**: Initializes the `SpreadSheet` object with the spreadsheet ID, name, and sheet name. It also handles creating a new spreadsheet if the `spreadsheet_id` is `None`.

**Parameters**:
- `spreadsheet_id` (str): The ID of the Google Sheet spreadsheet.  Specify `None` to create a new spreadsheet.
- `spreadsheet_name` (str): Name of the new spreadsheet if `spreadsheet_id` is not specified.
- `sheet_name` (str): Name of the sheet in Google Sheets.

**Raises**:
- `gspread.exceptions.SpreadsheetNotFound`: If the specified spreadsheet does not exist.


#### `_create_credentials`

**Description**: Creates Google Sheets API credentials from a JSON key file.

**Returns**:
- `oauth2client.service_account.ServiceAccountCredentials`: The created credentials.

**Raises**:
- `Exception`: Any error during credential creation.


#### `_authorize_client`

**Description**: Authorizes the client to access the Google Sheets API using the provided credentials.

**Returns**:
- `gspread.Client`: The authorized client object.

**Raises**:
- `Exception`: Any error during authorization.


#### `get_worksheet`

**Description**: Retrieves a worksheet by name.  If the worksheet doesn't exist, it raises an exception unless `create_if_not_present` is set (implied, not explicitly a member).

**Parameters**:
- `worksheet_name` (str | Worksheet): Name of the sheet in Google Sheets.
- `create_if_not_present` (bool, optional): Flag to create a new sheet if it does not exist. Defaults to `False`.

**Returns**:
- `Worksheet | None`: The worksheet object, or `None` if an error occurs.

**Raises**:
- `gspread.exceptions.WorksheetNotFound`: If the worksheet does not exist and `create_if_not_present` is `False`.


#### `create_worksheet`

**Description**: Creates a new worksheet with the specified title and dimensions.

**Parameters**:
- `title` (str): The title of the new worksheet.
- `dim` (dict, optional): A dictionary specifying the dimensions (rows, cols). Defaults to 100 rows and 10 columns.


**Returns**:
- `Worksheet`: The newly created worksheet, or `None` if an error occurs.

**Raises**:
- `Exception`: Any error during worksheet creation.


#### `copy_worksheet`

**Description**: Copies a worksheet to a new worksheet. (Placeholder, implementation incomplete)

**Parameters**:
- `from_worksheet` (str): The name of the worksheet to copy.
- `to_worksheet` (str): The name of the new worksheet.


**Raises**:
- `Exception`:  Any error during worksheet copying.



#### `upload_data_to_sheet`

**Description**: Uploads data from a CSV file to a Google Sheet.

**Raises**:
- `ValueError`: If the `data_file` is not set or doesn't exist.
- `Exception`: Any other error during the upload process.