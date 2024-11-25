html
<h1>Module arguments</h1>

<h2>Overview</h2>
<p>This module provides helper functions for handling arguments related to product IDs and lists.</p>

<h2>Functions</h2>

<h3><code>get_list_as_string</code></h3>

<p><strong>Description</strong>: Converts a list or string to a comma-separated string.  Handles cases where the input is None.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>value</code> (object): The input value to convert. Can be a list or string, or None.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>str | None</code>: Returns a comma-separated string if the input is a list, the input string if it's a string, otherwise, it returns None if the input is None</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>InvalidArgumentException</code>: Raised if the input is neither a list nor a string.</li>
</ul>


<h3><code>get_product_ids</code></h3>

<p><strong>Description</strong>: Extracts product IDs from a string or list of product identifiers using the <code>get_product_id</code> function from the <code>tools</code> module.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>values</code> (str | list): A string containing a comma-separated list of product identifiers or a list of product identifiers.  If a string is passed, it will be split on the comma.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>list</code>: A list of product IDs.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>InvalidArgumentException</code>: Raised if the input is not a string or a list.</li>
</ul>