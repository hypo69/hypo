html
<h1>Module: hypotez/src/utils/image</h1>

<h2>Overview</h2>
<p>This module provides asynchronous functions to download, save, and retrieve image data.</p>

<h2>Functions</h2>

<h3><code>save_png_from_url</code></h3>

<p><strong>Description</strong>: Download an image from a URL and save it locally asynchronously.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>image_url</code> (str): The URL to download the image from.</li>
  <li><code>filename</code> (str | Path): The name of the file to save the image to.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>str | None</code>: The path to the saved file or <code>None</code> if the operation failed.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>:  Description of general errors during the download process.</li>
</ul>

<h3><code>save_png</code></h3>

<p><strong>Description</strong>: Save an image in PNG format asynchronously.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>image_data</code> (bytes): The binary image data.</li>
  <li><code>file_name</code> (str | Path): The name of the file to save the image to.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>str | None</code>: The path to the saved file or <code>None</code> if the operation failed.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>: Description of general errors during the saving process, including file not created, empty file, and others.</li>
</ul>


<h3><code>get_image_data</code></h3>

<p><strong>Description</strong>: Retrieve binary data of a file if it exists.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>file_name</code> (str | Path): The name of the file to read.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>bytes | None</code>: The binary data of the file if it exists, or <code>None</code> if the file is not found or an error occurred.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>: Description of general errors during file reading.</li>
</ul>