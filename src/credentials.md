```rst
.. module: src.credentials
```
[Русский](https://github.com/hypo69/hypo/tree/master/src/credentials.ru.md)
[Up to Parent](https://github.com/hypo69/hypo/tree/master/src/README.MD)
## Overview

This module contains the `ProgramSettings` class, which implements the Singleton pattern to store global project settings. The class loads and stores credential information (API keys, passwords, etc.) from the `credentials.kdbx` KeePass database file. It also includes the `set_project_root` function to locate the project's root directory.

## Functions

### `set_project_root`

**Description**: Finds the project's root directory starting from the current directory. The search goes up through the directories until a directory containing one of the files in the `marker_files` list is found.

**Parameters**:

- `marker_files` (tuple): A tuple of strings representing file or directory names used to identify the project's root directory. By default, it looks for the following markers: `pyproject.toml`, `requirements.txt`, `.git`.

**Returns**:

- `Path`: The path to the project's root directory if found, otherwise the path to the directory where the script is located.

### `singleton`

**Description**: A decorator to create a singleton class.

**Parameters**:

- `cls`: The class that should be converted into a singleton.

**Returns**:

- `function`: A function that returns an instance of the singleton class.

## Classes

### `ProgramSettings`

**Description**: A class for program settings. It sets up the main parameters and project settings. It loads the configuration from `config.json` and credential data from the `credentials.kdbx` KeePass database file.

**Attributes**:

- `host_name` (str): The host name.
- `base_dir` (Path): The path to the project's root directory.
- `config` (SimpleNamespace): An object containing the project configuration.
- `credentials` (SimpleNamespace): An object containing the credentials.
- `MODE` (str): The project's operation mode (e.g., 'dev', 'prod').
- `path` (SimpleNamespace): An object containing paths to various project directories.

**Methods**:

- `__init__(self, **kwargs)`: Initializes the class instance.
  - Loads the project configuration from `config.json`.
  - Initializes the `path` attribute with paths to various project directories.
  - Calls `check_latest_release` to check for a new project version.
  - Loads credentials from `credentials.kdbx`.
- `_load_credentials(self) -> None`: Loads credentials from KeePass.
- `_open_kp(self, retry: int = 3) -> PyKeePass | None`: Opens the KeePass database. Handles possible exceptions when opening the database.
- `_load_aliexpress_credentials(self, kp: PyKeePass) -> bool`: Loads Aliexpress credentials from KeePass.
- `_load_openai_credentials(self, kp: PyKeePass) -> bool`: Loads OpenAI credentials from KeePass.
- `_load_gemini_credentials(self, kp: PyKeePass) -> bool`: Loads GoogleAI credentials from KeePass.
- `_load_telegram_credentials(self, kp: PyKeePass) -> bool`: Loads Telegram credentials from KeePass.
- `_load_discord_credentials(self, kp: PyKeePass) -> bool`: Loads Discord credentials from KeePass.
- `_load_PrestaShop_credentials(self, kp: PyKeePass) -> bool`: Loads PrestaShop credentials from KeePass.
- `_load_presta_translations_credentials(self, kp: PyKeePass) -> bool`: Loads PrestaShop Translations credentials from KeePass.
- `_load_smtp_credentials(self, kp: PyKeePass) -> bool`: Loads SMTP credentials from KeePass.
- `_load_facebook_credentials(self, kp: PyKeePass) -> bool`: Loads Facebook credentials from KeePass.
- `_load_gapi_credentials(self, kp: PyKeePass) -> bool`: Loads Google API credentials from KeePass.
- `now(self) -> str`: Returns the current timestamp in the format specified in the `config.json` file.

**Possible Exceptions**:

- `BinaryError`: Exception for binary data errors.
- `CredentialsError`: Exception for credential data errors.
- `DefaultSettingsException`: Exception for default settings errors.
- `HeaderChecksumError`: Exception for header checksum errors.
- `KeePassException`: Exception for KeePass database errors.
- `PayloadChecksumError`: Exception for payload checksum errors.
- `UnableToSendToRecycleBin`: Exception for recycle bin sending errors.
- `Exception`: General exception.

## Notes

- The module uses PyKeePass to work with the `credentials.kdbx` file.
- Exception handling blocks (`ex`) are present in the code.
- The password file (`password.txt`) contains passwords in plain text. This is a potential vulnerability. A secure password storage mechanism needs to be developed.

## Initialization and Configuration

When the project starts, it initializes and configures various settings and credentials. This document explains how these values are set and managed.

### Determining the Project's Root Directory

The project automatically determines its root directory by searching upwards from the current file directory for specific marker files (`pyproject.toml`, `requirements.txt`, `.git`). This ensures that the project can find its resources regardless of the current working directory.

```python
def set_project_root(marker_files=('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Finds the project's root directory starting from the current file directory,
    searching upwards and stopping at the first directory containing any of the marker files.
    
    Args:
        marker_files (tuple): File or directory names for identifying the project's root directory.
    
    Returns:
        Path: The path to the root directory if found, otherwise the directory where the script is located.
    """
    __root__:Path
    current_path:Path = Path(__file__).resolve().parent
    __root__ = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__
```

### Loading Configuration

The project loads its default settings from the `config.json` file located in the `src` directory. This JSON file contains various configuration parameters such as:

- **Author Information**: Details about the author.
- **Available Modes**: Supported modes (`dev`, `debug`, `test`, `prod`).
- **Paths**: Directories for logs, temporary files, external storage, and Google Drive.
- **Project Details**: Name, version, and release information of the project.

```python
self.config = j_loads_ns(self.base_dir / 'src' / 'config.json')
if not self.config:
    logger.error('Error loading settings')
    ...
    return

self.config.project_name = self.base_dir.name
```

### Managing Credentials Using KeePass

**What is KeePass?**

KeePass is a free and open-source password manager that securely stores your passwords and other sensitive information in an encrypted database. The database is protected by a master password, which is the only password you need to remember. KeePass uses strong encryption algorithms (such as AES and Twofish) to ensure the security of your data.

**Why is KeePass Good?**

- **Security**: KeePass uses industry-standard encryption to protect your data, making it highly secure against unauthorized access.
- **Portability**: You can store your KeePass database on a USB drive or in cloud storage and access it from multiple devices.
- **Customization**: KeePass allows you to organize your passwords into groups and subgroups, making it easier to manage a large number of credentials.
- **Open Source**: Being an open-source project, KeePass is transparent and can be reviewed by the community for its security.

**How KeePass Works in This Project**

Credentials are securely managed using the KeePass database (`credentials.kdbx`). The master password for this database is handled differently depending on the environment:

- **Development Mode**: The password is read from a file named `password.txt` located in the `secrets` directory.
- **Production Mode**: The password is entered via the console. (Remove the `password.txt` file from the `secrets` directory)

```python
def _open_kp(self, retry: int = 3) -> PyKeePass | None:
    """ Opens the KeePass database
    Args:
        retry (int): Number of retries
    """
    while retry > 0:
        try:
            password:str = Path( self.path.secrets / 'password.txt').read_text(encoding="utf-8") or None
            kp = PyKeePass(str(self.path.secrets / 'credentials.kdbx'), 
                           password = password or getpass.getpass(print('Enter KeePass master password: ').lower()))
            return kp
        except Exception as ex:
            print(f"Failed to open KeePass database. Exception: {ex}, {retry-1} retries left.")
            ...
            retry -= 1
            if retry < 1:
                logger.critical('Failed to open KeePass database after multiple attempts', exc_info=True)
                ...
                sys.exit()
```

### KeePass Database Tree Structure

```
credentials.kdbx
├── suppliers
│   └── aliexpress
│       └── api
│           └── entry (Aliexpress API credentials)
├── openai
│   ├── entry (OpenAI API keys)
│   └── assistants
│       └── entry (OpenAI assistant IDs)
├── gemini
│   └── entry (GoogleAI credentials)
├── telegram
│   └── entry (Telegram credentials)
├── discord
│   └── entry (Discord credentials)
├── prestashop
│   ├── entry (PrestaShop credentials)
│   └── clients
│       └── entry (PrestaShop client credentials)
│   └── translation
│       └── entry (PrestaShop translation credentials)
├── smtp
│   └── entry (SMTP credentials)
├── facebook
│   └── entry (Facebook credentials)
└── google
    └── gapi
        └── entry (Google API credentials)
```

### Detailed Structure Description:

1. **suppliers/aliexpress/api**:
   - Contains Aliexpress API credentials.
   - Example entry: `self.credentials.aliexpress.api_key`, `self.credentials.aliexpress.secret`, `self.credentials.aliexpress.tracking_id`, `self.credentials.aliexpress.email`, `self.credentials.aliexpress.password`.

2. **openai**:
   - Contains OpenAI API keys.
   - Example entry: `self.credentials.openai.api_key`.

3. **openai/assistants**:
   - Contains OpenAI assistant IDs.
   - Example entry: `self.credentials.openai.assistant_id`.

4. **gemini**:
   - Contains GoogleAI credentials.
   - Example entry: `self.credentials.gemini.api_key`.

5. **telegram**:
   - Contains Telegram credentials.
   - Example entry: `self.credentials.telegram.token`.

6. **discord**:
   - Contains Discord credentials.
   - Example entry: `self.credentials.discord.application_id`, `self.credentials.discord.public_key`, `self.credentials.discord.bot_token`.

7. **prestashop**:
   - Contains PrestaShop credentials.
   - Example entry: `self.credentials.presta.client.api_key`, `self.credentials.presta.client.api_domain`, `self.credentials.presta.client.db_server`, `self.credentials.presta.client.db_user`, `self.credentials.presta.client.db_password`.

8. **prestashop/clients**:
   - Contains PrestaShop client credentials.
   - Example entry: `self.credentials.presta.client.api_key`, `self.credentials.presta.client.api_domain`, `self.credentials.presta.client.db_server`, `self.credentials.presta.client.db_user`, `self.credentials.presta.client.db_password`.

9. **prestashop/translation**:
   - Contains PrestaShop translation credentials.
   - Example entry: `self.credentials.presta.translations.server`, `self.credentials.presta.translations.port`, `self.credentials.presta.translations.database`, `self.credentials.presta.translations.user`, `self.credentials.presta.translations.password`.

10. **smtp**:
    - Contains SMTP credentials.
    - Example entry: `self.credentials.smtp.server`, `self.credentials.smtp.port`, `self.credentials.smtp.user`, `self.credentials.smtp.password`.

11. **facebook**:
    - Contains Facebook credentials.
    - Example entry: `self.credentials.facebook.app_id`, `self.credentials.facebook.app_secret`, `self.credentials.facebook.access_token`.

12. **google/gapi**:
    - Contains Google API credentials.
    - Example entry: `self.credentials.gapi.api_key`.

### Notes:
- Each group (`group`) in KeePass corresponds to a specific path (`path`).
- Each entry (`entry`) in a group contains specific credentials.
- The `_load_*_credentials` methods load data from the corresponding groups and entries in the KeePass database and store them in the `self.credentials` object attributes.

### Global Instance of `ProgramSettings`

```python
# Global instance of ProgramSettings
gs: ProgramSettings = ProgramSettings()
```

**Why is this needed?**

This global instance of `ProgramSettings` (`gs`) is created to provide access to the project settings and credentials from anywhere in the code. This way, you don't need to create a new instance of the `ProgramSettings` class every time you need to access settings or credentials.

**How is it used?**

In other project modules, you can import this global instance and use it to access settings and credentials:

```python
from src import gs

# Example usage
api_key = gs.credentials.openai.api_key
```

This simplifies access to settings and credentials, making the code cleaner and more convenient to use.