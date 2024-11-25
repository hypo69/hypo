html
<h1>Module src.suppliers.aliexpress.campaign.gsheet</h1>

<h2>Overview</h2>
<p>This module provides a class <code>AliCampaignGoogleSheet</code> for interacting with Google Sheets within AliExpress campaigns. It inherits from <code>SpreadSheet</code> and offers methods for managing Google Sheets worksheets, recording category and product data, and formatting sheets.</p>

<h2>Classes</h2>

<h3><code>AliCampaignGoogleSheet</code></h3>

<p><strong>Description</strong>: A class for working with Google Sheets within AliExpress campaigns. It inherits from <code>SpreadSheet</code> and provides additional methods for managing Google Sheets worksheets, recording data about categories and products, and formatting sheets.</p>

<p><strong>Attributes</strong>:</p>
<ul>
  <li><code>spreadsheet_id</code> (str): The ID of the Google Sheets spreadsheet.  Value: '1nu4mNNFMzSePlggaaL_QM2vdKVP_NNBl2OG7R9MNrs0'.</li>
  <li><code>spreadsheet</code> (SpreadSheet): The Google Sheets spreadsheet object.</li>
  <li><code>worksheet</code> (Worksheet): The Google Sheets worksheet object.</li>
</ul>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__(self, campaign_name: str, language: str | dict = None, currency: str = None)</code>:
    <p><strong>Description</strong>: Initialize <code>AliCampaignGoogleSheet</code> with specified Google Sheets spreadsheet ID and additional parameters.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>campaign_name</code> (str): The name of the campaign.</li>
      <li><code>language</code> (str | dict, optional): The language for the campaign. Defaults to <code>None</code>.</li>
      <li><code>currency</code> (str, optional): The currency for the campaign. Defaults to <code>None</code>.</li>
    </ul>
    <p><strong>Raises</strong>:</p>
    <ul>
      <li>Exceptions related to spreadsheet interaction.</li>
    </ul>
  </li>
  <li><code>clear(self)</code>:
    <p><strong>Description</strong>: Clear contents. Deletes product sheets and clears data on the categories and other specified sheets.</p>
    <p><strong>Raises</strong>:</p>
    <ul>
      <li><code>Exception</code>: Any error during sheet deletion.</li>
    </ul>
  </li>
  <li><code>delete_products_worksheets(self)</code>:
    <p><strong>Description</strong>: Delete all sheets from the Google Sheets spreadsheet except 'categories' and 'product_template'.</p>
    <p><strong>Raises</strong>:</p>
    <ul>
      <li><code>Exception</code>: Any error during worksheet deletion.</li>
    </ul>
  </li>
  <li><code>set_campaign_worksheet(self, campaign: SimpleNamespace)</code>:
    <p><strong>Description</strong>: Write campaign data to a Google Sheets worksheet.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>campaign</code> (SimpleNamespace): SimpleNamespace object with campaign data fields for writing.</li>
    </ul>
    <p><strong>Raises</strong>:</p>
    <ul>
      <li><code>Exception</code>: Error during campaign data setting.</li>
    </ul>
  </li>
  <li><code>set_products_worksheet(self, category_name: str)</code>:
    <p><strong>Description</strong>: Write data from a list of SimpleNamespace objects to Google Sheets cells.  Retrieves products from the corresponding category.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>category_name</code> (str): The name of the category to fetch products from.</li>
    </ul>
    <p><strong>Raises</strong>:</p>
    <ul>
      <li><code>Exception</code>: Error during product data setting.</li>
    </ul>
  </li>
  <li><code>set_categories_worksheet(self, categories: SimpleNamespace)</code>:
     <p><strong>Description</strong>: Write category data to the 'categories' sheet.</p>
      <p><strong>Parameters</strong>:</p>
      <ul>
        <li><code>categories</code> (SimpleNamespace): SimpleNamespace object containing category data.</li>
      </ul>
      <p><strong>Raises</strong>:</p>
      <ul>
        <li><code>Exception</code>: Error during category data setting.</li>
      </ul>
  </li>
  <li><code>get_categories(self)</code>:
    <p><strong>Description</strong>: Retrieves category data from the 'categories' sheet.</p>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li>list of dicts: Category data as a list of dictionaries.</li>
    </ul>
  </li>
  <li><code>set_category_products(self, category_name: str, products: dict)</code>:
    <p><strong>Description</strong>: Writes product data to the corresponding category sheet.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>category_name</code> (str): The category name.</li>
      <li><code>products</code> (dict): Dictionary containing product data.</li>
    </ul>
    <p><strong>Raises</strong>:</p>
    <ul>
      <li><code>Exception</code>: Error during product data setting.</li>
    </ul>
  </li>
   <li><code>_format_categories_worksheet(self, ws: Worksheet)</code>:
    <p><strong>Description</strong>: Formats the 'categories' sheet.</p>
  </li>
  <li><code>_format_category_products_worksheet(self, ws: Worksheet)</code>:
     <p><strong>Description</strong>: Formats the product sheet of a category.</p>
  </li>


</ul>


<h2>Functions</h2>
<p>(None)</p>