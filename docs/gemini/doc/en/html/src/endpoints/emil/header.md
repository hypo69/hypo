html
<h1>hypotez/src/endpoints/emil/header.py</h1>

<h2>Overview</h2>
<p>This module defines functions for setting the project root directory and loading project settings. It utilizes the <code>gs</code> module and handles potential errors during file reading.</p>

<h2>Functions</h2>

<h3><code>set_project_root</code></h3>

<p><strong>Description</strong>: Finds the root directory of the project starting from the current file's directory, searching upwards until a directory containing specified marker files is found. If no such directory is found, it returns the directory where the script is located. Also adds the root directory to the Python path.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>marker_files</code> (tuple): Filenames or directory names to identify the project root. Defaults to ('pyproject.toml', 'requirements.txt', '.git').</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Path</code>: Path to the root directory if found, otherwise the directory where the script is located.</li>
</ul>

<h3><code>set_project_root</code></h3>

<p><strong>Description</strong>: Finds the root directory of the project starting from the current file's directory, searching upwards until a directory containing specified marker files is found. If no such directory is found, it returns the directory where the script is located. Also adds the root directory to the Python path.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>marker_files</code> (tuple, optional): Filenames or directory names to identify the project root. Defaults to ('pyproject.toml', 'requirements.txt', '.git').</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Path</code>: Path to the root directory if found, otherwise the directory where the script is located.</li>
</ul>


<p><strong>Raises</strong>:</p>
<ul>
  <li>No exceptions are explicitly raised, but `FileNotFoundError` could potentially be raised if the marker files do not exist.</li>
</ul>