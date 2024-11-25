html
<h1>AliexpressAffiliateLinkGenerateRequest</h1>

<h2>Overview</h2>
<p>This module defines the <code>AliexpressAffiliateLinkGenerateRequest</code> class, which is part of the Aliexpress API for generating affiliate links.</p>

<h2>Classes</h2>

<h3><code>AliexpressAffiliateLinkGenerateRequest</code></h3>

<p><strong>Description</strong>: This class handles requests to generate affiliate links on AliExpress.</p>

<p><strong>Methods</strong>:</p>
<ul>
<li><code>__init__</code>: Initializes the request object.</li>
<li><code>getapiname</code>: Returns the API name for this request.</li>
</ul>

<hr>
<h3><code>__init__</code></h3>

<p><strong>Description</strong>: Initializes the <code>AliexpressAffiliateLinkGenerateRequest</code> object.  It initializes the parent <code>RestApi</code> class and sets default values for various attributes.</p>

<p><strong>Parameters</strong>:</p>
<ul>
<li><code>domain</code> (str, optional): The domain of the AliExpress API. Defaults to "api-sg.aliexpress.com".</li>
<li><code>port</code> (int, optional): The port of the AliExpress API. Defaults to 80.</li>
</ul>


<p><strong>Raises</strong>:</p>
<ul>
<li><code>Exception</code>:  Raised if there is an error during initialization.</li>
</ul>

<hr>
<h3><code>getapiname</code></h3>

<p><strong>Description</strong>: Returns the name of the API method used for generating affiliate links.</p>


<p><strong>Returns</strong>:</p>
<ul>
<li><code>str</code>: The name of the API method ("aliexpress.affiliate.link.generate").</li>
</ul>


<hr>

<p><em>Note: The provided Python code snippet does not contain the necessary `Args`, `Returns`, and `Raises` sections. This documentation is a template based on the provided instructions.  To get accurate documentation, the corresponding comments need to be included in the original Python source code.</em></p>