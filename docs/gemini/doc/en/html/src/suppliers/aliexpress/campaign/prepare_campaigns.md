html
<h1>Module: prepare_campaigns</h1>

<h2>Overview</h2>
<p>This module prepares AliExpress campaigns by processing categories, handling campaign data, and generating promotional materials. It utilizes the <code>AliCampaignEditor</code> class to interact with campaign data and provides functions for processing single campaigns and all campaigns within a directory.</p>

<h3>Examples</h3>
<p>To run the script for a specific campaign:</p>
<pre><code>python src/suppliers/aliexpress/campaigns/prepare_campaigns.py summer_sale -c electronics -l EN -cu USD
</code></pre>
<p>To process all campaigns:</p>
<pre><code>python src/suppliers/aliexpress/campaigns/prepare_campaigns.py --all -l EN -cu USD
</code></pre>


<h2>Functions</h2>

<h3><code>process_campaign_category</code></h3>

<p><strong>Description</strong>: Processes a specific category within a campaign for a given language and currency.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>campaign_name</code> (str): Name of the advertising campaign.</li>
  <li><code>category_name</code> (str): Category for the campaign.</li>
  <li><code>language</code> (str): Language for the campaign.</li>
  <li><code>currency</code> (str): Currency for the campaign.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>List[str]</code>: List of product titles within the category.  Example: <code>['Product 1', 'Product 2']</code></li>
</ul>


<h3><code>process_campaign</code></h3>

<p><strong>Description</strong>: Processes a campaign and handles the campaign's setup and processing.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>campaign_name</code> (str): Name of the advertising campaign.</li>
  <li><code>language</code> (Optional[str], optional): Language for the campaign. If not provided, process for all locales. Defaults to <code>None</code>.</li>
  <li><code>currency</code> (Optional[str], optional): Currency for the campaign. If not provided, process for all locales. Defaults to <code>None</code>.</li>
  <li><code>campaign_file</code> (Optional[str], optional): Optional path to a specific campaign file. Defaults to <code>None</code>.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>bool</code>: True if campaign processed, else False.</li>
</ul>


<h3><code>process_all_campaigns</code></h3>

<p><strong>Description</strong>: Processes all campaigns in the 'campaigns' directory for the specified language and currency.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>language</code> (Optional[str], optional): Language for the campaigns. Defaults to <code>None</code>.</li>
  <li><code>currency</code> (Optional[str], optional): Currency for the campaigns. Defaults to <code>None</code>.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>None</code></li>
</ul>


<h3><code>main_process</code></h3>

<p><strong>Description</strong>: Main function to process a campaign.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>campaign_name</code> (str): Name of the advertising campaign.</li>
  <li><code>categories</code> (List[str]): List of categories for the campaign. If empty, process the campaign without specific categories.</li>
  <li><code>language</code> (Optional[str], optional): Language for the campaign. Defaults to <code>None</code>.</li>
  <li><code>currency</code> (Optional[str], optional): Currency for the campaign. Defaults to <code>None</code>.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>None</code></li>
</ul>


<h3><code>main</code></h3>

<p><strong>Description</strong>: Main function to parse arguments and initiate processing.</p>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>None</code></li>
</ul>


<h2>Global Variables</h2>

<p><code>campaigns_directory</code></p>
<p>Specifies the path to the directory containing campaign data.</p>

<p><strong>Type</strong>:<code>Path</code></p>


<!-- Add a section for the AliCampaignEditor class and its methods if available -->