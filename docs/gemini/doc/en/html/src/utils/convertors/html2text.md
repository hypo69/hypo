html
<h1>Module: hypotez/src/utils/convertors/html2text</h1>

<h2>Overview</h2>
<p>This module provides a function for converting HTML to Markdown-formatted text. It supports various features like entity handling, link and image formatting, emphasis, and list rendering. The module also includes options for customization, such as wrapping long lines, handling internal links, and defining different list styles.  It's designed for converting HTML content to plain text suitable for rendering in a markdown format, potentially for documentation or other use cases requiring text extraction from HTML.</p>

<h2>Functions</h2>

<h3><code>html2text_file</code></h3>

<p><strong>Description</strong>: Processes an HTML string and writes the converted markdown output to an output stream. Takes an HTML string, an optional output function, and a base URL as arguments.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>html</code> (str): The HTML string to be converted.</li>
  <li><code>out</code> (callable, optional): An output function to write the converted markdown to. Defaults to <code>wrapwrite</code>, which writes the output to standard output.</li>
  <li><code>baseurl</code> (str, optional): The base URL for relative links. Defaults to an empty string.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li>None: Returns nothing, but writes the converted text to the output stream.</li>
</ul>


<h3><code>html2text</code></h3>

<p><strong>Description</strong>: Converts an HTML string to Markdown-formatted text, handling various formatting and escaping issues, and potentially wrapping long lines for better readability.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>html</code> (str): The HTML string to be converted.</li>
  <li><code>baseurl</code> (str, optional): Base URL for relative links.  Defaults to an empty string.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li>str: The converted Markdown-formatted text.</li>
</ul>


<h3><code>replaceEntities</code></h3>
<p><strong>Description</strong>: Helper function for handling character references and entity references within HTML entities.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>s</code> (match): A regular expression match object containing the entity to be replaced.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li>str: The replaced entity. </li>
</ul>

<h3><code>unescape</code></h3>

<p><strong>Description</strong>: Function to unescape HTML entities.</p>
<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>s</code> (str): The HTML string to be unescaped.
  </li>
</ul>
<p><strong>Returns</strong>:</p>
<ul>
  <li>str: The unescaped string.</li>
</ul>

<!-- ... (Other functions and classes from the code) ... -->


<h2>Classes</h2>

<h3><code>_html2text</code></h3>

<p><strong>Description</strong>:  A class that extends the <code>HTMLParser</code> to handle HTML parsing and conversion to Markdown. Contains various methods for handling tags, attributes, entities, and formatting details.</p>


<p><strong>Methods (partial list)</strong>:</p>
<ul>
 <li><code>handle_starttag</code></li>
 <li><code>handle_endtag</code></li>
 <li><code>handle_charref</code></li>
 <li><code>handle_entityref</code></li>
 <li><code>handle_data</code></li>
 <li><code>handle_emphasis</code></li>
</ul>

<h2>Options (as set in the main block):</h2>
<p><code>options</code> is a <code>Storage</code> class instance containing configuration options for the conversion process, allowing for customization like using Google Docs specific formats or defining custom list item marks.</p>

<p>See the source code for a complete list of functions, classes and options.</p>