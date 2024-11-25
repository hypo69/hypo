html
<h1>header.py</h1>

<h2>Overview</h2>
<p>This module defines the root path of the project. All imports are based on this path.</p>

<h2>Functions</h2>

<h3><code>set_project_root</code></h3>

<p><strong>Description</strong>: Finds the root directory of the project, starting from the current file's directory, searching upwards. Stops at the first directory containing any of the specified marker files.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>marker_files</code> (tuple): Filenames or directory names to identify the project root. Defaults to <code>('pyproject.toml', 'requirements.txt', '.git')</code>.</li>
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
</ul>

<p><strong>Example Usage</strong> (not directly in the function, but demonstrated by the code):</p>

<pre><code class="language-python">
__root__ = set_project_root()
</code></pre>

<h2>Variables</h2>

<h3><code>__root__</code></h3>
<p><strong>Description</strong>: The root directory of the project, obtained by calling <code>set_project_root()</code>.</p>
<p><strong>Type</strong>: <code>Path</code></p>


<h3><code>settings</code></h3>
<p><strong>Description</strong>: Settings loaded from <code>settings.json</code>.</p>
<p><strong>Type</strong>: <code>dict</code></p>
<p><strong>Default</strong>: <code>None</code></p>


<h3><code>doc_str</code></h3>
<p><strong>Description</strong>: Contents read from <code>README.MD</code>.</p>
<p><strong>Type</strong>: <code>str</code></p>
<p><strong>Default</strong>: <code>None</code></p>


<h3><code>__project_name__</code></h3>
<p><strong>Description</strong>: Project name, obtained from <code>settings.json</code>, or defaults to 'hypotez'.</p>
<p><strong>Type</strong>: <code>str</code></p>
<p><strong>Default</strong>: 'hypotez'</p>

<h3><code>__version__</code></h3>
<p><strong>Description</strong>: Project version, obtained from <code>settings.json</code>, or defaults to ''.</p>
<p><strong>Type</strong>: <code>str</code></p>
<p><strong>Default</strong>: ''</p>

<h3><code>__doc__</code></h3>
<p><strong>Description</strong>: Project documentation, obtained from <code>README.MD</code>, or defaults to ''.</p>
<p><strong>Type</strong>: <code>str</code></p>
<p><strong>Default</strong>: ''</p>

<h3><code>__details__</code></h3>
<p><strong>Description</strong>: Project details, defaults to ''.</p>
<p><strong>Type</strong>: <code>str</code></p>
<p><strong>Default</strong>: ''</p>

<h3><code>__author__</code></h3>
<p><strong>Description</strong>: Project author, obtained from <code>settings.json</code>, or defaults to ''.</p>
<p><strong>Type</strong>: <code>str</code></p>
<p><strong>Default</strong>: ''</p>

<h3><code>__copyright__</code></h3>
<p><strong>Description</strong>: Project copyright, obtained from <code>settings.json</code>, or defaults to ''.</p>
<p><strong>Type</strong>: <code>str</code></p>
<p><strong>Default</strong>: ''</p>

<h3><code>__cofee__</code></h3>
<p><strong>Description</strong>: Link to support the developer (coffee), obtained from <code>settings.json</code>, or defaults to a link.</p>
<p><strong>Type</strong>: <code>str</code></p>
<p><strong>Default</strong>: "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"</p>


<p><strong>Exceptions</strong>:</p>
<ul>
<li><code>FileNotFoundError</code>: Raised if <code>settings.json</code> or <code>README.MD</code> are not found.</li>
<li><code>json.JSONDecodeError</code>: Raised if there's an error decoding the JSON file.</li>
</ul>