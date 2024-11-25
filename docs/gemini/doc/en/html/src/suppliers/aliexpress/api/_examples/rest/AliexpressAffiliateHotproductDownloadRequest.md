html
<h1>AliexpressAffiliateHotproductDownloadRequest</h1>

<h2>Overview</h2>
<p>This module defines the <code>AliexpressAffiliateHotproductDownloadRequest</code> class, which interacts with the AliExpress API for downloading hot product data.  It inherits from the <code>RestApi</code> base class.</p>

<h2>Table of Contents</h2>
<ul>
<li><a href="#class-aliexpressaffiliatehotproductdownloadrequest">AliexpressAffiliateHotproductDownloadRequest Class</a></li>
</ul>

<h2>Classes</h2>

<h3><a id="class-aliexpressaffiliatehotproductdownloadrequest">AliexpressAffiliateHotproductDownloadRequest</a></h3>

<p><strong>Description</strong>: This class handles requests to the AliExpress API for downloading hot product data.  It's designed to be used with the AliExpress affiliate program.</p>

<p><strong>Constructor</strong>:</p>

<pre><code>python
def __init__(self, domain="api-sg.aliexpress.com", port=80):
    """
    Initializes the AliexpressAffiliateHotproductDownloadRequest object.

    Args:
        domain (str, optional): The API domain. Defaults to "api-sg.aliexpress.com".
        port (int, optional): The API port. Defaults to 80.

    Raises:
        Exception:  If there is an issue during initialization (not explicitly detailed).
    """
    RestApi.__init__(self,domain, port)
    self.app_signature = None
    self.category_id = None
    self.country = None
    self.fields = None
    self.scenario_language_site = None
    self.page_no = None
    self.page_size = None
    self.target_currency = None
    self.target_language = None
    self.tracking_id = None
</code></pre>


<p><strong>Methods</strong>:</p>

<ul>
<li><a href="#method-getapiname"><code>getapiname</code></a></li>
</ul>

<h3><a id="method-getapiname"><code>getapiname</code></a></h3>

<pre><code>python
def getapiname(self):
    """
    Returns the API name for the request.

    Returns:
        str: The API name.
    """
    return 'aliexpress.affiliate.hotproduct.download'
</code></pre>