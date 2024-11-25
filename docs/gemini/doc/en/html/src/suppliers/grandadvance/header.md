html
<h1>Module: hypotez/src/suppliers/grandadvance/header.py</h1>

<h2>Overview</h2>
<p>This module defines a function to find the root directory of a project. It loads project settings from a JSON file and optionally reads a README file. It also defines various project metadata variables.</p>

<h2>Functions</h2>

<h3><code>set_project_root</code></h3>

<p><strong>Description</strong>: Finds the root directory of the project starting from the current file's directory, searching upwards.</p>

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
  <li>None</li>
</ul>


<h3><code><var>__details__</var></code></h3>
<p><strong>Description</strong>: Currently empty string</p>
<p><strong>Returns</strong>:</p>
<ul>
<li><code>string</code>: Empty string</li>
</ul>
<p><strong>Raises</strong>:</p>
<ul>
<li>None</li>
</ul>


<h3><code><var>__doc__</var></code></h3>
<p><strong>Description</strong>: The content of the README.md file, or an empty string if it does not exist.</p>
<p><strong>Returns</strong>:</p>
<ul>
<li><code>string</code>: The content of the README.md file, or an empty string if it does not exist.</li>
</ul>
<p><strong>Raises</strong>:</p>
<ul>
  <li><code>FileNotFoundError</code>: If the README.MD file does not exist.</li>
  <li><code>json.JSONDecodeError</code>: If there is an error decoding the JSON data in the file.</li>
</ul>




<h3><code><var>__project_name__</var></code></h3>
<p><strong>Description</strong>: The project name, obtained from the settings.json file or defaults to 'hypotez'.</p>
<p><strong>Returns</strong>:</p>
<ul>
<li><code>string</code>: The project name, obtained from the settings.json file or defaults to 'hypotez'.</li>
</ul>
<p><strong>Raises</strong>:</p>
<ul>
  <li><code>FileNotFoundError</code>: If the settings.json file does not exist.</li>
  <li><code>json.JSONDecodeError</code>: If there is an error decoding the JSON data in the file.</li>
</ul>


<h3><code><var>__version__</var></code></h3>
<p><strong>Description</strong>: The project version, obtained from the settings.json file or defaults to an empty string.</p>
<p><strong>Returns</strong>:</p>
<ul>
<li><code>string</code>: The project version, obtained from the settings.json file or defaults to an empty string.</li>
</ul>
<p><strong>Raises</strong>:</p>
<ul>
  <li><code>FileNotFoundError</code>: If the settings.json file does not exist.</li>
  <li><code>json.JSONDecodeError</code>: If there is an error decoding the JSON data in the file.</li>
</ul>


<h3><code><var>__author__</var></code></h3>
<p><strong>Description</strong>: The author of the project, obtained from the settings.json file or defaults to an empty string.</p>
<p><strong>Returns</strong>:</p>
<ul>
<li><code>string</code>: The author of the project, obtained from the settings.json file or defaults to an empty string.</li>
</ul>
<p><strong>Raises</strong>:</p>
<ul>
  <li><code>FileNotFoundError</code>: If the settings.json file does not exist.</li>
  <li><code>json.JSONDecodeError</code>: If there is an error decoding the JSON data in the file.</li>
</ul>


<h3><code><var>__copyright__</var></code></h3>
<p><strong>Description</strong>: The copyright holder, obtained from the settings.json file or defaults to an empty string.</p>
<p><strong>Returns</strong>:</p>
<ul>
<li><code>string</code>: The copyright holder, obtained from the settings.json file or defaults to an empty string.</li>
</ul>
<p><strong>Raises</strong>:</p>
<ul>
  <li><code>FileNotFoundError</code>: If the settings.json file does not exist.</li>
  <li><code>json.JSONDecodeError</code>: If there is an error decoding the JSON data in the file.</li>
</ul>


<h3><code><var>__cofee__</var></code></h3>
<p><strong>Description</strong>: A link to support the developer via coffee. Obtained from settings.json or defaults to a link.</p>
<p><strong>Returns</strong>:</p>
<ul>
<li><code>string</code>: The link to support the developer, obtained from the settings.json file or defaults to a link.</li>
</ul>
<p><strong>Raises</strong>:</p>
<ul>
  <li><code>FileNotFoundError</code>: If the settings.json file does not exist.</li>
  <li><code>json.JSONDecodeError</code>: If there is an error decoding the JSON data in the file.</li>
</ul>