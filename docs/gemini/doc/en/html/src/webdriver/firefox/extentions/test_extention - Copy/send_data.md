html
<h1>send_data.js</h1>

<h2>Overview</h2>
<p>This JavaScript file handles the collection and sending of webpage data to a server.</p>

<h2>Functions</h2>

<h3><code>onPageLoad</code></h3>

<p><strong>Description</strong>: This function collects the title, URL, and body content of the current webpage and sends this data to the specified server endpoint using a POST request.</p>

<p><strong>Parameters</strong>:</p>
<ul>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Error</code>: This error is thrown if the network response is not ok.</li>
</ul>

<p><strong>Implementation Details</strong>:</p>
<ol>
  <li>It retrieves the page title using <code>document.title</code>.</li>
  <li>It retrieves the page URL using <code>window.location.href</code>.</li>
  <li>It retrieves the page body content using <code>document.body.innerHTML</code>.</li>
  <li>It constructs a JSON object containing the collected data.</li>
  <li>It makes a POST request to the server using <code>fetch</code>, sending the JSON data.</li>
  <li>It handles the response from the server, checking for success or errors.</li>
  <li>It logs the server's response or any errors encountered to the browser's console.</li>
</ol>
<pre><code>javascript
function onPageLoad() {
    // ... (code as provided)
}
</code></pre>

<h3><code>window.addEventListener('load', onPageLoad)</code></h3>

<p><strong>Description</strong>: This line of code attaches the <code>onPageLoad</code> function as a listener for the 'load' event of the window object. This ensures that the <code>onPageLoad</code> function is executed only after the entire page has finished loading, guaranteeing that all necessary elements are present in the DOM.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>'load'</code>: Specifies the event to listen for (the page loading).</li>
  <li><code>onPageLoad</code>: The function to execute when the event occurs.</li>
</ul>
<pre><code>javascript
window.addEventListener('load', onPageLoad);
</code></pre>