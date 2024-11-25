html
<h1>Module translate_product_fields</h1>

<h2>Overview</h2>
<p>This module manages product translation operations. It acts as a bridge between the product field dictionary, the translation table, and translation services.</p>

<h2>Functions</h2>

<h3><code>get_translations_from_presta_translations_table</code></h3>

<p><strong>Description</strong>: Retrieves product translations from the PrestaShop translation table.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>product_reference</code> (str): The reference of the product to fetch translations for.</li>
  <li><code>credentials</code> (dict): Credentials for connecting to the translation database.</li>
  <li><code>i18n</code> (str, optional): The target language code (e.g., 'en_EN', 'he_HE', 'ru-RU'). Defaults to None.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>list</code>: A list of product translation records.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>: Generic exception if an error occurs during database interaction.</li>
</ul>

<h3><code>insert_new_translation_to_presta_translations_table</code></h3>

<p><strong>Description</strong>: Inserts a new translation record into the PrestaShop translation table.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>record</code> (dict): The translation record to insert.</li>
  <li><code>credentials</code> (dict): Credentials for connecting to the translation database.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>: Generic exception if an error occurs during database interaction.</li>
</ul>


<h3><code>translate_record</code></h3>

<p><strong>Description</strong>: Translates a product record from one language to another.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>record</code> (dict): The product record to translate.</li>
  <li><code>from_locale</code> (str): The original language code.</li>
  <li><code>to_locale</code> (str): The target language code.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>dict</code>: The translated product record.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>: Generic exception if an error occurs during translation.</li>
</ul>