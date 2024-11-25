html
<h1>hypotez/src/suppliers/header.py</h1>

<h2>Overview</h2>
<p>This module defines functions for setting the project root directory and loading settings from a JSON file. It utilizes the <code>gs</code> module for path manipulation and handles potential errors during file reading.</p>

<h2>Functions</h2>

<h3><code>set_project_root</code></h3>

<p><strong>Description</strong>: Finds the root directory of the project by searching up from the current file's directory until a directory containing specified marker files (pyproject.toml, requirements.txt, .git) is found. If no such directory is found, the directory containing the current script is returned.</p>

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
</ul>


<h2>Variables</h2>
<h3><code>__root__</code></h3>
<p><strong>Description</strong>: Path to the root directory of the project.  Initialized by calling <code>set_project_root()</code>.</p>
<ul>
  <li><strong>Type:</strong> <code>Path</code></li>
</ul>



<h3><code>settings</code></h3>
<p><strong>Description</strong>: Loaded settings from settings.json. Initialized from a JSON file in the src directory.</p>

<ul>
  <li><strong>Type:</strong> <code>dict</code></li>
</ul>

<p><strong>Raises:</strong></p>
<ul>
  <li><code>FileNotFoundError</code>: If the settings.json file is not found.</li>
  <li><code>json.JSONDecodeError</code>: If the settings.json file is not valid JSON.</li>
</ul>

<h3><code>doc_str</code></h3>
<p><strong>Description</strong>: Content of the README.MD file. Initialized by reading a README.MD file in the src directory.</p>

<ul>
  <li><strong>Type:</strong> <code>str</code></li>
</ul>


<p><strong>Raises:</strong></p>
<ul>
  <li><code>FileNotFoundError</code>: If the README.MD file is not found.</li>
  <li><code>json.JSONDecodeError</code>: If the README.MD file content is not valid.</li>
</ul>




<h3><code>__project_name__</code></h3>
<p><strong>Description</strong>: Project name, retrieved from the settings (defaults to 'hypotez').</p>

<ul>
  <li><strong>Type:</strong> <code>str</code></li>
</ul>


<h3><code>__version__</code></h3>
<p><strong>Description</strong>: Project version, retrieved from the settings (defaults to '').</p>

<ul>
  <li><strong>Type:</strong> <code>str</code></li>
</ul>

<h3><code>__doc__</code></h3>
<p><strong>Description</strong>: Project documentation, retrieved from the README.MD file (defaults to '').</p>

<ul>
  <li><strong>Type:</strong> <code>str</code></li>
</ul>



<h3><code>__details__</code></h3>
<p><strong>Description</strong>: Project details (empty by default).</p>

<ul>
  <li><strong>Type:</strong> <code>str</code></li>
</ul>

<h3><code>__author__</code></h3>
<p><strong>Description</strong>: Project author, retrieved from the settings (defaults to '').</p>

<ul>
  <li><strong>Type:</strong> <code>str</code></li>
</ul>

<h3><code>__copyright__</code></h3>
<p><strong>Description</strong>: Project copyright, retrieved from the settings (defaults to '').</p>

<ul>
  <li><strong>Type:</strong> <code>str</code></li>
</ul>

<h3><code>__cofee__</code></h3>
<p><strong>Description</strong>: Support link for developer, retrieved from the settings (defaults to a specific link). </p>

<ul>
  <li><strong>Type:</strong> <code>str</code></li>
</ul>