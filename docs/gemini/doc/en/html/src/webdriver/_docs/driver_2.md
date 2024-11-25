html
<h1>DriverBase Module Documentation</h1>

<h2>Overview</h2>
<p>This module defines the <code>DriverBase</code> class, a base class for various WebDriver implementations.  It encapsulates common methods and attributes applicable to different webdrivers (e.g., Chrome, Firefox, Edge), providing functionalities for page interaction, JavaScript execution, and cookie management.</p>

<h2>Table of Contents</h2>
<ul>
  <li><a href="#driverbase-class">DriverBase Class</a></li>
</ul>

<h2 id="driverbase-class">DriverBase Class</h2>

<h3><code>DriverBase</code></h3>

<p><strong>Description</strong>: Base class for a WebDriver with common attributes and methods. This class contains methods and attributes common to all WebDriver implementations, including functionalities for page interaction, JavaScript execution, and managing cookies.</p>

<p><strong>Attributes</strong>:</p>
<ul>
  <li><code>previous_url</code>: Stores the URL of the previous page.</li>
  <li><code>referrer</code>: Stores the referrer URL.</li>
  <li><code>page_lang</code>: Stores the language of the current page.</li>
  <li><code>ready_state</code>: (Details about this attribute would require the Python implementation)</li>
  <li><code>get_page_lang</code>: (Details about this method would require the Python implementation)</li>
  <!-- Add more attributes as necessary -->
</ul>


<p><strong>Methods</strong>:</p>
<ul>
  <li><code>driver_payload()</code>: Initializes JavaScript and ExecuteLocator for page command execution.
    <ul>
      <li><strong>Description</strong>: Initializes necessary components for interaction with the page.</li>
      <!-- Add specific details about parameters and return values as they exist in the Python code -->
    </ul>
  </li>
  <li><code>scroll(scrolls: int = 3, frame_size: int = 500, direction: str = 'forward', delay: float = 0.5)</code>: Scrolls the page.
    <ul>
      <li><strong>Description</strong>: Scrolls the page in the specified direction.</li>
      <li><strong>Parameters</strong>:
        <ul>
          <li><code>scrolls</code> (int): Number of scrolls (default: 3)</li>
          <li><code>frame_size</code> (int): Size of the scroll frame (default: 500)</li>
          <li><code>direction</code> (str): Scroll direction ('forward' or 'backward', default: 'forward')</li>
          <li><code>delay</code> (float): Delay between scrolls (default: 0.5)</li>
        </ul>
      </li>
      <li><strong>Returns</strong>: None</li>
       <!-- Add more details -->
    </ul>
  </li>
  <li><code>locale()</code>: Retrieves the language of the page.
    <ul>
       <li><strong>Description</strong>: Determines the language of the current page.</li>
       <li><strong>Returns</strong>: str | None: The language of the page, or None if not found.</li>
    </ul>
  </li>
  <li><code>get_url(url: str) -> bool</code>: Navigates to a URL and checks for successful navigation.
    <ul>
      <li><strong>Description</strong>: Navigates the browser to the specified URL and checks for any errors.</li>
      <li><strong>Parameters</strong>:
        <ul>
          <li><code>url</code> (str): The URL to navigate to.</li>
        </ul>
      </li>
      <li><strong>Returns</strong>: bool: True if navigation is successful, False otherwise.</li>
       <!-- Add more details -->
    </ul>
  </li>
  <li><code>extract_domain(url: str) -> str</code>: Extracts the domain name from a URL.
    <ul>
      <li><strong>Description</strong>: Extracts the domain name from the given URL string.</li>
      <li><strong>Parameters</strong>:
        <ul><li><code>url</code> (str): Input URL.</li></ul></li>
      <li><strong>Returns</strong>: str: The extracted domain name.</li>
    </ul>
  </li>
  <li><code>_save_cookies_localy(to_file: Union[str, Path])</code>: Saves cookies to a file.
      <!-- Add details as they exist in Python code -->
  </li>
  <li><code>page_refresh()</code>: Refreshes the current page.</li>
  <li><code>window_focus()</code>: Restores focus to the page.</li>
  <li><code>wait(interval: float)</code>: Waits for a specified interval.</li>
  <li><code>delete_driver_logs()</code>: Deletes temporary files and logs. </li>
  <!-- Add more methods as necessary -->
</ul>

<p><strong>Raises</strong>:</p>
<ul>
    <!-- List any exceptions raised by the methods -->
</ul>

<!-- Add more sections for classes and functions as needed -->