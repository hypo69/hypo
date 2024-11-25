html
<h1>Code Assistant: Training the Project Code Model</h1>

<h2>Overview</h2>
<p><code>Code Assistant</code> is a tool for interacting with **Gemini** and **OpenAI** models to process source code. It performs tasks such as generating documentation, checking code, and generating tests based on the code from specified files.</p>

<h2>Main Capabilities</h2>
<ul>
  <li><strong>Reading Source Files</strong>: Reads code from files with extensions <code>.py</code> and <code>README.MD</code> from the specified directories.</li>
  <li><strong>Processing with Models</strong>: Sends code to models to perform tasks like generating documentation or checking for errors.</li>
  <li><strong>Generating Results</strong>: Model responses are saved to specified directories for each role.</li>
</ul>

<h2>Project Structure</h2>
<ul>
  <li><strong>Models</strong>: Uses **Gemini** and **OpenAI** models for processing requests.</li>
  <li><strong>Prompts</strong>: The program reads prompts from files in the <code>src/ai/prompts/developer/</code> directory (e.g., <code>doc_writer_en.md</code>).</li>
  <li><strong>Files</strong>: Processes files with extensions <code>.py</code> and <code>README.MD</code> in specified starting directories.</li>
</ul>

<h2>Example Usage</h2>

<h3>Running with Settings from JSON</h3>
<pre><code>bash
python assistant.py --settings settings.json
</code></pre>

<h3>Running with Explicit Parameters</h3>
<pre><code>bash
python assistant.py --role doc_writer --lang ru --models gemini openai --start_dirs /path/to/dir1 /path/to/dir2
</code></pre>

<h3>Example for Role <code>code_checker</code></h3>
<pre><code>bash
python assistant.py --role code_checker --lang en --models gemini --start_dirs /path/to/dir
</code></pre>

<h3>Example for Model <code>openai</code></h3>
<pre><code>bash
python assistant.py --role doc_writer --lang en --models openai
</code></pre>

<h2>Command-Line Parameters</h2>
<ul>
  <li><code>--settings</code>: Path to the JSON file with settings. Loads parameters from the file.</li>
  <li><code>--role</code>: Model role for task execution (e.g., <code>doc_writer</code>, <code>code_checker</code>).</li>
  <li><code>--lang</code>: Language for task execution (e.g., <code>ru</code> or <code>en</code>).</li>
  <li><code>--models</code>: List of models for initialization (e.g., <code>gemini</code>, <code>openai</code>).</li>
  <li><code>--start_dirs</code>: List of directories for processing (e.g., <code>/path/to/dir1</code>).</li>
</ul>

<h2>Functionality</h2>
<ol>
  <li><strong>Reading Files</strong>: Locates files with <code>.py</code> and <code>README.MD</code> extensions in the specified starting directories.</li>
  <li><strong>Loading Prompts</strong>: Loads prompt files for each role and language from the <code>src/ai/prompts/developer/</code> directory.</li>
  <li><strong>Processing Requests</strong>: Forms requests based on loaded files and sends them to models.</li>
  <li><strong>Saving Responses</strong>: Saves responses from models to directories corresponding to the role and model (e.g., <code>docs/raw_rst_from_<model>/<lang>/</code>).</li>
</ol>

<h2>Exceptions</h2>
<p>Configuration of exceptions for files and directories using parameters:</p>
<ul>
  <li><code>exclude_file_patterns</code>: List of regular expressions to exclude files.</li>
  <li><code>exclude_dirs</code>: List of directories to exclude.</li>
  <li><code>exclude_files</code>: List of files to exclude.</li>
</ul>

<h2>Logging</h2>
<p>Logs are saved using the <code>logger</code> library and contain information about the file processing process and the received responses.</p>

<h2>Dependencies</h2>
<ul>
  <li><strong>Gemini API</strong>: Requires an API key for working with the Gemini model.</li>
  <li><strong>OpenAI API</strong>: Requires an API key for working with the OpenAI model.</li>
</ul>