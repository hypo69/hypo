html
<h1>Module header</h1>

<h2>Overview</h2>
<p>This module contains configuration settings, likely for a development environment, and imports necessary libraries.</p>

<h2>Constants</h2>

<h3><code>MODE</code></h3>

<p><strong>Description</strong>: A string variable defining the operating mode.  In this case, 'dev'.</p>

<p><strong>Value</strong>: 'dev'</p>


<h2>Imports</h2>

<ul>
<li><code>pathlib</code>: Used for path manipulation.</li>
<li><code>sys</code>: Provides access to system-specific parameters and functions.</li>
<li><code>src.credentials</code>: Imports the `gs` object, likely for Google Services authentication or similar credentials.</li>
</ul>


<h2>Functions</h2>

<h3><code><pre><code>__init__</code></pre></h3>

<p><strong>Description</strong>: Initializes the module.</p>



<h2>Variables</h2>

<h3><code>src_path</code></h3>

<p><strong>Description</strong>:  Determines the path to the project's source directory. It resolves the parent directory of the current file. </p>

<p><strong>Type</strong>: string</p>


<h3><code><pre><code>sys.path</code></pre></h3>

<p><strong>Description</strong>: The module dynamically adds the source path to Python's module search path if it is not already present, ensuring the correct file paths.</p>



<p><strong>Type</strong>: list</p>