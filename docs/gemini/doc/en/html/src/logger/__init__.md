html
<h1>Module: hypotez/src/logger/__init__.py</h1>

<h2>Overview</h2>
<p>This module initializes the logger and imports necessary classes and exceptions from submodules. It defines a constant <code>MODE</code> with a value of 'dev'.</p>

<h2>Constants</h2>

<h3><code>MODE</code></h3>

<p><strong>Description</strong>:  A constant representing the current logging mode. Currently set to 'dev'.</p>
<p><strong>Value</strong>: 'dev'</p>


<h2>Classes</h2>

<p>No classes are defined in this module.</p>

<h2>Functions</h2>

<p>No functions are defined in this module.</p>

<h2>Imports</h2>

<p>This module imports the following:</p>
<ul>
<li><code>logger</code> from <code>.logger</code></li>
<li><code>ExecuteLocatorException</code>, <code>DefaultSettingsException</code>, <code>CredentialsError</code>, <code>PrestaShopException</code>, and <code>PayloadChecksumError</code> from <code>.exceptions</code></li>
</ul>

<h2>Exceptions</h2>

<p>The module imports the following exceptions:</p>

<ul>
<li><code>ExecuteLocatorException</code>:  Exception related to locating execution data.</li>
<li><code>DefaultSettingsException</code>: Exception indicating a problem with default settings.</li>
<li><code>CredentialsError</code>: Exception related to credential issues.</li>
<li><code>PrestaShopException</code>: Exception related to PrestaShop-specific operations.</li>
<li><code>PayloadChecksumError</code>: Exception related to payload checksum issues.</li>
</ul>