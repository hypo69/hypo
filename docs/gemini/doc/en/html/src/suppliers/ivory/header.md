html
<h1>Module: hypotez.src.suppliers.ivory.header</h1>

<h2>Overview</h2>
<p>This module defines functions for setting the project root directory and loading project settings from a JSON file. It leverages the `gs` module and the `packaging.version` library for handling versioning and project path management.</p>

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

<h3><code>set_project_root</code></h3>

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
  <li>None</li>
</ul>



<p><strong>Example Usage (Illustrative):</strong></p>
<pre><code>python
from pathlib import Path
project_root = set_project_root()
print(project_root)
</code></pre>

<p><strong>Note:</strong> This is a placeholder example.  The actual use case would depend on how the `set_project_root` function is used in other parts of the code. </p>


<h2>Variables</h2>

<h3><code>__root__</code></h3>

<p><strong>Description</strong>: Path to the root directory of the project.</p>
<p><strong>Type</strong>: Path</p>


<h3><code>settings</code></h3>

<p><strong>Description</strong>: Project settings loaded from settings.json.</p>
<p><strong>Type</strong>: dict</p>


<h3><code>doc_str</code></h3>

<p><strong>Description</strong>: Project documentation loaded from README.md.</p>
<p><strong>Type</strong>: str</p>

<h3><code>__project_name__</code></h3>

<p><strong>Description</strong>: Project name, defaults to 'hypotez' if not found in settings.</p>
<p><strong>Type</strong>: str</p>


<h3><code>__version__</code></h3>

<p><strong>Description</strong>: Project version, defaults to empty string if not found in settings.</p>
<p><strong>Type</strong>: str</p>

<h3><code>__doc__</code></h3>

<p><strong>Description</strong>: Project documentation, defaults to empty string if not found.</p>
<p><strong>Type</strong>: str</p>

<h3><code>__details__</code></h3>

<p><strong>Description</strong>: Project details, default to empty string.</p>
<p><strong>Type</strong>: str</p>


<h3><code>__author__</code></h3>

<p><strong>Description</strong>: Project author, defaults to empty string if not found in settings.</p>
<p><strong>Type</strong>: str</p>

<h3><code>__copyright__</code></h3>

<p><strong>Description</strong>: Project copyright, defaults to empty string if not found in settings.</p>
<p><strong>Type</strong>: str</p>

<h3><code>__cofee__</code></h3>

<p><strong>Description</strong>: A link to a way to support the developer, defaults to a link to a Boosty page.</p>
<p><strong>Type</strong>: str</p>