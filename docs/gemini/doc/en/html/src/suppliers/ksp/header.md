html
<h1>Module: hypotez.src.suppliers.ksp.header</h1>

<h2>Overview</h2>
<p>This module provides functionality for finding the project root directory and loading settings from a JSON file. It also incorporates versioning and documentation handling.</p>

<h2>Functions</h2>

<h3><code>set_project_root</code></h3>

<p><strong>Description</strong>: Finds the root directory of the project by traversing up the directory tree from the current file location until it encounters a directory containing specific marker files (e.g., pyproject.toml, requirements.txt, .git). If not found, it uses the directory where the script is located. It also adds the root directory to Python's sys.path.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>marker_files</code> (tuple): A tuple of filenames or directory names to identify the project root. Defaults to ('pyproject.toml', 'requirements.txt', '.git').</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Path</code>: Path to the root directory if found, otherwise the directory where the script is located.</li>
</ul>


<h3><code>set_project_root</code></h3>

<p><strong>Description</strong>: This function is responsible for locating the root directory of the project. It begins by resolving the current file's path and then iterates through its parent directories.  The search stops when a directory containing any of the specified marker files is found. If no suitable root directory is located, the script's current directory is returned.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>marker_files</code> (tuple, optional): A tuple of filenames or directory names to identify the project root. Defaults to ('pyproject.toml', 'requirements.txt', '.git').</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Path</code>: The path to the project root directory. If the root is not found, the directory of the current file is returned.</li>
</ul>


<p><strong>Example Usage (Illustrative):</strong></p>
<pre><code class="language-python">
root_path = set_project_root()
print(root_path)
</code></pre>


<p><strong>Raises</strong>:</p>
<ul>
</ul>