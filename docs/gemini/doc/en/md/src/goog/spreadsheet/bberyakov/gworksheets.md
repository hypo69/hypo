# gworksheets.py

## Overview

This module provides a class `GWorksheet` for managing Google Sheets worksheets. It inherits from the `Worksheet` class and handles worksheet creation, access, and formatting.  It utilizes the `GSRender` class for formatting and rendering operations.  Crucially, it integrates with the `global_settingspread` module for spreadsheet interaction.


## Classes

### `GWorksheet`

**Description**: This class represents a Google Sheet worksheet and provides methods for interacting with it.  It extends functionality of the base `Worksheet` class.

**Inheritances**: Implements `Worksheet`.


**Methods**

#### `__init__`

**Description**: Initializes a `GWorksheet` object.

**Parameters**:
- `self`: The instance of the `GWorksheet` class.
- `sh`: The spreadsheet object.
- `ws_title` (str = 'new'): The title of the worksheet. Defaults to 'new' for creating a new sheet.
- `rows` (optional): Number of rows for the worksheet. Defaults to `None`.
- `cols` (optional): Number of columns for the worksheet. Defaults to `None`.
- `direcion` (str = 'rtl'): Worksheet text direction. Defaults to 'rtl'.
- `wipe_if_exist` (bool = True):  If True, existing data in the worksheet is cleared.


**Returns**:
- `None`


#### `get`

**Description**: Creates or retrieves a worksheet from a spreadsheet object (`sh`).

**Parameters**:
- `self`: The instance of the `GWorksheet` class.
- `sh`: The spreadsheet object.
- `ws_title` (str = 'new'): The title of the worksheet.
- `rows` (int = 100): Number of rows in the worksheet. Defaults to 100.
- `cols` (int = 100): Number of columns in the worksheet. Defaults to 100.
- `direction` (str = 'rtl'): Text direction for the worksheet. Defaults to 'rtl'.
- `wipe_if_exist` (bool = True): If True, existing data is wiped before creating/retrieving the worksheet.

**Returns**:
- `None`


**Details**:
- If `ws_title` is 'new', a new worksheet is created.
- If `ws_title` exists, it retrieves the existing worksheet.
- If `wipe_if_exist` is True, the existing worksheet data is cleared.


#### `header`

**Description**: Sets the header for the worksheet.

**Parameters**:
- `self`: The instance of the `GWorksheet` class.
- `world_title` (str): The title of the header.
- `range` (str = 'A1:Z1'): The range to apply the header. Defaults to the range A1 to Z1.
- `merge_type` (str ('MERGE_ALL') | str ('MERGE_COLUMNS') | str ('MERGE_ROWS') = 'MERGE_ALL'): The merge type for the header cells. Defaults to 'MERGE_ALL'.

**Returns**:
- `None`


#### `category`

**Description**: Writes a category title to the worksheet.


**Parameters**:
- `self`: The instance of the `GWorksheet` class.
- `ws_category_title`: The category title to write.

**Returns**:
- `None`


#### `direction`

**Description**: Sets the text direction of the worksheet.

**Parameters**:
- `self`: The instance of the `GWorksheet` class.
- `direction` (str = 'rtl'): The desired text direction. Defaults to 'rtl'.

**Returns**:
- `None`


## Functions

(None in this file)


## Modules

- `global_settingspread`
- `goog.grender`


## Notes

- Comments within the code are incomplete.  More detailed documentation is needed.
- The code uses `sh.gsh` which suggests an internal structure.  More context about this structure would be beneficial.
- The `...` in the `__init__` method indicates missing code, and complete implementation details are absent.