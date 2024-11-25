html
<h1>WebDriver Executor</h1>

<h2>Overview</h2>
<p>The <code>ExecuteLocator</code> class provides a framework for navigating and interacting with web pages using Selenium WebDriver. It processes locator dictionaries to perform automated actions on web elements.</p>

<h2>Classes</h2>

<h3><code>ExecuteLocator</code></h3>

<p><strong>Description</strong>: This class encapsulates the logic for executing locator-based actions on a web page using Selenium WebDriver. It handles various types of locators and actions, including clicks, sending messages, and retrieving attributes.</p>

<p><strong>Attributes</strong>:</p>
<ul>
  <li><code>driver</code> (<code>webdriver.WebDriver</code>): The Selenium WebDriver instance used for browser interactions.</li>
  <li><code>actions</code> (<code>ActionChains</code>): An instance of <code>ActionChains</code> for performing complex actions on web elements.</li>
  <li><code>by_mapping</code> (<code>dict</code>): A dictionary mapping string representations of locators to Selenium <code>By</code> objects.</li>
</ul>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__(self, driver, *args, **kwargs)</code>:
    <p><strong>Description</strong>: Initializes the <code>ExecuteLocator</code> object. Takes the WebDriver instance as a parameter and optionally other arguments.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>driver</code> (<code>webdriver.WebDriver</code>): The Selenium WebDriver instance.</li>
      <li><code>*args</code>: Variable positional arguments.</li>
      <li><code>**kwargs</code>: Variable keyword arguments.</li>
    </ul>
  </li>
  <li><code>execute_locator(self, locator: dict, message: str = None, typing_speed: float = 0, continue_on_error: bool = True) -> Union[str, list, dict, WebElement, bool]</code>:
    <p><strong>Description</strong>: Executes a locator-based action. This is the main method for interacting with web elements based on the provided locator.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>locator</code> (<code>dict</code>): A dictionary containing the locator information (e.g., selector, attribute, by).  See locator examples.</li>
      <li><code>message</code> (<code>str</code>, optional): The message to send if needed. Defaults to <code>None</code>.</li>
      <li><code>typing_speed</code> (<code>float</code>, optional): Typing speed. Defaults to 0 (normal).</li>
      <li><code>continue_on_error</code> (<code>bool</code>, optional): Whether to continue execution on errors. Defaults to <code>True</code>.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>Union[str, list, dict, WebElement, bool]</code>: The result of the executed action, which can vary based on the type of action.</li>
    </ul>
    <p><strong>Raises</strong>:</p>
    <ul>
        <li><code>WebDriverException</code>: If any Selenium WebDriver-related error occurs.</li>
        <li><code>ExecuteLocatorException</code>: If a specific error related to the locator execution occurs.</li>
    </ul>
  </li>
  <li>... (other methods)</li>
</ul>

<h2>Functions</h2>
<ul>
<li><code>get_locator_keys() -> list</code>:
    <p><strong>Description</strong>: Returns a list of available locator keys.</p>
    <p><strong>Returns</strong>:</p>
    <ul>
        <li><code>list</code>: A list of locator keys.</li>
    </ul>

</ul>

<h2>Locator Examples</h2>
<p>The module uses a specific structure for locator dictionaries. Examples of locators are included in the comments (and displayed in HTML formatting.)</p>

<h2>Error Handling</h2>
<p>The module includes comprehensive error handling using try-except blocks. It handles exceptions such as <code>NoSuchElementException</code> and <code>TimeoutException</code> gracefully.</p>



<h2>Dependencies</h2>
<p>The module relies on Selenium for WebDriver operations, including locating elements, sending keys, and interacting with web pages. It also uses internal modules for settings, logging, and exception handling.</p>

<h2>Example Usage</h2>
<p>Please see the example usage code block in the original file.</p>



```