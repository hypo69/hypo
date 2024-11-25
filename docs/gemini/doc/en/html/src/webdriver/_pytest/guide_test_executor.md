html
<h1>Module: guide_test_executor</h1>

<h2>Overview</h2>
<p>This guide provides detailed instructions for testing the <code>ExecuteLocator</code> class in a project. It covers the essential steps, from environment setup to test writing and execution.</p>

<h2>Classes</h2>

<h3><code>ExecuteLocator</code></h3>

<p><strong>Description</strong>: The <code>ExecuteLocator</code> class is designed to interact with web elements through Selenium WebDriver. It includes methods for performing various actions on webpage elements, such as retrieving attributes and sending messages.</p>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>get_webelement_by_locator</code>: Retrieves a web element using a specified locator. Handles cases with a single or multiple matching elements, and gracefully handles scenarios where no element is found.</li>
  <li><code>get_attribute_by_locator</code>: Retrieves a specific attribute from a web element.</li>
  <li><code>send_message</code>: Sends a message to a web element, allowing for optional typing speed control for realistic simulation and handling of potential errors.</li>
</ul>

<h2>Functions</h2>

<!-- Note:  The following functions are test functions, not part of the class -->

<h3><code>test_get_webelement_by_locator_single_element</code></h3>

<p><strong>Description</strong>: Tests the <code>get_webelement_by_locator</code> method for the case where a single web element is found.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>execute_locator</code> (ExecuteLocator): An instance of the <code>ExecuteLocator</code> class.</li>
  <li><code>driver_mock</code>: A mock object representing the Selenium WebDriver.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>None</code>: This function does not directly return a value, but assertions are used to verify the correctness of the method's behavior.</li>
</ul>


<h3><code>test_get_webelement_by_locator_multiple_elements</code></h3>

<p><strong>Description</strong>: Tests the <code>get_webelement_by_locator</code> method for the case where multiple web elements are found.</p>
<p><strong>Parameters</strong>:</p>
<ul>
    <li><code>execute_locator</code> (ExecuteLocator): An instance of the <code>ExecuteLocator</code> class.</li>
    <li><code>driver_mock</code>: A mock object representing the Selenium WebDriver.</li>
</ul>
<p><strong>Returns</strong>:</p>
<ul>
    <li><code>None</code>: This function does not directly return a value, but assertions are used to verify the correctness of the method's behavior.</li>
</ul>

<h3><code>test_get_webelement_by_locator_no_element</code></h3>

<p><strong>Description</strong>: Tests the <code>get_webelement_by_locator</code> method for the case where no web element is found.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>execute_locator</code> (ExecuteLocator): An instance of the <code>ExecuteLocator</code> class.</li>
  <li><code>driver_mock</code>: A mock object representing the Selenium WebDriver.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>None</code>: This function does not directly return a value, but assertions are used to verify the correctness of the method's behavior.</li>
</ul>


<h3><code>test_get_attribute_by_locator</code></h3>

<p><strong>Description</strong>: Tests the <code>get_attribute_by_locator</code> method for retrieving a specific attribute from a web element.</p>
<p><strong>Parameters</strong>:</p>
<ul>
    <li><code>execute_locator</code> (ExecuteLocator): An instance of the <code>ExecuteLocator</code> class.</li>
    <li><code>driver_mock</code>: A mock object representing the Selenium WebDriver.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
    <li><code>None</code>: This function does not directly return a value, but assertions are used to verify the correctness of the method's behavior.</li>
</ul>

<h3><code>test_send_message</code></h3>

<p><strong>Description</strong>: Tests the <code>send_message</code> method for sending a message to a web element, including handling typing speed and error scenarios with continue_on_error.</p>

<p><strong>Parameters</strong>:</p>
<ul>
    <li><code>execute_locator</code> (ExecuteLocator): An instance of the <code>ExecuteLocator</code> class.</li>
    <li><code>driver_mock</code>: A mock object representing the Selenium WebDriver.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
    <li><code>None</code>: This function does not directly return a value, but assertions are used to verify the correctness of the method's behavior.</li>
</ul>

<h3><code>test_send_message_typing_speed</code></h3>

<p><strong>Description</strong>: Tests the <code>send_message</code> method with variable typing speed.</p>
<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>execute_locator</code> (ExecuteLocator): An instance of the <code>ExecuteLocator</code> class.</li>
  <li><code>driver_mock</code>: A mock object representing the Selenium WebDriver.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>None</code>: This function does not directly return a value, but assertions are used to verify the correctness of the method's behavior.</li>
</ul>


<h2>Environment Setup</h2>

<p><strong>Dependencies</strong>: Install required libraries using:</p>
<pre><code>bash
pip install -r requirements.txt
</code></pre>
<p>Ensure that <code>requirements.txt</code> includes the necessary dependencies, which are pytest, selenium, and the appropriate Selenium WebDriver.</p>

<p><strong>WebDriver Setup</strong>: Install and configure the appropriate WebDriver for your chosen browser.</p>

<h2>Test Execution</h2>

<p>Run the tests using:</p>
<pre><code>bash
pytest tests/test_executor.py
</code></pre>

<h2>Result Interpretation</h2>

<p><code>pytest</code> will output results. Successful tests indicate that the <code>ExecuteLocator</code> class behaves as expected.</p>



<h2>Documentation Update</h2>

<p>Keep the documentation updated with any changes made to the tests or <code>ExecuteLocator</code> class.</p>

<h2>Further Resources</h2>

<ul>
  <li><a href="https://docs.pytest.org/en/latest/">pytest Documentation</a></li>
  <li><a href="https://www.selenium.dev/documentation/webdriver/">Selenium WebDriver Documentation</a></li>
</ul>