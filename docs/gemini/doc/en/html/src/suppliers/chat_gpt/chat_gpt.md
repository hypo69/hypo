html
<h1>Module chat_gpt</h1>

<h2>Overview</h2>
<p>This module contains the <code>ChatGpt</code> class for handling conversations, likely related to a Chat GPT integration.</p>

<h2>Constants</h2>

<h3><code>MODE</code></h3>

<p><strong>Description</strong>: Defines the operation mode (likely 'dev').</p>
<p><strong>Value</strong>: <code>'dev'</code></p>

<h2>Classes</h2>

<h3><code>ChatGpt</code></h3>

<p><strong>Description</strong>: A class for managing and potentially processing chat conversations, likely related to Chat GPT.</p>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>yeld_conversations_htmls</code>: Generates HTML representations of chat conversations.</li>
</ul>

<h2>Functions</h2>

(No functions are defined in the provided snippet)


<h2>Method Details</h2>

<h3><code>ChatGpt.yeld_conversations_htmls</code></h3>

<p><strong>Description</strong>: Yields HTML representations of chat conversations found in a directory.</p>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>str</code>: A string containing the HTML representation of the conversation (not fully defined in the snippet). </li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li>Potential `FileNotFoundError` or other exceptions related to file I/O if the specified file or directory is not found.</li>
</ul>


<p><strong>Implementation Notes:</strong> This method likely reads HTML files from the <code>gs.path.data / 'chat_gpt' / 'conversations'</code> directory and constructs some sort of output string from them.  The 'yeld' in the name suggests it might use a generator.</p>


<p><strong>Parameters:</strong> (None explicitly declared, but the presence of <code>self</code> and the use of <code>gs.path.data</code> imply internal parameters):</p>
<ul>
 <li>Implied parameters related to file operations and potentially conversation data.</li>
</ul>


<p><strong>Example Usage (Hypothetical):</strong></p>
<pre><code>
import src.suppliers.chat_gpt.chat_gpt as chatgpt
# ... (initialize chatgpt object)
for conversation_html in chatgpt.yeld_conversations_htmls():
  # ... (process each conversation_html string)
</code></pre>