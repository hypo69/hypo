html
<h1>hypotez/src/webdriver/bs/header.py</h1>

<h2>Overview</h2>
<p>This module defines functions for setting the project root directory and retrieving project settings from a JSON file.  It also handles potential errors during file reading.</p>

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

<p><strong>Raises</strong>:</p>
<ul>
  <li>None</li>
</ul>


<h3><code><ins>__init__</ins></code></h3>

<p><strong>Description</strong>: Initializes the module by setting the project root and loading settings.</p>

<p><strong>Returns</strong>:</p>
<ul>
 <li>None (Implicitly returns a global variable) </li>
</ul>



<p><strong>Raises</strong>:</p>
<ul>
  <li><code>FileNotFoundError</code>: Raised if the 'settings.json' file is not found.</li>
  <li><code>json.JSONDecodeError</code>: Raised if the 'settings.json' file is not valid JSON.</li>
 <li>None </li>
</ul>


<h3><code><ins>__init__</ins></code></h3>

<p><strong>Description</strong>: Initializes the module by setting the project root and loading the project documentation from a README.MD file.</p>

<p><strong>Returns</strong>:</p>
<ul>
 <li>None (Implicitly returns a global variable) </li>
</ul>



<p><strong>Raises</strong>:</p>
<ul>
  <li><code>FileNotFoundError</code>: Raised if the 'README.MD' file is not found.</li>
  <li><code>json.JSONDecodeError</code>: Raised if the 'README.MD' file is not valid JSON.</li>
 <li>None </li>
</ul>


<p><strong>Global Variables</strong></p>


<ul>
  <li><code>__root__</code> (Path): Path to the root directory of the project.  Initialized by <code>set_project_root</code>.</li>
    <li><code>settings</code> (dict): Project settings loaded from 'settings.json'.</li>
    <li><code>doc_str</code> (str):  Project documentation loaded from 'README.MD'.</li>
  <li><code>__project_name__</code> (str):  Project name from settings or 'hypotez' if not found.</li>
  <li><code>__version__</code> (str): Project version from settings or '' if not found.</li>
  <li><code>__doc__</code> (str): Project documentation, from 'README.MD' or ''.</li>
  <li><code>__details__</code> (str): Project details.</li>
  <li><code>__author__</code> (str): Project author.</li>
  <li><code>__copyright__</code> (str): Project copyright.</li>
  <li><code>__cofee__</code> (str): Link to coffee support.</li>
</ul>