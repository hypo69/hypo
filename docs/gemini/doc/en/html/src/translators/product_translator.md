html
<h1>Module: hypotez/src/translators/product_translator.py</h1>

<h2>Overview</h2>
<p>This module manages product translations. It acts as a bridge between the product field dictionary, the translation table, and translation services.</p>

<h2>Functions</h2>

<h3><code>get_translations_from_presta_translations_table</code></h3>

<p><strong>Description</strong>: Retrieves product translations from the PrestaShop translations table.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>product_reference</code> (str): The reference of the product to retrieve translations for.</li>
  <li><code>i18n</code> (str, optional): The target locale (e.g., "en_EN", "he_HE"). Defaults to None.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>list</code>: A list of product translations.  Returns an empty list if no translations are found.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>: Any exceptions that occur during database interaction.</li>
</ul>


<h3><code>insert_new_translation_to_presta_translations_table</code></h3>

<p><strong>Description</strong>: Inserts a new translation record into the PrestaShop translations table.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>record</code> (dict): The translation record to insert.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>: Any exceptions during database interaction.</li>
</ul>

<h3><code>translate_record</code></h3>

<p><strong>Description</strong>: Translates a product record from one locale to another using an external translation service.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>record</code> (dict): The product record to translate.</li>
  <li><code>from_locale</code> (str): The original locale of the record.</li>
  <li><code>to_locale</code> (str): The target locale for translation.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>dict</code>: The translated product record.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>: Any exceptions during translation process.</li>
</ul>