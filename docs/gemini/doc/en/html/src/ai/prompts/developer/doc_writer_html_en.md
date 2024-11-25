html
<h1>Module Documentation</h1>

<h2>Overview</h2>
<p>This module contains the <code>CodeAssistant</code> class, used for interacting with AI models (like Google Gemini and OpenAI) for code processing tasks.</p>

<h2>Classes</h2>

<h3><code>CodeAssistant</code></h3>

<p><strong>Description</strong>: The <code>CodeAssistant</code> class interacts with various AI models for code analysis and documentation generation.</p>

<p><strong>Attributes</strong>:</p>
<ul>
  <li><code>role</code> (str): The role of the assistant (e.g., 'code_checker').</li>
  <li><code>lang</code> (str): The language the assistant will use (e.g., 'ru').</li>
  <li><code>model</code> (list): List of AI models used (e.g., ['gemini']).</li>
</ul>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>process_files</code>:  A method for processing code files.</li>
</ul>

<p><strong>Detailed Description</strong>: The <code>CodeAssistant</code> class is responsible for interacting with AI models.  It's designed to handle tasks like analyzing code, generating documentation, or other code-related processing.</p>


<p><strong>Example Usage</strong>:</p>
<pre><code class="language-python">assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
assistant.process_files()
</code></pre>


<h3><code>process_files</code></h3>

<p><strong>Description</strong>: This method processes a list of files using an AI model for analysis and documentation generation.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>files</code> (list of str): A list of file paths to process.</li>
  <li><code>options</code> (dict, optional): Additional parameters for configuration (e.g., specific AI model parameters). Defaults to an empty dictionary.</li>
</ul>


<p><strong>Return Value</strong>:</p>
<ul>
  <li><code>list</code>: A list of results from the processed files.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>FileNotFoundError</code>: If a file in the input list does not exist.</li>
  <li><code>Exception</code>: For other unexpected errors during processing.</li>
</ul>

<p><strong>Example Usage</strong>:</p>
<pre><code class="language-python">assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
result = assistant.process_files(files=['file1.py', 'file2.py'], options={})
print(result)
</code></pre>


<h2>Functions</h2>

<!-- No functions found in the provided input code -->


<h2>Exceptions</h2>

<!-- No exceptions found in the provided input code -->