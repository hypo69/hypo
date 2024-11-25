html
<h1>webdriver/executor Module</h1>

<h2>Overview</h2>
<p>This module provides functions for interacting with web elements using locators. It handles various actions such as executing locators, retrieving web elements, getting attributes, sending messages, and fetching URLs.</p>

<h2>Functions</h2>

<h3><code>execute_locator</code></h3>

<p><strong>Description</strong>: Executes actions on a web element based on the provided locator.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>locator</code> (dict): A dictionary or object containing locator information (e.g., type, selector).</li>
  <li><code>message</code> (str, optional): Optional message to send to the web element (e.g., text to enter). Defaults to ''.</li>
  <li><code>typing_speed</code> (float, optional): Speed of typing when sending a message (in seconds between keystrokes). Defaults to 0.0.</li>
  <li><code>continue_on_error</code> (bool, optional): Flag indicating whether to continue execution if an error occurs. Defaults to True.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>any</code>: The result of the locator execution, which could be the web element, a list of elements, an attribute value, or action result.</li>
</ul>


<h3><code>get_webelement_by_locator</code></h3>

<p><strong>Description</strong>: Finds and returns a web element based on the provided locator.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>locator</code> (dict): A dictionary or object containing locator information (e.g., type, selector).</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>any</code>: The found web element or a list of elements, depending on the locator's specification.</li>
</ul>


<h3><code>get_attribute_by_locator</code></h3>

<p><strong>Description</strong>: Retrieves the attribute value of a web element identified by the locator.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>locator</code> (dict): A dictionary or object containing locator information (e.g., type, selector).</li>
  <li><code>message</code> (str, optional): Optional message to send to the web element (e.g., text to enter before retrieving attribute). Defaults to ''.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>any</code>: The value of the attribute of the found web element, or None if an error occurs.</li>
</ul>


<h3><code>send_message</code></h3>

<p><strong>Description</strong>: Sends a message (e.g., text) to a web element identified by the locator.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>locator</code> (dict): A dictionary or object containing locator information (e.g., type, selector).</li>
  <li><code>message</code> (str): The message to send to the web element.</li>
  <li><code>typing_speed</code> (float, optional): Speed of typing when sending the message (in seconds between keystrokes). Defaults to 0.0.</li>
  <li><code>continue_on_error</code> (bool, optional): Flag indicating whether to continue execution if an error occurs. Defaults to True.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>bool</code>: True if the message is sent successfully, otherwise False.</li>
</ul>


<h3><code>get_url</code></h3>

<p><strong>Description</strong>: Retrieves HTML content from a specified URL or file path.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>url</code> (str): The URL or file path to fetch the HTML content from.</li>
  <li><code>protocol</code> (str, optional): The protocol to use for URL (default is 'https://'). Defaults to 'https://'.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>bool</code>: True if the content is successfully fetched, otherwise False.</li>
</ul>