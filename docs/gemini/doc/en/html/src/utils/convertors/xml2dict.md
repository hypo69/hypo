html
<h1>Module: xml2dict</h1>

<h2>Overview</h2>
<p>This module provides utilities for converting XML data into dictionaries. It includes functions for parsing XML strings and converting XML element trees into dictionary representations.</p>

<h2>Functions</h2>

<h3><code>_parse_node</code></h3>

<p><strong>Description</strong>: Parses an XML node into a dictionary.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>node</code> (<code>ET.Element</code>): The XML element to parse.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>dict | str</code>: A dictionary representation of the XML node, or a string if the node has no attributes or children.</li>
</ul>


<h3><code>_make_dict</code></h3>

<p><strong>Description</strong>: Generates a dictionary with the tag name and value.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>tag</code> (<code>str</code>): The tag name of the XML element.</li>
  <li><code>value</code> (<code>any</code>): The value associated with the tag.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>dict</code>: A dictionary with the tag name as the key and the value as the dictionary value.</li>
</ul>


<h3><code>xml2dict</code></h3>

<p><strong>Description</strong>: Parses an XML string into a dictionary.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>xml</code> (<code>str</code>): The XML string to parse.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>dict</code>: The dictionary representation of the XML.</li>
</ul>


<h3><code>ET2dict</code></h3>

<p><strong>Description</strong>: Converts an XML element tree into a dictionary.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>element_tree</code> (<code>ET.Element</code>): The XML element tree.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>dict</code>: The dictionary representation of the XML element tree.</li>
</ul>