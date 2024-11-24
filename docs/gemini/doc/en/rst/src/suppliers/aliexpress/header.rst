aliexpress Header Module
=========================

.. module:: hypotez.src.suppliers.aliexpress.header
    :platform: Windows, Unix
    :synopsis: This module contains functions for setting the project root and loading settings.


Module Description
------------------

This module provides functions for setting the project root directory and loading project settings from a JSON file. It leverages the `pathlib` module for file path manipulation and `packaging.version` for version handling.  The module includes error handling for potential `FileNotFoundError` and `json.JSONDecodeError` during settings file loading.

Functions
---------

.. autofunction:: hypotez.src.suppliers.aliexpress.header.set_project_root