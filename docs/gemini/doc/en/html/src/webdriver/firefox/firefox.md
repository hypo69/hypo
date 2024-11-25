html
<h1>Firefox WebDriver</h1>

<h2>Overview</h2>
<p>This module defines a subclass of <code>selenium.webdriver.Firefox</code> called <code>Firefox</code>. It provides additional functionality, including launching Firefox in kiosk mode and setting up a Firefox profile for the WebDriver.</p>

<h2>Classes</h2>

<h3><code>Firefox</code></h3>

<p><strong>Description</strong>: A subclass of <code>selenium.webdriver.Firefox</code> offering extended capabilities.</p>

<p><strong>Attributes</strong>:</p>
<ul>
  <li><code>driver_name</code> (str): Name of the WebDriver (defaults to 'firefox').</li>
</ul>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__</code>: Initializes the Firefox WebDriver.</li>
</ul>

<h3><code>__init__</code></h3>

<p><strong>Description</strong>: Initializes the Firefox WebDriver with specified launch options, profile, geckodriver version, Firefox version, and user agent.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>profile_name</code> (Optional[str], optional): Name of the Firefox profile to use.</li>
  <li><code>geckodriver_version</code> (Optional[str], optional): Version of the geckodriver to use.</li>
  <li><code>firefox_version</code> (Optional[str], optional): Version of Firefox to use.</li>
  <li><code>user_agent</code> (Optional[dict], optional): A dictionary containing user agent settings.</li>
  <li><code>*args</code>: Variable length argument list.</li>
  <li><code>**kwargs</code>: Arbitrary keyword arguments.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>None</code>: This method does not return a value.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>WebDriverException</code>: Raised if the driver cannot be started.</li>
  <li><code>Exception</code>: Raised for other errors during initialization.</li>
</ul>

<h3><code>_payload</code></h3>

<p><strong>Description</strong>: Loads executors for locators and JavaScript scenarios.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li>None</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>None</code>: This method does not return a value.</li>
</ul>


<h2>Functions</h2>

<!-- No functions found in the provided code -->


```