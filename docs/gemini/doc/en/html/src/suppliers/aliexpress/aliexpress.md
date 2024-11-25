html
<h1>Module: aliexpress</h1>

<h2>Overview</h2>
<p>This module provides the <code>Aliexpress</code> class, integrating functionality from <code>Supplier</code>, <code>AliRequests</code>, and <code>AliApi</code> for working with AliExpress.</p>

<h2>Constants</h2>

<h3><code>MODE</code></h3>

<p><strong>Description</strong>: Defines the operating mode (currently 'dev').</p>


<h2>Classes</h2>

<h3><code>Aliexpress</code></h3>

<p><strong>Description</strong>: Base class for AliExpress. This class combines features of the <code>Supplier</code>, <code>AliRequests</code>, and <code>AliApi</code> classes to facilitate interaction with AliExpress.</p>

<p><strong>Usage Examples</strong>:</p>

<pre><code>python
# Run without a webdriver
a = Aliexpress()

# Webdriver `Chrome`
a = Aliexpress('chrome')

# Requests mode
a = Aliexpress(requests=True)
</code></pre>

<p><strong>Methods</strong>:</p>

<ul>
<li><code>__init__</code></li>
</ul>

<h4><code>__init__</code></h4>

<p><strong>Description</strong>: Initializes the <code>Aliexpress</code> class.</p>

<p><strong>Parameters</strong>:</p>
<ul>
<li><code>webdriver</code> (bool | str, optional): Webdriver mode.  Supported values are:
    <ul>
        <li><code>False</code> (default): No webdriver.</li>
        <li><code>'chrome'</code>: Use the Chrome webdriver.</li>
        <li><code>'mozilla'</code>: Use the Mozilla webdriver.</li>
        <li><code>'edge'</code>: Use the Edge webdriver.</li>
        <li><code>'default'</code>: Use the system's default webdriver.</li>
    </ul>
</li>
<li><code>locale</code> (str | dict, optional): The language and currency settings for the script. Defaults to <code>{'EN': 'USD'}</code>.</li>
<li><code>*args</code>: Additional positional arguments.</li>
<li><code>**kwargs</code>: Additional keyword arguments.</li>
</ul>


<p><strong>Examples</strong>:</p>

<pre><code>python
# Run without a webdriver
a = Aliexpress()

# Webdriver `Chrome`
a = Aliexpress('chrome')
</code></pre>

<p><strong>Raises</strong>:</p>
<ul>
<li>N/A</li> </ul>


<p><strong>Returns</strong>: N/A</p>

<p><strong>Inherited methods from Supplier, AliRequests, AliApi</strong>: 
    The <code>Aliexpress</code> class inherits methods from <code>Supplier</code>, <code>AliRequests</code>, and <code>AliApi</code>.
    Please refer to the documentation of those classes for details about these inherited methods.</p>



</ul>

<h2>Imported Modules</h2>

<p>This module imports the following modules:</p>

<ul>
    <li><code>header</code></li>
    <li><code>pickle</code></li>
    <li><code>requests</code></li>
    <li><code>threading</code></li>
    <li><code>fake_useragent</code></li>
    <li><code>pathlib</code></li>
    <li><code>typing</code></li>
    <li><code>requests.cookies</code></li>
    <li><code>urllib.parse</code></li>
    <li><code>gs</code> from <code>src</code></li>
    <li><code>Supplier</code> from <code>src.suppliers.supplier</code></li>
    <li><code>AliRequests</code> from <code>.alirequests</code></li>
    <li><code>AliApi</code> from <code>.aliapi</code></li>
    <li><code>logger</code> from <code>src.logger</code></li>
</ul>