html
<h1>StringFormatter Module</h1>

<h2>Overview</h2>
<p>This module provides utility functions for formatting strings, including removing line breaks, HTML tags, non-Latin characters, and special characters.  It also offers functions for data transformation and URL cleaning.</p>

<h2>Classes</h2>

<h3><code>StringFormatter</code></h3>

<p><strong>Description</strong>: This class encapsulates string formatting utilities.</p>

<p><strong>Static Methods</strong>:</p>
<ul>
  <li><code>remove_line_breaks(input_str: str) -> str</code>:
    <p><strong>Description</strong>: Removes line breaks (\\n and \\r) from the input string.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>input_str</code> (str): The input string containing line breaks.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>str</code>: The input string with line breaks removed.</li>
    </ul>
  </li>
  <li><code>remove_htmls(input_html: str) -> str</code>:
    <p><strong>Description</strong>: Removes HTML tags from the input string.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>input_html</code> (str): The input string containing HTML tags.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>str</code>: The input string with HTML tags removed.</li>
    </ul>
  </li>
  <li><code>escape_html_tags(input_html: str) -> str</code>:
    <p><strong>Description</strong>: Escapes HTML tags &lt; and &gt; in the input string.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>input_html</code> (str): The input string containing HTML tags.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>str</code>: The input string with HTML tags escaped.</li>
    </ul>
  </li>
  <li><code>escape_to_html(text: str) -> str</code>:
    <p><strong>Description</strong>: Replaces characters with their HTML escape sequences.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>text</code> (str): The input string.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>str</code>: The input string with characters escaped to HTML format.</li>
    </ul>
  </li>
    <li><code>remove_non_latin_characters(input_str: str) -> str</code>:
    <p><strong>Description</strong>: Removes non-Latin characters from the input string.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>input_str</code> (str): The input string.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>str</code>: The input string with non-Latin characters removed.</li>
    </ul>
  </li>
  <li><code>remove_special_characters(input_str: str | list) -> str | list</code>:
    <p><strong>Description</strong>: Removes special characters from a string or list of strings.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>input_str</code> (str | list): The input string or list of strings.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>str | list</code>: The processed string or list with special characters removed.</li>
    </ul>
  </li>
  <li><code>clear_numbers(input_str: str) -> str</code>:
    <p><strong>Description</strong>: Clears the input string, leaving only decimal numbers and points.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>input_str</code> (str): The input string.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>str</code>: The cleared string containing only numbers and points.</li>
    </ul>
  </li>
</ul>
<h2>Functions</h2>
<!-- (Functions are listed here, following the same format as for class methods) -->
<!-- Add documentation for other functions as per the instruction. -->