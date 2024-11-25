html
<h1>Module: hypotez/src/endpoints/prestashop/product.py</h1>

<h2>Overview</h2>
<p>This module provides functionality for interacting with PrestaShop products via its API. It defines a class <code>PrestaProduct</code> inheriting from <code>PrestaShop</code>, offering methods for checking product existence, searching, and retrieving product details.</p>

<h2>Classes</h2>

<h3><code>PrestaProduct</code></h3>

<p><strong>Description</strong>: Represents a PrestaShop product and interacts with the API directly.</p>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>check(product_reference: str) -> dict | bool</code>: Checks if a product exists in the database based on its product reference (SKU, MKT). Returns the product details as a dictionary if found, otherwise returns <code>False</code>.</li>
  <li><code>search(filter: str, value: str) -> list | None</code>: Performs an advanced search in the database based on filters. Returns a list of matching products or <code>None</code> if no results are found.</li>
  <li><code>get(id_product) -> dict | None</code>: Retrieves product information based on its ID. Returns the product details as a dictionary, or <code>None</code> if the product is not found.</li>
</ul>

<h3><code>__init__</code></h3>

<p><strong>Description</strong>: Initializes a <code>PrestaProduct</code> object.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>credentials (Optional[dict | SimpleNamespace], optional):</code> A dictionary or SimpleNamespace object containing 'api_domain' and 'api_key' parameters. Defaults to <code>None</code>.</li>
  <li><code>api_domain (Optional[str], optional):</code> The API domain. Defaults to <code>None</code>.</li>
  <li><code>api_key (Optional[str], optional):</code> The API key. Defaults to <code>None</code>.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>ValueError</code>: Raised if both <code>api_domain</code> and <code>api_key</code> are not provided.</li>
</ul>

<p><strong>Notes</strong>: If <code>credentials</code> is provided, it overrides any other `api_domain` or `api_key` arguments.  The initialization will use the provided values or raise a ValueError if not both the api_domain and the api_key are set.</p>


<h2>Functions</h2>

<p>(None in this module)</p>