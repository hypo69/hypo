hypotez/src/fast_api/header.py
============================

.. module:: hypotez.src.fast_api.header
   :platform: Windows, Unix
   :synopsis: This module provides functions for setting the project root and loading settings from a JSON file.


Project Initialization
----------------------

.. autofunction:: set_project_root
   :noindex:
   :show-inheritance:


   Args:
       marker_files (tuple, optional): A tuple of filenames or directory names to identify the project root. Defaults to ('pyproject.toml', 'requirements.txt', '.git').

   Returns:
       Path: The path to the project root directory. If no marker files are found, returns the directory containing the current script.

Project Root and Settings
------------------------

.. autovariable:: __root__
   :annotation: (Path)
   :noindex:
   :show-inheritance:

   Path to the root directory of the project.


.. autovariable:: settings
   :annotation: (dict)
   :noindex:
   :show-inheritance:

   Dictionary containing project settings loaded from ``settings.json``.


Project Metadata
----------------

.. autovariable:: __project_name__
   :annotation: (str)
   :noindex:
   :show-inheritance:

   Project name.  Defaults to 'hypotez' if settings.json is not found or the key is missing.


.. autovariable:: __version__
   :annotation: (str)
   :noindex:
   :show-inheritance:

   Project version. Defaults to empty string if settings.json is not found or the key is missing.

.. autovariable:: __doc__
   :annotation: (str)
   :noindex:
   :show-inheritance:


   Project documentation. Defaults to empty string if README.MD is not found or the file is empty.

.. autovariable:: __details__
   :annotation: (str)
   :noindex:
   :show-inheritance:

   Project details. Currently empty.

.. autovariable:: __author__
   :annotation: (str)
   :noindex:
   :show-inheritance:

   Author of the project. Defaults to empty string if settings.json is not found or the key is missing.

.. autovariable:: __copyright__
   :annotation: (str)
   :noindex:
   :show-inheritance:

   Copyright information for the project. Defaults to empty string if settings.json is not found or the key is missing.


.. autovariable:: __cofee__
   :annotation: (str)
   :noindex:
   :show-inheritance:

   A link for supporting the developers. Defaults to a specific link if settings.json is not found or the key is missing.