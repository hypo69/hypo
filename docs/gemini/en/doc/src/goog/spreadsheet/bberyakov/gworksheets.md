# gworksheets.py

## Overview

This module provides a class `GWorksheet` for managing Google Sheets worksheets.  It inherits from the `Worksheet` class and offers functionalities for creating, accessing, and manipulating worksheets within a spreadsheet.  It integrates with `GSRender` for formatting and presentation.


## Classes

### `GWorksheet`

**Description**: This class extends the `Worksheet` class to provide specific methods for interacting with Google Sheets worksheets. It handles worksheet creation, retrieval, clearing, and setting the direction (e.g., RTL).

**Inheritances**:
- Implements `Worksheet`:  Provides a way to work with spreadsheet data.


**Methods**:

#### `__init__`

**Description**: Initializes a `GWorksheet` object.

**Parameters**:
- `self`: The instance of the `GWorksheet` object.
- `sh`: The spreadsheet object containing the worksheet.
- `ws_title` (str = 'new'): The title of the worksheet. Defaults to 'new' for creating a new worksheet.
- `rows` (Optional[int], optional): The number of rows in the worksheet. Defaults to `None`.
- `cols` (Optional[int], optional): The number of columns in the worksheet. Defaults to `None`.
- `direcion` (str = 'rtl'): The text direction for the worksheet (e.g., 'rtl' for right-to-left). Defaults to 'rtl'.
- `wipe_if_exist` (bool = True): Whether to wipe existing data in the worksheet if the title already exists. Defaults to `True`.
- `*args`:  Variable positional arguments.
- `**kwards`: Variable keyword arguments.

**Returns**:
- `None`:  This method doesn't explicitly return a value.

#### `get`

**Description**: Creates or retrieves a worksheet.  If a worksheet with the specified title already exists, it optionally clears the existing data.

**Parameters**:
- `self`: The instance of the `GWorksheet` object.
- `sh`: The spreadsheet object to interact with.
- `ws_title` (str = 'new'): The title of the worksheet. Defaults to 'new'.
- `rows` (int = 100): The number of rows to create/retrieve.
- `cols` (int = 100): The number of columns to create/retrieve.
- `direction` (str = 'rtl'): The text direction for the worksheet. Defaults to 'rtl'.
- `wipe_if_exist` (bool = True): Whether to clear the worksheet if it already exists. Defaults to `True`.


**Returns**:
- `None`:  This method doesn't explicitly return a value.

**Raises**:

- `ValueError`: if `ws_title` isn't a valid string value.
- `AttributeError`: If a critical object `sh` is missing attributes


#### `header`

**Description**: Adds a header to the worksheet.

**Parameters**:
- `self`: The instance of the `GWorksheet` object.
- `world_title` (str): The title of the header.
- `range` (str = 'A1:Z1'): The range to apply the header in.
- `merge_type` (str('MERGE_ALL') | str('MERGE_COLUMNS') | str('MERGE_ROWS') = 'MERGE_ALL'): Specifies how cells should be merged. Defaults to merging all cells in the specified range.

**Returns**:
- `None`: This method doesn't explicitly return a value.


#### `category`

**Description**: Writes a category title to the worksheet.

**Parameters**:
- `self`: The instance of the `GWorksheet` object.
- `ws_category_title`: The title of the category to be written.


**Returns**:
- `None`: This method doesn't explicitly return a value.


#### `direction`

**Description**: Sets the text direction of the worksheet.

**Parameters**:
- `self`: The instance of the `GWorksheet` object.
- `direction` (str = 'rtl'): The text direction for the worksheet (e.g., 'rtl'). Defaults to 'rtl'.

**Returns**:
- `None`: This method doesn't explicitly return a value.


## Functions

(None in this file)