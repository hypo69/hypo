html
<h1>Module: hypotez/src/endpoints/advertisement/facebook/scenarios/switch_account.py</h1>

<h2>Overview</h2>
<p>This module defines a function for switching between Facebook accounts.</p>

<h2>Constants</h2>

<h3><code>MODE</code></h3>
<p><strong>Description</strong>: A constant representing the current mode, likely 'dev'.</p>


<h2>Functions</h2>

<h3><code>switch_account</code></h3>

<p><strong>Description</strong>: Handles switching between Facebook accounts, specifically checking for a "Switch" button and interacting with it.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>driver</code> (<code>Driver</code>): An instance of the webdriver class, likely containing methods for interacting with the browser.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li>None</li>
</ul>


<h2>Classes</h2>

(No classes are defined in this file)

<h2>Global Variables</h2>


<h3><code>locator</code></h3>
<p><strong>Description</strong>: A `SimpleNamespace` object loaded from the JSON file located at `gs.path.src / 'endpoints' / 'advertisement' / 'facebook' / 'locators' / 'post_message.json'`. This likely contains locators for elements on the Facebook page. </p>

<p><strong>Type</strong>: `SimpleNamespace`</p>



<!--
Possible improvements (depending on context):

- Add links to related modules or classes (if any exist).
- Expand the description of the `gs.path` variable and its usage context.
- Provide examples of how to use the `switch_account` function.
- Include the content of the 'post_message.json' file for context (if possible).
- Explain the functionality of the `execute_locator` method.
 -->