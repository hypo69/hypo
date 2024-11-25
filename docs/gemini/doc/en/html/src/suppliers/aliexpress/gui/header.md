html
<h1>Module: hypotez/src/suppliers/aliexpress/gui/header.py</h1>

<h2>Overview</h2>
<p>This module defines the development mode for the aliexpress supplier GUI and sets up the project path.</p>

<h2>Constants</h2>

<h3><code>MODE</code></h3>

<p><strong>Description</strong>:  A string constant that defines the application mode (e.g., 'dev', 'prod').</p>

<p><strong>Value</strong>: 'dev'</p>


<h2>Functions</h2>

<!-- No functions defined in the provided code -->

<h2>Variables</h2>

<h3><code>__root__</code></h3>

<p><strong>Description</strong>:  A Path object representing the root directory of the project.</p>
<p><strong>Initialization</strong>: It retrieves the current working directory, finds the 'hypotez' folder, and creates a Path object pointing to it.</p>
<p><strong>Purpose</strong>:  This variable is used to add the project root directory to the Python module search path (sys.path), allowing modules from anywhere in the project to be imported without specifying a full path.</p>


<h2>Modules Imported</h2>

<ul>
  <li><code>sys</code>:  Provides access to system-specific parameters and functions.</li>
  <li><code>os</code>:  Provides a way of using operating system dependent functionality.</li>
  <li><code>pathlib</code>:  Provides object-oriented implementations of filesystem paths.</li>
</ul>