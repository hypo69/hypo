html
<h1>Module: affiliated_products_generator</h1>

<h2>Overview</h2>
<p>The <code>affiliated_products_generator.py</code> file contains the <code>AliAffiliatedProducts</code> class. This class is responsible for generating complete product data from the Aliexpress Affiliate API. It builds on the <code>AliApi</code> class to process product URLs or IDs and retrieve details about affiliate products, including saving images, videos, and JSON data.</p>

<h2>Classes</h2>

<h3><code>AliAffiliatedProducts</code></h3>

<p><strong>Description</strong>: This class collects full product data from URLs or product IDs using the Aliexpress Affiliate API.</p>
<p><strong>Usage Example</strong>:</p>
<pre><code>python
prod_urls = ['123', '456', ...]
prod_urls = ['https://www.aliexpress.com/item/123.html', '456', ...]

parser = AliAffiliatedProducts(
    campaign_name,
    campaign_category,
    language,
    currency
)

products = parser._affiliate_product(prod_urls)
</code></pre>

<p><strong>Attributes</strong>:</p>
<ul>
  <li><code>campaign_name</code> (str): Name of the advertising campaign.</li>
  <li><code>campaign_category</code> (Optional[str], optional): Category for the campaign. Defaults to <code>None</code>.</li>
  <li><code>campaign_path</code> (Path): Path to the directory where campaign materials are stored.</li>
  <li><code>language</code> (str): Language for the campaign (default is 'EN').</li>
  <li><code>currency</code> (str): Currency for the campaign (default is 'USD').</li>
</ul>


<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__</code>: Initializes the <code>AliAffiliatedProducts</code> object.
    <ul>
      <li><code>campaign_name</code> (str): Name of the campaign directory.</li>
      <li><code>campaign_category</code> (Optional[str], optional): The campaign category.</li>
      <li><code>language</code> (str, optional): Campaign language (default 'EN').</li>
      <li><code>currency</code> (str, optional): Campaign currency (default 'USD').</li>
    </ul>
  </li>
    <li><code>process_affiliate_products</code>: Processes a list of product URLs to retrieve affiliate links, save images, videos and store product details.
    <ul>
      <li><code>prod_urls</code> (List[str]): List of product URLs or IDs.</li>
      <li><code>returns</code> (List[SimpleNamespace]): A list of processed products.</li>
    </ul>
  </li>
    <li><code>delete_product</code>: Removes a product that lacks an affiliate link.
    <ul>
      <li><code>product_id</code> (str): ID of the product to delete.</li>
    </ul>
  </li>
</ul>


<h2>Functions</h2>
<!-- Add function documentation here if any -->


</ul>

</html>