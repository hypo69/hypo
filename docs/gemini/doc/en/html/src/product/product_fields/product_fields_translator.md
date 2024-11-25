html
<h1>Module: product_fields_translator</h1>

<h2>Overview</h2>
<p>This module provides functions for translating product fields to the client database language. It handles various aspects of language identification and translation from the PrestaShop system to the client database.</p>

<h2>Constants</h2>

<h3><code>MODE</code></h3>

<p><strong>Description</strong>: Defines the operating mode of the module.  Currently set to 'dev'.</p>


<h2>Functions</h2>

<h3><code>rearrange_language_keys</code></h3>

<p><strong>Description</strong>: Updates the language identifier in the `presta_fields_dict` dictionary to match the client language schema if the page language matches.  This ensures consistency in language identifiers.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>presta_fields_dict</code> (dict): The dictionary containing the product fields.  Expected to contain nested dictionaries for each language, with a 'language' key.</li>
  <li><code>client_langs_schema</code> (list | dict): The schema defining the client's available languages.  Expected to contain dictionaries with 'locale', 'iso_code', 'language_code', and 'id' keys.</li>
  <li><code>page_lang</code> (str): The language code of the page.  Used to match the client language.  If not provided, the function may attempt to determine the language from the content.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>dict</code>: The updated `presta_fields_dict` with language identifiers changed to match the client language schema.</li>
</ul>


<h3><code>translate_presta_fields_dict</code></h3>

<p><strong>Description</strong>: Translates multilingual product fields to match the client language identifiers.  It retrieves translations from the PrestaShop database and applies them to the product field data.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>presta_fields_dict</code> (dict): The dictionary containing product fields, potentially with multilingual data.</li>
  <li><code>client_langs_schema</code> (list | dict): The schema of the client's languages for translation.  Expected to contain dictionaries of available client languages, with 'id', 'iso_code', 'locale', and 'language_code' keys.</li>
  <li><code>page_lang</code> (str, optional): The language code of the page. If not provided, the function may try to detect the language. Defaults to <code>None</code>.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>dict</code>: The translated `presta_fields_dict` dictionary.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>ProductFieldException</code>:  Potentially raised if errors occur during translation processes (not explicitly shown in the code but assumed to be handled by the `logger`).</li>
</ul>


<h2>External Imports</h2>

<p>The module imports various components from the following packages:</p>
<ul>
 <li><code>pathlib</code></li>
 <li><code>typing</code></li>
 <li><code>gs</code> (likely from the <code>src</code> package)</li>
 <li><code>pprint</code> (likely from the <code>src.utils</code> package)</li>
 <li><code>logger</code> (likely from the <code>src.logger</code> package)</li>
  <li><em>Potentially other imports from the `src` package, indicated by comments.</em></li>
</ul>

<h2>Important Notes</h2>
<p>The code includes placeholders for functions and classes from the <code>src</code> package, which are assumed to provide database interaction, translation retrieval, and logging facilities.</p>
<p>The function `rearrange_language_keys` and `translate_presta_fields_dict` use the  `client_langs_schema` to determine the appropriate `id` for the translated values and use a potentially unreliable method to identify the language from strings.</p>
<p>The code assumes that PrestaShop data has a consistent structure (e.g., `language` key within the dictionaries).  The way exceptions are handled might require improvement.</p>