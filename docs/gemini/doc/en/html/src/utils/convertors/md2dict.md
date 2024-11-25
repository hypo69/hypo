html
<h1>Module: md2dict</h1>

<h2>Overview</h2>
<p>This module provides a function for converting a Markdown string into a structured dictionary, including extraction of JSON content if present.</p>

<h2>Functions</h2>

<h3><code>md2dict</code></h3>

<p><strong>Description</strong>: Converts a Markdown string into a structured dictionary, extracting JSON content if present.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>md_string</code> (str): The Markdown string to convert.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Dict[str, dict | list]</code>: A structured representation of the Markdown content. Returns a dictionary with a "json" key if JSON content is found, otherwise a dictionary containing sections extracted from the markdown.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>: General exception during Markdown parsing or JSON extraction. Detailed error logged.</li>
</ul>

<h3><code>extract_json_from_string</code></h3>

<p><strong>Description</strong>: Extracts JSON content from a string if present.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>text</code> (str): The string to extract JSON content from.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>dict | None</code>: The extracted JSON content, or <code>None</code> if no JSON is found.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>: General exception during JSON extraction. Detailed error logged.</li>
</ul>