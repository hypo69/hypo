html
<h1>Module: hypotez/src/suppliers/aliexpress/campaign/header.py</h1>

<h2>Overview</h2>
<p>This module defines a function to find the project root directory and loads settings from a JSON file.</p>

<h2>Functions</h2>

<h3><code>set_project_root</code></h3>

<p><strong>Description</strong>: Finds the root directory of the project starting from the current file's directory, searching upwards and stopping at the first directory containing any of the marker files.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>marker_files</code> (tuple): Filenames or directory names to identify the project root.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Path</code>: Path to the root directory if found, otherwise the directory where the script is located.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li>No exceptions are explicitly raised, but searching for files could raise exceptions, if not found.
 </ul>


<!-- Add other functions here, following the format above -->

<h2>Variables</h2>

<h3><code>__root__</code></h3>

<p><strong>Description</strong>: Path to the root directory of the project.</p>

<h3><code>settings</code></h3>
<p><strong>Description</strong>: A dictionary containing project settings loaded from <code>settings.json</code>.</p>

<p><strong>Type</strong>: dict</p>

<p><strong>Default</strong>: <code>None</code></p>

<p><strong>Notes</strong>: The variable is loaded from the file located at <code>gs.path.root / 'src' / 'settings.json'</code> and is populated with the JSON content of this file if the file exists and the JSON is valid.</p>

<h3><code>doc_str</code></h3>
<p><strong>Description</strong>: String containing documentation content from <code>README.MD</code> file.</p>

<p><strong>Type</strong>: str</p>

<p><strong>Default</strong>: <code>None</code></p>

<p><strong>Notes</strong>: Loaded from the file located at <code>gs.path.root / 'src' / 'README.MD'</code> if the file exists.</p>


<h3><code>__project_name__</code></h3>

<p><strong>Description</strong>: Project name. Retrieves the <code>project_name</code> value from the <code>settings</code> dictionary. If <code>settings</code> is <code>None</code> or the key is not found, defaults to 'hypotez'.</p>

<p><strong>Type</strong>: str</p>


<h3><code>__version__</code></h3>

<p><strong>Description</strong>: Project version. Retrieves the <code>version</code> value from the <code>settings</code> dictionary. If <code>settings</code> is <code>None</code> or the key is not found, defaults to ''.</p>

<p><strong>Type</strong>: str</p>


<h3><code>__doc__</code></h3>

<p><strong>Description</strong>: Project documentation.  If <code>doc_str</code> is not <code>None</code>, use the value of <code>doc_str</code>, otherwise use an empty string.</p>

<p><strong>Type</strong>: str</p>

<h3><code>__details__</code></h3>
<p><strong>Description</strong>: Project details. Initialized as an empty string.</p>

<p><strong>Type</strong>: str</p>

<h3><code>__author__</code></h3>
<p><strong>Description</strong>: Project author. Retrieves the <code>author</code> value from the <code>settings</code> dictionary. If <code>settings</code> is <code>None</code> or the key is not found, defaults to ''.</p>
<p><strong>Type</strong>: str</p>

<h3><code>__copyright__</code></h3>

<p><strong>Description</strong>: Project copyright. Retrieves the <code>copyright</code> value from the <code>settings</code> dictionary. If <code>settings</code> is <code>None</code> or the key is not found, defaults to ''.</p>
<p><strong>Type</strong>: str</p>

<h3><code>__cofee__</code></h3>

<p><strong>Description</strong>: Author's coffee link. Retrieves the <code>cofee</code> value from the <code>settings</code> dictionary. If <code>settings</code> is <code>None</code> or the key is not found, defaults to a string containing a link to support the author through coffee.</p>
<p><strong>Type</strong>: str</p>