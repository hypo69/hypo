html
<h1>Module Documentation</h1>

<h2>Overview</h2>
<p>This document provides documentation for an advanced Python code analyzer that processes and documents code using the reStructuredText (RST) format.  It aims to improve code quality by adding comments, correcting formatting, and handling different input types (Python, Markdown, RST, JSON).  Specific rules for comment format, spacing, configuration loading, and handling existing comments are enforced.</p>

<h2>Detailed Requirements</h2>

<h3>Comment Format</h3>
<p>Comments should use the reStructuredText (RST) format, including :param, :type, :returns, :rtype, and :raises directives for function, method, and class documentation.  Single quotes (') must be used for string literals in Python code within the comments. </p>

<h3>Spacing Around Assignment Operator</h3>
<p>Always use spaces around the assignment operator (=) in Python code for better readability. This applies to all assignment statements, including function parameters, lists, dictionaries, and tuples.</p>

<h3>Loading Configurations Using <code>j_loads</code> and <code>j_loads_ns</code></h3>
<p>Use the <code>j_loads</code> and <code>j_loads_ns</code> functions for loading data from JSON files.  These functions provide better error handling.  If loading fails, use <code>logger.error</code> to log the issue and handle the error appropriately.</p>

<h3>Preserving Existing Comments</h3>
<p>Do not modify or delete existing comments starting with #.  If a comment is redundant or unnecessary, leave it, but document the change in the "Changes" section.</p>


<h3>Handling Various Input Types</h3>
<p>Supports Python code, Markdown files, RST files, and JSON/dictionaries.  Python code is analyzed for functions, methods, and classes, and RST/Markdown files are checked for formatting and structure. JSON/dictionaries are returned unchanged.  The improved code adheres to best practices for the file type.</p>

<h3>Analyzing Project Structure</h3>
<p>Considers file paths, imports, and consistency of function/variable names. Missing imports are considered and added if necessary, based on existing files in the project.</p>


<h3>Response Template</h3>
<p>The response follows a consistent format: "Received Code," "Improved Code," and "Changes," ensuring clear presentation of the original code, the modifications made, and a detailed list of changes.</p>


<h3>Handling <code>...</code></h3>
<p>Preserves the <code>...</code>  marker as a placeholder for code that is not yet implemented.  Empty lines or comments that do not contain specific documentation requirements are excluded from the generated documentation.</p>