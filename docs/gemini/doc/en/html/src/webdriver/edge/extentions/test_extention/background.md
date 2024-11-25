html
<h1>background.js</h1>

<h2>Overview</h2>
<p>This file contains the background script for a Chrome extension. It listens for messages from content scripts and, if a message indicates data collection, sends collected data to a server.</p>

<h2>Functions</h2>

<h3><code>sendDataToServer</code></h3>

<p><strong>Description</strong>: This function sends collected data to a specified server endpoint. It retrieves collected data from storage, constructs a POST request, and handles potential errors during the request.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>url</code> (string): The URL of the page from which the data needs to be collected.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li>None (implicitly): The function does not return a value.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Error</code>: If the server request fails (e.g., network issue, incorrect server response).</li>
</ul>


<h3><code>chrome.runtime.onMessage.addListener</code></h3>

<p><strong>Description</strong>: This function listens for messages sent from other parts of the extension (content scripts, other background scripts).  If the message indicates data collection, it calls <code>sendDataToServer()</code>.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>(message, sender, sendResponse)</code>:  Three parameters are passed when a message is received:
    <ul>
      <li><code>message</code> (object): The message sent by the sender.</li>
      <li><code>sender</code> (object): Information about the sender, such as its ID and whether it is a tab or another extension.</li>
      <li><code>sendResponse</code> (function): A function that can be used to send a response back to the sender, though not used in this case.</li>
    </ul>
  </li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>boolean</code>:  Returns `true` to indicate that the message handler function will potentially block the event loop (important for asynchronous operations). Otherwise return false.</li>
</ul>
<p><strong>Raises</strong>:</p>
<ul>
  <li>None explicitly. Error handling is done within the fetch call and sendDataToServer function.</li>
</ul>

<h3><code>chrome.browserAction.onClicked.addListener</code></h3>

<p><strong>Description</strong>: This function is a listener that executes a piece of code when the extension's icon/button is clicked.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>tab</code> (object): Information about the currently active tab, where data needs to be collected from.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li>None (implicitly): The function does not return a value.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li>None explicitly.</li>
</ul>