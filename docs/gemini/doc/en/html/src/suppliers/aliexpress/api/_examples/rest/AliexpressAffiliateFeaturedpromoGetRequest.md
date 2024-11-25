html
<h1>AliexpressAffiliateFeaturedpromoGetRequest</h1>

<h2>Overview</h2>
<p>This module defines the <code>AliexpressAffiliateFeaturedpromoGetRequest</code> class, which is used for interacting with the AliExpress Affiliate Featuredpromo API. It inherits from the <code>RestApi</code> class.</p>

<h2>Classes</h2>

<h3><code>AliexpressAffiliateFeaturedpromoGetRequest</code></h3>

<p><strong>Description</strong>: This class handles requests to the AliExpress Affiliate Featuredpromo API.</p>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__</code>: Initializes the <code>AliexpressAffiliateFeaturedpromoGetRequest</code> object.
    <ul>
      <li>
        <pre><code>python
def __init__(self, domain="api-sg.aliexpress.com", port=80):
    RestApi.__init__(self, domain, port)
    self.app_signature = None
    self.fields = None
</code></pre>
        <p><strong>Description</strong>: Initializes the <code>AliexpressAffiliateFeaturedpromoGetRequest</code> class.
      </li>
      <li><strong>Parameters</strong>:</li>
      <ul>
        <li><code>domain</code> (str, optional): The domain of the API endpoint. Defaults to "api-sg.aliexpress.com".</li>
        <li><code>port</code> (int, optional): The port of the API endpoint. Defaults to 80.</li>
      </ul>
      <li><strong>Raises</strong>:</li>
      <ul>
        <li>No explicit exceptions raised within the constructor.</li>
      </ul>
        </li>
  </li>
  <li><code>getapiname</code>: Returns the API name.
    <ul>
      <li>
        <pre><code>python
def getapiname(self):
    return 'aliexpress.affiliate.featuredpromo.get'
</code></pre>
      </li>
      <li><strong>Description</strong>: Returns the name of the API endpoint.</li>
      <li><strong>Returns</strong>:</li>
      <ul>
        <li><code>str</code>: The name of the API endpoint.</li>
      </ul>
      <li><strong>Raises</strong>:</li>
      <ul>
        <li>No explicit exceptions raised.</li>
      </ul>
    </ul>
  </li>
</ul>


</ul>