html
<h1>request_parameters Module</h1>

<h2>Overview</h2>
<p>This module defines classes for specifying parameters used in requests to the AliExpress API.  It includes enums for product types, sorting criteria, and link types.</p>

<h2>Classes</h2>

<h3><code>ProductType</code></h3>

<p><strong>Description</strong>: Defines possible product types for filtering product listings.</p>

<p><strong>Constants</strong>:</p>
<ul>
  <li><code>ALL</code> (str): Represents all product types.</li>
  <li><code>PLAZA</code> (str): Represents Plaza product type.</li>
  <li><code>TMALL</code> (str): Represents Tmall product type.</li>
</ul>

<h3><code>SortBy</code></h3>

<p><strong>Description</strong>: Defines possible sorting criteria for product listings.</p>

<p><strong>Constants</strong>:</p>
<ul>
  <li><code>SALE_PRICE_ASC</code> (str): Sorts by sale price in ascending order.</li>
  <li><code>SALE_PRICE_DESC</code> (str): Sorts by sale price in descending order.</li>
  <li><code>LAST_VOLUME_ASC</code> (str): Sorts by last volume in ascending order.</li>
  <li><code>LAST_VOLUME_DESC</code> (str): Sorts by last volume in descending order.</li>
</ul>

<h3><code>LinkType</code></h3>

<p><strong>Description</strong>: Defines possible types of links.</p>

<p><strong>Constants</strong>:</p>
<ul>
  <li><code>NORMAL</code> (int): Represents a normal link.</li>
  <li><code>HOTLINK</code> (int): Represents a hotlink.</li>
</ul>