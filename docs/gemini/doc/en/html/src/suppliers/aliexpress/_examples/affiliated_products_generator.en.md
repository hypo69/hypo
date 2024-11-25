html
<h1>`affiliated_products_generator.en.html`</h1>

<h2>Overview</h2>
<p>This module provides functionality for generating affiliate links and saving associated images and videos for products sourced from AliExpress. It utilizes the `AliAffiliatedProducts` class for handling product data retrieval, processing, and saving.</p>

<h2>Classes</h2>

<h3><code>AliAffiliatedProducts</code></h3>

<p><strong>Description</strong>: This class is responsible for fetching product data from AliExpress, generating affiliate links, and saving associated images and videos.</p>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>process_affiliate_products(prod_urls: list[str]) -> list[Product] | None</code>
    <p><strong>Description</strong>: Fetches product data, generates affiliate links, and saves images and videos for a list of product URLs or IDs.  Returns a list of processed `Product` objects, or `None` if there are errors or no products found.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>prod_urls</code> (list[str]): A list of product URLs or IDs to process.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>list[Product] | None</code>: A list of `Product` objects with affiliate links and saved images/videos, or `None` if there are errors.</li>
    </ul>
    <p><strong>Raises</strong>:</p>
    <ul>
      <li><code>AliExpressAPIError</code>:  Raised if there are issues communicating with the AliExpress API.</li>
      <li><code>InvalidProductURL</code>:  Raised if a provided product URL or ID is invalid or cannot be processed.</li>
      <li><code>IOError</code>:  Raised if there are issues saving images or videos to the local file system.</li>
      <li><code>UnexpectedResponseError</code>: Raised if the API returns an unexpected response format.</li>
    </ul>
  </li>
</ul>


<h2>Functions</h2>

<h3><code>main</code></h3>

<p><strong>Description</strong>:  Demonstrates the usage of the `AliAffiliatedProducts` class. Sets up campaign parameters, creates an instance, processes a list of product URLs or IDs, and prints the resulting affiliate products.</p>
<p><strong>Parameters</strong>:</p>
<ul>
  <li>None</li>
</ul>
<p><strong>Returns</strong>:</p>
<ul>
  <li>None (Prints results to console)</li>
</ul>
<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>: Any exception raised within the `main` function will be caught.</li>
</ul>

<h2>Example Usage (from example_usage.py)</h2>
<p>See the provided example code demonstrating how to use `AliAffiliatedProducts` and `main` to generate affiliate links, fetch images, and process data.</p>


```html