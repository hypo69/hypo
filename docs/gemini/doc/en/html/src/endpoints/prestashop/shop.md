html
<h1>Module: hypotez/src/endpoints/prestashop/shop.py</h1>

<h2>Overview</h2>
<p>This module provides a class for interacting with PrestaShop stores. It inherits from the <code>PrestaShop</code> class, offering methods for various store operations.</p>

<h2>Classes</h2>

<h3><code>PrestaShopShop</code></h3>

<p><strong>Description</strong>: A class for working with PrestaShop stores. It inherits from the <code>PrestaShop</code> class, providing methods for interacting with the store's API.</p>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__</code>: Initializes a PrestaShopShop object.</li>
</ul>


<h2>Functions</h2>

(No functions found in the provided code snippet)

<h2>Attributes</h2>
<ul>
  <li><code>MODE</code>: (str): Stores the mode of operation for the module.  The current value is 'dev'.</li>
</ul>

<h3><code>__init__</code></h3>

<p><strong>Description</strong>: Initializes a PrestaShopShop object.  This method sets up the connection to the PrestaShop API using the provided credentials.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>credentials</code> (Optional[dict | SimpleNamespace], optional): A dictionary or SimpleNamespace object containing the API domain and key. Defaults to <code>None</code>.</li>
  <li><code>api_domain</code> (Optional[str], optional): The PrestaShop API domain. Defaults to <code>None</code>.</li>
  <li><code>api_key</code> (Optional[str], optional): The PrestaShop API key. Defaults to <code>None</code>.</li>
  <li><code>*args</code>: Additional positional arguments (not documented).</li>
  <li><code>**kwards</code>: Additional keyword arguments (not documented).</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>ValueError</code>: If both <code>api_domain</code> and <code>api_key</code> are not provided.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li>None: The method initializes the object; no explicit return value.</li>
</ul>

<p><strong>Note</strong>: If the <code>credentials</code> argument is provided, it overrides any values set for <code>api_domain</code> or <code>api_key</code>. If <code>credentials</code> is provided, the values in <code>credentials</code> will be used.  If neither <code>credentials</code> or <code>api_domain/api_key</code> is provided, a ValueError will be raised. </p>