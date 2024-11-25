html
<h1>Module: hypotez/src/suppliers/gearbest/graber.py</h1>

<h2>Overview</h2>
<p>This module defines the <code>Graber</code> class, a subclass of <code>Grbr</code> for grabbing product fields from GearBest. It uses asynchronous operations and handles various product details, including but not limited to product information, images, and specifications.</p>

<h2>Classes</h2>

<h3><code>Graber</code></h3>

<p><strong>Description</strong>: This class is responsible for grabbing product fields from the GearBest supplier. It inherits from the <code>Grbr</code> base class and initializes with the <code>supplier_prefix</code> and a <code>driver</code> instance.</p>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__</code>(driver: Driver):
    <p><strong>Description</strong>: Initializes the <code>Graber</code> object with a given driver instance and sets the <code>supplier_prefix</code>.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>driver</code> (Driver): The webdriver instance used for interacting with the website.</li>
    </ul>
  </li>
  <li><code>grab_page</code>(driver: Driver) -> ProductFields:
    <p><strong>Description</strong>: An asynchronous function to grab product fields from the GearBest website.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>driver</code> (Driver): The driver instance to use for the web interactions.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>ProductFields</code>: The grabbed product fields.</li>
    </ul>
    <p><strong>Raises</strong>:</p>
    <ul>
      <li><code>ExecuteLocatorException</code>: If an error occurs during locator execution.</li>
        <!-- Add other potential exception types -->
    </ul>
</li>
</ul>


<h2>Functions</h2>
<!-- No functions defined in the provided code. -->

<!-- Add any functions if present -->


</ul>

<hr>
<p><strong>Note:</strong>  The provided code snippet contains numerous calls to functions (e.g., <code>self.id_product</code>, <code>self.description_short</code>) that are not defined within the module itself.  To generate complete documentation, the definitions of these functions would need to be included. Additionally, the comment format of """" """"  is not consistent. Please fix those inconsistencies as well. </p>