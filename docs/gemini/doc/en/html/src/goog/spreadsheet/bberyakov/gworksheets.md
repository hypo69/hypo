html
<h1>Module gworksheets</h1>

<h2>Overview</h2>
<p>This module provides classes and functions for working with Google Sheets, specifically managing worksheets.  It handles creating, retrieving, and manipulating worksheets within a spreadsheet, along with formatting options.</p>

<h2>Classes</h2>

<h3><code>GWorksheet</code></h3>

<p><strong>Description</strong>: This class encapsulates operations related to Google Sheets worksheets. It inherits from the <code>Worksheet</code> class, extending its functionality.</p>

<p><strong>Inheritances</strong>:</p>
<ul>
  <li>Implements <code>Worksheet</code>: Provides foundational worksheet management capabilities.</li>
</ul>


<p><strong>Attributes</strong>:</p>
<ul>
  <li><code>sh</code>:  Represents the spreadsheet object.</li>
  <li><code>ws</code>: The worksheet object.</li>
  <li><code>render</code>: An instance of <code>GSRender</code> for formatting tasks.</li>
</ul>


<p><strong>Methods</strong>:</p>

<h4><code>__init__</code></h4>

<p><strong>Description</strong>: Initializes a <code>GWorksheet</code> object, either creating a new worksheet or retrieving an existing one. It handles various parameters for worksheet configuration.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>self</code>: The instance of the <code>GWorksheet</code> class.</li>
  <li><code>sh</code>: The spreadsheet object to operate on.</li>
  <li><code>ws_title</code> (str = 'new'): The name of the worksheet. Defaults to 'new' for creating a new worksheet.</li>
  <li><code>rows</code> (Optional[int], optional): The number of rows for the worksheet. Defaults to <code>None</code>.</li>
  <li><code>cols</code> (Optional[int], optional): The number of columns for the worksheet. Defaults to <code>None</code>.</li>
  <li><code>direcion</code> (str = 'rtl'): The writing direction of the worksheet. Defaults to 'rtl'.</li>
  <li><code>wipe_if_exist</code> (bool = True): A flag to wipe existing data if a worksheet with the same name exists. Defaults to <code>True</code>.</li>
  <li><code>*args</code>: Additional positional arguments.</li>
  <li><code>**kwards</code>: Additional keyword arguments.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>None</code>: No explicit return value.</li>
</ul>



<h4><code>get</code></h4>

<p><strong>Description</strong>: Creates or retrieves a worksheet from the spreadsheet.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>self</code>: The instance of the <code>GWorksheet</code> class.</li>
  <li><code>sh</code>: The spreadsheet object.</li>
  <li><code>ws_title</code> (str = 'new'): The name of the worksheet.</li>
  <li><code>rows</code> (int = 100): The number of rows.</li>
  <li><code>cols</code> (int = 100): The number of columns.</li>
  <li><code>direction</code> (str = 'rtl'): The writing direction.</li>
  <li><code>wipe_if_exist</code> (bool = True): Flag to wipe existing data.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
<li><code>None</code>: No explicit return value.</li>
</ul>
<p><strong>Raises</strong>:</p>
<ul>
  <li>None</li>
</ul>
<h4><code>header</code></h4>

<p><strong>Description</strong>: Sets the header for the worksheet.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>self</code>: The instance of the <code>GWorksheet</code> class.</li>
  <li><code>world_title</code> (str): The title of the header.</li>
  <li><code>range</code> (str = 'A1:Z1'): The cell range for the header.</li>
  <li><code>merge_type</code> (str('MERGE_ALL') | str('MERGE_COLUMNS') | str('MERGE_ROWS') = 'MERGE_ALL'): The merge type for the header.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>None</code>: No explicit return value.</li>
</ul>

<h4><code>category</code></h4>

<p><strong>Description</strong>: Writes a category title to the worksheet.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>self</code>: The instance of the <code>GWorksheet</code> class.</li>
  <li><code>ws_category_title</code>: The category title to write.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>None</code>: No explicit return value.</li>
</ul>

<h4><code>direction</code></h4>

<p><strong>Description</strong>: Sets the writing direction of the worksheet.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>self</code>: The instance of the <code>GWorksheet</code> class.</li>
  <li><code>direction</code> (str = 'rtl'): The writing direction (e.g., 'rtl', 'ltr').</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>None</code>: No explicit return value.</li>
</ul>

<h2>Functions</h2>

<p>(No functions are found in the given code snippet that do not belong to a class.)</p>