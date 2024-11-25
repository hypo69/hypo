html
<h1>Module: hypotez/src/product/__init__.py</h1>

<h2>Overview</h2>
<p>This module provides an initial setup for the product handling. It imports necessary classes and functions from submodules, specifically `product.py`, `product_fields.py`, and `product_fields_translator.py`, and defines a global variable `MODE`.</p>

<h2>External Classes and Attributes</h2>

<h3><code>Product</code></h3>

<p><strong>Description</strong>: Methods and attributes of the product. Detailed description in <code>product.py</code>.</p>

<h3><code>ProductFields</code></h3>

<p><strong>Description</strong>: Product fields. Detailed description in <code>product_fields.py</code>.</p>

<h3><code>record</code></h3>

<p><strong>Description</strong>: A dictionary of product fields in flat format (without nesting).</p>

<h3><code>translate_presta_fields_dict</code></h3>

<p><strong>Description</strong>: Function that translates multilingual fields of <code>ProductFields</code>. Detailed implementation in <code>product_fields/product_fields_translator.py</code>.</p>


<h2>Variables</h2>

<h3><code>MODE</code></h3>

<p><strong>Description</strong>: A global variable storing the current application mode.  Current value: 'dev'.</p>


<h2>Imports</h2>

<p>This module imports the following:</p>

<ul>
  <li><code>Product</code> from <code>.product</code></li>
  <li><code>ProductFields</code> from <code>.product_fields.product_fields</code></li>
  <li><code>translate_presta_fields_dict</code> from <code>.product_fields.product_fields_translator</code></li>
</ul>