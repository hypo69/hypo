html
<h1>Module: hypotez/src/endpoints/header.py</h1>

<h2>Overview</h2>
<p>This module defines functions for setting the project root directory and loading project settings. It utilizes the <code>gs</code> module for file paths and handles potential errors during file reading.</p>

<h2>Functions</h2>

<h3><code>set_project_root</code></h3>

<p><strong>Description</strong>: Finds the root directory of the project by searching upwards from the current file's directory. It stops when it encounters a directory containing any of the specified marker files.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>marker_files</code> (tuple): Filenames or directory names to identify the project root. Defaults to ('pyproject.toml', 'requirements.txt', '.git').</li>
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
  <li><code>Path</code>: Path to the root directory if found, otherwise the directory where the script is located.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li>No exceptions are explicitly raised by this function.</li>
</ul>

<h2>Variables</h2>

<h3><code>__root__</code></h3>

<p><strong>Description</strong>: Represents the path to the project root, obtained by calling the <code>set_project_root</code> function.</p>

<p><strong>Type</strong>: <code>Path</code></p>

<p><strong>Usage</strong>: This variable is typically used to construct paths relative to the project root.</p>


<p><strong>Description</strong>: Stores project settings loaded from 'settings.json'.</p>

<p><strong>Type</strong>: <code>dict</code> or <code>None</code></p>



<h3><code>doc_str</code></h3>

<p><strong>Description</strong>: Contains the content of the 'README.MD' file.</p>

<p><strong>Type</strong>: <code>str</code> or <code>None</code></p>

<p><strong>Usage</strong>: Used for documentation, or other text processing in the project. </p>



<h3><code>__project_name__</code></h3>

<p><strong>Description</strong>: Project name, retrieved from the 'settings.json' file. Defaults to 'hypotez'.</p>

<p><strong>Type</strong>: <code>str</code></p>



<h3><code>__version__</code></h3>

<p><strong>Description</strong>: Project version, retrieved from 'settings.json'. Defaults to an empty string.</p>

<p><strong>Type</strong>: <code>str</code></p>



<h3><code>__doc__</code></h3>

<p><strong>Description</strong>: Project documentation, read from 'README.MD'. Defaults to an empty string.</p>

<p><strong>Type</strong>: <code>str</code></p>



<h3><code>__details__</code></h3>

<p><strong>Description</strong>: Project details.</p>

<p><strong>Type</strong>: <code>str</code></p>



<h3><code>__author__</code></h3>

<p><strong>Description</strong>: Author of the project.</p>

<p><strong>Type</strong>: <code>str</code></p>



<h3><code>__copyright__</code></h3>

<p><strong>Description</strong>: Copyright information for the project.</p>

<p><strong>Type</strong>: <code>str</code></p>


<h3><code>__cofee__</code></h3>

<p><strong>Description</strong>:  A link to treat the developer to a coffee.</p>

<p><strong>Type</strong>: <code>str</code></p>