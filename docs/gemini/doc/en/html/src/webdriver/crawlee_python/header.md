html
<h1>header.py</h1>

<h2>Overview</h2>
<p>This module provides functions for setting the project root directory and loading project settings.</p>

<h2>Functions</h2>

<h3><code>set_project_root</code></h3>

<p><strong>Description</strong>: Finds the root directory of the project by searching upwards from the current file's directory.  It stops at the first directory containing any of the specified marker files (e.g., <code>pyproject.toml</code>, <code>requirements.txt</code>, <code>.git</code>).</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>marker_files</code> (tuple): Filenames or directory names to identify the project root. Defaults to a tuple containing 'pyproject.toml', 'requirements.txt', and '.git'.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Path</code>: Path to the root directory if found, otherwise the directory where the script is located.</li>
</ul>


<h3><code>set_project_root</code></h3>

<p><strong>Description</strong>: Finds the root directory of the project starting from the current file's directory.  Searches upwards until it finds a directory containing any of the specified marker files.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>marker_files</code> (tuple, optional): Filenames or directory names to identify the project root. Defaults to a tuple of ('pyproject.toml', 'requirements.txt', '.git').</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Path</code>: Path to the root directory if found. Otherwise returns the directory where the current script is located.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li>No exceptions are explicitly raised.</li>
</ul>


<h2>Variables</h2>

<h3><code>__root__</code></h3>

<p><strong>Description</strong>: Stores the path to the project root directory, obtained from <code>set_project_root()</code>.</p>

<p><strong>Type</strong>: <code>Path</code></p>


<h2>Module Variables</h2>

<h3><code>MODE</code></h3>

<p><strong>Description</strong>: Stores the mode of operation, currently set to 'dev'.</p>

<p><strong>Type</strong>: <code>str</code></p>

<h3><code>settings</code></h3>

<p><strong>Description</strong>: Contains project settings loaded from <code>settings.json</code>.</p>

<p><strong>Type</strong>: <code>dict</code></p>


<h3><code>doc_str</code></h3>

<p><strong>Description</strong>: Stores the content of the README.md file.</p>

<p><strong>Type</strong>: <code>str</code></p>


<h3><code>__project_name__</code></h3>

<p><strong>Description</strong>: Project name, obtained from <code>settings.json</code> or defaults to 'hypotez'.</p>

<p><strong>Type</strong>: <code>str</code></p>


<h3><code>__version__</code></h3>

<p><strong>Description</strong>: Project version, obtained from <code>settings.json</code> or defaults to an empty string.</p>

<p><strong>Type</strong>: <code>str</code></p>



<h3><code>__doc__</code></h3>

<p><strong>Description</strong>: Project documentation, obtained from <code>README.md</code> or defaults to an empty string.</p>

<p><strong>Type</strong>: <code>str</code></p>



<h3><code>__details__</code></h3>

<p><strong>Description</strong>: Project details, currently set to an empty string.</p>

<p><strong>Type</strong>: <code>str</code></p>


<h3><code>__author__</code></h3>

<p><strong>Description</strong>: Project author, obtained from <code>settings.json</code> or defaults to an empty string.</p>

<p><strong>Type</strong>: <code>str</code></p>


<h3><code>__copyright__</code></h3>

<p><strong>Description</strong>: Project copyright, obtained from <code>settings.json</code> or defaults to an empty string.</p>

<p><strong>Type</strong>: <code>str</code></p>


<h3><code>__cofee__</code></h3>

<p><strong>Description</strong>:  A string containing a coffee boosting link for the developer. Obtained from <code>settings.json</code> or defaults to a default link.</p>

<p><strong>Type</strong>: <code>str</code></p>