html
<h1>send_data.js</h1>

<h2>Overview</h2>
<p>This JavaScript file defines a function <code>onPageLoad</code> to collect page information (title, URL, and body content) and send it as a POST request to a specified API endpoint.  The script utilizes the `fetch` API for sending the data.</p>

<h2>Functions</h2>

<h3><code>onPageLoad</code></h3>

<p><strong>Description</strong>: This function collects page information and sends it to the specified API endpoint.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li>None (implicit parameters are handled internally).</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li>None (no explicit return statement).</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Error</code>: Thrown if the network request is not successful.</li>
</ul>

<p><strong>Implementation Details</strong>:</p>

<ol>
  <li>Collects the document title, URL, and body content using <code>document.title</code>, <code>window.location.href</code>, and <code>document.body.innerHTML</code>, respectively.</li>
  <li>Creates a JavaScript object <code>data</code> containing the collected information.</li>
  <li>Makes a POST request to the API endpoint 'http://127.0.0.1/hypotez.online/api/' using the `fetch` API, including the JSON data in the request body.</li>
  <li>Handles the response from the API, logging success or error messages to the console.</li>
</ol>


<h3><code>fetch</code></h3>

<p><strong>Description</strong>: Fetches data from a specified resource. This is part of the JavaScript API, not a function within this particular script.</p>
<p><strong>Implementation Details</strong>: This function is used in the script, but the specifics of its use are within the overall workings of the <code>onPageLoad</code> method and are well-documented in the web's JavaScript API documentation.</p>

<p><strong>Detailed Example usage in <code>onPageLoad()</code></strong></p>
<p>
   ```javascript
    fetch('http://127.0.0.1/hypotez.online/api/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    ```
</p>