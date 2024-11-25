html
<h1>Module: hypotez/src/utils/convertors/dict</h1>

<h2>Overview</h2>
<p>This module contains functions for recursively converting dictionaries to SimpleNamespace objects, exporting data to various formats (XML, CSV, JSON, XLS, PDF, HTML), and vice versa.</p>

<h2>Functions</h2>

<h3><code>dict2pdf</code></h3>

<p><strong>Description</strong>: Saves dictionary data to a PDF file.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>data</code> (<code>dict | SimpleNamespace</code>): The dictionary or SimpleNamespace object to convert.</li>
  <li><code>file_path</code> (<code>str | Path</code>): Path to the output PDF file.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>None</code>:  This function does not return a value. It saves the data to a file.</li>
</ul>


<h3><code>dict2ns</code></h3>

<p><strong>Description</strong>: Recursively converts dictionaries to SimpleNamespace objects.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>data</code> (<code>Dict[str, Any] | List[Any]</code>): The data to convert (either a dictionary or a list).</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Any</code>: The converted data as a SimpleNamespace or a list of SimpleNamespace objects.  Handles nested dictionaries and lists recursively.</li>
</ul>


<h3><code>dict2xml</code></h3>

<p><strong>Description</strong>: Generates an XML string from a dictionary.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>data</code> (<code>Dict[str, Any]</code>): The dictionary to convert to XML.</li>
  <li><code>encoding</code> (<code>str</code>, optional): Data encoding (defaults to 'UTF-8').</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>str</code>: The XML string representing the input dictionary.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>: If more than one root node is provided in the input dictionary.</li>
</ul>


<h3><code>dict2csv</code></h3>

<p><strong>Description</strong>: Saves dictionary or SimpleNamespace data to a CSV file.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>data</code> (<code>dict | SimpleNamespace</code>): The data to save.</li>
  <li><code>file_path</code> (<code>str | Path</code>): Path to the CSV file.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>bool</code>: True if the file was saved successfully; False otherwise. (This assumes there's a function <code>save_csv_file</code> that handles the actual CSV saving.)</li>
</ul>


<h3><code>dict2xls</code></h3>

<p><strong>Description</strong>: Saves dictionary or SimpleNamespace data to an XLS file.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>data</code> (<code>dict | SimpleNamespace</code>): The data to save.</li>
  <li><code>file_path</code> (<code>str | Path</code>): Path to the XLS file.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>bool</code>: True if the file was saved successfully; False otherwise. (This assumes there's a function <code>save_xls_file</code> that handles the actual XLS saving.)</li>
</ul>


<h3><code>dict2html</code></h3>

<p><strong>Description</strong>: Generates an HTML table string from a dictionary or SimpleNamespace object.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>data</code> (<code>dict | SimpleNamespace</code>): The data to convert to HTML.</li>
  <li><code>encoding</code> (<code>str</code>, optional): Data encoding (defaults to 'UTF-8').</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>str</code>: The HTML string representing the input dictionary as a table.</li>
</ul>