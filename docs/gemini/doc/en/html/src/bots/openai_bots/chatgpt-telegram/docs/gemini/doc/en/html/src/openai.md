html
<h1>openai.js</h1>

<h2>Overview</h2>
<p>This module provides a wrapper around the OpenAI API for interacting with various models, including chat and transcription.</p>

<h2>Classes</h2>

<h3><code>OpenAI</code></h3>

<p><strong>Description</strong>: A class for interacting with the OpenAI API.</p>

<p><strong>Properties</strong>:</p>
<ul>
  <li><code>roles</code> (object): An object containing predefined roles for messages.</li>
</ul>

<p><strong>Constructor</strong>:</p>

<h3><code>constructor(apiKey)</code></h3>

<p><strong>Description</strong>: Initializes an instance of the OpenAI class.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>apiKey</code> (string): The API key for the OpenAI API.</li>
</ul>

<p><strong>Methods</strong>:</p>

<h3><code>chat(messages)</code></h3>

<p><strong>Description</strong>: Sends a chat message to the OpenAI API.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>messages</code> (array): An array of messages to send to the model.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>object | undefined</code>: The response from the OpenAI API, or <code>undefined</code> if an error occurs.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Error</code>: Any error encountered during the API call.</li>
</ul>


<h3><code>transcription(filepath)</code></h3>

<p><strong>Description</strong>: Transcribes audio from a file using the OpenAI Whisper model.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>filepath</code> (string): The path to the audio file.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>string | undefined</code>: The transcribed text, or <code>undefined</code> if an error occurs.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Error</code>: Any error encountered during the API call.</li>
</ul>


<h2>Constants</h2>

<h3><code>openai</code></h3>

<p><strong>Description</strong>: A pre-configured instance of the <code>OpenAI</code> class using the API key from the <code>config</code> module.</p>