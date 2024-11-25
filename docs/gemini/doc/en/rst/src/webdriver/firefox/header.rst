hypotez/src/webdriver/firefox/header.py
=====================================

.. module:: hypotez.src.webdriver.firefox.header
   :platform: Windows, Unix
   :synopsis: This module contains functions for setting the project root directory and loading project settings.


Module Description
------------------

This module provides a function `set_project_root` to find the root directory of the project,
ensuring that it is added to the Python path. It also loads settings from a `settings.json`
file located in the project's root directory and reads documentation from `README.MD`.  It defines
several constants (`MODE`, `__project_name__`, `__version__`, `__doc__`, `__details__`, `__author__`,
`__copyright__`, `__cofee__`).  All of these variables are initialized with default values
in case a `settings.json` or `README.MD` is missing.


Functions
---------

.. autofunction:: set_project_root