html
<h1>Module: hypotez/src/ai/helicone/header.py</h1>

<h2>Overview</h2>
<p>This module defines the root path to the project. All imports are built relative to this path.</p>
<p><b>TODO</b>: In the future, move this to a system variable.</p>


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
  <li><code>marker_files</code> (tuple, optional): Filenames or directory names to identify the project root. Defaults to ('pyproject.toml', 'requirements.txt', '.git').</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Path</code>: Path to the root directory if found, otherwise the directory where the script is located.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>FileNotFoundError</code>: If no marker files are found in any parent directory.</li>
</ul>


<h2>Global Variables</h2>

<h3><code>__root__</code></h3>

<p><strong>Description</strong>: Path to the root directory of the project.</p>

<h3><code>settings</code></h3>
<p><strong>Description</strong>: Dictionary containing project settings loaded from <code>settings.json</code>.</p>

<p><strong>Type</strong>: dict</p>

<h3><code>doc_str</code></h3>
<p><strong>Description</strong>: String containing the project documentation (README.md).</p>
<p><strong>Type</strong>: str</p>


<h3><code>__project_name__</code></h3>
<p><strong>Description</strong>: Project name. Defaults to "hypotez" if settings.json is not found or does not contain a project_name.</p>

<h3><code>__version__</code></h3>

<p><strong>Description</strong>: Project version.</p>

<h3><code>__doc__</code></h3>

<p><strong>Description</strong>: Project documentation string.</p>


<h3><code>__details__</code></h3>
<p><strong>Description</strong>: Additional project details.</p>
<h3><code>__author__</code></h3>
<p><strong>Description</strong>: Author of the project.</p>
<h3><code>__copyright__</code></h3>
<p><strong>Description</strong>: Copyright information.</p>
<h3><code>__cofee__</code></h3>
<p><strong>Description</strong>: Link to a coffee donation button.</p>