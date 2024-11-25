html2text Module
=================

.. module:: hypotez.src.utils.convertors.html2text
   :platform: Windows, Unix
   :synopsis:  Converts HTML to Markdown-structured text.


Module Description
------------------

This module provides a function (`html2text`) to convert HTML markup into equivalent Markdown text.  It supports various features, including handling entities, wrapping long lines, skipping internal links, using inline links, and more.  Extensive options are available through the command line.  The module also offers flexible configuration options for customizing the output format.


Functions
---------

.. autofunction:: hypotez.src.utils.convertors.html2text.html2text_file
.. autofunction:: hypotez.src.utils.convertors.html2text.html2text
.. autofunction:: hypotez.src.utils.convertors.html2text.wrapwrite
.. autofunction:: hypotez.src.utils.convertors.html2text.unescape
.. autofunction:: hypotez.src.utils.convertors.html2text.replaceEntities
.. autofunction:: hypotez.src.utils.convertors.html2text.entityref
.. autofunction:: hypotez.src.utils.convertors.html2text.charref
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
.. autofunction:: hypotez.src.utils.convertors.html2text._html2text


Classes
-------

.. autoclass:: hypotez.src.utils.convertors.html2text.Storage
   :members:
   
.. autoclass:: hypotez.src.utils.convertors.html2text._html2text
    :members: