html
<h1>HotProductsResponse Model</h1>

<h2>Overview</h2>
<p>This module defines the <code>HotProductsResponse</code> class, which represents a response containing information about hot products from the AliExpress API.  It includes pagination information and a list of <code>Product</code> objects.</p>

<h2>Classes</h2>

<h3><code>HotProductsResponse</code></h3>

<p><strong>Description</strong>: Represents a response containing data about hot products, including pagination details and a list of products.</p>

<p><strong>Attributes</strong>:</p>
<ul>
  <li><code>current_page_no</code> (int): The current page number in the pagination.</li>
  <li><code>current_record_count</code> (int): The number of records on the current page.</li>
  <li><code>total_record_count</code> (int): The total number of records across all pages.</li>
  <li><code>products</code> (List[Product]): A list of <code>Product</code> objects representing the hot products.</li>
</ul>