html
<h1>Module: cursor_spinner</h1>

<h2>Overview</h2>
<p>This module provides a utility to show a spinning cursor in the console to simulate a loading or waiting process.</p>

<h2>Functions</h2>

<h3><code>spinning_cursor</code></h3>

<p><strong>Description</strong>: Generator for a spinning cursor that cycles through |, /, -, \\ symbols.</p>

<p><strong>Yields</strong>:</p>
<ul>
  <li><code>str</code>: The next symbol in the cursor sequence.</li>
</ul>

<p><strong>Example</strong>:</p>
<pre><code class="language-python">
cursor = spinning_cursor()
next(cursor)  # '|'
next(cursor)  # '/'
next(cursor)  # '-'
next(cursor)  # '\\'
</code></pre>


<h3><code>show_spinner</code></h3>

<p><strong>Description</strong>: Shows a spinning cursor in the console for a specified duration.</p>

<p><strong>Args</strong>:</p>
<ul>
  <li><code>duration</code> (float): How long the spinner should run (in seconds). Defaults to 5.0.</li>
  <li><code>delay</code> (float): Delay between each spin (in seconds). Defaults to 0.1.</li>
</ul>

<p><strong>Example</strong>:</p>
<pre><code class="language-python">
show_spinner(duration=3.0, delay=0.2)  # Shows a spinner for 3 seconds
</code></pre>

<p><strong>Raises</strong>:  </p>
<ul>
  <li>None</li>
</ul>



<h2>Constants</h2>

<h3><code>MODE</code></h3>

<p><strong>Description</strong>:  Set to 'dev'</p>

<p><strong>Value</strong>:  'dev'</p>

<p><strong>Type</strong>:  str</p>