html
<h1>Driver Module Documentation</h1>

<h2>Overview</h2>
<p>This module provides a base driver class and implementations for various web drivers (Chrome, Firefox, Edge) using Selenium.</p>

<h2>Classes</h2>

<h3><code>Driver</code></h3>

<p><strong>Description</strong>: Base class for web driver interactions. This class handles common driver functionalities, such as navigating, interacting with elements, and managing cookies.</p>

<p><strong>Attributes</strong>:</p>
<ul>
<li><code>previous_url: str</code>: Stores the previous URL visited.</li>
<li><code>referrer: str</code>: Stores the referrer URL.</li>
<li><code>page_lang: str</code>: Stores the language of the page.</li>
<li><code>ready_state</code>: Stores the current state of the page loading.</li>
<li><code>get_page_lang()</code>: Retrieves the language of the current page.</li>
<li><code>unhide_DOM_element()</code>: Unhides a DOM element.</li>
<li><code>get_referrer()</code>: Retrieves the referrer URL.</li>
<li><code>window_focus()</code>: Sets the focus to the current window.</li>
<li><code>execute_locator()</code>: Executes a locator command.</li>
<li><code>click()</code>: Clicks on a web element.</li>
<li><code>get_webelement_as_screenshot()</code>: Takes a screenshot of a web element.</li>
<li><code>get_attribute_by_locator()</code>: Retrieves an attribute value using a locator.</li>
<li><code>send_message()</code>: Sends a message to the driver.</li>
<li><code>send_key_to_webelement()</code>: Sends a key sequence to a web element.</li>
</ul>


<p><strong>Methods</strong>:</p>
<ul>
<li><code>driver_payload(self)</code>: Retrieves the payload data for the driver.</li>
<li><code>scroll(self, scrolls: int, frame_size: int, direction: str, delay: float) -> None | bool</code>: Scrolls through the page.
    <ul>
        <li><code>scrolls</code> (int): Number of scrolls.</li>
        <li><code>frame_size</code> (int): Size of the frame to scroll.</li>
        <li><code>direction</code> (str): Direction of the scroll.</li>
        <li><code>delay</code> (float): Delay between scrolls.</li>
        <li><code>Returns</code>: <code>None | bool</code>: Returns <code>None</code> on success or a boolean indicating the success of the scroll.</li>
    </ul>
</li>

<li><code>locale(self) -> None | str</code>: Retrieves the locale of the current page.</li>
<li><code>get_url(self, url: str) -> bool</code>: Retrieves the URL.
    <ul>
      <li><code>url</code> (str): URL to retrieve.</li>
      <li><code>Returns</code>: <code>bool</code>: Returns True on success, otherwise False.</li>
    </ul>
</li>
<li><code>extract_domain(self, url: str) -> str</code>: Extracts the domain from a URL.
    <ul>
        <li><code>url</code> (str): The input URL</li>
        <li><code>Returns</code>: <code>str</code>: The extracted domain</li>
    </ul>
</li>

<li><code>_save_cookies_localy(self, to_file: str | Path) -> bool</code>: Saves cookies locally.
    <ul>
        <li><code>to_file</code> (str | Path): The path to save the cookies to.</li>
        <li><code>Returns</code>: <code>bool</code>: True if saving is successful, False otherwise.</li>
    </ul>
</li>

<li><code>page_refresh(self) -> bool</code>: Refreshes the current page.
    <li><code>Returns</code>: <code>bool</code>: True if refresh is successful, False otherwise.</li>
</li>
<li><code>wait(self, interval: float)</code>: Waits for a certain interval.
    <ul>
        <li><code>interval</code> (float): The interval in seconds.</li>
    </ul>
</li>
<li><code>delete_driver_logs(self) -> bool</code>: Deletes the driver logs.
    <ul>
        <li><code>Returns</code>: <code>bool</code>: True if deletion is successful, False otherwise.</li>
    </ul>
</li>
</ul>


<h3><code>DriverMeta</code></h3>

<p><strong>Description</strong>: Metaclass for the <code>Driver</code> class.  Handles creation of specific driver instances (Chrome, Firefox, etc.).</p>

<p><strong>Methods</strong>:</p>

<ul>
    <li><code>__call__(cls, webdriver_cls, *args, **kwargs)</code>: Creates a specific driver instance.
        <ul>
          <li><code>webdriver_cls</code> (class): The specific driver class (e.g., <code>Chrome</code>).</li>
        </ul>
    </li>
</ul>

<h2>Usage Example</h2>
<p>Shows how to use the driver class (example using Chrome driver):</p>
<pre><code class="language-python">from src.webdriver import Driver, Chrome
d = Driver(Chrome)
</code></pre>
<p>Note: Actual instantiation and use cases for <code>Driver</code>, and other specialized drivers (e.g., <code>Chrome</code>, <code>Firefox</code>, <code>Edge</code>) would be documented in their own respective modules.</p>

<h2>Functions</h2>
<!-- Add function documentation here if there are any functions outside of class methods -->