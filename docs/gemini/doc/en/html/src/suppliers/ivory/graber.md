html
<h1>Module: hypotez/src/suppliers/ivory/graber.py</h1>

<h2>Overview</h2>
<p>This module defines the <code>Graber</code> class, which is a subclass of the <code>Grbr</code> class from the <code>src.suppliers</code> module. This class handles the process of grabbing product fields from the Ivory supplier. It utilizes asynchronous operations and includes methods for extracting various product details.</p>

<h2>Classes</h2>

<h3><code>Graber</code></h3>

<p><strong>Description</strong>: This class is responsible for retrieving product fields from the Ivory supplier. It extends the functionality of the base <code>Grbr</code> class.</p>

<p><strong>Attributes</strong>:</p>
<ul>
  <li><code>supplier_prefix</code> (str): The prefix identifier for the Ivory supplier.</li>
</ul>


<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__</code>(driver: Driver):
    <p><strong>Description</strong>: Initializes the <code>Graber</code> object.  It sets the supplier prefix and calls the parent class's constructor, passing the supplier prefix and driver object.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>driver</code> (Driver): The driver instance to use for interactions.</li>
    </ul>
    </li>
    <li><code>grab_page</code>(driver: Driver) -> ProductFields:
    <p><strong>Description</strong>: An asynchronous function to gather product fields.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>driver</code> (Driver): The driver instance to use for web interactions.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>ProductFields</code>: A data structure containing the fetched product information.</li>
    </ul>
  </li>
</ul>


<h2>Functions</h2>

<!-- Function definitions (fetch_all_data, id_product, etc) and their details are omitted due to significant length and repetitive structure. -->


<p><strong>Note</strong>:  The code includes numerous placeholder functions (e.g., <code>id_product</code>) that are likely to have more detailed documentation in the actual implementation.  The detailed parameter descriptions, return values, and potential exceptions should be included in the documentation for each of these functions using the specified format.</p>


```