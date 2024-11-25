html
<h1>Module: hypotez/src/suppliers/ivory/__morlevi__.py</h1>

<h2>Overview</h2>
<p>This module contains functions for interacting with the Morlevi website, specifically for product acquisition. It includes functions for login, product scraping, and pagination through product listings.</p>

<h2>Classes</h2>

<h3><code>Product</code></h3>

<p><strong>Description</strong>:  This class likely represents a product from the Morlevi site.  The provided code snippet doesn't show the full class definition, so the description is inferred based on the functions that use it.</p>

<p><strong>Methods</strong>:</p>
<ul>
<li><code>__init__</code> (likely): Initializes a Product object.  Accepts a supplier object as an argument.</li>
</ul>


<h2>Functions</h2>

<h3><code>login</code></h3>

<p><strong>Description</strong>: Attempts to log in to the Morlevi website.  Handles potential pop-ups and errors during the login process.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>supplier</code> (object): An object representing the supplier (likely containing driver, locators, etc.).</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>bool</code>: True if login is successful, False if not, and None if the login attempts failed completely.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>: Any exception during the login process.</li>
</ul>


<h3><code>_login</code></h3>

<p><strong>Description</strong>: Internal function responsible for the actual login procedure. Executes actions required to log into Morlevi system.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>_s</code> (object): An object representing the supplier (likely containing driver, locators, etc.).</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>bool</code>: True if login is successful; False otherwise.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>: Any exception during the login process.</li>
</ul>


<h3><code>grab_product_page</code></h3>

<p><strong>Description</strong>: Fetches product details from the Morlevi website.  This function appears to collect various product attributes like SKU, title, price, description, images, etc., from the product page.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>s</code> (object): An object representing the supplier (likely containing driver, locators, etc.).</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Product</code>: A Product object populated with the gathered product data.  Returns None if fetching fails.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>: Any exception during the data retrieval process.</li>
</ul>



<h3><code>list_products_in_category_from_pagination</code></h3>

<p><strong>Description</strong>: Retrieves a list of product URLs from a specified category on the Morlevi website, handling pagination.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>supplier</code> (object): An object containing driver and locators for website interaction.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>list</code>: A list of product URLs or an empty list if no products are found or there's an error.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>: Any exception during the process.</li>
</ul>

<h3><code>get_list_products_in_category</code></h3>

<p><strong>Description</strong>: Retrieves a list of product URLs from a category, potentially utilizing pagination for full result set. It handles different data formats and errors during fetching. More information on the parameters will be needed to complete the description.</p>


<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>s</code> (object): Supplier object.</li>
  <li><code>scenario</code> (JSON): Scenario data.</li>
  <li><code>presath</code> (object): PrestaShop Web Service data.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>list</code>: List of products.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
<li><code>Exception</code>: Generic exception in case of error.</li>
</ul>

<h3><code>get_list_categories_from_site</code></h3>

<p><strong>Description</strong>: Retrieves a list of categories from a website.  More details about the parameters are necessary for a complete description.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>s</code> (object): Supplier object.</li>
  <li><code>scenario_file</code> (str): File path to the scenario file.</li>
  <li><code>brand</code> (str): Brand filter (optional).</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li>(inferred) <code>list</code>:  List of categories.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
<li>(inferred) <code>Exception</code>: Any exception during the process.</li>
</ul>