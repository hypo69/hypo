html
<h1>Module post_message</h1>

<h2>Overview</h2>
<p>This module contains functions for posting messages on Facebook, including adding titles, descriptions, media, and publishing the post.</p>

<h2>Global Variables</h2>

<h3><code>MODE</code></h3>

<p><strong>Description</strong>: Stores the current mode of operation (e.g., 'dev', 'prod').</p>


<h2>Functions</h2>

<h3><code>post_title</code></h3>

<p><strong>Description</strong>: Sends the title and description of a campaign to the post message box.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>d</code> (Driver): The driver instance used for interacting with the webpage.</li>
  <li><code>message</code> (SimpleNamespace | str): The title and description of the message.  Can be a SimpleNamespace object (containing title and description attributes) or a string representing the message.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>bool</code>: <code>True</code> if the title and description were sent successfully; otherwise, <code>None</code> is implicitly returned by the function. This is the case when the scroll or add post box operations fail.</li>
</ul>

<p><strong>Examples</strong>:</p>
<pre><code>python
driver = Driver(...)
category = SimpleNamespace(title="Campaign Title", description="Campaign Description")
post_title(driver, category)
</code></pre>


<h3><code>upload_media</code></h3>

<p><strong>Description</strong>: Uploads media files to the images section and updates captions.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>d</code> (Driver): The driver instance used for interacting with the webpage.</li>
  <li><code>media</code> (SimpleNamespace | List[SimpleNamespace] | str | list[str]): The media to upload. Can be a single media item (SimpleNamespace, string, or path to a file) or a list of such items.</li>
  <li><code>no_video</code> (bool, optional): If True, skips video upload. Defaults to <code>False</code>.</li>
   <li><code>without_captions</code> (bool, optional): If True, skips caption updates. Defaults to <code>False</code>.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>bool</code>: <code>True</code> if media files were uploaded successfully; otherwise, <code>None</code> is implicitly returned by the function. This can be due to errors in file upload.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>: If there is an error during media upload or caption update.</li>
</ul>

<p><strong>Examples</strong>:</p>
<pre><code>python
driver = Driver(...)
products = [SimpleNamespace(local_saved_image='path/to/image.jpg')]
upload_media(driver, products)
</code></pre>


<h3><code>update_images_captions</code></h3>

<p><strong>Description</strong>: Adds descriptions to uploaded media files.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>d</code> (Driver): The driver instance used for interacting with the webpage.</li>
  <li><code>media</code> (List[SimpleNamespace]): List of products with details to update.</li>
  <li><code>textarea_list</code> (List[WebElement]): List of textareas where captions are added.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>: If there's an error updating the media captions.</li>
</ul>


<h3><code>publish</code></h3>

<p><strong>Description</strong>: Publishes the post.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>d</code> (Driver): The driver instance used for interacting with the webpage.</li>
  <li><code>attempts</code> (int, optional): Number of attempts to publish. Defaults to 5.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>bool</code>: <code>True</code> if the post was published successfully; otherwise, <code>None</code> (implicitly).</li>
</ul>


<h3><code>promote_post</code></h3>

<p><strong>Description</strong>: Manages the process of promoting a post with a title, description, and media files.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>d</code> (Driver): The driver instance used for interacting with the webpage.</li>
  <li><code>category</code> (SimpleNamespace): The category details used for the post title and description.</li>
  <li><code>products</code> (List[SimpleNamespace]): List of products containing media and details to be posted.</li>
   <li><code>no_video</code> (bool, optional): If True, skips video upload. Defaults to <code>False</code>.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>bool</code>: <code>True</code> if the post was promoted successfully; otherwise, <code>None</code> (implicitly).</li>
</ul>


<h3><code>post_message</code></h3>

<p><strong>Description</strong>: Manages the process of promoting a post with a title, description, and media files.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>d</code> (Driver): The driver instance used for interacting with the webpage.</li>
  <li><code>message</code> (SimpleNamespace): The message details used for the post title and description.</li>
  <li><code>no_video</code> (bool, optional): If True, skips video upload. Defaults to <code>False</code>.</li>
  <li><code>images</code> (Optional[str | list[str]], optional): List of image paths (optional). Defaults to <code>None</code>.</li>
  <li><code>without_captions</code> (bool, optional): If True, skips caption updates. Defaults to <code>False</code>.</li>

</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>bool</code>: <code>True</code> if the post was posted successfully; otherwise, <code>None</code> (implicitly).</li>
</ul>