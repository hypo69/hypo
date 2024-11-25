html
<h1>try_xpath_background.js</h1>

<h2>Overview</h2>
<p>This JavaScript file defines the background script for the Try XPath extension.  It handles communication with the popup and content scripts, managing the storage of state information and the sending of CSS updates to the active tab(s).</p>

<h2>Variables</h2>

<h3><code>tx</code></h3>
<p><strong>Description</strong>: An alias for the <code>tryxpath</code> object.</p>

<h3><code>fu</code></h3>
<p><strong>Description</strong>: An alias for the <code>tryxpath.functions</code> object.</p>


<h3><code>popupState</code></h3>
<p><strong>Description</strong>: Stores the current state related to the popup window.</p>

<h3><code>popupCss</code></h3>
<p><strong>Description</strong>: Stores the CSS rules to be applied to the popup window.</p>

<h3><code>results</code></h3>
<p><strong>Description</strong>: Stores the results of XPath queries.</p>

<h3><code>css</code></h3>
<p><strong>Description</strong>: Stores the CSS rules to be applied to the content page.</p>

<h3><code>attributes</code></h3>
<p><strong>Description</strong>: Stores the custom attributes used by the extension.</p>

<h2>Functions</h2>

<h3><code>loadDefaultCss()</code></h3>

<p><strong>Description</strong>: Loads default CSS from a file.</p>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Promise</code>: Resolves with the loaded CSS content, rejects on error.</li>
</ul>


<h3><code>genericListener(message, sender, sendResponse)</code></h3>

<p><strong>Description</strong>: A message listener that dispatches messages to specific handlers.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>message</code>: The message received.</li>
  <li><code>sender</code>: The sender of the message.</li>
  <li><code>sendResponse</code>: A function to send a response.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Error</code>: Any error that might occur during message handling.</li>
</ul>


<h3><code>genericListener.listeners.storePopupState(message)</code></h3>

<p><strong>Description</strong>: Stores the popup state.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>message</code>: The message containing the state.</li>
</ul>



<h3><code>genericListener.listeners.requestRestorePopupState(message)</code></h3>

<p><strong>Description</strong>: Sends the stored popup state to the requesting script.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>message</code>: The message containing request details.</li>
</ul>


<h3><code>genericListener.listeners.requestInsertStyleToPopup()</code></h3>

<p><strong>Description</strong>: Sends the stored popup CSS to the popup.</p>


<h3><code>genericListener.listeners.showAllResults(message, sender)</code></h3>

<p><strong>Description</strong>: Shows the results to the user</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>message</code>: Message containing results</li>
  <li><code>sender</code>: Sender of the message</li>
</ul>


<h3><code>genericListener.listeners.loadResults(message, sender, sendResponse)</code></h3>

<p><strong>Description</strong>: Sends the results to the requesting script.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>message</code>: The message received.</li>
  <li><code>sender</code>: The sender of the message.</li>
  <li><code>sendResponse</code>: A function to send a response.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>boolean</code>:  <code>true</code> to indicate asynchronous operation.</li>
</ul>


<h3><code>genericListener.listeners.updateCss(message, sender)</code></h3>

<p><strong>Description</strong>: Updates the CSS in the active tab. Removes expired CSS and inserts new CSS rules.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>message</code>: The message with the new CSS code and expired CSS set.</li>
  <li><code>sender</code>: The sender of the message.</li>
</ul>


<h3><code>genericListener.listeners.loadOptions(message, sender, sendResponse)</code></h3>

<p><strong>Description</strong>: Sends the stored extension attributes and CSS rules.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>message</code>: The message received.</li>
  <li><code>sender</code>: The sender of the message.</li>
  <li><code>sendResponse</code>: A function to send a response.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>boolean</code>:  <code>true</code> to indicate asynchronous operation.</li>
</ul>

<h3><code>genericListener.listeners.requestSetContentInfo(message, sender)</code></h3>

<p><strong>Description</strong>: Sends content information to the content script.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>message</code>: The message received.</li>
  <li><code>sender</code>: The sender of the message.</li>
</ul>


<h2>Event Listeners</h2>

<p>The file utilizes the <code>browser.storage.onChanged</code> event to react to changes in storage values. This ensures that updates to attributes, CSS, and popup CSS are reflected in the extension.</p>

<h2>Storage</h2>

<p>The file leverages <code>browser.storage.sync</code> to retrieve and potentially load default values. This is crucial for persistence and initial configuration of the extension.</p>