html
<h1>hypotez/src/bots/header.py</h1>

<h2>Overview</h2>
<p>This module defines the root path to the project. All imports are built relative to this path.</p>

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
  <li>None</li>
</ul>


<h2>Global Variables</h2>

<h3><code>MODE</code></h3>

<p><strong>Description</strong>:  A string representing the project mode.  Currently set to 'dev'.</p>

<h3><code>__root__</code></h3>

<p><strong>Description</strong>: Path to the root directory of the project, determined by the <code>set_project_root</code> function. </p>
<p><strong>Type</strong>: <code>Path</code></p>

<h3><code>settings</code></h3>

<p><strong>Description</strong>:  A dictionary containing project settings loaded from settings.json.</p>
<p><strong>Type</strong>: <code>dict</code> or <code>None</code></p>

<h3><code>doc_str</code></h3>

<p><strong>Description</strong>: String containing the content of the README.MD file, if it exists.</p>
<p><strong>Type</strong>: <code>str</code> or <code>None</code></p>


<h3><code>__project_name__</code></h3>

<p><strong>Description</strong>: Project name obtained from the <code>settings</code> dictionary or defaults to 'hypotez' if not found.</p>
<p><strong>Type</strong>: <code>str</code></p>


<h3><code>__version__</code></h3>

<p><strong>Description</strong>: Project version obtained from the <code>settings</code> dictionary or defaults to an empty string if not found.</p>
<p><strong>Type</strong>: <code>str</code></p>

<h3><code>__doc__</code></h3>

<p><strong>Description</strong>:  Project documentation string obtained from the <code>README.MD</code> file, or defaults to an empty string if not found.</p>
<p><strong>Type</strong>: <code>str</code></p>


<h3><code>__details__</code></h3>

<p><strong>Description</strong>:  An empty string, currently no details are defined.</p>
<p><strong>Type</strong>: <code>str</code></p>


<h3><code>__author__</code></h3>

<p><strong>Description</strong>: Author of the project, obtained from the <code>settings</code> dictionary or defaults to an empty string if not found.</p>
<p><strong>Type</strong>: <code>str</code></p>

<h3><code>__copyright__</code></h3>

<p><strong>Description</strong>: Copyright information, obtained from the <code>settings</code> dictionary or defaults to an empty string if not found.</p>
<p><strong>Type</strong>: <code>str</code></p>

<h3><code>__cofee__</code></h3>

<p><strong>Description</strong>: A link to provide support for the developers.</p>
<p><strong>Type</strong>: <code>str</code></p>