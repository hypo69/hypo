html
<h1>hypotez/src/utils/csv.py</h1>

<h2>Overview</h2>
<p>This module provides utilities for working with CSV and JSON files, including saving CSV data, reading CSV content, and converting CSV to JSON.</p>

<h2>Functions</h2>

<h3><code>save_csv_file</code></h3>

<p><strong>Description</strong>: Saves a list of dictionaries to a CSV file.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>data</code> (List[Dict[str, str]]): List of dictionaries to save.</li>
  <li><code>file_path</code> (Union[str, Path]): Path to the CSV file.</li>
  <li><code>mode</code> (str, optional): File mode ('a' to append, 'w' to overwrite). Defaults to 'a'.</li>
  <li><code>exc_info</code> (bool, optional): Include traceback information in logs. Defaults to True.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>bool</code>: True if successful, otherwise False.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>TypeError</code>: If input data is not a list of dictionaries.</li>
  <li><code>ValueError</code>: If input data is empty.</li>
</ul>


<h3><code>read_csv_file</code></h3>

<p><strong>Description</strong>: Reads CSV content as a list of dictionaries.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>file_path</code> (Union[str, Path]): Path to the CSV file.</li>
  <li><code>exc_info</code> (bool, optional): Include traceback information in logs. Defaults to True.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>List[Dict[str, str]] | None</code>: List of dictionaries or None if failed.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>FileNotFoundError</code>: If file not found.</li>
</ul>


<h3><code>read_csv_as_json</code></h3>

<p><strong>Description</strong>: Convert a CSV file to JSON format and save it.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>csv_file_path</code> (str | Path): Path to the CSV file.</li>
  <li><code>json_file_path</code> (str | Path): Path to save the JSON file.</li>
  <li><code>exc_info</code> (bool, optional): Include traceback information in logs. Defaults to True.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>bool</code>: True if conversion is successful, else False.</li>
</ul>


<h3><code>read_csv_as_dict</code></h3>

<p><strong>Description</strong>: Convert CSV content to a dictionary.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>csv_file</code> (str | Path): Path to the CSV file.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>dict | None</code>: Dictionary representation of CSV content, or None if failed.</li>
</ul>


<h3><code>read_csv_as_ns</code></h3>

<p><strong>Description</strong>: Load CSV data into a list of dictionaries using Pandas.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>file_path</code> (Union[str, Path]): Path to the CSV file.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>List[dict]</code>: List of dictionaries representing the CSV content.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>FileNotFoundError</code>: If file not found.</li>
</ul>