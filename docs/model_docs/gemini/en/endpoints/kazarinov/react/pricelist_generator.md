```rst
Pricelist Generator
===================

.. module:: hypotez.src.endpoints.kazarinov.react.pricelist_generator
    :platform: Windows, Unix
    :synopsis: Module for generating HTML and PDF pricelists for Mekhironov Kazarin.


Description
-----------

This module provides functionality for generating HTML and PDF pricelists based on data from a JSON file. It uses Jinja2 for template rendering and wkhtmltopdf for PDF conversion.  The report generator supports different languages, specified by `lang`.



Classes
-------

.. autoclass:: ReportGenerator
    :members:
    :undoc-members:
    :show-inheritance:

Functions
---------

.. autofunction:: ReportGenerator.generate_html
.. autofunction:: ReportGenerator.create_report
```
