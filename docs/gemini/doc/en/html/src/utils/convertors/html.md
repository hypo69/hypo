html
<h1>Module: hypotez/src/utils/convertors/html</h1>

<h2>Overview</h2>
<p>This module provides utilities for converting HTML to various formats, including escape sequences, dictionaries, and SimpleNamespace objects. It also includes a function for converting HTML to PDF using WeasyPrint.</p>

<h2>Functions</h2>

<h3><code>html2escape</code></h3>

<p><strong>Description</strong>: Converts HTML tags to escape sequences.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>input_str</code> (str): The HTML string to convert.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>str</code>: The HTML string with tags converted to escape sequences.</li>
</ul>

<p><strong>Example</strong>:</p>
<pre><code class="language-python">html = "<p>Hello, world!</p>"
result = html2escape(html)
print(result)  # Output: &lt;p&gt;Hello, world!&lt;/p&gt;
</code></pre>


<h3><code>escape2html</code></h3>

<p><strong>Description</strong>: Converts escape sequences back to HTML tags.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>input_str</code> (str): The string containing escape sequences.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>str</code>: The HTML string with escape sequences converted.</li>
</ul>

<p><strong>Example</strong>:</p>
<pre><code class="language-python">escaped = "&lt;p&gt;Hello, world!&lt;/p&gt;"
result = escape2html(escaped)
print(result)  # Output: &lt;p&gt;Hello, world!&lt;/p&gt;
</code></pre>


<h3><code>html2dict</code></h3>

<p><strong>Description</strong>: Converts HTML to a dictionary where tags are keys and content is values.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>html_str</code> (str): The HTML string to convert.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>dict</code>: A dictionary where keys are HTML tags and values are their content.</li>
</ul>

<p><strong>Example</strong>:</p>
<pre><code class="language-python">html = "<p>Hello</p><a href='link'>World</a>"
result = html2dict(html)
print(result)  # Output: {'p': 'Hello', 'a': 'World'}
</code></pre>


<h3><code>html2ns</code></h3>

<p><strong>Description</strong>: Converts HTML to a SimpleNamespace object.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>html_str</code> (str): The HTML string to convert.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>SimpleNamespace</code>: A SimpleNamespace object where HTML tags are attributes.</li>
</ul>

<p><strong>Example</strong>:</p>
<pre><code class="language-python">html = "<p>Hello</p><a href='link'>World</a>"
result = html2ns(html)
print(result.p)  # Output: Hello
print(result.a)  # Output: World
</code></pre>


<h3><code>html2pdf</code></h3>

<p><strong>Description</strong>: Converts HTML to PDF using WeasyPrint.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>html_str</code> (str): The HTML string to convert.</li>
  <li><code>pdf_file</code> (str | Path): The path to the output PDF file.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>bool | None</code>: <code>True</code> if successful, <code>None</code> otherwise.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>: If an error occurs during PDF generation.</li>
</ul>


<p><strong>Note</strong>:  The original `html2pdf` function using `xhtml2pdf` was commented out and replaced by a simpler example using WeasyPrint. This should be more reliable and robust.</p>