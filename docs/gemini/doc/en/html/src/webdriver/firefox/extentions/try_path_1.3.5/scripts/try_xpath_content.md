html
<h1>try_xpath_content.js</h1>

<h2>Overview</h2>
<p>This JavaScript file implements the Try XPath extension's core logic for interacting with the browser and handling XPath queries. It manages communication with the popup, retrieves data from the DOM, and updates the styles for highlighting results.</p>

<h2>Variables</h2>
<ul>
<li><code>tx</code>: An alias for the <code>tryxpath</code> object.</li>
<li><code>fu</code>: An alias for the <code>tryxpath.functions</code> object.</li>
<li><code>tx.isContentLoaded</code>: A boolean flag to prevent multiple executions.</li>
<li><code>dummyItem</code>, <code>dummyItems</code>, <code>invalidExecutionId</code>: Placeholder values.</li>
<li><code>styleElementHeader</code>: String for inserting the style element.</li>
<li><code>attributes</code>: An object containing attributes names.</li>
<li><code>prevMsg</code>: Holds the previous message for communication.</li>
<li><code>executionCount</code>: Counter for message IDs.</li>
<li><code>inBlankWindow</code>: Flag to indicate operation within an iframe.</li>
<li><code>currentDocument</code>: The current document being processed.</li>
<li><code>contextItem</code>, <code>currentItems</code>, <code>focusedItem</code>, <code>focusedAncestorItems</code>: Variables related to the currently selected item(s) in the DOM.</li>
<li><code>currentCss</code>: The current stylesheet.</li>
<li><code>insertedStyleElements</code>: A Map storing style elements inserted in documents.</li>
<li><code>expiredCssSet</code>: An object keeping track of expired styles.</li>
<li><code>originalAttributes</code>: A map to store original attributes.</li>
</ul>


<h2>Functions</h2>

<h3><code>setAttr</code></h3>
<p><strong>Description</strong>: Sets an attribute to an item in the DOM, saving the original value.</p>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>attr</code> (str): The name of the attribute to set.</li>
<li><code>value</code> (str): The value to set for the attribute.</li>
<li><code>item</code> (Object): The DOM element or attribute.</li>
</ul>

<h3><code>setIndex</code></h3>
<p><strong>Description</strong>: Sets index for a collection of elements, saving the original values.</p>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>attr</code> (str): The name of the attribute to set.</li>
<li><code>items</code> (Array): The elements to set the index for.</li>
</ul>


<h3><code>isFocusable</code></h3>
<p><strong>Description</strong>: Checks if an item is focusable.</p>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>item</code> (Object): The element or attribute to check.</li>
</ul>
<p><strong>Returns</strong>:</p>
<ul>
<li><code>boolean</code>: <code>true</code> if focusable, <code>false</code> otherwise.</li>
</ul>


<h3><code>focusItem</code></h3>
<p><strong>Description</strong>: Sets focus to the given item, handling different item types.</p>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>item</code> (Object): The element to focus.</li>
</ul>


<h3><code>setMainAttrs</code></h3>
<p><strong>Description</strong>: Sets context and element attributes for the result items.</p>

<h3><code>restoreAttrs</code></h3>
<p><strong>Description</strong>: Restores attributes of elements and collections.</p>


<h3><code>resetPrev</code></h3>
<p><strong>Description</strong>: Resets previous message, attributes, and variables for new operations.</p>


<h3><code>makeTypeStr</code></h3>
<p><strong>Description</strong>: Creates a string representation of the result type.</p>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>resultType</code> (Number): The type of result.</li>
</ul>
<p><strong>Returns</strong>:</p>
<ul>
<li><code>String</code>: The string representation of result type.</li>
</ul>



<h3><code>updateCss</code></h3>
<p><strong>Description</strong>: Sends a message to update CSS.</p>


<h3><code>getFrames</code>, <code>parseFrameDesignation</code>, <code>traceBlankWindows</code></h3>
<p><strong>Description</strong>: Functions for handling frame interactions. These functions are specifically tailored to deal with complex interactions with frames, iframes, and blank windows.</p>


<h3><code>handleCssChange</code></h3>
<p><strong>Description</strong>: Handles changes to the current stylesheet.</p>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>newCss</code> (String): The new stylesheet.</li>
</ul>


<h3><code>findFrameByMessage</code></h3>
<p><strong>Description</strong>: Retrieves the frame based on the received message and window.</p>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>event</code> (Object): The message event.</li>
<li><code>win</code> (Window): The target window.</li>
</ul>
<p><strong>Returns</strong>:</p>
<ul>
<li><code>Object</code>: The target frame or null.</li>
</ul>


<h3><code>setFocusFrameListener</code>, <code>initBlankWindow</code></h3>
<p><strong>Description</strong>: Functions for handling frame focus and initialization of blank windows.</p>


<h3><code>findStyleParent</code>, <code>updateStyleElement</code>, <code>updateAllStyleElements</code>, <code>removeStyleElement</code>, <code>removeAllStyleElements</code></h3>
<p><strong>Description</strong>: Functions for managing stylesheets in the browser, including adding, updating, and removing style elements.</p>


<h3><code>createResultMessage</code></h3>
<p><strong>Description</strong>: Creates a result message object with a default structure.</p>


<h3><code>genericListener</code></h3>
<p><strong>Description</strong>: A listener for generic messages sent to the background script, handling different event types and sending appropriate responses.</p>


<h3><code>genericListener.listeners.execute</code></h3>
<p><strong>Description</strong>: Handles the execution of XPath expressions.</p>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>message</code> (Object): The message containing the query details.</li>
<li><code>sender</code> (Object): The sender of the message.</li>
</ul>
<p><strong>Returns</strong>:</p>
<ul>
<li><code>void</code></li>
</ul>

<h3><code>genericListener.listeners.*</code></h3>
<p><strong>Description</strong>: List of all genericListeners functions, they handles various messages.</p>

<h3><code>browser.storage.onChanged.addListener</code></h3>
<p><strong>Description</strong>: Listens for changes in browser storage (e.g., attributes and CSS).</p>

<h3><code>window.addEventListener</code></h3>
<p><strong>Description</strong>: Handles messages received by the main window.</p>

<!-- Add more function documentation as needed -->