html
<h1>hypotez/src/logger/header.py</h1>

<h2>Overview</h2>
<p>This module defines the root path of the project. All imports are built relative to this path.
    In the future, this will be moved to a system variable.</p>

<h2>Constants</h2>

<h3><code>MODE</code></h3>

<p><strong>Description</strong>: Defines the current project mode (e.g., 'dev').</p>
<pre><code>python
MODE = 'dev'
</code></pre>


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


<pre><code class="language-python">
def set_project_root(marker_files=(\'pyproject.toml\', \'requirements.txt\', \'.git\')) -> Path:
    """
    Finds the root directory of the project starting from the current file's directory,
    searching upwards and stopping at the first directory containing any of the marker files.

    Args:
        marker_files (tuple): Filenames or directory names to identify the project root.
    
    Returns:
        Path: Path to the root directory if found, otherwise the directory where the script is located.
    """
    __root__:Path
    current_path:Path = Path(__file__).resolve().parent
    __root__ = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__
</code></pre>


<h2>Variables</h2>

<h3><code>__root__</code></h3>

<p><strong>Description</strong>: Path to the root directory of the project. Calculated using the <code>set_project_root()</code> function.</p>


<h3><code>settings</code></h3>

<p><strong>Description</strong>: Project settings loaded from <code>settings.json</code>.</p>

<p><strong>Type</strong>: <code>dict</code></p>

<h3><code>doc_str</code></h3>

<p><strong>Description</strong>: Project documentation loaded from <code>README.MD</code>.</p>

<p><strong>Type</strong>: <code>str</code></p>

<h3><code>__project_name__</code></h3>

<p><strong>Description</strong>: Name of the project. Derived from the <code>settings</code> variable.</p>

<h3><code>__version__</code></h3>

<p><strong>Description</strong>: Version of the project. Derived from the <code>settings</code> variable.</p>

<h3><code>__doc__</code></h3>

<p><strong>Description</strong>: Project documentation. Derived from the <code>doc_str</code> variable.</p>

<h3><code>__details__</code></h3>

<p><strong>Description</strong>: Project details.</p>

<h3><code>__author__</code></h3>

<p><strong>Description</strong>: Author of the project. Derived from the <code>settings</code> variable.</p>

<h3><code>__copyright__</code></h3>

<p><strong>Description</strong>: Copyright information. Derived from the <code>settings</code> variable.</p>

<h3><code>__cofee__</code></h3>

<p><strong>Description</strong>: Link to support the developer.</p>