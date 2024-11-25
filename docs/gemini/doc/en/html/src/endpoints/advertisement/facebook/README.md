html
<h1>Facebook Advertisement Endpoints</h1>

<h2>Overview</h2>
<p>This module provides endpoints for interacting with Facebook advertising APIs.</p>

<h2>Classes</h2>

<h3><code>FacebookAdClient</code></h3>

<p><strong>Description</strong>: A client for interacting with Facebook advertising APIs.</p>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>create_campaign(campaign_data: dict) -> dict | None</code>
    <p><strong>Description</strong>: Creates a new Facebook advertising campaign.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>campaign_data (dict):</code> Data for the new campaign.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>dict | None</code>: The created campaign object or <code>None</code> on failure.</li>
    </ul>
    <p><strong>Raises</strong>:</p>
    <ul>
      <li><code>APIError</code>: Error raised by the Facebook API.</li>
      <li><code>ValueError</code>: Invalid input data.</li>
    </ul>
  </li>
  <li><code>get_campaign_details(campaign_id: str) -> dict | None</code>
    <p><strong>Description</strong>: Retrieves details for a specific Facebook advertising campaign.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>campaign_id (str):</code> ID of the campaign to retrieve.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>dict | None</code>: Campaign details or <code>None</code> on failure or if campaign is not found.</li>
    </ul>
    <p><strong>Raises</strong>:</p>
    <ul>
      <li><code>APIError</code>: Error raised by the Facebook API.</li>
      <li><code>ValueError</code>: Invalid input data.</li>
      <li><code>NotFoundError</code>: The campaign with the specified ID was not found.</li>
    </ul>
  </li>
  <!-- Add other methods here as needed -->
</ul>


<h2>Functions</h2>
<!-- Add functions here if any -->

<!-- Add Table of Contents (TOC) if needed -->