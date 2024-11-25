html
<h1>popup.js Documentation</h1>

<h2>Overview</h2>
<p>This JavaScript file manages the popup UI for the Try XPath extension. It handles user interactions, communication with the content script, and displaying results.</p>

<h2>Variables</h2>
<p>Defines various constants and variables used for managing the popup's state, data, and communication with the content script.  These include: tab IDs, execution IDs, frame IDs, result arrays, and more.</p>

<h2>Functions</h2>

<h3><code>sendToActiveTab</code></h3>

<p><strong>Description</strong>: Sends a message to the currently active tab.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>msg</code> (object): The message to be sent.</li>
  <li><code>opts</code> (object, optional): Optional parameters for the message (e.g., `frameId`). Defaults to an empty object.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Promise</code>: A promise that resolves with the response from the active tab, if any. Returns a rejected Promise if an error occurs during tab communication.</li>
</ul>

<h3><code>sendToSpecifiedFrame</code></h3>

<p><strong>Description</strong>: Sends a message to a specified frame in the active tab.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>msg</code> (object): The message to send.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Promise</code>: A Promise that resolves after the content scripts have been executed or if the frame is invalid.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Error</code>: An error occurs during the execution of the content script. Includes a descriptive message and frame ID for easier debugging.</li>
</ul>

<h3><code>collectPopupState</code></h3>

<p><strong>Description</strong>: Collects the current state of the popup's UI elements (checkbox, dropdown, inputs). Returns an object capturing this state.</p>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>object</code>: An object containing the current state of the UI elements.</li>
</ul>

<!-- ... (rest of the function and variable documentation) ... -->


<h3><code>showDetailsPage</code></h3>

<p><strong>Description</strong>: Displays a paginated list of results from the content script.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>index</code> (number): The index of the page to display.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Error</code>: Any error during result processing (e.g. if index is not a number).</li>
</ul>


<h3><code>showError</code></h3>

<p><strong>Description</strong>: Displays an error message in the popup, clearing any previous results.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>message</code> (string): The error message to display.</li>
  <li><code>frameId</code> (number): The frame ID associated with the error, for debugging.</li>
</ul>


<h3><code>genericListener</code></h3>

<p><strong>Description</strong>: A listener function for messages from the content script.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>message</code> (object): The message received.</li>
  <li><code>sender</code> (object): Sender information.</li>
  <li><code>sendResponse</code> (function): Function to respond to the message.</li>
</ul>
<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Error</code>: An error occurs during result processing.</li>
</ul>


<!-- ... (rest of the functions documentation) ... -->

<h2>Event Listeners</h2>

<p>The file defines numerous event listeners for UI elements (buttons, inputs, etc.).  These are handled by functions like <code>sendExecute</code>, <code>changeContextVisible</code>, etc.</p>



<h2>Initialization</h2>
<p>The <code>window.addEventListener("load", ...)</code> block initializes the variables, adds event listeners, and sets up communication with the content script and background script.  This includes retrieving the necessary UI elements, setting up initial display and error handling.</p>

```