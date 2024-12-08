# hypotez/src/credentials.py

## Overview

This module defines the `ProgramSettings` class, a singleton responsible for storing and managing global project settings, including paths, passwords, logins, and API settings. It uses the `PyKeePass` library to securely load credentials from a KeePass database.  The module also includes functions for setting the project root directory.

## Table of Contents

* [Overview](#overview)
* [Classes](#classes)
    * [`ProgramSettings`](#programsettings)
* [Functions](#functions)
    * [`set_project_root`](#set_project_root)
    * [`singleton`](#singleton)
* [Methods](#methods)
    * [`ProgramSettings.__init__`](#programsettingsinit)
    * [`ProgramSettings._open_kp`](#programsettings_open_kp)
    * [`ProgramSettings._load_aliexpress_credentials`](#programsettings_load_aliexpress_credentials)
    * [`ProgramSettings._load_openai_credentials`](#programsettings_load_openai_credentials)
    * [`ProgramSettings._load_gemini_credentials`](#programsettings_load_gemini_credentials)
    * [`ProgramSettings._load_telegram_credentials`](#programsettings_load_telegram_credentials)
    * [`ProgramSettings._load_discord_credentials`](#programsettings_load_discord_credentials)
    * [`ProgramSettings._load_PrestaShop_credentials`](#programsettings_load_prestashop_credentials)
    * [`ProgramSettings._load_smtp_credentials`](#programsettings_load_smtp_credentials)
    * [`ProgramSettings._load_facebook_credentials`](#programsettings_load_facebook_credentials)
    * [`ProgramSettings._load_presta_translations_credentials`](#programsettings_load_presta_translations_credentials)
    * [`ProgramSettings._load_gapi_credentials`](#programsettings_load_gapi_credentials)
    * [`ProgramSettings.now`](#programsettingsnow)



## Classes

### `ProgramSettings`

**Description**: A singleton class representing program settings.  Holds various configurations, paths, and loaded credentials.

**Parameters**:
- `host_name` (str): The hostname of the current machine.
- `base_dir` (Path): The root directory of the project, found using `set_project_root()`.
- `config` (SimpleNamespace): A namespace containing project configuration data from `config.json`.
- `credentials` (SimpleNamespace): A complex namespace containing various API keys, passwords, and configurations.
- `MODE` (str): Operating mode (e.g., 'dev').
- `path` (SimpleNamespace): Namespace containing paths to project directories.

**Methods**:

#### `ProgramSettings.__init__`

**Description**: Initializes the `ProgramSettings` instance. Loads configuration data from `config.json`, sets project paths, and loads credentials from the KeePass database.

#### `ProgramSettings._open_kp`

**Description**: Opens the KeePass database.

**Args**:
    `retry` (int): Number of retries.

**Returns**:
    `PyKeePass` or None: The KeePass database instance if successful, otherwise None.


#### `ProgramSettings._load_credentials`

**Description**: Loads credentials from the KeePass database.


**Raises**:
    `Exception`: Various exceptions if KeePass database access fails or credentials extraction fails for each service.


#### `ProgramSettings._load_aliexpress_credentials`, `_load_openai_credentials`, etc.

**Description**: Methods for loading specific API credentials from the KeePass database, such as Aliexpress, OpenAI, Gemini, Telegram, Discord, PrestaShop, SMTP, Facebook, and GAPI.

**Args**:
    `kp` (`PyKeePass`): The KeePass database instance.

**Returns**:
    `bool`: True if the loading was successful, False otherwise.


#### `ProgramSettings.now`

**Description**: Returns the current timestamp in a specific format.

**Args**:
    `dformat` (str, optional): The desired timestamp format. Defaults to `'%y_%m_%d_%H_%M_%S_%f'`.


**Returns**:
    `str`: The formatted timestamp.


## Functions

### `set_project_root`

**Description**: Finds the root directory of the project.

**Args**:
    `marker_files` (tuple): Filenames or directory names to identify the project root.


**Returns**:
    `Path`: The path to the project root.

### `singleton`

**Description**: A decorator for implementing the Singleton pattern. Ensures only one instance of a class can be created.



##  (Other functions and methods are documented similarly)