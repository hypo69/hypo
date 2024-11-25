html
<h1>hypotez/src/webdriver/_examples/_example_executor.py</h1>

<h2>Overview</h2>
<p>This module provides an example of using the <code>ExecuteLocator</code> class for interacting with web elements using Selenium. It demonstrates various functionalities, including locating elements, handling different events, sending messages, and error handling.</p>

<h2>Classes</h2>

<h3><code>ExecuteLocator</code></h3>

<p><strong>Description</strong>: A class that extends the Selenium webdriver functionality to handle various web element interactions.  It allows for specifying locators with optional actions (events) and error handling.</p>

<p><strong>Methods</strong>:</p>
<ul>
<li><code>execute_locator</code>: Executes a given locator to locate and interact with a web element.  It takes a locator dictionary as input and optionally handles exceptions and continuing on errors.
<ul>
<li><strong>Parameters</strong>:
<ul>
<li><code>locator</code> (dict): A dictionary defining the locator parameters (by, selector, attribute, event, etc.).</li>
<li><code>continue_on_error</code> (bool, optional): Whether to continue execution if an error occurs. Defaults to False.</li>
</ul></li>
<li><strong>Returns</strong>:
<ul>
<li><code>result</code> (mixed): The result of the locator execution, which could be the value of an attribute, element if found, or None.</li>
</ul></li>
<li><strong>Raises</strong>:
<ul>
<li><code>ExecuteLocatorException</code>: If a problem occurs during locator execution.</li>
</ul></li>
</ul></li>

<li><code>send_message</code>: Simulates user input by sending a message to a specified element.
<ul>
<li><strong>Parameters</strong>:
<ul>
<li><code>locator</code> (dict): The locator dictionary defining the element to interact with.</li>
<li><code>message</code> (str): The message to send.</li>
<li><code>typing_speed</code> (float, optional): The speed at which the message is typed. Defaults to 0.05.</li>
<li><code>continue_on_error</code> (bool, optional): Whether to continue execution if an error occurs. Defaults to False.</li>
</ul></li>
<li><strong>Returns</strong>:
<ul>
<li><code>result</code> (mixed): The result of the sending message operation, e.g., True if successful or a descriptive error message if not.</li>
</ul></li>
<li><strong>Raises</strong>:
<ul>
<li><code>ExecuteLocatorException</code>: If a problem occurs during message sending.</li>
</ul></li>
</ul></li>

<li><code>evaluate_locator</code>:  Evaluates a locator attribute, commonly used for getting values like text content or attributes.
<ul>
<li><strong>Parameters</strong>:
<ul>
<li><code>locator_attribute</code> (str): The attribute of the element to evaluate.</li>
</ul></li>
<li><strong>Returns</strong>:
<ul>
<li><code>attribute_value</code> (mixed): The value of the specified attribute.</li>
</ul></li>
</ul></li>

</ul>


<h2>Functions</h2>

<h3><code>main</code></h3>

<p><strong>Description</strong>: The main function that orchestrates the entire example execution.
</p>
<p><strong>Parameters</strong>: None</p>

<p><strong>Returns</strong>: None</p>

<p><strong>Raises</strong>: None</p>


</html>