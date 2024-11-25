html
<h1>hypotez/src/suppliers/aliexpress/api/models/category.py</h1>

<h2>Overview</h2>
<p>This module defines classes for representing categories and child categories on the AliExpress API. It includes a base `Category` class and a subclass `ChildCategory` to represent hierarchical relationships.</p>

<h2>Classes</h2>

<h3><code>Category</code></h3>

<p><strong>Description</strong>: Represents a general category.</p>

<p><strong>Attributes</strong>:</p>
<ul>
  <li><code>category_id</code> (int): The unique identifier of the category.</li>
  <li><code>category_name</code> (str): The name of the category.</li>
</ul>


<h3><code>ChildCategory</code></h3>

<p><strong>Description</strong>: Represents a child category, inheriting from the `Category` class and adding a parent category identifier.</p>

<p><strong>Attributes</strong>:</p>
<ul>
  <li><code>parent_category_id</code> (int): The unique identifier of the parent category.</li>
  <li><code>category_id</code> (int): The unique identifier of the child category (inherited from `Category`).</li>
  <li><code>category_name</code> (str): The name of the child category (inherited from `Category`).</li>
</ul>