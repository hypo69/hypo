html
<h1>Module Documentation</h1>

<h2>Overview</h2>
<p>This module provides documentation generation functionality for Python code.</p>

<h2>Instructions</h2>
<p>This module contains instructions for generating Markdown documentation for Python code files.  These instructions detail the format and structure required for the generated documentation, including header levels, parameter descriptions, return values, and exception handling.</p>

<h2>Instructions Details</h2>
<p>The generated documentation must meet the following requirements:</p>
<ul>
<li><b>Documentation Format</b>:
    <ul>
    <li>Use Markdown (.md) standard.</li>
    <li>Each file begins with a header and a brief description of its contents.</li>
    <li>All classes and functions use the specified comment format for documentation:</li>
    </ul>
</li>

<li><b>Table of Contents (TOC)</b>:
    <ul>
        <li>Include a TOC section at the beginning of each documentation file.</li>
        <li>TOC includes links to all major sections of the module.</li>
    </ul>
</li>
<li><b>Formatting</b>:
    <ul>
        <li>Proper Markdown syntax for headers, lists, and links.</li>
        <li>Structured sections for classes, functions, and methods (description, parameters, return values, exceptions).</li>
    </ul>
</li>

<li><b>Section Headings</b>:
    <ul>
        <li>Use level 1 (#), level 2 (##), level 3 (###), and level 4 (####) headers consistently.</li>
    </ul>
</li>
</ul>

<h2>Example</h2>
<pre><code>
# Module Name

## Overview

Brief description of the module's purpose.

## Classes

### ClassName

**Description**: Brief description of the class.

**Methods**:
- method_name: Brief description of the method.

## Functions

### function_name

**Description**: Brief description of the function.

**Parameters**:
- param (str): Description of the `param` parameter.
- param1 (Optional[str | dict | str], optional): Description of the `param1` parameter. Defaults to `None`.

**Returns**:
- dict | None: Description of the return value.

**Raises**:
- SomeError: Description of the situation in which the `SomeError` exception is raised.
</code></pre>

<p>This example demonstrates the required format. The generated HTML must be able to be parsed and transformed into the example Markdown structure.</p>