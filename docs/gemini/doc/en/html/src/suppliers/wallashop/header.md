html
<h1>Module: hypotez/src/suppliers/wallashop/header.py</h1>

<h2>Overview</h2>
<p>This module defines a function to find the project root directory and loads settings from a JSON file. It also retrieves the project name, version, documentation, details, author, copyright, and a coffee link from the settings file or default values.</p>

<h2>Functions</h2>

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


<p><strong>Example Usage</strong>:
```python
project_root = set_project_root()
print(project_root)
```
</p>


<h2>Variables</h2>

<h3><code>__root__</code></h3>

<p><strong>Description</strong>: Path to the root directory of the project, obtained by calling the <code>set_project_root()</code> function.</p>

<p><strong>Type</strong>: <code>Path</code></p>

<h3><code>settings</code></h3>

<p><strong>Description</strong>: A dictionary containing project settings loaded from settings.json.</p>

<p><strong>Type</strong>: <code>dict</code></p>


<h3><code>doc_str</code></h3>

<p><strong>Description</strong>: Project documentation string, loaded from README.MD. </p>


<p><strong>Type</strong>: <code>str</code></p>


<h3><code>__project_name__</code></h3>

<p><strong>Description</strong>: Name of the project. Obtained from the settings, falling back to 'hypotez'.</p>

<p><strong>Type</strong>: <code>str</code></p>


<h3><code>__version__</code></h3>

<p><strong>Description</strong>: Version of the project. Obtained from the settings, falling back to an empty string.</p>

<p><strong>Type</strong>: <code>str</code></p>


<h3><code>__doc__</code></h3>

<p><strong>Description</strong>: Documentation string for the project. Obtained from the settings, falling back to an empty string.</p>

<p><strong>Type</strong>: <code>str</code></p>


<h3><code>__details__</code></h3>

<p><strong>Description</strong>: Details about the project (empty by default).</p>

<p><strong>Type</strong>: <code>str</code></p>


<h3><code>__author__</code></h3>

<p><strong>Description</strong>: Author of the project. Obtained from the settings, falling back to an empty string.</p>

<p><strong>Type</strong>: <code>str</code></p>


<h3><code>__copyright__</code></h3>

<p><strong>Description</strong>: Copyright information for the project. Obtained from the settings, falling back to an empty string.</p>

<p><strong>Type</strong>: <code>str</code></p>


<h3><code>__cofee__</code></h3>

<p><strong>Description</strong>: A link to support the developer through a coffee donation. Obtained from the settings, falling back to a default link.</p>

<p><strong>Type</strong>: <code>str</code></p>