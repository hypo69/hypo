html
<h1>Module: hypotez/src/suppliers/aliexpress/campaign/_pytest/test_alipromo_campaign.py</h1>

<h2>Overview</h2>
<p>This module contains pytest test cases for the <code>AliPromoCampaign</code> class, verifying its functionality related to campaign data initialization, product retrieval, processing, and saving.</p>

<h2>Fixtures</h2>

<h3><code>campaign</code></h3>

<p><strong>Description</strong>: A fixture that creates an instance of <code>AliPromoCampaign</code> for use in tests, providing a pre-configured campaign object. It takes campaign name, category name, language, and currency as input to initialize the campaign.</p>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>AliPromoCampaign</code>: An instance of the <code>AliPromoCampaign</code> class.</li>
</ul>


<h2>Functions</h2>

<h3><code>test_initialize_campaign</code></h3>

<p><strong>Description</strong>: Tests the <code>initialize_campaign</code> method to ensure the campaign data is correctly initialized, verifying the campaign name and category name after initialization.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>mocker</code>: A Mocker fixture for mocking dependencies.</li>
  <li><code>campaign</code>: A fixture providing a <code>AliPromoCampaign</code> instance.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
</ul>


<h3><code>test_get_category_products_no_json_files</code></h3>

<p><strong>Description</strong>: Tests the <code>get_category_products</code> method when no JSON files are present, verifying that an empty list is returned.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>mocker</code>: A Mocker fixture for mocking dependencies.</li>
  <li><code>campaign</code>: A fixture providing a <code>AliPromoCampaign</code> instance.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
</ul>


<h3><code>test_get_category_products_with_json_files</code></h3>

<p><strong>Description</strong>: Tests the <code>get_category_products</code> method when JSON files exist, verifying that the products are fetched and returned correctly.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>mocker</code>: A Mocker fixture for mocking dependencies.</li>
  <li><code>campaign</code>: A fixture providing a <code>AliPromoCampaign</code> instance.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
</ul>



<h3><code>test_create_product_namespace</code></h3>

<p><strong>Description</strong>: Tests the <code>create_product_namespace</code> method for correctly creating a product namespace from provided data.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>campaign</code>: A fixture providing a <code>AliPromoCampaign</code> instance.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
</ul>


<h3><code>test_create_category_namespace</code></h3>

<p><strong>Description</strong>: Tests the <code>create_category_namespace</code> method for correctly creating a category namespace from provided data.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>campaign</code>: A fixture providing a <code>AliPromoCampaign</code> instance.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
</ul>


<h3><code>test_create_campaign_namespace</code></h3>

<p><strong>Description</strong>: Tests the <code>create_campaign_namespace</code> method for correctly creating a campaign namespace from provided data, checking the campaign name and title after creation.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>campaign</code>: A fixture providing a <code>AliPromoCampaign</code> instance.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
</ul>



<h3><code>test_prepare_products</code></h3>

<p><strong>Description</strong>: Tests the <code>prepare_products</code> method, verifying that it calls the <code>process_affiliate_products</code> method.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>mocker</code>: A Mocker fixture for mocking dependencies.</li>
  <li><code>campaign</code>: A fixture providing a <code>AliPromoCampaign</code> instance.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
</ul>



<h3><code>test_fetch_product_data</code></h3>

<p><strong>Description</strong>: Tests the <code>fetch_product_data</code> method for correctly fetching product data from product IDs and the returned data.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>mocker</code>: A Mocker fixture for mocking dependencies.</li>
  <li><code>campaign</code>: A fixture providing a <code>AliPromoCampaign</code> instance.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
</ul>



<h3><code>test_save_product</code></h3>

<p><strong>Description</strong>: Tests the <code>save_product</code> method, verifying that the product data is saved to a file correctly.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>mocker</code>: A Mocker fixture for mocking dependencies.</li>
  <li><code>campaign</code>: A fixture providing a <code>AliPromoCampaign</code> instance.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
</ul>


<h3><code>test_list_campaign_products</code></h3>

<p><strong>Description</strong>: Tests the <code>list_campaign_products</code> method for correctly listing the product titles.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>campaign</code>: A fixture providing a <code>AliPromoCampaign</code> instance.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
</ul>