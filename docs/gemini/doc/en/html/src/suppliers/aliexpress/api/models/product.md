html
<h1>Product Model</h1>

<h2>Overview</h2>
<p>This module defines the <code>Product</code> class, representing product data fetched from AliExpress.</p>

<h2>Classes</h2>

<h3><code>Product</code></h3>

<p><strong>Description</strong>: Represents a product from AliExpress, containing details like prices, categories, and URLs.</p>

<p><strong>Attributes</strong>:</p>
<ul>
  <li><code>app_sale_price</code> (str): The application sale price.</li>
  <li><code>app_sale_price_currency</code> (str): The currency of the application sale price.</li>
  <li><code>commission_rate</code> (str): The commission rate.</li>
  <li><code>discount</code> (str): The discount applied.</li>
  <li><code>evaluate_rate</code> (str): The evaluation rate.</li>
  <li><code>first_level_category_id</code> (int): The ID of the first-level category.</li>
  <li><code>first_level_category_name</code> (str): The name of the first-level category.</li>
  <li><code>lastest_volume</code> (int): The latest volume.</li>
    <li><code>hot_product_commission_rate</code> (str): The commission rate for hot products.</li>
    <li><code>lastest_volume</code> (int): The latest volume.</li>
  <li><code>original_price</code> (str): The original price.</li>
  <li><code>original_price_currency</code> (str): The currency of the original price.</li>
  <li><code>product_detail_url</code> (str): The URL for the product details.</li>
  <li><code>product_id</code> (int): The unique identifier for the product.</li>
  <li><code>product_main_image_url</code> (str): The URL of the main product image.</li>
  <li><code>product_small_image_urls</code> (List[str]): A list of URLs for small product images.</li>
  <li><code>product_title</code> (str): The title of the product.</li>
  <li><code>product_video_url</code> (str): The URL for a product video (if available).</li>
  <li><code>promotion_link</code> (str): The URL for any promotion related to the product.</li>
  <li><code>relevant_market_commission_rate</code> (str): The commission rate for the relevant market.</li>
  <li><code>sale_price</code> (str): The sale price.</li>
  <li><code>sale_price_currency</code> (str): The currency of the sale price.</li>
  <li><code>second_level_category_id</code> (int): The ID of the second-level category.</li>
  <li><code>second_level_category_name</code> (str): The name of the second-level category.</li>
  <li><code>shop_id</code> (int): The ID of the shop where the product is listed.</li>
  <li><code>shop_url</code> (str): The URL of the shop.</li>
  <li><code>target_app_sale_price</code> (str): The target application sale price.</li>
  <li><code>target_app_sale_price_currency</code> (str): The currency of the target application sale price.</li>
  <li><code>target_original_price</code> (str): The target original price.</li>
  <li><code>target_original_price_currency</code> (str): The currency of the target original price.</li>
  <li><code>target_sale_price</code> (str): The target sale price.</li>
  <li><code>target_sale_price_currency</code> (str): The currency of the target sale price.</li>
</ul>