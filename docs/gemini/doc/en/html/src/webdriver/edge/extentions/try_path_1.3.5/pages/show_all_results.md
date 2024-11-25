html
<h1>show_all_results.js</h1>

<h2>Overview</h2>
<p>This JavaScript file handles the display of search results from the TryXPath extension. It populates the UI with information from `results` object, providing context details and main results.  It also handles exporting the data in different formats and allows focusing on specific results within the browser.</p>

<h2>Variables</h2>

<h3><code>detailKeys</code></h3>

<p><strong>Description</strong>: An array containing the keys used to access details from the results.</p>
<p><strong>Value</strong>: `["type", "name", "value", "textContent"]`</p>

<h3><code>headerValues</code></h3>

<p><strong>Description</strong>: An array containing the corresponding header names for the details table.</p>
<p><strong>Value</strong>: `["Type", "Name", "Value", "textContent"]`</p>

<h3><code>relatedTabId</code>, <code>relatedFrameId</code>, <code>executionId</code></h3>

<p><strong>Description</strong>: Variables storing information related to the current tab, frame, and execution context.</p>


<h2>Functions</h2>

<h3><code>showAllResults(results)</code></h3>

<p><strong>Description</strong>: Populates the HTML elements with the provided search results.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>results</code> (object): An object containing the search results data.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>fu.onError</code>: An error occured during processing. </li>
</ul>

<h3><code>makeTextDownloadUrl(text)</code></h3>

<p><strong>Description</strong>: Creates a URL for downloading text as a file.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>text</code> (string): The text content to be downloaded.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>string</code>: The URL for downloading the text file.</li>
</ul>

<h3><code>makeInfoText(results)</code></h3>

<p><strong>Description</strong>: Generates a string containing formatted information from the results object, useful for text export.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>results</code> (object): The results object to process.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>string</code>: The formatted text information.</li>
</ul>

<h3><code>makeConvertedInfoText(results)</code></h3>

<p><strong>Description</strong>:  Similar to <code>makeInfoText</code>, but converts certain values (e.g., `value`, `textContent`) to JSON strings for export.</p>

<p><strong>Parameters</strong>:</p>
<ul>
<li><code>results</code> (object): The results object to process.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>string</code>: The formatted text information with JSON converted values.</li>
</ul>



<p><strong>Note</strong>: Detailed information on the contents of `cont` and `main` and their sub-elements are included within the respective function descriptions, and should be inferred from the JavaScript code itself.</p>


<h2>Event Handlers</h2>


<h3><code>window.addEventListener("load", ...)</code></h3>
<p><strong>Description</strong>: Listens for the "load" event and performs actions after the page loads.</p>
<p><strong>Actions</strong>:  Handles result loading from the browser extension (browser.runtime.sendMessage).  Populates the UI, sets up download links for text formats, and adds event listeners for button clicks to focus on context items and main items.</p>


<h3><code>contDetail.addEventListener("click", ...)</code></h3>
<p><strong>Description</strong>: Listens for clicks on elements within the context details section.</p>
<p><strong>Actions</strong>: If a button is clicked, it sends a message to the browser extension to focus on the corresponding context item (using `browser.tabs.sendMessage`).</p>


<h3><code>mainDetails.addEventListener("click", ...)</code></h3>
<p><strong>Description</strong>: Listens for clicks on elements within the main details section.</p>
<p><strong>Actions</strong>: If a button is clicked, it sends a message to the browser extension to focus on the corresponding main item (using `browser.tabs.sendMessage`).</p>

<p><strong>Note</strong>: The `data-index` attribute is used to identify the target item.</p>


<h2>Other</h2>

<h3><code>tx</code>, <code>fu</code></h3>

<p><strong>Description</strong>: Aliases for the TryXPath object and functions.</p>