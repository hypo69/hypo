html
<h1>hypotez/src/goog/drive/header.py</h1>

<h2>Overview</h2>
<p>This module defines functions for setting the project root directory and accessing project settings and documentation.</p>

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

<p><strong>Description</strong>: Finds the root directory of the project starting from the current file's directory.</p>

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
</ul>


<p><strong>Example Usage</strong>:</p>
<pre><code>python
project_root = set_project_root()
print(project_root)
</code></pre>

<h2>Variables</h2>

<h3><code>__root__</code></h3>

<p><strong>Description</strong>: Path to the root directory of the project.  Initialized by calling <code>set_project_root()</code>.</p>
<p><strong>Type</strong>: <code>Path</code></p>


<h3><code>settings</code></h3>

<p><strong>Description</strong>: Project settings loaded from <code>settings.json</code>.  Can be <code>None</code> if the file is not found or invalid.</p>
<p><strong>Type</strong>: <code>dict</code></p>


<h3><code>doc_str</code></h3>

<p><strong>Description</strong>: Project documentation loaded from <code>README.MD</code>. Can be <code>None</code> if the file is not found or invalid.</p>
<p><strong>Type</strong>: <code>str</code></p>


<h3><code>__project_name__</code></h3>

<p><strong>Description</strong>: Name of the project, fetched from <code>settings.json</code> or defaulted to 'hypotez'.</p>
<p><strong>Type</strong>: <code>str</code></p>


<h3><code>__version__</code></h3>

<p><strong>Description</strong>: Project version, fetched from <code>settings.json</code> or defaulted to empty string.</p>
<p><strong>Type</strong>: <code>str</code></p>


<h3><code>__doc__</code></h3>

<p><strong>Description</strong>: Project documentation, fetched from <code>README.MD</code> or defaulted to empty string.</p>
<p><strong>Type</strong>: <code>str</code></p>


<h3><code>__details__</code></h3>

<p><strong>Description</strong>: Project details (currently empty).</p>
<p><strong>Type</strong>: <code>str</code></p>


<h3><code>__author__</code></h3>

<p><strong>Description</strong>: Author of the project, fetched from <code>settings.json</code> or defaulted to empty string.</p>
<p><strong>Type</strong>: <code>str</code></p>


<h3><code>__copyright__</code></h3>

<p><strong>Description</strong>: Copyright information of the project, fetched from <code>settings.json</code> or defaulted to empty string.</p>
<p><strong>Type</strong>: <code>str</code></p>


<h3><code>__cofee__</code></h3>

<p><strong>Description</strong>: Link to a coffee donation page for the developer.</p>
<p><strong>Type</strong>: <code>str</code></p>