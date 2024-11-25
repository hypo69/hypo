```markdown
# hypotez/src/goog/spreadsheet/bberyakov/grender.py

## Overview

This module provides a class `GSRender` for rendering Google Sheets. It handles formatting, merging cells, setting worksheet direction, and adding headers and category titles.  It also includes utility functions for determining the first empty row and working with colors and formatting.

## Classes

### `GSRender`

**Description**: This class encapsulates methods for rendering Google Sheets. It provides methods for formatting headers, merging cells, setting worksheet direction, and writing content into worksheets.

**Methods**:

#### `__init__`

**Description**: Initializes the `GSRender` object.  The code currently contains an ellipsis (`...`) indicating that some internal schema loading functionality is likely missing and needs to be documented.


**Parameters**:

- `*args`: Variable positional arguments.
- `**kwards`: Arbitrary keyword arguments.

**Returns**:

- `None`:  The function does not return a value.


#### `render_header`

**Description**: Renders the header of a Google Sheet worksheet.  This method formats the header cells with specified colors, alignment, and boldness. It also merges cells based on the `merge_type`.


**Parameters**:

- `self`: Instance of the `GSRender` class.
- `ws` (Worksheet): The worksheet object to render the header in.
- `world_title` (str): The title of the Google Sheet.
- `range` (str, optional): The range of cells to format (default is 'A1:Z1').
- `merge_type` (str, optional): The type of cell merging ('MERGE_ALL', 'MERGE_COLUMNS', 'MERGE_ROWS', default is 'MERGE_ALL').


**Returns**:

- `None`: The function does not return a value.


#### `merge_range`

**Description**: Merges cells in a worksheet based on the specified `merge_type`.

**Parameters**:

- `self`: Instance of the `GSRender` class.
- `ws` (Worksheet): The worksheet object to merge cells in.
- `range` (str): The range of cells to merge.
- `merge_type` (str, optional): The type of cell merging ('MERGE_ALL', 'MERGE_COLUMNS', 'MERGE_ROWS', default is 'MERGE_ALL').

**Returns**:

- `None`: The function does not return a value.

#### `set_worksheet_direction`

**Description**: Updates the direction of the worksheet to either left-to-right ('ltr') or right-to-left ('rtl').

**Parameters**:

- `self`: Instance of the `GSRender` class.
- `sh` (Spreadsheet): The spreadsheet object containing the worksheet.
- `ws` (Worksheet): The worksheet to update.
- `direction` (str, optional): The direction ('ltr' or 'rtl', default is 'rtl').

**Returns**:

- `None`: The function does not return a value.


#### `header`

**Description**: Adds a header row to the worksheet.


**Parameters**:

- `self`: Instance of the `GSRender` class.
- `ws` (Worksheet): The worksheet object to add the header to.
- `ws_header` (str | list): The header content (either a single string or a list of strings).
- `row` (int, optional): The row number to insert the header (default is the next empty row).

**Returns**:

- `None`: The function does not return a value.


#### `write_category_title`

**Description**: Adds a category title row to the worksheet.

**Parameters**:

- `self`: Instance of the `GSRender` class.
- `ws` (Worksheet): The worksheet object to add the category title to.
- `ws_category_title` (str | list): The category title content (either a single string or a list of strings).
- `row` (int, optional): The row number to insert the category title (default is the next empty row).

**Returns**:

- `None`: The function does not return a value.



#### `get_first_empty_row`

**Description**: Determines the first empty row in a worksheet.

**Parameters**:

- `self`: Instance of the `GSRender` class.
- `ws` (Worksheet): The worksheet object to check.
- `by_col` (int, optional): Optional column number to search for the first empty cell. If `None`, searches for the first empty cell in the last column.

**Returns**:

- `int`: The row number of the first empty row.


## Functions


**(Note:  No functions are found in the code other than those part of the GSRender class.)**


## Modules/Libraries used

- json
- typing
- gspread_formatting
- gspread
- goog.helpers
- gspread.utils
- src.helpers
- spread_formatting
- spread
-  src.gs