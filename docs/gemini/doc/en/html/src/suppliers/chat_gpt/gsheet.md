html
<h1>hypotez/src/suppliers/chat_gpt/gsheet.py</h1>

<h2>Overview</h2>
<p>This module provides a class <code>GptGs</code> for managing Google Sheets within AliExpress campaigns.  It inherits from <code>SpreadSheet</code> and allows writing category and product data, formatting sheets, and handling various operations like clearing data, updating campaign worksheets, and reading/writing category and product data.</p>

<h2>Classes</h2>

<h3><code>GptGs</code></h3>

<p><strong>Description</strong>: Manages Google Sheets for AliExpress campaigns. Inherits from <code>SpreadSheet</code> to manage Google Sheets, write category and product data, and format sheets.</p>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__</code>: Initializes <code>GptGs</code> with the Google Sheets spreadsheet ID.</li>
  <li><code>clear</code>: Clears contents of specified sheets, deleting product sheets and clearing data on category, campaign, and other relevant sheets.</li>
  <li><code>update_chat_worksheet</code>: Writes campaign data to a Google Sheets worksheet, updating the specified `conversation_name` sheet with data from a SimpleNamespace or dictionary.</li>
  <li><code>get_campaign_worksheet</code>: Reads campaign data from the 'campaign' worksheet and returns it as a SimpleNamespace object.</li>
  <li><code>set_category_worksheet</code>: Writes data from a SimpleNamespace object to the 'category' worksheet vertically.</li>
  <li><code>get_category_worksheet</code>: Reads category data from the 'category' worksheet and returns it as a SimpleNamespace object.</li>
  <li><code>set_categories_worksheet</code>: Writes data from a SimpleNamespace object to the 'categories' worksheet, handling multiple categories.</li>
  <li><code>get_categories_worksheet</code>: Reads data from columns A to E, starting from the second row, from the 'categories' worksheet.</li>
  <li><code>set_product_worksheet</code>: Writes product data to a new Google Sheets spreadsheet, copying from a template 'product_template' and creating worksheets for each category.</li>
  <li><code>get_product_worksheet</code>: Reads product data from the 'products' worksheet and returns it as a SimpleNamespace object.</li>
  <li><code>set_products_worksheet</code>: Writes data from a list of SimpleNamespace objects to the 'products' worksheet.</li>
  <li><code>delete_products_worksheets</code>: Deletes all sheets from the Google Sheets spreadsheet except 'categories' and 'product_template'.</li>
  <li><code>save_categories_from_worksheet</code>: Saves edited category data from the Google Sheet.</li>
  <li><code>save_campaign_from_worksheet</code>: Saves edited campaign data from the Google Sheet.</li>
</ul>

</ul>