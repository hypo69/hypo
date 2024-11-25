html
<h1>AliexpressAffiliateOrderGetRequest</h1>

<h2>Overview</h2>
<p>This module defines the <code>AliexpressAffiliateOrderGetRequest</code> class, which is a subclass of <code>RestApi</code>.  It provides functionality for retrieving affiliate order information from AliExpress.</p>

<h2>Classes</h2>

<h3><code>AliexpressAffiliateOrderGetRequest</code></h3>

<p><strong>Description</strong>: This class handles requests for retrieving affiliate order data from the AliExpress API.  It inherits from the base <code>RestApi</code> class.</p>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__</code>: Initializes the <code>AliexpressAffiliateOrderGetRequest</code> object.
    <ul>
        <li><code>domain</code> (str, optional): The API domain (defaults to "api-sg.aliexpress.com").</li>
        <li><code>port</code> (int, optional): The API port (defaults to 80).</li>
    </ul>
  </li>
  <li><code>getapiname</code>: Returns the API name.
    <ul>
        <li>Returns (str): The API name ("aliexpress.affiliate.order.get").</li>
    </ul>
  </li>
</ul>

<hr>

<div style="text-align:center;">
  <a href="#AliexpressAffiliateOrderGetRequest">Back to Top</a>
</div>