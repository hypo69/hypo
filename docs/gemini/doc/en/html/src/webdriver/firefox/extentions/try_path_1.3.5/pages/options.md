html
<h1>options.js Documentation</h1>

<h2>Overview</h2>
<p>This JavaScript file handles the options page for the Try XPath extension. It allows users to configure various attributes and styles for the extension.</p>

<h2>Variables</h2>

<h3><code>defaultAttributes</code></h3>

<p><strong>Description</strong>: An object containing default attribute values for the extension.</p>
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

<p><strong>Description</strong>: An object containing default styles for the popup body.</p>
<pre><code>javascript
const defaultPopupBodyStyles = {
    "width": "367px",
    "height": "auto"
};
</code></pre>


<h2>Functions</h2>

<h3><code>isValidAttrName</code></h3>

<p><strong>Description</strong>: Checks if the given attribute name is valid.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>name</code> (str): The attribute name to check.</li>
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

<p><strong>Description</strong>: Checks if all attribute names in the provided object are valid.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>names</code> (Object): An object containing attribute names.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>boolean</code>: <code>true</code> if all attribute names are valid, <code>false</code> otherwise.</li>
</ul>

<h3><code>isValidStyleLength</code></h3>

<p><strong>Description</strong>: Checks if the given style length is valid (e.g., "367px", "auto").</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>len</code> (str): The style length to check.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>boolean</code>: <code>true</code> if the style length is valid, <code>false</code> otherwise.</li>
</ul>

<h3><code>loadDefaultCss</code></h3>

<p><strong>Description</strong>: Loads default CSS from a file.</p>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Promise&lt;string&gt;</code>: A promise that resolves to the loaded CSS text.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Error</code>: If an error occurs during the request.</li>
</ul>


<h3><code>extractBodyStyles</code></h3>

<p><strong>Description</strong>: Extracts width and height styles from CSS.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>css</code> (str): The CSS string.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Object</code>: An object containing extracted width and height styles.</li>
</ul>

<h3><code>createPopupCss</code></h3>

<p><strong>Description</strong>: Creates CSS for the popup body with specified styles.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>bodyStyles</code> (Object): An object containing width and height styles.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>string</code>: The CSS string for the popup body.</li>
</ul>

<!-- ... other functions and variables ... -->


<h2>Event Listeners</h2>

<p>This section describes event listeners added to the page.</p>

<h3><code>window.addEventListener("load", ...)</code></h3>

<p>This listener handles initial setup and loading of options when the window loads.</p>

<!-- ...  event listener details ... -->