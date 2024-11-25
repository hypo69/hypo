html
<h1>hypotez/src/webdriver/executor.py</h1>

<h2>Overview</h2>
<p>The <code>executor</code> module provides functionalities for interacting with web elements using Selenium, handling various locator types, and continuing execution on errors.  It converts locator dictionaries into <code>SimpleNamespace</code> objects for flexibility, allows for clicks, sending messages, executing events, and retrieving attributes.  The module supports single and multiple locators, providing versatile web element interaction automation.</p>

<h2>Classes</h2>

<h3><code>ExecuteLocator</code></h3>

<p><strong>Description</strong>: A class for handling web element locators and actions.</p>

<p><strong>Attributes</strong>:</p>
<ul>
  <li><code>driver</code> (Optional[object]): The Selenium WebDriver instance.</li>
  <li><code>actions</code> (ActionChains): Selenium ActionChains object (initialized in <code>__post_init__</code>).</li>
  <li><code>by_mapping</code> (dict): A mapping of locator strings to their corresponding Selenium <code>By</code> enum values.</li>
  <li><code>mode</code> (str): Operational mode ("debug" or "dev").</li>
</ul>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__post_init__</code>: Initializes the <code>ActionChains</code> object if a driver is provided.</li>
  <li><code>execute_locator</code>: Executes actions on a web element based on the provided locator.</li>
  <li><code>evaluate_locator</code>: Evaluates and processes locator attributes, handling special character codes.</li>
  <li><code>get_attribute_by_locator</code>: Retrieves attribute values from an element or list of elements.</li>
  <li><code>get_webelement_by_locator</code>: Fetches web elements according to the locator, with timeout handling.</li>
  <li><code>get_webelement_as_screenshot</code>: Takes a screenshot of the located web element.</li>
  <li><code>execute_event</code>: Executes various events on a web element, handling clicks, pauses, uploads, and typing messages.</li>
  <li><code>send_message</code>: Sends a message to a web element. This includes handling keyboard shortcuts, and pauses in between typing.
</ul>


<h2>Functions</h2>

<!-- Function descriptions would go here -->

</ul>