html
<h1>Module try_path_1.3.5 popup</h1>

<h2>Overview</h2>
<p>This module provides the JavaScript logic for the popup UI of the try-xpath extension. It handles user input, sends messages to the active tab or specified frame, manages result display, and provides interactive elements for navigating and interacting with the results.</p>

<h2>Functions</h2>

<h3><code>sendToActiveTab</code></h3>

<p><strong>Description</strong>: Sends a message to the currently active tab.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>msg</code> (Object): The message to be sent to the active tab.</li>
  <li><code>opts</code> (Object, optional): Options for the message. Defaults to an empty object.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Promise</code>: A Promise representing the result of sending the message.  Returns a Promise that resolves with the response from the tab.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Error</code>: An error could occur during the tab query or message sending process.</li>
</ul>


<h3><code>sendToSpecifiedFrame</code></h3>

<p><strong>Description</strong>: Sends a message to a specified frame within the active tab.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>msg</code> (Object): The message to be sent to the specified frame.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Promise</code>: A Promise that resolves when the message is sent and the frame has initialized or resolves with `undefined` if no frame id is provided.  Returns a Promise that resolves with the response from the specified frame.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Error</code>: An error might occur during the frame execution script or message sending process.</li>
</ul>


<h3><code>collectPopupState</code></h3>

<p><strong>Description</strong>: Collects the current state of the popup UI elements.</p>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Object</code>: An object containing the current state of the popup UI.</li>
</ul>


<h3><code>changeContextVisible</code></h3>

<p><strong>Description</strong>: Changes the visibility of the context section based on the checked state of the context checkbox.</p>

<p><strong>Parameters</strong>:</p>
<ul>
<li>None</li>
</ul>

<h3><code>changeResolverVisible</code></h3>
<h3><code>changeFrameIdVisible</code></h3>
<h3><code>changeFrameDesignationVisible</code></h3>
<h3><code>changeHelpVisible</code></h3>
<!-- ... (Other functions should be documented similarly) ... -->


<h3><code>makeExecuteMessage</code></h3>

<p><strong>Description</strong>: Creates a message object containing the user's input for the XPath execution.</p>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Object</code>: The message object.</li>
</ul>

<h3><code>getSpecifiedFrameId</code></h3>
<p><strong>Description</strong>: Retrieves the specified frame ID from the UI elements.</p>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Integer</code>: The frame ID. If the `frameIdCheckbox` is not checked returns 0</li>
</ul>

<h3><code>execContentScript</code></h3>

<p><strong>Description</strong>: Executes JavaScript scripts in the active tab and its frames to initialize the context for try-xpath operations.</p>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Promise</code>: A Promise that resolves when the content scripts have executed successfully.</li>
</ul>

<h3><code>sendExecute</code></h3>

<p><strong>Description</strong>: Sends the execute message to the active tab (or specified frame) to initiate the XPath evaluation.</p>

<h3><code>handleExprEnter</code></h3>

<p><strong>Description</strong>: Handles the Enter key press event for the main expression input, preventing default behavior and triggering the XPath execution when Enter key is pressed without shift key pressed.</p>
<!-- ... (Continue documenting functions) ... -->

<h2>Event Listeners</h2>

<p>This module uses various event listeners (e.g., on "load", "click", "keypress") to respond to user interactions.</p>

<!-- ... (Document other sections like variables and their descriptions, and event listeners similarly) ... -->