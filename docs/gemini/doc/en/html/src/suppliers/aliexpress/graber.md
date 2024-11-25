html
<h1>Module: hypotez/src/suppliers/aliexpress/graber.py</h1>

<h2>Overview</h2>
<p>This module defines the <code>Graber</code> class for scraping product data from AliExpress. It inherits from the <code>Grbr</code> class and provides asynchronous methods for grabbing product fields.</p>

<h2>Global Variables</h2>

<h3><code>MODE</code></h3>

<p><strong>Description</strong>: Stores the current operation mode (likely 'dev').</p>


<h2>Classes</h2>

<h3><code>Context</code></h3>

<p><strong>Description</strong>: A class to hold global configuration settings for the scraping process.  It's a container for driver, locator, and supplier prefix.</p>

<p><strong>Attributes</strong>:</p>
<ul>
  <li><code>driver</code> (Driver): The WebDriver instance used for interaction with the browser.  Initialized as None.</li>
  <li><code>locator</code> (SimpleNamespace): A namespace containing locator objects (e.g., for pop-up closures). Initialized as None.</li>
  <li><code>supplier_prefix</code> (str): The prefix for this supplier, currently 'aliexpress'.</li>
</ul>


<h3><code>Graber</code></h3>

<p><strong>Description</strong>: A class for grabbing product fields from AliExpress. It inherits from the <code>Grbr</code> class, providing methods for data extraction.</p>

<p><strong>Attributes</strong>:</p>
<ul>
  <li><code>supplier_prefix</code> (str): The prefix for this supplier, set to 'aliexpress'.</li>
</ul>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__</code>(driver: Driver):
    <p><strong>Description</strong>: Initializes the <code>Graber</code> instance. Sets the <code>supplier_prefix</code> and calls the parent class constructor.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>driver</code> (Driver): The WebDriver instance.</li>
    </ul>
  </li>
  <li><code>grab_page</code>(driver: Driver) -> ProductFields:
    <p><strong>Description</strong>: Asynchronous function to grab product fields from the specified page using the provided driver.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>driver</code> (Driver): The WebDriver instance.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>ProductFields</code>: An object containing the extracted product fields.</li>
    </ul>
    <p><strong>Details</strong>: The method uses a nested asynchronous function, <code>fetch_all_data</code>, to call multiple data extraction functions. It returns the extracted product fields.</p>
  </li>
    <li><code>id_product</code></li>
    <li><code>additional_shipping_cost</code></li>
    <li><code>delivery_in_stock</code></li>
    <li><code>active</code></li>
    <li><code>additional_delivery_times</code></li>
    <li><code>advanced_stock_management</code></li>
    <li><code>affiliate_short_link</code></li>
    <li><code>affiliate_summary</code></li>
    <li><code>affiliate_summary_2</code></li>
    <li><code>affiliate_text</code></li>
    <li><code>affiliate_image_large</code></li>
    <li><code>affiliate_image_medium</code></li>
    <li><code>affiliate_image_small</code></li>
    <li><code>available_date</code></li>
    <li><code>available_for_order</code></li>
    <li><code>available_later</code></li>
    <li><code>available_now</code></li>
    <li><code>cache_default_attribute</code></li>
    <li><code>cache_has_attachments</code></li>
    <li><code>cache_is_pack</code></li>
    <li><code>condition</code></li>
    <li><code>customizable</code></li>
    <li><code>date_add</code></li>
    <li><code>date_upd</code></li>
    <li><code>default_image_url</code></li>
    <li><code>delivery_out_stock</code></li>
    <li><code>depth</code></li>
    <li><code>description</code></li>
    <li><code>description_short</code></li>
    <li><code>ean13</code></li>
    <li><code>ecotax</code></li>
    <li><code>height</code></li>
    <li><code>how_to_use</code></li>
    <li><code>id_category_default</code></li>
    <li><code>additional_categories</code></li>
    <li><code>id_default_combination</code></li>
    <li><code>id_default_image</code></li>
    <li><code>id_manufacturer</code></li>
    <li><code>id_supplier</code></li>
    <li><code>id_tax</code></li>
    <li><code>id_type_redirected</code></li>
    <li><code>images_urls</code></li>
    <li><code>indexed</code></li>
    <li><code>ingredients</code></li>
    <li><code>meta_description</code></li>
    <li><code>meta_keywords</code></li>
    <li><code>meta_title</code></li>
    <li><code>is_virtual</code></li>
    <li><code>isbn</code></li>
    <li><code>name</code></li>
    <li><code>link_rewrite</code></li>
    <li><code>location</code></li>
    <li><code>low_stock_alert</code></li>
    <li><code>low_stock_threshold</code></li>
    <li><code>minimal_quantity</code></li>
    <li><code>mpn</code></li>
    <li><code>online_only</code></li>
    <li><code>on_sale</code></li>
    <li><code>out_of_stock</code></li>
    <li><code>pack_stock_type</code></li>
    <li><code>locale</code></li>
    <li><code>price</code></li>
    <li><code>product_type</code></li>
    <li><code>quantity_discount</code></li>
    <li><code>redirect_type</code></li>
    <li><code>reference</code></li>
    <li><code>show_condition</code></li>
    <li><code>show_price</code></li>
    <li><code>specification</code></li>
    <li><code>state</code></li>
    <li><code>text_fields</code></li>
    <li><code>unit_price_ratio</code></li>
    <li><code>unity</code></li>
    <li><code>upc</code></li>
    <li><code>uploadable_files</code></li>
    <li><code>visibility</code></li>
    <li><code>weight</code></li>
    <li><code>wholesale_price</code></li>
    <li><code>width</code></li>
    <li><code>local_saved_image</code></li>
    <li><code>local_saved_video</code></li>
</ul>

<h2>Functions</h2>
<!-- Function definitions omitted for brevity. -->

<h2>Exceptions</h2>

<p><em>(Omitted for brevity -  they can be inferred by the exception handling 'ex' keywords in the code)</em></p>