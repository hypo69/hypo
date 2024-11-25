html
<h1>Module: hypotez.src.suppliers.morlevi.header</h1>

<h2>Overview</h2>
<p>This module defines functions for interacting with the settings and documentation for the project. It primarily focuses on locating the project root directory and loading settings from a JSON file.  It also attempts to retrieve documentation from a README.md file.</p>

<h2>Functions</h2>

<h3><code>set_project_root</code></h3>

<p><strong>Description</strong>: Finds the root directory of the project by searching up the directory tree from the current file's location. It searches for specific marker files to identify the project root. If the root is not found or is not in sys.path, it inserts the path to sys.path.</p>

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
  <li><code>marker_files</code> (tuple, optional): Filenames or directory names to identify the project root. Defaults to ('pyproject.toml', 'requirements.txt', '.git').</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Path</code>: Path to the root directory if found; otherwise, the directory containing the current file.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
<li>No exceptions are explicitly raised.</li>
</ul>

<h2>Global Variables</h2>
<p>This module also defines several global variables that hold information from the settings and documentation files, if they are successfully loaded.</p>

<h3><code>__root__</code></h3>

<p><strong>Description</strong>: A global variable storing the project root directory path retrieved by calling `set_project_root()`</p>
<p><strong>Type</strong>: Path</p>


<h3><code>settings</code></h3>

<p><strong>Description</strong>: A global variable that stores the settings loaded from `settings.json`. It defaults to None if the file is not found or cannot be parsed.</p>
<p><strong>Type</strong>: dict</p>


<h3><code>doc_str</code></h3>

<p><strong>Description</strong>: A global variable that contains the content read from the README.md file.  Defaults to None if not found or parseable.</p>
<p><strong>Type</strong>: str</p>


<h3><code>__project_name__</code></h3>

<p><strong>Description</strong>: The project name, retrieved from the settings, or defaults to 'hypotez'.</p>
<p><strong>Type</strong>: str</p>


<h3><code>__version__</code></h3>

<p><strong>Description</strong>: The project version, retrieved from the settings, or defaults to an empty string.</p>
<p><strong>Type</strong>: str</p>


<h3><code>__doc__</code></h3>

<p><strong>Description</strong>: The project documentation, retrieved from the README.md file or defaults to an empty string.</p>
<p><strong>Type</strong>: str</p>


<h3><code>__details__</code></h3>

<p><strong>Description</strong>: Placeholder for project details.</p>
<p><strong>Type</strong>: str</p>


<h3><code>__author__</code></h3>

<p><strong>Description</strong>: The author's name from the settings, or defaults to an empty string.</p>
<p><strong>Type</strong>: str</p>

<h3><code>__copyright__</code></h3>

<p><strong>Description</strong>: The copyright information from the settings, or defaults to an empty string.</p>
<p><strong>Type</strong>: str</p>


<h3><code>__cofee__</code></h3>

<p><strong>Description</strong>: Contact information for supporting the developers.</p>
<p><strong>Type</strong>: str</p>