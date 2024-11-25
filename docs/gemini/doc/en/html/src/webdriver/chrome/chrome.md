html
<h1>Chrome WebDriver Module</h1>

<h2>Overview</h2>
<p>This module provides a custom implementation of Selenium's Chrome WebDriver. It integrates settings defined in the <code>chrome.json</code> configuration file, such as user-agent and browser profile settings, to allow for flexible and automated browser interactions.</p>

<h2>Classes</h2>

<h3><code>Chrome</code></h3>

<p><strong>Description</strong>: Class for Chrome WebDriver, ensuring a single instance and centralizing configurations.</p>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__new__</code>:
    <p><strong>Description</strong>: Ensures a single instance of the Chrome WebDriver. If an instance already exists, calls <code>window_open()</code>.</p>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>Chrome</code>: The singleton instance of the Chrome WebDriver.</li>
    </ul>
  </li>
  <li><code>__init__</code>:
    <p><strong>Description</strong>: Initializes the Chrome WebDriver with specified options and profile.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>user_agent (Optional[str])</code>: The user agent string to be used. Defaults to a random user agent.</li>
    </ul>
    <p><strong>Raises</strong>:</p>
    <ul>
      <li><code>Exception</code>: Error setting up Chrome WebDriver (e.g., issues with JSON configuration or executable path).</li>
      <li><code>WebDriverException</code>: Error initializing the Chrome WebDriver.</li>
      <li><code>Exception</code>: Chrome WebDriver crashed with a general error.</li>
    </ul>
  </li>
   <li><code>_payload</code>:
    <p><strong>Description</strong>: Loads the executor for locators and JavaScript scenarios. This method initializes various JavaScript related functionalities for interaction with the webdriver.</p>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>None</code>: Method does not return a value.</li>
    </ul>
  </li>
</ul>


<h2>Functions</h2>


<h3><code>normalize_path</code></h3>

<p><strong>Description</strong>: Replaces placeholders in a path string with actual environment paths (e.g., %APPDATA%, %LOCALAPPDATA%).</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>path (str)</code>: The path string with placeholders.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>str</code>: The normalized path with environment variables substituted.</li>
</ul>