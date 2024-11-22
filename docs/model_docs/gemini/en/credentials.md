```rst
hypotez/src/credentials.py
==========================

This module defines the `ProgramSettings` class, a singleton responsible for holding global project settings, paths, credentials, and more. It utilizes the `pydantic` library for data validation and the `pykeepass` library for handling KeePass database interactions.  It also includes functions to load credentials from the database.

.. automodule:: hypotez.src.credentials
    :members:
    :undoc-members:
    :show-inheritance:

Classes
-------

.. autoclass:: hypotez.src.credentials.ProgramSettings
    :members:
    :show-inheritance:

Functions
--------

.. autofunction:: hypotez.src.credentials.singleton
.. autofunction:: hypotez.src.credentials._get_project_root
.. autofunction:: hypotez.src.credentials.ProgramSettings.__init__
.. autofunction:: hypotez.src.credentials.ProgramSettings._load_credentials
.. autofunction:: hypotez.src.credentials.ProgramSettings._open_kp
.. autofunction:: hypotez.src.credentials.ProgramSettings._load_aliexpress_credentials
.. autofunction:: hypotez.src.credentials.ProgramSettings._load_openai_credentials
.. autofunction:: hypotez.src.credentials.ProgramSettings._load_gemini_credentials
.. autofunction:: hypotez.src.credentials.ProgramSettings._load_telegram_credentials
.. autofunction:: hypotez.src.credentials.ProgramSettings._load_discord_credentials
.. autofunction:: hypotez.src.credentials.ProgramSettings._load_PrestaShop_credentials
.. autofunction:: hypotez.src.credentials.ProgramSettings._load_presta_translations_credentials
.. autofunction:: hypotez.src.credentials.ProgramSettings._load_smtp_credentials
.. autofunction:: hypotez.src.credentials.ProgramSettings._load_facebook_credentials
.. autofunction:: hypotez.src.credentials.ProgramSettings._load_gapi_credentials
.. autofunction:: hypotez.src.credentials.ProgramSettings.now


Global Variables
---------------

.. autodata:: hypotez.src.credentials.gs
```
