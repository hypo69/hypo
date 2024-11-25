html
<h1>hypotez/src/suppliers/aliexpress/campaign/_pytest/test_prepeare_campaigns.py</h1>

<h2>Overview</h2>
<p>This file contains pytest tests for functions related to preparing AliExpress campaigns.</p>

<h2>Fixtures</h2>

<h3><code>mock_j_loads</code></h3>

<p><strong>Description</strong>: A pytest fixture that patches the <code>src.utils.jjson.j_loads</code> function, allowing for mocking of JSON loading.</p>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>mock</code>: A mock object for the <code>src.utils.jjson.j_loads</code> function.</li>
</ul>


<h3><code>mock_j_dumps</code></h3>

<p><strong>Description</strong>: A pytest fixture that patches the <code>src.utils.jjson.j_dumps</code> function, allowing for mocking of JSON dumping.</p>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>mock</code>: A mock object for the <code>src.utils.jjson.j_dumps</code> function.</li>
</ul>


<h3><code>mock_logger</code></h3>

<p><strong>Description</strong>: A pytest fixture that patches the <code>src.logger.logger</code> object, allowing for mocking of logging functions.</p>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>mock</code>: A mock object for the <code>src.logger.logger</code> object.</li>
</ul>


<h3><code>mock_get_directory_names</code></h3>

<p><strong>Description</strong>: A pytest fixture that patches the <code>src.utils.get_directory_names</code> function, allowing for mocking of directory name retrieval.</p>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>mock</code>: A mock object for the <code>src.utils.get_directory_names</code> function.</li>
</ul>


<h3><code>mock_ali_promo_campaign</code></h3>

<p><strong>Description</strong>: A pytest fixture that patches the <code>src.suppliers.aliexpress.campaign.AliPromoCampaign</code> class, allowing for mocking of campaign objects.</p>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>mock</code>: A mock object for the <code>src.suppliers.aliexpress.campaign.AliPromoCampaign</code> class.</li>
</ul>


<h2>Functions</h2>

<h3><code>test_update_category_success</code></h3>

<p><strong>Description</strong>: Tests the <code>update_category</code> function with successful JSON loading and dumping.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>mock_j_loads</code>: A mock object for JSON loading.</li>
  <li><code>mock_j_dumps</code>: A mock object for JSON dumping.</li>
  <li><code>mock_logger</code>: A mock object for logging.</li>
  <li><code>mock_json_path</code> (Path): Path to the JSON file.</li>
  <li><code>mock_category</code> (SimpleNamespace): Category data.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>True</code>: Indicates successful execution.</li>
</ul>


<h3><code>test_update_category_failure</code></h3>

<p><strong>Description</strong>: Tests the <code>update_category</code> function with a JSON loading failure.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>mock_j_loads</code>: A mock object for JSON loading.</li>
  <li><code>mock_j_dumps</code>: A mock object for JSON dumping.</li>
  <li><code>mock_logger</code>: A mock object for logging.</li>
  <li><code>mock_json_path</code> (Path): Path to the JSON file.</li>
  <li><code>mock_category</code> (SimpleNamespace): Category data.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>False</code>: Indicates failure.</li>
</ul>


<h3><code>test_process_campaign_category_success</code></h3>

<p><strong>Description</strong>: Tests the <code>process_campaign_category</code> function with successful execution.</p>

<p><strong>Parameters</strong>:</p>
<ul>
<li><code>mock_ali_promo_campaign</code>: A mock object for the AliPromoCampaign class.</li>
<li><code>mock_logger</code>: A mock object for logging.</li>
<li><code>mock_campaign_name</code> (str): Name of the campaign.</li>
<li><code>mock_category_name</code> (str): Name of the category.</li>
<li><code>mock_language</code> (str): Language.</li>
<li><code>mock_currency</code> (str): Currency.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
<li>Non-None Value: Indicates successful execution.</li>
</ul>


<h3><code>test_process_campaign_category_failure</code></h3>

<p><strong>Description</strong>: Tests the <code>process_campaign_category</code> function with a failure within the called function.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li>Same as <code>test_process_campaign_category_success</code></li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
<li><code>None</code>: Indicates failure.</li>
</ul>



<h3><code>test_process_campaign</code></h3>

<p><strong>Description</strong>: Tests the <code>process_campaign</code> function.</p>

<p><strong>Parameters</strong>:</p>
<ul>
 <li><code>mock_get_directory_names</code>: A mock object for getting directory names.</li>
 <li><code>mock_logger</code>: A mock object for logging.</li>
<li><code>mock_campaign_name</code> (str): Name of the campaign.</li>
<li><code>mock_categories</code> (list): List of categories.</li>
<li><code>mock_language</code> (str): Language.</li>
<li><code>mock_currency</code> (str): Currency.</li>
<li><code>mock_force</code> (bool): Force flag.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>list</code> of tuples (category_name, result): Results of processing.</li>
</ul>


<h3><code>test_main</code></h3>

<p><strong>Description</strong>: Tests the <code>main</code> function.</p>

<p><strong>Parameters</strong>:</p>
<ul>
 <li><code>mock_get_directory_names</code>: A mock object for getting directory names.</li>
<li><code>mock_campaign_name</code> (str): Name of the campaign.</li>
<li><code>mock_categories</code> (list): List of categories.</li>
<li><code>mock_language</code> (str): Language.</li>
<li><code>mock_currency</code> (str): Currency.</li>
<li><code>mock_force</code> (bool): Force flag.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>None</code>: Indicates asynchronous function execution.</li>
</ul>