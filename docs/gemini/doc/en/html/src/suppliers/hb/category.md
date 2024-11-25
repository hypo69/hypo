html
<h1>hypotez/src/suppliers/hb/category.py</h1>

<h2>Overview</h2>
<p>This module handles the collection of product listings from the HB supplier's category pages using a web driver.  It implements a specific scraping logic for HB.co.il, including handling pagination and potentially updating the list of categories to reflect changes on the website.</p>

<h2>Functions</h2>

<h3><code>get_list_products_in_category</code></h3>

<p><strong>Description</strong>: Retrieves a list of product URLs from a given category page.  Handles potential pagination if necessary.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>s</code> (<code>Supplier</code>): The supplier object containing driver, locators, and scenario data.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>list[str, str, None]</code>: A list of product URLs. Returns <code>None</code> if no product links are found.  The actual structure is either a list of strings or a single string, which may need further processing.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>: Any exception that occurs during the process of fetching product URLs or handling the pagination.</li>
</ul>


<h3><code>paginator</code></h3>

<p><strong>Description</strong>: Handles pagination for product listings, checking for the next page button.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>d</code> (<code>Driver</code>): The web driver instance.</li>
  <li><code>locator</code> (<code>dict</code>): Dictionary containing locators for the pagination.</li>
  <li><code>list_products_in_category</code> (<code>list</code>): The current list of product URLs. </li>
</ul>


<p><strong>Returns</strong>:</p>
<ul>
  <li><code>bool</code>: Returns <code>True</code> if pagination is successful and additional product links are found; otherwise, returns <code>False</code>.</li>
</ul>
<p><strong>Raises</strong>:</p>
<ul>
 <li><code>Exception</code>:  Any exception during pagination.</li>
</ul>


<h3><code>get_list_categories_from_site</code></h3>

<p><strong>Description</strong>: Collects a list of active categories from the HB site.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>s</code> (<code>Supplier</code>): Supplier object.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>list</code>: List of category information.  Specific return type depends on how the information is extracted.</li>
</ul>
<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>: Any exception encountered during the category retrieval process.</li>
</ul>