html
<h1>aliexpress API</h1>

<h2>Overview</h2>
<p>This module provides a wrapper for the AliExpress API, allowing interaction with various AliExpress resources. It includes a main API class and a models module for data representations.</p>

<h2>Modules</h2>
<ul>
  <li><a href="#aliexpressapi">AliexpressApi</a></li>
  <li><a href="#models">models</a></li>
</ul>

<h2>Classes</h2>
<h3 id="aliexpressapi"><code>AliexpressApi</code></h3>

<p><strong>Description</strong>: This class provides the main interface for interacting with the AliExpress API.</p>

<p><strong>Methods</strong>:</p>
<ul>
<li><a href="#AliexpressApi.get_product_details">get_product_details</a></li>
</ul>



<h3 id="models"><code>models</code></h3>

<p><strong>Description</strong>:  This module contains models for data representation used by the AliExpress API.</p>



<h2>Functions</h2>
<p>This module does not contain any functions.</p>


<h3 id="AliexpressApi.get_product_details"><code>AliexpressApi.get_product_details</code></h3>

<p><strong>Description</strong>: Retrieves detailed information about a product on AliExpress.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>product_id</code> (str): The unique identifier of the product.</li>
  <li><code>country_code</code> (Optional[str], optional): The country code to use for location-based product information (e.g., 'US'). Defaults to None.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>dict | None</code>: A dictionary containing product details or <code>None</code> if an error occurs.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>APIError</code>: An error occurred while communicating with the API.</li>
  <li><code>ValueError</code>: Invalid input parameters.</li>
</ul>