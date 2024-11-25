html
<h1>hypotez/src/goog/quickstart.py</h1>

<h2>Overview</h2>
<p>This module provides a quickstart example for interacting with the Google Apps Script API. It demonstrates creating a new Apps Script project, uploading code files, and logging the project URL.</p>

<h2>Constants</h2>

<h3><code>MODE</code></h3>

<p><strong>Description</strong>: A string representing the current mode (e.g., 'dev').</p>


<h3><code>SCOPES</code></h3>

<p><strong>Description</strong>: A list of scopes required for interacting with the Google Apps Script API.</p>


<h3><code>SAMPLE_CODE</code></h3>

<p><strong>Description</strong>:  Example code snippet for a server-side JavaScript function.</p>


<h3><code>SAMPLE_MANIFEST</code></h3>

<p><strong>Description</strong>: Example manifest (JSON) for the script project.</p>


<h2>Functions</h2>

<h3><code>main</code></h3>

<p><strong>Description</strong>: Calls the Apps Script API to create and configure a new script project.</p>

<p><strong>Returns</strong>:</p>
<ul>
  <li>None</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>errors.HttpError</code>: Raised if there is an error during the API call.</li>
</ul>


<h3><code>__main__</code></h3>

<p><strong>Description</strong>: This special block allows calling the `main` function if the script is executed directly (not imported).
</p>


<h2>Classes</h2>

<h3><code>Path</code></h3>

<p><strong>Description</strong>:  The `Path` class from the `pathlib` module, used for handling file paths.</p>


<h2>Modules</h2>

<h3><code>header</code></h3>

<p><strong>Description</strong>: Placeholder for a module named header (not defined in the code). </p>


<h3><code>gs</code></h3>

<p><strong>Description</strong>: Placeholder for a module named gs (not defined in the code). </p>



<h3><code>Request</code></h3>

<p><strong>Description</strong>: A class for making HTTP requests.</p>


<h3><code>Credentials</code></h3>

<p><strong>Description</strong>:  Represents authentication credentials.  Used to authenticate with Google APIs.</p>


<h3><code>InstalledAppFlow</code></h3>

<p><strong>Description</strong>: Facilitates the authorization flow for installed applications.</p>


<h3><code>errors</code></h3>

<p><strong>Description</strong>: A module containing custom error objects for handling exceptions.</p>


<h3><code>build</code></h3>

<p><strong>Description</strong>: Constructs a Google API service object, enabling interaction with the API.</p>


<h3><code>Request</code></h3>

<p><strong>Description</strong>: A class providing methods for making HTTP requests. This is likely from the `google.auth` library.</p>


<p><strong>Methods</strong>:</p>
<ul>
  <li><code>refresh()</code>: Refreshes the authentication credentials.</li>
</ul>