html
<h1>Module src.suppliers.visualdg.graber</h1>

<h2>Overview</h2>
<p>This module defines the <code>Graber</code> class for grabbing product fields from the VisualDG supplier. It utilizes asynchronous operations and integrates with the broader PrestaShop product fetching pipeline.</p>

<h2>Classes</h2>

<h3><code>Graber</code></h3>

<p><strong>Description</strong>: This class handles the process of grabbing product fields from the Morlevi product supplier.  It inherits from the base <code>Grbr</code> class and manages the supplier-specific logic.</p>

<p><strong>Attributes</strong>:</p>
<ul>
  <li><code>supplier_prefix</code> (str): A string identifying the supplier ("visualdg").</li>
</ul>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__</code>(driver: Driver):
    <p><strong>Description</strong>: Initializes the Graber instance, setting the supplier prefix and initializing the base class. Also sets the `Context.locator` to None.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>driver</code> (Driver): The WebDriver instance.</li>
    </ul>
  </li>
  <li><code>grab_page</code>(driver: Driver) -> ProductFields:
    <p><strong>Description</strong>: Asynchronously grabs product fields from the page. It calls multiple helper methods to fetch various product details.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>driver</code> (Driver): The driver instance for interacting with the page.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>ProductFields</code>: A data structure containing the retrieved product fields.</li>
    </ul>
     <p><strong>Inner Function (fetch_all_data)</strong>:
        <p>This function calls several other asynchronous methods to fetch product data.  It's structured to dynamically fetch specific data fields based on provided keyword arguments.</p>
    </ul>
     </li>
  
</ul>


<h2>Functions</h2>


<!-- The following functions are stubs because the provided code snippet doesn't provide docstrings for them. -->
<h3><code>fetch_all_data</code></h3>

<p><strong>Description</strong>: Placeholder for a function that fetches all the data fields from the web page using the other helper functions.</p>
<p><strong>Parameters</strong>: N/A</p>
<p><strong>Returns</strong>: N/A</p>


<!-- Other functions (id_product, additional_shipping_cost, etc.) -->
<!-- ... (repeat the structure for other functions, replacing with actual docstrings from the code) ... -->


<h2>Global Variables</h2>

<h3><code>MODE</code></h3>
<p><strong>Description</strong>:  Stores the mode of operation, likely "dev" for development.</p>


<!-- Include documentation for other global variables and imports if available -->


</ul>