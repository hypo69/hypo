html
<h1>hypotez/src/webdriver/driver.py</h1>

<h2>Overview</h2>
<p>This module provides a class for working with Selenium webdrivers. The <code>Driver</code> class provides a unified interface for interacting with various webdrivers like Chrome, Firefox, and Edge.  It handles driver initialization, navigation, cookie management, and exception handling.</p>

<h2>Classes</h2>

<h3><code>Driver</code></h3>

<p><strong>Description</strong>: A unified class for interacting with Selenium WebDriver.  It provides a consistent interface for different webdrivers, simplifying interaction with various browsers.</p>

<p><strong>Attributes</strong>:</p>
<ul>
  <li><code>driver</code> (selenium.webdriver): The Selenium WebDriver instance.</li>
</ul>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__(self, webdriver_cls, *args, **kwargs)</code>: Initializes a <code>Driver</code> instance.
    <ul>
      <li><strong>Parameters</strong>:
        <ul>
          <li><code>webdriver_cls</code> (type): The WebDriver class (e.g., <code>Chrome</code>).</li>
          <li><code>args</code>: Positional arguments for the webdriver.</li>
          <li><code>kwargs</code>: Keyword arguments for the webdriver.</li>
        </ul>
      </li>
      <li><strong>Raises</strong>:
        <ul>
          <li><code>TypeError</code>: If <code>webdriver_cls</code> is not a valid WebDriver class.</li>
        </ul>
      </li>
      <li><strong>Example</strong>:
        <code>from selenium.webdriver import Chrome
driver = Driver(Chrome, executable_path='/path/to/chromedriver')</code>
      </li>
    </ul>
  </li>
  <li><code>__init_subclass__(cls, *, browser_name=None, **kwargs)</code>: Automatically called when a subclass of <code>Driver</code> is created.
    <ul>
      <li><strong>Parameters</strong>:
        <ul>
          <li><code>browser_name</code> (str): The name of the browser.</li>
          <li><code>kwargs</code>: Additional arguments.</li>
        </ul>
      </li>
      <li><strong>Raises</strong>:
        <ul>
          <li><code>ValueError</code>: If <code>browser_name</code> is not provided.</li>
        </ul>
      </li>
    </ul>
  </li>
  <li><code>__getattr__(self, item)</code>: Proxy for accessing driver attributes.
    <ul>
      <li><strong>Parameters</strong>:
        <ul>
          <li><code>item</code> (str): The attribute name.</li>
        </ul>
      </li>
      <li><strong>Example</strong>:
      <code>driver.current_url</code></li>
    </ul>
  </li>
   <li><code>scroll(self, scrolls=1, frame_size=600, direction='both', delay=.3) -> bool</code>: Scrolls the page in the specified direction.
    <ul>
        <li><strong>Parameters</strong>, **Returns** and **Raises**: See docstring.</li>
    </ul>
  </li>
  <li><code>get_url(self, url: str) -> bool</code>: Navigates to a given URL.
    <ul>
        <li><strong>Parameters</strong>, **Returns** and **Raises**: See docstring.</li>
    </ul>
  </li>
  <li><code>window_open(self, url: Optional[str] = None) -> None</code>: Opens a new tab/window.
    <ul><li><strong>Parameters</strong>: See docstring.</li></ul>
  </li>
   <li><code>wait(self, delay: float = .3) -> None</code>: Pauses execution.
    <ul><li><strong>Parameters</strong>: See docstring.</li></ul>
  </li>
  <li><code>_save_cookies_localy(self) -> None</code>: Saves current cookies to a file.
    <ul><li><strong>Returns</strong> and **Raises**: See docstring.</li></ul>
  </li>
  <li><code>fetch_html(self, url: str) -> Optional[bool]</code>: Fetches HTML content from a file or URL.
    <ul><li><strong>Parameters</strong>, **Returns** and **Raises**: See docstring.</li></ul>
  </li>
  <li><code>locale(self) -> Optional[str]</code>: Determines the language of the page.
    <ul><li><strong>Parameters</strong>, **Returns** and **Example**: See docstring.</li></ul>
  </li>


</ul>


<h2>Functions</h2>

<p>(None found in the provided code)</p>