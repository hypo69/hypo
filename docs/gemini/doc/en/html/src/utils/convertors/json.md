html
<h1>hypotez/src/utils/convertors/json.py</h1>

<h2>Overview</h2>
<p>This module provides functions for converting JSON data into various formats: CSV, SimpleNamespace, XML, and XLS.</p>

<h2>Functions</h2>

<h3><code>json2csv</code></h3>

<p><strong>Description</strong>: Converts JSON data or a JSON file to CSV format.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>json_data</code> (str | list | dict | Path): JSON data as a string, list of dictionaries, or file path to a JSON file.  </li>
  <li><code>csv_file_path</code> (str | Path): Path to the CSV file to write.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>bool</code>: True if successful, False otherwise.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>ValueError</code>: If unsupported type for <code>json_data</code>.</li>
  <li><code>Exception</code>: If unable to parse JSON or write CSV.</li>
</ul>


<h3><code>json2ns</code></h3>

<p><strong>Description</strong>: Converts JSON data or a JSON file to a SimpleNamespace object.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>json_data</code> (str | dict | Path): JSON data as a string, dictionary, or file path to a JSON file.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>SimpleNamespace</code>: Parsed JSON data as a SimpleNamespace object.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>ValueError</code>: If unsupported type for <code>json_data</code>.</li>
  <li><code>Exception</code>: If unable to parse JSON.</li>
</ul>


<h3><code>json2xml</code></h3>

<p><strong>Description</strong>: Converts JSON data or a JSON file to XML format.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>json_data</code> (str | dict | Path): JSON data as a string, dictionary, or file path to a JSON file.</li>
  <li><code>root_tag</code> (str, optional): The root element tag for the XML. Defaults to "root".</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>str</code>: The resulting XML string.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>ValueError</code>: If unsupported type for <code>json_data</code>.</li>
  <li><code>Exception</code>: If unable to parse JSON or convert to XML.</li>
</ul>



<h3><code>json2xls</code></h3>

<p><strong>Description</strong>: Converts JSON data or a JSON file to XLS format.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>json_data</code> (str | list | dict | Path): JSON data as a string, list of dictionaries, or file path to a JSON file.</li>
  <li><code>xls_file_path</code> (str | Path): Path to the XLS file to write.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>bool</code>: True if successful, False otherwise.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>ValueError</code>: If unsupported type for <code>json_data</code>.</li>
  <li><code>Exception</code>: If unable to parse JSON or write XLS.</li>
</ul>