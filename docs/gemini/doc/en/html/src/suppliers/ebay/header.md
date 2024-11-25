html
<h1>hypotez/src/suppliers/ebay/header.py</h1>

<h2>Overview</h2>
<p>This module defines functions for setting the project root directory and loading project settings.</p>

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

<p><strong>Description</strong>: Finds the root directory of the project starting from the current file's directory.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>marker_files</code> (tuple, optional): Filenames or directory names to identify the project root. Defaults to a tuple containing 'pyproject.toml', 'requirements.txt', and '.git'.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Path</code>: Path to the root directory if found, otherwise the directory where the script is located.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li>No exceptions are explicitly raised.</li>
</ul>


<h2>Variables</h2>

<h3><code>__root__</code></h3>

<p><strong>Description</strong>: A variable representing the path to the project root directory. Initialized by the <code>set_project_root</code> function. (Path object)</p>


<h3><code>settings</code></h3>

<p><strong>Description</strong>: A dictionary containing project settings. Loaded from <code>settings.json</code>. May be <code>None</code> if the file doesn't exist or is invalid JSON.</p> (dict or None)


<h3><code>doc_str</code></h3>

<p><strong>Description</strong>: A string containing the project documentation, loaded from <code>README.MD</code>.  May be <code>None</code> if the file is missing or an error occurs during reading.</p> (str or None)



<h3><code>__project_name__</code></h3>

<p><strong>Description</strong>: Project name, retrieved from the settings. Defaults to "hypotez".</p> (str)


<h3><code>__version__</code></h3>

<p><strong>Description</strong>: Project version, retrieved from the settings. Defaults to an empty string.</p> (str)


<h3><code>__doc__</code></h3>

<p><strong>Description</strong>: Project documentation, retrieved from the settings. Defaults to an empty string.</p> (str)


<h3><code>__details__</code></h3>

<p><strong>Description</strong>: Project details, retrieved from the settings. Defaults to an empty string.</p> (str)


<h3><code>__author__</code></h3>

<p><strong>Description</strong>: Project author, retrieved from the settings. Defaults to an empty string.</p> (str)


<h3><code>__copyright__</code></h3>

<p><strong>Description</strong>: Project copyright, retrieved from the settings. Defaults to an empty string.</p> (str)


<h3><code>__cofee__</code></h3>

<p><strong>Description</strong>: Project author's coffee link, retrieved from the settings. Defaults to a link.</p> (str)