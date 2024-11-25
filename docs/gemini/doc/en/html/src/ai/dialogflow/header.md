html
<h1>hypotez/src/ai/dialogflow/header.py</h1>

<h2>Overview</h2>
<p>This module defines the root path to the project. All imports are built relative to this path.
Future development should consider moving the root path definition to a system variable.</p>

<h2>Functions</h2>

<h3><code>set_project_root</code></h3>

<p><strong>Description</strong>: Finds the root directory of the project starting from the current file's directory. It searches upwards in the directory hierarchy until it finds a directory containing one of the specified marker files (pyproject.toml, requirements.txt, .git). If no such directory is found, it returns the directory containing the script itself.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>marker_files</code> (tuple): Filenames or directory names to identify the project root. Defaults to ('pyproject.toml', 'requirements.txt', '.git').</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Path</code>: Path to the root directory if found, otherwise the directory where the script is located.</li>
</ul>


<h3><code>set_project_root</code></h3>

<p><strong>Description</strong>: Finds the root directory of the project starting from the current file's directory. It searches upwards in the directory hierarchy until it finds a directory containing one of the specified marker files (pyproject.toml, requirements.txt, .git). If no such directory is found, it returns the directory containing the script itself.
This function ensures that the project root is added to Python's path if it's not already present.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>marker_files</code> (tuple, optional): Filenames or directory names to identify the project root. Defaults to ('pyproject.toml', 'requirements.txt', '.git').</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Path</code>: Path to the root directory if found, otherwise the directory where the script is located.</li>
</ul>


<h2>Variables</h2>

<h3><code>__root__</code></h3>

<p><strong>Description</strong>: Path to the root directory of the project. Initialized using the <code>set_project_root</code> function.</p>
<p><strong>Type</strong>: <code>Path</code></p>


<h3><code>settings</code></h3>

<p><strong>Description</strong>: Dictionary containing project settings loaded from <code>settings.json</code>.</p>
<p><strong>Type</strong>: <code>dict</code> or <code>None</code></p>

<h3><code>doc_str</code></h3>

<p><strong>Description</strong>: String containing the content of <code>README.MD</code> file.</p>
<p><strong>Type</strong>: <code>str</code> or <code>None</code></p>

<h3><code>__project_name__</code></h3>

<p><strong>Description</strong>: Project name, taken from <code>settings.json</code> or defaulting to 'hypotez'.</p>
<p><strong>Type</strong>: <code>str</code></p>

<h3><code>__version__</code></h3>

<p><strong>Description</strong>: Project version, taken from <code>settings.json</code> or defaulting to empty string.</p>
<p><strong>Type</strong>: <code>str</code></p>

<h3><code>__doc__</code></h3>

<p><strong>Description</strong>: Project documentation string, taken from <code>README.MD</code> or defaulting to empty string.</p>
<p><strong>Type</strong>: <code>str</code></p>

<h3><code>__details__</code></h3>

<p><strong>Description</strong>: Project details string (currently empty).</p>
<p><strong>Type</strong>: <code>str</code></p>

<h3><code>__author__</code></h3>

<p><strong>Description</strong>: Project author, taken from <code>settings.json</code> or defaulting to empty string.</p>
<p><strong>Type</strong>: <code>str</code></p>

<h3><code>__copyright__</code></h3>

<p><strong>Description</strong>: Project copyright, taken from <code>settings.json</code> or defaulting to empty string.</p>
<p><strong>Type</strong>: <code>str</code></p>

<h3><code>__cofee__</code></h3>

<p><strong>Description</strong>: A string containing a link to a donation platform for a cup of coffee.</p>
<p><strong>Type</strong>: <code>str</code></p>