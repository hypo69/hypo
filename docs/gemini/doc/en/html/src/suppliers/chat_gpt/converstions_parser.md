html
<h1>converstions_parser.py</h1>

<h2>Overview</h2>
<p>This module provides a function for extracting conversation elements from an HTML file.</p>

<h2>Functions</h2>

<h3><code>extract_conversations_from_html</code></h3>

<p><strong>Description</strong>: A generator function that reads an HTML file and yields all the <code>&lt;div class="conversation"&gt;</code> elements.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>file_path</code> (Path): The path to the HTML file to process.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>conversation</code>: A BeautifulSoup <code>&lt;div&gt;</code> object representing a conversation.</li>
</ul>

<p><strong>Yields</strong>:</p>
<ul>
  <li><code>conversation</code> (bs4.element.Tag):  Each conversation found in the HTML file.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li>FileNotFoundError: Raised if the specified file path does not exist.</li>
  <li>UnicodeDecodeError: Raised if the file cannot be decoded using the specified encoding (UTF-8 in this case).</li>
</ul>


<p><strong>Example Usage:</strong></p>

<pre><code class="language-python">
file_path = Path(gs.path.data / 'chat_gpt' / 'chat.html')
for conversation in extract_conversations_from_html(file_path):
    print(conversation.prettify())
</code></pre>


</body>
</html>