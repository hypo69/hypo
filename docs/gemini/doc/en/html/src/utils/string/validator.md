html
<h1>hypotez/src/utils/string/validator.py</h1>

<h2>Overview</h2>
<p>This module provides functions for validating strings based on various criteria and formats.  It includes checks for presence of specific characters, string length, email format, URLs, and more.</p>

<h2>Classes</h2>

<h3><code>ProductFieldsValidator</code></h3>

<p><strong>Description</strong>: A class for validating product-related string fields.</p>

<p><strong>Static Methods</strong>:</p>
<ul>
  <li><code>validate_price(price: str) -> bool</code>
    <p><strong>Description</strong>: Validates the price string.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>price</code> (str): The price string to validate.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>bool</code>: <code>True</code> if the price is valid (convertible to a float), <code>None</code> otherwise.</li>
    </ul>
  </li>
  <li><code>validate_weight(weight: str) -> bool</code>
    <p><strong>Description</strong>: Validates the weight string.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>weight</code> (str): The weight string to validate.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>bool</code>: <code>True</code> if the weight is valid (convertible to a float), <code>None</code> otherwise.</li>
    </ul>
  </li>
  <li><code>validate_sku(sku: str) -> bool</code>
    <p><strong>Description</strong>: Validates the SKU (Stock Keeping Unit) string.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>sku</code> (str): The SKU string to validate.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>bool</code>: <code>True</code> if the SKU is valid (at least 3 characters after cleaning), <code>None</code> otherwise.</li>
    </ul>
  </li>
  <li><code>validate_url(url: str) -> bool</code>
    <p><strong>Description</strong>: Validates the URL string.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>url</code> (str): The URL string to validate.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>bool</code>: <code>True</code> if the URL is valid (parseable), <code>None</code> otherwise.</li>
    </ul>
  </li>
  <li><code>isint(s: str) -> bool</code>
    <p><strong>Description</strong>: Checks if a string can be converted to an integer.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>s</code> (str): The string to check.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>bool</code>: <code>True</code> if convertible, <code>None</code> otherwise.</li>
    </ul>
   </li>
</ul>

<h2>Functions</h2>

<p>(None)</p>

<h2>Module Attributes</h2>

<p>(None)</p>