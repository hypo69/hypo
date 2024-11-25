html
<h1>Module: hypotez.src.suppliers.amazon.header</h1>

<h2>Overview</h2>
<p>This module provides functionality for locating the project root directory and loading settings from a JSON file. It also handles potential errors during file loading.</p>

<h2>Functions</h2>

<h3><code>set_project_root</code></h3>

<p><strong>Description</strong>: Finds the root directory of the project. It starts from the current file's directory and searches upwards until a directory containing any of the specified marker files is found. If no such directory is found, it returns the directory where the script is located.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>marker_files</code> (tuple): Filenames or directory names to identify the project root. Defaults to ('pyproject.toml', 'requirements.txt', '.git').</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Path</code>: Path to the root directory if found, otherwise the directory where the script is located.</li>
</ul>


<h3><code>set_project_root</code></h3>

<p><strong>Description</strong>: This function searches up the file system from the current file's location to find the project root directory. It looks for files like 'pyproject.toml', 'requirements.txt', or '.git' to determine the root.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>marker_files</code> (tuple, optional): A tuple of files or directories to look for in the parent directories. Defaults to ('pyproject.toml', 'requirements.txt', '.git').</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Path</code>: The path to the project root directory.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
<li>No exceptions are explicitly raised. The function might implicitly return a `Path` object for successful searches, or possibly the current directory if no project root is found.</li>
</ul>

<p><strong>Example Usage</strong>:</p>
<pre><code class="language-python">
project_root = set_project_root()
print(project_root)
</code></pre>