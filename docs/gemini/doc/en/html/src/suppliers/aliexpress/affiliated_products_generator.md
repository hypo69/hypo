html
<h1>Module: hypotez/src/suppliers/aliexpress/affiliated_products_generator.py</h1>

<h2>Overview</h2>
<p>This module defines the <code>AliAffiliatedProducts</code> class for collecting product data from AliExpress, including affiliate links and image/video downloads.  It handles the process of fetching product details, generating affiliate links, downloading associated images and videos, and saving the results in a structured format.</p>

<h2>Classes</h2>

<h3><code>AliAffiliatedProducts</code></h3>

<p><strong>Description</strong>: A subclass of <code>AliApi</code> designed to collect full product data, including affiliate links and saved images for a given list of product IDs or URLs.</p>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__</code>:
    <p><strong>Description</strong>: Initializes the <code>AliAffiliatedProducts</code> class.  It takes language and currency as parameters, initializing the superclass <code>AliApi</code> with these details. It also validates the provided language and currency arguments, logging a critical message if either is missing.</p>

    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>language</code> (str | dict, optional): Language for the campaign (default 'EN').</li>
      <li><code>currency</code> (str, optional): Currency for the campaign (default 'USD').</li>
    </ul>

  </li>
  <li><code>process_affiliate_products</code>:
    <p><strong>Description</strong>: Processes a list of product IDs or URLs and returns a list of products with affiliate links and saved images.  It fetches affiliate links, retrieves product details, downloads images and videos (if available), saves the data, and returns a list of processed product objects.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>prod_ids</code> (list[str]): List of product URLs or IDs.</li>
      <li><code>category_root</code> (Path | str): The directory where the data will be saved.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>list[SimpleNamespace]</code>: A list of processed products with affiliate links and saved images.</li>
    </ul>
    <p><strong>Raises</strong>:</p>
    <ul>
      <li><code>Exception</code>: If the category name is not found in the campaign or if no affiliate links are found.</li>
    </ul>
  </li>
</ul>


<h2>Functions</h2>
<p>(None defined in the provided code)</p>