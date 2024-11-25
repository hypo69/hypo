html
<h1>Module: extract_product_id</h1>

<h2>Overview</h2>
<p>This module provides a function for extracting product IDs from URLs or a list of URLs.  It also handles the case when product IDs are provided directly as strings.</p>

<h2>Functions</h2>

<h3><code>extract_prod_ids</code></h3>

<p><strong>Description</strong>: Extracts item IDs from a list of URLs or directly returns IDs if given.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>urls</code> (str | list[str]): A URL, a list of URLs, or product IDs.
  </li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>str | list[str] | None</code>: A list of extracted item IDs, a single ID, or <code>None</code> if no valid ID is found.
  </li>
</ul>

<p><strong>Examples</strong>:</p>
<pre><code class="language-python">
>>> extract_prod_ids("https://www.aliexpress.com/item/123456.html")
'123456'

>>> extract_prod_ids(["https://www.aliexpress.com/item/123456.html", "7891011.html"])
['123456', '7891011']

>>> extract_prod_ids(["https://www.example.com/item/123456.html", "https://www.example.com/item/abcdef.html"])
['123456']

>>> extract_prod_ids("7891011")
'7891011'

>>> extract_prod_ids("https://www.example.com/item/abcdef.html")
None
</code></pre>

<h3><code>extract_id</code></h3>

<p><strong>Description</strong>: Extracts a product ID from a given URL or validates a product ID.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>url</code> (str): The URL or product ID.
  </li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>str | None</code>: The extracted product ID or the input itself if it's a valid ID, or <code>None</code> if no valid ID is found.
  </li>
</ul>

<p><strong>Examples</strong>:</p>
<pre><code class="language-python">
>>> extract_id("https://www.aliexpress.com/item/123456.html")
'123456'

>>> extract_id("7891011")
'7891011'

>>> extract_id("https://www.example.com/item/abcdef.html")
None
</code></pre>