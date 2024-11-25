# gspreadsheet.py

## Overview

This module provides a class for interacting with Google Sheets. It allows for creating, accessing, and managing Google Sheets using the `gspread` library.  The class inherits from a base `Spreadsheet` class (defined elsewhere).

## Classes

### `GSpreadsheet`

**Description**: This class encapsulates interactions with a Google Sheet.  It handles authentication, retrieving sheets by ID or title, and other related operations.

**Inheritances**:
- Implements `Spreadsheet`

**Attributes**:
- `gsh`:  A `Spreadsheet` object representing the currently active Google Sheet.
- `gclient`: A `gspread.client` object for interacting with the Google Sheets API.

**Methods**:

#### `__init__`

**Description**: Initializes a `GSpreadsheet` object.

**Parameters**:
- `self`: The instance of the `GSpreadsheet` class.
- `s_id` (str, optional): The ID of the Google Sheet to open. Defaults to None.
- `s_title` (str, optional): The title of the Google Sheet to open. Defaults to None.
- `*args`:  Variable positional arguments.
- `**kwards`:  Variable keyword arguments.

**Raises**:
-  None

#### `get_project_spreadsheets_dict`

**Description**: Retrieves a dictionary of project spreadsheets.

**Parameters**:
- `self`: The instance of the `GSpreadsheet` class.

**Returns**:
- `dict`: A dictionary containing information about the spreadsheets.

#### `get_by_title`

**Description**: Opens or creates a Google Sheet based on its title.

**Parameters**:
- `self`: The instance of the `GSpreadsheet` class.
- `sh_title` (str, optional): The title of the spreadsheet. Defaults to 'New Spreadsheet'.


**Raises**:
-  None

#### `get_by_id`

**Description**: Opens a Google Sheet based on its ID.

**Parameters**:
- `self`: The instance of the `GSpreadsheet` class.
- `sh_id` (str): The ID of the spreadsheet to open.

**Returns**:
- `Spreadsheet`: The opened Google Sheet object.

**Raises**:
- None

#### `get_all_spreadsheets_for_current_account`

**Description**: Retrieves all spreadsheets associated with the current account.

**Parameters**:
- `self`: The instance of the `GSpreadsheet` class.

**Returns**:
-  None (implicitly returns the list of spreadsheets).

**Raises**:
- None


## Functions

**(None)**

## Modules

**(None)**