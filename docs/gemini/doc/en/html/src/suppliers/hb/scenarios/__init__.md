html
<h1>Module: src.suppliers.hb.scenarios</h1>

<h2>Overview</h2>
<p>This module contains functions and classes for interacting with the <code>hb.co.il</code> supplier, including product retrieval, category handling, and login.</p>

<h2>Constants</h2>

<h3><code>MODE</code></h3>

<p><strong>Description</strong>: A constant representing the current mode (e.g., development or production).  Currently set to 'dev'.</p>

<h2>Functions</h2>

<h3><code>get_list_products_in_category</code></h3>

<p><strong>Description</strong>: Retrieves a list of products within a specified category.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li>N/A (function parameters not specified in the input)</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>list</code>: A list of products.</li>
</ul>


<h3><code>get_list_categories_from_site</code></h3>

<p><strong>Description</strong>: Retrieves a list of categories from the supplier's website.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li>N/A (function parameters not specified in the input)</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>list</code>: A list of categories.</li>
</ul>


<h3><code>grab_product_page</code></h3>

<p><strong>Description</strong>: Retrieves the HTML content of a specific product page.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li>N/A (function parameters not specified in the input)</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>str</code>: The HTML content of the product page.</li>
</ul>


<h3><code>login</code></h3>

<p><strong>Description</strong>: Logs into the supplier's website.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li>N/A (function parameters not specified in the input)</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>bool</code>: True if login is successful, False otherwise.</li>
</ul>


<h2>Classes</h2>
<p>N/A (No classes defined in the provided code)</p>



<h2>Imports</h2>
<p><code>from packaging.version import Version</code></p>
<p><code>from .version import __version__, __doc__, __details__</code></p>
<p><code>from .categories import get_list_products_in_category, get_list_categories_from_site</code></p>
<p><code>from .grabber import grab_product_page</code></p>
<p><code>from .login import login</code></p>