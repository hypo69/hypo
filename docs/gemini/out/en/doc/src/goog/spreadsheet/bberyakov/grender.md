# hypotez/src/goog/spreadsheet/bberyakov/grender.py

## Overview

This module provides functionality for rendering Google Spreadsheet data. It includes a `GSRender` class for formatting and manipulating worksheets, including header formatting, merging cells, setting worksheet direction, and appending data.  It leverages the `gspread` and `gspread-formatting` libraries for interacting with Google Sheets.  Error handling and logging are integrated.

## Table of Contents

* [Classes](#classes)
    * [GSRender](#gsrender)
* [Functions](#functions)
    * [render_header](#render_header)
    * [merge_range](#merge_range)
    * [set_worksheet_direction](#set_worksheet_direction)
    * [header](#header)
    * [write_category_title](#write_category_title)
    * [get_first_empty_row](#get_first_empty_row)


## Classes

### `GSRender`

**Description**: The `GSRender` class encapsulates methods for rendering and manipulating Google Sheets.  It's designed to work with existing Spreadsheet and Worksheet objects.

**Attributes**:

- `render_schemas`: A dictionary likely containing rendering schemas.  Details on the format are not available from the provided code.


**Methods**:

- `__init__(*args, **kwards)`:
    **Description**: Initializes the `GSRender` instance.
    **Parameters**:
        - `*args`: Variable positional arguments.
        - `**kwards`: Variable keyword arguments.
    **Returns**:
        - `None`: No return value.

- `render_header(ws: Worksheet, world_title: str, range: str = 'A1:Z1', merge_type: str('MERGE_ALL') | str('MERGE_COLUMNS') | str('MERGE_ROWS') = 'MERGE_ALL') -> None`:
    **Description**: Renders the header of a worksheet.
    **Parameters**:
        - `ws` (Worksheet): The worksheet to render the header on.
        - `world_title` (str): The title of the Google Sheet.
        - `range` (str, optional): The range of cells to format. Defaults to 'A1:Z1'.
        - `merge_type` (str('MERGE_ALL') | str('MERGE_COLUMNS') | str('MERGE_ROWS'), optional): Specifies how cells should be merged. Defaults to 'MERGE_ALL'.
    **Returns**:
        - `None`: No return value.
    **Raises**:
        - `ValueError`: If invalid `merge_type` is given.
- `merge_range(ws: Worksheet, range: str, merge_type: str('MERGE_ALL') | str('MERGE_COLUMNS') | str('MERGE_ROWS') = 'MERGE_ALL') -> None`:
    **Description**: Merges cells in a specified range within the worksheet.
    **Parameters**:
        - `ws` (Worksheet): The worksheet to merge cells in.
        - `range` (str): The range of cells to merge.
        - `merge_type` (str, optional): The type of merge operation. Defaults to 'MERGE_ALL'. Valid types are 'MERGE_ALL', 'MERGE_COLUMNS', 'MERGE_ROWS'.
    **Returns**:
        - `None`: No return value.
    **Raises**:
        - `ValueError`: If invalid `merge_type` is given.

- `set_worksheet_direction(sh: Spreadsheet, ws: Worksheet, direction: str('ltr') | str('rtl') = 'rtl')`:
    **Description**: Sets the direction of the worksheet to left-to-right or right-to-left.
    **Parameters**:
        - `sh` (Spreadsheet): The spreadsheet object.
        - `ws` (Worksheet): The worksheet to modify.
        - `direction` (str, optional): The direction of the sheet, either 'ltr' or 'rtl'. Defaults to 'rtl'.
    **Returns**:
        - `None`: No return value.
        **Raises**:
            - `ValueError`: If invalid `direction` is given.

- `header(ws: Worksheet, ws_header: str | list, row: int = None)`:
    **Description**: Appends a header row to the worksheet.
    **Parameters**:
        - `ws` (Worksheet): The worksheet to append to.
        - `ws_header` (str | list): The header data. Can be a single string or a list of strings.
        - `row` (int, optional): The row number to append to. If `None`, the next available row is used.
    **Returns**:
        - `None`: No return value.

- `write_category_title(ws: Worksheet, ws_category_title: str | list, row: int = None)`:
    **Description**: Appends a category title row to the worksheet.
    **Parameters**:
        - `ws` (Worksheet): The worksheet to append to.
        - `ws_category_title` (str | list): The category title data.
        - `row` (int, optional): The row number to append to. If `None`, the next available row is used.
    **Returns**:
        - `None`: No return value.

- `get_first_empty_row(ws: Worksheet, by_col: int = None) -> int`:
    **Description**: Retrieves the row number of the first empty row in the worksheet, optionally considering a specific column.
    **Parameters**:
        - `ws` (Worksheet): The worksheet to search.
        - `by_col` (int, optional): The column number to check for empty cells. If `None`, searches the entire worksheet.
    **Returns**:
        - `int`: The row number of the first empty row.
    **Raises**:
        - `TypeError`: If input data is not in the expected format.


## Functions

(No standalone functions are found in this module)