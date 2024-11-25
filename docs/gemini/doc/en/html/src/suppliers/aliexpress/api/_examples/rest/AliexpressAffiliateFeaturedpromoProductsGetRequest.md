html
<h1>AliexpressAffiliateFeaturedpromoProductsGetRequest</h1>

<h2>Overview</h2>
<p>This module defines the <code>AliexpressAffiliateFeaturedpromoProductsGetRequest</code> class, which is used to make requests to the AliExpress API for featured promotional products.</p>

<h2>Classes</h2>

<h3><code>AliexpressAffiliateFeaturedpromoProductsGetRequest</code></h3>

<p><strong>Description</strong>: This class handles requests to retrieve featured promotional products from the AliExpress affiliate API.</p>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__</code>: Initializes the <code>AliexpressAffiliateFeaturedpromoProductsGetRequest</code> object.</li>
  <li><code>getapiname</code>: Returns the API name for this request.</li>
</ul>


<hr>

<h3><code>__init__</code></h3>

<p><strong>Description</strong>: Initializes the class instance with API domain, port and various parameters for the request.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>domain</code> (str, optional): The domain of the API endpoint. Defaults to "api-sg.aliexpress.com".</li>
  <li><code>port</code> (int, optional): The port number for the API connection. Defaults to 80.</li>
  <li><code>app_signature</code> (Any, optional):  Not documented.</li>
  <li><code>category_id</code> (Any, optional): Not documented.</li>
  <li><code>country</code> (Any, optional): Not documented.</li>
  <li><code>fields</code> (Any, optional): Not documented.</li>
  <li><code>page_no</code> (Any, optional): Not documented.</li>
  <li><code>page_size</code> (Any, optional): Not documented.</li>
  <li><code>promotion_end_time</code> (Any, optional): Not documented.</li>
  <li><code>promotion_name</code> (Any, optional): Not documented.</li>
  <li><code>promotion_start_time</code> (Any, optional): Not documented.</li>
  <li><code>sort</code> (Any, optional): Not documented.</li>
  <li><code>target_currency</code> (Any, optional): Not documented.</li>
  <li><code>target_language</code> (Any, optional): Not documented.</li>
  <li><code>tracking_id</code> (Any, optional): Not documented.</li>

</ul>


<p><strong>Raises</strong>:</p>
<ul>
</ul>

<hr>

<h3><code>getapiname</code></h3>

<p><strong>Description</strong>: Returns the name of the API method to be used for the request.</p>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>str</code>: The name of the API method, 'aliexpress.affiliate.featuredpromo.products.get'.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
</ul>

<hr>
<p><strong>Note</strong>: The parameters passed to the <code>__init__</code> method, excluding <code>domain</code> and <code>port</code>, are not documented, and their specific purpose or meaning is not readily apparent. This lack of documentation within the code makes it difficult to provide meaningful descriptions and examples.  A more detailed description from the API documentation or internal project documentation is needed to fully comprehend their functionality.</p>