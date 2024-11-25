html
<h1>Module: src.suppliers.aliexpress.api.helpers.requests</h1>

<h2>Overview</h2>
<p>This module provides an API request helper function for interacting with the AliExpress API. It handles potential errors during the request and response processing, and returns the result or appropriate error messages.</p>

<h2>Functions</h2>

<h3><code>api_request</code></h3>

<p><strong>Description</strong>: This function facilitates API requests, handling potential exceptions and returning the result or an error message.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>request</code> (object): The request object to be used for the API call.</li>
  <li><code>response_name</code> (str): The name of the response key within the response object.</li>
  <li><code>attemps</code> (int, optional): The number of attempts to make the request. Defaults to 1.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>response.result</code> (object): Returns the result from the API request if the response code is 200. This is assumed to be a Python object loaded from the response.</li>
  <li><code>None</code>: Returns `None` if any exception occurs during the request, response processing, or if the response code is not 200.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>ApiRequestException</code>: Raised if an error occurs during the request process. More specific error information is likely contained in the `error.message`.</li>
  <li><code>ApiRequestResponseException</code>: Raised if an error occurs during the response processing or if the response code is not 200.</li>
</ul>


<p><strong>Implementation Details</strong>:</p>
<ul>
  <li>It attempts to get the response using <code>request.getResponse()</code>.</li>
  <li>It extracts the `resp_result` from the response using the `response_name` key.</li>
  <li>It deserializes the JSON response using `json.loads` and `object_hook` to create a `SimpleNamespace` object for easier access to the data.</li>
  <li>Checks the `resp_code` and returns the appropriate result or an error message.</li>
  <li> Includes logging for critical, warning and error cases using the `logger` object.</li>
  <li> Includes `pprint` for displaying error messages more usefully.</li>
  <li> Uses exception handling to gracefully manage errors, preventing the program from crashing.</li>
</ul>