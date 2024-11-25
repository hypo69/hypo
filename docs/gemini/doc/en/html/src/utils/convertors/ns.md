html
<h1>hypotez/src/utils/convertors/ns.py</h1>

<h2>Overview</h2>
<p>This module provides functions for converting SimpleNamespace objects to various formats, including dictionary, JSON, CSV, XML, and XLS.</p>

<h2>Functions</h2>

<h3><code>ns2dict</code></h3>

<p><strong>Description</strong>: Converts a SimpleNamespace object to a dictionary.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>ns_obj</code> (SimpleNamespace): The SimpleNamespace object to convert.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>dict</code>: The converted dictionary.</li>
</ul>


<h3><code>ns2json</code></h3>

<p><strong>Description</strong>: Converts a SimpleNamespace object to JSON format.  Can optionally save the JSON to a file.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>ns_obj</code> (SimpleNamespace): The SimpleNamespace object to convert.</li>
  <li><code>json_file_path</code> (str | Path, optional): Path to save the JSON file. If not provided, returns the JSON string.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>str | bool</code>: JSON string if no file path is provided, otherwise True if the file is written successfully.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>: Any exception during JSON conversion or file writing.</li>
</ul>


<h3><code>ns2csv</code></h3>

<p><strong>Description</strong>: Converts a SimpleNamespace object to CSV format and saves it to a file.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>ns_obj</code> (SimpleNamespace): The SimpleNamespace object to convert.</li>
  <li><code>csv_file_path</code> (str | Path): Path to save the CSV file.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>bool</code>: True if successful, False otherwise.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>: Any exception during CSV conversion or file writing.</li>
</ul>


<h3><code>ns2xml</code></h3>

<p><strong>Description</strong>: Converts a SimpleNamespace object to XML format.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>ns_obj</code> (SimpleNamespace): The SimpleNamespace object to convert.</li>
  <li><code>root_tag</code> (str, optional): The root element tag for the XML. Defaults to "root".</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>str</code>: The resulting XML string.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>: Any exception during XML conversion.</li>
</ul>


<h3><code>ns2xls</code></h3>

<p><strong>Description</strong>: Converts a SimpleNamespace object to XLS format and saves it to a file.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>ns_obj</code> (SimpleNamespace): The SimpleNamespace object to convert.</li>
  <li><code>xls_file_path</code> (str | Path): Path to save the XLS file.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>bool</code>: True if successful, False otherwise.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>: Any exception during XLS conversion or file writing.</li>
</ul>