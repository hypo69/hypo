## \file src/translator/__init__.py
## \file src/translator/__init__.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
""" """
...

from packaging.version import Version
from .version import __version__, __doc__, __details__ 
from .product_translator import translate, get_translations_from_presta_translations_table, insert_new_translation_to_presta_translations_table
from .product_translator import translate_record

