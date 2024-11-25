html
<h1>Module: categories</h1>

<h2>Overview</h2>
<p>This module contains functions for filtering categories and subcategories from the AliExpress API.</p>

<h2>Functions</h2>

<h3><code>filter_parent_categories</code></h3>

<p><strong>Description</strong>: Filters and returns a list of categories that do not have a parent category.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>categories</code> (List[models.Category | models.ChildCategory]): List of category or child category objects.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>List[models.Category]</code>: List of category objects without a parent category.</li>
</ul>


<h3><code>filter_child_categories</code></h3>

<p><strong>Description</strong>: Filters and returns a list of child categories that belong to the specified parent category.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>categories</code> (List[models.Category | models.ChildCategory]): List of category or child category objects.</li>
  <li><code>parent_category_id</code> (int): The ID of the parent category to filter child categories by.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>List[models.ChildCategory]</code>: List of child category objects with the specified parent category ID.</li>
</ul>

<p><strong>Notes</strong>:</p>
<ul>
  <li>The functions handle cases where input is not a list, converting a single non-category value to a list.</li>
</ul>