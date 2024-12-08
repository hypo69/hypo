# gspreadsheet.py

## Overview

This module provides a class for interacting with Google Sheets. It utilizes the `gspread` library to manage spreadsheets, including creating, retrieving, and potentially modifying them.  It leverages service account authentication.


## Table of Contents

* [GSpreadsheet](#gspreadsheet)
    * [__init__](#__init__)
    * [get_project_spreadsheets_dict](#get_project_spreadsheets_dict)
    * [get_by_title](#get_by_title)
    * [get_by_id](#get_by_id)
    * [get_all_spreadsheets_for_current_account](#get_all_spreadsheets_for_current_account)


## Classes

### `GSpreadsheet`

**Description**: This class extends the `Spreadsheet` class, providing methods for interacting with Google Sheets.  It handles opening, creating, and retrieving spreadsheets.

**Inheritances**: Implements `Spreadsheet` (description needed).

**Attributes**:
- `gsh`: `Spreadsheet` object representing the currently opened Google Sheet.


**Methods**:

#### `__init__`

**Description**: Initializes the `GSpreadsheet` object.

**Parameters**:
- `s_id` (str, optional): The ID of the spreadsheet to open. Defaults to `None`.
- `s_title` (str, optional): The title of the spreadsheet to open. Defaults to `None`.
- `*args`:  Variable positional arguments.
- `**kwards`: Variable keyword arguments.


**Raises**:


#### `get_project_spreadsheets_dict`

**Description**: Retrieves project spreadsheets as a dictionary.

**Parameters**:
- `self` : The `GSpreadsheet` object.


**Returns**:
- `dict`: A dictionary representing project spreadsheets.


**Raises**:


#### `get_by_title`

**Description**: Retrieves or creates a spreadsheet by its title.

**Parameters**:
- `self`: The `GSpreadsheet` object.
- `sh_title` (str, optional): The title of the spreadsheet. Defaults to `'New Spreadsheet'`.


**Raises**:


#### `get_by_id`

**Description**: Retrieves a spreadsheet by its ID.

**Parameters**:
- `self`: The `GSpreadsheet` object.
- `sh_id` (str): The ID of the spreadsheet to open.


**Returns**:
- `Spreadsheet`: The retrieved spreadsheet object.


**Raises**:


#### `get_all_spreadsheets_for_current_account`

**Description**: Retrieves all spreadsheets for the current account.

**Parameters**:
- `self`: The `GSpreadsheet` object.


**Returns**:


**Raises**: