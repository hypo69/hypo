html
<h1>try_xpath_content.js</h1>

<h2>Overview</h2>
<p>This JavaScript file implements the Try XPath extension's core logic for interacting with the browser's DOM, handling messages, and updating the visual style of elements for easier XPath evaluation.</p>

<h2>Variables</h2>

<h3><code>tx</code></h3>

<p><strong>Description</strong>: An alias for the <code>tryxpath</code> object, likely a global object containing extension functions.</p>

<h3><code>fu</code></h3>

<p><strong>Description</strong>: An alias for <code>tryxpath.functions</code>, likely a namespace for helper functions.</p>

<h3><code>tx.isContentLoaded</code></h3>

<p><strong>Description</strong>: A flag to prevent multiple executions of initialization logic.</p>


<h3><code>dummyItem</code>, <code>dummyItems</code>, <code>invalidExecutionId</code>, <code>styleElementHeader</code></h3>

<p><strong>Description</strong>: Placeholder values used for initialization and error handling.</p>

<h3><code>attributes</code></h3>

<p><strong>Description</strong>: An object containing the names of custom attributes used to store information about elements for the Try XPath extension. </p>

<h3><code>prevMsg</code>, <code>executionCount</code></h3>

<p><strong>Description</strong>:  Used to store previous message and the execution count.</p>

<h3><code>inBlankWindow</code>, <code>currentDocument</code>, <code>contextItem</code>, <code>currentItems</code>, <code>focusedItem</code>, <code>focusedAncestorItems</code>, <code>currentCss</code></h3>

<p><strong>Description</strong>: Variables used to track the current state of the extension, including the context, selected elements, focus information, and current style.</p>

<h3><code>insertedStyleElements</code>, <code>expiredCssSet</code>, <code>originalAttributes</code></h3>

<p><strong>Description</strong>: Variables handling style elements, cached CSS, and attribute storage.</p>



<h2>Functions</h2>

<h3><code>setAttr(attr, value, item)</code></h3>

<p><strong>Description</strong>: Sets a custom attribute to an element or item.  Saves the original attribute value.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>attr</code> (str): The name of the attribute.</li>
  <li><code>value</code> (any): The value to set.</li>
  <li><code>item</code> (any): The element or item to set the attribute on.</li>
</ul>

<h3><code>setIndex(attr, items)</code></h3>

<p><strong>Description</strong>: Sets custom attributes to multiple items. Saves original attributes.</p>


<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>attr</code> (str): The name of the attribute.</li>
  <li><code>items</code> (array): An array of items to set the attribute on.</li>
</ul>

<h3><code>isFocusable(item)</code></h3>

<p><strong>Description</strong>: Checks if an item is focusable.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>item</code> (any): The item to check.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>boolean</code>: True if focusable, false otherwise.</li>
</ul>


<h3><code>focusItem(item)</code></h3>

<p><strong>Description</strong>: Sets focus on a specific item, clearing previous focus and updating related attributes.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>item</code> (any): The item to focus on.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Error</code>: If the item is not focusable.</li>
</ul>


<h3><code>setMainAttrs()</code></h3>

<p><strong>Description</strong>: Sets context and element attributes.</p>


<h3><code>restoreAttrs()</code></h3>

<p><strong>Description</strong>: Restores original attributes.</p>

<h3><code>resetPrev()</code></h3>

<p><strong>Description</strong>: Resets variables for a new execution.</p>

<h3><code>makeTypeStr(resultType)</code></h3>

<p><strong>Description</strong>: Converts a result type to a string format. Handles numeric types.</p>

<h3><code>updateCss()</code></h3>

<p><strong>Description</strong>: Sends a message to update the CSS if needed.</p>

<h3><code>getFrames(spec)</code>, <code>parseFrameDesignation(frameDesi)</code></h3>

<p><strong>Description</strong>: Parse frame specification and get the frame ancestry.</p>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Error</code>: For invalid frame specifications.</li>
</ul>

<h3><code>traceBlankWindows(desi, win)</code></h3>

<p><strong>Description</strong>: Traces through a series of frame indices and determines if a frame is a blank window or not.</p>


<h3><code>handleCssChange(newCss)</code></h3>

<p><strong>Description</strong>: Handles changes to the current CSS, either replacing or updating it.</p>

<h3><code>findFrameByMessage(event, win)</code></h3>

<p><strong>Description</strong>: Finds a frame based on a message containing a frame index.</p>

<h3><code>setFocusFrameListener(win, isBlankWindow)</code></h3>

<p><strong>Description</strong>: Sets up a message listener for focusing frames.</p>

<h3><code>initBlankWindow(win)</code></h3>

<p><strong>Description</strong>: Initializes the tryxpath object in blank windows.</p>

<h3><code>findStyleParent(doc)</code></h3>

<p><strong>Description</strong>: Finds the parent element for a style tag in the document (either head or body).</p>

<h3><code>updateStyleElement(doc)</code>, <code>updateAllStyleElements()</code>, <code>removeStyleElement(doc)</code>, <code>removeAllStyleElements()</code></h3>

<p><strong>Description</strong>: Functions for managing the insertion and removal of style elements.</p>

<h3><code>createResultMessage()</code></h3>

<p><strong>Description</strong>: Creates a default result message object.</p>


<h3><code>genericListener(message, sender, sendResponse)</code></h3>

<p><strong>Description</strong>: A generic message listener that dispatches messages to specific handlers based on the <code>message.event</code> property.</p>

<h3><code>genericListener.listeners</code></h3>

<p><strong>Description</strong>: A map that stores the message listeners using the message event type as the key.</p>


<h3><code>genericListener.listeners.execute(message, sender)</code></h3>

<p><strong>Description</strong>: Handles the execution of XPath queries, interacting with frames and contexts, handling errors, and sending results back to the popup.</p>

<p><strong>Parameters</strong>:</p>
<ul>
<li><code>message</code> (object): The message containing the query expression, frame designation, and context information.</li>
<li><code>sender</code> (object): The sender of the message.</li>
</ul>


<p><strong>Raises</strong>:</p>
<ul>
<li><code>Error</code>: For invalid frame specifications and errors during XPath evaluation.</li>
</ul>


<h3><code>genericListener.listeners.focusItem</code>, <code>genericListener.listeners.focusContextItem</code>, <code>genericListener.listeners.focusFrame</code></h3>


<p><strong>Description</strong>: Focus handling functions for elements identified by the extension.</p>

<h3><code>genericListener.listeners.requestShowResultsInPopup</code>, <code>genericListener.listeners.requestShowAllResults</code>, <code>genericListener.listeners.resetStyle</code>, <code>genericListener.listeners.setStyle</code>, <code>genericListener.listeners.finishInsertCss</code>, <code>genericListener.listeners.finishRemoveCss</code></h3>

<p><strong>Description</strong>:  Listeners for handling various actions related to displaying results, resetting style, and managing CSS updates.</p>


<h3><code>browser.storage.onChanged.addListener</code></h3>

<p><strong>Description</strong>: Listens for changes in browser storage, particularly for attribute and CSS updates.</p>

<h3><code>window.addEventListener("message", event => { ... })</code></h3>

<p><strong>Description</strong>: Listens for messages from other windows, handling messages related to errors.</p>

<p><strong>Raises</strong>:</p>
<ul>
<li><code>Error</code>: For errors while handling messages from other windows.</li>
</ul>

<p><strong>Note</strong>: This JavaScript code is deeply intertwined with the rest of the Try XPath extension and its functionality is complex and multifaceted. The provided HTML documentation gives a high-level overview.</p>