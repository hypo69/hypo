html
<h1>Documentation for Python Code</h1>

<h2>Overview</h2>
<p>This document provides a template for generating HTML documentation from Python code.  It outlines the structure and content necessary for creating comprehensive and well-formatted documentation, including a table of contents.</p>

<h2>Instructions</h2>
<ol>
  <li><strong>Python Code Structure:</strong>  Each Python file should contain clear and concise comments in Markdown format, including descriptions of the module, classes, and functions.  The format should adhere to the detailed specification provided in the input prompt.</li>
  <li><strong>HTML Generation:</strong> This template will be used to transform Markdown comments into HTML.</li>
  <li><strong>Documentation Structure:</strong> The generated HTML documentation will include a table of contents, module description, class and function descriptions, including parameters, return values, and exceptions (with specific, descriptive explanations).  Exceptions should be documented separately.</li>
</ol>


<h2>Example Python Code Snippet</h2>

<pre><code class="language-python">
import logging

# Module-level description
def my_function(param1: int, param2: str = "default") -> str:
    """
    Args:
        param1 (int):  An integer parameter.
        param2 (str, optional): A string parameter. Defaults to "default".

    Returns:
        str: A string result.

    Raises:
        ValueError: If param1 is negative.
    """
    if param1 < 0:
        raise ValueError("Parameter 1 cannot be negative")

    logging.info(f"Executing function with param1: {param1} and param2: {param2}")
    return f"Result for {param1} and {param2}"
</code></pre>


<h2>Corresponding HTML Output (example)</h2>

<pre><code class="language-html">
<h1>my_module</h1>

<h2>Overview</h2>
<p>This module contains a function for demonstrating documentation generation.</p>

<h2>Functions</h2>

<h3><code>my_function</code></h3>

<p><strong>Description</strong>:  This function performs a calculation and returns a string.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>param1</code> (int): An integer parameter.</li>
  <li><code>param2</code> (str, optional): A string parameter. Defaults to "default".</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>str</code>: A string result.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>ValueError</code>: If <code>param1</code> is negative.</li>
</ul>
</code></pre>

<h2>Detailed Output Requirements (HTML)</h2>
<p>The exact HTML structure will follow the patterns exemplified above.  Critical components include:</p>
<ul>
    <li>Well-defined headers (h1, h2, h3, h4) for modules, classes, functions, and descriptions.</li>
    <li>Clear descriptions of parameters, return values, and potential exceptions.</li>
    <li>Consistent formatting for lists (ul, li) and code blocks (pre, code).</li>
    <li>A proper table of contents for navigating the documentation.</li>
</ul>

<p>Crucially, the output HTML must be in a format suitable for rendering, adhering to web standards.</p>