html
<h1>Module: hypotez/src/translators/header.py</h1>

<h2>Overview</h2>
<p>This module defines functions for setting the project root directory and loading settings from a JSON file.</p>

<h2>Functions</h2>

<h3><code>set_project_root</code></h3>

<p><strong>Description</strong>: Finds the root directory of the project starting from the current file's directory.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>marker_files</code> (tuple): Filenames or directory names to identify the project root. Defaults to ('pyproject.toml', 'requirements.txt', '.git').</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Path</code>: Path to the root directory if found, otherwise the directory where the script is located.</li>
</ul>


<h3><code>set_project_root</code></h3>

<p><strong>Description</strong>: Finds the root directory of the project by checking parent directories until a marker file is found. Inserts the root directory into the PYTHONPATH.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>marker_files</code> (tuple, optional): A tuple of files or directories that indicate the project root. Defaults to ('pyproject.toml', 'requirements.txt', '.git').</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Path</code>: The path to the project root directory.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
</ul>



<!-- Additional functions (set_project_root is detailed above) -->