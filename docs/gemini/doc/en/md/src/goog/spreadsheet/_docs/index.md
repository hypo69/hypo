# hypotez/src/goog/spreadsheet/_docs

## Overview

This module provides a Python class (`Spreadsheet`) for interacting with Google Sheets API v4.  It encapsulates the process of creating, updating, and accessing spreadsheets, including managing column widths, cell formatting, and data input.


## Classes

### `Spreadsheet`

**Description**: This class acts as a wrapper around the Google Sheets API v4, simplifying interaction with spreadsheets. It handles batch updates and provides methods for various spreadsheet operations.


**Methods**:

- `__init__(spreadsheet_id: str, credentials_file: str, sheet_id: int = 0, sheet_title: str = 'Sheet 1') -> None`:
    **Description**: Initializes the Spreadsheet object.
    **Parameters**:
        - `spreadsheet_id` (str): The ID of the Google Sheet to access.
        - `credentials_file` (str): The path to the service account JSON key file.
        - `sheet_id` (int, optional): The ID of the sheet to work with. Defaults to 0 (first sheet).
        - `sheet_title` (str, optional): The name of the sheet. Defaults to 'Sheet 1'.
    **Raises**:
        - `ValueError`: If input parameters are invalid.



- `prepare_setColumnWidth(col_index: int, width: int) -> None`:
    **Description**: Prepares a request to update the width of a specified column.
    **Parameters**:
        - `col_index` (int): The index of the column to update (zero-based).
        - `width` (int): The desired width of the column in pixels.


- `prepare_setColumnsWidth(start_col: int, end_col: int, width: int) -> None`:
    **Description**: Prepares a request to update the width of multiple columns.
    **Parameters**:
        - `start_col` (int): The index of the first column to update (zero-based).
        - `end_col` (int): The index of the last column to update (zero-based).
        - `width` (int): The desired width of the columns in pixels.

- `prepare_mergeCells(range_string: str) -> None`:
    **Description**: Prepares a request to merge cells in the specified range.
    **Parameters**:
        - `range_string` (str): The range to merge in A1 notation (e.g., "A1:E1").


- `prepare_setCellsFormat(range_string: str, format_dict: dict, fields: str = 'userEnteredFormat') -> None`:
     **Description**: Prepares a request to set the format of cells in a given range.
     **Parameters**:
          - `range_string` (str): The range of cells to format in A1 notation (e.g., "A1:E1").
          - `format_dict` (dict): A dictionary defining the cell format properties (e.g., horizontal alignment, bold text).
          - `fields` (str, optional):  The fields to update in the format. Defaults to 'userEnteredFormat'.



- `prepare_setValues(cells_range: str, values: list, major_dimension: str = 'ROWS') -> None`:
    **Description**: Prepares a request to set values in a specified range.
    **Parameters**:
        - `cells_range` (str): The range of cells to set values in (A1 notation).
        - `values` (list): A list of lists representing the values to insert.
        - `major_dimension` (str, optional):  The dimension to insert values into (e.g., 'ROWS' or 'COLUMNS').


- `runPrepared(value_input_option: str = 'USER_ENTERED') -> tuple`:
    **Description**: Executes all prepared requests (column width, merge cells, set values) in a batch update to the spreadsheet.
    **Parameters**:
        - `value_input_option` (str, optional): The option for how values are interpreted (e.g., 'USER_ENTERED', 'RAW'). Defaults to 'USER_ENTERED'.
    **Returns**:
        tuple: A tuple containing the results of the batch updates.


## Functions

(None found in the provided code)