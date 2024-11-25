html
<h1>AliCampaignEditor Module Documentation</h1>

<h2>Overview</h2>
<p>This module provides the editor for advertising campaigns on AliExpress.</p>

<h2>Classes</h2>

<h3><code>AliCampaignEditor</code></h3>

<p><strong>Description</strong>: Editor for advertising campaigns, inheriting from <code>AliPromoCampaign</code>.</p>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__</code>:
    <p><strong>Description</strong>: Initializes the <code>AliCampaignEditor</code> with campaign name, language, currency, and optionally a campaign file.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>campaign_name</code> (str): The name of the campaign.</li>
      <li><code>language</code> (Optional[str | dict], optional): The language of the campaign. Defaults to 'EN'.</li>
      <li><code>currency</code> (Optional[str], optional): The currency for the campaign. Defaults to 'USD'.</li>
      <li><code>campaign_file</code> (Optional[str | Path], optional): Optionally load a `<lang>_<currency>.json` file. Defaults to `None`.</li>
    </ul>
    <p><strong>Raises</strong>:</p>
    <ul>
      <li><code>CriticalError</code>: If neither <code>campaign_name</code> nor <code>campaign_file</code> is provided.</li>
    </ul>
  </li>
  <li><code>delete_product</code>:
    <p><strong>Description</strong>: Deletes a product from the campaign if it doesn't have an affiliate link.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>product_id</code> (str): The ID of the product to delete.</li>
      <li><code>exc_info</code> (bool, optional): Whether to include exception details in the logs. Defaults to `False`.</li>
    </ul>
  </li>
  <li><code>update_product</code>:
    <p><strong>Description</strong>: Updates product details within a specific category.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>category_name</code> (str): Name of the category.</li>
      <li><code>lang</code> (str): Language of the campaign.</li>
      <li><code>product</code> (dict): A dictionary containing product details to update.</li>
    </ul>
  </li>
  <li><code>update_campaign</code>:
    <p><strong>Description</strong>: Updates campaign properties (description, tags, etc.).</p>
  </li>
  <li><code>update_category</code>:
    <p><strong>Description</strong>: Updates a category in a JSON file.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>json_path</code> (Path): Path to the JSON file.</li>
      <li><code>category</code> (SimpleNamespace): Category object to be updated.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li>bool: True if the update was successful, False otherwise.</li>
    </ul>
  </li>
  <li><code>get_category</code>:
    <p><strong>Description</strong>: Retrieves a category from the campaign.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>category_name</code> (str): Name of the category to retrieve.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li>Optional[SimpleNamespace]: The category object, or `None` if not found.</li>
    </ul>
  </li>
  <li><code>list_categories</code>:
    <p><strong>Description</strong>: Returns a list of category names in the campaign.</p>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li>Optional[List[str]]: A list of category names, or `None` if no categories found.</li>
    </ul>
  </li>
  <li><code>get_category_products</code>:
    <p><strong>Description</strong>: Reads product data from JSON files for a specific category.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>category_name</code> (str): Category name.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li>Optional[List[SimpleNamespace]]: A list of product objects, or `None` if no JSON files found.</li>
    </ul>
  </li>
</ul>

<h2>Functions</h2>
<!-- Add function documentation here if any -->


</ul>