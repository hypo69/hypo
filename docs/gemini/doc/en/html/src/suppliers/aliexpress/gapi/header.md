html
<h1>Module: hypotez/src/suppliers/aliexpress/gapi/header.py</h1>

<h2>Overview</h2>
<p>This module defines the root path to the project. All imports are built relative to this path.  Future versions should ideally store this in a system variable.</p>


<h2>Variables</h2>

<h3><code>MODE</code></h3>

<p><strong>Description</strong>: Stores the development mode, currently set to 'dev'.</p>


<h3><code>__root__</code></h3>

<p><strong>Description</strong>: Path to the project root directory.  Determined by calling <code>set_project_root()</code>.</p>


<h3><code>settings</code></h3>

<p><strong>Description</strong>: A dictionary containing project settings.  Loaded from <code>src/settings.json</code>.  Defaults to <code>None</code> if the file is missing or invalid.</p>


<h3><code>doc_str</code></h3>

<p><strong>Description</strong>:  String containing the project's documentation, usually from <code>README.MD</code>. Defaults to <code>None</code> if the file is missing or invalid.</p>


<h3><code>__project_name__</code></h3>

<p><strong>Description</strong>: Project name, obtained from the settings, defaults to 'hypotez'.</p>


<h3><code>__version__</code></h3>

<p><strong>Description</strong>: Project version, obtained from the settings, defaults to empty string.</p>


<h3><code>__doc__</code></h3>

<p><strong>Description</strong>: Project documentation, obtained from <code>doc_str</code>, defaults to empty string.</p>


<h3><code>__details__</code></h3>

<p><strong>Description</strong>: Project details, currently empty.</p>


<h3><code>__author__</code></h3>

<p><strong>Description</strong>: Project author, obtained from the settings, defaults to empty string.</p>


<h3><code>__copyright__</code></h3>

<p><strong>Description</strong>: Project copyright, obtained from the settings, defaults to empty string.</p>


<h3><code>__cofee__</code></h3>

<p><strong>Description</strong>: Project's coffee link, obtained from the settings, defaults to a predefined coffee link for developer support.</p>


<h2>Functions</h2>

<h3><code>set_project_root</code></h3>

<p><strong>Description</strong>: Finds the root directory of the project starting from the current file's directory, searching upwards until it finds a directory containing any of the specified marker files.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>marker_files</code> (tuple): Filenames or directory names to identify the project root. Defaults to ('pyproject.toml', 'requirements.txt', '.git').</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Path</code>: Path to the root directory if found, otherwise the directory where the script is located.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
</ul>


<h2>Modules</h2>
<p><strong>Modules used:</strong></p>
<ul>
<li><code>sys</code></li>
<li><code>json</code></li>
<li><code>packaging.version</code></li>
<li><code>pathlib</code></li>
<li><code>src.gs</code></li>
</ul>