translate_product_fields.py
==========================

.. module:: hypotez.src.translators.translate_product_fields
   :platform: Windows, Unix
   :synopsis: Module for translating product fields. Acts as a connection layer between the product field dictionary, the translation table, and translators.


Functions
--------

.. autofunction:: get_translations_from_presta_translations_table
   :param product_reference:
   :type product_reference: str
   :param credentials:
   :type credentials: dict
   :param i18n:
   :type i18n: str
   :raises TypeError: if input types are incorrect
   :raises ValueError: if input values are invalid
   :returns: list
   :classdoc: Returns a list of product translations. Retrieves product translations from the PrestaShop translation table.


.. autofunction:: insert_new_translation_to_presta_translations_table
   :param record:
   :type record: dict
   :param credentials:
   :type credentials: dict
   :raises TypeError: if input types are incorrect
   :raises ValueError: if input values are invalid
   :returns: None
   :classdoc: Inserts a new translation record into the PrestaShop translation table.


.. autofunction:: translate_record
   :param record:
   :type record: dict
   :param from_locale:
   :type from_locale: str
   :param to_locale:
   :type to_locale: str
   :raises TypeError: if input types are incorrect
   :raises ValueError: if input values are invalid
   :returns: dict
   :classdoc: Translates the product record's fields from one locale to another.