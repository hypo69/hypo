html
<h1>Module: CodeAssistant</h1>

<h2>Overview</h2>
<p>This module provides a class for interacting with various AI models, such as Google Gemini and OpenAI, for code processing tasks.</p>

<h2>Classes</h2>

<h3><code>CodeAssistant</code></h3>

<p><strong>Description</strong>: This class handles interactions with AI models for code analysis and documentation generation.</p>

<p><strong>Attributes</strong>:</p>
<ul>
  <li><code>role</code> (str): The role of the assistant (e.g., 'code_checker').</li>
  <li><code>lang</code> (str): The language for assistant operation (e.g., 'ru').</li>
  <li><code>model</code> (list): A list of AI models to use (e.g., ['gemini']).</li>
</ul>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>process_files(files: list, options: dict = {}) -> list | None</code>:
    <p><strong>Description</strong>: Processes a list of files using the configured AI models. Processes each file in the list and returns a list of processed data.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>files</code> (list): A list of file paths to process.</li>
      <li><code>options</code> (dict, optional): Additional parameters for configuring the process. Defaults to an empty dictionary.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>list | None</code>: A list of processed data or <code>None</code> if an error occurs.</li>
    </ul>
    <p><strong>Raises</strong>:</p>
    <ul>
      <li><code>FileNotFoundError</code>: If a file in the input list does not exist.</li>
	  <li><code>AIError</code>: An error during communication with the AI model.</li>
    </ul>
  </li>
</ul>

<h2>Functions</h2>
<!-- No functions defined in the input code -->

<h2>Exceptions</h2>

<h3><code>FileNotFoundError</code></h3>

<p><strong>Description</strong>: This exception is raised when a file specified in the input list is not found.</p>
<p><strong>Parameters</strong>:</p>
<ul>
 <li><code>file</code> (str): The path to the file that was not found.</li>
</ul>


<h3><code>AIError</code></h3>

<p><strong>Description</strong>: This exception is raised when there is an error during communication with the AI model.</p>
<p><strong>Parameters</strong>:</p>
<ul>
 <li><code>error_message</code> (str): Description of the error during communication with the AI model.</li>
</ul>