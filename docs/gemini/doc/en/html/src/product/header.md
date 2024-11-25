html
<h1>hypotez/src/product/header.py</h1>

<h2>Overview</h2>
<p>This module defines the root path to the project. All imports are based on this path.</p>
<p>TODO: In the future, move this to a system variable.</p>

<h2>Constants</h2>

<h3><code>MODE</code></h3>

<p><strong>Description</strong>: Specifies the current development mode.</p>
<p><strong>Value</strong>: 'dev'</p>

<h2>Functions</h2>

<h3><code>set_project_root</code></h3>

<p><strong>Description</strong>: Finds the root directory of the project, starting from the current file's directory, searching upwards until it finds a directory containing any of the specified marker files.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>marker_files</code> (tuple): Filenames or directory names to identify the project root.  Defaults to ('pyproject.toml', 'requirements.txt', '.git').</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Path</code>: Path to the root directory if found, otherwise the directory where the script is located.</li>
</ul>


<h3><code>set_project_root</code></h3>

<p><strong>Description</strong>: Finds the root directory of the project starting from the current file's directory, searching upwards and stopping at the first directory containing any of the marker files.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>marker_files</code> (tuple, optional): Filenames or directory names to identify the project root. Defaults to ('pyproject.toml', 'requirements.txt', '.git').</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Path</code>: Path to the root directory if found; otherwise, the directory containing the current script.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li>No exceptions are explicitly raised.</li>
</ul>


<h2>Variables</h2>

<h3><code>__root__</code></h3>

<p><strong>Description</strong>: Path to the root directory of the project. Initialized by the `set_project_root` function.</p>
<p><strong>Type</strong>: <code>Path</code></p>

<h3><code>settings</code></h3>

<p><strong>Description</strong>: Project settings loaded from settings.json.</p>
<p><strong>Type</strong>: <code>dict</code></p>
<p><strong>Initial Value</strong>: <code>None</code></p>

<h3><code>doc_str</code></h3>

<p><strong>Description</strong>: Project documentation string loaded from README.md.</p>
<p><strong>Type</strong>: <code>str</code></p>
<p><strong>Initial Value</strong>: <code>None</code></p>


<h3><code>__project_name__</code></h3>

<p><strong>Description</strong>: Project name obtained from the settings. Defaults to 'hypotez' if settings are not available or missing the 'project_name' key.</p>
<p><strong>Type</strong>: <code>str</code></p>


<h3><code>__version__</code></h3>

<p><strong>Description</strong>: Project version obtained from the settings. Defaults to '' if settings are not available or missing the 'version' key.</p>
<p><strong>Type</strong>: <code>str</code></p>


<h3><code>__doc__</code></h3>

<p><strong>Description</strong>: Project documentation string loaded from README.md. Defaults to '' if not found.</p>
<p><strong>Type</strong>: <code>str</code></p>


<h3><code>__details__</code></h3>

<p><strong>Description</strong>: Project details string (currently empty).</p>
<p><strong>Type</strong>: <code>str</code></p>


<h3><code>__author__</code></h3>

<p><strong>Description</strong>: Author information from the settings. Defaults to '' if settings are not available or missing the 'author' key.</p>
<p><strong>Type</strong>: <code>str</code></p>


<h3><code>__copyright__</code></h3>

<p><strong>Description</strong>: Copyright information from the settings. Defaults to '' if settings are not available or missing the 'copyright' key.</p>
<p><strong>Type</strong>: <code>str</code></p>


<h3><code>__cofee__</code></h3>

<p><strong>Description</strong>: Contact information for supporting the project via coffee. Defaults to a specific link if settings are not available or missing the 'cofee' key.</p>
<p><strong>Type</strong>: <code>str</code></p>