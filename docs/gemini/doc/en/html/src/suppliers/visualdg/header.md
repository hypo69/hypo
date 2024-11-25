html
<h1>Module: hypotez/src/suppliers/visualdg/header.py</h1>

<h2>Overview</h2>
<p>This module defines functions for finding the project root directory and loading project settings.</p>

<h2>Functions</h2>

<h3><code>set_project_root</code></h3>

<p><strong>Description</strong>: Finds the root directory of the project by searching upwards from the current file's directory.</p>

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
  <li>N/A (No exceptions explicitly raised).</li>
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
  <li>N/A (No exceptions explicitly raised).</li>
</ul>


<h2>Variables</h2>

<h3><code>MODE</code></h3>

<p><strong>Description</strong>:  A string variable that represents the development mode. Its value is 'dev'.</p>


<h3><code>__root__</code></h3>

<p><strong>Description</strong>: A Path object representing the project root directory. Initialized by calling the <code>set_project_root</code> function.</p>


<h3><code>settings</code></h3>

<p><strong>Description</strong>: A dictionary containing project settings, loaded from <code>src/settings.json</code>.</p>

<p><strong>Type</strong>: <code>dict | None</code></p>


<p><strong>Loading Details</strong>: Loaded from the file <code>gs.path.root / 'src' / 'settings.json'</code>. If the file doesn't exist or is not a valid JSON file, it's set to <code>None</code>.</p>


<h3><code>doc_str</code></h3>

<p><strong>Description</strong>: A string variable containing the content of the project's <code>README.MD</code> file, if found. Otherwise, it's set to <code>None</code>.</p>

<p><strong>Type</strong>: <code>str | None</code></p>


<p><strong>Loading Details</strong>: Loaded from the file <code>gs.path.root / 'src' / 'README.MD'</code>. If the file doesn't exist or is not readable, it's set to <code>None</code>.</p>


<h3><code>__project_name__</code></h3>

<p><strong>Description</strong>: The project name, retrieved from the <code>settings</code> dictionary. Defaults to 'hypotez' if <code>settings</code> is not available or doesn't contain the key.</p>

<p><strong>Type</strong>: <code>str</code></p>


<h3><code>__version__</code></h3>

<p><strong>Description</strong>: The project version, retrieved from the <code>settings</code> dictionary. Defaults to an empty string if <code>settings</code> is not available or doesn't contain the key.</p>

<p><strong>Type</strong>: <code>str</code></p>

<h3><code>__doc__</code></h3>
<p><strong>Description</strong>: A string representing the project documentation. Defaults to an empty string if <code>doc_str</code> is not available.</p>


<h3><code>__details__</code></h3>
<p><strong>Description</strong>: A string representing project details. Its initial value is an empty string.</p>

<h3><code>__author__</code></h3>
<p><strong>Description</strong>: The author of the project, retrieved from the <code>settings</code> dictionary. Defaults to an empty string if <code>settings</code> is not available or doesn't contain the key.</p>


<h3><code>__copyright__</code></h3>
<p><strong>Description</strong>: The copyright information for the project, retrieved from the <code>settings</code> dictionary. Defaults to an empty string if <code>settings</code> is not available or doesn't contain the key.</p>


<h3><code>__cofee__</code></h3>
<p><strong>Description</strong>: Information for coffee support, retrieved from <code>settings</code>.  Defaults to a support link if <code>settings</code> is not available or doesn't contain the key.</p>