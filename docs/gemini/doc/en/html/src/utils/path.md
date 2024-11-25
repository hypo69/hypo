html
<h1>Module: hypotez/src/utils/path.py</h1>

<h2>Overview</h2>
<p>This module defines the root path to the project. All imports are built relative to this path.
    :platform: Windows, Unix
    :synopsis: Module determining the root path to the project. All imports are built relative to this path.
    :TODO: In the future, move to a system variable</p>

<h2>Variables</h2>

<h3><code>MODE</code></h3>

<p><strong>Description</strong>: A string variable representing the development mode.</p>


<h2>Functions</h2>

<h3><code>get_relative_path</code></h3>

<p><strong>Description</strong>: Returns the part of the path starting from the specified segment to the end.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>full_path</code> (str): The full path.</li>
  <li><code>relative_from</code> (str): The path segment from which extraction should begin.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Optional[str]</code>: The relative path starting from <code>relative_from</code>, or <code>None</code> if the segment is not found.</li>
</ul>