```html
<!-- INSTRUCTION -->

<p>For each input Python file, create documentation in <code>HTML</code> format for subsequent use. The documentation must meet the following requirements:</p>

<ol>
  <li>
    <strong>Documentation Format</strong>:
    <ul>
      <li>Use the <code>HTML</code> standard.</li>
      <li>Each file should begin with a header and a brief description of its contents.</li>
      <li>For all classes and functions, use the following comment format:
        <pre><code>python
def function(param: str, param1: Optional[str | dict | str] = None) -> dict | None:
    """
    Args:
        param (str): Description of the `param` parameter.
        param1 (Optional[str | dict | str], optional): Description of the `param1` parameter. Defaults to `None`.

    Returns:
        dict | None: Description of the return value. Returns a dictionary or `None`.

    Raises:
        SomeError: Description of the situation in which the `SomeError` exception is raised.
    """
</code></pre>
      </li>
      <li>Use <code>ex</code> instead of <code>e</code> in exception handling blocks.</li>
    </ul>
  </li>

  <li>
    <strong>TOC (Table of Contents)</strong>:
    <ul>
      <li>Include a table of contents section at the beginning of each documentation file.</li>
      <li>The structure should include links to all major sections of the module documentation.</li>
    </ul>
  </li>

  <li>
    <strong>Documentation Formatting</strong>:
    <ul>
      <li>Use proper <code>HTML</code> syntax for all headers, lists, and links.</li>
      <li>For documenting classes, functions, and methods, include structured sections with descriptions, parameter details, return values, and raised exceptions. Example:
        <pre><code>html
<h2>Functions</h2>

<h3><code>function_name</code></h3>

<p><strong>Description</strong>: Brief description of the function.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>param</code> (str): Description of the `param` parameter.</li>
  <li><code>param1</code> (Optional[str | dict | str], optional): Description of the `param1` parameter. Defaults to `None`.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>dict | None</code>: Description of the return value.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>SomeError</code>: Description of the situation in which the `SomeError` exception is raised.</li>
</ul>
</code></pre>
      </li>
    </ul>
  </li>

  <li>
    <strong>Section Headings</strong>:
    <ul>
      <li>Use level 1 headers (<code>&lt;h1&gt;</code>), level 2 headers (<code>&lt;h2&gt;</code>), level 3 headers (<code>&lt;h3&gt;</code>), and level 4 headers (<code>&lt;h4&gt;</code>) consistently throughout the file.</li>
    </ul>
  </li>

  <li>
    <strong>Example File</strong>:
    <pre><code>html
<h1>Module Name</h1>

<h2>Overview</h2>
<p>Brief description of the module's purpose.</p>

<h2>Classes</h2>

<h3><code>ClassName</code></h3>

<p><strong>Description</strong>: Brief description of the class.</p>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>method_name</code>: Brief description of the method.</li>
</ul>

<h2>Functions</h2>

<h3><code>function_name</code></h3>

<p><strong>Description</strong>: Brief description of the function.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>param</code> (str): Description of the `param` parameter.</li>
  <li><code>param1</code> (Optional[str | dict | str], optional): Description of the `param1` parameter. Defaults to `None`.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>dict | None</code>: Description of the return value.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>SomeError</code>: Description of the situation in which the `SomeError` exception is raised.</li>
</ul>
</code></pre>
  </li>
</ol>

<p>Generate the corresponding documentation for each input Python file in <code>HTML</code> format.</p>
<h1>## Response format: `.md` (markdown)</h1>
<!-- END OF INSTRUCTION -->
```
