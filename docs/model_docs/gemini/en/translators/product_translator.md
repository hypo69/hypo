```rst
Product Translator Module
=========================

This module handles translation of product data. It bridges the gap between
product field dictionaries, translation tables, and translation services.

.. automodule:: hypotez.src.translators.product_translator
    :members:
    :undoc-members:
    :show-inheritance:

Functions
---------

.. autofunction:: get_translations_from_presta_translations_table
    :noindex:

.. autofunction:: insert_new_translation_to_presta_translations_table
    :noindex:


.. autofunction:: translate_record
    :noindex:


Function Details
---------------

`get_translations_from_presta_translations_table`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Retrieves product translations from the PrestaShop translation table.

Args:
    product_reference (str): The reference of the product.
    i18n (str, optional): The locale for the translation (e.g., "en_EN"). Defaults to None.

Returns:
    list: A list of product translations.


`insert_new_translation_to_presta_translations_table`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Inserts a new translation record into the PrestaShop translation table.

Args:
    record (dict): The translation record to insert.


`translate_record`
~~~~~~~~~~~~~~~~~~~

Translates a product record from one locale to another.

Args:
    record (dict): The product record to translate.
    from_locale (str): The source locale.
    to_locale (str): The target locale.

Returns:
    dict: The translated product record.
```
