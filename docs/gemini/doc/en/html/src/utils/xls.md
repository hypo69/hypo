html
<h1>hypotez/src/utils/xls.py</h1>

<h2>Overview</h2>
<p>This module provides functions for converting Excel (`.xls`) files to JSON and vice-versa, handling multiple sheets and error conditions.</p>

<h2>Constants</h2>

<h3><code>MODE</code></h3>

<p><strong>Description</strong>: Stores a string representing the current mode (e.g., 'dev').</p>


<h2>Functions</h2>

<h3><code>read_xls_as_dict</code></h3>

<p><strong>Description</strong>: Reads an Excel file and converts it to JSON. Optionally converts a specific sheet and saves the result to a JSON file. Handles errors gracefully.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>xls_file</code> (str): Path to the input Excel file.</li>
  <li><code>json_file</code> (str, optional): Path to save the output JSON file. Defaults to <code>None</code>.</li>
  <li><code>sheet_name</code> (Union[str, int], optional): Name or index of the sheet to convert. Defaults to <code>None</code>. If <code>None</code>, all sheets are processed.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Union[Dict, List[Dict], bool]</code>:
    <ul>
      <li>A dictionary where keys are sheet names and values are lists of dictionaries representing the data if successful.
      </li>
      <li>A list of dictionaries for a single sheet, if only a single sheet is processed.</li>
      <li><code>False</code> if an error occurs (e.g., file not found, error processing sheet).</li>
    </ul>
  </li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>FileNotFoundError</code>: If the input Excel file does not exist.</li>
  <li>Other exceptions: If any other error occurs during file processing.</li>
</ul>


<h3><code>save_xls_file</code></h3>

<p><strong>Description</strong>: Saves JSON data to an Excel file. The data should be a dictionary where keys are sheet names and values are lists of dictionaries representing rows. Handles errors gracefully.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>data</code> (Dict[str, List[Dict]]): The JSON data to save. Keys are sheet names, values are lists of dictionaries.</li>
  <li><code>file_path</code> (str): Path to the output Excel file.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>bool</code>: <code>True</code> if the save operation is successful, <code>False</code> otherwise.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li>Other exceptions: If any error occurs during the save operation.</li>
</ul>