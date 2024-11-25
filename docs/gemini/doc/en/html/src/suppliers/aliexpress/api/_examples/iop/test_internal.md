html
<h1>Module: test_internal</h1>

<h2>Overview</h2>
<p>This module provides a test example for interacting with the iop API using the <code>IopClient</code> and <code>IopRequest</code> classes.</p>

<h2>Classes</h2>

<h3><code>IopClient</code></h3>

<p><strong>Description</strong>: This class represents a client for interacting with the iop API.</p>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>execute(request: IopRequest, access_token=None) -> IopResponse</code>: Executes an API request and returns the response.</li>
</ul>


<h3><code>IopRequest</code></h3>

<p><strong>Description</strong>: This class represents an API request.</p>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>add_api_param(name: str, value: str) -> None</code>: Adds an API parameter to the request.</li>
</ul>


<h2>Functions</h2>


<h3><code><pre><code class="language-python">execute(request)
</code></pre>
</td></h3>

<p><strong>Description</strong>: Executes the specified API request using the IopClient instance.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>request</code> (<code>IopRequest</code>): The API request object to execute.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>IopResponse</code>: The response object containing the results of the API call.</li>
</ul>


<h2>Examples</h2>

<pre><code class="language-python">
client = iop.IopClient(
    'https://api-pre.taobao.tw/rest', '100240', 'hLeciS15d7UsmXKoND76sBVPpkzepxex'
)
request = iop.IopRequest('/product/item/get', 'GET')

request.add_api_param('itemId', '157432005')
request.add_api_param('authDO', '{"sellerId":2000000016002}')

response = client.execute(request)

print(response.type)
print(response.code)
print(response.message)
print(response.request_id)
print(response.body)
print(str(round(time.time())) + '000')

</code></pre>