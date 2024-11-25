html
<h1>Module: hypotez/src/utils/printer.py</h1>

<h2>Overview</h2>
<p>This module provides functions for pretty printing data with optional text styling, including color, background, and font styles. It handles various data types like dictionaries, lists, strings, and file paths, offering enhanced output formatting.</p>

<h2>Constants</h2>

<h3><code>MODE</code></h3>
<p><strong>Description</strong>: A constant representing the current mode.  Currently set to 'dev'.</p>


<h3><code>RESET</code></h3>
<p><strong>Description</strong>: An ANSI escape code for resetting text formatting.</p>

<h3><code>TEXT_COLORS</code></h3>
<p><strong>Description</strong>: A dictionary mapping text color names (e.g., "red", "green") to their corresponding ANSI escape codes.  Used for coloring text output.</p>

<h3><code>BG_COLORS</code></h3>
<p><strong>Description</strong>: A dictionary mapping background color names to their ANSI escape codes. Used for setting background colors for text.</p>

<h3><code>FONT_STYLES</code></h3>
<p><strong>Description</strong>: A dictionary mapping font style names (e.g., "bold", "underline") to their ANSI escape codes. Used for styling the text output.</p>

<h2>Functions</h2>

<h3><code>_color_text</code></h3>

<p><strong>Description</strong>: Applies color, background, and font styling to a given text string using ANSI escape codes.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>text</code> (str): The text string to be styled.</li>
  <li><code>text_color</code> (str, optional): The text color to apply. Defaults to "". See <code>TEXT_COLORS</code> for valid options.</li>
  <li><code>bg_color</code> (str, optional): The background color to apply. Defaults to "". See <code>BG_COLORS</code> for valid options.</li>
  <li><code>font_style</code> (str, optional): The font style to apply. Defaults to "". See <code>FONT_STYLES</code> for valid options.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li>str: The styled text string.</li>
</ul>

<p><strong>Example Usage (in documentation):</strong></p>
<pre><code>>>> _color_text("Hello, World!", text_color="green", font_style="bold")
'\033[1m\033[32mHello, World!\033[0m'
</code></pre>


<h3><code>pprint</code></h3>

<p><strong>Description</strong>: Pretty prints the given data with optional color, background, and font styling.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>print_data</code> (Any, optional): The data to print. Can be <code>None</code>, <code>dict</code>, <code>list</code>, <code>str</code>, or <code>Path</code>.  If <code>Path</code>, it must point to a file. </li>
  <li><code>text_color</code> (str, optional): The text color to apply. Defaults to "white". See <code>TEXT_COLORS</code> for valid options.</li>
  <li><code>bg_color</code> (str, optional): The background color to apply. Defaults to "". See <code>BG_COLORS</code> for valid options.</li>
  <li><code>font_style</code> (str, optional): The font style to apply. Defaults to "". See <code>FONT_STYLES</code> for valid options.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li>None</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>: If the input data type is unsupported or an error occurs during formatting or printing.</li>
</ul>

<p><strong>Example Usage (in documentation):</strong></p>
<pre><code>>>> pprint({"name": "Alice", "age": 30}, text_color="green")
\033[32m{
    "name": "Alice",
    "age": 30
}\033[0m
</code></pre>


<h2>Imports</h2>
<p>This section lists the external modules used in the `printer.py` module.</p>
<ul>
<li><code>json</code></li>
<li><code>csv</code></li>
<li><code>pandas as pd</code></li>
<li><code>pathlib</code></li>
<li><code>typing</code></li>
<li><code>pprint</code></li>
</ul>