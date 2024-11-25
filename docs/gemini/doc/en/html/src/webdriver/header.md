html
<h1>hypotez/src/webdriver/header.py</h1>

<h2>Overview</h2>
<p>This module contains functions for setting the project root directory, loading project settings, and accessing project documentation.</p>

<h2>Functions</h2>

<h3><code>set_project_root</code></h3>

<p><strong>Description</strong>: Finds the root directory of the project starting from the current file's directory.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>marker_files</code> (tuple): Filenames or directory names to identify the project root. Defaults to ('pyproject.toml', 'requirements.txt', '.git').</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Path</code>: Path to the root directory if found, otherwise the directory where the script is located.</li>
</ul>


<h3><code>set_project_root</code></h3>

<p><strong>Description</strong>: Finds the root directory of the project, handling cases where marker files are not found and inserting the root directory into the Python path.</p>

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

<h3><code>settings</code></h3>

<p><strong>Description</strong>: Loads project settings from 'settings.json' in the project root directory.</p>

<p><strong>Parameters</strong>:</p>
<ul>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>dict</code>: Project settings as a dictionary. Returns None if the file is not found or if there's an error during parsing.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>FileNotFoundError</code>: If the 'settings.json' file is not found.</li>
  <li><code>json.JSONDecodeError</code>: If the 'settings.json' file is not in valid JSON format.</li>
</ul>



<h3><code>doc_str</code></h3>

<p><strong>Description</strong>: Loads project documentation from 'README.MD' in the project root directory.</p>

<p><strong>Parameters</strong>:</p>
<ul>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>str</code>: Project documentation as a string. Returns None if the file is not found or if there's an error during reading.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>FileNotFoundError</code>: If the 'README.MD' file is not found.</li>
  <li><code>json.JSONDecodeError</code> (not applicable): If the 'README.MD' is not in valid JSON format - no need to handle, it's a text file.</li>
</ul>