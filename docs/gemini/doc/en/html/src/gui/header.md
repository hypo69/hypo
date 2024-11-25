html
<h1>hypotez/src/gui/header.py</h1>

<h2>Overview</h2>
<p>This module defines the root path to the project. All imports are built relative to this path.  It aims to improve modularity and organization by centralizing the project's location.</p>

<h2>Functions</h2>

<h3><code>set_project_root</code></h3>

<p><strong>Description</strong>: Finds the root directory of the project starting from the current file's directory, searching upwards and stopping at the first directory containing any of the marker files.</p>

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
  <li><code>marker_files</code> (tuple): Filenames or directory names to identify the project root.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Path</code>: Path to the root directory if found, otherwise the directory where the script is located.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li>None</li>
</ul>



<h2>Global Variables</h2>

<h3><code>__root__</code></h3>

<p><strong>Description</strong>: Path to the root directory of the project, set by calling the <code>set_project_root</code> function.  This is crucial for resolving relative import paths correctly.</p>

<p><strong>Type</strong>: <code>Path</code></p>




<h3><code>settings</code></h3>

<p><strong>Description</strong>: Project settings loaded from <code>settings.json</code>.  It contains project-specific configurations.</p>

<p><strong>Type</strong>: <code>dict | None</code></p>

<h3><code>doc_str</code></h3>

<p><strong>Description</strong>: Project documentation (README content) from <code>README.MD</code></p>

<p><strong>Type</strong>: <code>str | None</code></p>



<h3><code>__project_name__</code></h3>

<p><strong>Description</strong>: Name of the project, retrieved from settings. Defaults to 'hypotez'.</p>
<p><strong>Type</strong>: <code>str</code></p>


<h3><code>__version__</code></h3>

<p><strong>Description</strong>: Project version, retrieved from settings. Defaults to empty string.</p>
<p><strong>Type</strong>: <code>str</code></p>


<h3><code>__doc__</code></h3>

<p><strong>Description</strong>: Project documentation, loaded from README. Defaults to empty string.</p>
<p><strong>Type</strong>: <code>str</code></p>

<h3><code>__details__</code></h3>

<p><strong>Description</strong>: Project details (empty by default). </p>
<p><strong>Type</strong>: <code>str</code></p>

<h3><code>__author__</code></h3>

<p><strong>Description</strong>: Author of the project, retrieved from settings. Defaults to empty string.</p>
<p><strong>Type</strong>: <code>str</code></p>


<h3><code>__copyright__</code></h3>

<p><strong>Description</strong>: Copyright information, retrieved from settings. Defaults to empty string.</p>
<p><strong>Type</strong>: <code>str</code></p>

<h3><code>__cofee__</code></h3>

<p><strong>Description</strong>: A link for supporting the developer through coffee donations.</p>
<p><strong>Type</strong>: <code>str</code></p>