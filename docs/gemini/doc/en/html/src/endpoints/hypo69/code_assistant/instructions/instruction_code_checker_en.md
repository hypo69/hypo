html
<!--
  INSTRUCTION:
  Generate HTML documentation for Python files based on the provided instructions.
-->
<h1>Documentation Generator</h1>

<p>This tool generates HTML documentation for Python files, adhering to specified formatting rules.</p>

<ul>
  <li><b>Documentation Format:</b> Uses HTML standard, includes header, brief description, and standardized function/class comments.</li>
  <li><b>TOC:</b>  Generates a Table of Contents (TOC) linking to major sections of the module.</li>
  <li><b>Formatting:</b> Uses proper HTML for headers, lists, and links. Includes structured sections for classes, functions, and methods (description, parameters, returns, exceptions).</li>
  <li><b>Section Headings:</b> Consistent use of h1, h2, h3, and h4 headers.</li>
  <li><b>Example File Structure:</b> Follows a predefined structure for presenting documentation.</li>
  <li><b>Preserves Comments:</b> All existing comments are preserved, with additional restructured text style comments added where necessary.</li>
  <li><b>Error Handling:</b> Uses <code>logger.error</code> for better exception handling.</li>
  <li><b>Data Handling:</b> Uses <code>j_loads</code>/<code>j_loads_ns</code> for JSON handling.</li>
</ul>

<p>To generate documentation, provide the Python code as input.  The output will be the corresponding HTML formated documentation.</p>

<!-- Example Usage -->
<div>
    <p><b>Example Input (Python Code)</b></p>
    <pre><code>python
import json
from typing import Optional

def my_function(param: str, param1: Optional[str] = None) -> dict:
    """
    Description of my_function
    :param param: Parameter description.
    :param param1: Optional parameter description.
    :return: Return value description.
    """
    # Function logic here
    return {'result': param}
</code></pre>
</div>

<div>
    <p><b>Corresponding Output (HTML Fragment)</b></p>
    <pre><code>html
<h1>Module Name</h1>

<h2>Overview</h2>
<p>Brief description of the module.</p>

<h2>Functions</h2>

<h3><code>my_function</code></h3>

<p><strong>Description</strong>: Description of my_function</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>param</code> (str): Parameter description.</li>
  <li><code>param1</code> (Optional[str], optional): Optional parameter description. Defaults to None.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>dict</code>: Return value description.</li>
</ul>
</code></pre>
</div>

</html>