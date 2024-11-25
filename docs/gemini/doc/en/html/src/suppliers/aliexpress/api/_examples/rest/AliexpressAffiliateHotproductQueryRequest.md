html
<h1>AliexpressAffiliateHotproductQueryRequest</h1>

<h2>Overview</h2>
<p>This module defines the <code>AliexpressAffiliateHotproductQueryRequest</code> class, which is used to query hot products on AliExpress for affiliate marketing purposes. It inherits from the <code>RestApi</code> class, providing a structured way to interact with the AliExpress API.</p>

<h2>Classes</h2>

<h3><code>AliexpressAffiliateHotproductQueryRequest</code></h3>

<p><strong>Description</strong>: This class handles the request for querying hot products on AliExpress.  It allows setting various parameters to refine the search, such as category IDs, keywords, price ranges, and more.</p>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__</code>:
    <p><strong>Description</strong>: Initializes the <code>AliexpressAffiliateHotproductQueryRequest</code> object.  It takes optional parameters for domain, port, app_signature, category_ids, and many other filtering parameters.  Defaults are set for domain and port.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>domain</code> (str, optional): The domain to use for the API request. Defaults to "api-sg.aliexpress.com".</li>
      <li><code>port</code> (int, optional): The port to use for the API request. Defaults to 80.</li>
      <li><code>app_signature</code> (object, optional):  The application signature.</li>
      <li><code>category_ids</code> (object, optional):  Category IDs for filtering.</li>
      <li><code>delivery_days</code> (object, optional):  Maximum delivery days.</li>
      <li><code>fields</code> (object, optional):  Fields to retrieve.</li>
      <li><code>keywords</code> (object, optional):  Keywords for searching.</li>
      <li><code>max_sale_price</code> (object, optional):  Maximum sale price.</li>
      <li><code>min_sale_price</code> (object, optional): Minimum sale price.</li>
      <li><code>page_no</code> (object, optional):  Page number for pagination.</li>
      <li><code>page_size</code> (object, optional): Page size for pagination.</li>
      <li><code>platform_product_type</code> (object, optional): Platform product type.</li>
      <li><code>ship_to_country</code> (object, optional): Country for shipping.</li>
      <li><code>sort</code> (object, optional): Sorting criteria.</li>
      <li><code>target_currency</code> (object, optional): Target currency.</li>
      <li><code>target_language</code> (object, optional): Target language.</li>
      <li><code>tracking_id</code> (object, optional): Tracking ID.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>None</code>:  Initializes the object.</li>
    </ul>
  </li>
  <li><code>getapiname</code>:
    <p><strong>Description</strong>: Returns the name of the API endpoint.</p>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>str</code>: The name of the API endpoint (<code>aliexpress.affiliate.hotproduct.query</code>).</li>
    </ul>
  </li>
</ul>