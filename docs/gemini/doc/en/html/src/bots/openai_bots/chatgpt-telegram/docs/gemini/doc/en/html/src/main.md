html
<h1>Module: main.js</h1>

<h2>Overview</h2>
<p>This module defines a Telegram bot using the Telegraf library. It handles voice and text messages, transcribes voice messages using OpenAI, and sends the transcription to OpenAI's chat API for processing.  The bot then responds with the generated response.</p>

<h2>Variables</h2>

<h3><code>bot</code></h3>
<p><strong>Description</strong>: An instance of the Telegraf bot initialized with the TELEGRAM_TOKEN.</p>
<p><strong>Type</strong>: Telegraf</p>

<h2>Functions</h2>

<h3><code>start</code></h3>
<p><strong>Description</strong>: Handles the /start command and replies with the JSON representation of the received message.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>ctx</code> (object): The Telegraf context object containing the message details.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Promise</code>: Resolves when the message is replied.</li>
</ul>


<h3><code>processVoiceMessage</code></h3>
<p><strong>Description</strong>: Processes voice messages received from the user.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>ctx</code> (object): The Telegraf context object containing the message details.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Promise</code>: Resolves if the message is successfully processed.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Error</code>: If any error occurs during processing (e.g., file retrieval, transcription, or chat API call).</li>
</ul>


<h3><code>processTextMessage</code></h3>
<p><strong>Description</strong>: Processes text messages received from the user.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>ctx</code> (object): The Telegraf context object containing the message details.</li>
    <li><code>text</code> (string): The text content of the message.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Promise</code>: Resolves if the message is successfully processed.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Error</code>: If any error occurs during processing. Note the use of 'e' here instead of 'ex' as specified in the instruction.  The example in the instruction may contain a typo. </li>
</ul>


<h2>Initialization and Termination</h2>

<p>The script initializes a Telegraf bot, listens for voice and text messages, and terminates gracefully on SIGINT and SIGTERM signals.</p>