rst
How to use the `credentials.py` module
=========================================================================================

Description
-------------------------
This Python module (`hypotez/src/credentials.py`) defines a `ProgramSettings` class. This class is a singleton designed to hold global project settings, including paths, passwords, logins, and API keys.  It reads configuration data from a `config.json` file and retrieves credentials from a KeePass database.  Critically, it manages the project root directory and ensures that necessary paths are added to the Python path. It also handles loading credentials for various services (e.g., Aliexpress, OpenAI, PrestaShop) from the KeePass database.

Execution steps
-------------------------
1. **Import the module:**
   ```python
   from hypotez.src.credentials import ProgramSettings
   ```

2. **Instantiate the singleton:**
   ```python
   settings = ProgramSettings()
   ```
   This creates a global instance of the `ProgramSettings` class.  The constructor automatically reads the configuration file and loads credentials.  If the configuration file is not found or an error occurs during the initialization, an error will be logged.

3. **Access settings:**
   ```python
   project_root = settings.path.root  # Access the project root path.
   aliexpress_api_key = settings.credentials.aliexpress.api_key
   # ... access other credentials, paths or settings as needed.
   ```

4. **Use credentials in other parts of your application:**
   The `ProgramSettings` object holds the loaded credentials in its `credentials` attribute (and other settings).  You can use these variables in your other application modules.


Usage example
-------------------------
.. code-block:: python

    from hypotez.src.credentials import ProgramSettings

    settings = ProgramSettings()

    # Access the project root path
    project_root = settings.path.root
    print(f"Project root: {project_root}")

    # Access the Aliexpress API key
    aliexpress_api_key = settings.credentials.aliexpress.api_key
    if aliexpress_api_key:
        print(f"Aliexpress API key: {aliexpress_api_key}")
    else:
        print("Aliexpress API key not found.")

    # Access the path to the config file
    config_file_path = settings.base_dir / 'src' / 'config.json'
    print(f"Config file path: {config_file_path}")