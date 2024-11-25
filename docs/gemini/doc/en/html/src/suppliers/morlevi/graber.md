html
<h1>Module hypotez/src/suppliers/morlevi/graber.py</h1>

<h2>Overview</h2>
<p>This module defines the <code>Graber</code> class for grabbing product fields from the Morlevi supplier webpage. It utilizes asynchronous operations and handles potential exceptions during execution.</p>

<h2>Classes</h2>

<h3><code>Graber</code></h3>

<p><strong>Description</strong>: A class for capturing product fields from the Morlevi supplier. It inherits from the <code>Grbr</code> class and provides methods for retrieving product data.  It initializes the <code>supplier_prefix</code> and sets the locator for closing pop-up windows.</p>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__</code>: Initializes the Graber object, setting the supplier prefix and driver.</li>
  <li><code>grab_page</code>: Asynchronous function for grabbing product fields. Fetches data using internal functions. Returns a <code>ProductFields</code> object containing the extracted data.</li>
  <li><code>local_saved_image</code>: Fetches the default product image from the webpage and saves it locally.  Handles potential errors during image retrieval and saving.</li>
   <li><code>fetch_all_data</code>:  (Internal) Function to fetch a multitude of data points. Note: the commented out invocations of functions (`await self.x...`) represent potential calls to fetch additional data, but are currently not implemented in the provided code.</li>
</ul>


<h2>Functions</h2>

<!-- (No functions defined in the provided code fragment) -->


<!-- (No exceptions or raises clauses documented) -->


<!-- (No constants documented) -->