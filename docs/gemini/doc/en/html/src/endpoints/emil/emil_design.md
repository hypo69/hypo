html
<h1>EmilDesign Module Documentation</h1>

<h2>Overview</h2>
<p>This module manages and processes images, promoting them to Facebook and PrestaShop. It utilizes various libraries for image description, Facebook posting, and PrestaShop integration.</p>

<h2>Classes</h2>

<h3><code>EmilDesign</code></h3>

<p><strong>Description</strong>: A class for designing and promoting images through various platforms.</p>

<p><strong>Attributes</strong>:</p>
<ul>
<li><code>base_path</code> (<code>Path</code>): Base path for module data, located in Google Drive.</li>
</ul>

<p><strong>Methods</strong>:</p>
<ul>
<li><code>__init__</code>:
<p><strong>Description</strong>: Initializes the <code>EmilDesign</code> class.</p>
</li>
<li><code>describe_images</code>:
<p><strong>Description</strong>: Describes images based on provided instructions and examples. Utilizes an AI model to generate descriptions. Saves the descriptions to a JSON file.</p>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>from_url</code> (<code>str</code>, optional): If True, uses URL to describe images. Defaults to False.</li>
</ul>
<p><strong>Raises</strong>:</p>
<ul>
<li>No specific exceptions are listed in the code.</li>
</ul>
</li>
<li><code>promote_to_facebook</code>:
<p><strong>Description</strong>: Promotes images and their descriptions to Facebook. Logs into Facebook and posts messages based on the image descriptions.</p>
<p><strong>Raises</strong>:</p>
<ul>
<li>No specific exceptions are listed in the code.</li>
</ul>
</li>
<li><code>upload_to_PrestaShop</code>:
<p><strong>Description</strong>: Uploads product information to PrestaShop. Initializes a product and PrestaShop instance for uploading data.</p>
<p><strong>Raises</strong>:</p>
<ul>
<li>No specific exceptions are listed in the code.</li>
</ul>
</li>
</ul>

<h2>Functions</h2>
<p>(None)</p>


<h2>Global Variables</h2>
<p>
<ul>
  <li><code>MODE</code>: (<code>str</code>):  Indicates the current mode ('dev').
</li>
</ul>
</p>

</ul>