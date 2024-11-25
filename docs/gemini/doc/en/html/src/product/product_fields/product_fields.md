html
<h1>Module src.product.product_fields</h1>

<h2>Overview</h2>
<p>This module defines the <code>ProductFields</code> class, which encapsulates data for product fields in a PrestaShop database.  It provides methods to load, store, and access various product attributes.  The structure is designed to handle multilingual aspects and potentially multi-store configurations.  Detailed descriptions of each field, along with their data types, are included within the class definition.</p>

<h2>Classes</h2>

<h3><code>ProductFields</code></h3>

<p><strong>Description</strong>: A class for managing product fields in PrestaShop format.  This class loads product field data from a file and provides properties to access and set specific product attributes.  The class is designed to handle various data types, including integers, decimals, strings, and dates, and incorporates error handling mechanisms.</p>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__</code>: Initializes the <code>ProductFields</code> object. Loads product fields from a file and sets up internal data structures.
    <ul>
      <li><strong>Parameters</strong>:
          <ul>
            <li>None</li>
          </ul>
      </li>
      <li><strong>Returns</strong>:
          <ul>
            <li>None</li>
          </ul>
      </li>
    </ul>
  </li>
  <li><code>_load_product_fields_list</code>: Loads a list of product field names from a text file.
    <ul>
      <li><strong>Parameters</strong>:
          <ul>
            <li>None</li>
          </ul>
      </li>
      <li><strong>Returns</strong>:
          <ul>
            <li><code>List[str]</code>: A list of product field names.</li>
          </ul>
      </li>
    </ul>
  </li>
    <li><code>_payload</code>: Loads default values for product fields from a JSON file.
    <ul>
      <li><strong>Parameters</strong>:
          <ul>
            <li>None</li>
          </ul>
      </li>
      <li><strong>Returns</strong>:
          <ul>
            <li><code>bool</code>: True if successful, False otherwise.</li>
          </ul>
      </li>
    </ul>
  </li>
  <li>and many others (properties and methods): Access and set specific product fields (e.g., <code>id_product</code>, <code>name</code>, <code>price</code>, etc.).  Each method follows the documented format, specifying parameters, returns, and possible exceptions.</li>
</ul>


<h2>Functions</h2>

<!-- Function documentation goes here -->


<h2>Attributes</h2>

<!-- Attributes documentation goes here -->


```