html
<h1>Module: hypotez/src/suppliers/aliexpress/campaign/__init__.py</h1>

<h2>Overview</h2>
<p>This module provides functions and classes for managing AliExpress advertising campaigns.  It includes tools for editing campaigns, preparing campaigns, and generating HTML reports.</p>

<h2>Constants</h2>

<h3><code>MODE</code></h3>

<p><strong>Description</strong>:  A string representing the mode of operation (e.g., 'dev', 'prod').  Currently set to 'dev'.</p>


<h2>Classes</h2>

<h3><code>AliCampaignEditor</code></h3>

<p><strong>Description</strong>: A class for editing AliExpress campaigns.</p>


<h2>Functions</h2>

<h3><code>process_campaign</code></h3>

<p><strong>Description</strong>: Processes a single AliExpress campaign.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li>No parameters specified in the provided code snippet.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>dict | None</code>:  Returns a dictionary containing campaign information or <code>None</code> if processing fails.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>:  Generic exception for any errors during processing.</li>
</ul>


<h3><code>process_campaign_category</code></h3>

<p><strong>Description</strong>: Processes campaigns within a specific category.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li>No parameters specified in the provided code snippet.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>dict | None</code>: Returns a dictionary containing campaign data or <code>None</code> if processing fails.</li>
</ul>


<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>: Generic exception for any errors during processing.</li>
</ul>


<h3><code>process_all_campaigns</code></h3>

<p><strong>Description</strong>: Processes all AliExpress campaigns.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li>No parameters specified in the provided code snippet.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>dict | None</code>:  Returns a dictionary containing a summary of all campaigns or <code>None</code> if processing fails.</li>
</ul>


<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>: Generic exception for any errors during processing.</li>
</ul>



<h3><code>CategoryHTMLGenerator</code></h3>

<p><strong>Description</strong>: A class to generate HTML for campaign categories.</p>


<h3><code>ProductHTMLGenerator</code></h3>

<p><strong>Description</strong>: A class to generate HTML for campaign products.</p>