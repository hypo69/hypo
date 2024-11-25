html
<h1>Module: via_webdriver</h1>

<h2>Overview</h2>
<p>This module provides functions for parsing KualaStyle product data via a webdriver.</p>

<h2>Functions</h2>

<h3><code>get_list_products_in_category</code></h3>

<p><strong>Description</strong>: Returns a list of product URLs from a category page.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>s</code> (Suplier): The supplier object containing the webdriver session.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>list[str, str, None]</code>: A list of product URLs, or <code>None</code> if no product URLs are found or an error occurs.  Note: The return type `list[str, str, None]` seems unusual. Consider a more appropriate return type (e.g., list[tuple[str,str]]) or even a dataclass if needed.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>AttributeError</code>: If the `driver`, `locators`, or `product_links` attribute of the `s` object is not found, or if any part of the webdriver interaction fails. This is a placeholder; more specific exceptions may be raised in the actual implementation. Please specify the appropriate exceptions.</li>
</ul>

<p><strong>Example Usage</strong> (Illustrative):</p>
<pre><code class="language-python">
supplier_instance = Suplier(...) # Replace with your supplier object
product_links = get_list_products_in_category(supplier_instance)
if product_links:
  for link in product_links:
    # Process each product link
    print(link)
else:
  print("No product links found or an error occurred.")

</code></pre>


<!-- Add other functions, classes, or sections as necessary -->