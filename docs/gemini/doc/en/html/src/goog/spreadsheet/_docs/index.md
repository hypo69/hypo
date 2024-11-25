html
<h1>Module: src.goog.spreadsheet._docs</h1>

<h2>Overview</h2>
<p>This module provides documentation for interacting with Google Spreadsheets using the v4 API.  It includes a wrapper class, <code>Spreadsheet</code>, to simplify common tasks.</p>

<h2>Classes</h2>

<h3><code>Spreadsheet</code></h3>

<p><strong>Description</strong>: A wrapper class for interacting with Google Sheets. This class simplifies batch operations and provides methods for setting column widths, merging cells, formatting cells, and setting values.</p>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__(credentials_file: str, spreadsheet_id: str = None, sheet_id: int = 0, sheet_title: str = None)</code>: Initializes the <code>Spreadsheet</code> object with credentials, spreadsheet ID, and sheet ID. Defaults to sheet 0 if not specified.</li>
  <li><code>prepare_setColumnWidth(col: int, width: int)</code>: Prepares a request to set the width of a specific column.</li>
  <li><code>prepare_setColumnsWidth(startCol: int, endCol: int, width: int)</code>: Prepares a request to set the width of multiple columns.</li>
  <li><code>prepare_mergeCells(range_str: str)</code>: Prepares a request to merge cells in the specified range (A1 notation).</li>
  <li><code>prepare_setCellsFormat(range_str: str, format_dict: dict)</code>: Prepares a request to format cells in the specified range.</li>
    <li><code>prepare_setCellsFormats(range_str: str, format_list: list)</code>: Prepares a request to format cells in the specified range, with per-cell formatting.</li>
  <li><code>prepare_setValues(cells_range: str, values: list, major_dimension: str = 'ROWS')</code>: Prepares a request to set values in the specified range.</li>
    <li><code>prepare_setDimensionPixelSize(dimension: str, startIndex: int, endIndex: int, pixelSize: int)</code>: Prepares a request to set the pixel size of a dimension.</li>
  <li><code>runPrepared(value_input_option: str = 'USER_ENTERED')</code>: Executes all prepared requests in a batch.</li>
  <li><code>toGridRange(range_str: str, sheet_id: int = 0) -> dict</code>: Converts an A1-notation range to a <code>GridRange</code> dictionary.</li>
</ul>

<h2>Functions</h2>

<!-- (No functions are directly defined in the provided code snippet, so this section is empty) -->


<h2>Example Usage (Illustrative)</h2>
<p>This example demonstrates setting column widths and setting values using the <code>Spreadsheet</code> class:</p>
<pre><code>python
# Example usage (Illustrative)
# ... import necessary modules ...

# ... (Spreadsheet class initialization) ...

ss.prepare_setColumnWidth(0, 317)
ss.prepare_setColumnWidth(1, 200)
ss.prepare_setColumnsWidth(2, 3, 165)
ss.prepare_setColumnWidth(4, 100)

ss.prepare_setValues("B2:C3", [
    ["This is B2", "This is C2"],
    ["This is B3", "This is C3"]
])

ss.runPrepared()
</code></pre>


<p>Please refer to the Google Sheets API v4 documentation for further details on available methods and parameters.</p>