html
<h1>Module: hypotez/src/endpoints/advertisement/facebook/facebook_groups_widgets.py</h1>

<h2>Overview</h2>
<p>This module provides a Facebook Groups widget for selecting groups to place advertisements. It utilizes a dropdown menu populated from a JSON file containing Facebook group URLs.</p>

<h2>Constants</h2>

<h3><code>MODE</code></h3>

<p><strong>Description</strong>:  A constant representing the mode of operation. In this case, it's set to 'dev'.</p>


<h2>Classes</h2>

<h3><code>FacebookGroupsWidget</code></h3>

<p><strong>Description</strong>: Creates a dropdown list widget for selecting Facebook groups from a provided JSON file.</p>

<p><strong>Methods</strong>:</p>

<h4><code>__init__</code></h4>

<p><strong>Description</strong>: Initializes the FacebookGroupsWidget with the path to the JSON file containing group data. It parses the JSON data and creates the dropdown widget.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>json_file_path</code> (Path): Path to the JSON file containing information about Facebook groups.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>: Raised if there's an error loading or parsing the JSON file.</li>
</ul>


<h4><code>create_dropdown</code></h4>

<p><strong>Description</strong>: Creates and returns the dropdown widget, populating it with the group URLs from the loaded JSON.</p>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Dropdown</code>: The generated dropdown widget.</li>
</ul>


<h4><code>display_widget</code></h4>

<p><strong>Description</strong>: Displays the created dropdown widget.</p>


<h2>Functions</h2>

<!-- (No functions in this module) -->