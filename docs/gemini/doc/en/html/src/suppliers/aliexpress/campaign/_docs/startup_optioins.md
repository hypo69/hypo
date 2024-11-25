html
<h1>Module: prepare_campaigns</h1>

<h2>Overview</h2>
<p>This module prepares material for advertising campaigns on AliExpress.  It handles initialization, creating campaign and category directories, saving campaign configurations, collecting product data, saving product data, creating promotional materials, reviewing the campaign, and finally publishing it. The module utilizes a step-by-step process as detailed in the provided diagram.</p>

<h2>Functions</h2>

<h3><code>update_category</code></h3>

<p><strong>Description</strong>: Updates a category in a JSON file.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>json_path</code> (Path): Path to the JSON file.</li>
  <li><code>category</code> (SimpleNamespace): Category object to update.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>bool</code>: <code>True</code> if the update is successful; <code>False</code> otherwise.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>: Any exception during JSON file handling or data processing.</li>
</ul>


<h3><code>process_campaign_category</code></h3>

<p><strong>Description</strong>: Processes a specific category within a campaign.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>campaign_name</code> (str): Name of the campaign.</li>
  <li><code>category_name</code> (str): Name of the category.</li>
  <li><code>language</code> (str): Language for the campaign.</li>
  <li><code>currency</code> (str): Currency for the campaign.</li>
  <li><code>force</code> (bool, optional): If <code>True</code>, forces update. Defaults to <code>False</code>.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Optional[bool]</code>: <code>True</code> if successful, <code>False</code> if not.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>: Any exception during category processing.</li>
</ul>


<h3><code>process_campaign</code></h3>

<p><strong>Description</strong>: Processes an entire campaign for all categories.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>campaign_name</code> (str): Name of the advertising campaign.</li>
  <li><code>categories</code> (List[str] | None, optional): List of categories to process. If <code>None</code>, all categories are processed. Defaults to <code>None</code>.</li>
  <li><code>language</code> (str, optional): Language for the campaign. Defaults to 'EN'.</li>
  <li><code>currency</code> (str, optional): Currency for the campaign. Defaults to 'USD'.</li>
  <li><code>force</code> (bool, optional): If <code>True</code>, forces update of the categories. Defaults to <code>False</code>.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>None</code>:  This function returns no explicit value. It processes and logs results.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>: Any exception during campaign processing.</li>
</ul>



<h3><code>main</code></h3>

<p><strong>Description</strong>: Asynchronous main function for campaign processing.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>campaign_name</code> (str): Name of the campaign.</li>
  <li><code>categories</code> (List[str]): List of categories.</li>
  <li><code>language</code> (str): Language of the campaign.</li>
  <li><code>currency</code> (str): Currency of the campaign.</li>
  <li><code>force</code> (bool, optional): If <code>True</code>, forces update. Defaults to <code>False</code>.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>None</code>: Asynchronous function.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>: Any exception during asynchronous processing.</li>
</ul>



<h2>Usage Example</h2>

<p>To run the script for a campaign named "summer_sale" processing categories "electronics" and "fashion" in English (EN) and USD currency, use:</p>

<pre><code>bash
python src/suppliers/aliexpress/campaigns/prepare_campaigns.py summer_sale -c electronics fashion -l EN -cu USD -f
</code></pre>