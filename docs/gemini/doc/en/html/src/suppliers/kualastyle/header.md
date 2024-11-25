html
<h1>Module: hypotez/src/suppliers/kualastyle/header.py</h1>

<h2>Overview</h2>
<p>This module defines functions for setting the project root directory and loading settings from a JSON file. It also handles potential errors during file operations.</p>

<h2>Functions</h2>

<h3><code>set_project_root</code></h3>

<p><strong>Description</strong>: Finds the root directory of the project by searching upwards from the current file's directory.</p>

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

<p><strong>Description</strong>: This function determines the root directory of the project.  It starts from the directory of the current Python file and recursively checks parent directories for specific marker files (like 'pyproject.toml', 'requirements.txt', or '.git'). It returns the path to the first directory found containing any of the marker files. If none of the marker files are found, it returns the directory containing the current file.  Importantly, if the root directory is not already in sys.path, it prepends this path to sys.path.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>marker_files</code> (tuple, optional): A tuple of filenames or directory names that will be searched for to determine the project root. Defaults to ('pyproject.toml', 'requirements.txt', '.git').</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Path</code>: The path to the project root directory.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
</ul>



<hr>

<!-- Hidden, auto-generated TOC -->
<details>
<summary>Table of Contents</summary>
<ol>
<li><a href="#Module-hypotez/src/suppliers/kualastyle/header.py">Module: hypotez/src/suppliers/kualastyle/header.py</a></li>
<li><a href="#Overview">Overview</a></li>
<li><a href="#Functions">Functions</a></li>
<li><a href="#set_project_root"><code>set_project_root</code></a></li>

</ol>
</details>