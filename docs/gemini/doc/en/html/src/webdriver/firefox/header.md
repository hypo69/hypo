html
<h1>hypotez/src/webdriver/firefox/header.py</h1>

<h2>Overview</h2>
<p>This module defines a function to locate the project root directory and initializes global settings. It also manages project metadata (name, version, author, etc.).</p>

<h2>Functions</h2>

<h3><code>set_project_root</code></h3>

<p><strong>Description</strong>: Locates the root directory of the project by searching upwards from the current file's directory, stopping at the first directory containing specific marker files (e.g., pyproject.toml, requirements.txt, .git).</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>marker_files</code> (tuple): A tuple of filenames or directory names to identify the project root. Defaults to ('pyproject.toml', 'requirements.txt', '.git').</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Path</code>: Path to the root directory if found, otherwise the directory where the script is located.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><em>No exceptions are explicitly raised.</em></li>
</ul>


<h3><code>set_project_root</code></h3>

<p><strong>Description</strong>: This function attempts to set the project root path based on the specified marker files.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>marker_files</code> (tuple): A tuple of filenames/directories to search for the project root. Defaults to ('pyproject.toml', 'requirements.txt', '.git').</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Path</code>: The path to the project root directory. Returns the directory of the current script if no marker files are found.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><em>No exceptions are explicitly raised.</em></li>
</ul>


<h2>Global Variables</h2>

<h3><code>MODE</code></h3>

<p><strong>Description</strong>: A string variable representing the development mode. Currently set to 'dev'.</p>


<h3><code>__root__</code></h3>

<p><strong>Description</strong>: A Path object representing the project root directory. Initialized by the <code>set_project_root</code> function.</p>


<h3><code>settings</code></h3>

<p><strong>Description</strong>: A dictionary containing project settings, loaded from <code>src/settings.json</code>. Defaults to <code>None</code> if the file is not found or if there's an error parsing the JSON.</p>

<h3><code>doc_str</code></h3>

<p><strong>Description</strong>: A string containing the content of the README.md file. Defaults to None if the file is not found or if there's an error reading the file.</p>

<h3><code>__project_name__</code></h3>

<p><strong>Description</strong>: A string representing the project name. Retrieved from the <code>settings</code> dictionary, falling back to 'hypotez' if no value is found or settings is None.</p>

<h3><code>__version__</code></h3>

<p><strong>Description</strong>: A string representing the project version. Retrieved from the <code>settings</code> dictionary, falling back to an empty string if no value is found or settings is None.</p>

<h3><code>__doc__</code></h3>

<p><strong>Description</strong>: A string containing the project documentation, or an empty string if no documentation is available.</p>


<h3><code>__details__</code></h3>

<p><strong>Description</strong>: A string containing project details (currently empty).</p>

<h3><code>__author__</code></h3>

<p><strong>Description</strong>: A string representing the project author. Retrieved from the <code>settings</code> dictionary, falling back to an empty string if no value is found or settings is None.</p>

<h3><code>__copyright__</code></h3>

<p><strong>Description</strong>: A string representing the project copyright. Retrieved from the <code>settings</code> dictionary, falling back to an empty string if no value is found or settings is None.</p>

<h3><code>__cofee__</code></h3>

<p><strong>Description</strong>: A string containing a link for the developer to receive coffee, a default string is provided if settings dictionary is empty or does not contain this key.</p>