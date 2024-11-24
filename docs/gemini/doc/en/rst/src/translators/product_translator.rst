hypotez/src/translators/product_translator.py
============================================

.. module:: hypotez.src.translators.product_translator
    :platform: Windows, Unix
    :synopsis: Module for managing translations. Provides a layer of communication between the product field dictionary, the translation table, and translators.


Module Description
------------------

This module handles the translation of product data. It serves as an intermediary between a product's field dictionary, a translation database (likely PrestaShop), and translation services (potentially using OpenAI).  It facilitates retrieving, inserting, and translating product field data.


Functions
---------

.. autofunction:: get_translations_from_presta_translations_table
.. autofunction:: insert_new_translation_to_presta_translations_table
.. autofunction:: translate_record