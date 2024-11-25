html
<h1>Module: hypotez/src/goog/spreadsheet/bberyakov/helpers.py</h1>

<h2>Overview</h2>
<p>This module provides functions for converting color formats.  It includes conversions between hexadecimal (HEX) and decimal representations, as well as converting HEX colors to RGB.</p>

<h2>Functions</h2>

<h3><code>hex_color_to_decimal</code></h3>

<p><strong>Description</strong>: Converts a hexadecimal color representation (e.g., "FF") to its decimal equivalent.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>letters</code> (str): The hexadecimal color code (e.g., "A", "AA").</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>int</code>: The decimal representation of the hexadecimal color.</li>
</ul>


<p><strong>Raises</strong>:</p>
<ul>
  <li>N/A</li>
</ul>


<h3><code>decimal_color_to_hex</code></h3>

<p><strong>Description</strong>: Converts a decimal number to its hexadecimal equivalent (e.g., 10 to A).</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>number</code> (int): The decimal number to convert.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>str</code>: The hexadecimal representation of the decimal number.</li>
</ul>


<p><strong>Raises</strong>:</p>
<ul>
  <li>N/A</li>
</ul>


<h3><code>hex_to_rgb</code></h3>

<p><strong>Description</strong>: Converts a hexadecimal color code to its RGB equivalent (e.g., "#FF0000" to (255, 0, 0)).</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>hex</code> (str): The hexadecimal color code (e.g., "#FFFFFF" or "FFFFFF").</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>tuple</code>: A tuple containing the RGB values (red, green, blue).</li>
</ul>


<p><strong>Raises</strong>:</p>
<ul>
  <li>N/A</li>
</ul>