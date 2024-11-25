html
<h1>show_all_results.js</h1>

<h2>Overview</h2>
<p>This JavaScript file handles the display of search results from the TryXPath extension.</p>

<h2>Functions</h2>

<h3><code>showAllResults</code></h3>

<p><strong>Description</strong>: Displays the search results in the UI.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>results</code> (object): An object containing the search results data.  Includes properties for the message, title, href, frameId, context, and main.  The structure of the results object is crucial to the function's operation.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li>None: This function does not explicitly return a value. It modifies the HTML elements in the page to display the results.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li>No explicit exceptions are caught or re-thrown.  Errors encountered during asynchronous operations are handled by the <code>.catch(fu.onError)</code> blocks.</li>
</ul>


<h3><code>makeTextDownloadUrl</code></h3>

<p><strong>Description</strong>: Creates a download URL for a given text string.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>text</code> (string): The text string to be downloaded.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li>string: The URL for downloading the text.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li>No explicit exceptions are raised.</li>
</ul>

<h3><code>makeInfoText</code></h3>
<p><strong>Description</strong>: Creates a formatted text string representing the search results.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>results</code> (object): An object containing the search results, as in <code>showAllResults</code>.</li>
</ul>
<p><strong>Returns</strong>:</p>
<ul>
  <li>string: The formatted text string including details about the context and main results.</li>
</ul>
<p><strong>Raises</strong>:</p>
<ul>
 <li>No explicit exceptions are raised.</li>
</ul>

<h3><code>makeConvertedInfoText</code></h3>
<p><strong>Description</strong>: Creates a formatted text string similar to <code>makeInfoText</code>, but with JSON stringification of specific fields.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>results</code> (object): An object containing the search results, as in <code>showAllResults</code>.</li>
</ul>
<p><strong>Returns</strong>:</p>
<ul>
  <li>string: The formatted text string with JSON for specified fields.</li>
</ul>
<p><strong>Raises</strong>:</p>
<ul>
 <li>No explicit exceptions are raised.</li>
</ul>


<h2>Event Handling</h2>
<p>The function utilizes event listeners on the elements of the HTML page, including "load" to initiate the fetching of results from the browser runtime and "click" on different details buttons to initiate communication with the browser context for item focus.</p>


<h2>External Dependencies</h2>
<p>This code relies on <code>browser.runtime.sendMessage</code>, <code>browser.tabs.sendMessage</code>, the `tx`, `fu`, and <code>URL</code> object, and the <code>document</code> object from the window object, indicating the use of a browser extension or similar environment.</p>


<h2>Error Handling</h2>

<p>The code includes a <code>.catch(fu.onError)</code> block within asynchronous operations. The nature of the error is not available from this perspective. Further detail about <code>fu.onError</code> is required to describe proper error handling.</p>


```