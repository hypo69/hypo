hypotez/src/utils/_examples/header.py
=====================================

.. module:: src.utils._examples
   :platform: Windows, Unix
   :synopsis: This module contains utility functions for the project.


Module Description
------------------

This module provides a function to find the project root directory. It searches upwards from the current file's directory until it finds a directory containing specified marker files.  It also handles potential errors if the marker files are not found or if the settings.json file is malformed, returning `None` in such cases.


Functions
---------

.. autofunction:: set_project_root