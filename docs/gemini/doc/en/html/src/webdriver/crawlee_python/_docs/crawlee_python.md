html
<h1>CrawleePython Module Documentation</h1>

<h2>Overview</h2>
<p>This module provides a Python class, <code>CrawleePython</code>, for performing web scraping tasks using the <code>crawlee</code> library and Playwright. It handles setting up a crawler, extracting data from web pages, and exporting the results to a JSON file.</p>

<h2>Classes</h2>

<h3><code>CrawleePython</code></h3>

<p><strong>Description</strong>: This class encapsulates the web scraping process, utilizing PlaywrightCrawler for efficient asynchronous data extraction.</p>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__</code></li>
</ul>

<p><strong>Methods Details:</strong></p>

<ul>
  <li><h3><code>__init__</code></h3>
  <p><strong>Description</strong>: Initializes the <code>CrawleePython</code> object with configuration parameters for the crawler.</p>
  
  <p><strong>Parameters</strong>:</p>
  <ul>
    <li><code>max_requests</code> (int): The maximum number of requests allowed during the crawl.  </li>
    <li><code>headless</code> (bool, optional): Whether to run the browser in headless mode. Defaults to <code>True</code>.</li>
    <li><code>browser_type</code> (str, optional): The type of browser to use (e.g., 'chromium', 'firefox'). Defaults to 'chromium'. </li>
  </ul>
  
  <p><strong>Raises</strong>:</p>
  <ul>
     <li><code>TypeError</code>: If an invalid type is provided for a parameter.</li>
     <li><code>ValueError</code>: If an invalid value is provided for a parameter, such as a negative `max_requests` value.</li>
  </ul>
  </li>
  <li><code>setup_crawler</code></li>
</ul>

<p><strong>Methods Details:</strong></p>

<ul>
  <li><h3><code>setup_crawler</code></h3>
  <p><strong>Description</strong>: Sets up the crawler by defining a default request handler.</p>
  <p><strong>Returns</strong>:</p>
  <ul>
    <li><code>PlaywrightCrawler</code>: The initialized crawler object.</li>
  </ul>
  <p><strong>Raises</strong>:
  <ul>
    <li><code>Exception</code>: For any other error during setup.</li>
  </ul></p>
</li>
<li><h3><code>run_crawler</code></h3>
  <p><strong>Description</strong>: Runs the crawler on a list of initial URLs.</p>
  <p><strong>Parameters</strong>:</p>
  <ul>
    <li><code>urls</code> (list): A list of starting URLs for the crawl.</li>
  </ul>
  <p><strong>Returns</strong>:</p>
  <ul>
    <li><code>list</code>: A list of dictionaries containing the extracted data from each page.</li>
  </ul>
  </li>
<li><h3><code>export_data</code></h3>
  <p><strong>Description</strong>: Exports the extracted data to a JSON file.</p>
  <p><strong>Parameters</strong>:</p>
  <ul>
    <li><code>data</code> (list): The data to be exported.</li>
    <li><code>output_file</code> (str, optional): The name of the output JSON file. Defaults to 'scraped_data.json'.</li>
  </ul>
  <p><strong>Raises</strong>:</p>
  <ul>
    <li><code>Exception</code>: For any I/O error during file writing. </li>
  </ul>

</li>
<li><h3><code>get_data</code></h3>
  <p><strong>Description</strong>: Retrieves the extracted data.
  </p>
<p><strong>Returns</strong>:</p>
<ul>
  <li><code>dict</code>: The extracted data as a dictionary.  Returns an empty dictionary if no data has been collected yet.</li>
</ul>
</li>
<li><h3><code>run</code></h3>
  <p><strong>Description</strong>: Orchestrates the entire web scraping process.
  </p>
<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>urls</code> (list): A list of starting URLs for the crawl.</li>
</ul>
<p><strong>Returns</strong>:</p>
<ul>
  <li><code>None</code></li>
</ul>
</li>


</ul>


<h2>Functions</h2>

<!-- List functions here if any -->


<h2>Example Usage</h2>
<p>Refer to the example code within the module for detailed usage instructions and implementation details.</p>


```