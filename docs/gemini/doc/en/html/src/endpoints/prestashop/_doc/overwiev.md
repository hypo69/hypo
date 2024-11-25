html
<h1>PrestaShop Module Documentation</h1>

<h2>Overview</h2>
<p>This module provides functionality for interacting with the PrestaShop API. It offers methods for managing various aspects of the PrestaShop platform, including categories, customers, languages, price lists, products, shops, suppliers, warehouses, and the API itself.</p>

<h2>Modules</h2>

<h3><code>__init__.py</code></h3>
<p><strong>Description</strong>: Initializes the PrestaShop module.</p>


<h3><code>category.py</code></h3>
<p><strong>Description</strong>: Manages category-related functionality.</p>


<h3><code>customer.py</code></h3>
<p><strong>Description</strong>: Manages customer-related functionality.</p>


<h3><code>language.py</code></h3>
<p><strong>Description</strong>: Manages language-related functionality.</p>


<h3><code>pricelist.py</code></h3>
<p><strong>Description</strong>: Manages price list-related functionality.</p>


<h3><code>product.py</code></h3>
<p><strong>Description</strong>: Manages product-related functionality.</p>


<h3><code>shop.py</code></h3>
<p><strong>Description</strong>: Manages shop-related functionality.</p>


<h3><code>supplier.py</code></h3>
<p><strong>Description</strong>: Manages supplier-related functionality.</p>


<h3><code>version.py</code></h3>
<p><strong>Description</strong>: Manages the version information of the module.</p>


<h3><code>warehouse.py</code></h3>
<p><strong>Description</strong>: Manages warehouse-related functionality.</p>


<h2>API Module</h2>

<h3><code>api.py</code></h3>
<p><strong>Description</strong>: Contains the main logic for interacting with the PrestaShop API.</p>

<h2>API Schemas Module</h2>

<h3><code>api_resourses_list.py</code></h3>
<p><strong>Description</strong>: Lists available API resources.</p>


<h3><code>api_schemas_builder.py</code></h3>
<p><strong>Description</strong>: Script for building API schemas.</p>



<h2>Domains Module</h2>

<h3><code>domains/__init__.py</code></h3>
<p><strong>Description</strong>: Initializes the domains module.</p>


<h3><code>domains/ecat_co_il/__init__.py</code></h3>
<p><strong>Description</strong>: Initializes the ecat.co.il domain.</p>
<h3><code>domains/emildesign_com/__init__.py</code></h3>
<p><strong>Description</strong>: Initializes the emildesign.com domain.</p>
<h3><code>domains/sergey_mymaster_co_il/__init__.py</code></h3>
<p><strong>Description</strong>: Initializes the sergey.mymaster.co.il domain.</p>

<p>Note: The documentation for individual functions/methods within the Python files is not included here as it needs the actual code of each file to create complete documentation.</p>


<h2>Example Usage (Product Module)</h2>
<pre><code class="language-python">
from PrestaShop.product import Product

# Initialize the Product
product = Product()

# Example operation on product (replace with actual ID)
product_data = product.get_product_data(product_id="12345")

print(product_data)
</code></pre>