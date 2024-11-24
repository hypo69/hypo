hypotez/src/endpoints/emil/header.py
====================================

.. module:: hypotez.src.endpoints.emil.header
   :platform: Windows, Unix
   :synopsis: This module contains functions for setting the project root directory and loading project settings.


Module Description
------------------

This module provides a function to determine the project root directory.  It searches upwards from the current file's location until it finds a directory containing specific marker files.  It also handles loading project settings from a JSON file and project documentation from a markdown file.


Functions
---------

.. autofunction:: hypotez.src.endpoints.emil.header.set_project_root