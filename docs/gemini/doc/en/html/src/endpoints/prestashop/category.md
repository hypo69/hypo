html
<h1>Module: hypotez/src/endpoints/prestashop/category.py</h1>

<h2>Overview</h2>
<p>This module defines the <code>PrestaCategory</code> class, providing methods for interacting with PrestaShop categories. It acts as a layer between client categories (PrestaShop) and suppliers, offering functionalities for adding, deleting, updating categories, and retrieving parent categories.</p>


<h2>Classes</h2>

<h3><code>PrestaCategory</code></h3>

<p><strong>Description</strong>: This class handles interactions with PrestaShop categories. It extends the <code>PrestaShop</code> class and provides methods for category management.</p>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__</code>:
    <p><strong>Description</strong>: Initializes the <code>PrestaCategory</code> object.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>credentials</code> (Optional[dict | SimpleNamespace], optional): A dictionary or SimpleNamespace object containing API domain and key. Defaults to <code>None</code>.</li>
      <li><code>api_domain</code> (Optional[str], optional): The API domain. Defaults to <code>None</code>.</li>
      <li><code>api_key</code> (Optional[str], optional): The API key. Defaults to <code>None</code>.</li>
    </ul>
    <p><strong>Raises</strong>:</p>
    <ul>
      <li><code>ValueError</code>: If both <code>api_domain</code> and <code>api_key</code> are not provided.</li>
    </ul>
  </li>
  <li><code>get_parent_categories_list</code>:
    <p><strong>Description</strong>: Retrieves the parent categories for a given category ID.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>id_category</code> (str | int): The ID of the category to find parents for.</li>
      <li><code>parent_categories_list</code> (List[int], optional): An existing list of parent categories to append new results to, enabling recursion. Defaults to an empty list.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>list</code>: A list of parent category IDs.</li>
    </ul>
    <p><strong>Raises</strong>:</p>
    <ul>
      <li><code>ValueError</code>: If <code>id_category</code> is empty.</li>
    <li><code>logger.error</code>: If there's an issue with category retrieval.</li>
    </ul>
     <p><strong>Details</strong>:  The method recursively retrieves parent categories until it finds a category with a parent ID less than or equal to 2 (which represents a root category). </p>
  </li>
</ul>

<h2>Functions</h2>

<!-- No functions are defined in the provided code -->


</ul>