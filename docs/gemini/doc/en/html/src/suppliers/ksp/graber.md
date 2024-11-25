html
<h1>Module src.suppliers.ksp.graber</h1>

<h2>Overview</h2>
<p>This module defines the <code>Graber</code> class for grabbing product fields from a KSP supplier. It utilizes asynchronous operations and incorporates a decorator for closing pop-up windows.</p>

<h2>Classes</h2>

<h3><code>Graber</code></h3>

<p><strong>Description</strong>: A class for gathering Morlevi product information.  It extends the base <code>Graber</code> class and handles the KSP specific product data retrieval.</p>

<p><strong>Attributes</strong>:</p>
<ul>
  <li><code>supplier_prefix</code> (str): The prefix for the supplier (e.g., 'ksp').</li>
</ul>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__</code>(driver: Driver):
    <p><strong>Description</strong>: Initializes the Graber instance. Sets the supplier prefix, extends the base Graber class, and potentially sets the global context's locator.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>driver</code> (Driver): The webdriver instance used for interactions.</li>
    </ul>
  </li>
  <li><code>grab_page</code>(driver: Driver) -> ProductFields:
    <p><strong>Description</strong>: Asynchronously retrieves product fields. Grabs data through a series of individual functions. </p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>driver</code> (Driver): The driver instance to use for grabbing.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>ProductFields</code>: The retrieved product data.</li>
    </ul>
  </li>
</ul>

<h2>Functions</h2>


<!--  The following functions are commented out/stubbed in the code.  
      Include documentation for them if they are actually used. -->


<h2>Global Variables</h2>
<ul>
<li><code>MODE</code> (str):  Value is 'dev'.</li>
<li><code>d</code> (Driver): A global driver object.  (Note: Global variables should be avoided whenever possible; this is a placeholder.)</li>
</ul>



<!--  Include documentation for any other classes or functions if they exist. -->