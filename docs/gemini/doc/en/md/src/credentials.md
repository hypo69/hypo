# hypotez/src/credentials.py

## Overview

This module contains the `ProgramSettings` class, a singleton responsible for managing global project settings.  It handles loading credentials from a KeePass database, configuration from a JSON file, and setting up paths.  It also includes functions for finding the project root directory.


## Classes

### `ProgramSettings`

**Description**: This class acts as a singleton to store and manage global program settings, including paths, API keys, and other credentials.  It loads configuration from a JSON file and credentials from a KeePass database file.


**Methods**

- `__init__(self, **kwargs)`: Initializes the `ProgramSettings` object by loading the configuration, setting up project paths, and checking for new releases. It also loads credentials from the KeePass database.

- `_load_credentials(self) -> None`: Loads credentials from the KeePass database. This method attempts to load credentials for various services (Aliexpress, OpenAI, Gemini, Discord, Telegram, PrestaShop, SMTP, Facebook, GAPI).

- `_open_kp(self, retry: int = 3) -> PyKeePass | None`: Opens the KeePass database file specified by the path (`credentials.kdbx`).  Handles potential exceptions and retries up to 3 times.

- `_load_aliexpress_credentials(self, kp: PyKeePass) -> bool`: Loads Aliexpress API credentials from the KeePass database.


- `_load_openai_credentials(self, kp: PyKeePass) -> bool`: Loads OpenAI API keys and assistant IDs from the KeePass database.

- `_load_gemini_credentials(self, kp: PyKeePass) -> bool`: Loads GoogleAI Gemini API keys from the KeePass database.


- `_load_discord_credentials(self, kp: PyKeePass) -> bool`: Loads Discord application ID, public key, and bot token from the KeePass database.


- `_load_telegram_credentials(self, kp: PyKeePass) -> bool`: Loads Telegram bot token from the KeePass database.

- `_load_PrestaShop_credentials(self, kp: PyKeePass) -> bool`: Loads PrestaShop credentials (including client details) from the KeePass database.

- `_load_presta_translations_credentials(self, kp: PyKeePass) -> bool`: Loads PrestaShop translation credentials from the KeePass database.

- `_load_smtp_credentials(self, kp: PyKeePass) -> bool`: Loads SMTP credentials from the KeePass database.

- `_load_facebook_credentials(self, kp: PyKeePass) -> bool`: Loads Facebook application ID, secret, and access token from the KeePass database.

- `_load_gapi_credentials(self, kp: PyKeePass) -> bool`: Loads Google API credentials from the KeePass database.

- `now(self, dformat: str = '%y_%m_%d_%H_%M_%S_%f') -> str`: Returns the current timestamp in a specified format.


## Functions

### `set_project_root(marker_files=(\'pyproject.toml\', \'requirements.txt\', \'.git\')) -> Path`

**Description**: Finds the root directory of the project starting from the current file's directory.

**Parameters**:

- `marker_files (tuple)`: Filenames or directory names to identify the project root.


**Returns**:

- `Path`: Path to the root directory if found, otherwise the directory where the script is located.


### `singleton(cls)`

**Description**: Decorator for implementing the Singleton pattern.

**Parameters**:

- `cls`: The class to be made a singleton.

**Returns**:

- The singleton instance of the class.


## Module Constants

- `MODE`:  A string variable likely representing the current program mode (e.g., 'dev', 'prod').