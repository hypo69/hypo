html
<h1>Module: hypotez/src/suppliers/gearbest/header.py</h1>

<h2>Overview</h2>
<p>This module provides a function to find the root directory of a project and initializes project settings and documentation strings.</p>

<h2>Functions</h2>

<h3><code>set_project_root</code></h3>

<p><strong>Description</strong>: This function searches up the directory tree from the current file's location to find the project root directory based on the presence of specified marker files.  It ensures that the root directory is added to the Python path.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>marker_files</code> (tuple): A tuple of filenames or directory names to identify the project root. Defaults to ('pyproject.toml', 'requirements.txt', '.git').</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Path</code>: The path to the project root directory. If no matching directory is found, it returns the directory where the script is located.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li>None</li>
</ul>


<h3><code>__project_name__</code></h3>
<p><strong>Description</strong>: Gets the project name from the settings file or defaults to 'hypotez' if the settings file isn't found or doesn't contain a project name.</p>
<ul>
<li>Type: str</li>
</ul>

<h3><code>__version__</code></h3>
<p><strong>Description</strong>: Gets the project version from the settings file. If the settings file is not found or the version key is missing, it defaults to an empty string.</p>
<ul>
<li>Type: str</li>
</ul>


<h3><code>__doc__</code></h3>
<p><strong>Description</strong>: Gets the project documentation string from the README.md file if available; otherwise, it's an empty string.</p>
<ul>
<li>Type: str</li>
</ul>


<h3><code>__details__</code></h3>
<p><strong>Description</strong>: Gets project details, returning an empty string if the details aren't present in the settings file. </p>
<ul>
<li>Type: str</li>
</ul>


<h3><code>__author__</code></h3>
<p><strong>Description</strong>: Gets the author information from the settings file if available; otherwise, it's an empty string.</p>
<ul>
<li>Type: str</li>
</ul>


<h3><code>__copyright__</code></h3>
<p><strong>Description</strong>: Gets the copyright information from the settings file. If not found or the key is missing, it defaults to an empty string.</p>
<ul>
<li>Type: str</li>
</ul>


<h3><code>__cofee__</code></h3>
<p><strong>Description</strong>: Retrieves the coffee link from settings. Defaults to a standard link if not present.</p>
<ul>
<li>Type: str</li>
</ul>

<h2>Global Variables</h2>


<h3><code>MODE</code></h3>
<p><strong>Description</strong>: A global variable storing the project mode ('dev').</p>
<ul>
<li>Type: str</li>
</ul>


<h3><code>settings</code></h3>
<p><strong>Description</strong>: A global variable to store project settings loaded from settings.json.</p>
<ul>
<li>Type: dict</li>
</ul>
<h3><code>doc_str</code></h3>
<p><strong>Description</strong>: A global variable holding the content of the project's README.MD file.</p>
<ul>
<li>Type: str</li>
</ul>