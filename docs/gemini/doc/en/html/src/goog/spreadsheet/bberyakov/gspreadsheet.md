html
<h1>gspreadsheet.py</h1>

<h2>Overview</h2>
<p>This module provides a class for interacting with Google Sheets using the gspread library. It handles authentication, spreadsheet creation, retrieval, and manipulation.</p>

<h2>Classes</h2>

<h3><code>GSpreadsheet</code></h3>

<p><strong>Description</strong>: This class represents a Google Sheet and provides methods for interacting with it.</p>

<p><strong>Inheritances</strong>:</p>
<ul>
  <li>Implements <code>Spreadsheet</code>: [description]</li>
</ul>

<p><strong>Attributes</strong>:</p>
<ul>
  <li><code>gsh</code> (<code>Spreadsheet</code>): The currently opened Google Sheet.  Initialized to <code>None</code>.</li>
  <li><code>gclient</code> (<code>gspread.client</code>): The gspread client object.</li>
</ul>

<p><strong>Methods</strong>:</p>

<h4><code>__init__</code></h4>

<p><strong>Description</strong>: Initializes a <code>GSpreadsheet</code> object.  It can open an existing spreadsheet by ID or title.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>s_id</code> (str, optional): The ID of the spreadsheet to open. Defaults to <code>None</code>.</li>
  <li><code>s_title</code> (str, optional): The title of the spreadsheet to open. Defaults to <code>None</code>.</li>
  <li><code>*args</code>:  Variadic positional arguments.</li>
  <li><code>**kwards</code>: Keyword arguments.</li>
</ul>

<p><strong>Example Usage</strong>:</p>
<pre><code>python
# Example usage (assuming you have the necessary setup)
spreadsheet = GSpreadsheet(s_id='1ZcK74BCgWKVr4kODjPmSvjp5IyO0OxhXdbeHKWzLQiM')
</code></pre>

<h4><code>get_project_spreadsheets_dict</code></h4>

<p><strong>Description</strong>: Retrieves a dictionary representing the project's spreadsheets.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>self</code>: The <code>GSpreadsheet</code> object itself.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>dict</code>: A dictionary representing the project's spreadsheets. It loads the data from <code>goog\\spreadsheets.json</code>.</li>
</ul>

<h4><code>get_by_title</code></h4>

<p><strong>Description</strong>: Opens or creates a Google Sheet based on its title.  If the spreadsheet exists, it opens it; otherwise, it creates a new one and shares it.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>self</code>: The <code>GSpreadsheet</code> object itself.</li>
  <li><code>sh_title</code> (str, optional): The title of the spreadsheet. Defaults to 'New Spreadsheet'.</li>
</ul>


<h4><code>get_by_id</code></h4>

<p><strong>Description</strong>: Opens a Google Sheet based on its ID.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>self</code>: The <code>GSpreadsheet</code> object itself.</li>
  <li><code>sh_id</code> (str): The ID of the spreadsheet.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Spreadsheet</code>: The opened Google Sheet.</li>
</ul>

<h4><code>get_all_spreadsheets_for_current_account</code></h4>

<p><strong>Description</strong>: Retrieves all spreadsheets for the current account.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>self</code>: The <code>GSpreadsheet</code> object itself.</li>
</ul>

<h2>Functions</h2>

<!-- (No functions in the input code to document) -->


<h2>Exceptions</h2>

<!-- (No exceptions in the input code to document) -->