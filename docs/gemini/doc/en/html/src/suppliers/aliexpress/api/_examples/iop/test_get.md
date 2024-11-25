html
<h1>Module: test_get</h1>

<h2>Overview</h2>
<p>This module demonstrates the usage of the <code>iop</code> library to interact with the AliExpress API for retrieving logistics seller addresses. It showcases creating an API request, executing it, and handling the response.</p>

<h2>Functions</h2>

<h3><code>client</code></h3>

<p><strong>Description</strong>: Initializes an <code>IopClient</code> instance with the necessary API details.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>gateway_url</code> (str): The base URL of the AliExpress API gateway.</li>
  <li><code>app_key</code> (str): The application key for API access.</li>
  <li><code>app_secret</code> (str): The application secret for API access.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>IopClient</code>: An initialized <code>IopClient</code> object.</li>
</ul>


<h3><code>request</code></h3>

<p><strong>Description</strong>: Creates an <code>IopRequest</code> object for the 'aliexpress.logistics.redefining.getlogisticsselleraddresses' API endpoint.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>api_name</code> (str): The name of the API endpoint.</li>
  <li><code>http_method</code> (str): The HTTP method to be used (default is POST).</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>IopRequest</code>: The initialized <code>IopRequest</code> object.</li>
</ul>


<h3><code>response</code></h3>

<p><strong>Description</strong>: Executes the API request and retrieves the response from the AliExpress API.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>request</code> (IopRequest): The API request object.</li>
  <li><code>request_id</code>(str): Unique identifier for the request.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>IopResponse</code>: The API response object.</li>
</ul>


<h3><code>print(response.type)</code></h3>

<p><strong>Description</strong>: Prints the type of the response.  This indicates whether there was an error or not.</p>


<h3><code>print(response.code)</code></h3>

<p><strong>Description</strong>: Prints the response code.</p>


<h3><code>print(response.message)</code></h3>

<p><strong>Description</strong>: Prints the response error message, if any.</p>


<h3><code>print(response.request_id)</code></h3>

<p><strong>Description</strong>: Prints the unique request ID associated with the response.</p>

<h3><code>print(response.body)</code></h3>

<p><strong>Description</strong>: Prints the complete response body.</p>

<h2>Classes</h2>

<h3><code>IopClient</code></h3>
<p><strong>Description</strong>:  A client for interacting with the iop service.</p>

<h3><code>IopRequest</code></h3>
<p><strong>Description</strong>: Represents an API request to be executed.</p>
<p><strong>Methods</strong>:</p>
<ul>
  <li><code>set_simplify()</code>: Configures the request for simplified response.</li>
  <li><code>add_api_param(param_name, param_value)</code>: Adds a parameter to the request.</li>
</ul>



<h3><code>IopResponse</code></h3>
<p><strong>Description</strong>: Holds the response from the API call.</p>
<p><strong>Attributes</strong>:</p>
<ul>
  <li><code>type</code> (str): Indicates the type of response (nil, ISP, ISV, SYSTEM).</li>
  <li><code>code</code> (int): The response code (0 for success, non-zero for errors).</li>
  <li><code>message</code> (str): The error message if applicable.</li>
  <li><code>request_id</code> (str): Unique identifier for the request.</li>
  <li><code>body</code> (dict): The full response body.</li>
</ul>