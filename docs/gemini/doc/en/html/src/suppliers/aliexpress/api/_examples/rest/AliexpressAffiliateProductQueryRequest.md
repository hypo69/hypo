html
<h1>AliexpressAffiliateProductQueryRequest</h1>

<h2>Overview</h2>
<p>This module defines the <code>AliexpressAffiliateProductQueryRequest</code> class, which is used to query product information from AliExpress. It inherits from the <code>RestApi</code> class and provides methods for setting query parameters and retrieving the API name.</p>

<h2>Classes</h2>

<h3><code>AliexpressAffiliateProductQueryRequest</code></h3>

<p><strong>Description</strong>: This class handles the request for querying affiliate products on AliExpress. It allows setting various parameters to refine the search and inherits from the <code>RestApi</code> class.</p>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__</code>:
    <p><strong>Description</strong>: Initializes the <code>AliexpressAffiliateProductQueryRequest</code> object.
    </p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>domain</code> (str, optional): The domain for the API endpoint. Defaults to "api-sg.aliexpress.com".</li>
      <li><code>port</code> (int, optional): The port for the API endpoint. Defaults to 80.</li>
    </ul>
    <p><strong>Raises</strong>:</p>
    <ul>
        <li><code>Exception</code>: A generic exception is raised in case of initialization errors (not explicitly stated in the code but should be considered).</li>
    </ul>
  </li>
  <li><code>getapiname</code>:
    <p><strong>Description</strong>: Returns the name of the API endpoint.</p>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>str</code>: The API name.</li>
    </ul>

  </li>
</ul>
<p><strong>Attributes</strong>:</p>
<ul>
<li><code>app_signature</code></li>
<li><code>category_ids</code></li>
<li><code>delivery_days</code></li>
<li><code>fields</code></li>
<li><code>keywords</code></li>
<li><code>max_sale_price</code></li>
<li><code>min_sale_price</code></li>
<li><code>page_no</code></li>
<li><code>page_size</code></li>
<li><code>platform_product_type</code></li>
<li><code>ship_to_country</code></li>
<li><code>sort</code></li>
<li><code>target_currency</code></li>
<li><code>target_language</code></li>
<li><code>tracking_id</code></li>
</ul>

</ul>

</ul>