html
<h1>Module: hypotez/src/templates/version.py</h1>

<h2>Overview</h2>
<p>This module defines constants related to the project's mode, version, and other metadata. It attempts to load settings from a <code>settings.json</code> file in the parent directory.</p>

<h2>Variables</h2>

<h3><code>MODE</code></h3>

<p><strong>Description</strong>: A string representing the project mode. Currently set to 'dev'.</p>


<h3><code>__project_name__</code></h3>

<p><strong>Description</strong>: The name of the project. Defaults to 'hypotez', loading from settings.json if available.</p>


<h3><code>__version__</code></h3>

<p><strong>Description</strong>: The version string of the project. Defaults to an empty string, loading from settings.json if available.</p>


<h3><code>__doc__</code></h3>

<p><strong>Description</strong>: A docstring for the module. Currently an empty string.</p>


<h3><code>__details__</code></h3>

<p><strong>Description</strong>: A string providing more details about the module. Currently an empty string.</p>


<h3><code>__author__</code></h3>

<p><strong>Description</strong>: The author of the project. Defaults to an empty string, loading from settings.json if available.</p>


<h3><code>__copyright__</code></h3>

<p><strong>Description</strong>: The copyright information for the project. Defaults to an empty string, loading from settings.json if available.</p>


<h3><code>__cofee__</code></h3>

<p><strong>Description</strong>: A string containing a link for supporting the developers. Defaults to a standard message, loading from settings.json if available.</p>


<h3><code>settings</code></h3>

<p><strong>Description</strong>: A dictionary containing project settings loaded from <code>settings.json</code>.</p>

<p><strong>Details</strong>: Attempts to load settings from <code>../settings.json</code>. If the file is not found or the JSON is invalid, <code>settings</code> will be <code>None</code>. This is then used to populate various project-related variables.</p>


<h2>Exceptions</h2>

<p><strong>Description</strong>: The module handles potential exceptions during JSON loading. The exact exceptions that can be raised will depend on the structure of <code>settings.json</code>.</p>

<ul>
  <li><code>FileNotFoundError</code>: The file <code>../settings.json</code> could not be found.</li>
  <li><code>json.JSONDecodeError</code>: The file <code>../settings.json</code> is not valid JSON.</li>
</ul>


<h2>Functions</h2>

<p>No functions are defined in this module.</p>