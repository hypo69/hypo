html
<h1>AliExpress Campaign Module Documentation</h1>

<h2>Overview</h2>
<p>This module manages and edits AliExpress promotional campaigns. It interacts with Google Sheets for data retrieval and preparation. The module includes functions for initializing campaigns, fetching category products, and preparing product data for use.</p>

<h2>Classes</h2>

<h3><code>AliPromoCampaign</code></h3>

<p><strong>Description</strong>: Manages a single AliExpress promotional campaign.</p>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__(campaign_name: str, category_name: str, language: str, currency: str, force_update: bool = False)</code>
    <p><strong>Description</strong>: Initializes an AliExpress promotional campaign object.
    </p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>campaign_name</code> (str): The name of the campaign.</li>
      <li><code>category_name</code> (str): The name of the category for the campaign.</li>
      <li><code>language</code> (str): The language of the campaign.</li>
      <li><code>currency</code> (str): The currency of the campaign.</li>
      <li><code>force_update</code> (bool, optional): If True, forces an update of campaign data. Defaults to False.</li>
    </ul>
  </li>
  <li><code>initialize_campaign()</code>
    <p><strong>Description</strong>: Initializes the campaign data by loading JSON data, creating a SimpleNamespace for the campaign, and retrieving category products.</p>
  </li>
  <li><code>get_category_from_campaign()</code>
    <p><strong>Description</strong>: Retrieves the category data from the campaign object, ensuring the 'category' attribute exists.</p>
  </li>
   <li><code>get_category_products(force_update: bool = False)</code>
    <p><strong>Description</strong>: Retrieves products for the specified campaign category, optionally forcing an update.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>force_update</code> (bool, optional): If True, forces an update of the product data. Defaults to False.</li>
    </ul>
  </li>
   <li><code>create_product_namespace(**kwargs)</code>
    <p><strong>Description</strong>: Creates a SimpleNamespace object for product data.</p>
  </li>
   <li><code>create_campaign_namespace(**kwargs)</code>
    <p><strong>Description</strong>: Creates a SimpleNamespace object for campaign data.</p>
  </li>
  <li><code>prepare_products()</code>
    <p><strong>Description</strong>: Prepares product data for use by fetching prepared products, reading source files, extracting product IDs, and processing affiliate products.</p>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>List[dict]</code>: A list of prepared product data.</li>
    </ul>
  </li>
</ul>

<h2>Functions</h2>

<h3><code>process_campaign_category(campaign_name, category_name, language, currency, force=False)</code></h3>

<p><strong>Description</strong>: Processes a single campaign category.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>campaign_name</code> (str): The name of the campaign.</li>
  <li><code>category_name</code> (str): The name of the category.</li>
  <li><code>language</code> (str): The language of the campaign.</li>
  <li><code>currency</code> (str): The currency of the campaign.</li>
  <li><code>force</code> (bool, optional): If True, forces an update. Defaults to False.</li>
</ul>


<h3><code>process_campaign(campaign_name, categories, language, currency, force=False)</code></h3>

<p><strong>Description</strong>: Processes a specific campaign.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>campaign_name</code> (str): The name of the campaign.</li>
  <li><code>categories</code> (list): A list of category names.</li>
  <li><code>language</code> (str): The language of the campaign.</li>
  <li><code>currency</code> (str): The currency of the campaign.</li>
  <li><code>force</code> (bool, optional): If True, forces an update. Defaults to False.</li>
</ul>


<h3><code>process_all_campaigns(language, currency, force=True)</code></h3>

<p><strong>Description</strong>: Processes all campaigns.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>language</code> (str): The language of the campaigns.</li>
  <li><code>currency</code> (str): The currency of the campaigns.</li>
  <li><code>force</code> (bool, optional): If True, forces an update. Defaults to True.</li>
</ul>


<h2>Modules Used</h2>
<p>This module uses various Python modules, including those for file operations, JSON handling, Google Sheets interaction, data manipulation (like CSV handling), and error handling (logger). Refer to the code for specific module dependencies.</p>

<h2>Error Handling</h2>
<p>The module utilizes appropriate error handling, catching potential exceptions and reporting them through logging mechanisms. Note the consistent use of 'ex' instead of 'e' in exception blocks.</p>

<h2>Example Usage</h2>
<p>See the provided example usage sections within the module's description for concrete examples on how to leverage its functionalities.</p>