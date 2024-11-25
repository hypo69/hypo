html
<h1>Module: hypotez/src/endpoints/prestashop/language.py</h1>

<h2>Overview</h2>
<p>This module defines the <code>PrestaLanguage</code> class for managing language settings in a PrestaShop store. It inherits from the <code>PrestaShop</code> class and provides methods for adding, deleting, updating, and retrieving language details.</p>

<h2>Classes</h2>

<h3><code>PrestaLanguage</code></h3>

<p><strong>Description</strong>: A class responsible for managing PrestaShop store languages.  Provides methods for interacting with the PrestaShop API to add, delete, update, and retrieve language information. </p>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__</code>: Initializes the <code>PrestaLanguage</code> object.</li>
</ul>


<h2>Functions</h2>


<h3><code>__init__</code></h3>

<p><strong>Description</strong>: Initializes the <code>PrestaLanguage</code> class. </p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>credentials</code> (Optional[dict | SimpleNamespace], optional): A dictionary or a SimpleNamespace object containing the API domain and key. Defaults to None.  If provided, it overrides any individual `api_domain` and `api_key` parameters. </li>
  <li><code>api_domain</code> (Optional[str], optional): The PrestaShop API domain. Defaults to None.  </li>
  <li><code>api_key</code> (Optional[str], optional): The PrestaShop API key. Defaults to None. </li>
</ul>

<p><strong>Returns</strong>:  None</p>


<p><strong>Raises</strong>:</p>
<ul>
  <li><code>ValueError</code>: If both <code>api_domain</code> and <code>api_key</code> are not provided (either directly or via the <code>credentials</code> parameter).</li>
</ul>


<p><strong>Notes</strong>: The <code>credentials</code> parameter is recommended for improved security and code clarity, allowing for the passing of multiple API credentials in a single location.</p>

<p><strong>Example Usage (in Docstring):</strong></p>
<pre><code>python
    prestalanguage = PrestaLanguage(API_DOMAIN=API_DOMAIN, API_KEY=API_KEY)
    prestalanguage.add_language_PrestaShop('English', 'en')
    prestalanguage.delete_language_PrestaShop(3)
    prestalanguage.update_language_PrestaShop(4, 'Updated Language Name')
    print(prestalanguage.get_language_details_PrestaShop(5))
</code></pre>

<p><strong>Important Note</strong>:  The code example provided in the docstring likely contains missing or placeholder values (e.g., `API_DOMAIN`, `API_KEY`).  Ensure these are appropriately defined in your actual implementation. </p>