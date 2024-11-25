html
<h1>Module: hypotez/src/endpoints/prestashop/supplier.py</h1>

<h2>Overview</h2>
<p>This module defines the <code>PrestaSupplier</code> class for interacting with PrestaShop suppliers. It inherits from the <code>PrestaShop</code> class and provides methods for various supplier-related operations.</p>

<h2>Classes</h2>

<h3><code>PrestaSupplier</code></h3>

<p><strong>Description</strong>: A class for working with PrestaShop suppliers.</p>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__</code>: Initializes a PrestaSupplier object.</li>
</ul>

<p><strong>Inherits from</strong>: <code>PrestaShop</code></p>


<h3><code>__init__</code></h3>

<p><strong>Description</strong>: Initializes the PrestaSupplier object.  It uses provided credentials or defaults to raise an exception if credentials are missing.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>credentials</code> (Optional[dict | SimpleNamespace], optional): A dictionary or SimpleNamespace object containing API domain and key. Defaults to None.</li>
  <li><code>api_domain</code> (Optional[str], optional): The API domain. Defaults to None.</li>
  <li><code>api_key</code> (Optional[str], optional): The API key. Defaults to None.</li>
  <li><code>*args</code>: Variable positional arguments.</li>
  <li><code>**kwards</code>: Keyword arguments.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li>None</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>ValueError</code>: Raised if both <code>api_domain</code> and <code>api_key</code> are not provided.</li>
</ul>


<h2>Functions</h2>

<p>(No functions defined in this file.)</p>