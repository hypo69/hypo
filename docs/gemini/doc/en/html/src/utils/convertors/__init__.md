html
<h1>Module convertors</h1>

<h2>Overview</h2>
<p>This module provides various conversion utilities for different data formats, including CSV, JSON, XML, HTML, and more.</p>

<h2>Constants</h2>

<h3><code>MODE</code></h3>

<p><strong>Description</strong>:  A string representing the current mode (e.g., 'dev').</p>


<h2>Modules</h2>

<h3><code>csv</code></h3>

<p><strong>Description</strong>:  Contains functions for converting CSV data.</p>

<p><strong>Functions</strong>:</p>
<ul>
  <li><code>csv2dict</code>: Converts CSV data to a dictionary.</li>
  <li><code>csv2ns</code>: Converts CSV data to a named sequence format.</li>
</ul>


<h3><code>dict</code></h3>

<p><strong>Description</strong>: Contains functions for converting dictionaries to various formats.</p>

<p><strong>Functions</strong>:</p>
<ul>
  <li><code>dict2ns</code>: Converts a dictionary to a named sequence format.</li>
  <li><code>dict2xls</code>: Converts a dictionary to an XLS format.</li>
  <li><code>dict2xml</code>: Converts a dictionary to an XML format.</li>
  <li><code>dict2csv</code>: Converts a dictionary to a CSV format.</li>
    <li><code>dict2html</code>: Converts a dictionary to an HTML format.</li>
</ul>


<h3><code>html</code></h3>

<p><strong>Description</strong>: Contains functions for manipulating HTML data.</p>

<p><strong>Functions</strong>:</p>
<ul>
  <li><code>html2escape</code>: Escapes HTML characters.</li>
  <li><code>html2ns</code>: Converts HTML data to a named sequence format.</li>
  <li><code>html2dict</code>: Converts HTML data to a dictionary.</li>
  <li><code>escape2html</code>: Converts escaped HTML characters back to HTML entities.</li>
</ul>


<h3><code>html2text</code></h3>

<p><strong>Description</strong>: Contains functions for converting HTML to plain text.</p>

<p><strong>Functions</strong>:</p>
<ul>
  <li><code>html2text</code>: Converts HTML to plain text.</li>
  <li><code>html2text_file</code>: Converts HTML from a file to plain text.</li>
  <li><code>google_fixed_width_font</code>: ...</li>
  <li><code>google_has_height</code>: ...</li>
  <li><code>google_list_style</code>: ...</li>
  <li><code>google_nest_count</code>: ...</li>
  <li><code>google_text_emphasis</code>: ...</li>
  <li><code>dumb_css_parser</code>: ...</li>
  <li><code>dumb_property_dict</code>: ...</li>
</ul>


<h3><code>json</code></h3>

<p><strong>Description</strong>: Contains functions for converting JSON data to various formats.</p>

<p><strong>Functions</strong>:</p>
<ul>
  <li><code>json2csv</code>: Converts JSON to CSV.</li>
  <li><code>json2ns</code>: Converts JSON to a named sequence format.</li>
  <li><code>json2xls</code>: Converts JSON to XLS format.</li>
  <li><code>json2xml</code>: Converts JSON to XML format.</li>
</ul>


<h3><code>ns</code></h3>

<p><strong>Description</strong>: Contains functions for working with named sequences (NS).</p>

<p><strong>Functions</strong>:</p>
<ul>
  <li><code>ns2csv</code>: Converts named sequence to CSV.</li>
  <li><code>ns2dict</code>: Converts named sequence to a dictionary.</li>
  <li><code>ns2json</code>: Converts named sequence to JSON.</li>
  <li><code>ns2xls</code>: Converts named sequence to XLS.</li>
  <li><code>ns2xml</code>: Converts named sequence to XML.</li>
</ul>


<h3><code>md2dict</code></h3>

<p><strong>Description</strong>: Contains functions for converting markdown to dictionaries.</p>

<p><strong>Functions</strong>:</p>
<ul>
  <li><code>md2dict</code>: Converts markdown to a dictionary.</li>
</ul>


<h3><code>xls</code></h3>

<p><strong>Description</strong>: Contains functions for converting XLS data.</p>

<p><strong>Functions</strong>:</p>
<ul>
  <li><code>xls2dict</code>: Converts XLS data to a dictionary.</li>
</ul>


<h3><code>xml2dict</code></h3>

<p><strong>Description</strong>: Contains functions for converting XML data to a dictionary.</p>

<p><strong>Functions</strong>:</p>
<ul>
  <li><code>xml2dict</code>: Converts XML data to a dictionary.</li>
</ul>


<h3><code>base64</code></h3>

<p><strong>Description</strong>: Contains functions related to Base64 encoding/decoding.</p>

<p><strong>Functions</strong>:</p>
<ul>
  <li><code>base64_to_tmpfile</code>: Converts base64 data to a temporary file.</li>
  <li><code>base64encode</code>: Encodes data to base64.</li>
</ul>


<h3><code>png</code></h3>

<p><strong>Description</strong>: Contains functions related to PNG image processing and generation.</p>

<p><strong>Classes/Functions</strong>:</p>
<ul>
  <li><code>TextToImageGenerator</code>: A class for generating text images.</li>
  <li><code>webp2png</code>: Converts WebP images to PNG.</li>
</ul>


<h3><code>tts</code></h3>

<p><strong>Description</strong>: Contains text-to-speech (TTS) related functions.</p>

<p><strong>Functions</strong>:</p>
<ul>
  <li><code>speech_recognizer</code>: ...</li>
  <li><code>text2speech</code>: ...</li>
</ul>


<h3><code>dot</code></h3>

<p><strong>Description</strong>: Contains a function for converting DOT (graph) files to PNG images.</p>

<p><strong>Functions</strong>:</p>
<ul>
  <li><code>dot2png</code>: Converts DOT file to a PNG image.</li>
</ul>