html
<h1>hypotez/src/utils/convertors/xls.py</h1>

<h2>Overview</h2>
<p>This module provides functions for converting XLS files to dictionaries and vice-versa.</p>

<h2>Constants</h2>

<h3><code>MODE</code></h3>

<p><strong>Description</strong>: A constant representing the current mode (e.g., 'dev').</p>
<p><strong>Value</strong>: 'dev'</p>


<h2>Functions</h2>

<h3><code>xls2dict</code></h3>

<p><strong>Description</strong>: Converts an XLS file to a dictionary.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>xls_file</code> (str | Path): The path to the XLS file.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>dict | None</code>: A dictionary representation of the XLS file contents, or <code>None</code> if an error occurs.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>:  Any exception encountered during the file reading or conversion process.</li>
</ul>