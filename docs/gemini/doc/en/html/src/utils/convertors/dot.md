html
<h1>Module: hypotez/src/utils/convertors/dot.py</h1>

<h2>Overview</h2>
<p>This module provides a function to convert DOT files to PNG images using the Graphviz library.</p>

<h2>Functions</h2>

<h3><code>dot2png</code></h3>

<p><strong>Description</strong>: Converts a DOT file to a PNG image.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>dot_file</code> (str): The path to the input DOT file.</li>
  <li><code>png_file</code> (str): The path where the output PNG file will be saved.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>None</code>: This function does not return a value; it saves the PNG image to the specified file.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>FileNotFoundError</code>: If the DOT file does not exist.</li>
  <li><code>Exception</code>: For other errors during conversion.</li>
</ul>

<p><strong>Example Usage</strong>:</p>
<pre><code>python
dot2png('example.dot', 'output.png')
</code></pre>
<p>This converts the DOT file 'example.dot' into a PNG image named 'output.png'.</p>
<p><strong>Sample DOT content (example.dot):</strong></p>
<pre><code class="language-dot">
digraph G {
    A -> B;
    B -> C;
    C -> A;
}
</code></pre>
<p><strong>Command-line usage:</strong></p>
<pre><code>bash
python dot2png.py example.dot output.png
</code></pre>
<p>This command will create a PNG file named 'output.png' from the graph defined in 'example.dot'.</p>


<h2>Main Execution Block</h2>

<p>This section contains the code that is executed when the script is run directly. </p>
<p><strong>Description</strong>: It checks if the correct number of command-line arguments is provided and then calls the <code>dot2png</code> function with the provided arguments.</p>
<p><strong>Usage:</strong></p>
<pre><code>bash
python dot2png.py <input_dot_file> <output_png_file>
</code></pre>