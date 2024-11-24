credentials.py
============

.. module:: hypotez.src.credentials
   :platform: Windows, Unix
   :synopsis: Global Project Settings: paths, passwords, logins, and API settings


Module Description
------------------

This module defines the `ProgramSettings` class, a singleton that holds essential project parameters and configurations.  It handles loading credentials from a KeePass database, and sets up important paths and environment variables.


Classes
-------

.. autoclass:: hypotez.src.credentials.ProgramSettings
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autofunction:: hypotez.src.credentials.set_project_root
.. autofunction:: hypotez.src.credentials.singleton


Methods
-------

.. automethod:: hypotez.src.credentials.ProgramSettings.__init__
.. automethod:: hypotez.src.credentials.ProgramSettings._load_credentials
.. automethod:: hypotez.src.credentials.ProgramSettings._open_kp
.. automethod:: hypotez.src.credentials.ProgramSettings._load_aliexpress_credentials
.. automethod:: hypotez.src.credentials.ProgramSettings._load_openai_credentials
.. automethod:: hypotez.src.credentials.ProgramSettings._load_gemini_credentials
.. automethod:: hypotez.src.credentials.ProgramSettings._load_telegram_credentials
.. automethod:: hypotez.src.credentials.ProgramSettings._load_discord_credentials
.. automethod:: hypotez.src.credentials.ProgramSettings._load_PrestaShop_credentials
.. automethod:: hypotez.src.credentials.ProgramSettings._load_presta_translations_credentials
.. automethod:: hypotez.src.credentials.ProgramSettings._load_smtp_credentials
.. automethod:: hypotez.src.credentials.ProgramSettings._load_facebook_credentials
.. automethod:: hypotez.src.credentials.ProgramSettings._load_gapi_credentials
.. automethod:: hypotez.src.credentials.ProgramSettings.now