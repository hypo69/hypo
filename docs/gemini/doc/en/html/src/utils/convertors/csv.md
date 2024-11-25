html
<h1>hypotez/src/utils/convertors/csv.py</h1>

<h2>Overview</h2>
<p>This module provides utilities for converting CSV data to dictionaries, SimpleNamespace objects, and JSON format. It includes functions for reading CSV files, converting the data to various formats, and saving the converted data to JSON files.</p>

<h2>Constants</h2>

<h3><code>MODE</code></h3>
<p><strong>Description</strong>: A constant representing the development mode.</p>
<p><strong>Value</strong>: 'dev'</p>

<h2>Functions</h2>

<h3><code>csv2dict</code></h3>

<p><strong>Description</strong>: Converts CSV data to a dictionary.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>csv_file</code> (str | Path): Path to the CSV file to read.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>dict | None</code>: Dictionary containing the data from CSV converted to JSON format, or <code>None</code> if conversion failed.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>: If unable to read CSV.</li>
</ul>


<h3><code>csv2ns</code></h3>

<p><strong>Description</strong>: Converts CSV data to SimpleNamespace objects.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>csv_file</code> (str | Path): Path to the CSV file to read.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>SimpleNamespace | None</code>: SimpleNamespace object containing the data from CSV, or <code>None</code> if conversion failed.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>: If unable to read CSV.</li>
</ul>

<h3><code>csv_to_json</code></h3>

<p><strong>Description</strong>: Converts a CSV file to JSON format and saves it to a JSON file.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>csv_file_path</code> (str | Path): The path to the CSV file to read.</li>
  <li><code>json_file_path</code> (str | Path): The path to the JSON file to save.</li>
  <li><code>exc_info</code> (bool, optional): If <code>True</code>, includes traceback information in the log. Defaults to <code>True</code>.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>List[Dict[str, str]] | None</code>: The JSON data as a list of dictionaries, or <code>None</code> if conversion failed.</li>
</ul>

<p><strong>Example</strong>:</p>
<pre><code>python
json_data = csv_to_json('dialogue_log.csv', 'dialogue_log.json')
print(json_data)
</code></pre>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>: If there's an error during the conversion or file operations.</li>
</ul>