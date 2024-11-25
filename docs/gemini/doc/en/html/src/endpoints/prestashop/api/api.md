html
<h1>Module api</h1>

<h2>Overview</h2>
<p>This module provides a class, <code>PrestaShop</code>, for interacting with the PrestaShop web service API. It supports JSON and XML data formats, handles various HTTP methods (GET, POST, PUT, DELETE), and includes methods for creating, reading, updating, deleting resources, searching, and uploading images.  It also features error handling for responses and data parsing.</p>

<h2>Classes</h2>

<h3><code>PrestaShop</code></h3>

<p><strong>Description</strong>:  This class facilitates interactions with the PrestaShop API, enabling various operations like CRUD, searching, and image uploading.</p>

<p><strong>Attributes</strong>:</p>
<ul>
  <li><code>client</code> (<code>Session</code>): The HTTP session object for making requests.</li>
  <li><code>debug</code> (<code>bool</code>): Flag to enable/disable debug mode. Defaults to <code>True</code>.</li>
  <li><code>language</code> (<code>int</code>): Default language ID. Defaults to <code>None</code>.</li>
  <li><code>data_format</code> (<code>str</code>): Default data format (JSON or XML). Defaults to 'JSON'.</li>
  <li><code>ps_version</code> (<code>str</code>): PrestaShop web service version.</li>
   <li><code>API_DOMAIN</code> (<code>str</code>): The API domain URL.</li>
  <li><code>API_KEY</code> (<code>str</code>): The API key for authentication.</li>
</ul>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__</code>: Initializes the <code>PrestaShop</code> object.
    <ul>
      <li>Takes API domain, API key, data format, default language, and debug mode as parameters.</li>
       <li>Initializes the HTTP session client and stores authentication credentials.</li>
      <li>Retrieves and stores the PrestaShop version from the server.</li>
      <li>Sets up the API connection.</li>
    </ul>
  </li>
  <li><code>ping</code>: Checks if the PrestaShop web service is operational.
    <ul>
      <li>Returns <code>True</code> if the service is reachable, otherwise <code>False</code>.</li>
      <li>Handles HTTP errors.</li>
    </ul>
  </li>
   <li><code>_check_response</code>: Checks the HTTP status code of a response.
    <ul>
      <li>Returns <code>True</code> for successful responses (200, 201), otherwise <code>False</code> and logs errors.</li>
    </ul>
  </li>
  <li><code>_parse_response_error</code>: Parses error responses from the PrestaShop API.
    <ul>
      <li>Handles both JSON and XML error responses.</li>
      <li>Extracts error code and message.</li>
      <li>Logs the error details.</li>
    </ul>
  </li>
  <li><code>_prepare</code>: Prepares the URL for the API request by incorporating parameters.
  </li>
  <li><code>_exec</code>: Executes an HTTP request to the PrestaShop API.
    <ul>
      <li>Supports various HTTP methods (GET, POST, PUT, DELETE).</li>
      <li>Handles data, headers, and optional search filters.</li>
      <li>Supports JSON and XML data formats.</li>
      <li>Includes debug mode for logging requests and responses.</li>
      <li>Returns parsed data or <code>False</code> on failure.</li>
      <li>Validates the response and handles potential errors.</li>

    </ul>
  </li>
  <li><code>_parse</code>: Parses the API response (XML or JSON).
    <ul>
      <li>Handles potential errors during parsing and logs them.</li>
    </ul>
  </li>
  <li><code>create</code>: Creates a new resource on the PrestaShop API.
    <ul>
      <li>Takes the resource name and data as input.</li>
    </ul>
  </li>
  <li><code>read</code>: Retrieves a resource from the PrestaShop API by ID.
  </li>
  <li><code>write</code>: Updates an existing resource.
  </li>
  <li><code>unlink</code>: Deletes a resource.
  </li>
  <li><code>search</code>: Searches for resources based on a filter.
  </li>
  <li><code>create_binary</code>: Uploads a binary file (image).
  </li>
  <li><code>_save</code>: Saves the fetched data to a file.
  </li>
  <li><code>get_data</code>: Fetches data from a resource, saves it, and returns it.
  </li>
  <li><code>remove_file</code>: Removes a file from the file system.
  </li>
  <li><code>get_apis</code>: Retrieves the list of available APIs.
  </li>
   <li><code>get_languages_schema</code>: Retrieves the schema for languages.</li>
  <li><code>upload_image_async</code>: Uploads an image to PrestaShop API asynchronously (using temporary files).
  </li>
  <li><code>upload_image</code>: Uploads an image (using temporary files).
  </li>
  <li><code>get_product_images</code>: Gets a list of images for a given product ID.</li>
</ul>

<p><strong>Exceptions</strong>:</p>
<ul>
  <li><code>PrestaShopException</code></li>
  <li><code>PrestaShopAuthenticationError</code></li>
  <li><code>ExpatError</code></li>
   <li><code>ValueError</code></li>
</ul>


<h2>Functions</h2>

<!-- List functions here if any exist -->

<h2>Enums</h2>

<h3><code>Format</code></h3>

<p><strong>Description</strong>: Defines data formats (JSON or XML) for API responses.</p>
<p><strong>Attributes</strong>:</p>
<ul>
  <li><code>JSON</code>: Constant for JSON format.</li>
  <li><code>XML</code>: Constant for XML format.</li>
</ul>