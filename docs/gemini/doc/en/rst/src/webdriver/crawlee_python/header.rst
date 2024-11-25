Crawlee Header Module
=======================

.. module:: hypotez.src.webdriver.crawlee_python.header
   :platform: Windows, Unix
   :synopsis: This module defines functions for setting the project root directory and loading project settings.

Module Description
------------------

This module provides a function `set_project_root` to locate the project's root directory, essential for adding project paths to `sys.path`.  It also loads project settings from a `settings.json` file.  Error handling is incorporated to gracefully manage potential `FileNotFoundError` or `json.JSONDecodeError` exceptions during file loading.

Functions
---------

.. autofunction:: hypotez.src.webdriver.crawlee_python.header.set_project_root
   :noindex:


.. autofunction:: hypotez.src.webdriver.crawlee_python.header.set_project_root
   :members:
   :undoc-members:
   :show-inheritance: