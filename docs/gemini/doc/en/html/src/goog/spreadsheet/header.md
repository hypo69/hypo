html
<h1>hypotez/src/goog/spreadsheet/header.py</h1>

<h2>Overview</h2>
<p>This module provides functionality to locate the project root directory and load settings from a JSON file. It also attempts to load documentation from a README.md file. The module initializes important variables like project name, version, documentation string, author, copyright, and a developer support link.</p>

<h2>Functions</h2>

<h3><code>set_project_root</code></h3>

<p><strong>Description</strong>: Finds the root directory of the project starting from the current file's directory, searching upwards and stopping at the first directory containing any of the marker files (pyproject.toml, requirements.txt, .git).</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>marker_files</code> (tuple): Filenames or directory names to identify the project root.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Path</code>: Path to the root directory if found, otherwise the directory where the script is located.</li>
</ul>


<h3><code>set_project_root</code></h3>

<p><strong>Description</strong>: Finds the root directory of the project starting from the current file's directory, searching upwards and stopping at the first directory containing any of the marker files.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>marker_files</code> (tuple, optional): Filenames or directory names to identify the project root. Defaults to ('pyproject.toml', 'requirements.txt', '.git').</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
<li><code>Path</code>: Path to the root directory if found, otherwise the directory where the script is located.  </li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li>None</li>
</ul>


<p><strong>Example Usage (within the code):</strong></p>
<pre><code>python
__root__ = set_project_root()
</code></pre>