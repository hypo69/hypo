html
<h1>Module: hypotez/src/suppliers/aliexpress/campaign/gsheets_check_this_code.py</h1>

<h2>Overview</h2>
<p>This module provides a class <code>AliCampaignGoogleSheet</code> for managing Google Sheets within AliExpress campaigns. It inherits from the <code>SpreadSheet</code> class and offers methods for handling worksheets, recording category and product data, and formatting sheets.</p>

<h2>Classes</h2>

<h3><code>AliCampaignGoogleSheet</code></h3>

<p><strong>Description</strong>: A class for interacting with Google Sheets within AliExpress campaigns. It inherits from the <code>SpreadSheet</code> class and provides enhanced methods for sheet management, data input, and formatting.</p>

<p><strong>Attributes</strong>:</p>
<ul>
  <li><code>spreadsheet_id</code> (str): The ID of the Google Sheets spreadsheet. Value: '1nu4mNNFMzSePlggaaL_QM2vdKVP_NNBl2OG7R9MNrs0'.</li>
  <li><code>spreadsheet</code> (SpreadSheet): The Google Sheets spreadsheet object.</li>
  <li><code>worksheet</code> (Worksheet): The active worksheet.</li>
  <li><code>driver</code> (Driver): WebDriver object for interacting with Google Sheets (defaults to Chrome).</li>
</ul>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__(self, campaign_name: str, language: str | dict = None, currency: str = None)</code>
    <ul>
      <li><strong>Description</strong>: Initializes the <code>AliCampaignGoogleSheet</code> object with the campaign name, optional language and currency parameters.</li>
      <li><strong>Parameters</strong>:
        <ul>
          <li><code>campaign_name</code> (str): The name of the AliExpress campaign.</li>
          <li><code>language</code> (str | dict, optional): The language of the campaign. Defaults to <code>None</code>.</li>
          <li><code>currency</code> (str, optional): The currency of the campaign. Defaults to <code>None</code>.</li>
        </ul>
      </li>
      <li><strong>Raises</strong>: No explicit exception handling.</li>
    </ul>
  </li>
  <li><code>clear(self)</code>
    <ul>
      <li><strong>Description</strong>: Clears the Google Sheet data by deleting product worksheets and cleaning categories sheet data.</li>
      <li><strong>Raises</strong>: Catches any exception during the clear process and logs an error message.</li>
    </ul>
  </li>
  <li><code>delete_products_worksheets(self)</code>
    <ul>
      <li><strong>Description</strong>: Deletes all worksheets from the Google Sheet except 'categories', 'product', and 'product_template'.</li>
      <li><strong>Raises</strong>: Catches exceptions during the deletion process and logs an error message, also re-raises the caught exception for higher-level handling.</li>
    </ul>
  </li>
  <li><code>set_campaign_worksheet(self, campaign: SimpleNamespace)</code>
    <ul>
      <li><strong>Description</strong>: Writes campaign data (name, title, language, currency, description) to the 'campaign' worksheet.</li>
      <li><strong>Parameters</strong>:
        <ul>
          <li><code>campaign</code> (SimpleNamespace): An object containing campaign data.</li>
        </ul>
      </li>
      <li><strong>Raises</strong>: Catches exceptions during the process and logs an error message, also re-raises the caught exception.</li>
    </ul>
  </li>
   <li><code>set_products_worksheet(self, category_name: str)</code>
    <ul>
      <li><strong>Description</strong>: Writes product data (from the specified category) to the respective product worksheet.</li>
      <li><strong>Parameters</strong>:
        <ul>
          <li><code>category_name</code> (str): The name of the category.</li>
        </ul>
      </li>
      <li><strong>Raises</strong>: Catches exceptions during the process and logs an error message, also re-raises the caught exception.</li>
    </ul>
  </li>
   <li><code>set_categories_worksheet(self, categories: SimpleNamespace)</code>
    <ul>
      <li><strong>Description</strong>: Writes category data (name, title, description, tags, product count) to the 'categories' worksheet.</li>
      <li><strong>Parameters</strong>:
        <ul>
          <li><code>categories</code> (SimpleNamespace): An object containing category data.</li>
        </ul>
      </li>
      <li><strong>Raises</strong>: Catches exceptions during the process and logs an error message, also re-raises the caught exception.</li>
    </ul>
  </li>
  <li><code>get_categories(self)</code>
    <ul>
      <li><strong>Description</strong>: Retrieves category data from the 'categories' worksheet.</li>
      <li><strong>Returns</strong>: A list of dictionaries representing category data.</li>
      <li><strong>Raises</strong>: No explicit exception handling.</li>
    </ul>
  </li>
  <li><code>set_category_products(self, category_name: str, products: dict)</code>
    <ul>
      <li><strong>Description</strong>: Writes product data for a specific category to a new worksheet.</li>
      <li><strong>Parameters</strong>:
        <ul>
          <li><code>category_name</code> (str): The name of the category.</li>
          <li><code>products</code> (dict): A dictionary containing product data.</li>
        </ul>
      </li>
      <li><strong>Raises</strong>: Catches exceptions during the process and logs an error message, also re-raises the caught exception.</li>
    </ul>
  </li>
  <li><code>_format_categories_worksheet(self, ws: Worksheet)</code></li>
  <li><code>_format_category_products_worksheet(self, ws: Worksheet)</code></li>


</ul>

<h2>Functions</h2>
<p>(No functions defined in the provided code)</p>