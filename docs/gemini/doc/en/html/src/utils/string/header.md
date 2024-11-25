html
<h1>hypotez/src/logger/header.py</h1>

<h2>Overview</h2>
<p>This module defines the root path to the project. All imports are built relative to this path.  Future versions will likely store this path in a system variable.</p>

<h2>Constants</h2>

<h3><code>MODE</code></h3>

<p><strong>Description</strong>: A string representing the development mode. Currently set to 'dev'.</p>


<h2>Functions</h2>

<h3><code>set_project_root</code></h3>

<p><strong>Description</strong>: Finds the root directory of the project starting from the current file's directory.  It searches upwards through parent directories until it encounters a directory containing any of the specified marker files.</p>

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

<p><strong>Description</strong>: A Path object representing the root directory of the project, as determined by the <code>set_project_root()</code> function. </p>

<p><strong>Type</strong>: <code>Path</code></p>



<h3><code>settings</code></h3>

<p><strong>Description</strong>: A dictionary containing project settings loaded from the 'settings.json' file in the project root.  If the file is not found or cannot be parsed as JSON, the variable defaults to <code>None</code>.</p>

<p><strong>Type</strong>: <code>dict | None</code></p>


<h3><code>doc_str</code></h3>

<p><strong>Description</strong>:  String containing the content of the README.MD file in the project root. If the file is not found or cannot be read, the variable defaults to <code>None</code>.</p>

<p><strong>Type</strong>: <code>str | None</code></p>


<h3><code>__project_name__</code></h3>

<p><strong>Description</strong>: The project name.  Defaults to 'hypotez' if not specified in settings.json.</p>

<p><strong>Type</strong>: <code>str</code></p>


<h3><code>__version__</code></h3>

<p><strong>Description</strong>: The project version. Defaults to an empty string if not specified in settings.json.</p>

<p><strong>Type</strong>: <code>str</code></p>


<h3><code>__doc__</code></h3>

<p><strong>Description</strong>: The project documentation. Defaults to an empty string if not found.</p>

<p><strong>Type</strong>: <code>str</code></p>


<h3><code>__details__</code></h3>

<p><strong>Description</strong>:  Placeholder for project details (currently empty).</p>

<p><strong>Type</strong>: <code>str</code></p>


<h3><code>__author__</code></h3>

<p><strong>Description</strong>: The project author, taken from settings.json.</p>

<p><strong>Type</strong>: <code>str</code></p>


<h3><code>__copyright__</code></h3>

<p><strong>Description</strong>: The project copyright, taken from settings.json.</p>

<p><strong>Type</strong>: <code>str</code></p>


<h3><code>__cofee__</code></h3>

<p><strong>Description</strong>: A string containing a link for supporting the project. </p>

<p><strong>Type</strong>: <code>str</code></p>