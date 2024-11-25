html
<h1>hypotez/src/endpoints/advertisement/facebook/promoter.py</h1>

<h2>Overview</h2>
<p>This module handles the promotion of messages and events in Facebook groups. It processes campaigns and events, posting them to Facebook groups while avoiding duplicate promotions.</p>

<h2>Constants</h2>

<h3><code>MODE</code></h3>

<p><strong>Description</strong>: Stores the current mode of operation (e.g., 'dev').</p>


<h2>Functions</h2>

<h3><code>get_event_url</code></h3>

<p><strong>Description</strong>: Returns the modified URL for creating an event on Facebook, replacing <code>group_id</code> with the value from the input URL.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>group_url</code> (str): Facebook group URL containing <code>group_id</code>.</li>
  <li><code>event_id</code> (str): Event identifier.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>str</code>: Modified URL for creating the event.</li>
</ul>


<h3><code>FacebookPromoter.__init__</code></h3>

<p><strong>Description</strong>: Initializes the promoter for Facebook groups.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>d</code> (Driver): WebDriver instance for browser automation.</li>
  <li><code>promoter</code> (str): Promoter identifier.</li>
  <li><code>group_file_paths</code> (list[str | Path], optional): List of file paths containing group data. Defaults to getting filenames from a specific Google Drive path.</li>
  <li><code>no_video</code> (bool, optional): Flag to disable videos in posts. Defaults to False.</li>
</ul>


<h3><code>FacebookPromoter.promote</code></h3>

<p><strong>Description</strong>: Promotes a category or event in a Facebook group.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>group</code> (SimpleNamespace): Data about the Facebook group.</li>
  <li><code>item</code> (SimpleNamespace): Data about the item to promote.</li>
  <li><code>is_event</code> (bool, optional): Whether promoting an event. Defaults to False.</li>
  <li><code>language</code> (str, optional): Language for filtering promotions.</li>
  <li><code>currency</code> (str, optional): Currency for filtering promotions.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>bool</code>: True if promotion successful, otherwise False.</li>
</ul>


<h3><code>FacebookPromoter.log_promotion_error</code></h3>

<p><strong>Description</strong>: Logs promotion error for category or event.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>is_event</code> (bool): Whether the promoted item was an event.</li>
  <li><code>item_name</code> (str): Name of the item that failed to promote.</li>
</ul>


<h3><code>FacebookPromoter.update_group_promotion_data</code></h3>

<p><strong>Description</strong>: Updates group promotion data with the new promotion.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>group</code> (SimpleNamespace): Group data.</li>
  <li><code>item_name</code> (str): Name of the item promoted.</li>
  <li><code>is_event</code> (bool, optional): Whether promoting an event. Defaults to False.</li>
</ul>


<h3><code>FacebookPromoter.process_groups</code></h3>

<p><strong>Description</strong>: Processes all groups for the current campaign or event promotion.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>campaign_name</code> (str, optional): Campaign name.</li>
  <li><code>events</code> (list[SimpleNamespace], optional): List of events to promote.</li>
  <li><code>is_event</code> (bool, optional): True if promoting events, otherwise False. Defaults to False.</li>
  <li><code>group_file_paths</code> (list[str], optional): List of file paths containing group data.</li>
  <li><code>group_categories_to_adv</code> (list[str], optional): List of categories to promote. Defaults to ['sales'].</li>
  <li><code>language</code> (str, optional): Language for filtering promotions.</li>
  <li><code>currency</code> (str, optional): Currency for filtering promotions.</li>
</ul>


<h3><code>FacebookPromoter.get_category_item</code></h3>

<p><strong>Description</strong>: Fetches the category item for promotion based on the campaign and promoter.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>campaign_name</code> (str): Name of the campaign.</li>
  <li><code>group</code> (SimpleNamespace): Group data.</li>
  <li><code>language</code> (str): Language for promotions.</li>
  <li><code>currency</code> (str): Currency for promotions.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>SimpleNamespace</code>: Item data.</li>
</ul>


<h3><code>FacebookPromoter.check_interval</code></h3>

<p><strong>Description</strong>: Checks if the required interval has passed for the next promotion.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>group</code> (SimpleNamespace): Group data.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>bool</code>: True if the interval has passed, otherwise False.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>ValueError</code>: If the interval format is invalid.</li>
</ul>


<h3><code>FacebookPromoter.parse_interval</code></h3>

<p><strong>Description</strong>: Converts a string interval to a timedelta object.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>interval</code> (str): Interval in string format (e.g., '1H', '6M').</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>timedelta</code>: Corresponding timedelta object.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>ValueError</code>: If the interval format is invalid.</li>
</ul>


<h3><code>FacebookPromoter.run_campaigns</code></h3>

<p><strong>Description</strong>: Runs the campaign promotion cycle for all groups and categories sequentially.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>campaigns</code> (list[str]): List of campaign names to promote.</li>
  <li><code>group_file_paths</code> (list[str], optional): List of file paths containing group data.</li>
  <li><code>group_categories_to_adv</code> (list[str], optional): List of categories to promote. Defaults to ['sales'].</li>
  <li><code>language</code> (str, optional): Language for filtering promotions.</li>
  <li><code>currency</code> (str, optional): Currency for filtering promotions.</li>
  <li><code>no_video</code> (bool, optional): Flag to disable videos in posts.</li>
</ul>


<h3><code>FacebookPromoter.run_events</code></h3>

<p><strong>Description</strong>: Runs event promotion in all groups sequentially.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>events_names</code> (list[str]): List of event names to promote.</li>
  <li><code>group_file_paths</code> (list[str]): List of file paths containing group data.</li>
</ul>


<h3><code>FacebookPromoter.stop</code></h3>

<p><strong>Description</strong>: Stops the promotion process by quitting the WebDriver instance.</p>


<h2>Classes</h2>

<h3><code>FacebookPromoter</code></h3>

<p><strong>Description</strong>: Class for promoting AliExpress products and events in Facebook groups.</p>


<p><strong>Attributes</strong>:</p>
<ul>
  <li><code>d</code> (Driver): WebDriver instance.</li>
  <li><code>group_file_paths</code> (str | Path): Path to group files.</li>
  <li><code>no_video</code> (bool): Disable video posting.</li>
  <li><code>promoter</code> (str): Promoter identifier.</li>
  <li><code>spinner</code> (spinning_cursor): Spinner object.</li>
</ul>