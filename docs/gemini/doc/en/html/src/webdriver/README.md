html
<h1>WebDriver Executor Module Documentation</h1>

<h2>Overview</h2>
<p>The WebDriver Executor module provides an execution framework for navigating and interacting with web pages using a WebDriver. It processes scripts and locators to perform automated actions on web elements.</p>

<h2>Main Features</h2>

<ul>
  <li><b>Locator Handling</b>
    <ul>
      <li><b>Initialization</b>: The <code>ExecuteLocator</code> class is initialized with a WebDriver instance and optional arguments. It sets up the WebDriver and action chains for interacting with web elements.</li>
      <li><b>Locator Execution</b>: The <code>execute_locator</code> method processes a locator dictionary to find and interact with web elements, handling different locator types and actions.</li>
      <li><b>Element Retrieval</b>: The <code>get_webelement_by_locator</code> method retrieves web elements based on locator information (e.g., XPath, ID, CSS selectors). It waits for elements to be present and returns a single element, a list of elements, or <code>False</code> if no elements are found.</li>
      <li><b>Attribute Retrieval</b>: The <code>get_attribute_by_locator</code> method retrieves attributes from elements identified by a locator.</li>
      <li><b>Message Sending</b>: The <code>send_message</code> method sends text input to web elements, simulating typing with configurable speed.</li>
    </ul>
  </li>
  <li><b>Screenshots</b>
    <ul>
      <li><b>Element Screenshot</b>: The <code>get_webelement_as_screenshot</code> method captures a screenshot of a web element and returns it as a PNG image. Supports capturing multiple elements and handles errors if elements are not found.</li>
    </ul>
  </li>
  <li><b>Click Action</b>
    <ul>
      <li><b>Element Click</b>: The <code>click</code> method performs a click action on a web element identified by a locator. Handles navigation to new pages or window openings, logging errors if the click fails.</li>
    </ul>
  </li>
  <li><b>Locator Evaluation</b>
    <ul>
      <li><b>Attribute Evaluation</b>: The <code>evaluate_locator</code> method evaluates locator attributes, handling placeholders like <code>%EXTERNAL_MESSAGE%</code>.</li>
    </ul>
  </li>
</ul>

<h2>Error Handling</h2>
<p>The module uses try-except blocks to catch and log errors during operations, such as finding elements, sending messages, and taking screenshots.  Specific exceptions (e.g., <code>NoSuchElementException</code>, <code>TimeoutException</code>) are handled to prevent script crashes.</p>

<h2>Usage</h2>
<p>To use the module, instantiate an <code>ExecuteLocator</code> object with a WebDriver instance.  Then, use methods like <code>execute_locator</code>, <code>get_webelement_by_locator</code>, and others to interact with web elements.  Refer to the example usage below.</p>


<h2>Classes</h2>

<h3><code>ExecuteLocator</code></h3>

<p><b>Description</b>: The core class for executing locators and actions on web elements using Selenium WebDriver.</p>

<p><b>Attributes</b>:</p>
<ul>
  <li><code>driver</code> (WebDriver): A reference to the WebDriver instance.</li>
  <li><code>actions</code> (ActionChains): An ActionChains instance for performing complex actions on web elements.</li>
  <li><code>by_mapping</code> (dict): Maps locator strings to Selenium <code>By</code> objects.</li>
</ul>

<p><b>Methods</b>:</p>
<ul>
  <li><code>__init__(self, driver, *args, **kwargs)</code></li>
  <li><code>execute_locator(self, locator: dict, message: str = None, typing_speed: float = 0, continue_on_error: bool = True) -> Union[str, list, dict, WebElement, bool]</code></li>
  <li><code>get_webelement_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> WebElement | List[WebElement] | bool</code></li>
  <li><code>get_attribute_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> str | list | dict | bool</code></li>
  <li><code>send_message(self, locator: dict | SimpleNamespace, message: str, typing_speed: float, continue_on_error: bool) -> bool</code></li>
  <li><code>evaluate_locator(self, attribute: str | list | dict) -> str</code></li>
  <li><code>get_webelement_as_screenshot(self, locator: dict | SimpleNamespace, message: str = None) -> str | None</code></li>
  <li><code>click(self, locator: dict) -> bool</code></li>
  <li>... (other methods)</li>
</ul>

<h2>Dependencies</h2>
<p>Selenium, Python's built-in libraries for exception handling and time management.</p>

<h2>Example Usage</h2>
<pre><code>python
from src.webdriver import Driver, Chrome
from selenium.webdriver.common.by import By

def main():
    # ... (example usage code from the input) ...

if __name__ == "__main__":
    main()
</code></pre>


</body>