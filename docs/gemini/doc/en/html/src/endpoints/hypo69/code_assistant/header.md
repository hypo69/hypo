html
<h1>Module: hypotez/src/logger/header.py</h1>

<h2>Overview</h2>
<p>This module defines the root path of the project. All imports are built relative to this path.  Future versions will likely move this functionality to a system variable for improved flexibility.</p>

<h2>Constants</h2>

<h3><code>MODE</code></h3>

<p><strong>Description</strong>: A string constant representing the development mode.</p>
<p><strong>Value</strong>: 'dev'</p>

<h2>Functions</h2>

<h3><code>set_project_root</code></h3>

<p><strong>Description</strong>: Finds the root directory of the project starting from the current file's directory, searching upwards until a directory containing any of the specified marker files is found.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>marker_files</code> (tuple, optional): A tuple of filenames or directory names to identify the project root. Defaults to ('pyproject.toml', 'requirements.txt', '.git').</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Path</code>: The path to the root directory if found.  Returns the directory of the current file if no suitable root directory is found.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li>None</li>
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

<p><strong>Description</strong>: Stores the root path of the project, obtained using <code>set_project_root()</code>. This path is also added to <code>sys.path</code>.</p>
<p><strong>Type</strong>: <code>Path</code></p>

<h2>Modules</h2>
<p><strong>Imports</strong>:</p>
<ul>
<li><code>sys</code></li>
<li><code>json</code></li>
<li><code>packaging.version import Version</code></li>
<li><code>pathlib.Path</code></li>
<li><code>src.gs</code></li>
</ul>


<h2>Global Variables</h2>
<p><code>settings</code>: Dictionary containing project settings.  Loaded from <code>src/settings.json</code>. Can be <code>None</code> if the file is not found or cannot be parsed. </p>


<p><code>doc_str</code>: String containing the README.MD documentation. Loaded from <code>src/README.MD</code>. Can be <code>None</code> if the file is not found or cannot be parsed.</p>



<p><code>__project_name__</code>: Name of the project.  Defaults to 'hypotez'. Retrieved from the <code>settings.json</code> file if available.</p>
<p><code>__version__</code>: Version of the project. Retrieved from the <code>settings.json</code> file if available.</p>
<p><code>__doc__</code>: Documentation string. Defaults to an empty string, loaded from <code>src/README.MD</code> if available.</p>
<p><code>__details__</code>: Extra details string.  Defaults to an empty string.</p>
<p><code>__author__</code>: Author of the project. Retrieved from the <code>settings.json</code> file if available.</p>
<p><code>__copyright__</code>: Copyright information for the project. Retrieved from the <code>settings.json</code> file if available.</p>
<p><code>__cofee__</code>: Information on how to support developers.  Defaults to a specific link, loaded from <code>settings.json</code> if available.</p>