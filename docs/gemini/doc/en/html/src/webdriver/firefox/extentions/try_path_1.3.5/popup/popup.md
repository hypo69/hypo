html
<h1>try_path_1.3.5 Popup Script Documentation</h1>

<h2>Overview</h2>
<p>This JavaScript file, <code>popup.js</code>, manages the user interface and communication with the content script for the Try XPath extension. It handles user inputs, sends messages to the active tab for XPath evaluation, displays results, and allows navigation through results.</p>

<h2>Functions</h2>

<h3><code>sendToActiveTab</code></h3>

<p><strong>Description</strong>: Sends a message to the currently active tab.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>msg</code> (object): The message to be sent.</li>
  <li><code>opts</code> (object, optional): Optional message options. Defaults to an empty object.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Promise</code>: A promise that resolves with the response from the content script if available; otherwise, it potentially throws an error.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Error</code>: If there's an issue with communication to the active tab.</li>
</ul>


<h3><code>sendToSpecifiedFrame</code></h3>

<p><strong>Description</strong>: Executes a content script within a specified frame.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>msg</code> (object): The message to send to the specified frame.</li>
</ul>


<p><strong>Returns</strong>:</p>
<ul>
 <li><code>Promise</code>: A promise that resolves with the response from the frame if available; otherwise, it potentially throws an error.</li>
</ul>


<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Error</code>: If the frameId is invalid or communication fails.</li>
</ul>


<h3><code>collectPopupState</code></h3>

<p><strong>Description</strong>: Collects the current state of the popup elements.</p>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>object</code>: An object containing the current state of the popup elements (e.g., checkbox states, input values, etc.).</li>
</ul>


<h3><code>changeContextVisible</code></h3>
<p><strong>Description</strong>: Modifies the visibility of the context section based on the checkbox state.</p>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>null</code>: Takes no parameters.</li>
</ul>
<p><strong>Returns</strong>:</p>
<ul>
<li><code>null</code>: Returns nothing, but changes the visibility of elements in the UI</li>
</ul>

<h3><code>changeResolverVisible</code></h3>
<h3><code>changeFrameIdVisible</code></h3>
<h3><code>changeFrameDesignationVisible</code></h3>
<h3><code>changeHelpVisible</code></h3>
<p>(Similar structure to changeContextVisible, but for different sections/elements)</p>


<h3><code>makeExecuteMessage</code></h3>

<p><strong>Description</strong>: Creates a message object containing user-provided XPath expressions for execution in the content script.</p>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>object</code>: A message object with the XPath expressions and other parameters.</li>
</ul>

<h3><code>getSpecifiedFrameId</code></h3>
<p><strong>Description</strong>: Retrieves the ID of the frame to target, handling manual input if the user has chosen a specific frame.</p>
<p><strong>Returns</strong>:</p>
<ul>
<li><code>integer</code>: returns the frame ID to target, or 0 if no frame is selected. </li>
</ul>

<h3><code>execContentScript</code></h3>

<p><strong>Description</strong>: Executes necessary content scripts in the active tab's frames.</p>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Promise</code>: Resolves when scripts have been executed, or throws an error if the execution fails.</li>
</ul>

<h3><code>sendExecute</code></h3>

<p><strong>Description</strong>: Sends the message to execute the XPath expression to the content script.</p>

<p><strong>Parameters</strong>:</p>
<ul>
<li><code>null</code>: Takes no parameters.</li>
</ul>
<p><strong>Returns</strong>:</p>
<ul>
<li><code>null</code>: Returns nothing, but sends the message to execute the XPath expression. </li>
</ul>


<h3><code>handleExprEnter</code></h3>
<h3><code>showDetailsPage</code></h3>
<h3><code>showError</code></h3>
<h3><code>genericListener</code></h3>
<p>(These are more complex functions and detailed descriptions would require examining the specific implementation to be accurate. The format will be similar to the examples provided.)</p>


<!-- Add more function documentation here as needed -->

<h2>Event Listeners</h2>
<p>This section documents the event listeners, their purpose and handler functions.</p>

<!-- Add more sections for classes, additional event listeners, and any other needed documentation.  These are just placeholders -->

<h2>Global Variables</h2>

<p>This section documents the global variables used within the script.</p>

<!-- Add documentation for the global variables as needed -->