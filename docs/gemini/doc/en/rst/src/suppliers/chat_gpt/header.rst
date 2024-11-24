hypotez/src/suppliers/chat_gpt/header.py
==========================================

.. module:: hypotez.src.suppliers.chat_gpt.header
   :platform: Windows, Unix
   :synopsis: This module provides functions for setting the project root directory and loading project settings.


Module Description
------------------

This module defines a function `set_project_root` to find the root directory of the project.
It also loads project settings from a JSON file (`settings.json`) and project documentation from a Markdown file (`README.MD`).
It retrieves various project details like name, version, author, copyright, and documentation strings from these files, providing a centralized location for accessing project metadata.


Functions
--------

.. autofunction:: hypotez.src.suppliers.chat_gpt.header.set_project_root