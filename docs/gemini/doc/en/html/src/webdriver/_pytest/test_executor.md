html
<h1>hypotez/src/webdriver/_pytest/test_executor.py</h1>

<h2>Overview</h2>
<p>This module contains test cases for the <code>ExecuteLocator</code> class, which interacts with web elements.  It utilizes pytest for testing and mocks Selenium WebDriver interactions.  The module defines fixtures for a mocked driver and an <code>ExecuteLocator</code> instance, along with tests for various scenarios like finding elements by locator, retrieving attributes, sending messages, and handling cases where elements are not found.</p>

<h2>Fixtures</h2>

<h3><code>driver_mock</code></h3>

<p><strong>Description</strong>: Creates a mock object representing a WebDriver instance.</p>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>MagicMock</code>: A mocked WebDriver object.</li>
</ul>


<h3><code>execute_locator</code></h3>

<p><strong>Description</strong>: Creates an instance of the <code>ExecuteLocator</code> class using a mocked WebDriver.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>driver_mock</code> (<code>MagicMock</code>): The mocked WebDriver instance.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>ExecuteLocator</code>: An instance of the <code>ExecuteLocator</code> class.</li>
</ul>


<h2>Functions</h2>

<h3><code>test_get_webelement_by_locator_single_element</code></h3>

<p><strong>Description</strong>: Tests the retrieval of a single web element using a locator.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>execute_locator</code>: The <code>ExecuteLocator</code> instance.</li>
  <li><code>driver_mock</code>: The mocked WebDriver instance.</li>
  <li><code>locator</code>: A dictionary containing the locator details.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>WebElement</code>: The retrieved web element.</li>
</ul>

<p><strong>Assertions</strong>:</p>
<ul>
<li> Verifies that <code>driver_mock.find_elements</code> is called with the correct locator.</li>
<li> Checks that the returned element matches the expected mock.</li>
</ul>


<h3><code>test_get_webelement_by_locator_multiple_elements</code></h3>

<p><strong>Description</strong>: Tests the retrieval of multiple web elements using a locator.</p>
<p><strong>Parameters</strong> and <strong>Returns</strong> are similar to <code>test_get_webelement_by_locator_single_element</code>, but with multiple elements being returned.</p>

<p><strong>Assertions</strong>:</p>
<ul>
<li> Verifies that <code>driver_mock.find_elements</code> is called with the correct locator.</li>
<li> Checks that the returned elements match the expected list of mocks.</li>
</ul>


<h3><code>test_get_webelement_by_locator_no_element</code></h3>

<p><strong>Description</strong>: Tests the case where no element is found using the locator.</p>
<p><strong>Parameters</strong> and <strong>Returns</strong> are similar to <code>test_get_webelement_by_locator_single_element</code>, but with an empty list returned from <code>driver_mock.find_elements</code>.</p>

<p><strong>Assertions</strong>:</p>
<ul>
<li> Verifies that <code>driver_mock.find_elements</code> is called with the correct locator.</li>
<li> Checks that the returned value is <code>False</code>, indicating no element was found.</li>
</ul>


<h3><code>test_get_attribute_by_locator</code></h3>

<p><strong>Description</strong>: Tests the retrieval of an attribute from a web element using a locator.</p>
<p><strong>Parameters</strong>:</p>
<ul>
<li> <code>locator</code> (dictionary): Includes an "attribute" key to specify the attribute to retrieve.
</ul>
<p><strong>Assertions</strong>:</p>
<ul>
<li> Verifies that <code>driver_mock.find_elements</code> and <code>element.get_attribute</code> are called correctly.</li>
<li> Checks that the returned attribute value matches the expected one.</li>
</ul>



<h3><code>test_send_message</code></h3>

<p><strong>Description</strong>: Tests sending a message (text input) to a web element with default typing speed and error handling.</p>
<p><strong>Assertions</strong>:</p>
<ul>
<li> Checks the correct call to <code>driver_mock.find_elements</code>.</li>
<li> Asserts that the <code>send_keys</code> method on the element is called with the provided message.</li>
<li> Verifies that the returned result is True.</li>
</ul>


<h3><code>test_send_message_typing_speed</code></h3>

<p><strong>Description</strong>: Tests sending a message with a specific typing speed.</p>
<p><strong>Assertions</strong>:</p>
<ul>
<li> Checks that <code>driver_mock.find_elements</code> is called once.</li>
<li> Checks that <code>element.send_keys</code> is called multiple times (matching the message length).</li>
<li> Asserts that the mocked <code>time.sleep</code> function is called with the specified <code>typing_speed</code>.</li>
<li> Verifies that the returned result is True.</li>
</ul>