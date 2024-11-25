html
<h1>PrestaCustomer Class Documentation</h1>

<h2>Overview</h2>
<p>This module defines the <code>PrestaCustomer</code> class for interacting with PrestaShop customers. It extends the <code>PrestaShop</code> class and provides methods for adding, deleting, updating, and retrieving customer details.</p>

<h2>Classes</h2>

<h3><code>PrestaCustomer</code></h3>

<p><strong>Description</strong>: A class for interacting with PrestaShop customers. It extends the <code>PrestaShop</code> class, enabling access to customer-specific functionalities.  This class provides methods for various customer operations.</p>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__</code>: Initializes a <code>PrestaCustomer</code> object.
    <ul>
      <li><strong>Parameters</strong>:
          <ul>
            <li><code>credentials</code> (Optional[dict | SimpleNamespace], optional): Dictionary or SimpleNamespace object containing API domain and key. Defaults to None.</li>
            <li><code>api_domain</code> (Optional[str], optional): API domain. Defaults to None.</li>
            <li><code>api_key</code> (Optional[str], optional): API key. Defaults to None.</li>
          </ul>
      </li>
      <li><strong>Description</strong>:  Initializes the PrestaShop client. Retrieves API domain and key from the credentials if provided; otherwise, from the `api_domain` and `api_key` parameters. Validates that both `api_domain` and `api_key` are provided. Raises a <code>ValueError</code> if either is missing.</li>
      <li><strong>Raises</strong>:
          <ul>
            <li><code>ValueError</code>: Raised if both `api_domain` and `api_key` are not provided.</li>
          </ul>
      </li>
      </li>
    </ul>

  <li><code>add_customer_PrestaShop</code>: Adds a new customer to PrestaShop (Placeholder).
      <p><strong>Parameters</strong>: (Placeholder)</p>
      <p><strong>Returns</strong>: (Placeholder)</p>
      <p><strong>Raises</strong>: (Placeholder)</p>
  </li>
  <li><code>delete_customer_PrestaShop</code>: Deletes a customer from PrestaShop (Placeholder).
      <p><strong>Parameters</strong>: (Placeholder)</p>
      <p><strong>Returns</strong>: (Placeholder)</p>
      <p><strong>Raises</strong>: (Placeholder)</p>
  </li>
  <li><code>update_customer_PrestaShop</code>: Updates a customer in PrestaShop (Placeholder).
      <p><strong>Parameters</strong>: (Placeholder)</p>
      <p><strong>Returns</strong>: (Placeholder)</p>
      <p><strong>Raises</strong>: (Placeholder)</p>
  </li>
  <li><code>get_customer_details_PrestaShop</code>: Retrieves customer details from PrestaShop (Placeholder).
      <p><strong>Parameters</strong>: (Placeholder)</p>
      <p><strong>Returns</strong>: (Placeholder)</p>
      <p><strong>Raises</strong>: (Placeholder)</p>
  </li>
</ul>
</ul>

<h2>Functions</h2>
<p>(No functions are present in the provided code snippet.)</p>