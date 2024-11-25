html
<h1>AliExpress Campaign Management Module</h1>

<h2>Overview</h2>
<p>This module provides functionalities for managing AliExpress campaigns, including campaign creation, editing, promotional campaigns, and data preparation.</p>

<h2>Dependencies</h2>
<ul>
  <li><code>gspread</code>: For interacting with Google Sheets.</li>
  <li><code>pandas</code>: For data manipulation and analysis.</li>
  <li><code>src.settings.gs</code>: Contains settings specific to Google Sheet interactions.</li>
  <li><code>AliCampaignGoogleSheet</code>:  For managing campaign data stored in Google Sheets.</li>
</ul>

<h2>Modules</h2>

<h3><code>ali_campaign_editor.py</code></h3>

<p><strong>Description</strong>: Contains the core logic for editing AliExpress campaigns.</p>

<h3><code>ali_promo_campaign.py</code></h3>

<p><strong>Description</strong>: Manages promotional campaigns for AliExpress.</p>
<p><strong>Dependencies</strong>:
<ul>
  <li><code>from src.suppliers.aliexpress import AliCampaignGoogleSheet</code></li>
</ul></p>

<h3><code>gsheet.py</code></h3>

<p><strong>Description</strong>: Handles interactions with Google Sheets for campaign data.</p>
<p><strong>Dependencies</strong>:
<ul>
  <li><code>gspread</code></li>
  <li><code>pandas</code></li>
  <li><code>src.settings.gs</code></li>
</ul></p>

<h3><code>header.py</code></h3>

<p><strong>Description</strong>: Contains common functions or classes used across the campaign module.</p>

<h3><code>prepare_campaigns.py</code></h3>

<p><strong>Description</strong>: Sets up and organizes necessary data for campaigns.</p>

<h3><code>ttypes.py</code></h3>

<p><strong>Description</strong>: Defines types and structures used in the campaign module.</p>

<h3><code>version.py</code></h3>

<p><strong>Description</strong>: Contains version information for the campaign module.</p>


<h2>Files</h2>
<ul>
    <li><a href="campaign/__init__.py"><code>__init__.py</code></a>: Initializes the campaign module.</li>
</ul>

<h2>Example Scripts</h2>
<ul>
    <li><a href="_examples/_example_prepare_campains.py"><code>_examle_prepare_campains.py</code></a>: Example for preparing campaigns.</li>
    <li><a href="_examples/_example_ali_promo_campaign.py"><code>_example_ali_promo_campaign.py</code></a>: Example for AliExpress promotional campaigns.</li>
    <li><a href="_examples/_example_edit_campaign.py"><code>_example_edit_campaign.py</code></a>: Example for editing campaigns.</li>
     <li><a href="_examples/header.py"><code>header.py</code></a>: Example of common imports and settings.</li>
</ul>

<h2>Testing</h2>
<ul>
    <li><a href="_pytest/guide_test.md"><code>guide_test.md</code></a>: Guide for testing.</li>
    <li><a href="_pytest/test_alipromo_campaign.py"><code>test_alipromo_campaign.py</code></a>: Test script for <code>ali_promo_campaign</code>.</li>
    <li><a href="_pytest/test_campaign_integration.py"><code>test_campaign_integration.py</code></a>: Integration tests.</li>
    <li><a href="_pytest/test_edit_capmaign.py"><code>test_edit_capmaign.py</code></a>: Test script for editing campaigns.</li>
     <li><a href="_pytest/test_prepeare_campaigns.py"><code>test_prepeare_campaigns.py</code></a>: Test script for preparing campaigns.</li>
</ul>

<h2>Documentation</h2>
<ul>
    <li><a href="_docs/campaign.md"><code>campaign.md</code></a>: Documentation for the campaign module.</li>
    <li><a href="_docs/code_instructions.md"><code>code_instructions.md</code></a>: Instructions for coding and using the campaign module.</li>
    <li><a href="_docs/startup_optioins.md"><code>startup_optioins.md</code></a>: Information on startup options.</li>
</ul>


<h2>Graphical Representations</h2>
<ul>
    <li><a href="_dot/aliexpress_campaign.dot"><code>aliexpress_campaign.dot</code></a>: DOT file for campaign structure.</li>
    <li><a href="_mermaid/AliAffiliatedProducts.mer"><code>AliAffiliatedProducts.mer</code></a>: Mermaid diagram for affiliated products.</li>
    <li><a href="_mermaid/aliexpress_campaign.mer"><code>aliexpress_campaign.mer</code></a>: Mermaid diagram for the AliExpress campaign.</li>
</ul>