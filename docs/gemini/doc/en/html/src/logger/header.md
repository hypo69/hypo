html
<h1>hypotez/src/logger/header.py</h1>

<h2>Overview</h2>
<p>This module defines the root path of the project. All imports are built relative to this path.</p>

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

<p><strong>Description</strong>: Finds the root directory of the project starting from the current file's directory, searching upwards and stopping at the first directory containing any of the marker files.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>marker_files</code> (tuple): Filenames or directory names to identify the project root.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Path</code>: Path to the root directory if found, otherwise the directory where the script is located.</li>
</ul>

<h2>Variables</h2>

<h3><code>__root__</code></h3>

<p><strong>Description</strong>: Path to the root directory of the project. This is set by calling the <code>set_project_root()</code> function.</p>
<p><strong>Type</strong>: <code>Path</code></p>



<h3><code>settings</code></h3>

<p><strong>Description</strong>: Project settings loaded from <code>settings.json</code>.</p>
<p><strong>Type</strong>: <code>dict</code></p>

<h3><code>doc_str</code></h3>

<p><strong>Description</strong>: Contents of the README.MD file.</p>
<p><strong>Type</strong>: <code>str</code></p>


<h3><code>__project_name__</code></h3>

<p><strong>Description</strong>: Project name, taken from <code>settings.json</code> or defaults to 'hypotez'.</p>
<p><strong>Type</strong>: <code>str</code></p>


<h3><code>__version__</code></h3>

<p><strong>Description</strong>: Project version, taken from <code>settings.json</code> or defaults to an empty string.</p>
<p><strong>Type</strong>: <code>str</code></p>


<h3><code>__doc__</code></h3>

<p><strong>Description</strong>: Project documentation, taken from <code>README.MD</code> or defaults to an empty string.</p>
<p><strong>Type</strong>: <code>str</code></p>


<h3><code>__details__</code></h3>

<p><strong>Description</strong>: Project details, defaults to an empty string.</p>
<p><strong>Type</strong>: <code>str</code></p>


<h3><code>__author__</code></h3>

<p><strong>Description</strong>: Author of the project, taken from <code>settings.json</code> or defaults to an empty string.</p>
<p><strong>Type</strong>: <code>str</code></p>


<h3><code>__copyright__</code></h3>

<p><strong>Description</strong>: Copyright information, taken from <code>settings.json</code> or defaults to an empty string.</p>
<p><strong>Type</strong>: <code>str</code></p>


<h3><code>__cofee__</code></h3>

<p><strong>Description</strong>: Link to support the developers with coffee, taken from <code>settings.json</code> or defaults to a specific URL.</p>
<p><strong>Type</strong>: <code>str</code></p>