html
<h1>Module: hypotez/src/utils/_examples/get_relative_path</h1>

<h2>Overview</h2>
<p>This module demonstrates the use of the <code>get_relative_path</code> function to obtain the relative path to a specific directory from a given file.</p>

<h2>Functions</h2>

<h3><code>get_relative_path</code></h3>

<p><strong>Description</strong>: Calculates the relative path from a given file path to a target directory.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>file_path</code> (<code>Path</code>): The path to the file from which the relative path is calculated.</li>
  <li><code>target_dir</code> (<code>str</code>): The target directory.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>str</code>: The relative path to the target directory from the given file path.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>ValueError</code>: If the target directory is not found or if the calculation fails.</li>
</ul>


<h3><code><a name="get_relative_path"></a>get_relative_path(file_path: Path, target_dir: str) -> str</code></h3>

<p><strong>Description</strong>: Calculates the relative path from a given file path to a target directory.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>file_path</code> (<code>Path</code>): The path to the file from which the relative path is calculated.</li>
  <li><code>target_dir</code> (<code>str</code>): The target directory.  Note: The input is expected to be a string representing the directory name, not a full path.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>str</code>: The relative path to the target directory from the given file path.</li>
</ul>


<p><strong>Raises</strong>:</p>
<ul>
  <li><code>ValueError</code>: If the target directory is not found or if the calculation fails.  This is a more specific and useful error message than just a generic exception.</li>
</ul>


<h2>Variables</h2>
<h3><code>MODE</code></h3>
<p><strong>Description</strong>:  A variable holding a string value, likely used for a mode identifier.</p>

<p><strong>Value</strong>:</p>
<p><code>'dev'</code></p>

<h3><code>relative_path</code></h3>
<p><strong>Description</strong>: The result of calling <code>get_relative_path</code> on <code>Path(__file__).resolve()</code> and 'hypotez'.</p>

<p><strong>Value</strong>:</p>

<p>The value of the variable will depend on the file system and the current working directory.</p>