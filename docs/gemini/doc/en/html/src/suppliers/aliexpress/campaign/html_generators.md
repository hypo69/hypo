html
<h1>Module: hypotez/src/suppliers/aliexpress/campaign/html_generators.py</h1>

<h2>Overview</h2>
<p>This module provides classes for generating HTML content for AliExpress campaign data, including individual product pages, category pages, and an overall campaign overview page.</p>

<h2>Global Variables</h2>

<h3><code>MODE</code></h3>

<p><strong>Description</strong>:  A string variable holding the current mode, likely 'dev' in this case.</p>


<h2>Classes</h2>

<h3><code>ProductHTMLGenerator</code></h3>

<p><strong>Description</strong>: A class for generating HTML for individual products.</p>

<h4><code>set_product_html</code></h4>

<p><strong>Description</strong>: Creates an HTML file for an individual product.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>product</code> (SimpleNamespace): The product details to include in the HTML.</li>
  <li><code>category_path</code> (str | Path): The path to save the HTML file.</li>
</ul>


<p><strong>Returns</strong>:</p>
<ul>
  <li>None:  The function doesn't explicitly return a value. It saves the HTML content to a file.</li>
</ul>


<p><strong>Raises</strong>:</p>
<ul>
  <li>None:  No exceptions are explicitly raised in the function.</li>
</ul>


<h3><code>CategoryHTMLGenerator</code></h3>

<p><strong>Description</strong>: A class for generating HTML for product categories.</p>

<h4><code>set_category_html</code></h4>

<p><strong>Description</strong>: Creates an HTML file for the category.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>products_list</code> (list[SimpleNamespace] | SimpleNamespace): List of products to include in the HTML. Accepts a single product if it's not a list.</li>
  <li><code>category_path</code> (str | Path): Path to save the HTML file.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li>None: The function doesn't explicitly return a value. It saves the HTML content to a file.</li>
</ul>


<p><strong>Raises</strong>:</p>
<ul>
  <li>None: No exceptions are explicitly raised in the function.</li>
</ul>


<h3><code>CampaignHTMLGenerator</code></h3>

<p><strong>Description</strong>: A class for generating HTML for a campaign.</p>

<h4><code>set_campaign_html</code></h4>

<p><strong>Description</strong>: Creates an HTML file for the campaign, listing all categories.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>categories</code> (list[str]): List of category names.</li>
  <li><code>campaign_path</code> (str | Path): Path to save the HTML file.</li>
</ul>


<p><strong>Returns</strong>:</p>
<ul>
  <li>None: The function doesn't explicitly return a value. It saves the HTML content to a file.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li>None: No exceptions are explicitly raised in the function.</li>
</ul>


<h2>Imported Modules</h2>
<p>The module imports the following modules:</p>

<ul>
  <li><code>header</code></li>
  <li><code>pathlib</code></li>
  <li><code>types</code></li>
  <li><code>src.utils.file</code></li>
  <li><code>html</code></li>
</ul>

<p>Note: The exact functionality of imported modules may need more information to complete the documentation.</p>