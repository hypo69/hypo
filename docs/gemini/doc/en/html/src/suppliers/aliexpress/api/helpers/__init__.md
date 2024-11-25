html
<h1>aliexpress.api.helpers</h1>

<h2>Overview</h2>
<p>This module provides helper functions for interacting with the AliExpress API.  It handles various aspects of data retrieval and processing.</p>

<h2>Functions</h2>

<h3><code>api_request</code></h3>

<p><strong>Description</strong>:  Handles the actual API request, likely making HTTP requests to AliExpress.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>url</code> (str): The URL to request.</li>
  <li><code>params</code> (dict, optional): Parameters to be included in the request. Defaults to `None`.</li>
  <li><code>headers</code> (dict, optional): Headers for the request. Defaults to `None`.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>dict | None</code>: The response data from the API, or `None` if an error occurs.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>RequestError</code>: If there is an issue making the API request.</li>
</ul>


<h3><code>get_list_as_string</code></h3>

<p><strong>Description</strong>: Formats a list of items into a string.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>items</code> (list): The list of items to format. </li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>str</code>: The formatted string of items, or an empty string if the input is not a list or is empty.</li>
</ul>


<h3><code>get_product_ids</code></h3>

<p><strong>Description</strong>: Extracts product IDs from input data.  </p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>data</code> (any): The input data. </li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>list[int]</code>: A list of product IDs extracted from the input data.  Returns an empty list if no product IDs are found.</li>
</ul>


<h3><code>parse_products</code></h3>

<p><strong>Description</strong>: Parses product data received from the API.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>data</code> (dict): The API response data containing product information.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>list[dict]</code>: A list of dictionaries, each representing a parsed product.</li>
</ul>


<h3><code>filter_parent_categories</code></h3>

<p><strong>Description</strong>: Filters the parent categories in product data.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>data</code> (list[dict]): List of dictionaries containing categories data. </li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>list[str]</code>: A list of parent category names.</li>
</ul>


<h3><code>filter_child_categories</code></h3>

<p><strong>Description</strong>: Filters the child categories in product data.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>data</code> (list[dict]): List of dictionaries containing categories data. </li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>list[str]</code>: A list of child category names. </li>
</ul>