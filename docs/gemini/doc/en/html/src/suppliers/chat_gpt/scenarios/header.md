html
<h1>hypotez/src/suppliers/chat_gpt/scenarios/header.py</h1>

<h2>Overview</h2>
<p>This module provides functions for setting the project root directory and loading project settings from a JSON file.</p>

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


<h3><code>set_project_root</code></h3>

<p><strong>Description</strong>: Finds the root directory of the project starting from the current file's directory, searching upwards and stopping at the first directory containing any of the marker files.</p>

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
  <li>No exceptions are explicitly raised, but the function might implicitly raise exceptions if there are issues interacting with the file system.</li>
</ul>


<p><strong>Example Usage</strong>:</p>
<pre><code class="language-python">
__root__ = set_project_root()
print(__root__)
</code></pre>


<h2>Variables</h2>

<h3><code>__root__</code></h3>

<p><strong>Description</strong>: Path to the root directory of the project.  Initialized by calling the <code>set_project_root</code> function.</p>
<p><strong>Type</strong>: <code>Path</code></p>


<h3><code>settings</code></h3>

<p><strong>Description</strong>: Project settings loaded from <code>settings.json</code>. If the file is not found or contains invalid JSON, <code>settings</code> will be <code>None</code>.</p>
<p><strong>Type</strong>: <code>dict</code> or <code>None</code></p>


<h3><code>doc_str</code></h3>

<p><strong>Description</strong>: Content of the project's README.MD file if found, otherwise <code>None</code>.</p>
<p><strong>Type</strong>: <code>str</code> or <code>None</code></p>


<h3><code>__project_name__</code></h3>

<p><strong>Description</strong>: Name of the project, retrieved from the <code>settings.json</code> file. Defaults to 'hypotez' if not found.</p>
<p><strong>Type</strong>: <code>str</code></p>


<h3><code>__version__</code></h3>

<p><strong>Description</strong>: Version of the project, retrieved from the <code>settings.json</code> file. Defaults to an empty string if not found.</p>
<p><strong>Type</strong>: <code>str</code></p>


<h3><code>__doc__</code></h3>

<p><strong>Description</strong>: Documentation string for the project, retrieved from the README.MD file if found.</p>
<p><strong>Type</strong>: <code>str</code></p>

<h3><code>__details__</code></h3>
<p><strong>Description</strong>: Project details (currently empty).</p>
<p><strong>Type</strong>: <code>str</code></p>

<h3><code>__author__</code></h3>
<p><strong>Description</strong>: Project author, retrieved from the <code>settings.json</code> file.</p>
<p><strong>Type</strong>: <code>str</code></p>

<h3><code>__copyright__</code></h3>
<p><strong>Description</strong>: Project copyright, retrieved from the <code>settings.json</code> file.</p>
<p><strong>Type</strong>: <code>str</code></p>


<h3><code>__cofee__</code></h3>
<p><strong>Description</strong>: A string containing a message encouraging users to treat the developer to a cup of coffee.</p>
<p><strong>Type</strong>: <code>str</code></p>