html
<h1>Module: hypotez/src/suppliers/aliexpress/api/_examples/iop/base.py</h1>

<h2>Overview</h2>
<p>This module provides a Python SDK for interacting with the iop API. It handles API requests, signatures, and error logging.</p>

<h2>Constants</h2>
<h3><code>P_SDK_VERSION</code></h3>

<p><strong>Description</strong>: The version of the iop SDK.</p>
<p><strong>Value</strong>: "iop-sdk-python-20220609"</p>

<h3><code>P_APPKEY</code></h3>

<p><strong>Description</strong>: Application key for API authentication.</p>

<h3><code>P_ACCESS_TOKEN</code></h3>

<p><strong>Description</strong>: Access token for API authentication.</p>


<h3><code>P_TIMESTAMP</code></h3>

<p><strong>Description</strong>: Timestamp for API requests.</p>

<h3><code>P_SIGN</code></h3>

<p><strong>Description</strong>: Signature for API requests.</p>

<h3><code>P_SIGN_METHOD</code></h3>

<p><strong>Description</strong>: Signature method for API requests.</p>

<h3><code>P_PARTNER_ID</code></h3>

<p><strong>Description</strong>: Partner ID for API requests.</p>

<h3><code>P_METHOD</code></h3>

<p><strong>Description</strong>: API method name.</p>

<h3><code>P_DEBUG</code></h3>

<p><strong>Description</strong>: Debug mode flag.</p>

<h3><code>P_SIMPLIFY</code></h3>

<p><strong>Description</strong>: Simplify response flag.</p>

<h3><code>P_FORMAT</code></h3>

<p><strong>Description</strong>: Response format.</p>

<h3><code>P_CODE</code></h3>

<p><strong>Description</strong>: API response code.</p>

<h3><code>P_TYPE</code></h3>

<p><strong>Description</strong>: API response type.</p>

<h3><code>P_MESSAGE</code></h3>

<p><strong>Description</strong>: API response message.</p>

<h3><code>P_REQUEST_ID</code></h3>

<p><strong>Description</strong>: API request ID.</p>

<h3><code>P_LOG_LEVEL_DEBUG</code></h3>

<p><strong>Description</strong>: Debug log level.</p>

<h3><code>P_LOG_LEVEL_INFO</code></h3>

<p><strong>Description</strong>: Info log level.</p>

<h3><code>P_LOG_LEVEL_ERROR</code></h3>

<p><strong>Description</strong>: Error log level.</p>

<h2>Functions</h2>

<h3><code>sign</code></h3>

<p><strong>Description</strong>: Computes the signature for an API request.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>secret</code> (str): Secret key for API authentication.</li>
  <li><code>api</code> (str): API endpoint.</li>
  <li><code>parameters</code> (dict): API request parameters.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>str</code>: Computed signature.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>: Any error during signature generation.</li>
</ul>



<h3><code>mixStr</code></h3>

<p><strong>Description</strong>: Converts various types to strings.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>pstr</code> (str | unicode | any): Value to convert.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>str</code>: The string representation of the input.</li>
</ul>

<h3><code>logApiError</code></h3>

<p><strong>Description</strong>: Logs API errors.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>appkey</code> (str): Application key.</li>
  <li><code>sdkVersion</code> (str): SDK version.</li>
  <li><code>requestUrl</code> (str): Request URL.</li>
  <li><code>code</code> (str): Error code.</li>
  <li><code>message</code> (str): Error message.</li>
</ul>


<h2>Classes</h2>

<h3><code>IopRequest</code></h3>

<p><strong>Description</strong>: Represents an API request.</p>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>add_api_param(key, value)</code>: Adds an API parameter.</li>
  <li><code>add_file_param(key, value)</code>: Adds a file parameter.</li>
  <li><code>set_simplify()</code>: Sets simplify response flag.</li>
  <li><code>set_format(value)</code>: Sets response format.</li>
</ul>


<h3><code>IopResponse</code></h3>

<p><strong>Description</strong>: Represents an API response.</p>

<p><strong>Attributes</strong>:</p>
<ul>
  <li><code>type</code>: Response type.</li>
  <li><code>code</code>: Response code.</li>
  <li><code>message</code>: Response message.</li>
  <li><code>request_id</code>: Request ID.</li>
  <li><code>body</code>: Response body (JSON).</li>
</ul>


<h3><code>IopClient</code></h3>

<p><strong>Description</strong>: Client for interacting with the iop API.</p>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>execute(request, access_token=None)</code>: Executes the API request.</li>
</ul>

<p><strong>Attributes</strong>:</p>

<ul>
<li><code>server_url</code> (str): Server URL for the iop API.</li>
<li><code>app_key</code> (str): Application key for authentication.</li>
<li><code>app_secret</code> (str): Application secret key for authentication.</li>
<li><code>timeout</code> (int): Timeout for API requests.</li>
</ul>