html
<h1>Module: hypotez/src/suppliers/aliexpress/api/helpers/products.py</h1>

<h2>Overview</h2>
<p>This module provides functions for parsing product data. It contains functions to parse individual products and collections of products.</p>

<h2>Functions</h2>

<h3><code>parse_product</code></h3>

<p><strong>Description</strong>: Parses a single product object, extracting and formatting the product small image URLs.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>product</code>: The product object to parse.  Expected to have a 'product_small_image_urls' attribute containing a `HTML.String`.
</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>product</code>: The modified product object with the small image URLs extracted and formatted as a string.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>AttributeError</code>: Raised if the input `product` object does not have a `product_small_image_urls` attribute.</li>
  <li><code>TypeError</code>: Raised if `product.product_small_image_urls` is not a `HTML.String` object.</li>

</ul>


<h3><code>parse_products</code></h3>

<p><strong>Description</strong>: Parses a list of product objects.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>products</code> (list): A list of product objects to parse.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>new_products</code> (list): A list of parsed product objects.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
 <li><code>TypeError</code>: If input `products` is not a list or if any element within the list is not a parseable product object.</li>
</ul>