html
<h1>StringNormalizer Module</h1>

<h2>Overview</h2>
<p>This module provides methods for normalizing various data types, including booleans, strings, integers, and floats.</p>

<h2>Classes</h2>

<h3><code>StringNormalizer</code></h3>

<p><strong>Description</strong>: This class encapsulates methods for normalizing product fields.</p>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>normalize_boolean(input_data: Any) -> bool</code>:
    <p><strong>Description</strong>: Normalizes data into a boolean value. Accepts various input types (bool, string, integer) and converts them to a boolean.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>input_data (Any)</code>: Data that can represent a boolean (e.g., bool, string, integer).</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>bool</code>: Boolean representation of the input.</li>
    </ul>
    <p><strong>Raises</strong>:</p>
    <ul>
      <li><code>Exception</code>:  If an error occurs during conversion.</li>
    </ul>
  </li>
  <li><code>normalize_string(input_data: Union[str, List[str]]) -> str</code>:
    <p><strong>Description</strong>: Normalizes a string or a list of strings. Cleans the input by removing HTML tags, line breaks, special characters, and extra whitespace.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>input_data (str | List[str])</code>: Input data (string or list of strings).</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>str</code>: Cleaned and normalized string.</li>
    </ul>
    <p><strong>Raises</strong>:</p>
    <ul>
      <li><code>Exception</code>: If an error occurs during cleaning or normalization.</li>
    </ul>
  </li>
  <li><code>normalize_int(input_data: Union[str, int, float, Decimal]) -> int</code>:
    <p><strong>Description</strong>: Normalizes data into an integer. Handles various input types (string, integer, float, Decimal).</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>input_data (str | int | float | Decimal)</code>: Input data (string, integer, float, or Decimal).</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>int</code>: Integer representation of the input.</li>
    </ul>
    <p><strong>Raises</strong>:</p>
    <ul>
      <li><code>ValueError</code>: If the input cannot be converted to an integer.</li>
      <li><code>TypeError</code>: If the input type is invalid.</li>
      <li><code>InvalidOperation</code>: For Decimal related errors.</li>
    </ul>
  </li>
    <li><code>normalize_float(value: Any) -> float | None</code>:
    <p><strong>Description</strong>: Converts input to float or a list of floats. Handles both single values and lists/tuples.  Includes error handling and logging for invalid conversions.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
        <li><code>value (Any)</code>: The input value to be converted (number, string, list, or tuple).</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
        <li><code>float | List[float] | None</code>: A float, list of floats, or None if the conversion fails.</li>
    </ul>
    <p><strong>Raises</strong>:</p>
    <ul>
        <li><code>ValueError</code>: If the input cannot be converted to a float.</li>
        <li><code>TypeError</code>: If the input type is invalid.</li>
    </ul>
  </li>
</ul>

<h2>Functions</h2>
<!-- No functions defined in the provided code -->

</html>