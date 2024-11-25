html
<h1>hypotez/src/ai/myai/header.py</h1>

<h2>Overview</h2>
<p>This module provides functions for setting the project root directory and loading project settings from a JSON file.</p>

<h2>Functions</h2>

<h3><code>set_project_root</code></h3>

<p><strong>Description</strong>: Finds the root directory of the project starting from the current file's directory, searching upwards and stopping at the first directory containing any of the marker files.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>marker_files</code> (tuple): Filenames or directory names to identify the project root.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Path</code>: Path to the root directory if found, otherwise the directory where the script is located.</li>
</ul>


<h3><code>set_project_root</code></h3>

<p><strong>Description</strong>:  Finds the root directory of the project. It searches upwards from the current file's directory until it finds a directory containing any of the specified marker files (pyproject.toml, requirements.txt, .git).</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>marker_files</code> (tuple, optional): A tuple of filenames or directory names to search for. Defaults to ('pyproject.toml', 'requirements.txt', '.git').</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Path</code>: The path to the project root directory.  If no marker files are found, it returns the directory containing the current file.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li>No exceptions explicitly raised.</li>
</ul>