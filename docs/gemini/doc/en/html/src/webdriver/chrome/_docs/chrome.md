html
<h1>Chrome WebDriver Documentation</h1>

<h2>Overview</h2>
<p>This module provides a custom Chrome WebDriver class, extending the `selenium.webdriver.Chrome` class, offering additional functionality for WebDriver initialization and configuration.  It leverages settings from a configuration file (`chrome.json`) for driver and browser paths and handles potential errors during initialization. The module dynamically determines a free port for the WebDriver instance, crucial for avoiding conflicts and ensuring smooth operation.</p>

<h2>Classes</h2>

<h3><code>Chrome</code></h3>

<p><strong>Description</strong>: A subclass of `selenium.webdriver.Chrome` providing additional functionality for configuring and initializing a Chrome WebDriver instance.</p>

<p><strong>Attributes</strong>:</p>
<ul>
  <li><code>driver_name</code> (str): The name of the WebDriver ('chrome').</li>
  <li><code>d</code> (webdriver.Chrome): The WebDriver instance (initialized in the constructor).</li>
  <li><code>options</code> (ChromeOptions): Chrome browser options object.</li>
  <li><code>user_agent</code> (dict): User agent settings for the browser.</li>
</ul>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__</code>(self, user_agent: dict = None, *args, **kwargs) -> None:
    <p><strong>Description</strong>: Initializes the Chrome WebDriver with the specified options and profile. Loads settings from `chrome.json`, sets up ChromeDriver and Chrome binary paths, and creates a ChromeService object. Configures the browser with a free port and the user-agent, and handles exceptions during initialization.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>user_agent</code> (dict, optional): User-agent settings. Defaults to a randomly generated user-agent from the `fake_useragent` library.</li>
    </ul>
    <p><strong>Raises</strong>:</p>
    <ul>
      <li><code>Exception</code>: General error during initialization.</li>
      <li><code>WebDriverException</code>: Error during initialization of the WebDriver.</li>
    </ul>
  </li>
  <li><code>find_free_port</code>(self, start_port: int, end_port: int) -> int | None:
    <p><strong>Description</strong>: Finds a free port within the specified range.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>start_port</code> (int): The starting port for the search.</li>
      <li><code>end_port</code> (int): The ending port for the search.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li>int | None: A free port if found, otherwise None.</li>
    </ul>
    <p><strong>Raises</strong>:</p>
    <ul>
      <li><code>OSError</code>: If a port is already in use.</li>
    </ul>
  </li>
  <li><code>set_options</code>(self, settings: list | dict | None = None) -> ChromeOptions:
    <p><strong>Description</strong>: Sets launch options for the Chrome WebDriver based on the provided settings (e.g. from `chrome.json`).</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>settings</code> (list | dict | None, optional): Settings to configure the launch options from the configuration file. Defaults to None.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li>ChromeOptions: A `ChromeOptions` object with the configured launch options.</li>
    </ul>
    <p><strong>Note</strong>: The method parses the settings in the format `key=value`, which is used for browser parameters.</p>
  </li>
</ul>


<h2>Functions</h2>
<p>(None in this file)</p>


<h2>Configuration File (`chrome.json`)</h2>

<p><strong>Description</strong>: The configuration file containing paths to ChromeDriver, Chrome binary, and other relevant settings for the Chrome WebDriver.</p>
<p><strong>Components</strong>:</p>
<ul>
  <li><code>profiles</code>: Directory paths for various Chrome profiles.</li>
  <li><code>driver</code>:
    <ul>
      <li><code>chromedriver</code>: Path to the ChromeDriver executable.</li>
      <li><code>chrome_binary</code>: Path to the Chrome executable.</li>
    </ul>
  </li>
  <li><code>headers</code>: HTTP headers to configure the WebDriver.</li>
</ul>
<p><strong>Example Structure</strong>: (Refer to provided example in the original input). </p>


```
```