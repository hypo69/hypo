html
<h1>hypotez/src/category/header.py</h1>

<h2>Overview</h2>
<p>This module defines the root path of the project. All imports are built relative to this path.</p>

<h2>Variables</h2>

<h3><code>MODE</code></h3>

<p><strong>Description</strong>:  A string representing the development mode of the project.</p>


<h3><code>__root__</code></h3>

<p><strong>Description</strong>: Path object representing the root directory of the project.  Initialized by the <code>set_project_root()</code> function.</p>


<h3><code>settings</code></h3>

<p><strong>Description</strong>: A dictionary containing project settings loaded from <code>settings.json</code>.  Returns <code>None</code> if the file doesn't exist or can't be parsed.</p>


<h3><code>doc_str</code></h3>

<p><strong>Description</strong>: String containing the project documentation from <code>README.MD</code>. Returns <code>None</code> if the file doesn't exist or can't be parsed.</p>


<h3><code>__project_name__</code></h3>

<p><strong>Description</strong>: Project name from <code>settings.json</code>, or 'hypotez' if not found.</p>


<h3><code>__version__</code></h3>

<p><strong>Description</strong>: Project version from <code>settings.json</code>, or an empty string if not found.</p>


<h3><code>__doc__</code></h3>

<p><strong>Description</strong>: Project documentation, read from README.MD or defaults to an empty string.</p>


<h3><code>__details__</code></h3>

<p><strong>Description</strong>: Project details (currently an empty string).</p>


<h3><code>__author__</code></h3>

<p><strong>Description</strong>: Project author from <code>settings.json</code>, or an empty string if not found.</p>


<h3><code>__copyright__</code></h3>

<p><strong>Description</strong>: Project copyright from <code>settings.json</code>, or an empty string if not found.</p>


<h3><code>__cofee__</code></h3>

<p><strong>Description</strong>: A string containing a link for supporting the developer through a cup of coffee. Default value if not found in settings.</p>


<h2>Functions</h2>

<h3><code>set_project_root</code></h3>

<p><strong>Description</strong>: Finds the root directory of the project.  Starts from the current file's directory, searches upwards, and stops at the first directory containing any of the specified marker files.</p>

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
  <li>None</li>
</ul>


<h2>Modules</h2>

<p><strong>Modules</strong>:</p>
<ul>
  <li><code>sys</code></li>
  <li><code>json</code></li>
  <li><code>pathlib</code></li>
   <li><code>packaging.version</code></li>
   <li><code>src.gs</code></li>
</ul>