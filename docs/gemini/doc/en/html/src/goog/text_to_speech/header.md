html
<h1>Module: hypotez/src/goog/text_to_speech/header.py</h1>

<h2>Overview</h2>
<p>This module defines a function to find the root directory of a project and sets the project root in the Python path. It also loads project settings from a JSON file and optionally a README.md file. The module imports necessary libraries like <code>sys</code>, <code>json</code>, <code>pathlib</code>, and <code>packaging.version</code>, and utilizes functions from the <code>src</code> and <code>gs</code> modules.</p>

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


<h3><code>set_project_root</code></h3>

<p><strong>Description</strong>: Finds the root directory of the project starting from the current file's directory, searching upwards and stopping at the first directory containing any of the marker files.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>marker_files</code> (tuple, optional): Filenames or directory names to identify the project root. Defaults to ('pyproject.toml', 'requirements.txt', '.git').</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Path</code>: Path to the root directory if found, otherwise the directory where the script is located.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li>No exceptions are explicitly raised by this function.</li>
</ul>

<h2>Variables</h2>

<h3><code>MODE</code></h3>

<p><strong>Description</strong>: Stores the mode, currently set to 'dev'.</p>
<p><strong>Type</strong>: str</p>


<h3><code>__root__</code></h3>

<p><strong>Description</strong>: Stores the Path object representing the root directory of the project.</p>
<p><strong>Type</strong>: Path</p>


<h3><code>settings</code></h3>

<p><strong>Description</strong>: Stores the project settings loaded from the 'settings.json' file.</p>
<p><strong>Type</strong>: dict or None</p>

<h3><code>doc_str</code></h3>

<p><strong>Description</strong>: Stores the content read from the 'README.MD' file (if exists).</p>
<p><strong>Type</strong>: str or None</p>

<h3><code>__project_name__</code></h3>

<p><strong>Description</strong>: The name of the project, obtained from the <code>settings</code> dictionary, or defaults to 'hypotez'.</p>
<p><strong>Type</strong>: str</p>

<h3><code>__version__</code></h3>

<p><strong>Description</strong>: The version of the project, obtained from the <code>settings</code> dictionary, or defaults to an empty string.</p>
<p><strong>Type</strong>: str</p>

<h3><code>__doc__</code></h3>

<p><strong>Description</strong>: The documentation string, obtained from the <code>doc_str</code>, or defaults to an empty string.</p>
<p><strong>Type</strong>: str</p>

<h3><code>__details__</code></h3>

<p><strong>Description</strong>: Contains details about the project (currently empty).</p>
<p><strong>Type</strong>: str</p>

<h3><code>__author__</code></h3>

<p><strong>Description</strong>: The author of the project, obtained from the <code>settings</code> dictionary, or defaults to an empty string.</p>
<p><strong>Type</strong>: str</p>

<h3><code>__copyright__</code></h3>

<p><strong>Description</strong>: The copyright information for the project, obtained from the <code>settings</code> dictionary, or defaults to an empty string.</p>
<p><strong>Type</strong>: str</p>

<h3><code>__cofee__</code></h3>

<p><strong>Description</strong>: Contains the coffee donation link for the developer (or default message).</p>
<p><strong>Type</strong>: str</p>


<p><strong>Raises</strong>:</p>
<ul>
  <li><code>FileNotFoundError</code>: If 'settings.json' or 'README.MD' is not found.</li>
  <li><code>json.JSONDecodeError</code>: If 'settings.json' contains invalid JSON.</li>
</ul>