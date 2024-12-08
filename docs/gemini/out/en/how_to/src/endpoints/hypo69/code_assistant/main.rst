rst
How to use the code block in main.py
========================================================================================

Description
-------------------------
This Python script (`main.py`) is a command-line interface (CLI) for a code assistant. It allows you to configure and run the assistant with various options, such as selecting a role (e.g., `doc_writer`, `code_checker`), specifying languages (`ru`, `en`), choosing models (`gemini`, `openai`), and providing directories to process.  It can either load settings from a JSON file or accept command-line parameters to customize the assistant's behavior.

Execution steps
-------------------------
1. **Import necessary modules**: The script begins by importing the `argparse`, `json`, `pathlib`, and `CodeAssistant` modules.

2. **`parse_args()` function**: This function parses command-line arguments using `argparse`.  It defines options for:
    - `--settings`: Path to a JSON configuration file.
    - `--role`: Role of the code assistant (`code_checker`, `code_analyzer`, `doc_writer`, `tests_creator`).
    - `--lang`: Language for the assistant (`ru`, `en`).
    - `--models`: List of models to use (`gemini`, `openai`).
    - `--start_dirs`: List of directories to process.

3. **`main()` function**: This is the main execution block:
    - **Argument Parsing**: It calls `parse_args()` to obtain the command-line arguments.
    - **Settings File Handling**: If a `--settings` option is provided, it loads the configurations from the specified JSON file using `json.load()`.  It verifies the file's existence.
    - **Default Configuration**: If no settings file is given, it creates a `CodeAssistant` object using default parameters (`'en'` for language, `['gemini']` for model). It extracts role, language, models, and starting directories from the parsed arguments, providing fallback values if not provided.
    - **Initialization**: It initializes the models using `assistant.initialize_models()`.
    - **Processing**: It calls `assistant.process_files()` to start the code assistant's processing logic.


Usage example
-------------------------
.. code-block:: bash

    # Run with settings from a JSON file
    python main.py --settings settings.json

    # Run with specified role, language, and models
    python main.py --role doc_writer --lang ru --models gemini openai --start_dirs /path/to/dir1 /path/to/dir2

    # Run with specified role, language, and model, no start dirs
    python main.py --role code_checker --lang en --models gemini


# Example settings.json (replace with actual settings)
.. code-block:: json

    {
        "role": "doc_writer",
        "lang": "en",
        "model": ["gemini", "openai"],
        "start_dirs": ["/path/to/dir1", "/path/to/dir2"]
    }