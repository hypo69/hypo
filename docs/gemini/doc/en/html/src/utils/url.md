html
<h1>Module: hypotez/src/utils/string/url.py</h1>

<h2>Overview</h2>
<p>This module provides functions for working with URL strings, including extracting query parameters and validating URLs. It leverages the `urllib.parse` and `validators` libraries.</p>

<h2>Constants</h2>

<h3><code>MODE</code></h3>

<p><strong>Description</strong>:  A constant representing the current mode (e.g., development). Its value is set to 'dev'.</p>

<h2>Functions</h2>

<h3><code>extract_url_params</code></h3>

<p><strong>Description</strong>: Extracts parameters from a URL string.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>url</code> (str): The URL string to parse.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>dict | None</code>: A dictionary containing the query parameters and their values, or <code>None</code> if the URL doesn't contain parameters.  If a parameter has only one value, it's converted to a string.</li>
</ul>


<h3><code>is_url</code></h3>

<p><strong>Description</strong>: Checks if the provided text is a valid URL using the `validators` library.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>text</code> (str): The string to validate.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>bool</code>: <code>True</code> if the string is a valid URL, otherwise <code>False</code>.</li>
</ul>


<h2>Example Usage (in `if __name__ == "__main__":`)</h2>

<p>This section demonstrates how to use the functions in the module, prompting the user for a URL and then printing the extracted parameters, or a message indicating invalid input.</p>


```html