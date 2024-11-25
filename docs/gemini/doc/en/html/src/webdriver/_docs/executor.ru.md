html
<h1>Module executor</h1>

<h2>Overview</h2>
<p>This module provides the <code>ExecuteLocator</code> class for interacting with web page elements using Selenium WebDriver, based on locator dictionaries.</p>

<h2>Classes</h2>

<h3><code>ExecuteLocator</code></h3>

<p><strong>Description</strong>: This class handles various actions with web page elements using Selenium WebDriver, based on locator configurations.  It provides methods for locating elements, retrieving attributes, sending messages, and handling different locator types.</p>

<p><strong>Attributes</strong>:</p>
<ul>
  <li><code>driver</code> (<code>webdriver</code>): The Selenium WebDriver instance used for browser interaction.</li>
  <li><code>actions</code> (<code>ActionChains</code>): The ActionChains object for complex element interactions.</li>
  <li><code>by_mapping</code> (<code>dict</code>): A dictionary mapping string locator types to Selenium's <code>By</code> objects.</li>
</ul>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__(self, driver, *args, **kwargs)</code>
    <p><strong>Description</strong>: Initializes the <code>ExecuteLocator</code> object.  Takes a WebDriver instance and optional arguments.</p>
    <p><strong>Args</strong>:</p>
    <ul>
      <li><code>driver</code> (<code>webdriver</code>): The Selenium WebDriver instance.</li>
      <li><code>*args</code>: Variable positional arguments.</li>
      <li><code>**kwargs</code>: Arbitrary keyword arguments.</li>
    </ul>
  </li>
  <li><code>execute_locator(self, locator: dict, message: str = None, typing_speed: float = 0, continue_on_error: bool = True) -> Union[str, list, dict, WebElement, bool]</code>
    <p><strong>Description</strong>: Executes actions based on the provided <code>locator</code> dictionary.  Handles different locator types and actions (e.g., clicking, sending messages).</p>
    <p><strong>Args</strong>:</p>
    <ul>
      <li><code>locator</code> (<code>dict</code>): Dictionary containing parameters for the action to be performed.</li>
      <li><code>message</code> (<code>str</code>, optional): The message to be sent (e.g., text input). Defaults to <code>None</code>.</li>
      <li><code>typing_speed</code> (<code>float</code>, optional): Speed of typing, in characters per second. Defaults to <code>0</code>.</li>
      <li><code>continue_on_error</code> (<code>bool</code>, optional): Whether to continue execution on errors. Defaults to <code>True</code>.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>Union[str, list, dict, WebElement, bool]</code>: Result of the execution.</li>
    </ul>
    <p><strong>Raises</strong>:</p>
    <ul>
      <li><code>NoSuchElementException</code>: Element not found.</li>
      <li><code>TimeoutException</code>: Element not found within the specified timeout.</li>
      <li><code>DefaultSettingsException</code>: Problems with default settings.</li>
	  <li><code>WebDriverException</code>: General WebDriver errors.</li>
	  <li><code>ExecuteLocatorException</code>: Specific errors during locator execution.</li>
    </ul>
  </li>
  <li><code>get_webelement_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> WebElement | List[WebElement] | bool</code>
  <li><code>get_attribute_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> str | list | dict | bool</code>
  <li><code>_get_element_attribute(self, element: WebElement, attribute: str) -> str | None</code>
  <li><code>send_message(self, locator: dict | SimpleNamespace, message: str, typing_speed: float, continue_on_error:bool) -> bool</code>
  <li><code>evaluate_locator(self, attribute: str | list | dict) -> str</code>
  <li><code>_evaluate(self, attribute: str) -> str | None</code>
  <li><code>get_locator_keys() -> list</code></li>
</ul>


<h2>Functions</h2>
<p>(No functions listed directly, but helper methods and static methods are mentioned within the class.)</p>

<h2>Examples</h2>
<p>(Locator examples are given in JSON format)</p>

<h2>Imports</h2>
<p>Imports are listed in the input code, which provide modules for Selenium, internal utilities, and logging.</p>