html
<h1>Module: hypotez/src/endpoints/hypo69/psychologist_bot/header.py</h1>

<h2>Overview</h2>
<p>This module provides functions for setting the project root directory and loading project settings. It also imports necessary modules.</p>

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

<p><strong>Description</strong>: Finds the root directory of the project, starting from the current file's directory, searching upwards for marker files (pyproject.toml, requirements.txt, .git). Sets the root path to sys.path. Returns the Path to the project root.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>marker_files</code> (tuple, optional): A tuple of filenames or directories to use as markers for the project root. Defaults to ('pyproject.toml', 'requirements.txt', '.git').</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Path</code>: The path to the root directory of the project. Returns the current directory if no marker files are found.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><em>None</em>: No exceptions are explicitly raised.</li>
</ul>


<p><strong>Example usage (within the module):</strong></p>
<pre><code>python
__root__ = set_project_root()
</code></pre>


<h2>Global Variables</h2>

<h3><code>__root__</code></h3>

<p><strong>Description</strong>: Stores the path to the project root directory. Initialized by calling <code>set_project_root()</code>.</p>

<p><strong>Type</strong>:</p>
<ul>
  <li><code>Path</code></li>
</ul>


<h3><code>settings</code></h3>

<p><strong>Description</strong>: Stores project settings loaded from <code>settings.json</code>.</p>
<p><strong>Type</strong>:</p>
<ul>
  <li><code>dict</code></li>
</ul>


<h3><code>doc_str</code></h3>

<p><strong>Description</strong>: Stores the content of the README.MD file, if found.</p>

<p><strong>Type</strong>:</p>
<ul>
  <li><code>str</code></li>
</ul>


<h3><code>__project_name__</code></h3>

<p><strong>Description</strong>: Project name, retrieved from settings or defaults to 'hypotez'.</p>

<p><strong>Type</strong>:</p>
<ul>
  <li><code>str</code></li>
</ul>


<h3><code>__version__</code></h3>

<p><strong>Description</strong>: Project version, retrieved from settings or defaults to empty string.</p>

<p><strong>Type</strong>:</p>
<ul>
  <li><code>str</code></li>
</ul>


<h3><code>__doc__</code></h3>

<p><strong>Description</strong>: Project documentation, retrieved from README.MD or defaults to empty string.</p>

<p><strong>Type</strong>:</p>
<ul>
  <li><code>str</code></li>
</ul>

<h3><code>__details__</code></h3>

<p><strong>Description</strong>: Project details, defaults to empty string.</p>

<p><strong>Type</strong>:</p>
<ul>
  <li><code>str</code></li>
</ul>


<h3><code>__author__</code></h3>

<p><strong>Description</strong>: Project author, retrieved from settings or defaults to empty string.</p>

<p><strong>Type</strong>:</p>
<ul>
  <li><code>str</code></li>
</ul>


<h3><code>__copyright__</code></h3>

<p><strong>Description</strong>: Project copyright, retrieved from settings or defaults to empty string.</p>

<p><strong>Type</strong>:</p>
<ul>
  <li><code>str</code></li>
</ul>


<h3><code>__cofee__</code></h3>

<p><strong>Description</strong>:  Link to support the developer, retrieved from settings or default value.</p>

<p><strong>Type</strong>:</p>
<ul>
  <li><code>str</code></li>
</ul>