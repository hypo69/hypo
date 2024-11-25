html
<h1>Module: hypotez/src/goog/header.py</h1>

<h2>Overview</h2>
<p>This module provides functions for setting the project root directory and loading project settings and documentation.</p>

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
  <li><em>No exceptions are explicitly raised by this function.</em></li>
</ul>


<h3><code><a name='set_project_root'></a>set_project_root(marker_files=(\'pyproject.toml\', \'requirements.txt\', \'.git\')) -> Path</code></h3>

<p><strong>Description</strong>: Finds the root directory of the project starting from the current file's directory, searching upwards and stopping at the first directory containing any of the marker files.</p>

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
  <li><em>No exceptions are explicitly raised by this function.</em></li>
</ul>


<hr>

<h2>Variables</h2>

<h3><code>MODE</code></h3>

<p><strong>Description</strong>:  A string variable, likely defining the project's mode (e.g., 'dev', 'prod').</p>

<p><strong>Value</strong>: 'dev'</p>

<h3><code>__root__</code></h3>

<p><strong>Description</strong>:  The path to the project root directory, set by the <code>set_project_root</code> function.</p>

<h3><code>settings</code></h3>

<p><strong>Description</strong>: A dictionary containing project settings loaded from <code>settings.json</code>.</p>


<h3><code>doc_str</code></h3>

<p><strong>Description</strong>: A string containing the project documentation loaded from <code>README.MD</code>.</p>

<h3><code>__project_name__</code></h3>

<p><strong>Description</strong>: The project name, obtained from the <code>settings</code> dictionary or set to 'hypotez' if no settings are available or the key is not found.</p>

<h3><code>__version__</code></h3>

<p><strong>Description</strong>: The project version, obtained from the <code>settings</code> dictionary or set to an empty string if no settings are available or the key is not found.</p>

<h3><code>__doc__</code></h3>

<p><strong>Description</strong>: The project documentation string, obtained from the <code>doc_str</code> variable or set to an empty string if no documentation is available.</p>


<h3><code>__details__</code></h3>

<p><strong>Description</strong>: A string, likely containing detailed information about the project.</p>


<h3><code>__author__</code></h3>

<p><strong>Description</strong>: The author of the project, obtained from the <code>settings</code> dictionary or set to an empty string if no settings are available or the key is not found.</p>


<h3><code>__copyright__</code></h3>

<p><strong>Description</strong>: The copyright information, obtained from the <code>settings</code> dictionary or set to an empty string if no settings are available or the key is not found.</p>


<h3><code>__cofee__</code></h3>

<p><strong>Description</strong>: A string containing information about how to support the project developers.</p>