```rst
html2text Module
=================

.. module:: hypotez.src.utils.convertors.html2text
    :platform: Windows, Unix
    :synopsis:  HTML -> Markdown conversion


This module provides functions for converting HTML content to Markdown-formatted text.  It handles various HTML elements, formatting, and entities.


Functions
---------

.. autofunction:: hypotez.src.utils.convertors.html2text.has_key
.. autofunction:: hypotez.src.utils.convertors.html2text.name2cp
.. autofunction:: hypotez.src.utils.convertors.html2text.charref
.. autofunction:: hypotez.src.utils.convertors.html2text.entityref
.. autofunction:: hypotez.src.utils.convertors.html2text.replaceEntities
.. autofunction:: hypotez.src.utils.convertors.html2text.unescape
.. autofunction:: hypotez.src.utils.convertors.html2text.onlywhite
.. autofunction:: hypotez.src.utils.convertors.html2text.optwrap
.. autofunction:: hypotez.src.utils.convertors.html2text.hn
.. autofunction:: hypotez.src.utils.convertors.html2text.dumb_property_dict
.. autofunction:: hypotez.src.utils.convertors.html2text.dumb_css_parser
.. autofunction:: hypotez.src.utils.convertors.html2text.element_style
.. autofunction:: hypotez.src.utils.convertors.html2text.google_list_style
.. autofunction:: hypotez.src.utils.convertors.html2text.google_nest_count
.. autofunction:: hypotez.src.utils.convertors.html2text.google_has_height
.. autofunction:: hypotez.src.utils.convertors.html2text.google_text_emphasis
.. autofunction:: hypotez.src.utils.convertors.html2text.google_fixed_width_font
.. autofunction:: hypotez.src.utils.convertors.html2text.list_numbering_start

Class
------

.. autoclass:: hypotez.src.utils.convertors.html2text._html2text
    :members:
    :undoc-members:
    :show-inheritance:

Other Functions
---------------

.. autofunction:: hypotez.src.utils.convertors.html2text.wrapwrite
.. autofunction:: hypotez.src.utils.convertors.html2text.html2text_file
.. autofunction:: hypotez.src.utils.convertors.html2text.html2text


Class Storage
-------------

.. autoclass:: hypotez.src.utils.convertors.html2text.Storage
    :members:
    :undoc-members:
    :show-inheritance:

Command-line Usage
------------------

This module can be used from the command line to convert HTML files or URLs to Markdown.  See the help message (`-h` or `--help`).
```
