html
<h1>Module pricelist</h1>

<h2>Overview</h2>
<p>This module defines the <code>PriceListRequester</code> class for requesting and modifying product prices from a PrestaShop API.</p>

<h2>Classes</h2>

<h3><code>PriceListRequester</code></h3>

<p><strong>Description</strong>: A class for requesting a list of prices from a PrestaShop API. Inherits from <code>PrestaShop</code>.</p>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__</code>: Initializes the <code>PriceListRequester</code> object.</li>
  <li><code>request_prices</code>: Requests a list of prices for specified products.</li>
  <li><code>update_source</code>: Updates the data source for price requests.</li>
  <li><code>modify_product_price</code>: Modifies the price of a specific product.</li>
</ul>

<h3><code>PrestaShop</code></h3>
<p><strong>Description</strong>:  (Presumed base class, as it is referenced in the code but not defined here).  This class is used as a base for handling PrestaShop API interactions.</p>



<h2>Functions</h2>

<!-- No functions defined in this file -->


<h2>Method Details</h2>

<h3><code>PriceListRequester.__init__</code></h3>

<p><strong>Description</strong>: Initializes the <code>PriceListRequester</code> object.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>api_credentials</code> (dict): A dictionary containing API credentials, including 'api_domain' and 'api_key'.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <!--No potential exception handling in the provided method-->
</ul>


<h3><code>PriceListRequester.request_prices</code></h3>

<p><strong>Description</strong>: Requests a list of prices for specified products.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>products</code> (list): A list of product names for which to retrieve prices.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>dict | None</code>: A dictionary where keys are product names and values are their prices. Returns <code>None</code> if an error occurs during the request. Example: {'product1': 10.99, 'product2': 5.99}.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <!--No potential exception handling in the provided method-->
</ul>


<h3><code>PriceListRequester.update_source</code></h3>

<p><strong>Description</strong>: Updates the data source for price requests.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>new_source</code>: The new data source.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <!--No potential exception handling in the provided method-->
</ul>


<h3><code>PriceListRequester.modify_product_price</code></h3>

<p><strong>Description</strong>: Modifies the price of a specific product.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>product</code> (str): The name of the product.</li>
  <li><code>new_price</code>: The new price for the product.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <!--No potential exception handling in the provided method-->
</ul>