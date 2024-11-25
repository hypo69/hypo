html
<h1>Module src.product</h1>

<h2>Overview</h2>
<p>Defines the behavior of a product in the project, interacting with the website, product, and PrestaShop.</p>

<h2>Constants</h2>

<h3><code>MODE</code></h3>
<p><strong>Description</strong>: Stores the current mode (e.g., 'dev').</p>


<h2>Classes</h2>

<h3><code>Product</code></h3>

<p><strong>Description</strong>: Manipulations with the product.  Initially, the grabber fetches product page data, then interacts with the PrestaShop API.</p>

<p><strong>Inherits from</strong>: <code>ProductFields</code>, <code>PrestaShop</code></p>

<h4><code>__init__</code></h4>

<p><strong>Description</strong>: Initializes a Product object.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>args</code>: Variable length argument list.</li>
  <li><code>kwargs</code>: Arbitrary keyword arguments.</li>
</ul>


<h3><code>Category</code></h3>
<p><strong>Description</strong>: (Placeholder - Needs the Category class definition)</p>

<p><strong>Methods</strong>:</p>

<ul>
  <li><code>get_parents</code>:  Retrieves parent categories for a given category ID.</li>
</ul>


<h2>Functions</h2>

<h3><code>get_parent_categories</code></h3>

<p><strong>Description</strong>: Collects parent categories from a specified category ID. Duplicates the `get_parents` function from the `Category` class.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>id_category</code> (int): ID of the category.</li>
  <li><code>dept</code> (int, optional): Depth of the category. Defaults to 0.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>list</code>: List of parent categories.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>TypeError</code>: If <code>id_category</code> is not an integer.</li>
</ul>