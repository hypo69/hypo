html
<h1>Module: hypotez/src/utils/string/html_escapes.py</h1>

<h2>Overview</h2>
<p>This module defines a dictionary mapping UTF-8 characters to their corresponding HTML entity escapes.  It provides a way to convert special characters to their HTML representation.</p>

<h2>Constants</h2>

<h3><code>MODE</code></h3>

<p><strong>Description</strong>: A constant representing the current mode (likely for development or production).</p>
<p><strong>Value</strong>: 'dev' </p>

<h3><code>html_escapes</code></h3>

<p><strong>Description</strong>: A dictionary containing UTF-8 characters and their corresponding HTML entity escapes. </p>

<p><strong>Data Structure</strong>:</p>

<p>A dictionary where keys are UTF-8 characters (strings) and values are their HTML entity escapes (strings). For example, '&' maps to '&amp;'.</p>

<p><strong>Example Usage</strong>:  To escape a character:  <code>html_escapes.get('&')</code> would return <code>'&amp;'</code>.</p>



<p><strong>Content Details</strong>:</p>
<p>The dictionary contains a large number of mappings, including various punctuation marks, accented characters, Greek letters, mathematical symbols, and more.</p>