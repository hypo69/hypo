html
<h1>Module: src.endpoints.kazarinov.react.templates</h1>

<h2>Overview</h2>
<p>This module provides a template for rendering product listings in an HTML format. It utilizes Bootstrap CSS for styling and includes dynamic content for product titles, descriptions, images, and prices.</p>

<h2>Variables</h2>

<h3><code>MODE</code></h3>

<p><strong>Description</strong>: A variable defining the current application mode.  Currently set to 'debug'.</p>


<h2>HTML Structure</h2>

<p><strong>Description</strong>: The HTML template structure used to display product information.</p>

<h3><code>&lt;!DOCTYPE html&gt;</code></h3>

<p><strong>Description</strong>: Specifies the document type as HTML5.</p>

<h3><code>&lt;html lang="{{ language }}"&gt;</code></h3>

<p><strong>Description</strong>: Defines the root element of the HTML document, including the language attribute.</p>

<h3><code>&lt;head&gt;</code></h3>

<p><strong>Description</strong>: Contains meta-information about the HTML document, including character set, viewport settings, title, and style links.</p>

<h3><code>&lt;title&gt;{{ title }}&lt;/title&gt;</code></h3>

<p><strong>Description</strong>: Sets the title of the HTML page.  The value is dynamically inserted using Jinja2 templating.</p>

<h3><code>&lt;link rel="stylesheet" ... &gt;</code></h3>

<p><strong>Description</strong>: Includes Bootstrap CSS for styling the webpage.</p>

<h3><code>&lt;style&gt;...&lt;/style&gt;</code></h3>

<p><strong>Description</strong>: Contains custom CSS styles to enhance the appearance of the rendered page, including color themes, font families, and styling for product cards, price tags, and footers.</p>

<h3><code>&lt;body&gt;</code></h3>

<p><strong>Description</strong>: Contains the visible content of the HTML page.</p>


<h3><code>&lt;div class="container"&gt;...&lt;/div&gt;</code></h3>

<p><strong>Description</strong>: The main container element for the page content, offering responsive design capabilities.</p>

<h3><code>&lt;h1 class="text-center my-5"&gt;{{ title }}&lt;/h1&gt;</code></h3>

<p><strong>Description</strong>: Displays the title of the page, dynamically populated with the variable 'title'.</p>

<h3><code>&lt;p class="lead"&gt;{{ description }}&lt;/p&gt;</code></h3>

<p><strong>Description</strong>: Displays a lead paragraph providing a brief description of the content. Value is dynamically provided by the Jinja2 templating engine.</p>


<h3><code>&lt;div class="row"&gt;...&lt;/div&gt;</code></h3>

<p><strong>Description</strong>: This is a row container to arrange product cards in a grid layout.</p>

<h3><code>{% for product in products %}...{% endfor %}</code></h3>

<p><strong>Description</strong>: A loop through the product data to render the product cards.</p>


<h3><code>&lt;div class="col-md-6 product-card"&gt;...&lt;/div&gt;</code></h3>

<p><strong>Description</strong>: A product card to display individual product details. It has a responsive design using Bootstrap classes.</p>

<h3><code>&lt;img src="{{ product.image_local_saved_path }}" alt="{{ product.product_title }}" class="img-fluid" /&gt;</code></h3>

<p><strong>Description</strong>: Displays the image of the product. Dynamically fetches the image path from the 'product' data.</p>

<h3><code>&lt;h3&gt;{{ product.product_title }}&lt;/h3&gt;</code></h3>
<p><strong>Description</strong>: Displays the title of the product.</p>

<h3><code>&lt;p&gt;{{ product.product_description }}&lt;/p&gt;</code></h3>
<p><strong>Description</strong>: Displays a description of the product.</p>

<h3><code>&lt;div class="footer"&gt;...&lt;/div&gt;</code></h3>

<p><strong>Description</strong>:  A footer section displaying the total price.</p>

<h3><code>&lt;span class="price-tag"&gt;{{ price }} {{ currency }}&lt;/span&gt;</code></h3>

<p><strong>Description</strong>: Displays the calculated price and currency.</p>


<h2>Jinja2 Templating</h2>

<p><strong>Description</strong>: The template uses Jinja2 templating language, indicated by the use of curly braces <code>{{ }}</code>. This allows dynamic insertion of variables into the HTML.</p>

<p>The example demonstrates using <code>{{ title }}</code>, <code>{{ description }}</code>, and the `for` loop with `product in products`.</p>