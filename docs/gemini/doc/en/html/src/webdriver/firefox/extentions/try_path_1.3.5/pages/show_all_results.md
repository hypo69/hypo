html
<h1>show_all_results.js</h1>

<h2>Overview</h2>
<p>This JavaScript file handles the display of search results from the TryXPath extension. It populates various elements on the webpage with data from the `results` object, including context details, main results, and download links for the results.</p>

<h2>Functions</h2>

<h3><code>showAllResults</code></h3>

<p><strong>Description</strong>: This function updates the displayed search results based on the input `results` object.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>results</code> (object): An object containing the search results, including message, title, URL, frameId, context, and main information.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li>None: This function does not return a value.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Error</code>: Catches errors during the process via the `fu.onError` function.</li>
</ul>

<h3><code>makeTextDownloadUrl</code></h3>

<p><strong>Description</strong>: Creates a URL for downloading text content.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>text</code> (string): The text content to be downloaded.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>string</code>: A URL for downloading the text.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li>None</li>
</ul>


<h3><code>makeInfoText</code></h3>

<p><strong>Description</strong>: Constructs a formatted string containing the search results for download.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>results</code> (object): The search results object.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>string</code>: The formatted string with details of the search results.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li>None</li>
</ul>

<h3><code>makeConvertedInfoText</code></h3>

<p><strong>Description</strong>: Constructs a formatted string containing the search results for download, converting values to JSON strings.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>results</code> (object): The search results object.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>string</code>: The formatted string with details of the search results, values converted to JSON strings.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li>None</li>
</ul>


<h3><code>updateDetailsTable</code></h3>
<p><strong>Description</strong>: This is a likely helper function defined in another file (<code>tryxpath.functions</code>).  The provided code snippet lacks the implementation details.</p>
<p><strong>Parameters</strong>:
	<ul>
		<li><code>tbody</code> (HTML table body): The target table body to be updated.</li>
		<li><code>data</code> (Array): The array of data to insert into the table.</li>
		<li><code>options</code> (Object): An object containing options for the table update.</li>
	</ul>

</p>

<p><strong>Returns</strong>: Promise that resolves when the table is updated.</p>

<p><strong>Raises</strong>:
	<ul>
	<li><code>Error</code>: Error related to table update.</li>
	</ul>
</p>

<h3><code>onError</code></h3>
<p><strong>Description</strong>: Error handling function defined in another file (<code>tryxpath.functions</code>). The provided code snippet lacks the implementation details.</p>

<h2>Event Listeners</h2>

<p>The file includes event listeners on load, context details, and main details for interacting with the browser.</p>