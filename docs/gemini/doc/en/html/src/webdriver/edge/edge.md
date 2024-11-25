html
<h1>hypotez/src/webdriver/edge/edge.py</h1>

<h2>Overview</h2>
<p>This module defines a custom Edge WebDriver class, <code>Edge</code>, extending the base <code>selenium.webdriver.Edge</code> class. It simplifies configuration using the <code>fake_useragent</code> library and provides enhanced functionality through methods for executing locators and JavaScript scenarios.</p>

<h2>Classes</h2>

<h3><code>Edge</code></h3>

<p><strong>Description</strong>: A custom Edge WebDriver class with additional methods for interacting with the browser, enhancing functionality and simplifying configuration. It uses <code>fake_useragent</code> for generating user-agents and loads executors for locators and JavaScript.</p>

<p><strong>Attributes</strong>:</p>
<ul>
  <li><code>driver_name</code> (str): Name of the WebDriver used (defaulting to 'edge').</li>
</ul>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__(self, user_agent: Optional[dict] = None, *args, **kwargs) -> None</code>
    <p><strong>Description</strong>: Initializes the Edge WebDriver with the specified user agent and options. If <code>user_agent</code> is not provided, a random user agent is generated.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>user_agent</code> (Optional[dict], optional): Dictionary to specify the user agent. If <code>None</code>, a random user agent is generated. Defaults to <code>None</code>.</li>
    </ul>
    <p><strong>Raises</strong>:</p>
    <ul>
      <li><code>WebDriverException</code>: Exception raised if the Edge WebDriver fails to start.</li>
      <li><code>Exception</code>: General error exception raised if the WebDriver crashes.</li>
    </ul>
  </li>
  <li><code>_payload(self) -> None</code>
    <p><strong>Description</strong>: Loads executors for locators and JavaScript scenarios.</p>
  </li>
  <li><code>set_options(self, opts: Optional[List[str]] = None) -> EdgeOptions</code>
    <p><strong>Description</strong>: Creates and configures launch options for the Edge WebDriver.
    </p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>opts</code> (Optional[List[str]], optional): A list of options to add to the Edge WebDriver. Defaults to <code>None</code>.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>EdgeOptions</code>: Configured <code>EdgeOptions</code> object.</li>
    </ul>
  </li>
</ul>


<h2>Functions</h2>

<!-- No functions in this module -->