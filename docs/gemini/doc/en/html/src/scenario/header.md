html
<h1>hypotez/src/scenario/header.py</h1>

<h2>Overview</h2>
<p>This module defines functions for interacting with settings and locating the project root directory.</p>

<h2>Functions</h2>

<h3><code>set_project_root</code></h3>

<p><strong>Description</strong>: Finds the root directory of the project.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>marker_files</code> (tuple): Filenames or directory names to identify the project root.  Defaults to ('pyproject.toml', 'requirements.txt', '.git').</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Path</code>: Path to the root directory if found, otherwise the directory where the script is located.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li>No exceptions are explicitly raised.</li>
</ul>


<h3><code>set_project_root</code></h3>

<p><strong>Description</strong>: This function is designed to locate the root directory of the project.  It iterates upwards from the current file's directory, checking if any of the specified marker files exist within each parent directory. If found, it sets the root directory, adds it to the Python path if it's not already present, and returns the Path object representing the root directory.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>marker_files</code> (tuple, optional): A tuple of files or directories used to identify the project root. Defaults to ('pyproject.toml', 'requirements.txt', '.git').</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Path</code>: The Path object representing the root directory. Returns the current file's directory if no matching marker files are found.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
 <li>None</li>
</ul>

<h2>Global Variables</h2>


<h3><code>__root__</code></h3>

<p><strong>Description</strong>: Stores the path to the root directory of the project. Initialized by the <code>set_project_root</code> function.</p>


<p><strong>Type</strong>: <code>Path</code></p>
<p><strong>Initialization</strong>: Path to the root directory of the project, determined by the set_project_root function.</p>

<h3><code>settings</code></h3>

<p><strong>Description</strong>: A dictionary containing project settings loaded from <code>settings.json</code>.</p>

<p><strong>Type</strong>: <code>dict</code></p>
<p><strong>Initialization</strong>: Loaded from <code>gs.path.root / 'src' / 'settings.json'</code>. Defaults to <code>None</code> if the file is not found or cannot be parsed.</p>


<h3><code>doc_str</code></h3>

<p><strong>Description</strong>:  Stores the content of the project's README file (README.MD).</p>

<p><strong>Type</strong>: <code>str</code></p>
<p><strong>Initialization</strong>: Loaded from <code>gs.path.root / 'src' / 'README.MD'</code>. Defaults to <code>None</code> if the file is not found or cannot be opened.</p>



<h3><code>__project_name__</code></h3>

<p><strong>Description</strong>: The name of the project.  Defaults to 'hypotez' if <code>settings</code> is not available or 'project_name' is not found in <code>settings</code>.</p>

<p><strong>Type</strong>: <code>str</code></p>


<h3><code>__version__</code></h3>

<p><strong>Description</strong>: The version of the project. Defaults to an empty string if <code>settings</code> is not available or 'version' is not found in <code>settings</code>.</p>

<p><strong>Type</strong>: <code>str</code></p>



<h3><code>__doc__</code></h3>

<p><strong>Description</strong>:  The project's documentation, if available.</p>

<p><strong>Type</strong>: <code>str</code></p>


<h3><code>__details__</code></h3>

<p><strong>Description</strong>: Placeholder for project details.  Initialized to an empty string.</p>

<p><strong>Type</strong>: <code>str</code></p>


<h3><code>__author__</code></h3>

<p><strong>Description</strong>: Author of the project. Defaults to an empty string if not found in <code>settings</code>.</p>

<p><strong>Type</strong>: <code>str</code></p>



<h3><code>__copyright__</code></h3>

<p><strong>Description</strong>: Copyright information. Defaults to an empty string if not found in <code>settings</code>.</p>

<p><strong>Type</strong>: <code>str</code></p>



<h3><code>__cofee__</code></h3>

<p><strong>Description</strong>: A link to support the developer via coffee. Defaults to a link to a specific Boosty page if not found in <code>settings</code>.</p>

<p><strong>Type</strong>: <code>str</code></p>