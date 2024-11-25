html
<h1>try_xpath_content.js</h1>

<h2>Overview</h2>
<p>This JavaScript file implements the Try XPath extension's core logic for interacting with the browser and executing XPath queries. It handles various aspects such as retrieving elements, focusing items, managing style updates, and handling messages from the popup window and other frames. It utilizes the browser API for communication and interaction.</p>

<h2>Variables</h2>

<h3><code>tx</code></h3>
<p><strong>Description</strong>: An alias for the <code>tryxpath</code> object, likely containing utility functions.</p>

<h3><code>fu</code></h3>
<p><strong>Description</strong>: An alias for the <code>tryxpath.functions</code> object, containing functions related to XPath processing and element manipulation.</p>

<h3><code>tx.isContentLoaded</code></h3>
<p><strong>Description</strong>: A boolean flag to prevent multiple script executions.</p>

<h3><code>dummyItem</code>, <code>dummyItems</code>, <code>invalidExecutionId</code>, <code>styleElementHeader</code></h3>
<p><strong>Description</strong>: Dummy values used for initialization and placeholder purposes.</p>

<h3><code>attributes</code></h3>
<p><strong>Description</strong>: An object containing the attribute names used to store information about selected elements and contexts.</p>

<h3><code>prevMsg</code></h3>
<p><strong>Description</strong>: Stores the previous message sent from the script to the popup, likely used for error handling and result persistence.</p>

<h3><code>executionCount</code></h3>
<p><strong>Description</strong>: A counter tracking the number of executed queries.</p>

<h3><code>inBlankWindow</code></h3>
<p><strong>Description</strong>: A flag indicating whether the script is running within a blank window. </p>

<h3><code>currentDocument</code></h3>
<p><strong>Description</strong>: The current document being processed.</p>

<h3><code>contextItem</code>, <code>currentItems</code>, <code>focusedItem</code>, <code>focusedAncestorItems</code>, <code>currentCss</code>, <code>insertedStyleElements</code>, <code>expiredCssSet</code>, <code>originalAttributes</code></h3>
<p><strong>Description</strong>: Variables storing data about the currently selected context, items, focused elements, style information, and attribute management.</p>


<h2>Functions</h2>

<h3><code>setAttr(attr, value, item)</code></h3>

<p><strong>Description</strong>: Sets an attribute to a given item, storing the original value before modification.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>attr</code> (str): The attribute name to set.</li>
  <li><code>value</code> (str): The value to set the attribute to.</li>
  <li><code>item</code> (object): The DOM element to set the attribute on.</li>
</ul>

<h3><code>setIndex(attr, items)</code></h3>
<p><strong>Description</strong>: Sets an index attribute to items, storing original values.</p>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>attr</code> (str): The index attribute to set.</li>
<li><code>items</code> (Array): An array of items to set the index for.</li>
</ul>


<h3><code>isFocusable(item)</code></h3>
<p><strong>Description</strong>: Checks if an item is focusable based on its type.</p>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>item</code> (object): The item to check.</li>
</ul>
<p><strong>Returns</strong>:</p>
<ul>
<li><code>boolean</code>: True if the item is focusable, false otherwise.</li>
</ul>

<h3><code>focusItem(item)</code></h3>
<p><strong>Description</strong>: Sets the focus to a given item, managing focused and ancestor items.</p>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>item</code> (object): The item to focus.</li>
</ul>

<h3><code>setMainAttrs()</code></h3>
<p><strong>Description</strong>: Sets attributes related to the main context.</p>


<h3><code>restoreAttrs()</code></h3>
<p><strong>Description</strong>: Resets attributes to their original states.</p>

<h3><code>resetPrev()</code></h3>
<p><strong>Description</strong>: Resets various internal variables and creates a new result message.</p>


<h3><code>makeTypeStr(resultType)</code></h3>
<p><strong>Description</strong>: Formats a result type into a string.</p>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>resultType</code>: The result type.</li>
</ul>
<p><strong>Returns</strong>:</p>
<ul>
<li><code>string</code>: The formatted result type string.</li>
</ul>


<h3><code>updateCss()</code></h3>
<p><strong>Description</strong>: Sends a message to update the CSS in the background.</p>

<h3><code>getFrames(spec)</code>, <code>parseFrameDesignation(frameDesi)</code></h3>
<p><strong>Description</strong>: Functions for handling frame specifications. They parse and validate frame indices and possibly extract frame ancestry, handling errors gracefully.</p>

<h3><code>traceBlankWindows(desi, win)</code></h3>
<p><strong>Description</strong>: Traces a sequence of potentially blank windows. It navigates through a chain of frames specified in the parameter and checks whether each frame is a blank window. If a non-blank window is encountered, it reports an error.</p>

<h3><code>handleCssChange(newCss)</code></h3>
<p><strong>Description</strong>: Handles changes to the CSS style, updating and managing active styles or marking expired styles.</p>


<h3><code>findFrameByMessage(event, win)</code></h3>
<p><strong>Description</strong>: Finds a frame based on a message and frame index.</p>

<h3><code>setFocusFrameListener(win, isBlankWindow)</code></h3>
<p><strong>Description</strong>: Sets a message listener for focusing frames.</p>

<h3><code>initBlankWindow(win)</code></h3>
<p><strong>Description</strong>: Initializes a blank window if it hasn't already been initialized.</p>


<h3><code>findStyleParent(doc)</code>, <code>updateStyleElement(doc)</code>, <code>updateAllStyleElements()</code>, <code>removeStyleElement(doc)</code>, <code>removeAllStyleElements()</code></h3>
<p><strong>Description</strong>: Functions for managing the insertion, update, and removal of style elements in a document.</p>


<h3><code>createResultMessage()</code></h3>
<p><strong>Description</strong>: Creates a result message object for communication with the popup.</p>

<h3><code>genericListener</code></h3>
<p><strong>Description</strong>: A listener function for handling messages from the background script or other frames.  It routes messages to appropriate event handlers.</p>

<p><strong>Listeners</strong>:</p>
<ul>
<li><code>setContentInfo</code></li>
<li><code>execute</code></li>
<li><code>focusItem</code></li>
<li><code>focusContextItem</code></li>
<li><code>focusFrame</code></li>
<li><code>requestShowResultsInPopup</code></li>
<li><code>requestShowAllResults</code></li>
<li><code>resetStyle</code></li>
<li><code>setStyle</code></li>
<li><code>finishInsertCss</code></li>
<li><code>finishRemoveCss</code></li>
</ul>

<h3><code>browser.storage.onChanged.addListener</code></h3>
<p><strong>Description</strong>: Listens for changes in browser storage related to attributes and styles, and updates relevant values if necessary.</p>


<h3><code>window.addEventListener</code></h3>
<p><strong>Description</strong>: Handles messages from other frames or windows, potentially related to error reporting or frame traversal.</p>


<p><em>Note: Detailed explanations and type hints for some of these functions are not complete or accessible from just the JavaScript code alone.  In order to create a more comprehensive and accurate documentation you would need access to the complete definition of the `tryxpath` and `tryxpath.functions` objects.</em></p>