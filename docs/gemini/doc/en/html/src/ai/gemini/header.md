html
<h1>hypotez/src/ai/gemini/header.py</h1>

<h2>Overview</h2>
<p>This module defines the root path to the project. All imports are built relative to this path.</p>
<p>Future implementation will involve moving the root path definition to a system-level variable.</p>


<h2>Functions</h2>

<h3><code>set_project_root</code></h3>

<p><strong>Description</strong>: Finds the root directory of the project, starting from the current file's directory, searching upwards and stopping at the first directory containing any of the marker files.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>marker_files</code> (tuple): Filenames or directory names used to identify the project root. Defaults to a tuple containing 'pyproject.toml', 'requirements.txt', and '.git'.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Path</code>: Path to the root directory if found, otherwise the directory where the script is located.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li>None</li>
</ul>


<h3><code>set_project_root</code></h3>

<p><strong>Description</strong>: Finds the root directory of the project starting from the current file's directory, searching upwards and stopping at the first directory containing any of the marker files.
</p>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>marker_files</code> (tuple, optional): A tuple of filenames or directory names to identify the project root. Defaults to ('pyproject.toml', 'requirements.txt', '.git').
</li>
</ul>
<p><strong>Returns</strong>:</p>
<ul><li><code>Path</code>: The path to the root directory if found.  Otherwise, the directory containing the script.</li></ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li>None</li>
</ul>


<h2>Variables</h2>

<h3><code>__root__</code></h3>

<p><strong>Description</strong>: Path to the root directory of the project.  Set by the <code>set_project_root()</code> function.
</p>

<p><strong>Type</strong>: <code>Path</code></p>

<h2>Modules</h2>

<h3><code>sys</code></h3>
<p>Python's built-in module for interacting with system-level aspects, such as manipulating the path.</p>

<h3><code>json</code></h3>
<p>Python's built-in module for working with JSON data.</p>

<h3><code>pathlib</code></h3>
<p>Python module for working with paths.</p>

<h3><code>packaging.version</code></h3>
<p>Provides tools for working with software versions.</p>


<h2>Module Constants</h2>

<h3><code>MODE</code></h3>
<p><strong>Description</strong>: A string representing the current project mode.  It's currently set to 'dev'.</p>
<p><strong>Type</strong>: <code>str</code></p>


<h2>Global Variables</h2>

<h3><code>settings</code></h3>

<p><strong>Description</strong>: A dictionary storing project settings.  Loaded from <code>settings.json</code> file in the 'src' directory of the root project.
</p>
<p><strong>Type</strong>: <code>dict</code></p>


<h3><code>doc_str</code></h3>

<p><strong>Description</strong>: Contains the content of the <code>README.MD</code> file in the project's root directory.</p>
<p><strong>Type</strong>: <code>str</code></p>

<h3><code>__project_name__</code></h3>

<p><strong>Description</strong>: Name of the project. Defaults to 'hypotez'. Retrieved from <code>settings.json</code>.</p>
<p><strong>Type</strong>: <code>str</code></p>

<h3><code>__version__</code></h3>

<p><strong>Description</strong>: Version of the project.  Retrieved from <code>settings.json</code>.</p>
<p><strong>Type</strong>: <code>str</code></p>
<h3><code>__doc__</code></h3>

<p><strong>Description</strong>: Documentation string. Retrieved from <code>README.MD</code> file if available.</p>
<p><strong>Type</strong>: <code>str</code></p>

<h3><code>__details__</code></h3>
<p><strong>Description</strong>: Details about the project.  Currently an empty string.</p>
<p><strong>Type</strong>: <code>str</code></p>

<h3><code>__author__</code></h3>

<p><strong>Description</strong>: Author of the project. Retrieved from <code>settings.json</code>.</p>
<p><strong>Type</strong>: <code>str</code></p>

<h3><code>__copyright__</code></h3>

<p><strong>Description</strong>: Copyright information. Retrieved from <code>settings.json</code>.</p>
<p><strong>Type</strong>: <code>str</code></p>

<h3><code>__cofee__</code></h3>

<p><strong>Description</strong>: A string containing a link to a donation platform for the developer.</p>
<p><strong>Type</strong>: <code>str</code></p>