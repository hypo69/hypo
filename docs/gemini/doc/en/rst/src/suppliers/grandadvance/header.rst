GrandAdvance Header Module
=========================

.. module:: hypotez.src.suppliers.grandadvance.header
    :platform: Windows, Unix
    :synopsis: This module provides functions for setting the project root directory and loading project settings.


Description
----------

This module defines a function `set_project_root` to find the root directory of the project and adds it to the Python path.  It also attempts to load settings from a JSON file (`settings.json`) and documentation from a Markdown file (`README.MD`).  The module then exposes various project attributes (name, version, author, copyright, etc.) as variables.


Functions
--------

.. autofunction:: hypotez.src.suppliers.grandadvance.header.set_project_root
    :noindex:


Variables
---------

.. autovariable:: hypotez.src.suppliers.grandadvance.header.__root__
    :noindex:


.. autovariable:: hypotez.src.suppliers.grandadvance.header.__project_name__
    :noindex:

.. autovariable:: hypotez.src.suppliers.grandadvance.header.__version__
    :noindex:

.. autovariable:: hypotez.src.suppliers.grandadvance.header.__doc__
    :noindex:

.. autovariable:: hypotez.src.suppliers.grandadvance.header.__details__
    :noindex:

.. autovariable:: hypotez.src.suppliers.grandadvance.header.__author__
    :noindex:

.. autovariable:: hypotez.src.suppliers.grandadvance.header.__copyright__
    :noindex:

.. autovariable:: hypotez.src.suppliers.grandadvance.header.__cofee__
    :noindex:



Example Usage
------------

This example shows how to use the `set_project_root` function and access the loaded project settings.  (Note: This assumes appropriate setup, including the existence of `pyproject.toml`, `requirements.txt`, and `settings.json`).

.. code-block:: python
    from hypotez.src.suppliers.grandadvance.header import set_project_root
    root_directory = set_project_root()
    print(f"Project root: {root_directory}")
    print(f"Project name: {__project_name__}")