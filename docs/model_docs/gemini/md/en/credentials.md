```markdown
# Module: hypotez/src/credentials.py

## Overview

This module defines the `ProgramSettings` class, a singleton responsible for holding project settings, paths, credentials, and API keys. It utilizes the `pydantic` library for data validation and the `PyKeePass` library for retrieving credentials from a KeePass database.  The settings are loaded from a `config.json` file and the credentials from a `credentials.kdbx` file in the `secrets` folder.

## Table of Contents

- [ProgramSettings](#programsettings)
- [Functions](#functions)
    - [`singleton`](#singleton)

## Classes

### `ProgramSettings`

**Description**: This class represents the program's settings.  It's a singleton, ensuring only one instance exists throughout the application. It stores various settings including paths, API keys, and credentials for different services (e.g., AliExpress, OpenAI, PrestaShop).

**Attributes**:

- `base_dir` (Path): The root directory of the project.
- `settings` (SimpleNamespace): A namespace for general settings.
- `credentials` (SimpleNamespace): A namespace containing credentials for various services.  Sub-namespaces exist for different services (e.g., `credentials.aliexpress`).
- `MODE` (str): Operating mode (e.g., 'development', 'production').
- `path` (SimpleNamespace): Namespace containing paths to crucial project directories.
- `config` (SimpleNamespace):  Namespace containing settings loaded from `config.json`.


**Methods**:

- `__init__`: Initializes the `ProgramSettings` object, loading settings and credentials from files. Includes logic for handling different operating systems.
- `_load_credentials`: Loads credentials from the KeePass database, handling potential errors.
- `_open_kp`: Attempts to open the KeePass database and returns a PyKeePass object.  Includes retry logic.
- `_load_{service}_credentials`: Loads credentials for specific services from KeePass, like `_load_aliexpress_credentials`.  Each method handles specific service and potential exceptions.
- `now`: Returns the current timestamp in a specific format.


## Functions

### `singleton`

**Description**: A decorator that implements the Singleton design pattern. Ensures only one instance of a class can be created.

**Parameters**:
- `cls`: The class to be decorated.

**Returns**:
- The `get_instance` function, which is used to retrieve or create a singleton instance of the class.


**Example Usage**:

```python
@singleton
class MySingletonClass:
    # Class definition
    pass

instance1 = MySingletonClass()
instance2 = MySingletonClass()

print(instance1 is instance2)  # Output: True
```

**Note:**  The documentation for the various `_load_{service}_credentials` functions (e.g., `_load_aliexpress_credentials`) is not fully generated because they are very repetitive in structure.  Each function is similar; they all receive a PyKeePass object, attempt to retrieve specific credentials from the database, and return `True` or `None` if successful or not. Each method includes a `try...except` block to handle potential `Exception` during credential retrieval.


```