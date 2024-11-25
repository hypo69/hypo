html
<h1>hypotez/src/fast_api/header.py</h1>

<h2>Overview</h2>
<p>This module defines functions for setting the project root directory and loading project settings.</p>

<h2>Functions</h2>

<h3><code>set_project_root</code></h3>

<p><strong>Description</strong>: Finds the root directory of the project.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>marker_files</code> (tuple): Filenames or directory names to identify the project root.  Defaults to ('pyproject.toml', 'requirements.txt', '.git').</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Path</code>: Path to the root directory if found, otherwise the directory where the script is located.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li>No exceptions are explicitly raised.</li>
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
  <li>None</li>
</ul>


<p><strong>Example Usage</strong> (Illustrative):</p>
<pre><code>python
root_path = set_project_root()
print(root_path)
</code></pre>


<h2>Variables</h2>
<h3><code>MODE</code></h3>

<p><strong>Description</strong>: A string variable holding the current project mode (e.g., 'dev', 'prod').</p>


<h3><code>__root__</code></h3>

<p><strong>Description</strong>:  A Path object representing the root directory of the project.</p>


<h3><code>settings</code></h3>

<p><strong>Description</strong>: A dictionary containing project settings loaded from settings.json.  Can be None if the file is missing or invalid.</p>


<h3><code>doc_str</code></h3>

<p><strong>Description</strong>: A string containing the content of the project's README.md file. Can be None if the file is missing or invalid.</p>


<h3><code>__project_name__</code></h3>

<p><strong>Description</strong>: The project name, taken from the settings.json file or defaulting to 'hypotez'.</p>

<h3><code>__version__</code></h3>

<p><strong>Description</strong>: The project version, taken from the settings.json file or defaulting to an empty string.</p>


<h3><code>__doc__</code></h3>

<p><strong>Description</strong>: The project documentation, taken from the README.md file or defaulting to an empty string.</p>

<h3><code>__details__</code></h3>

<p><strong>Description</strong>: The project details, initialized as an empty string.</p>


<h3><code>__author__</code></h3>

<p><strong>Description</strong>: The author of the project, taken from the settings.json file or defaulting to an empty string.</p>


<h3><code>__copyright__</code></h3>

<p><strong>Description</strong>: The copyright information of the project, taken from the settings.json file or defaulting to an empty string.</p>


<h3><code>__cofee__</code></h3>

<p><strong>Description</strong>: A string containing a link to support the project's developer through coffee donations. Defaults to a specific URL if no donation link is available in the settings file.</p>


<p><strong>Important Note:</strong> The docstrings for variables are not necessarily complete and illustrative since a variable's docstring rarely provides the level of detail found in function docstrings. In practice, the documentation for these variables might be more substantial, or they could be missing entirely.</p>