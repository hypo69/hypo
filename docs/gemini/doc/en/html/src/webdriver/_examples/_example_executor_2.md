html
<h1>hypotez/src/webdriver/_examples/_example_executor_2.py</h1>

<h2>Overview</h2>
<p>This Python file demonstrates the usage of the <code>ExecuteLocator</code> class for various testing scenarios. It provides examples of creating an <code>ExecuteLocator</code> instance and performing different tasks using its methods, including handling errors and using different locator types.</p>

<h2>Classes</h2>

<h3><code>ExecuteLocator</code></h3>

<p><strong>Description</strong>:  A class for locating and interacting with elements on a web page using Selenium WebDriver. This class provides methods for executing complex locators with various attributes and events, enabling more dynamic and controlled element interaction.</p>


<h2>Functions</h2>


<h2>Module Variables</h2>

<h3><code>MODE</code></h3>

<p><strong>Description</strong>:  A module-level variable holding the current operation mode.  Its purpose isn't fully apparent from the provided code.</p>


<h2>Examples</h2>


<h3>Simple Locator Example</h3>

<p><strong>Description</strong>: This example demonstrates the basic usage of <code>ExecuteLocator</code> to locate an element using an XPath selector and retrieve its text content.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>simple_locator</code> (dict): A dictionary defining the locator details, including the locator type (XPATH), selector, attribute to retrieve, and other options.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>result</code> (str): The text content of the located element.  Returns None if not found.</li>
</ul>

<h3>Complex Locator Example</h3>

<p><strong>Description</strong>: This demonstrates locating multiple elements and performing actions like clicking on pagination links. The example also demonstrates the usage of nested dictionaries within the locator parameters.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>complex_locator</code> (dict): A complex dictionary defining a multi-step locator, potentially containing multiple selectors and actions.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>result</code> (object): The result of executing the complex locator (likely a dictionary).  The precise nature of the returned object depends on the actions defined in the locator.</li>
</ul>

<h3>Error Handling Example</h3>

<p><strong>Description</strong>:  Illustrates how to handle potential <code>ExecuteLocatorException</code> exceptions during locator execution using the <code>continue_on_error</code> parameter to allow execution to continue even if some elements are not found.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>complex_locator</code> (dict): The locator details.</li>
  <li><code>continue_on_error</code> (bool, optional): Whether to continue on errors. Defaults to False.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>ExecuteLocatorException</code>:  Details about the error encountered.</li>
</ul>

<h3>Message Sending Example</h3>

<p><strong>Description</strong>:  Provides an example of sending text to an input field on the page.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>message_locator</code> (dict): The locator details for the input field.</li>
  <li><code>message</code> (str): The text to be sent to the field.</li>
  <li><code>typing_speed</code> (float, optional): Controls the typing speed. Defaults to 0.05.</li>
  <li><code>continue_on_error</code> (bool, optional): Whether to continue on errors. Defaults to True.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>result</code> (object): The result of sending the message.</li>
</ul>

<h3>Multiple Locators Example</h3>

<p><strong>Description</strong>:  Shows how to work with a list of locators (multi_locator), handling different operations on multiple elements simultaneously.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>multi_locator</code> (dict): A dictionary defining multiple locators, each with a corresponding set of attributes and events.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>results</code> (list): A list of results, one for each locator in the set.</li>
</ul>


<h3>Evaluating Locators Example</h3>

<p><strong>Description</strong>:  Demonstrates the use of the <code>evaluate_locator</code> method to retrieve an attribute value from a located element.</p>


<h3>Exception Handling Example</h3>

<p><strong>Description</strong>:  Provides an example of handling potential exceptions during locator execution, continuing the program flow even if an error occurs.</p>


<h3>Full Test Example</h3>

<p><strong>Description</strong>: A complete example of using the <code>execute_locator</code> method, demonstrating its functionality and error handling.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>test_locator</code> (dict): The locator details for the test.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>result</code> (object): The outcome of the test.</li>
</ul>

<p><strong>Note:</strong> This example explicitly closes the WebDriver using <code>driver.quit()</code> at the end to prevent resource leaks.</p>