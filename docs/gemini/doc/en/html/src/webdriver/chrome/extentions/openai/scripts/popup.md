html
<h1>popup.js Documentation</h1>

<h2>Overview</h2>
<p>This JavaScript file initializes an Angular application for interacting with an OpenAI model through a backend API (likely FastAPI). It allows users to select an assistant and send messages to the model, receiving responses.</p>

<h2>Angular Module</h2>

<h3><code>openaiApp</code></h3>

<p><strong>Description</strong>: The Angular module responsible for the application structure.</p>

<h2>Controller</h2>

<h3><code>MainController</code></h3>

<p><strong>Description</strong>: Manages the user interface logic, including message input, response display, and assistant selection.</p>

<p><strong>Functions</strong>:</p>
<ul>
  <li><code>loadAssistants</code>: Retrieves a list of available assistants from a backend API (<code>http://localhost:8000/assistants</code>).</li>
  <li><code>sendMessage</code>: Sends a message to the OpenAI model via a POST request to the backend API (<code>http://localhost:8000/ask</code>). Includes the user's message, a system instruction, and the selected assistant's ID.</li>
</ul>

<h3><code>loadAssistants</code></h3>

<p><strong>Description</strong>: Fetches a list of assistants from the specified API endpoint.</p>

<p><strong>Parameters</strong>: None.</p>

<p><strong>Returns</strong>: None (updates the <code>$scope.assistants</code> variable).</p>

<p><strong>Raises</strong>:  (Assumed) Any errors related to the API request (e.g., network issues, incorrect API).  The <code>error</code> object is logged to the console.</p>


<h3><code>sendMessage</code></h3>

<p><strong>Description</strong>: Sends a message to the backend API.</p>

<p><strong>Parameters</strong>: None (implicitly handles data within the scope).</p>


<p><strong>Parameters (passed in data):</strong></p>
<ul>
  <li><code>message</code> (string): The user's input message.</li>
  <li><code>system_instruction</code> (string): Instructions given to the model. (Currently hardcoded).</li>
  <li><code>assistant_id</code> (number): The ID of the selected assistant.</li>
</ul>

<p><strong>Returns</strong>: None (updates the <code>$scope.response</code> variable).</p>

<p><strong>Raises</strong>:  (Assumed) Any errors related to the API request (e.g., network issues, incorrect API, invalid assistant ID). The <code>error</code> object is logged to the console, and a default error message is displayed to the user.</p>


<h2>Angular Scope Variables</h2>
<ul>
  <li><code>message</code>: Stores the user's input message.</li>
  <li><code>response</code>: Displays the response received from the OpenAI model.</li>
  <li><code>assistants</code>: An array containing assistant objects.</li>
  <li><code>selectedAssistant</code>: The currently selected assistant object.</li>
</ul>


<h2>Dependencies</h2>

<p>The code relies on the AngularJS library and the <code>$http</code> service for making HTTP requests.</p>