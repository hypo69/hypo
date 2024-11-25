html
<h1>Module: hypotez/src/endpoints/advertisement/facebook/scenarios/post_message_async.py</h1>

<h2>Overview</h2>
<p>This module contains asynchronous functions for posting messages to Facebook, specifically for advertisement campaigns from AliExpress.</p>

<h2>Constants</h2>

<h3><code>MODE</code></h3>

<p><strong>Description</strong>: A string representing the current mode of operation (e.g., 'dev', 'prod').</p>


<h2>Functions</h2>

<h3><code>post_title</code></h3>

<p><strong>Description</strong>: Sends the title and description of a campaign to the post message box.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>d</code> (<code>Driver</code>): The driver instance used for interacting with the webpage.</li>
  <li><code>category</code> (<code>SimpleNamespace</code>): The category containing the title and description to be sent.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>bool</code>: <code>True</code> if the title and description were sent successfully, otherwise <code>None</code>.</li>
</ul>

<h3><code>upload_media</code></h3>

<p><strong>Description</strong>: Uploads media files to the images section and updates captions.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>d</code> (<code>Driver</code>): The driver instance used for interacting with the webpage.</li>
  <li><code>products</code> (<code>List[SimpleNamespace]</code>): List of products containing media file paths.</li>
  <li><code>no_video</code> (<code>bool</code>, optional): Flag to exclude video uploads. Defaults to <code>False</code>.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>bool</code>: <code>True</code> if media files were uploaded successfully, otherwise <code>None</code>.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>: If there is an error during media upload or caption update.</li>
</ul>


<h3><code>update_images_captions</code></h3>

<p><strong>Description</strong>: Adds descriptions to uploaded media files asynchronously.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>d</code> (<code>Driver</code>): The driver instance used for interacting with the webpage.</li>
  <li><code>products</code> (<code>List[SimpleNamespace]</code>): List of products with details to update.</li>
  <li><code>textarea_list</code> (<code>List[WebElement]</code>): List of textareas where captions are added.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>: If there's an error updating the media captions.</li>
</ul>



<h3><code>promote_post</code></h3>

<p><strong>Description</strong>: Manages the process of promoting a post with a title, description, and media files.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>d</code> (<code>Driver</code>): The driver instance used for interacting with the webpage.</li>
  <li><code>category</code> (<code>SimpleNamespace</code>): The category details used for the post title and description.</li>
  <li><code>products</code> (<code>List[SimpleNamespace]</code>): List of products containing media and details to be posted.</li>
   <li><code>no_video</code> (<code>bool</code>, optional): Flag to exclude video uploads. Defaults to <code>False</code>.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>bool</code>: True if the post promotion was successful, otherwise <code>None</code>.</li>
</ul>


<p><strong>Examples</strong>:</p>
<ul>
  <li>Illustrative code snippets demonstrating function usage are included.</li>
</ul>