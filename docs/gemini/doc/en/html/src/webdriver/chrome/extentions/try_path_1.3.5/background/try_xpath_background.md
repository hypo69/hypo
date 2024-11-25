html
<h1>try_xpath_background.js</h1>

<h2>Overview</h2>
<p>This JavaScript file handles background processes for the Try XPath extension. It manages communication with content scripts, stores popup state, and updates CSS styles for the extension's popup.</p>

<h2>Variables</h2>

<h3><code>tx</code></h3>
<p><strong>Description</strong>: Alias for the <code>tryxpath</code> object.</p>

<h3><code>fu</code></h3>
<p><strong>Description</strong>: Alias for the <code>tryxpath.functions</code> object.</p>

<h3><code>popupState</code></h3>
<p><strong>Description</strong>: Stores the current state of the extension's popup.</p>

<h3><code>popupCss</code></h3>
<p><strong>Description</strong>: Stores the CSS styles for the extension's popup.</p>

<h3><code>results</code></h3>
<p><strong>Description</strong>: Stores the results of XPath queries.</p>

<h3><code>css</code></h3>
<p><strong>Description</strong>: Stores the CSS styles for the extension's content scripts.</p>

<h3><code>attributes</code></h3>
<p><strong>Description</strong>: Stores custom attributes for use in the extension.</p>

<h2>Functions</h2>

<h3><code>loadDefaultCss()</code></h3>

<p><strong>Description</strong>: Loads the default CSS styles for the extension's popup from a specified URL.</p>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Promise&lt;string&gt;</code>: Resolves with the content of the CSS file.</li>
</ul>

<h3><code>genericListener(message, sender, sendResponse)</code></h3>

<p><strong>Description</strong>: A generic listener function for handling messages from content scripts. It dispatches messages to specific listeners.</p>


<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>message</code> (object): The message received from a content script.</li>
  <li><code>sender</code> (object): Information about the sender (e.g., tab ID).</li>
  <li><code>sendResponse</code> (function): A function to send a response to the sender.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li>N/A</li>
</ul>

<h3><code>genericListener.listeners.storePopupState(message)</code></h3>

<p><strong>Description</strong>: Stores the popup state received in the <code>message</code>.</p>


<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>message</code> (object): The message containing the popup state.</li>
</ul>


<p><strong>Raises</strong>:</p>
<ul>
  <li>N/A</li>
</ul>

<h3><code>genericListener.listeners.requestRestorePopupState(message)</code></h3>

<p><strong>Description</strong>: Sends a message to restore the popup state.</p>

<p><strong>Raises</strong>:</p>
<ul>
  <li>N/A</li>
</ul>


<h3><code>genericListener.listeners.requestInsertStyleToPopup()</code></h3>

<p><strong>Description</strong>: Sends a message to insert the <code>popupCss</code> to the popup.</p>

<p><strong>Raises</strong>:</p>
<ul>
  <li>N/A</li>
</ul>


<h3><code>genericListener.listeners.showAllResults(message, sender)</code></h3>
<p><strong>Description</strong>: Handles the request to show all results by creating a new tab.</p>
<p><strong>Parameters</strong></p>
<ul>
<li>message (object): Message from content script.</li>
<li>sender (object): Information about the sender.</li>
</ul>
<p><strong>Raises</strong>:</p>
<ul>
<li>N/A</li>
</ul>

<h3><code>genericListener.listeners.loadResults(message, sender, sendResponse)</code></h3>

<p><strong>Description</strong>: Sends the <code>results</code> to the sender.</p>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>message</code> (object): Message from content script</li>
<li><code>sender</code> (object): Information about the sender.</li>
<li><code>sendResponse</code> (function): Function to send a response to the sender.</li>
</ul>
<p><strong>Returns</strong>: <code>true</code></p>

<h3><code>genericListener.listeners.updateCss(message, sender)</code></h3>

<p><strong>Description</strong>: Updates CSS styles in the current tab by removing and inserting the specified CSS. Handles errors during the process.</p>

<h3><code>genericListener.listeners.loadOptions(message, sender, sendResponse)</code></h3>
<p><strong>Description</strong>: Returns the attributes, css, and popupCss data in a response to the sender.</p>
<p><strong>Parameters</strong></p>
<ul><li>message (object)</li>
<li>sender (object)</li>
<li>sendResponse (function)</li></ul>
<p><strong>Returns</strong>: <code>true</code></p>

<h3><code>genericListener.listeners.requestSetContentInfo(message, sender)</code></h3>

<p><strong>Description</strong>: Sends a message to the content script to set the content info.</p>

<h3><code>browser.storage.onChanged.addListener(changes)</code></h3>

<p><strong>Description</strong>: Listens for changes in browser storage and updates the corresponding variables.</p>

<h3><code>browser.storage.sync.get(...)</code></h3>

<p><strong>Description</strong>: Retrieves data from browser storage. Fetches default CSS if not present.</p>


<h2>Event Listeners</h2>

<p>The code uses <code>browser.runtime.onMessage.addListener()</code> to register listeners for various events.</p>

<h2>Error Handling</h2>

<p>The code uses <code>fu.onError</code> to handle errors gracefully.</p>

<h2>CSS Handling</h2>
<p>The code dynamically loads, inserts, and removes CSS styles.</p>