html
<h1>Module: hypotez/src/suppliers/grandadvance/graber.py</h1>

<h2>Overview</h2>
<p>This module defines the <code>Graber</code> class for capturing product fields from the Grandadvance supplier. It utilizes asynchronous operations and interacts with a web driver for data extraction.</p>

<h2>Classes</h2>

<h3><code>Graber</code></h3>

<p><strong>Description</strong>: A class for grabbing product fields from the Morlevi supplier.</p>

<p><strong>Attributes</strong>:</p>
<ul>
  <li><code>supplier_prefix</code> (str): The prefix identifying the supplier.</li>
</ul>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__(self, driver: Driver)</code>:
    <p><strong>Description</strong>: Initializes the Graber class with a driver instance.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>driver</code> (Driver): The WebDriver instance for interacting with the browser.</li>
    </ul>
  </li>
  <li><code>grab_page(self, driver: Driver) -> ProductFields</code>:
    <p><strong>Description</strong>: Asynchronous function to grab product fields.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>driver</code> (Driver): The driver instance to use for grabbing.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>ProductFields</code>: The grabbed product fields.</li>
    </ul>
  </li>
  <li><code>local_saved_image(self, value: Any = None)</code>:
    <p><strong>Description</strong>: Fetches and saves the product's default image locally.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>value</code> (Any, optional):  Value to be saved; if provided, it's used instead of fetching a new image from the website.</li>
    </ul>
    <p><strong>Raises</strong>:</p>
    <ul>
      <li><code>Exception</code>: Error during image retrieval or saving.</li>
    </ul>
  </li>
    <!-- Add other methods as needed -->
</ul>


<h2>Functions</h2>
<!-- Add functions if any.  They were not present in the provided code snippet -->


<!-- Add other sections if needed (e.g., Constants, Global Variables) -->
<!--Example of adding a section for constants-->
<h2>Global Variables</h2>
<h3>MODE</h3>

<p><strong>Description</strong>: Global variable to define the operational mode (e.g., 'dev').</p>

<!-- Add other sections for other global variables if necessary -->