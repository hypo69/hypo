html
<h1>hypotez/src/logger/header.py</h1>

<h2>Overview</h2>
<p>This module defines the root path of the project. All imports are built relative to this path.</p>

<h2>Constants</h2>

<h3><code>MODE</code></h3>

<p><strong>Description</strong>: A string constant defining the current mode of the application.</p>
<p><strong>Value</strong>: 'dev'</p>


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


<h2>Variables</h2>

<h3><code>__root__</code></h3>

<p><strong>Description</strong>: Path to the root directory of the project.</p>
<p><strong>Type</strong>: Path</p>

<h3><code>settings</code></h3>

<p><strong>Description</strong>: Project settings loaded from <code>settings.json</code>.  Defaults to <code>None</code>.</p>
<p><strong>Type</strong>: dict</p>

<h3><code>doc_str</code></h3>

<p><strong>Description</strong>: Project documentation loaded from <code>README.MD</code>. Defaults to <code>None</code>.</p>
<p><strong>Type</strong>: str</p>


<h3><code>__project_name__</code></h3>

<p><strong>Description</strong>: Project name, retrieved from <code>settings.json</code>. Defaults to 'hypotez'.</p>
<p><strong>Type</strong>: str</p>


<h3><code>__version__</code></h3>

<p><strong>Description</strong>: Project version, retrieved from <code>settings.json</code>. Defaults to empty string.</p>
<p><strong>Type</strong>: str</p>


<h3><code>__doc__</code></h3>

<p><strong>Description</strong>: Project documentation, loaded from <code>README.MD</code>. Defaults to empty string.</p>
<p><strong>Type</strong>: str</p>

<h3><code>__details__</code></h3>

<p><strong>Description</strong>: Project details.  Defaults to an empty string.</p>
<p><strong>Type</strong>: str</p>

<h3><code>__author__</code></h3>

<p><strong>Description</strong>: Project author, retrieved from <code>settings.json</code>. Defaults to an empty string.</p>
<p><strong>Type</strong>: str</p>

<h3><code>__copyright__</code></h3>

<p><strong>Description</strong>: Project copyright, retrieved from <code>settings.json</code>. Defaults to an empty string.</p>
<p><strong>Type</strong>: str</p>


<h3><code>__cofee__</code></h3>

<p><strong>Description</strong>: A link to a platform for supporting the developer with a coffee. Defaults to a pre-defined link.</p>
<p><strong>Type</strong>: str</p>