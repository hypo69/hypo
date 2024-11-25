html
<h1>Module Documentation</h1>

<h2>Overview</h2>
<p>This module provides a framework for interacting with AI models for code processing tasks. It includes a <code>CodeAssistant</code> class for handling interactions with various AI engines like Google Gemini and OpenAI.</p>

<h2>Classes</h2>

<h3><code>CodeAssistant</code></h3>

<p><strong>Description</strong>: This class facilitates interactions with AI models for code analysis and documentation generation.</p>

<p><strong>Attributes</strong>:</p>
<ul>
  <li><code>role</code> (str): The role of the assistant (e.g., 'code_checker').</li>
  <li><code>lang</code> (str): The language the assistant will use (e.g., 'ru').</li>
  <li><code>model</code> (list): A list of AI models to use (e.g., ['gemini']).</li>
</ul>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>process_files</code>: Processes a list of files using the configured AI models.
    <ul>
      <li><strong>Description</strong>: This method analyzes and processes the provided files using the chosen AI models.  It should attempt to generate documentation for the files, handling exceptions during the process.</li>
      <li><strong>Parameters</strong>:
        <ul>
          <li><code>files</code> (list): A list of file paths to process.</li>
          <li><code>options</code> (dict, optional): Additional parameters for controlling the processing.  Defaults to an empty dictionary.</li>
        </ul>
      </li>
      <li><strong>Returns</strong>:
        <ul>
          <li><code>list</code>: A list of results from processing each file.  Returns an empty list if no files were given or if errors occur.</li>
        </ul>
      </li>
      <li><strong>Raises</strong>:
        <ul>
          <li><code>Exception</code>:  Any unexpected error during processing.</li>
        </ul>
      </li>
      <li><strong>Example Usage</strong>:
        <pre><code>python
assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
results = assistant.process_files(files=['file1.py', 'file2.py'], options={})
print(results)
</code></pre>
      </li>
    </ul>
  </li>
</ul>