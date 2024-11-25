html
<h1>popup.js</h1>

<h2>Overview</h2>
<p>This JavaScript file handles the logic for the Chrome extension popup.  It allows the user to send the active tab's URL to a backend service.</p>

<h2>Functions</h2>

<h3><code>addEventListener</code></h3>

<p><strong>Description</strong>: This function attaches an event listener to the element with the ID "sendUrlButton".  When the button is clicked, it triggers the action defined in the event handler.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>"click"</code> (string): The event type to listen for.</li>
  <li><code>() => { ... }</code> (function): The event handler function.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li>None</li>
</ul>



<h3><code>alert</code></h3>

<p><strong>Description</strong>: Displays an alert dialog box with the specified message.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>"Hello, world!"</code> (string): The message to display in the alert box.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li>None</li>
</ul>

<h3><code>chrome.tabs.query</code></h3>

<p><strong>Description</strong>: Queries for tabs matching the specified criteria.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>{ active: true, currentWindow: true }</code> (object): The criteria to match.</li>
  <li><code>(tabs) => { ... }</code> (function): The callback function that will be executed with the matching tabs. </li>
</ul>


<p><strong>Returns</strong>:</p>
<ul>
<li><code>tabs</code>: (array of tab objects): An array containing the matched tabs.</li>
</ul>


<p><strong>Raises</strong>:</p>
<ul>
  <li>None</li>
</ul>




<h3><code>chrome.runtime.sendMessage</code></h3>

<p><strong>Description</strong>: Sends a message to another part of the extension or to a background script.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>{ action: "sendUrl", url: activeTabUrl }</code> (object): The message to send. Contains the action and the active tab URL.</li>
  <li><code>(response) => { ... }</code> (function): The callback function that will be executed when a response is received. </li>
</ul>



<p><strong>Returns</strong>:</p>
<ul>
<li><code>response</code> (object): The response received from the message handler.</li>
</ul>


<p><strong>Raises</strong>:</p>
<ul>
  <li>None</li>
</ul>