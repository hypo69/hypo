html
<h1>AliexpressAffiliateCategoryGetRequest</h1>

<h2>Overview</h2>
<p>This module defines the <code>AliexpressAffiliateCategoryGetRequest</code> class, which is used for making API requests to retrieve affiliate category information from AliExpress.</p>

<h2>Classes</h2>

<h3><code>AliexpressAffiliateCategoryGetRequest</code></h3>

<p><strong>Description</strong>: This class handles requests to retrieve affiliate category data from the AliExpress API.</p>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__</code>: Initializes the <code>AliexpressAffiliateCategoryGetRequest</code> object.</li>
  <li><code>getapiname</code>: Returns the API name for the affiliate category get request.</li>
</ul>


<h2>Methods</h2>

<h3><code>__init__</code></h3>

<p><strong>Description</strong>: Initializes the <code>AliexpressAffiliateCategoryGetRequest</code> object.  This method inherits from the <code>RestApi</code> class and initializes the necessary attributes for making API requests.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>domain</code> (str, optional): The domain of the API endpoint. Defaults to "api-sg.aliexpress.com".</li>
  <li><code>port</code> (int, optional): The port number of the API endpoint. Defaults to 80.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li>No explicit exceptions raised in the provided code.</li>
</ul>


<h3><code>getapiname</code></h3>

<p><strong>Description</strong>: Returns the name of the API method for retrieving affiliate category information.</p>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>str</code>: The name of the API method, which is "aliexpress.affiliate.category.get".</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li>No explicit exceptions raised in the provided code.</li>
</ul>