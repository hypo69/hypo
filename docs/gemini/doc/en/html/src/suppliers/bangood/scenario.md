html
<h1>Module: hypotez/src/suppliers/bangood/scenario.py</h1>

<h2>Overview</h2>
<p>This module handles the process of collecting product data from Bangood. It defines functions for retrieving categories and products from the supplier's website using a web driver.</p>

<h2>Constants</h2>

<h3><code>MODE</code></h3>

<p><strong>Description</strong>: Defines the operation mode of the script. Currently set to 'dev'.</p>


<h2>Functions</h2>

<h3><code>get_list_products_in_category</code></h3>

<p><strong>Description</strong>: Retrieves a list of product URLs from a given category page.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>s</code> (Supplier): The supplier object containing the web driver and locator information.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>list[str, str, None]</code>: A list of product URLs or <code>None</code> if no product URLs are found.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>None</code>: The function can return None in case of errors, or lack of locators, this should be handled in the calling code.  </li>
</ul>


<h3><code>get_list_categories_from_site</code></h3>

<p><strong>Description</strong>: Retrieves a list of categories from the supplier's website.  (Implementation is currently marked as incomplete.)</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>s</code> (Supplier): The supplier object containing the web driver and locator information.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
 <li><code>...</code>:  The return type is unspecified, indicating an incomplete implementation.  </li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
 <li><code>None</code>: The function can return None in case of errors, or lack of locators, this should be handled in the calling code.  </li>
</ul>