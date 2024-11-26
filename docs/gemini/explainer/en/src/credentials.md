## File hypotez/src/credentials.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src 
	:platform: Windows, Unix
	:synopsis: Global Project Settings: paths, passwords, logins, and API settings

"""
MODE = 'dev'


import datetime
from datetime import datetime
import getpass
import os
import sys
import json
import warnings
from dataclasses import dataclass, field
from pathlib import Path
from types import SimpleNamespace
from typing import Optional

from pydantic import BaseModel, Field
from pykeepass import PyKeePass

from src.check_release import check_latest_release
from src.logger.logger import logger
from src.logger.exceptions import (
    BinaryError,
    CredentialsError,
    DefaultSettingsException,
    HeaderChecksumError,
    KeePassException,
    PayloadChecksumError,
    UnableToSendToRecycleBin,
)
from src.utils.file import read_text_file
from src.utils.jjson import j_loads, j_loads_ns
from src.utils.printer import pprint

def set_project_root(marker_files=('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Finds the root directory of the project starting from the current file's directory,
    searching upwards and stopping at the first directory containing any of the marker files.


    Args:
        marker_files (tuple): Filenames or directory names to identify the project root.
    
    Returns:
        Path: Path to the root directory if found, otherwise the directory where the script is located.
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

def singleton(cls):
    """Декоратор для реализации Singleton."""
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

@singleton
class ProgramSettings(BaseModel):
    """ 
    `ProgramSettings` - класс настроек программы.

    Синглтон, хранящий основные параметры и настройки проекта.
    """
    
    class Config:
        arbitrary_types_allowed = True


    base_dir: Path = Field(default_factory=lambda: set_project_root())
    config: SimpleNamespace = Field(default_factory=lambda: SimpleNamespace())
    credentials: SimpleNamespace = field(default_factory=lambda: SimpleNamespace(
        aliexpress=SimpleNamespace(
            api_key=None,
            secret=None,
            tracking_id=None,
            username=None,
            email=None,
            password=None
        ),
        # ... (other credential sections)
    ))
    MODE: str = Field(default='development')
    path: SimpleNamespace = Field(default_factory=lambda: SimpleNamespace(
        root=None,
        src=None,
        bin=None,
        log=None,
        tmp=None,
        data=None,
        secrets=None,
        google_drive=None,
        external_storage=None,
        dev_null='nul' if sys.platform == 'win32' else '/dev/null'
    ))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #Loads config from json file
        self.config = j_loads_ns(self.base_dir / 'src' / 'config.json')
        if not self.config:
            logger.error('Ошибка при загрузке настроек')
            return
        
        #Initializes other attributes.
        self.config.project_name = self.base_dir.name
        self.path = SimpleNamespace(
            root = Path(self.base_dir),
            bin = Path(self.base_dir / 'bin'),
            src = Path(self.base_dir) / 'src',
            endpoints = Path(self.base_dir) / 'src' / 'endpoints',
            secrets = Path(self.base_dir / 'secrets'),
            log = Path(getattr(self.config.path, 'log', self.base_dir / 'log')),
            tmp = Path(getattr(self.config.path, 'tmp', self.base_dir / 'tmp')),
            data = Path(getattr(self.config.path, 'data', self.base_dir / 'data')),
            google_drive = Path(getattr(self.config.path, 'google_drive', self.base_dir / 'google_drive')),
            external_storage = Path(getattr(self.config.path, 'external_storage',  self.base_dir / 'external_storage'))
        )
        # Checks for updates and does something if needed
        if check_latest_release(self.config.git_user, self.config.git):
            ...
        self.MODE = self.config.mode
        #Adds bin directories to the python path.
        self._add_bin_paths()
        self._set_gtk_env()
        warnings.filterwarnings("ignore", category=UserWarning)
        self._load_credentials()
        

    # ... (other methods)

    def _add_bin_paths(self):
        # Adds bin directories to sys.path
        # ...

    def _set_gtk_env(self):
        os.environ['WEASYPRINT_DLL_DIRECTORIES'] = str(self.base_dir / 'bin' / 'gtk' / 'gtk-nsis-pack' / 'bin')

    def _load_credentials(self):
        # Loads credentials from a KeePass database.
        # ... (methods for loading different types of credentials)
    

    def now(self, dformat: str = '%y_%m_%d_%H_%M_%S_%f') -> str:
        """Returns current timestamp in a specific format."""
        timestamp = datetime.now().strftime(dformat)
        return f"{timestamp[:-3]}" #Return only first 3 digits from microseconds



# Global instance of ProgamSettings
gs: ProgramSettings = ProgramSettings()
```

```
<algorithm>
1. **set_project_root(marker_files)**:
    - Takes a tuple of marker files.
    - Starts from the current file's directory.
    - Traverses up the directory hierarchy.
    - Checks if any marker file exists in the current directory.
    - If found, returns the parent directory; otherwise, returns the current file's directory.
    - Example:
        - Input: marker_files = ('pyproject.toml', 'requirements.txt')
        - Starting Directory: /path/to/file
        - Output: /path/to/project_root (if 'pyproject.toml' or 'requirements.txt' exist in that directory)


2. **singleton(cls)**:
    - Decorator to enforce singleton pattern.
    - Creates a dictionary to store instances.
    - Returns a function `get_instance`.
    - Example:
        - `@singleton`
        - Will make sure that multiple calls to `ProgramSettings()` will return the same instance.


3. **ProgramSettings():**
    - Initializes the `ProgramSettings` object.
    - Loads project settings from `config.json`.
    - Calculates paths for important directories, like `src`, `bin`, `log`, `secrets` relative to the project root directory determined by `set_project_root`.
    - Loads credentials from the KeePass database using `_load_credentials` method.
    - Sets environment variables for specific libraries.
    - Example:
        - Loading configuration from `hypotez/src/config.json`.
        - Determining the `base_dir`.
        - Establishing paths for logs and other files.
        - Loading different API keys from a KeePass database.


4. **_load_credentials():**
    - Loads credentials from the KeePass database.
    - Loops through different credential types (e.g., Aliexpress, OpenAI, Discord).
    - Calls specialized methods (_load_aliexpress_credentials, etc.) to load specific credentials from the KeePass database based on predefined groups and paths.
    - Example:
        - Tries to open a KeePass database.
        - If successful, extract Aliexpress API key.
        - Extract other credential types (OpenAI, Gemini, etc.).


5. **_open_kp(retry)**:
    - Attempts to open KeePass database multiple times (retry).
    - Extracts password from a text file to avoid having a password in the git.
    - If the database is successfully opened, returns a PyKeePass instance.
    - Example:
        - Attempts to open KeePass.
        - Tries to read the password from a file.
        - If reading is successful, use that password.
        - If reading is unsuccessful, prompts user for password.

6.  **now():**
    - Returns the current timestamp in a specified format.
    - Example:
        - `now('%y_%m_%d_%H_%M_%S_%f')` returns a string like '23_10_27_10_30_00_123456'
```

```
<explanation>

- **Imports**:
    - `datetime`, `getpass`, `os`, `sys`, `json`, `warnings`: Standard Python libraries for date/time manipulation, password input, file system operations, system-level interactions, JSON encoding/decoding, warnings management, respectively.
    - `dataclasses`, `pathlib`, `types`, `typing`:  Standard Python modules for creating dataclasses, working with file paths, managing different types, and typing hints, respectively.
    - `pydantic`, `pykeepass`: Third-party libraries for data validation and working with KeePass password managers, respectively.
    - `src.*`: Modules from the project's own `src` folder, likely providing functionalities for checking for updates, logging, file handling, and printing.  This modularization is crucial for maintainability and reusability.


- **Classes**:
    - `ProgramSettings(BaseModel)`: This is a crucial class for storing and managing all the project settings, acting as a central repository.
        - `base_dir`: Stores the project's root directory using a default factory. This allows the application to find the root directory relative to where the script is run.
        - `config`: Holds the program's configuration, likely loaded from a JSON file.
        - `credentials`: Stores credentials for various APIs and services (AliExpress, OpenAI, Telegram, etc.), organized as a nested structure using `SimpleNamespace`. This nested structure clearly defines API specific settings.
        - `path`: Stores various file paths related to the project (binaries, source code, logs, etc.) in a way that it's easy to locate and utilize for the different project components.
        - `__init__()`: Initializes the `ProgramSettings` object, loading settings from the `config.json` file and setting up various paths.
        - `_load_credentials()`: Loads credentials from a KeePass database. This is a critical function and has to be carefully reviewed to avoid leaking any sensitive information.


- **Functions**:
    - `set_project_root()`: Finds the root directory of the project.
    - `singleton()`: Decorator to create a singleton class instance. This decorator ensures that only one instance of the `ProgramSettings` class exists throughout the project's execution, which is important to avoid data inconsistencies.

- **Variables**:
    - `MODE`: A string variable that defines the current mode (e.g., 'dev').
    - `gs`: A global instance of the `ProgramSettings` class, which acts as a central repository of project configurations and credentials.


- **Potential Errors/Improvements**:
    - **Security:**  The code directly reads the password from the `password.txt` file. This is extremely vulnerable to attackers.  Storing passwords in clear text is a critical security flaw that should be immediately addressed. Implement a secure way to handle sensitive data, such as encryption or using a secure storage system (e.g., storing the password in a secure configuration management system).
    - **Error Handling:** While error handling is present (using `try...except` blocks), the handling might not be sufficient to address all potential exceptions that can arise during the file operations or database interactions. The logging of failures should be more detailed.
    - **Code Clarity**: The variable naming in the `_load_credentials` methods could be more descriptive (e.g., `kp_load_credentials`).

- **Relationships**:
    - `ProgramSettings` relies on `src.check_release`, `src.logger.logger`, `src.utils.file`, `src.utils.jjson`, `src.utils.printer`, and other `src` modules. These modules are used for update checks, logging, file operations, JSON handling, and output formatting, respectively.
    - `ProgramSettings` has a strong dependency on the KeePass database `credentials.kdbx`.  The `ProgramSettings` class has to be reviewed for potential vulnerabilities, ensuring that authentication is secure and that credentials are handled safely.