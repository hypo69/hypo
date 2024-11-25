html
<h1>options.js Module Documentation</h1>

<h2>Overview</h2>
<p>This JavaScript file handles the options page for the TryXPath extension. It allows users to configure attributes and styles for XPath matching. The file interacts with browser APIs for storage and retrieval of these options. It also provides validation for input values.</p>

<h2>Variables</h2>

<h3><code>defaultAttributes</code></h3>

<p><strong>Description</strong>: An object containing default attribute values for XPath selection.</p>
<pre><code>javascript
const defaultAttributes = {
    "element": "data-tryxpath-element",
    "context": "data-tryxpath-context",
    "focused": "data-tryxpath-focused",
    "focusedAncestor": "data-tryxpath-focused-ancestor",
    "frame": "data-tryxpath-frame",
    "frameAncestor": "data-tryxpath-frame-ancestor"
};
</code></pre>


<h3><code>defaultPopupBodyStyles</code></h3>

<p><strong>Description</strong>: An object containing default styles for the popup.</p>
<pre><code>javascript
const defaultPopupBodyStyles = {
    "width": "367px",
    "height": "auto"
};
</code></pre>


<h2>Functions</h2>

<h3><code>isValidAttrName</code></h3>

<p><strong>Description</strong>: Checks if an attribute name is valid for setting on an element.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>name</code> (str): The attribute name to validate.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>boolean</code>: <code>true</code> if the attribute name is valid, <code>false</code> otherwise.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Error</code>: If an error occurs during attribute setting.</li>
</ul>


<h3><code>isValidAttrNames</code></h3>

<p><strong>Description</strong>: Checks if all attribute names in an object are valid.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>names</code> (object): An object containing attribute names.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>boolean</code>: <code>true</code> if all attribute names are valid, <code>false</code> otherwise.</li>
</ul>


<h3><code>isValidStyleLength</code></h3>

<p><strong>Description</strong>: Validates if a style length is in a valid format.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>len</code> (str): The style length to validate.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>boolean</code>: <code>true</code> if the style length is valid, <code>false</code> otherwise.</li>
</ul>


<h3><code>loadDefaultCss</code></h3>

<p><strong>Description</strong>: Loads default CSS from a resource.</p>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Promise&lt;string&gt;</code>: A promise resolving to the loaded CSS.</li>
</ul>


<h3><code>extractBodyStyles</code></h3>

<p><strong>Description</strong>: Extracts width and height styles from a CSS string.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>css</code> (str): The CSS string to parse.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>object</code>: An object containing width and height styles.</li>
</ul>


<h3><code>createPopupCss</code></h3>

<p><strong>Description</strong>: Creates a CSS string for the popup's body.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>bodyStyles</code> (object): An object containing width and height styles.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>string</code>: The CSS string for the popup body.</li>
</ul>



<!-- ... (other functions and methods are documented similarly) ... -->

<h2>Event Listeners</h2>

<p>The file includes event listeners for:</p>
<ul>
  <li><code>window.load</code>: Initialization and handling of option saving/loading.
  </li>
  <li>click event on save button: Handling options saving to storage.</li>
  <li>click event on show-default button: Resetting to default values.</li>
</ul>

<!-- Add the remaining documentation for other parts of the code -->