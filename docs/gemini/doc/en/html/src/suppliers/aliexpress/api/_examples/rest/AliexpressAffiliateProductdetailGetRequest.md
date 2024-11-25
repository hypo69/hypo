html
<h1>AliexpressAffiliateProductdetailGetRequest</h1>

<h2>Overview</h2>
<p>This module defines the <code>AliexpressAffiliateProductdetailGetRequest</code> class, which is used to interact with the AliExpress Affiliate API to retrieve product details.</p>

<h2>Classes</h2>

<h3><code>AliexpressAffiliateProductdetailGetRequest</code></h3>

<p><strong>Description</strong>: This class handles requests to the AliExpress Affiliate API for retrieving product details. It inherits from the <code>RestApi</code> class.</p>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__</code>: Initializes the <code>AliexpressAffiliateProductdetailGetRequest</code> object.
    <ul>
      <li><strong>Description</strong>: Initializes the object with the API domain and port. Also, initializes attributes for application signature, country, fields, product IDs, target currency, target language, and tracking ID.</li>
      <li><strong>Parameters</strong>:
        <ul>
          <li><code>domain</code> (str, optional): The API domain. Defaults to "api-sg.aliexpress.com".</li>
          <li><code>port</code> (int, optional): The API port. Defaults to 80.</li>
        </ul>
      </li>
      <li><strong>Raises</strong>: None</li>
      </ul>
  </li>
  <li><code>getapiname</code>: Returns the API name.
    <ul>
      <li><strong>Description</strong>: Returns the name of the API endpoint.</li>
      <li><strong>Returns</strong>:
        <ul>
          <li><code>str</code>: The API name "aliexpress.affiliate.productdetail.get".</li>
        </ul>
      </li>
      <li><strong>Raises</strong>: None</li>
    </ul>
  </li>
</ul>

</ul>