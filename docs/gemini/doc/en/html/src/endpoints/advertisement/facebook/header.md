html
<h1>hypotez/src/endpoints/advertisement/facebook/header.py</h1>

<h2>Overview</h2>
<p>This module defines a function to set the project root directory and loads project settings from a JSON file.</p>

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

<p><strong>Raises</strong>:</p>
<ul>
  <li>No exceptions explicitly documented.</li>
</ul>


<h3><code><a id='settings_loading'> </a>loading settings </code></h3>
<p><strong>Description</strong>: Loads the project settings from a JSON file.</p>
<ul>
    <li>The function attempts to open the 'settings.json' file located within the project root.
    <li> If the file is found, it's parsed as JSON, and the loaded content is stored in the 'settings' variable.
    <li> If any errors occur during file reading or JSON parsing, the errors are silently handled (no specific exception handling provided). 
    <li>The 'settings' global variable will hold the parsed settings dictionary if successful or None otherwise. 
</ul>


<p><strong>Raises</strong>:</p>
<ul>
    <li><code>FileNotFoundError</code>: If the 'settings.json' file is not found.</li>
    <li><code>json.JSONDecodeError</code>: If the 'settings.json' file content is not valid JSON.</li>
</ul>

<h3><code><a id='documentation_loading'> </a> loading documentation</code></h3>

<p><strong>Description</strong>: Loads the project documentation from a README.MD file.</p>
<ul>
    <li>The function attempts to open the 'README.MD' file located within the project root.
    <li>If the file is found, its content is read and stored in the 'doc_str' variable.
    <li>If any errors occur during file reading, the errors are silently handled (no specific exception handling provided).
    <li>'doc_str' variable holds the README contents if loaded successfully or an empty string otherwise.
</ul>



<p><strong>Raises</strong>:</p>
<ul>
    <li><code>FileNotFoundError</code>: If the 'README.MD' file is not found.</li>
    <li><code>json.JSONDecodeError</code>: If the 'README.MD' file content is not valid JSON.</li>
</ul>



<h2>Variables</h2>
<ul>

 <li><code>MODE</code> (str): Stores the mode ('dev' in this example).</li>
 <li><code>settings</code> (dict): Stores loaded project settings from settings.json.</li>
 <li><code>doc_str</code> (str): Stores loaded project documentation from README.MD</li>
 <li><code>__project_name__</code> (str): Stores the project name from settings or defaults to 'hypotez'.</li>
 <li><code>__version__</code> (str): Stores the project version from settings or defaults to an empty string.</li>
 <li><code>__doc__</code> (str): Stores the project documentation from README.MD or defaults to an empty string.</li>
 <li><code>__details__</code> (str): Stores the project details. (empty string by default)</li>
 <li><code>__author__</code> (str): Stores the author information from settings or defaults to an empty string.</li>
 <li><code>__copyright__</code> (str): Stores the copyright information from settings or defaults to an empty string.</li>
 <li><code>__cofee__</code> (str): Stores the coffee link for developer support from settings or defaults to a link.</li>


 <li><code>__root__</code> (Path): Stores the project root directory obtained from <code>set_project_root</code>.</li>



</ul>

<h2>Module Attributes</h2>
<p>No module-level attributes are explicitly defined.</p>