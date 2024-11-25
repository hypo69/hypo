html
<h1>hypotez/src/gui/context_menu/qt6/header.py</h1>

<h2>Overview</h2>
<p>This module, located in the <code>hypotez/src/gui/context_menu/qt6</code> directory, appears to be a Python module likely related to context menus within a graphical user interface (GUI) built using Qt6. It defines a constant <code>MODE</code> with a value of 'dev', suggesting a development mode.</p>

<h2>Constants</h2>

<h3><code>MODE</code></h3>

<p><strong>Description</strong>: A constant representing the current mode of the application. The value is set to 'dev'.</p>


<h2>Imports</h2>
<p>The module imports the following:</p>
<ul>
<li><code>sys</code></li>
<li><code>os</code></li>
<li><code>pathlib.Path</code></li>
</ul>

<h2>Variables</h2>

<h3><code>__root__</code></h3>

<p><strong>Description</strong>: A variable defined using the <code>pathlib.Path</code> object. It's set to the absolute path of the <code>hypotez</code> directory, calculated by removing parts of the current working directory.</p>

<p><strong>Details</strong>: The path of <code>__root__</code> is extracted from <code>os.getcwd()</code> by finding the position of <code>hypotez</code> and setting the path.</p>


<h2>Usage Notes</h2>
<p>The module appends the calculated <code>__root__</code> path to the Python path <code>sys.path</code>, likely for importing modules from the project's source tree.</p>