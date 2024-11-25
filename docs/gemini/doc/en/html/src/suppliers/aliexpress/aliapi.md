html
<h1>Module aliapi</h1>

<h2>Overview</h2>
<p>This module provides an API class for interacting with AliExpress, specifically for retrieving product details and affiliate links. It extends the base <code>AliexpressApi</code> class and includes database interaction capabilities.</p>

<h2>Classes</h2>

<h3><code>AliApi</code></h3>

<p><strong>Description</strong>: Custom API class for AliExpress operations, extending <code>AliexpressApi</code>.</p>

<p><strong>Attributes</strong>:</p>
<ul>
  <li><code>manager_categories</code> (<code>CategoryManager</code>): Database manager for AliExpress categories.  (Initialized to <code>None</code>)</li>
  <li><code>manager_campaigns</code> (<code>ProductCampaignsManager</code>): Database manager for product campaigns and sales. (Initialized to <code>None</code>)</li>
</ul>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__</code>
    <p><strong>Description</strong>: Initializes an instance of the <code>AliApi</code> class.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>language</code> (str, optional): The language to use for API requests. Defaults to 'en'.</li>
      <li><code>currency</code> (str, optional): The currency to use for API requests. Defaults to 'usd'.</li>
    </ul>
    <p><strong>Raises</strong>:</p>
    <ul>
        <li>No explicit exceptions listed in the docstring.</li>
    </ul>
  </li>
  <li><code>retrieve_product_details_as_dict</code>
    <p><strong>Description</strong>: Sends a list of product IDs to AliExpress and retrieves a list of product descriptions as dictionaries.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>product_ids</code> (list): List of product IDs.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>dict | dict | None</code>: List of product data as dictionaries. Returns a dictionary or `None`.</li>
    </ul>
    <p><strong>Raises</strong>:</p>
      <ul>
        <li>No explicit exceptions listed in the docstring.</li>
      </ul>
      <p><strong>Example Usage (as shown in the docstring)</strong>:</p>
        <pre><code>python
namespace_list = [
    SimpleNamespace(a=1, b=2, c=3),
    SimpleNamespace(d=4, e=5, f=6),
    SimpleNamespace(g=7, h=8, i=9)
]

dict_list = [vars(ns) for ns in namespace_list]
print(dict_list)
</code></pre>
  </li>
  <li><code>get_affiliate_links</code>
    <p><strong>Description</strong>: Retrieves affiliate links for specified products.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>links</code> (str | list): Product links to process.</li>
      <li><code>link_type</code> (int, optional): Type of affiliate link. Defaults to 0.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>List[SimpleNamespace]</code>: List of SimpleNamespace objects containing affiliate links.</li>
    </ul>
    <p><strong>Raises</strong>:</p>
    <ul>
      <li>No explicit exceptions listed in the docstring.</li>
    </ul>
    
  </li>

</ul>

<h2>Functions</h2>
<p> (No functions are defined in this module other than class methods)</p>

<h2>Modules Used</h2>
<ul>
<li><code>re</code></li>
<li><code>json</code></li>
<li><code>asyncio</code></li>
<li><code>pathlib</code></li>
<li><code>typing</code></li>
<li><code>types</code></li>
<li><code>requests</code></li>
<li><code>src.gs</code></li>
<li><code>src.utils</code></li>
<li><code>src.logger</code></li>
<li><code>.api</code></li>
<li><code>src.db.manager_categories</code></li>
<li><code>src.db.manager_coupons_and_sales</code></li>

</ul>