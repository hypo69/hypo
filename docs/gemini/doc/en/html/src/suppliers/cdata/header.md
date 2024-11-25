html
<h1>hypotez/src/suppliers/cdata/header.py</h1>

<h2>Overview</h2>
<p>This module defines functions for setting the project root directory and loading project settings.</p>

<h2>Functions</h2>

<h3><code>set_project_root</code></h3>

<p><strong>Description</strong>: Finds the root directory of the project.</p>

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
</ul>

<p><strong>Example Usage</strong> (Illustrative):</p>
<pre><code class="language-python">
project_root = set_project_root()
print(f"Project root: {project_root}")
</code></pre>


<h2>Variables</h2>
<h3><code>__root__</code></h3>

<p><strong>Description</strong>: Path to the root directory of the project, set by the <code>set_project_root</code> function.  This is an internal variable.</p>
<p><strong>Type</strong>:  <code>Path</code></p>
<p><strong>Usage</strong>:  Used within the module to access project resources.</p>

<h3><code>settings</code></h3>

<p><strong>Description</strong>: Dictionary containing project settings loaded from <code>settings.json</code>.</p>
<p><strong>Type</strong>: <code>dict</code></p>
<p><strong>Usage</strong>: Provides access to project configuration information.</p>


<h3><code>doc_str</code></h3>

<p><strong>Description</strong>: String containing the project's documentation from <code>README.MD</code>.</p>
<p><strong>Type</strong>: <code>str</code></p>
<p><strong>Usage</strong>:  Provides a place to store the project documentation (if available).</p>

<h3><code>__project_name__</code></h3>

<p><strong>Description</strong>: Name of the project (obtained from <code>settings.json</code>, defaults to 'hypotez').</p>
<p><strong>Type</strong>: <code>str</code></p>
<p><strong>Usage</strong>: Used for project identification and references.</p>

<h3><code>__version__</code></h3>

<p><strong>Description</strong>: Project version (obtained from <code>settings.json</code>, defaults to '').</p>
<p><strong>Type</strong>: <code>str</code></p>
<p><strong>Usage</strong>:  Indicates the version of the project.</p>

<h3><code>__doc__</code></h3>

<p><strong>Description</strong>: Project documentation (obtained from <code>README.MD</code>, defaults to '').</p>
<p><strong>Type</strong>: <code>str</code></p>
<p><strong>Usage</strong>:  Stores the project's documentation text.</p>


<h3><code>__details__</code></h3>

<p><strong>Description</strong>: Placeholder for additional project details (empty by default).</p>
<p><strong>Type</strong>: <code>str</code></p>
<p><strong>Usage</strong>: Can be used to store other pertinent project data.</p>

<h3><code>__author__</code></h3>

<p><strong>Description</strong>: Project author (obtained from <code>settings.json</code>, defaults to '').</p>
<p><strong>Type</strong>: <code>str</code></p>
<p><strong>Usage</strong>: Indicates the author of the project.</p>

<h3><code>__copyright__</code></h3>

<p><strong>Description</strong>: Project copyright (obtained from <code>settings.json</code>, defaults to '').</p>
<p><strong>Type</strong>: <code>str</code></p>
<p><strong>Usage</strong>: Indicates the copyright holder of the project.</p>


<h3><code>__cofee__</code></h3>

<p><strong>Description</strong>: Link to donate a cup of coffee to the developer (obtained from <code>settings.json</code>, default to a predefined URL).</p>
<p><strong>Type</strong>: <code>str</code></p>
<p><strong>Usage</strong>: Provide support to the project developers.</p>