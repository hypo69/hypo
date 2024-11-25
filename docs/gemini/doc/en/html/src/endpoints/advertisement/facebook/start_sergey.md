html
<h1>Module: hypotez/src/endpoints/advertisement/facebook/start_sergey.py</h1>

<h2>Overview</h2>
<p>This module defines functions for launching Facebook advertisement campaigns. It handles campaign setup, execution, and potentially integration with Google Drive for campaign data.</p>

<h2>Constants</h2>

<h3><code>MODE</code></h3>

<p><strong>Description</strong>: Defines the current mode of operation (likely 'dev').</p>


<h2>Functions</h2>

<h3><code>run_campaign</code></h3>

<p><strong>Description</strong>: Launches a Facebook advertisement campaign.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>d</code> (Driver): Instance of the web driver (e.g., Chrome). Required for interacting with the Facebook platform.</li>
  <li><code>promoter_name</code> (str): Name of the advertiser (e.g., 'kazarinov', 'aliexpress').</li>
  <li><code>campaigns</code> (list): List of campaign names/identifiers.</li>
  <li><code>group_file_paths</code> (list): List of file paths to JSON files containing target Facebook groups.</li>
  <li><code>language</code> (str): Language of the campaign (e.g., 'RU', 'HE').</li>
  <li><code>currency</code> (str): Currency for the campaign (e.g., 'ILS').</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>None</code>: This function doesn't explicitly return a value. It runs the campaign logic within the function itself.</li>
</ul>

<h3><code>campaign_cycle</code></h3>

<p><strong>Description</strong>: Manages the looping and execution of multiple campaigns.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>d</code> (Driver): Instance of the web driver.</li>
</ul>


<p><strong>Returns</strong>:</p>
<ul>
  <li><code>True</code>: Indicates successful completion of the campaign cycle.</li>
</ul>


<h3><code>main</code></h3>

<p><strong>Description</strong>: Main function to orchestrate the entire campaign process.</p>

<p><strong>Returns</strong>:</p>
<ul>
<li><code>None</code>: Function runs continuously until interrupted.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>KeyboardInterrupt</code>: Graceful exit when the script is interrupted by the user.</li>
</ul>


<h2>Classes</h2>

(No classes defined in this file)


<h2>Imports</h2>
<p>The module imports various libraries and modules including header, random, time, copy, Path, Google sheets (gs), webdriver, FacebookPromoter, logger and date_time utilities.</p>