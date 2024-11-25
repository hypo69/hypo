html
<h1>Module: hypotez/src/endpoints/kazarinov/scenarios/scenario_pricelist.py</h1>

<h2>Overview</h2>
<p>This module provides functionality for extracting, parsing, and processing product data from various suppliers. It handles data preparation, AI processing, and integration with Facebook for product posting.</p>

<h2>Classes</h2>

<h3><code>Mexiron</code></h3>

<p><strong>Description</strong>: Handles suppliers' product extraction, parsing, and saving processes. Supported suppliers include Morlevi, Ivory, KSP, and Grandadvance.</p>

<p><strong>Attributes</strong>:</p>
<ul>
  <li><code>driver</code> (Driver): Selenium WebDriver instance.</li>
  <li><code>export_path</code> (Path): Path to export the data.</li>
  <li><code>mexiron_name</code> (str): Name of the Mexiron process.</li>
  <li><code>price</code> (float): Price of the product.</li>
  <li><code>timestamp</code> (str): Timestamp of the process.</li>
  <li><code>products_list</code> (List): List of products.</li>
  <li><code>model</code> (GoogleGenerativeAI): AI model instance.</li>
  <li><code>model_command</code> (str): Command for the AI model.</li>
  <li><code>config</code> (SimpleNamespace): Configuration data.</li>
</ul>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__(self, driver: Driver, mexiron_name: Optional[str] = None)</code>:
    <p><strong>Description</strong>: Initializes Mexiron class with required components.</p>
    <p><strong>Args</strong>:</p>
    <ul>
      <li><code>driver</code> (Driver): Selenium WebDriver instance.</li>
      <li><code>mexiron_name</code> (Optional[str], optional): Custom name for the Mexiron process. Defaults to the timestamp.</li>
    </ul>
    <p><strong>Raises</strong>:</p>
    <ul>
        <li><code>Exception</code>: If there's an error loading configuration.</li>
    </ul>
  </li>
  <li><code>run_scenario(self, system_instruction: Optional[str] = None, price: Optional[str] = None, mexiron_name: Optional[str] = None, urls: Optional[str | List[str]] = None) -> bool</code>:
    <p><strong>Description</strong>: Executes the scenario: parses products, processes them via AI, and stores data.</p>
    <p><strong>Args</strong>:</p>
    <ul>
      <li><code>system_instruction</code> (Optional[str], optional): System instructions for the AI model. Defaults to None.</li>
      <li><code>price</code> (Optional[str], optional): Price to process. Defaults to None.</li>
      <li><code>mexiron_name</code> (Optional[str], optional): Custom Mexiron name. Defaults to None.</li>
      <li><code>urls</code> (Optional[str | List[str]], optional): Product page URLs. Defaults to None.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>bool</code>: True if the scenario executes successfully, False otherwise.</li>
    </ul>
    <p><strong>Raises</strong>:</p>
    <ul>
        <li><code>Exception</code>: Various exceptions during execution.</li>
    </ul>
  </li>
  <li><code>get_graber_by_supplier_url(self, url: str) -> Optional[object]</code>:
    <p><strong>Description</strong>: Returns the appropriate graber for a given supplier URL.</p>
    <p><strong>Args</strong>:</p>
    <ul>
      <li><code>url</code> (str): Supplier page URL.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>Optional[object]</code>: Graber instance if a match is found, None otherwise.</li>
    </ul>
  </li>
  <li><code>convert_product_fields(self, f: ProductFields) -> dict</code>:
    <p><strong>Description</strong>: Converts product fields into a dictionary.</p>
    <p><strong>Args</strong>:</p>
    <ul>
      <li><code>f</code> (ProductFields): Object containing parsed product data.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>dict</code>: Formatted product data dictionary.</li>
    </ul>
  </li>
  <li><code>save_product_data(self, product_data: dict)</code>:
    <p><strong>Description</strong>: Saves individual product data to a file.</p>
    <p><strong>Args</strong>:</p>
    <ul>
      <li><code>product_data</code> (dict): Formatted product data.</li>
    </ul>
  </li>
  <li><code>process_ai(self, products_list: str, attempts: int = 3) -> tuple | bool</code>:
    <p><strong>Description</strong>: Processes the product list through the AI model.</p>
    <p><strong>Args</strong>:</p>
    <ul>
      <li><code>products_list</code> (list): List of product data dictionaries.</li>
      <li><code>attempts</code> (int): Number of attempts to retry processing if failed.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>tuple</code>: Processed response in 'ru' and 'he' formats, or returns `None` if failed.</li>
    </ul>
    <p><strong>Notes</strong>:  Includes error handling and retries for AI responses.</p>
  </li>
  <li><code>post_facebook(self, mexiron: SimpleNamespace) -> bool</code>:
    <p><strong>Description</strong>: Posts data to Facebook.</p>
    <p><strong>Args</strong>:</p>
      <ul>
        <li><code>mexiron</code> (SimpleNamespace): Data to post.</li>
      </ul>
      <p><strong>Returns</strong>:</p>
      <ul>
        <li><code>bool</code>: True if successful, False otherwise.</li>
      </ul>
      <p><strong>Raises</strong>:</p>
        <ul>
          <li><code>Exception</code>: Error posting to Facebook.</li>
        </ul>
  </li>
  <li><code>create_report(self)</code>:
    <p><strong>Description</strong>: Creates a report.</p>
  </li>
</ul>


<h2>Functions</h2>


<!-- Add documentation for functions here -->

<!-- Function documentation will be added here, if necessary.  There are no functions in the current code snippet -->

<!-- Add sections for any other elements of the file (e.g., data structures, constants) as needed -->