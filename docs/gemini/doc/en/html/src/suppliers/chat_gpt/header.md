html
<h1>Module: hypotez/src/suppliers/chat_gpt/header.py</h1>

<h2>Overview</h2>
<p>This module provides functions for setting the project root directory and loading project settings from a JSON file.  It also handles potential exceptions during file loading.</p>

<h2>Functions</h2>

<h3><code>set_project_root</code></h3>

<p><strong>Description</strong>: Finds the root directory of the project starting from the current file's directory, searching upwards.  It stops at the first directory containing any of the specified marker files (pyproject.toml, requirements.txt, .git).</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>marker_files</code> (tuple): Filenames or directory names to identify the project root. Defaults to ('pyproject.toml', 'requirements.txt', '.git').</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Path</code>: Path to the root directory if found, otherwise the directory where the script is located.</li>
</ul>


<h3><code>set_project_root</code></h3>

<p><strong>Description</strong>: Finds the root directory of the project, starting from the current file's directory, searching upwards and stopping at the first directory containing any of the marker files provided. If the root directory is not already in `sys.path`, it's added.
</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>marker_files</code> (tuple, optional): Filenames or directory names to identify the project root. Defaults to a tuple containing 'pyproject.toml', 'requirements.txt', and '.git'.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Path</code>: Path to the root directory. If the root directory cannot be found, returns the directory where the script is located.</li>
</ul>
<p><strong>Raises</strong>:</p>
<ul>
  <li>None</li>
</ul>


<h2>Variables</h2>

<h3><code>__root__</code></h3>
<p><strong>Description</strong>:  Path to the root directory of the project, retrieved using the <code>set_project_root</code> function.  A variable for convenience.</p>
<p><strong>Type</strong>: Path</p>



<h3><code>settings</code></h3>
<p><strong>Description</strong>:  Dictionary containing project settings loaded from <code>settings.json</code>. Can be None if the file is not found or not valid JSON.</p>
<p><strong>Type</strong>: dict | None</p>



<h3><code>doc_str</code></h3>
<p><strong>Description</strong>: String containing the project documentation, typically from README.md. Can be None if the file isn't found.</p>
<p><strong>Type</strong>: str | None</p>




<h3><code>__project_name__</code></h3>
<p><strong>Description</strong>:  Name of the project, retrieved from the <code>settings</code> dictionary. Defaults to 'hypotez' if the key is not found or if settings are not loaded.</p>
<p><strong>Type</strong>: str</p>


<h3><code>__version__</code></h3>
<p><strong>Description</strong>: Version of the project, retrieved from the <code>settings</code> dictionary. Defaults to an empty string if the key is not found or if settings are not loaded.</p>
<p><strong>Type</strong>: str</p>


<h3><code>__doc__</code></h3>
<p><strong>Description</strong>:  Project documentation string. Defaults to an empty string if no documentation is loaded.</p>
<p><strong>Type</strong>: str</p>


<h3><code>__details__</code></h3>
<p><strong>Description</strong>:  Empty string representing project details. This variable is included but likely not used in the current context.</p>
<p><strong>Type</strong>: str</p>


<h3><code>__author__</code></h3>
<p><strong>Description</strong>: Author of the project, retrieved from the <code>settings</code> dictionary. Defaults to an empty string if the key is not found or if settings are not loaded.</p>
<p><strong>Type</strong>: str</p>


<h3><code>__copyright__</code></h3>
<p><strong>Description</strong>: Copyright information for the project, retrieved from the <code>settings</code> dictionary. Defaults to an empty string if the key is not found or if settings are not loaded.</p>
<p><strong>Type</strong>: str</p>


<h3><code>__cofee__</code></h3>
<p><strong>Description</strong>: Link to support the developer via a cup of coffee.</p>
<p><strong>Type</strong>: str</p>