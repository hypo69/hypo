html
<h1>try_xpath_background.js</h1>

<h2>Overview</h2>
<p>This JavaScript file handles background interactions for the Try XPath extension. It listens for messages from content scripts, manages popup state, and interacts with browser APIs for CSS manipulation, storage, and communication with the popup.</p>

<h2>Variables</h2>

<h3><code>tx</code></h3>
<p><strong>Description</strong>: Alias for the <code>tryxpath</code> object.</p>

<h3><code>fu</code></h3>
<p><strong>Description</strong>: Alias for the <code>tryxpath.functions</code> object.</p>

<h3><code>popupState</code></h3>
<p><strong>Description</strong>: Stores the current state of the popup.</p>

<h3><code>popupCss</code></h3>
<p><strong>Description</strong>: Default CSS style for the popup.</p>

<h3><code>results</code></h3>
<p><strong>Description</strong>: Stores the results of XPath queries.</p>

<h3><code>css</code></h3>
<p><strong>Description</strong>: Stores the CSS code to be inserted.</p>

<h3><code>attributes</code></h3>
<p><strong>Description</strong>: Stores the attributes used for identifying elements.</p>

<h2>Functions</h2>

<h3><code>loadDefaultCss()</code></h3>

<p><strong>Description</strong>: Loads default CSS from a file.</p>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Promise<string></code>: Resolves with the loaded CSS content. Rejects on failure.</li>
</ul>

<h3><code>genericListener(message, sender, sendResponse)</code></h3>

<p><strong>Description</strong>: Handles messages from content scripts.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>message</code> (object): Message data.</li>
  <li><code>sender</code> (object): Sender details.</li>
  <li><code>sendResponse</code> (function): Callback for sending responses.</li>
</ul>


<h3><code>genericListener.listeners.storePopupState(message)</code></h3>

<p><strong>Description</strong>: Stores the popup state from a message.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>message</code> (object): Message data containing the state.</li>
</ul>

<h3><code>genericListener.listeners.requestRestorePopupState(message)</code></h3>

<p><strong>Description</strong>: Sends a message to restore the popup state.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>message</code> (object): Message data (not used).</li>
</ul>

<h3><code>genericListener.listeners.requestInsertStyleToPopup()</code></h3>

<p><strong>Description</strong>: Sends a message to insert CSS into the popup.</p>

<h3><code>genericListener.listeners.showAllResults(message, sender)</code></h3>

<p><strong>Description</strong>: Handles requests to display all results in a new tab.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>message</code> (object): Message data (not used).</li>
  <li><code>sender</code> (object): Sender details.</li>
</ul>

<h3><code>genericListener.listeners.loadResults(message, sender, sendResponse)</code></h3>

<p><strong>Description</strong>: Sends results to the sender.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>message</code> (object): Message data (not used).</li>
  <li><code>sender</code> (object): Sender details.</li>
  <li><code>sendResponse</code> (function): Callback for sending responses.</li>
</ul>


<h3><code>genericListener.listeners.updateCss(message, sender)</code></h3>

<p><strong>Description</strong>: Updates or removes CSS in a given tab.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>message</code> (object): Message containing the CSS to be updated or removed.</li>
  <li><code>sender</code> (object): Sender details.</li>
</ul>


<h3><code>genericListener.listeners.loadOptions(message, sender, sendResponse)</code></h3>

<p><strong>Description</strong>: Sends options (attributes, CSS, popup CSS) to the sender.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>message</code> (object): Message data (not used).</li>
  <li><code>sender</code> (object): Sender details.</li>
  <li><code>sendResponse</code> (function): Callback for sending responses.</li>
</ul>

<h3><code>genericListener.listeners.requestSetContentInfo(message, sender)</code></h3>

<p><strong>Description</strong>: Sends a message to set content info to the content script.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>message</code> (object): Message data (not used).</li>
  <li><code>sender</code> (object): Sender details.</li>
</ul>


<h2>Event Listeners</h2>

<p>The file listens for the following events:</p>
<ul>
    <li><code>browser.runtime.onMessage</code>: Handles messages from the popup or content scripts.</li>
    <li><code>browser.storage.onChanged</code>: Listens for storage changes and updates internal variables accordingly.</li>
</ul>


<h2>Error Handling</h2>

<p>The code uses <code>fu.onError</code> for catching errors.</p>

<h2>Storage</h2>

<p>The script retrieves and potentially loads default CSS from browser storage.</p>