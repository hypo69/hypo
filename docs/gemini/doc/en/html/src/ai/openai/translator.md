html
<h1>Module translator</h1>

<h2>Overview</h2>
<p>This module provides a function for translating text using the OpenAI API.</p>

<h2>Global Variables</h2>

<h3><code>MODE</code></h3>

<p><strong>Description</strong>:  A global variable defining the current mode (e.g., 'dev', 'prod').</p>


<h2>Functions</h2>

<h3><code>translate</code></h3>

<p><strong>Description</strong>: Translates text using the OpenAI API.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>text</code> (str): The text to translate.</li>
  <li><code>source_language</code> (str): The language of the source text.</li>
  <li><code>target_language</code> (str): The language to translate to.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>str</code>: The translated text.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>:  Any exception raised during the OpenAI API call, including network issues or API errors.</li>
</ul>

<p><strong>Example Usage</strong>:</p>
<pre><code>python
>>> source_text = "Привет, как дела?"
>>> source_language = "Russian"
>>> target_language = "English"
>>> translation = translate(source_text, source_language, target_language)
>>> print(f"Translated text: {translation}")
</code></pre>