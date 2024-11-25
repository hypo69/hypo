html
<h1>grender.py</h1>

<h2>Overview</h2>
<p>This module provides functions for rendering Google Sheets, including formatting cells, merging ranges, and setting worksheet properties. It handles various aspects of Google Sheet styling and data manipulation. It relies on the gspread library for interacting with Google Sheets.</p>

<h2>Classes</h2>

<h3><code>GSRender</code></h3>

<p><strong>Description</strong>: The <code>GSRender</code> class handles the rendering and styling of Google Sheets.</p>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__(*args, **kwards)</code>:
    <p><strong>Description</strong>: Initializes the <code>GSRender</code> object.  (Placeholder - specifics not detailed in code).</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>*args</code>: Variable positional arguments.</li>
      <li><code>**kwards</code>: Keyword arguments.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>None</code>: No explicit return value.</li>
    </ul>
  </li>
  <li><code>render_header(ws: Worksheet, world_title: str, range: str = 'A1:Z1', merge_type: str('MERGE_ALL') | str('MERGE_COLUMNS') | str('MERGE_ROWS') = 'MERGE_ALL') -> None</code>:
    <p><strong>Description</strong>: Renders the header of a worksheet.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>ws</code> (Worksheet): The worksheet object to render the header on.</li>
      <li><code>world_title</code> (str): The title of the Google Sheet.</li>
      <li><code>range</code> (str, optional): The cell range to format. Defaults to 'A1:Z1'.</li>
      <li><code>merge_type</code> (str('MERGE_ALL') | str('MERGE_COLUMNS') | str('MERGE_ROWS'), optional): The type of merge to apply. Defaults to 'MERGE_ALL'.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>None</code>: No explicit return value.</li>
    </ul>
  </li>
  <li><code>merge_range(ws: Worksheet, range: str, merge_type: str('MERGE_ALL') | str('MERGE_COLUMNS') | str('MERGE_ROWS') = 'MERGE_ALL') -> None</code>:
    <p><strong>Description</strong>: Merges cells in a specified range.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>ws</code> (Worksheet): The worksheet object to modify.</li>
      <li><code>range</code> (str): The cell range to merge.</li>
      <li><code>merge_type</code> (str('MERGE_ALL') | str('MERGE_COLUMNS') | str('MERGE_ROWS'), optional): The type of merge to apply. Defaults to 'MERGE_ALL'.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>None</code>: No explicit return value.</li>
    </ul>
  </li>
  <li><code>set_worksheet_direction(sh: Spreadsheet, ws: Worksheet, direction: str('ltr') | str('rtl') = 'rtl')</code>:
    <p><strong>Description</strong>: Sets the direction of the worksheet.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>sh</code> (Spreadsheet): The spreadsheet object.</li>
      <li><code>ws</code> (Worksheet): The worksheet object to modify.</li>
      <li><code>direction</code> (str('ltr') | str('rtl'), optional): The direction to set. Defaults to 'rtl'.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>None</code>: No explicit return value.</li>
    </ul>
    </li>
   <li><code>header(self, ws: Worksheet, ws_header: str | list, row: int = None)</code>:
    <p><strong>Description</strong>: Appends and formats header row(s).</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
    <li><code>ws</code> (Worksheet): The worksheet to append to.</li>
    <li><code>ws_header</code> (str | list): Header data.</li>
    <li><code>row</code> (int, optional): Row number for the header.</li>
    </ul>
    <p><strong>Returns</strong>:</p><ul>
      <li><code>None</code>: No explicit return value.</li>
    </ul>
  </li>
  <li><code>write_category_title(self, ws: Worksheet, ws_category_title: str | list, row: int = None)</code>
    <p><strong>Description</strong>: Appends and formats a category title row. (Placeholder)</p>
  </li>
   <li><code>get_first_empty_row(self, ws: Worksheet, by_col: int = None) -> int</code>:
    <p><strong>Description</strong>: Finds the first empty row in the worksheet.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>ws</code> (Worksheet): The worksheet object.</li>
      <li><code>by_col</code> (int, optional): Optional column to search for the last filled cell.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>int</code>: The row number of the first empty row.</li>
    </ul>
  </li>
</ul>


<h2>Functions</h2>
<p> (No functions documented separately from classes in this file)</p>