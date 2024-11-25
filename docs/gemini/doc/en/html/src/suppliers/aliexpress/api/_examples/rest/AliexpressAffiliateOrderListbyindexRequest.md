html
<h1>AliexpressAffiliateOrderListbyindexRequest</h1>

<h2>Overview</h2>
<p>This module defines the <code>AliexpressAffiliateOrderListbyindexRequest</code> class, which is used for interacting with the AliExpress affiliate order list API.  It inherits from the base <code>RestApi</code> class and provides methods to construct and send requests to the API.</p>

<h2>Classes</h2>

<h3><code>AliexpressAffiliateOrderListbyindexRequest</code></h3>

<p><strong>Description</strong>: This class handles requests to the AliExpress affiliate order list API. It allows for customization of request parameters for retrieving order details.</p>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__</code>:
    <p><strong>Description</strong>: Initializes the <code>AliexpressAffiliateOrderListbyindexRequest</code> object.</p>

    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>domain</code> (str, optional): The domain for the API endpoint. Defaults to "api-sg.aliexpress.com".</li>
      <li><code>port</code> (int, optional): The port for the API endpoint. Defaults to 80.</li>
    </ul>

    <p><strong>Raises</strong>:</p>
    <ul>
      <li>No exceptions listed in the provided code snippet</li>
    </ul>
  </li>
  <li><code>getapiname</code>:
    <p><strong>Description</strong>: Returns the API name for the request.</p>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li>str: The API name ("aliexpress.affiliate.order.listbyindex").</li>
    </ul>
    <p><strong>Raises</strong>:</p>
    <ul>
      <li>No exceptions listed in the provided code snippet</li>
    </ul>
  </li>
</ul>


<p><strong>Attributes (Instance Variables)</strong>:</p>
<ul>
<li><code>app_signature</code>:</li>
<li><code>end_time</code>:</li>
<li><code>fields</code>:</li>
<li><code>page_size</code>:</li>
<li><code>start_query_index_id</code>:</li>
<li><code>start_time</code>:</li>
<li><code>status</code>:</li>

</ul>