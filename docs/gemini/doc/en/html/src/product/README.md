html
<h1>product Module</h1>

<h2>Overview</h2>
<p>The <strong>product</strong> module is responsible for managing all aspects of product data, including processing, validation, and field management. It consists of the following components:</p>
<ol>
  <li><strong>product.py</strong>: Manages the core logic for handling products, including operations such as creating, updating, and deleting product records. It provides functions to process product data and ensures compliance with business rules for managing products within the application.</li>
  <li><strong>product_fields</strong>: Controls the logic related to product fields, handling field validation, formatting, and management. This module ensures that product fields meet the necessary criteria for consistent data entry, enabling accurate and efficient processing of product information.</li>
</ol>

<h2>Modules</h2>

<h3>product.py</h3>
<!-- Add documentation for product.py functions here -->
<!-- Example: -->
<h2>Functions</h2>

<h3><code>create_product</code></h3>

<p><strong>Description</strong>: Creates a new product record.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>product_data</code> (dict): The product data to be added (e.g., name, description, price).</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>dict | None</code>: The created product record if successful, or <code>None</code> if an error occurs.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>ValidationError</code>: If the input data does not meet validation criteria.</li>
  <li><code>DuplicateEntryError</code>: If a product with the same name already exists.</li>
</ul>


<h3><code>update_product</code></h3>

<p><strong>Description</strong>: Updates an existing product record.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>product_id</code> (int): The ID of the product to be updated.</li>
  <li><code>updated_data</code> (dict): The updated product data (e.g., name, description, price).</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>bool</code>: <code>True</code> if the update was successful, <code>False</code> otherwise.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>NotFoundError</code>: If the product with the given ID does not exist.</li>
  <li><code>ValidationError</code>: If the updated data does not meet validation criteria.</li>
</ul>


<!-- Add more functions here as they are defined in product.py -->

<h3>product_fields.py</h3>
<!-- Add documentation for product_fields.py functions here -->
<!-- Example: -->
<h2>Functions</h2>

<h3><code>validate_field</code></h3>

<p><strong>Description</strong>: Validates a product field.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>field_name</code> (str): The name of the field to be validated.</li>
  <li><code>field_value</code> (various types): The value of the field to be validated.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>bool</code>: <code>True</code> if the field is valid, <code>False</code> otherwise.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>InvalidFormatError</code>: If the field value is in an invalid format.</li>
  <li><code>MissingFieldError</code>: If a required field is missing.</li>
</ul>

<!-- Add more functions here as they are defined in product_fields.py -->