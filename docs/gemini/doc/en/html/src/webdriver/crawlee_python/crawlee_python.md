html
<h1>CrawleePython Module Documentation</h1>

<h2>Overview</h2>
<p>This module provides a class for launching a web crawl using Playwright.  It handles setting up a crawler, running the crawl, exporting the results, and retrieving the extracted data.</p>

<h2>Classes</h2>

<h3><code>CrawleePython</code></h3>

<p><strong>Description</strong>:  This class encapsulates the logic for web crawling using Playwright.</p>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__</code>(max_requests: int = 5, headless: bool = False, browser_type: str = 'firefox'):
    <p><strong>Description</strong>: Initializes the CrawleePython instance with parameters for the crawl.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>max_requests</code> (int): Maximum number of concurrent requests. Defaults to 5.</li>
      <li><code>headless</code> (bool): Whether to run the browser in headless mode. Defaults to False.</li>
      <li><code>browser_type</code> (str): Type of browser to use. Defaults to 'firefox'.</li>
    </ul>
  </li>
  <li><code>setup_crawler</code>():
    <p><strong>Description</strong>: Sets up the PlaywrightCrawler instance.</p>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li>None</li>
    </ul>
  </li>
  <li><code>run_crawler</code>(urls: list[str]):
    <p><strong>Description</strong>: Runs the crawler with the initial list of URLs.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>urls</code> (list[str]): List of URLs to start the crawl.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li>None</li>
    </ul>
  </li>
  <li><code>export_data</code>(file_path: str):
    <p><strong>Description</strong>: Exports the entire dataset to a JSON file.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>file_path</code> (str): Path to save the exported JSON file.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li>None</li>
    </ul>
  </li>
  <li><code>get_data</code>() -> dict:
    <p><strong>Description</strong>: Retrieves the extracted data.</p>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>dict</code>: Extracted data as a dictionary.</li>
    </ul>
  </li>
  <li><code>run</code>(urls: list[str]):
    <p><strong>Description</strong>: Main method to set up, run the crawler, and export data.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>urls</code> (list[str]): List of URLs to start the crawl.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li>None</li>
    </ul>
  </li>
</ul>
</ul>

<h2>Functions</h2>

<p>(None)</p>

<!-- Add function documentation if any exist. -->