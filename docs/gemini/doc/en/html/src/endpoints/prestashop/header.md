html
<h1>hypotez/src/logger/header.py</h1>

<h2>Overview</h2>
<p>This module defines the root path to the project. All imports are built relative to this path.  Future versions will likely move this to a system variable.</p>

<h2>Variables</h2>

<h3><code>MODE</code></h3>

<p><strong>Description</strong>: A string variable defining the current mode (e.g., 'dev').</p>


<h3><code>__root__</code></h3>

<p><strong>Description</strong>: Path to the root directory of the project. Calculated using the <code>set_project_root</code> function.</p>


<h3><code>settings</code></h3>

<p><strong>Description</strong>: A dictionary containing project settings loaded from <code>src/settings.json</code>.  Defaults to <code>None</code> if the file isn't found or is invalid JSON.</p>


<h3><code>doc_str</code></h3>

<p><strong>Description</strong>: A string containing the contents of <code>src/README.MD</code>. Defaults to <code>None</code> if the file is not found or is empty.</p>


<h3><code>__project_name__</code></h3>

<p><strong>Description</strong>: The project name.  Obtained from the <code>settings</code> dictionary or defaults to 'hypotez'.</p>


<h3><code>__version__</code></h3>

<p><strong>Description</strong>: The project version. Obtained from the <code>settings</code> dictionary, defaulting to ''.</p>


<h3><code>__doc__</code></h3>

<p><strong>Description</strong>: The project documentation string.  Obtained from <code>doc_str</code>, defaulting to ''.</p>


<h3><code>__details__</code></h3>

<p><strong>Description</strong>: Placeholder for additional project details (currently empty).</p>


<h3><code>__author__</code></h3>

<p><strong>Description</strong>: The author of the project.  Obtained from the <code>settings</code> dictionary, defaulting to ''.</p>


<h3><code>__copyright__</code></h3>

<p><strong>Description</strong>: Copyright information.  Obtained from the <code>settings</code> dictionary, defaulting to ''.</p>


<h3><code>__cofee__</code></h3>

<p><strong>Description</strong>: A string containing a link to a tip jar for developers (default link provided if <code>settings</code> is invalid).</p>


<h2>Functions</h2>

<h3><code>set_project_root</code></h3>

<p><strong>Description</strong>: Finds the root directory of the project.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>marker_files</code> (tuple): Filenames or directory names used to identify the project root.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Path</code>: Path to the root directory if found, otherwise the directory containing the script.</li>
</ul>


<h2>Modules Used</h2>
<ul><li><code>sys</code></li><li><code>json</code></li><li><code>packaging.version</code></li><li><code>pathlib</code></li><li><code>src.gs</code></li></ul>