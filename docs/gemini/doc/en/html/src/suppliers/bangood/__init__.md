html
<h1>Module bangood</h1>

<h2>Overview</h2>
<p>This module provides functionality for interacting with the Banggood supplier, including retrieving product listings and categories.</p>

<h2>Constants</h2>

<h3><code>MODE</code></h3>

<p><strong>Description</strong>:  A string variable defining the current mode (e.g., 'dev', 'prod').</p>

<p><strong>Value</strong>: 'dev'</p>

<h2>Classes</h2>

<h3><code>Graber</code></h3>

<p><strong>Description</strong>: A class for retrieving data from the Banggood website.</p>


<p><strong>Methods</strong>:</p>
<ul>
</ul>


<h2>Functions</h2>

<h3><code>get_list_categories_from_site</code></h3>

<p><strong>Description</strong>: Retrieves a list of categories from the Banggood website.</p>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>list</code>: A list of category data.</li>
</ul>

<h3><code>get_list_products_in_category</code></h3>

<p><strong>Description</strong>: Retrieves a list of products within a specific category from the Banggood website.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>category_id</code> (str): The ID of the category.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>list</code>: A list of product data.</li>
</ul>