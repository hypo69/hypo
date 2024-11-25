html
<h1>hypotez/src/goog/spreadsheet/_examples/google_sample.py</h1>

<h2>Overview</h2>
<p>This module demonstrates basic usage of the Google Sheets API. It retrieves data from a sample spreadsheet and prints the name and major of each student.</p>

<h2>Variables</h2>

<h3><code>MODE</code></h3>

<p><strong>Description</strong>: Defines the operating mode (currently set to 'dev').</p>


<h3><code>SCOPES</code></h3>

<p><strong>Description</strong>: Defines the scopes needed for accessing the Google Sheets API. This list specifies the types of access required from the application, in this case, reading only.</p>


<h3><code>SAMPLE_SPREADSHEET_ID</code></h3>

<p><strong>Description</strong>: Specifies the ID of the sample spreadsheet to retrieve data from.</p>


<h3><code>SAMPLE_RANGE_NAME</code></h3>

<p><strong>Description</strong>: Defines the range of cells to retrieve data from within the spreadsheet.</p>


<h3><code>ROOT_DIRECTORY</code></h3>

<p><strong>Description</strong>: Stores the absolute path of the current working directory.</p>

<h3><code>path</code></h3>

<p><strong>Description</strong>: Constructs the file path to the client secret JSON file. This file is crucial for authentication with the Google API.</p>


<h2>Functions</h2>

<h3><code>main</code></h3>

<p><strong>Description</strong>: The main function of the script. It handles authentication, fetches data from the spreadsheet, and prints the extracted data.</p>

<p><strong>Returns</strong>:
  <ul><li>None</li></ul>
</p>
<p><strong>Raises</strong>:
  <ul><li><code>HttpError</code>: Indicates an error occurred during the API call. The error message will be printed to the console.</li></ul>
</p>


<h3><code>main</code></h3>

<p><strong>Description</strong>: The main function of the script, responsible for the entire process of authentication, data retrieval, and output.</p>

<p><strong>Returns</strong>:
  <ul><li>None</li></ul>
</p>
<p><strong>Raises</strong>:
  <ul><li><code>HttpError</code>: Raised if there's a problem communicating with the Google Sheets API.</li></ul>
</p>


<p><strong>Parameters</strong>:
  <ul>
    <li>None</li>
  </ul>
</p>


<!-- Add other function/class documentation here following the same structure -->