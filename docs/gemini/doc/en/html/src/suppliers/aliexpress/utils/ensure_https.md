html
<h1>ensure_https Module</h1>

<h2>Overview</h2>
<p>This module provides a function to ensure that a URL string (or a list of strings) starts with "https://". If the input is a product ID, it constructs a full URL with the "https://" prefix and the `aliexpress.com` domain. It also handles cases where the input already has the correct format.</p>

<h2>Functions</h2>

<h3><code>ensure_https</code></h3>

<p><strong>Description</strong>: Ensures that the provided URL string(s) contain the https:// prefix. If the input is a product ID, it constructs a full URL with https:// prefix.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>prod_ids</code> (str | list[str]): A URL string or a list of URL strings to check and modify if necessary.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>str | list[str]</code>: The URL string or list of URL strings with the https:// prefix.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>ValueError</code>: If <code>prod_ids</code> is an instance of <code>WindowsPath</code>.</li>
</ul>

<p><strong>Examples</strong>:</p>
<pre><code>python
>>> ensure_https("example_product_id")
'https://www.aliexpress.com/item/example_product_id.html'

>>> ensure_https(["example_product_id1", "https://www.aliexpress.com/item/example_product_id2.html"])
['https://www.aliexpress.com/item/example_product_id1.html', 'https://www.aliexpress.com/item/example_product_id2.html']

>>> ensure_https("https://www.example.com/item/example_product_id")
'https://www.example.com/item/example_product_id'
</code></pre>


<h3><code>ensure_https_single</code></h3>

<p><strong>Description</strong>: Ensures a single URL or product ID string has the https:// prefix.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>prod_id</code> (str): The URL or product ID string.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>str</code>: The URL string with the https:// prefix.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>ValueError</code>: If <code>prod_id</code> is an instance of <code>WindowsPath</code>.</li>
</ul>

<p><strong>Examples</strong>:</p>
<pre><code>python
>>> ensure_https_single("example_product_id")
'https://www.aliexpress.com/item/example_product_id.html'

>>> ensure_https_single("https://www.example.com/item/example_product_id")
'https://www.example.com/item/example_product_id'
</code></pre>


<p><strong>Note</strong>: The documentation for <code>ensure_https_single</code> contains placeholder content because the original code has an incomplete function definition for it.  The ellipsis (...) in the original Python code indicates missing implementation details.  The provided example uses <code>extract_prod_ids</code> which is assumed to be defined elsewhere.</p>

<h2>Modules Used</h2>

<ul>
    <li><code>src.logger</code>: Used for logging messages.</li>
    <li><code>.extract_product_id</code>: Used for extracting product IDs from URLs or product IDs.</li>
</ul>